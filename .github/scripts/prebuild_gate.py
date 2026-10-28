#!/usr/bin/env python3
"""Read-only prebuild checks for changed documentation and repository paths."""

from __future__ import annotations

import os
import re
import subprocess
import sys
import unicodedata
from html import unescape
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


SECRET_PATTERNS = (
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}\b"),
    re.compile(r"\bgithub_pat_[A-Za-z0-9_]{50,}\b"),
    re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{20,}\b"),
)
HUNK = re.compile(r"^@@ -\d+(?:,\d+)? \+(\d+)(?:,(\d+))? @@")
REFERENCE_DEFINITION_START = re.compile(
    r"^(?: {0,3}>[ \t]?)* {0,3}(?:(?:[-+*]|[0-9]{1,9}[.)])[ \t]+)?\["
)
MARKDOWN_AUTOLINK = re.compile(
    r"<(?:[A-Za-z][A-Za-z0-9.+-]{1,31}:[^ \t\r\n<>]*|[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+@[A-Za-z0-9](?:[A-Za-z0-9.-]*[A-Za-z0-9])?)>"
)
HTML_ANCHOR_SUPPRESSED_CONTAINERS = {
    "iframe",
    "noembed",
    "noframes",
    "plaintext",
    "script",
    "style",
    "template",
    "textarea",
    "title",
    "xmp",
}
BLOCK_HTML_START = re.compile(
    r"^ {0,3}(?:<!--|<\?|<!\[CDATA\[|<![A-Z]|</?(?:address|article|aside|base|basefont|blockquote|body|caption|center|col|colgroup|dd|details|dialog|dir|div|dl|dt|fieldset|figcaption|figure|footer|form|frame|frameset|h[1-6]|head|header|hr|html|iframe|legend|li|link|main|menu|menuitem|meta|nav|noframes|ol|optgroup|option|p|param|search|section|summary|table|tbody|td|tfoot|th|thead|title|tr|track|ul)(?:[\t\n\f\r />]|$))",
    re.IGNORECASE,
)
WINDOWS_FORBIDDEN = set('<>:"/\\|?*')
WINDOWS_DEVICE_NAMES = {
    "con", "prn", "aux", "nul", "conin$", "conout$", "clock$",
    *(f"com{digit}" for digit in "123456789¹²³"),
    *(f"lpt{digit}" for digit in "123456789¹²³"),
}
MIN_PYTHON = (3, 9)


