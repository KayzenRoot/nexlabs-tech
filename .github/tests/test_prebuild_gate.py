from __future__ import annotations

import io
import os
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch


SCRIPT_DIRECTORY = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPT_DIRECTORY))
import prebuild_gate as gate  # noqa: E402


class MarkdownLinkRegressionTests(unittest.TestCase):
    CASES = {
        "multiline reference label": ("""[Foo
  bar]: missing.md

[use][Foo bar]
""", True),
        "spaced nested blockquote reference": (""">  > [Foo
>  >  bar]: missing.md
>  > [Baz][Foo bar]
""", True),
        "quoted bracket in HTML link label": ("""[label <span data-x="]">text](missing.md)
""", True),
        "div name is not an anchor": ("""<div name="ghost"></div>
[bad](#ghost)
""", True),
        "RCDATA textarea content is not an anchor": ("""<textarea>
<a id="ghost"></a>
</textarea>
[bad](#ghost)
""", True),
        "RCDATA title content is not an anchor": ("""<title>
<a id="ghost"></a>
</title>
[bad](#ghost)
""", True),
        "raw text xmp content is not an anchor": ("""<xmp>
<a id="ghost"></a>
</xmp>
[bad](#ghost)
""", True),
        "template content is not an anchor": ("""<template>
<a id="ghost"></a>
</template>
[bad](#ghost)
""", True),
        "textarea element id remains an anchor": ("""<textarea id="real">text</textarea>
[ok](#real)
""", False),
        "script comment closes before following anchor": ("""<script><!--</script>--><a id="after"></a>
[ok](#after)
""", False),
        "script tag inside RCDATA does not hide following anchor": ("""<textarea><script></textarea><a id="after"></a>
[ok](#after)
""", False),
        "comment inside RCDATA does not hide following anchor": ("""<textarea><!--</textarea>--><a id="after"></a>
[ok](#after)
""", False),
        "declaration inside RCDATA does not hide following anchor": ("""<textarea><!DOCTYPE </textarea>><a id="after"></a>
[ok](#after)
""", False),
        "processing instruction inside RCDATA does not hide following anchor": ("""<textarea><?probe </textarea>?><a id="after"></a>
[ok](#after)
""", False),
        "anchor name on a is valid": ("""<a name="named"></a>
[ok](#named)
""", False),
        "custom anchor does not shift heading duplicates": ("""<a id="title"></a>
# Title
# Title
[bad](#title-2)
""", True),
        "heading underscore punctuation is stripped": ("""# a_b
[ok](#ab)
[bad](#a_b)
""", True),
        "autolink text contributes to heading slug": ("""# Guide <https://example.com>
[ok](#guide-httpsexamplecom)
[bad](#guide)
""", True),
        "broken HTML srcset path": ("""<img srcset="missing.png 1x">
""", True),
        "inline image alt does not create anchor": ("""![<a id="ghost">badge</a>](image.png)
[bad](#ghost)
""", True),
        "reference image alt does not create anchor": ("""![<a id="ghost">badge</a>][img]
[img]: image.png
[bad](#ghost)
""", True),
        "image nested in link label does not create anchor": ("""[![<a id="ghost">badge</a>](image.png)](README.md)
[bad](#ghost)
""", True),
        "inline Markdown title HTML is not an anchor": ("""[title](README.md "<span id='ghost'>")
[bad](#ghost)
""", True),
        "reference title HTML is not an anchor": ("""[title]:
  README.md
  "<span id='ghost'>"
[go][title]
[bad](#ghost)
""", True),
        "escaped HTML is not an anchor": (r"""\<a id="ghost"></a>
[bad](#ghost)
""", True),
        "multiline code span does not create anchor": ("""`<a id="ghost">
text`
[bad](#ghost)
""", True),
        "code span stops at blank block boundary": ("""`opening

[bad](missing.md)
closing`
""", True),
        "backticks in inline link destination are literal": ("""[bad](README.md`x`.png)
""", True),
        "backticks in destination do not alter heading slug": ("""# [x](foo`) `bar`
[bad](#xfoo-bar)
""", True),
        "literal bracket-parenthesis does not alter heading slug": ("""# foo ](bar` <a id="ghost"> baz)`
[bad](#foo-bar-baz)
""", True),
        "backticks in reference destination are literal": ("""[bad]: README.md`x`.png

[go][bad]
""", True),
        "blockquote next-line destination resolves": ("""> [existing]:
>   target.md
>
> [go][existing]
""", False),
        "HTML anchor in normal link label remains visible": ("""[<a id="real"></a>](README.md)
[go](#real)
""", False),
        "HTML entity in href resolves after decoding": ("""<a href="target&amp;.md">go</a>
""", False),
        "percent-encoded Unicode path resolves": ("""[ok](caf%C3%A9.md)
""", False),
        "percent-encoded space path resolves": ("""[ok](target%20space.md)
""", False),
        "external URL is ignored": ("""[external](https://example.test/path#not-local)
""", False),
        "encoded traversal is rejected": ("""[bad](%2e%2e/outside.md)
""", True),
        "malformed URL is rejected": ("""[bad](http://[)
""", True),
        "valid unclosed anchor element still checks its target": ("""<a href="missing.md">broken
""", True),
        "unclosed href start tag fails closed": ("""<a href="missing.md"
""", True),
        "nested unclosed href start tag fails closed": ("""<div>
<span><a href="missing.md"
""", True),
        "malformed anchor in code span is ignored": ("""`<a href="missing.md"`
""", False),
        "escaped malformed anchor is ignored": (r"""\<a href="missing.md"
""", False),
        "entity-escaped malformed anchor is ignored": ("""&lt;a href="missing.md"
""", False),
        "malformed anchor in template is ignored": ("""<template><a href="missing.md"
</template>
""", False),
        "malformed anchor in script raw text is ignored": ("""<script><a href="missing.md"
</script>
""", False),
    }

    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory(prefix="prebuild-markdown-")
        self.addCleanup(self.temp_dir.cleanup)
        self.original_cwd = Path.cwd()
        os.chdir(self.temp_dir.name)
        self.addCleanup(os.chdir, self.original_cwd)
        Path("README.md").write_text("# Existing\n", encoding="utf-8")
        Path("target.md").write_text("# Target\n", encoding="utf-8")
        Path("image.png").write_bytes(b"image")
        Path("foo`").write_text("existing path", encoding="utf-8")
        Path("target&.md").write_text("entity target", encoding="utf-8")
        Path("café.md").write_text("unicode target", encoding="utf-8")
        Path("target space.md").write_text("space target", encoding="utf-8")
        Path("outside.md").write_text("outside repo", encoding="utf-8")

    def assert_link_result(self, name: str, content: str, should_fail: bool) -> list[str]:
        Path("case.md").write_text(content, encoding="utf-8")
        errors = gate.check_markdown_links(["case.md"])
        self.assertEqual(bool(errors), should_fail, name)
        return errors

    def test_markdown_link_regressions(self) -> None:
        for name, (content, should_fail) in self.CASES.items():
            with self.subTest(name=name):
                self.assert_link_result(name, content, should_fail)

    def test_html_rcdata_target_fragment_is_rejected(self) -> None:
        Path("ghost.html").write_text(
            '<textarea><a id="ghost"></a></textarea>\n', encoding="utf-8"
        )
        self.assert_link_result("RCDATA fragment", "[bad](ghost.html#ghost)\n", True)

    def test_invalid_utf8_still_fails_closed_for_broken_link(self) -> None:
        Path("case.md").write_bytes(b"# Broken encoding\n[bad](missing.md)\n\xff\n")
        errors = gate.check_markdown_links(["case.md"])
        self.assertTrue(errors, "invalid UTF-8 must not hide a broken link")

    def test_unclosed_html_link_reports_source_line(self) -> None:
        errors = self.assert_link_result(
            "unclosed HTML link", "# heading\n<a href=\"missing.md\"\n", True
        )
        self.assertTrue(any(":2" in error for error in errors), "report the malformed tag line")


