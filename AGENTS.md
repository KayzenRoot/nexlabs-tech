# AGENTS.md — NexLabs Technology (instruções do repositório)

## Estado canônico e intenção

Este repositório guarda a concepção institucional da **NexLabs Technology** e o histórico de decisões de planejamento.

- **Fase I — Concepção empresarial:** ENCERRADA, aprovada pelo fundador em 2026-10-15; [Carta institucional v1.0](docs/institutional/CHARTER-v1.0.md).
- **Fase II — Concepção visual:** EM DISCUSSÃO. **PROIBIDO iniciar software, imagens, protótipos, infraestrutura, agentes, integrações ou produtos** sem nova autorização expressa.
- **Decisões visuais aprovadas:** D02-01 opção C (Organismo Cognitivo Vivo), D02-02 opção C (Constelação Cognitiva Federada).
- **Requisitos desejados pelo fundador:** central com inspeção/controle/intervenção de agentes, observabilidade de tokens/Jev/finanças/VPS, Telegram como comunicação móvel com Chief of Staff e relatórios PDF/planilhas, voz dos agentes. São requisitos conceituais, não recursos existentes.
- **Próxima pergunta A/B/C:** D02-03 — linguagem dos personagens/agentes. Não foi respondida.

## Antes de qualquer resposta de continuidade

Leia, nesta ordem:
1. [Guia de handoff](docs/continuity/CHAT-HANDOFF.md) — último ponto e próxima escolha.
2. [Protocolo de planejamento](docs/continuity/PLANNING-PROTOCOL.md) — como fazer perguntas A/B/C, botão e persistência.
3. [Escopo corrente da Fase II](docs/design/DESIGN-PHASE-SCOPE-v0.2.md).
4. [Registro visual corrente](docs/design/VISUAL-CONCEPT-DECISIONS-v0.2.md).
5. [Carta institucional](docs/institutional/CHARTER-v1.0.md), [decisões institucionais](docs/institutional/DECISION-REGISTER-v1.0.md) e [aprovação formal](docs/institutional/PHASE-I-ACCEPTANCE-v1.0.md).

Não inferir que os arquivos listados foram implementados. Se os documentos receberem versões novas, seguir as referências mais recentes do README/Handoff e preservar versões históricas.

## Como interagir com o fundador

- Português do Brasil.
- Explicar brevemente as implicações da **última escolha já aprovada** e registrar o que foi aprovado.
- Formular **uma** nova decisão de cada vez, alternativas **A/B/C** distintas, recomendação fundamentada e **botão funcional de confirmação**, usando controles selecionáveis quando disponíveis.
- A seleção padrão da recomendação não equivale à aprovação; só a confirmação enviada pelo fundador aprova.
- Atualizar documentos Markdown de decisões e handoff a cada escolha confirmada; registrar o que foi ou não gravado.
- Quando um chat novo disser “veja o repositório e continue”, **não começar do zero** nem repetir a mesma pergunta aprovada; localizar a decisão pendente e continuar.
- Não introduzir novas fases, implementação, cronograma técnico, imagens ou artefatos de produto sem autorização expressa.

## Autoridade e segurança

A Carta v1.0 prevalece sobre decisões de design. O fundador possui a autoridade estratégica humana superior **dentro da lei**, e agentes atuam em mandatos limitados. Desejo de “controle total” implica observabilidade, capacidade de comando e transparência sobre limitações, **não** poder de desconsiderar direitos ou reverter efeitos externos impossíveis de desfazer.

Não inventar dados de VPS, custo de tokens, economia do Jev ou relatórios de produção. Separar estimativas de evidência verificada. Mensageria de bots do Telegram não deve ser tratada como canal fim a fim cifrado para segredos por padrão. A solução de voz “gratuita similar à ElevenLabs” não teve seu nome confirmado e não deve ser escolhida, instalada ou creditada como disponível.

## Mudanças de arquivo

- Manter histórico de versões. Não sobrescrever textos institucionais aprovados para registrar novos requisitos.
- Atualizar `docs/continuity/CHAT-HANDOFF.md` a cada nova decisão para garantir continuidade entre chats.
- Usar commits documentais claros e realizar leituras de verificação quando possível.
- Se não tiver permissão no GitHub, dizer isso claramente; não fingir que o estado remoto foi atualizado.