def git(*args: str, check: bool = True) -> bytes:
    result = subprocess.run(["git", *args], check=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if check and result.returncode:
        raise RuntimeError(result.stderr.decode("utf-8", "replace").strip() or "git command failed")
    return result.stdout


def changed_files() -> list[str]:
    event = os.environ.get("EVENT_NAME", "")
    base = os.environ.get("BASE_SHA", "")
    head = os.environ.get("HEAD_SHA", "")
    if not head:
        raise RuntimeError("HEAD_SHA is required")

    if event == "pull_request":
        if not base:
            raise RuntimeError("BASE_SHA is required for pull_request")
        output = git("diff", "--name-only", "--diff-filter=ACMRT", "-z", f"{base}...{head}")
    elif event == "push":
        if not base or set(base) == {"0"}:
            output = git("diff-tree", "--root", "-r", "--no-commit-id", "--name-only", "-z", head)
        else:
            output = git("diff", "--name-only", "--diff-filter=ACMRT", "-z", base, head)
    else:
        raise RuntimeError(f"Unsupported event: {event or '(missing)'}")
    return [name.decode("utf-8", "surrogateescape") for name in output.split(b"\0") if name]


def check_path_collisions() -> list[str]:
    paths = git("ls-tree", "-r", "--name-only", "-z", "HEAD").split(b"\0")
    seen: dict[str, str] = {}
    collisions: list[str] = []
    for raw_path in paths:
        if not raw_path:
            continue
        path = raw_path.decode("utf-8", "surrogateescape")
        normalized_parts: list[str] = []
        for part in path.split("/"):
            if any(char in WINDOWS_FORBIDDEN or ord(char) < 32 for char in part):
                collisions.append(f"Windows-incompatible path: {path}")
            normalized_part = part.rstrip(" .")
            if normalized_part != part:
                collisions.append(f"Windows-trimmed path component: {path}")
            if not normalized_part or normalized_part in {".", ".."}:
                collisions.append(f"Windows-incompatible path: {path}")
            device_stem = normalized_part.split(".", 1)[0].rstrip(" .").casefold()
            if device_stem in WINDOWS_DEVICE_NAMES:
                collisions.append(f"Windows-reserved device path: {path}")
            normalized_parts.append(normalized_part.casefold())
        key = "/".join(normalized_parts)
        if key in seen and seen[key] != path:
            collisions.append(f"Windows-normalized path collision: {seen[key]} | {path}")
        else:
            seen[key] = path
    return sorted(set(collisions))


def check_added_lines() -> list[str]:
    event = os.environ["EVENT_NAME"]
    base = os.environ.get("BASE_SHA", "")
    head = os.environ["HEAD_SHA"]
    if event == "pull_request":
        revision = f"{base}...{head}"
        args = ["diff", "--no-ext-diff", "--unified=0", revision, "--"]
    elif base and set(base) != {"0"}:
        args = ["diff", "--no-ext-diff", "--unified=0", base, head, "--"]
    else:
        args = ["diff", "--no-ext-diff", "--unified=0", "--root", head, "--"]
    diff = git(*args).decode("utf-8", "replace").splitlines()
    findings: list[str] = []
    current_file = "(unknown)"
    line_number = 0
    for line in diff:
        if line.startswith("+++ b/"):
            current_file = line[6:]
        elif line.startswith("+++ "):
            current_file = "(unknown)"
        elif line.startswith("@@"):
            match = HUNK.match(line)
            if match:
                line_number = int(match.group(1))
        elif line.startswith("+") and not line.startswith("+++"):
            added = line[1:]
            if any(pattern.search(added) for pattern in SECRET_PATTERNS):
                findings.append(f"Potential credential pattern at {current_file}:{line_number}")
            line_number += 1
        elif line.startswith(" "):
            line_number += 1
    return findings


def strip_blockquote_prefixes(line: str) -> str:
    content = line
    while True:
        quote = re.match(r"^ {0,3}>[ \t]?", content)
        if not quote:
            return content
        content = content[quote.end():]


def is_escaped(text: str, index: int) -> bool:
    backslashes = 0
    cursor = index - 1
    while cursor >= 0 and text[cursor] == "\\":
        backslashes += 1
        cursor -= 1
    return backslashes % 2 == 1


def strip_markdown_container_prefixes(line: str) -> str:
    """Remove blockquote and list markers for block-level syntax checks."""
    content = line
    while True:
        quote = re.match(r"^ {0,3}>[ \t]?", content)
        if quote:
            content = content[quote.end():]
            continue
        list_item = re.match(r"^ {0,3}(?:[-+*]|[0-9]{1,9}[.)])[ \t]+", content)
        if list_item:
            content = content[list_item.end():]
            continue
        return content


def blockquote_depth(line: str) -> int:
    depth = 0
    content = line
    while True:
        quote = re.match(r"^ {0,3}>[ \t]?", content)
        if not quote:
            return depth
        depth += 1
        content = content[quote.end():]


def crosses_markdown_block_boundary(text: str, start: int, closing: int) -> bool:
    opening_line_start = text.rfind("\n", 0, start) + 1
    opening_line_end = text.find("\n", start)
    if opening_line_end < 0:
        return False
    opening_quote_depth = blockquote_depth(text[opening_line_start:opening_line_end])
    between = text[start:closing]
    if re.search(r"\n[ \t]*\n", between):
        return True
    for line in between.split("\n")[1:]:
        if not line.strip() or re.fullmatch(r"\ue100\d+\ue101", line.strip()):
            return True
        quote_content = strip_blockquote_prefixes(line)
        if blockquote_depth(line) > opening_quote_depth:
            return True
        if re.match(r"^ {0,3}(?:[-+*]|[0-9]{1,9}[.)])[ \t]+", quote_content):
            return True
        if re.match(r"^ {0,3}#{1,6}[ \t]+", quote_content):
            return True
        if re.match(r"^ {0,3}(?:=+|-+)[ \t]*$", quote_content):
            return True
        if REFERENCE_DEFINITION_START.match(line) or BLOCK_HTML_START.match(quote_content):
            return True
    return False


def find_code_span_end(text: str, start: int, marker_size: int) -> tuple[int, int] | None:
    search = start + marker_size
    while search < len(text):
        marker_start = text.find("`", search)
        if marker_start < 0:
            return None
        marker_end = marker_start
        while marker_end < len(text) and text[marker_end] == "`":
            marker_end += 1
        if marker_end - marker_start == marker_size:
            if crosses_markdown_block_boundary(text, start, marker_start):
                return None
            return marker_start, marker_end
        search = marker_end
    return None


def is_reference_definition_closer(text: str, closing_bracket: int) -> bool:
    if closing_bracket >= len(text) or text[closing_bracket] != "]":
        return False
    current_start = text.rfind("\n", 0, closing_bracket) + 1
    while current_start >= 0:
        current_end = text.find("\n", current_start)
        if current_end < 0:
            current_end = len(text)
        line = text[current_start:current_end]
        opening = REFERENCE_DEFINITION_START.match(line)
        if opening:
            bracket_start = current_start + opening.end() - 1
            if matching_bracket(text, bracket_start) == closing_bracket:
                return True
        if current_start == 0:
            return False
        previous_end = current_start - 1
        previous_start = text.rfind("\n", 0, previous_end) + 1
        if not text[previous_start:previous_end].strip():
            return False
        current_start = previous_start
    return False


def reference_definition_tail_end(text: str, start: int) -> int | None:
    definition = re.match(r"\][ \t]*:", text[start:])
    if not definition or not is_reference_definition_closer(text, start):
        return None
    line_end = text.find("\n", start)
    if line_end < 0:
        return len(text)
    if text[start + definition.end():line_end].strip():
        return line_end
    next_start = line_end + 1
    if next_start >= len(text):
        return line_end
    next_end = text.find("\n", next_start)
    if next_end < 0:
        next_end = len(text)
    next_line = text[next_start:next_end]
    next_content = strip_markdown_container_prefixes(next_line)
    if re.match(r"^ {0,3}\S.*$", next_content) and not next_line.lstrip().startswith("["):
        return next_end
    return line_end


def transform_inline_code_spans(text: str, *, preserve_code: bool) -> str:
    transformed: list[str] = []
    link_destinations = inline_link_destination_spans(text)
    index = 0
    while index < len(text):
        if text[index] == "]" and not is_escaped(text, index):
            definition_end = reference_definition_tail_end(text, index)
            if definition_end is not None:
                transformed.append(text[index:definition_end])
                index = definition_end
                continue
        if index in link_destinations:
            destination_end = link_destinations[index]
            transformed.append(text[index:destination_end + 1])
            index = destination_end + 1
            continue
        if text[index] == "<":
            autolink_end = markdown_autolink_end(text, index)
            if autolink_end is not None:
                transformed.append(text[index:autolink_end])
                index = autolink_end
                continue
            html_end = html_construct_end(text, index)
            if html_end is not None:
                transformed.append(text[index:html_end])
                index = html_end
                continue
        if text[index] != "`":
            transformed.append(text[index])
            index += 1
            continue
        marker_end = index
        while marker_end < len(text) and text[marker_end] == "`":
            marker_end += 1
        if is_escaped(text, index):
            transformed.append(text[index:marker_end])
            index = marker_end
            continue
        closing = find_code_span_end(text, index, marker_end - index)
        if closing is None:
            transformed.append(text[index:marker_end])
            index = marker_end
            continue
        span_end = closing[1]
        if preserve_code:
            transformed.append(text[index:span_end])
        else:
            transformed.append("".join("\n" if char == "\n" else " " for char in text[index:span_end]))
        index = span_end
    return "".join(transformed)


def protect_inline_code_spans(text: str) -> tuple[str, dict[str, str]]:
    protected: list[str] = []
    code_spans: dict[str, str] = {}
    link_destinations = inline_link_destination_spans(text)
    index = 0
    while index < len(text):
        if index in link_destinations:
            destination_end = link_destinations[index]
            protected.append(text[index:destination_end + 1])
            index = destination_end + 1
            continue
        if text[index] == "<":
            autolink_end = markdown_autolink_end(text, index)
            if autolink_end is not None:
                protected.append(text[index:autolink_end])
                index = autolink_end
                continue
            html_end = html_construct_end(text, index)
            if html_end is not None:
                protected.append(text[index:html_end])
                index = html_end
                continue
        if text[index] != "`":
            protected.append(text[index])
            index += 1
            continue
        marker_end = index
        while marker_end < len(text) and text[marker_end] == "`":
            marker_end += 1
        if is_escaped(text, index):
            protected.append(text[index:marker_end])
            index = marker_end
            continue
        closing = find_code_span_end(text, index, marker_end - index)
        if closing is None:
            protected.append(text[index:marker_end])
            index = marker_end
            continue
        token = f"\ue000{len(code_spans)}\ue001"
        code_spans[token] = text[marker_end:closing[0]].replace("\n", " ")
        protected.append(token)
        index = closing[1]
    return "".join(protected), code_spans


def escape_markdown_html_openers(text: str) -> str:
    escaped: list[str] = []
    for index, char in enumerate(text):
        if char == "<" and (
            is_escaped(text, index) or markdown_autolink_end(text, index) is not None
        ):
            escaped.append("&lt;")
        else:
            escaped.append(char)
    return "".join(escaped)


def strip_html_tags(value: str) -> str:
    visible: list[str] = []
    index = 0
    while index < len(value):
        if value[index] == "<":
            autolink_end = markdown_autolink_end(value, index)
            if autolink_end is not None:
                visible.append(value[index:autolink_end])
                index = autolink_end
                continue
            html_end = html_construct_end(value, index)
            if html_end is not None:
                index = html_end
                continue
        visible.append(value[index])
        index += 1
    return "".join(visible)


def visible_markdown_lines(content: str, *, preserve_inline_code_text: bool = False) -> list[str]:
    """Remove block code and optionally retain inline-code text for heading slugs."""
    visible: list[str] = []
    fence_char = ""
    fence_size = 0
    for line in content.splitlines():
        container_line = strip_markdown_container_prefixes(line)
        if fence_char:
            closing = re.match(
                rf"^ {{0,3}}{re.escape(fence_char)}{{{fence_size},}}[ \t]*$",
                container_line,
            )
            visible.append("")
            if closing:
                fence_char = ""
                fence_size = 0
            continue
        opening = re.match(r"^ {0,3}(`{3,}|~{3,})", container_line)
        if opening:
            marker = opening.group(1)
            fence_char = marker[0]
            fence_size = len(marker)
            visible.append("")
            continue
        if container_line.startswith("    ") or container_line.startswith("\t"):
            visible.append("")
            continue
        visible.append(line)
    if not visible:
        return []
    _, definition_lines = collect_reference_definitions(visible)
    protected_lines = list(visible)
    protected_content: dict[str, str] = {}
    for line_number in sorted(definition_lines):
        token = f"\ue100{len(protected_content)}\ue101"
        protected_content[token] = protected_lines[line_number]
        protected_lines[line_number] = token
    transformed = transform_inline_code_spans(
        "\n".join(protected_lines),
        preserve_code=preserve_inline_code_text,
    )
    for token, line in protected_content.items():
        transformed = transformed.replace(token, line)
    return transformed.split("\n")


def parse_markdown_destination(value: str) -> str | None:
    """Read a CommonMark-style angle or balanced-parenthesis destination."""
    value = value.strip()
    if not value:
        return ""
    if value.startswith("<"):
        end = value.find(">")
        if end < 0:
            return None
        destination = value[1:end]
    else:
        chars: list[str] = []
        depth = 0
        escaped = False
        for char in value:
            if escaped:
                chars.append(char)
                escaped = False
                continue
            if char == "\\":
                escaped = True
                continue
            if char.isspace() and depth == 0:
                break
            if char == "(":
                depth += 1
            elif char == ")":
                if depth == 0:
                    break
                depth -= 1
            chars.append(char)
        if escaped:
            chars.append("\\")
        destination = "".join(chars)
    return unescape(destination).strip()


def markdown_autolink_end(text: str, start: int) -> int | None:
    match = MARKDOWN_AUTOLINK.match(text, start)
    return match.end() if match else None


def html_construct_end(text: str, start: int) -> int | None:
    if markdown_autolink_end(text, start) is not None:
        return None
    if text.startswith("<!--", start):
        end = text.find("-->", start + 4)
        return len(text) if end < 0 else end + 3
    if text.startswith("<![CDATA[", start):
        end = text.find("]]>", start + 9)
        return len(text) if end < 0 else end + 3
    if text.startswith("<?", start):
        end = text.find("?>", start + 2)
        return len(text) if end < 0 else end + 2
    if text.startswith("<!", start):
        tag_end = text.find(">", start + 2)
        return None if tag_end < 0 else tag_end + 1
    if not re.match(r"</?[A-Za-z][A-Za-z0-9:.-]*(?=[\t\n\f\r />])", text[start:]):
        return None

    quote = ""
    for index in range(start + 1, len(text)):
        char = text[index]
        if quote:
            if char == quote:
                quote = ""
        elif char in {"'", '"'}:
            quote = char
        elif char == ">":
            return index + 1
    return None


def matching_bracket(line: str, start: int) -> int | None:
    depth = 0
    index = start
    while index < len(line):
        char = line[index]
        if char == "\\":
            index += 2
            continue
        if char == "<":
            autolink_end = markdown_autolink_end(line, index)
            if autolink_end is not None:
                index = autolink_end
                continue
            html_end = html_construct_end(line, index)
            if html_end is not None:
                index = html_end
                continue
        if char == "[":
            depth += 1
        elif char == "]":
            depth -= 1
            if depth == 0:
                return index
        index += 1
    return None


def matching_parenthesis(line: str, start: int) -> int | None:
    depth = 1
    index = start + 1
    title_quote = ""
    title_paren_depth = 0
    quoted_title_closed = False
    while index < len(line):
        char = line[index]
        if char == "\\":
            index += 2
            continue
        if title_quote:
            if char == title_quote:
                title_quote = ""
                quoted_title_closed = True
            index += 1
            continue
        if title_paren_depth:
            if char == "(":
                title_paren_depth += 1
            elif char == ")":
                title_paren_depth -= 1
            index += 1
            continue
        if quoted_title_closed:
            if char == ")":
                return index
            index += 1
            continue
        if depth == 1 and char.isspace():
            title_start = index
            while title_start < len(line) and line[title_start].isspace():
                title_start += 1
            if title_start < len(line) and line[title_start] in {"'", '"'}:
                title_quote = line[title_start]
                index = title_start + 1
                continue
            if title_start < len(line) and line[title_start] == "(":
                title_paren_depth = 1
                index = title_start + 1
                continue
            index = title_start
            continue
        if char == "(":
            depth += 1
        elif char == ")":
            depth -= 1
            if depth == 0:
                return index
        index += 1
    return None


def inline_link_destination_spans(text: str) -> dict[int, int]:
    destinations: dict[int, int] = {}
    bracket_stack: list[int] = []
    index = 0
    while index < len(text):
        if text[index] == "\\":
            index += 2
            continue
        if text[index] == "<":
            autolink_end = markdown_autolink_end(text, index)
            if autolink_end is not None:
                index = autolink_end
                continue
            html_end = html_construct_end(text, index)
            if html_end is not None:
                index = html_end
                continue
        if text[index] == "`":
            marker_end = index
            while marker_end < len(text) and text[marker_end] == "`":
                marker_end += 1
            if not is_escaped(text, index):
                closing = find_code_span_end(text, index, marker_end - index)
                if closing is not None:
                    index = closing[1]
                    continue
            index = marker_end
            continue
        if text[index] == "[":
            bracket_stack.append(index)
        elif text[index] == "]" and bracket_stack:
            bracket_stack.pop()
            if index + 1 < len(text) and text[index + 1] == "(":
                destination_end = matching_parenthesis(text, index + 1)
                if destination_end is not None:
                    destinations[index] = destination_end
                    index = destination_end + 1
                    continue
        index += 1
    return destinations


def normalize_reference_label(value: str) -> str:
    value = "\n".join(strip_blockquote_prefixes(line) for line in value.split("\n"))
    value = re.sub(r"\\([^\w\s])", r"\1", value)
    return re.sub(r"\s+", " ", value.strip()).casefold()


def is_markdown_link_title(value: str) -> bool:
    value = strip_markdown_container_prefixes(value).strip()
    if len(value) < 2:
        return False
    if value[0] in {"'", '"'}:
        return value[-1] == value[0] and not is_escaped(value, len(value) - 1)
    return value[0] == "(" and matching_parenthesis(value, 0) == len(value) - 1


def collect_reference_definitions(lines: list[str]) -> tuple[dict[str, str | None], set[int]]:
    text = "\n".join(lines)
    offsets: list[int] = []
    offset = 0
    for line in lines:
        offsets.append(offset)
        offset += len(line) + 1

    definitions: dict[str, str | None] = {}
    consumed_lines: set[int] = set()
    for start_line, line in enumerate(lines):
        opening = REFERENCE_DEFINITION_START.match(line)
        if not opening:
            continue
        bracket_start = offsets[start_line] + opening.end() - 1
        bracket_end = matching_bracket(text, bracket_start)
        if bracket_end is None:
            continue
        destination_line = text.count("\n", 0, bracket_end)
        line_end = text.find("\n", bracket_end + 1)
        if line_end < 0:
            line_end = len(text)
        tail = re.match(r"^[ \t]*:(.*)$", text[bracket_end + 1:line_end])
        if not tail:
            continue

        label = normalize_reference_label(text[bracket_start + 1:bracket_end])
        destination_value = tail.group(1)
        consumed_lines.update(range(start_line, destination_line + 1))
        last_consumed_line = destination_line
        if not destination_value.strip() and destination_line + 1 < len(lines):
            next_line = lines[destination_line + 1]
            next_content = strip_markdown_container_prefixes(next_line)
            next_destination = re.match(r"^ {0,3}(\S.*)$", next_content)
            if next_destination and not next_content.lstrip().startswith("["):
                destination_value = next_destination.group(1)
                consumed_lines.add(destination_line + 1)
                last_consumed_line = destination_line + 1
        title_line = last_consumed_line + 1
        if title_line < len(lines) and is_markdown_link_title(lines[title_line]):
            consumed_lines.add(title_line)
        if label and label not in definitions:
            definitions[label] = (
                parse_markdown_destination(destination_value)
                if destination_value.strip()
                else None
            )
    return definitions, consumed_lines


def scan_markdown_links(text: str) -> tuple[list[tuple[str, int]], list[tuple[str, int]]]:
    """Return inline destinations and reference labels with their source lines."""
    targets: list[tuple[str, int]] = []
    references: list[tuple[str, int]] = []
    index = 0
    while index < len(text):
        if text[index] == "\\":
            index += 2
            continue
        if text[index] == "<":
            autolink_end = markdown_autolink_end(text, index)
            if autolink_end is not None:
                index = autolink_end
                continue
        is_image = text[index] == "!" and index + 1 < len(text) and text[index + 1] == "["
        if text[index] != "[" and not is_image:
            index += 1
            continue

        bracket_start = index + 1 if is_image else index
        closing = matching_bracket(text, bracket_start)
        if closing is None:
            index = bracket_start + 1
            continue

        label = text[bracket_start + 1:closing]
        line_number = text.count("\n", 0, bracket_start) + 1
        after_label = closing + 1
        if after_label < len(text) and text[after_label] == "(":
            destination_end = matching_parenthesis(text, after_label)
            if destination_end is not None:
                destination = parse_markdown_destination(text[after_label + 1:destination_end])
                if destination is not None:
                    targets.append((destination, line_number))
                index = destination_end + 1
                continue

        if after_label < len(text) and text[after_label] == "[":
            reference_end = matching_bracket(text, after_label)
            if reference_end is not None:
                explicit_label = text[after_label + 1:reference_end]
                reference = explicit_label or label
                if reference and not reference.lstrip().startswith("^"):
                    references.append((reference, line_number))
                index = reference_end + 1
                continue

        if label and not label.lstrip().startswith("^"):
            references.append((label, line_number))
        index = closing + 1
    return targets, references


def parse_srcset(value: str) -> list[str]:
    """Extract candidate URLs from an HTML srcset attribute."""
    targets: list[str] = []
    index = 0
    while index < len(value):
        while index < len(value) and (value[index].isspace() or value[index] == ","):
            index += 1
        if index >= len(value):
            break
        start = index
        while index < len(value) and not value[index].isspace():
            index += 1
        raw_target = value[start:index]
        target = raw_target.rstrip(",")
        if target:
            targets.append(target)
        if not raw_target.endswith(","):
            while index < len(value) and value[index] != ",":
                index += 1
            if index < len(value):
                index += 1
    return targets


def strip_markdown_links(value: str) -> str:
    """Keep rendered link text while removing inline and reference destinations."""
    visible: list[str] = []
    index = 0
    while index < len(value):
        if value[index] == "\\":
            visible.append(value[index:index + 2])
            index += 2
            continue
        if value[index] == "<":
            autolink_end = markdown_autolink_end(value, index)
            if autolink_end is not None:
                visible.append(value[index:autolink_end])
                index = autolink_end
                continue
        is_image = value[index] == "!" and index + 1 < len(value) and value[index + 1] == "["
        if value[index] != "[" and not is_image:
            visible.append(value[index])
            index += 1
            continue

        bracket_start = index + 1 if is_image else index
        closing = matching_bracket(value, bracket_start)
        if closing is None:
            visible.append(value[index])
            index += 1
            continue
        label = value[bracket_start + 1:closing]
        after_label = closing + 1
        if after_label < len(value) and value[after_label] == "(":
            destination_end = matching_parenthesis(value, after_label)
            if destination_end is not None:
                visible.append(label)
                index = destination_end + 1
                continue
        if after_label < len(value) and value[after_label] == "[":
            reference_end = matching_bracket(value, after_label)
            if reference_end is not None:
                visible.append(label)
                index = reference_end + 1
                continue
        visible.append(value[index])
        index += 1
    return "".join(visible)


def mask_markdown_link_destinations(text: str) -> str:
    ranges: list[tuple[int, int]] = []
    index = 0
    while index < len(text):
        if text[index] == "\\":
            index += 2
            continue
        if text[index] == "<":
            autolink_end = markdown_autolink_end(text, index)
            if autolink_end is not None:
                index = autolink_end
                continue
        if text[index] == "<":
            html_end = html_construct_end(text, index)
            if html_end is not None:
                index = html_end
                continue
        is_image = text[index] == "!" and index + 1 < len(text) and text[index + 1] == "["
        if text[index] != "[" and not is_image:
            index += 1
            continue

        bracket_start = index + 1 if is_image else index
        closing = matching_bracket(text, bracket_start)
        if closing is None:
            index += 1
            continue
        after_label = closing + 1
        if after_label < len(text) and text[after_label] == "(":
            destination_end = matching_parenthesis(text, after_label)
            if destination_end is not None:
                ranges.append((index if is_image else after_label, destination_end + 1))
                index = destination_end + 1 if is_image else index + 1
                continue
        if after_label < len(text) and text[after_label] == "[":
            reference_end = matching_bracket(text, after_label)
            if reference_end is not None:
                ranges.append((index if is_image else after_label, reference_end + 1))
                index = reference_end + 1 if is_image else index + 1
                continue
        if is_image:
            ranges.append((index, after_label))
            index = after_label
            continue
        index += 1

    merged_ranges: list[tuple[int, int]] = []
    for start, end in sorted(ranges):
        if merged_ranges and start <= merged_ranges[-1][1]:
            merged_ranges[-1] = (merged_ranges[-1][0], max(end, merged_ranges[-1][1]))
        else:
            merged_ranges.append((start, end))
    masked_text = list(text)
    for start, end in merged_ranges:
        for position in range(start, end):
            if masked_text[position] != "\n":
                masked_text[position] = " "
    return "".join(masked_text)


def markdown_html_visible_text(lines: list[str]) -> str:
    _, definition_lines = collect_reference_definitions(lines)
    html_lines = list(lines)
    for index in definition_lines:
        html_lines[index] = ""
    text = mask_markdown_link_destinations("\n".join(html_lines))
    return escape_markdown_html_openers(text)


class MarkdownHtmlLinks(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.targets: list[tuple[str, int]] = []
        self.anchors: set[str] = set()
        self.suppressed_containers: list[str] = []

    def in_suppressed_text_container(self) -> bool:
        return bool(self.suppressed_containers) and self.suppressed_containers[-1] != "template"

    def parse_starttag(self, index: int) -> int:
        if not self.in_suppressed_text_container():
            return super().parse_starttag(index)
        # A nested tag name inside RCDATA/RAWTEXT is text; it must not enable
        # HTMLParser's special script/style mode for the surrounding content.
        cdata_content_elements = self.CDATA_CONTENT_ELEMENTS
        self.CDATA_CONTENT_ELEMENTS = ()
        try:
            return super().parse_starttag(index)
        finally:
            self.CDATA_CONTENT_ELEMENTS = cdata_content_elements

    def parse_comment(self, index: int) -> int:
        if self.in_suppressed_text_container():
            return index + 1
        return super().parse_comment(index)

    def parse_html_declaration(self, index: int) -> int:
        if self.in_suppressed_text_container():
            return index + 1
        return super().parse_html_declaration(index)

    def parse_pi(self, index: int) -> int:
        if self.in_suppressed_text_container():
            return index + 1
        return super().parse_pi(index)

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        normalized_tag = tag.casefold()
        if self.suppressed_containers:
            if self.suppressed_containers[-1] == "template" and (
                normalized_tag == "template"
                or normalized_tag in HTML_ANCHOR_SUPPRESSED_CONTAINERS
            ):
                self.suppressed_containers.append(normalized_tag)
            return
        line_number = self.getpos()[0]
        for name, value in attrs:
            if not value:
                continue
            if name.casefold() in {"href", "src", "poster"}:
                self.targets.append((value, line_number))
            elif name.casefold() == "srcset":
                self.targets.extend((target, line_number) for target in parse_srcset(value))
            elif name.casefold() == "id" or (name.casefold() == "name" and normalized_tag == "a"):
                self.anchors.add(value)
        if normalized_tag in HTML_ANCHOR_SUPPRESSED_CONTAINERS:
            self.suppressed_containers.append(normalized_tag)

    def handle_endtag(self, tag: str) -> None:
        if (
            self.suppressed_containers
            and self.suppressed_containers[-1] != "plaintext"
            and tag.casefold() == self.suppressed_containers[-1]
        ):
            self.suppressed_containers.pop()

    handle_startendtag = handle_starttag


def github_heading_slug(value: str) -> str:
    value, code_spans = protect_inline_code_spans(value)
    value = escape_markdown_html_openers(value)
    value = strip_markdown_links(value)
    value = strip_html_tags(value)
    value = unescape(re.sub(r"[`*_~]", "", value)).lower()
    for token, code in code_spans.items():
        value = value.replace(token, code.lower())
    chars: list[str] = []
    for char in value:
        category = unicodedata.category(char)
        if char.isspace():
            chars.append(" ")
        elif category[0] in {"L", "N"} or char == "-":
            chars.append(char)
    return re.sub(r"\s+", "-", "".join(chars)).strip("-")


def markdown_anchors(lines: list[str], html_links: MarkdownHtmlLinks) -> set[str]:
    anchors = set(html_links.anchors)
    heading_anchors: set[str] = set()
    for index, line in enumerate(lines):
        container_line = strip_markdown_container_prefixes(line)
        heading = re.match(r"^ {0,3}#{1,6}[ \t]+(.+?)[ \t]*#*[ \t]*$", container_line)
        if heading:
            heading_text = heading.group(1)
        elif index > 0 and re.match(r"^ {0,3}(?:=+|-+)[ \t]*$", container_line):
            previous_line = strip_markdown_container_prefixes(lines[index - 1])
            if not previous_line.strip():
                continue
            heading_text = previous_line
        else:
            continue
        base = github_heading_slug(heading_text)
        if not base:
            continue
        slug = base
        suffix = 0
        while slug in heading_anchors:
            suffix += 1
            slug = f"{base}-{suffix}"
        heading_anchors.add(slug)
        anchors.add(slug)
    return anchors


def check_markdown_links(files: list[str]) -> list[str]:
    errors: list[str] = []
    repo_root = Path.cwd().resolve()
    anchor_cache: dict[Path, set[str]] = {}

    def anchors_for(path: Path) -> set[str]:
        cached = anchor_cache.get(path)
        if cached is not None:
            return cached
        content = path.read_text(encoding="utf-8", errors="replace")
        if path.suffix.casefold() in {".html", ".htm"}:
            html_links = MarkdownHtmlLinks()
            html_links.feed(content)
            html_links.close()
            anchors = set(html_links.anchors)
        else:
            lines = visible_markdown_lines(content, preserve_inline_code_text=True)
            html_lines = visible_markdown_lines(content)
            html_links = MarkdownHtmlLinks()
            html_links.feed(markdown_html_visible_text(html_lines))
            html_links.close()
            anchors = markdown_anchors(lines, html_links)
        anchor_cache[path] = anchors
        return anchors

    for name in files:
        if Path(name).suffix.casefold() not in {".md", ".markdown"}:
            continue
        source = (repo_root / Path(name)).resolve()
        try:
            source.relative_to(repo_root)
        except ValueError:
            errors.append(f"Markdown source escapes repository at {name}")
            continue
        if not source.is_file():
            continue
        content = source.read_text(encoding="utf-8", errors="replace")
        lines = visible_markdown_lines(content)
        reference_definitions, consumed_definition_lines = collect_reference_definitions(lines)
        html_links = MarkdownHtmlLinks()
        html_links.feed(markdown_html_visible_text(lines))
        html_links.close()
        targets: list[tuple[str, int]] = list(html_links.targets)
        scan_lines = list(lines)
        for index in consumed_definition_lines:
            scan_lines[index] = ""
        inline_targets, references = scan_markdown_links("\n".join(scan_lines))
        targets.extend(inline_targets)
        for reference, line_number in references:
            label = normalize_reference_label(reference)
            if label not in reference_definitions:
                continue
            target = reference_definitions[label]
            if target is None:
                errors.append(f"Invalid relative link at {name}:{line_number}")
            else:
                targets.append((target, line_number))

        heading_lines = visible_markdown_lines(content, preserve_inline_code_text=True)
        anchor_cache[source] = markdown_anchors(heading_lines, html_links)

        for raw_target, line_number in targets:
            try:
                target = urlsplit(raw_target)
            except ValueError:
                errors.append(f"Invalid relative link at {name}:{line_number}")
                continue
            if target.scheme or target.netloc:
                continue
            if not target.path and not target.fragment:
                continue
            decoded_path = unquote(target.path)
            candidate = (repo_root / decoded_path.lstrip("/")) if decoded_path.startswith("/") else (source.parent / decoded_path if decoded_path else source)
            resolved = candidate.resolve()
            try:
                resolved.relative_to(repo_root)
            except ValueError:
                errors.append(f"Relative link escapes repository at {name}:{line_number}")
                continue
            if not resolved.exists():
                errors.append(f"Broken relative link at {name}:{line_number}")
                continue
            if target.fragment and resolved.suffix.casefold() in {".md", ".markdown", ".html", ".htm"} and resolved.is_file():
                fragment = unquote(target.fragment)
                anchors = anchors_for(resolved)
                if fragment.startswith("user-content-") and fragment[13:] in anchors:
                    continue
                if fragment not in anchors:
                    errors.append(f"Broken relative link fragment at {name}:{line_number}")
    return errors


def run_checks() -> int:
    if sys.version_info < MIN_PYTHON:
        raise RuntimeError(f"Python {MIN_PYTHON[0]}.{MIN_PYTHON[1]} or newer is required")
    files = changed_files()
    collisions = check_path_collisions()
    secret_findings = check_added_lines()
    link_errors = check_markdown_links(files)
    problems = [*(f"Case-insensitive path collision: {item}" for item in collisions), *secret_findings, *link_errors]
    if problems:
        print("Prebuild checks failed:")
        for problem in problems:
            print(f"- {problem}")
        return 1
    print(
        f"Prebuild checks passed on Python {sys.version_info.major}.{sys.version_info.minor} "
        f"({len(files)} changed path(s); no credential patterns, relative-link errors, "
        "or Windows path collisions)."
    )
    return 0


if __name__ == "__main__":
    try:
        if len(sys.argv) != 2 or sys.argv[1] != "check":
            raise RuntimeError("Usage: prebuild_gate.py check")
        raise SystemExit(run_checks())
    except (OSError, RuntimeError, subprocess.CalledProcessError) as error:
        print(f"Prebuild check error: {error}", file=sys.stderr)
        raise SystemExit(1)