class WindowsPathRegressionTests(unittest.TestCase):
    def check_paths(self, *paths: bytes) -> list[str]:
        listing = b"\0".join(paths) + (b"\0" if paths else b"")
        with patch.object(gate, "git", return_value=listing):
            return gate.check_path_collisions()

    def test_reserved_device_names_and_suffixes_are_rejected(self) -> None:
        errors = self.check_paths(b"docs/CON.txt", b"docs/COM1.log", b"docs/NUL ")
        self.assertTrue(any("reserved device" in error for error in errors))

    def test_forbidden_characters_and_trailing_dot_or_space_are_rejected(self) -> None:
        errors = self.check_paths(b"docs/bad:name.md", b"docs/trailing.", b"docs/trailing ")
        self.assertTrue(any("Windows-incompatible" in error for error in errors))
        self.assertTrue(any("Windows-trimmed" in error for error in errors))

    def test_traversal_components_are_rejected(self) -> None:
        errors = self.check_paths(b"../outside.md", b"docs/../../outside.md")
        self.assertTrue(any("Windows-incompatible" in error for error in errors))

    def test_casefold_collisions_are_rejected(self) -> None:
        errors = self.check_paths(b"docs/Readme.md", b"docs/README.MD")
        self.assertTrue(any("normalized path collision" in error for error in errors))

    def test_unicode_and_long_total_paths_are_accepted(self) -> None:
        components = [f"segment-{index}-" + ("é" * 38) for index in range(6)]
        long_path = ("/".join(components) + "/café.md").encode("utf-8")
        self.assertGreater(len(long_path), 260)
        self.assertEqual(self.check_paths("docs/ação.md".encode("utf-8"), long_path), [])

    def test_surrogateescaped_git_path_does_not_crash(self) -> None:
        errors = self.check_paths(b"docs/invalid-\xff-name.md")
        self.assertIsInstance(errors, list)


class GitDiffRegressionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory(prefix="prebuild-git-")
        self.addCleanup(self.temp_dir.cleanup)
        self.repo = Path(self.temp_dir.name)
        original_cwd = Path.cwd()
        self.addCleanup(os.chdir, original_cwd)
        os.chdir(self.repo)
        self.run_git("init", "-q")
        self.run_git("config", "user.name", "Prebuild Gate Tests")
        self.run_git("config", "user.email", "prebuild-tests@example.invalid")

    def run_git(self, *args: str) -> str:
        result = subprocess.run(
            ["git", *args],
            cwd=self.repo,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        return result.stdout.strip()

    def commit_all(self, message: str) -> str:
        self.run_git("add", "-A")
        self.run_git("commit", "-q", "-m", message)
        return self.run_git("rev-parse", "HEAD")

    def changed(self, event: str, base: str, head: str) -> list[str]:
        original_cwd = Path.cwd()
        os.chdir(self.repo)
        try:
            with patch.dict(
                os.environ,
                {"EVENT_NAME": event, "BASE_SHA": base, "HEAD_SHA": head},
                clear=False,
            ):
                return gate.changed_files()
        finally:
            os.chdir(original_cwd)

    def test_root_commit_with_zero_base_lists_added_files(self) -> None:
        self.run_git("checkout", "-qb", "main")
        Path("root.md").write_text("root\n", encoding="utf-8")
        Path("nested").mkdir()
        Path("nested/file.txt").write_text("root\n", encoding="utf-8")
        head = self.commit_all("root")
        changed = self.changed("push", "0" * 40, head)
        self.assertEqual(set(changed), {"root.md", "nested/file.txt"})

    def test_pull_request_uses_triple_dot_merge_base(self) -> None:
        self.run_git("checkout", "-qb", "main")
        Path("base.txt").write_text("initial\n", encoding="utf-8")
        initial = self.commit_all("initial")
        self.run_git("checkout", "-qb", "feature", initial)
        Path("feature.md").write_text("feature\n", encoding="utf-8")
        feature = self.commit_all("feature")
        self.run_git("checkout", "-q", "main")
        Path("base-only.txt").write_text("base\n", encoding="utf-8")
        base = self.commit_all("base advances")
        self.assertEqual(self.changed("pull_request", base, feature), ["feature.md"])

    def test_rename_is_included_and_deletion_is_filtered(self) -> None:
        self.run_git("checkout", "-qb", "main")
        Path("old.md").write_text("same content\n", encoding="utf-8")
        Path("deleted.md").write_text("remove me\n", encoding="utf-8")
        base = self.commit_all("base")
        self.run_git("mv", "old.md", "renamed.md")
        Path("deleted.md").unlink()
        head = self.commit_all("rename and delete")
        changed = self.changed("pull_request", base, head)
        self.assertIn("renamed.md", changed)
        self.assertNotIn("old.md", changed)
        self.assertNotIn("deleted.md", changed)

    def test_push_uses_two_revision_diff(self) -> None:
        self.run_git("checkout", "-qb", "main")
        Path("base.txt").write_text("base\n", encoding="utf-8")
        base = self.commit_all("base")
        Path("push.txt").write_text("push\n", encoding="utf-8")
        head = self.commit_all("push")
        self.assertEqual(self.changed("push", base, head), ["push.txt"])

    def test_empty_revision_range_is_empty(self) -> None:
        self.run_git("checkout", "-qb", "main")
        Path("base.txt").write_text("base\n", encoding="utf-8")
        head = self.commit_all("base")
        self.assertEqual(self.changed("push", head, head), [])

    def test_missing_required_inputs_fail_closed(self) -> None:
        with patch.dict(os.environ, {"EVENT_NAME": "push", "HEAD_SHA": ""}, clear=False):
            with self.assertRaises(RuntimeError):
                gate.changed_files()
        with patch.dict(
            os.environ,
            {"EVENT_NAME": "pull_request", "BASE_SHA": "", "HEAD_SHA": "a" * 40},
            clear=False,
        ):
            with self.assertRaises(RuntimeError):
                gate.changed_files()
        with patch.dict(
            os.environ,
            {"EVENT_NAME": "unknown", "BASE_SHA": "b" * 40, "HEAD_SHA": "a" * 40},
            clear=False,
        ):
            with self.assertRaises(RuntimeError):
                gate.changed_files()


class SecretRedactionRegressionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory(prefix="prebuild-secrets-")
        self.addCleanup(self.temp_dir.cleanup)
        self.repo = Path(self.temp_dir.name)
        original_cwd = Path.cwd()
        self.addCleanup(os.chdir, original_cwd)
        os.chdir(self.repo)
        subprocess.run(["git", "init", "-q"], cwd=self.repo, check=True)
        subprocess.run(["git", "config", "user.name", "Prebuild Gate Tests"], cwd=self.repo, check=True)
        subprocess.run(["git", "config", "user.email", "prebuild-tests@example.invalid"], cwd=self.repo, check=True)

    def git(self, *args: str) -> str:
        result = subprocess.run(
            ["git", *args], cwd=self.repo, check=True,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        return result.stdout.strip()

    def commit_all(self, message: str) -> str:
        self.git("add", "-A")
        self.git("commit", "-q", "-m", message)
        return self.git("rev-parse", "HEAD")

    def test_added_synthetic_secrets_are_reported_without_values(self) -> None:
        self.git("checkout", "-qb", "main")
        unchanged_secret = "ghp_" + ("U" * 36)
        Path("existing.txt").write_text(unchanged_secret + "\n", encoding="utf-8")
        base = self.commit_all("base with unchanged synthetic value")

        synthetic_values = [
            "-----BEGIN " + "PRIVATE KEY-----",
            "AKIA" + ("A" * 16),
            "ghp_" + ("B" * 36),
            "github_pat_" + ("C" * 50),
            "xoxb-" + ("D" * 24),
        ]
        Path("new.txt").write_text("\n".join(synthetic_values) + "\n", encoding="utf-8")
        head = self.commit_all("add synthetic patterns")
        original_cwd = Path.cwd()
        os.chdir(self.repo)
        try:
            with patch.dict(
                os.environ,
                {"EVENT_NAME": "push", "BASE_SHA": base, "HEAD_SHA": head},
                clear=False,
            ):
                findings = gate.check_added_lines()
                output = io.StringIO()
                with redirect_stdout(output):
                    result = gate.run_checks()
        finally:
            os.chdir(original_cwd)

        self.assertEqual(len(findings), len(synthetic_values))
        self.assertTrue(all("new.txt:" in item for item in findings))
        self.assertEqual(result, 1)
        rendered = "\n".join(findings) + output.getvalue()
        for value in synthetic_values + [unchanged_secret]:
            self.assertNotIn(value, rendered, "secret values must never appear in findings or output")

    def test_secret_already_present_in_base_is_not_reported(self) -> None:
        self.git("checkout", "-qb", "main")
        baseline = "AKIA" + ("Z" * 16)
        Path("existing.txt").write_text(baseline + "\n", encoding="utf-8")
        base = self.commit_all("base with existing synthetic value")
        Path("new.txt").write_text("ordinary documentation\n", encoding="utf-8")
        head = self.commit_all("unrelated content")
        original_cwd = Path.cwd()
        os.chdir(self.repo)
        try:
            with patch.dict(
                os.environ,
                {"EVENT_NAME": "push", "BASE_SHA": base, "HEAD_SHA": head},
                clear=False,
            ):
                self.assertEqual(gate.check_added_lines(), [])
        finally:
            os.chdir(original_cwd)


if __name__ == "__main__":
    unittest.main()
