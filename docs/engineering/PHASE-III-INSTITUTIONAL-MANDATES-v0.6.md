# NexLabs Technology — Política Documental de Mandatos Institucionais v0.6

**Decisão:** D03-12 C, aprovada em 2026-10-16: mandatos limitados, revogáveis e proporcionais ao risco.
**Natureza:** planejamento documental (L0) somente. Nenhum agente, mandato operacional, permissão, software, API, teste, dado sintético ou integração criado.
**Autoridade:** [Carta Institucional v1.0](../institutional/CHARTER-v1.0.md), [Fase II encerrada](../design/PHASE-II-ACCEPTANCE-v1.0.md), [registro D03 v0.13](PHASE-III-DECISION-REGISTER-v0.17.md), [FCR v0.3](PHASE-III-FOUNDER-COMMAND-CENTER-v0.7.md).
**Relação de governança:** agentes INSTITUCIONAIS seriam responsáveis por missões empresariais futuras; agentes CONSTRUTORES seriam responsáveis por desenvolvimento futuro sob D03-08/09 C. Os regimes não herdam poderes, modelos, orçamentos ou acesso.

## 1. O contrato semântico de um mandato

| Campo conceitual | Requisito | Condição futura de validade |
| --- | --- | --- |
| Emissor e autoridade | identidade e competência humana/organizacional legítimas | mandato emitido por titular competente |
| Responsável e beneficiário | relação e prestação de contas | obrigação identificável, sem personalidade fictícia atribuída ao agente |
| Finalidade e objeto | motivo lícito e verificável | não atuar fora do objetivo |
| Escopo positivo e exclusões | atos, dados, sistemas, terceiros e proibições explícitas | privilégio mínimo, sem ampliação tácita |
| Temporalidade | início, validade, expiração e referências de versão | relógio e atualização confiáveis |
| Risco e reversibilidade | efeitos, terceiros, privacidade, finanças e impacto | critérios e exceções a ratificar |
| Custo e limite | orçamento, unidade, período e quem autoriza | valores ainda NÃO definidos; ausência não é ilimitado |
| Evidência e revisão | fonte, grau L0..L4, contestação e auditoria proporcional | autorrelato não comprova execução |
| Suspensão e revogação | emissor competente, efeito e estados em trânsito | novas ações impedidas após revogação válida |
| Histórico proporcional | versões, correções, retenção, acesso e direitos | preservar integridade sem reter excessivamente |

Os campos são **conceitos**, não tabelas, JSON, tokens, APIs, protocolos, códigos ou permissões efetivas.

## 2. Estados e segurança temporal

**PROPOSTO:** pedido sem poder. **EM ANÁLISE:** avaliação sem autorização. **ATIVO:** só após verificação legítima futura de emissor, escopo e condições. **SUSPENSO:** pausa de novos atos abrangidos, pendente de revisão. **REVOGADO:** mandato não autoriza novas ações, com avaliação de efeitos já produzidos. **EXPIRADO:** validade encerrada, sem renovação tácita. **RECUSADO/INVÁLIDO:** nunca executar. **DESCONHECIDO/CONFLITANTE:** não supor permissão; exigir esclarecimento humano proporcional ao risco.

**Revogação não é retroativa.** O projeto futuro deverá especificar momento de eficácia, tratamento de ações em curso, efeitos externos não reversíveis, correções e evidências de confirmação. Esta fase não promete capacidade de cancelamento em tempo real.

A autorização não pode ser criada pela mera leitura do Founder Command Center, por canal de comunicação, por autorrelato do agente ou por capacidade técnica. Atos constitucional ou legalmente reservados exigem autoridade humana legítima. Nenhum agente amplia ou subdelega sua própria competência sem nova autorização apropriada.

## 3. Casos de aceitação futuros MC-01..MC-14 (somente especificados)

