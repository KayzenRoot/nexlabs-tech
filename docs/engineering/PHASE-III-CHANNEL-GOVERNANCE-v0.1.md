# NexLabs Technology — Política Documental de Canais v0.1

**Work Order:** NX-P3-D03-13 · **Decisão:** D03-13 C, ratificada em 2026-10-17.
**Status:** APROVADA COMO DIRETRIZ CONCEITUAL L0; especificações, critérios e tecnologias ainda EM ANÁLISE. 
**Autoridade:** Carta Institucional v1.0; D03-11 C (FCR progressivo); D03-12 C (mandatos limitados e revogáveis); [Registro D03 v0.13](PHASE-III-DECISION-REGISTER-v0.13.md).
**Restrição:** Fase III somente documental; proíbe software, dados sintéticos, testes operacionais, autenticação, contas, integrações, infraestrutura, SDKs, agentes, bots, telas e orçamento não aprovado.

## 1. Objetivo e recorte

Uma decisão ou mandato institucional deve significar a mesma coisa qualquer que seja o futuro meio de interação. O FCR, Telegram, voz, notificações e relatórios são **canais candidatos**, e não fontes de autoridade ou sistemas de registro independentes. FCR é a **primeira experiência de supervisão a planejar**, com leitura autorizada, proveniência e estados verificáveis; os demais canais continuam requisitos para fases futuras, não compromissos do MVP.

## 2. Invariantes conceituais

- **CH-I01 Identidade:** atribuir intenção a principal autenticável por meio futuro a especificar; identidade alegada pelo canal não basta para atos reservados.
- **CH-I02 Mandato:** exigência de origem legítima, escopo, finalidade, vigência, risco, limites financeiros/dados e revogabilidade verificáveis. Canal não herda ou eleva competência.
- **CH-I03 Decisões:** separar solicitação, recebimento, validação, autorização, execução, resultado relatado, resultado comprovado, recusa, suspensão e revogação.
- **CH-I04 Temporalidade:** distinguir versão do mandato, última leitura, momento de autorização e eficácia de suspensão/revogação; dados defasados são identificados como tal.
- **CH-I05 Negação por incerteza:** divergência, assinatura/identidade inconclusiva, falta de conectividade, fonte indisponível ou versão conflituosa não se convertem em autorização.
- **CH-I06 Duplicidade e entrega:** comandos potencialmente retransmitidos precisam de identidade, ordem e tratamento de idempotência/replay a definir; confirmação de recebimento nunca equivale a confirmação de efeito.
- **CH-I07 Evidência:** fonte, versão, grau L0..L4, contestação, proteção e limitação acompanham toda alegação de resultado, inclusive em resumo de Chief of Staff.
- **CH-I08 Direitos:** restringir leitura e divulgação segundo autoridade, finalidade, minimização, sensibilidade, direitos de terceiros e retenção; relatório exportado não elimina proteção.
- **CH-I09 Escalada e humano:** decisões reservadas requerem aprovação humana explícita, não consentimento tácito, timeouts ou ação do canal.
- **CH-I10 Observabilidade:** custos, consumo/Jev, finanças e VPS só são conhecidos quando houver fonte legítima e medição verificada; indisponibilidade não é zero.
- **CH-I11 Neutralidade:** sem imposição de Telegram, provedor de identidade, infraestrutura, protocolo, SDK, framework ou tecnologia antes de ADR e gates específicos.
- **CH-I12 Limite da revogação:** revogar permissões futuras não reverte automaticamente efeito já causado; exigir política de consequências e prova.

## 3. Sequência condicional futura (não aprova implementação)

| Etapa candidata | Escopo pretendido | Dependências antes de qualquer execução |
| --- | --- | --- |
| S0 — Planejamento L0 | semântica de autoridade, fontes, riscos, CH-AC e contratos candidatos | aceitação documental e rastreabilidade; fase atual |
| S1 — Primeiro FCR | futura leitura e explicação verificáveis, sem permissão implícita para comandos | Fase IV autorizada, ADRs, privacidade, identidade, dados, gates e testes apropriados |
| S2 — Interações autorizadas | eventuais aprovações, pausas e revogações por humano legítimo | prova de alçada, versão, revogação, confirmação, riscos e efeitos |
| S3 — Outros canais | Telegram bilateral, voz, relatórios/exports em ordem a ratificar | decisão por canal, segurança, consistência, fornecedor, direitos, custo e revisão independente |

