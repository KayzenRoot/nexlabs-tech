# NexLabs Technology — Política Documental de Canais v0.6

**Work Order:** NX-P3-D03-13 · **Decisão:** D03-13 C, ratificada em 2026-10-17.
**Status:** APROVADA COMO DIRETRIZ CONCEITUAL L0; especificações, critérios e tecnologias ainda EM ANÁLISE. 
**Autoridade:** Carta Institucional v1.0; D03-11 C (FCR progressivo); D03-12 C (mandatos limitados e revogáveis); [Registro D03 v0.13](PHASE-III-DECISION-REGISTER-v0.15.md).
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

**STOP:** E3-01..04 EM PLANEJAMENTO; CG-01..12 PENDENTES; ADR-C-01..03 EM ANÁLISE; nenhuma execução/credencial/conta/canal/serviço; **Fase IV NÃO AUTORIZADA**. Próxima decisão proposta D03-14 C APROVADA documentalmente.

## 8. D03-14 C — Identidade e consistência integradas por risco (APROVADA em 2026-10-17)

**Aprovação DOCUMENTAL somente:** a independência dos canais decidida em D03-13 agora deverá ser especificada conjuntamente com identidade/alçada/sessão, confirmação de cada etapa, validade temporal/revogação de mandatos, tratamento de divergências, reconexão, duplicidade e evidência de efeitos. Ver [Política Integrada v0.1](PHASE-III-IDENTITY-CONSISTENCY-v0.5.md).

- Projeções do FCR, Chief of Staff, Telegram, voz e relatórios nunca se tornam fonte autônoma de permissão; um status recebido é diferente de um ato autorizado ou executado.
- A fonte legítima de autoridade, a versão e a validade devem prevalecer sobre mensagens atrasadas ou respostas do canal; conflito/indisponibilidade não significam consentimento.
- Planejar revalidação de identidade e alçada para futuras ações relevantes, bloqueio de atos reservados sem decisão humana e visibilidade controlada dos dados.
- CH-AC-01..12 seguem PROPOSTOS L0, agora ligados conceitualmente a IC-AC-01..12; nenhum teste, controle ou API criado.

**Ativação ainda condicionada:** FCR permanece primeiro canal FUTURO a planejar. Telegram/voz/exportações exigem autorização própria, privacidade, custo, prova e gates. A D03-14 não altera S0–S3 nem fecha E3 ou CG. **Fase IV NÃO AUTORIZADA. D03-15 C APROVADA documentalmente.**

## 9. D03-15 C — Núcleo comum sem apagar requisitos de canal

APROVADA SOMENTE DOCUMENTALMENTE em 2026-10-17 a estratégia KAC compartilhada e especializações SAC-CH-01/SAC-IC-01. Permanecem PROPOSTOS CH-AC-01..12, IC-AC-01..12 e suas provas particulares, principalmente autorização por canal, privacidade, replay, consistência temporal, expiração/revogação e reporte de resultado; nenhuma equivalência automática a critérios de FCR ou AUT.

[Mapa de Aceitação v0.1](PHASE-III-ACCEPTANCE-CORE-v0.1.md) preserva todos os identificadores históricos. O FCR é primeiro canal FUTURO de supervisão a planejar, e Telegram, voz, relatórios são posteriores e dependentes de autorização específica e gates próprios. **D03-16 PENDENTE; E3/CG/ADRs sem aceite; Fase IV NÃO AUTORIZADA**.

## 10. D03-17 C — Estados consistentes nas projeções de canal

Aprovação somente DOCUMENTAL (2026-10-27). SEM-06 da [Política de Contratos v0.1](PHASE-III-SEMANTIC-CONTRACTS-v0.3.md) estabelece como proposta que futuras projeções FCR/Chief of Staff/Telegram/voz/relatórios preservem fonte, direitos, versão, revogação e semântica, sem obter competência nova. SEM-06 não acrescenta canais ao MVP e não ativa serviços.

**Canal ≠ autoridade:** divergência, atraso, replay e identidade inconclusiva não concedem autorização; confirmação de entrega não prova efeito. CH-AC-01..12 permanecem PROPOSTOS L0; cada canal futuro exige nova autorização e gate separado. **ADR-C-03 EM ANÁLISE; CG PENDENTES; E3 EM PLANEJAMENTO; D03-18 C APROVADA documentalmente; Fase IV NÃO AUTORIZADA.**

## 11. D03-18 C — Conflito intercanal como cenário CFX documental

CFX-01/04/11/12/13/14 da [Matriz de Conflitos v0.1](PHASE-III-CONFLICT-RECOVERY-MATRIX-v0.2.md) mantêm canal, sessão e mensagem como meios sem alçada própria. Atrasos, replays, duplicatas, cache, reconexão, conflito de versões e visualização defasada não revogam atos humanos reservados nem conferem novos poderes. FCR primeiro e somente LEITURA futura; Telegram/voz/exportações condicionais a ato humano e gates próprios.

**D03-18 C ratificou apenas o planejamento**, CH-AC/IC-AC/CFX-AC propostos, CG sem aceite, ADRs em análise, E3 em planejamento, D03-19 pendente; Fase IV NÃO AUTORIZADA.

## 12. D03-19 C — Negativos para canal, tempo, direitos e autoridade

[NPV-01/04/11/12/13/14 v0.1](PHASE-III-NEGATIVE-PROOF-CATALOG-v0.1.md) distinguem prova de envio/recebimento, autorização, versão, direitos e efeito. Telegram/voz/relatório são canais futuros CONDICIONAIS e não fazem parte do MVP autorizado por inferência; FCR continua apenas leitura futura. Duplicidade, entrega e status stale não permitem ato reservado ou exposição de terceiros.

**D03-19 C SOMENTE DOCUMENTAL.** CH-AC/IC-AC/NPV-AC ainda PROPOSTOS L0; aceitação por canal, risco e gate próprios. Nenhuma identidade, serviço, canal, conta ou integração; D03-20 PENDENTE, CG/ADR/E3 não aceitos, Fase IV NÃO AUTORIZADA.