| Caso | Exigência para futura prova, quando execução for autorizada |
| --- | --- |
| MC-01 | pedido sem mandato não inicia ação |
| MC-02 | emissor e titular legitimados, finalidade verificada |
| MC-03 | escopo e atos proibidos respeitados |
| MC-04 | expiração impede renovação implícita |
| MC-05 | suspensão/revogação impedem novos atos cobertos |
| MC-06 | ação em trânsito, consequências e irreversibilidade transparentes |
| MC-07 | versões conflitantes levam a bloqueio ou escalada legítima |
| MC-08 | limites financeiros e consumo com fonte, unidade e teto aprovado |
| MC-09 | ato reservado não é autorizado pelo próprio agente |
| MC-10 | dados e direitos de terceiros tratados licitamente |
| MC-11 | relato e resultado verificado diferenciados por fonte e evidência |
| MC-12 | canais distintos não ampliam poderes por divergência de versões |
| MC-13 | registro e correção com histórico proporcional e privacidade |
| MC-14 | recusa, custo desconhecido e falha comunicados sem êxito fictício |

**MC-01..14 são propostas L0, não testes ou aceites.** Casos negativos incluem replay de mandato, revogação concorrente, perda de competência, fonte indisponível, tempo inconsistente, limite de despesa desconhecido, prova adulterada e acesso indevido.

## 4. Regras para FCR, dados e custos

O FCR futuro deverá mostrar legitimidade, vigência, estado, fonte e incerteza de um mandato, respeitando direitos de leitura; futuras ações humanas de aprovação, pausa ou revogação permanecem **requisitos**, não botões em funcionamento. O Chief of Staff via Telegram bilateral, vozes, PDF/planilhas, tokens/Jev, finanças e VPS permanecem **requisitos do fundador**, sem canais conectados.

Dados reais de terceiros exigirão finalidade, base legítima, minimização, proteção e retenção proporcional. Ausência de gasto não significa gasto zero; economia Jev não é comprovável sem baseline comparável. O custo futuro de controle de mandato inclui autenticação, atualização, revisão, retenção e auditoria, todos SEM MEDIÇÃO.

Os ADRs C-01 (stack), C-02 (persistência) e C-03 (contratos) permanecem EM ANÁLISE. Regras temporais não impõem banco, framework ou event sourcing.

## 5. DoR, DoD e STOP CONDITION

**DoR documental candidato:** atores e competências identificados; escopo/limites; direitos/temporalidade; critérios MC/AC/FCR-AC; dados, finalidade e riscos; orçamento e revisão; revogação e efeitos; fonte e responsável legitimados.

**DoD documental candidato:** casos e campos ratificados por autoridade competente, contratos coerentes AUT/MIS/EVD/CST/FCR, privacidade revisada, evidências e custos claramente classificados, riscos/ausências explícitos. **A presença desta proposta não satisfaz o DoD.**

**D03-12 C APROVADA como princípio apenas.** E3-01..04 EM PLANEJAMENTO e STOP CONDITIONS NÃO ATENDIDAS. CG-01..12 PENDENTES. ADR-C-01..03 EM ANÁLISE. Fase IV NÃO AUTORIZADA.

**D03-13 C APROVADA:** canais institucionais e consistência entre FCR e Chief of Staff, sem integrações agora.

## 6. D03-13 C — Mandato não depende do canal de origem (2026-10-17)

Ratificada a **independência conceitual** da fonte de autoridade perante FCR, Chief of Staff, Telegram, voz e relatórios. Nenhum desses meios pode criar, prorrogar, ampliar, aprovar ou revogar efetivamente um mandato sem verificação legitimada do ato humano correspondente. A ordem temporal, estados, escopo, direitos, proveniência e consequências de revogação são requisitos de consistência entre futuras representações.

**MC-01..14 permanecem PROPOSTOS**, não aceitos. A [Política de Canais v0.1](PHASE-III-CHANNEL-GOVERNANCE-v0.4.md) adiciona CH-AC-01..12 (também PROPOSTOS). Os E3 e CG seguem abertos, ADRs não ratificados, **Fase IV NÃO AUTORIZADA**, próxima D03-14 C APROVADA documentalmente.

## 7. D03-14 C — Legitimidade e revogação por evidência integrada (2026-10-17)

**Diretriz DOCUMENTAL aprovada:** distinguir principal identificado, autenticação futura, alçada legítima, mandato versionado/válido e confirmação de cada etapa, independentemente do canal. Aceitar pedido ou receber uma mensagem não emite mandato nem confirma execução; revogação/suspensão/expiração bloqueiam novas elegibilidades e exigem tratamento independente de efeitos já produzidos.