As etapas S1..S3 **não foram autorizadas** e não são cronograma, API ou release prometido.

## 4. Matriz de cenários de falha e proteção

| Cenário futuro | Resultado obrigatório no desenho |
| --- | --- |
| Telegram reporta “aprovado” sem fonte legítima | não tratar como autorização; registrar conflito e consultar fonte apropriada |
| Revogação no FCR e comando defasado em outro canal | impedir nova ação baseada em mandato inválido; tratar efeitos em trânsito separadamente |
| Mensagem/comando duplicado ou atrasado | não duplicar ato material; registrar recebimento versus resultado |
| Canal desconectado, tempo inconsistente ou fonte indisponível | estado INCONCLUSIVO/NÃO DISPONÍVEL; sem inferir autorização |
| Resumo de Chief of Staff apresenta missão como concluída | exigir evidência independente, fonte e grau de verificação |
| PDF/exportação com dados protegidos | minimizar, controlar divulgação e retenção, considerando direitos legais |
| Canal tenta contornar teto financeiro ou alçada | negar ação sem mandato e aprovação humana competentes |
| Confirmação recebida após expiração de mandato | verificar validade na etapa apropriada; não validar retroativamente |

## 5. Critérios candidatos CH-AC-01..12 (SEM ACEITE FINAL)

| ID | Exigência futura de prova |
| --- | --- |
| CH-AC-01 | mesma autoridade/mandato reconhecidos em múltiplos meios autorizados |
| CH-AC-02 | identidade e alçada verificadas para atos reservados |
| CH-AC-03 | canal não concede permissão por mera conectividade |
| CH-AC-04 | revogação/expiração impedem autorização indevida baseada em estado antigo |
| CH-AC-05 | ausência de fonte ou divergência gera estado inconclusivo seguro |
| CH-AC-06 | leitura, recebimento, autorização, execução e efeito não se confundem |
| CH-AC-07 | duplicidade, replay, atraso e corrida têm tratamento definido |
| CH-AC-08 | relato versus evidência verificada se mantém em todos os canais |
| CH-AC-09 | dados sensíveis, terceiros, exportação e retenção respeitam direitos |
| CH-AC-10 | custo e latência de canal/identidade/auditoria são comparáveis e atribuíveis quando medidos |
| CH-AC-11 | aprovação e intervenção humana reservadas não são inferidas do silêncio |
| CH-AC-12 | habilitação de cada canal requer autorização própria, segurança e testes proporcionais |

**CH-AC-01..12 ainda são propostas L0, não testes realizados, controles operantes ou DoD atendido.** Exigir revisão de sobreposição com MC-01..14, FCR-AC-01..12, AC-01..20 e CG-01..12 para evitar gates redundantes.

## 6. Impacto nos ADRs convergentes e riscos

- **C-01:** comparar linguagens/stack também pelo custo de manter contratos independentes de canal; não escolher tecnologia.
- **C-02:** avaliar fonte de verdade, consistência temporal e histórico legalmente proporcional, sem impor event sourcing nem banco.
- **C-03:** especificar futuramente contratos para identidade, mandatos, semântica de comandos/confirmações, erros, versões, negação e evidências acessíveis a cada canal.
- **Riscos:** autenticidade fingida, confusão entre recebimento e efeito, autorização defasada, replay, vazamento em relatório e dependência prematura de fornecedor.
- **Privacidade:** repositório público; nunca inserir segredos, documentos financeiros privados, dados pessoais não necessários, tokens ou credenciais.

## 7. DoR, DoD e STOP CONDITION

**DoR DOCUMENTAL proposto:** papéis e direitos identificados; tipos de ação e riscos; matrizes de estado/tempo; fontes legítimas; política de dados; critérios CH-AC sem duplicação; custos e gatilhos de escalada; dependências de ADR e canais delimitadas.

**DoD DOCUMENTAL proposto:** decisão D03-13 rastreável, invariantes e ameaças revisadas, critérios e exceções aceitos, contratos candidatos consistentes com D03-11/12 e Carta, matriz CG atualizada e aceite humano apropriado. Este documento **não basta** para declarar esse DoD atendido.

**STOP:** E3-01..04 EM PLANEJAMENTO; CG-01..12 PENDENTES; ADR-C-01..03 EM ANÁLISE; nenhuma execução/credencial/conta/canal/serviço; **Fase IV NÃO AUTORIZADA**. Próxima decisão proposta D03-14 permanece PENDENTE.