**Estados CONFLITANTE/INCONCLUSIVO:** versões, relógios, identidade, perda de sessão, replay e ações em trânsito não podem dar permissão por inferência. Risco institucional qualificado por impacto, direitos, reversibilidade e limite financeiro, sem copiar automaticamente R0–R3 dos construtores. A fonte legítima e os deveres humanos são superiores a qualquer canal.

[Política IC v0.1](PHASE-III-IDENTITY-CONSISTENCY-v0.3.md) agrega critérios propostos IC-AC-01..12, sem aceitar MC-01..14 ou criar controles. **E3/CG sem aceite; ADR-C-01..03 EM ANÁLISE; Fase IV NÃO AUTORIZADA; D03-15 C APROVADA documentalmente.**

## 8. D03-15 C — Mandatos no núcleo comum e SAC-AUT (2026-10-17)

A política de racionalização foi APROVADA **somente como método DOCUMENTAL L0**, não como delegação. MC-01..14, IC-AC, CH-AC e demais exigências continuam PROPOSTAS sem redução de autoridade/revogação, legitimidade de emissor, direitos e reserva humana.

- **KAC-01/02/03/04:** autoridade, alçada, limites temporais e identidade separados de conta/canal.
- **KAC-05/09:** pedido, recebimento, autorização, relato, efeito, revogação concorrente e conflito não se confundem.
- **SAC-AUT-01 e SAC-MIS-01:** preservar emissão, delegação e ações em trânsito como especializações quando risco e prova diferirem.
- O mesmo indicador de conformidade não pode comprovar, sem análise, missão autorizada e custo real; consultar [Núcleo v0.1](PHASE-III-ACCEPTANCE-CORE-v0.3.md) para mapa dos MC.

**D03-16 C APROVADA documentalmente.** E3-01..04 EM PLANEJAMENTO; CG-01..12 sem aceite final; ADR-C-01..03 EM ANÁLISE; nenhum mandato real, identidade operacional, credencial, agente ou Fase IV autorizados.

## 9. D03-16 C — AUT/MIS: risco crítico primeiro, com alçada e consequências

A ratificação é apenas **sequenciamento DOCUMENTAL L0**. Para V-01 AUT e V-02 MIS, a [Fatia Vertical v0.1](PHASE-III-RISK-FIRST-VERTICAL-v0.1.md) prioriza autoridade legítima, reserva humana, limites/expiração/revogação, recusa diante de identidade inconclusiva e efeitos em trânsito, antes de conveniências de canal. VSC-01/02/03/07/09 exigem fontes de prova **FUTURAS** e responsáveis funcionais propostos.

MC-01..14, IM-01..10 e KAC/SAC permanecem PROPOSTOS e relacionados; nenhum mandato real, conta, principal, orçamento, aprovador jurídico ou pessoa foi atribuído. A relação AUT/MIS não transfere direitos para FCR/Telegram/voz nem para construtores. **CG-01/04/07/11/12 sem aceite; E3 EM PLANEJAMENTO; ADR-C-01..03 EM ANÁLISE; D03-17 C APROVADA documentalmente; Fase IV NÃO AUTORIZADA.**

## 10. D03-17 C — Contrato SEM-02 de mandato a missão (2026-10-27)

A ratificação autoriza APENAS PLANEJAMENTO DOCUMENTAL: em [SEM-02](PHASE-III-SEMANTIC-CONTRACTS-v0.1.md), AUT transmite a MIS **elegibilidade semântica condicionada** a fonte legítima, versão, vigência, alçada, finalidade, direitos, risco e ausência de revogação. Aceitar um pedido ou mensagem não equivale a emitir mandato, iniciar missão ou comprovar efeito.

**Negativas e exceções:** ato reservado exige aprovação humana explícita; conflitos temporais, sessões vencidas, perda de fonte, revogação concorrente e replay não autorizam novos atos. SEM-ENV e SEM-07/08 são conceitos, não schemas, autenticadores ou algoritmos escolhidos; MC-01..14 e IM-01..10 permanecem PROPOSTOS. **CG-01/04/07/11/12 PENDENTES; E3 EM PLANEJAMENTO; ADRs EM ANÁLISE; Fase IV NÃO AUTORIZADA; D03-18 PENDENTE.**
