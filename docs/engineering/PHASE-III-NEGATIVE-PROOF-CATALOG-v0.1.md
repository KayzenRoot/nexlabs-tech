# NexLabs Technology — Catálogo Integrado de Provas Negativas e Critérios de Aceite por Risco v0.1

**Work Order:** NX-P3-D03-19. **Escolha expressa do fundador:** D03-19 C em **2026-10-27**. **Escopo ratificado:** elaborar catálogo DOCUMENTAL integrado com revisão crítica transversal. **Não ratificado:** critérios em conteúdo material, verificações reais, decisões de gate, controles operacionais ou Fase IV.
**Autoridade:** [Carta Institucional v1.0](../institutional/CHARTER-v1.0.md), [Registro D03 v0.19](PHASE-III-DECISION-REGISTER-v0.19.md), [Matriz CFX v0.2](PHASE-III-CONFLICT-RECOVERY-MATRIX-v0.2.md), [SEM v0.3](PHASE-III-SEMANTIC-CONTRACTS-v0.3.md), [KAC/SAC v0.5](PHASE-III-ACCEPTANCE-CORE-v0.5.md).
**Estado de todo o conteúdo:** **PROPOSTO L0 NÃO ACEITO** (exceto o MÉTODO documental D03-19 C expressamente aprovado). Nenhum caso foi executado, nenhum efeito real foi observado e nenhum resultado técnico ou de conformidade foi certificado.

## 1. Método aprovado e limites de interpretação

Construir **provas negativas** para a fatia AUT/MIS/EVD/CST/FCR: definir, por risco crítico, o que uma solução futura **não poderá afirmar, conceder, executar ou ocultar** sem determinada evidência. Cada linha cruza **CFX/SEM/KAC**, uma **fonte de verdade candidata**, um **artefato de prova FUTURO**, um **dono funcional PROPOSTO**, critério de refutação e **gate independente PENDENTE**. Isso NÃO significa projetar infraestrutura, autenticação, filas, contratos físicos, clientes reais, injeção de falhas, benchmarks ou testes nesta fase.

**Hierarquia preservada:** autoridade humana legítima > alegação de canal; relato ≠ efeito verificado; revogação barra novas elegibilidades, não reverte efeitos já ocorridos; prazo excedido/timeout não demonstra ausência de efeito; custo desconhecido ≠ zero ou economia Jev. Revisão textual ou status GitHub da documentação não comprova qualidade do sistema futuro.

## 2. Matriz NPV-01..16: cobertura nominal de CFX-01..16 (TODOS candidatos)

| Negativo / CFX | Risco · domínio | Contrato SEM | Núcleo KAC/SAC | Comportamento que NÃO se deve inferir | Fonte/prova FUTURA necessária, ainda indisponível | Dono funcional FUTURO proposto | Gates independentes NÃO ACEITOS |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NPV-01 / CFX-01 | V-RC · AUT | SEM-01/02/07 | KAC-01/04; SAC-AUT/IC | Uma sessão/canal sem mandato NÃO pode elevar poderes | fonte do mandato, versão, identidade e competência verificadas; evidência de rejeição futura | AUT + segurança + autoridade humana | CG-01/07/12 |
| NPV-02 / CFX-02 | V-RC · AUT/MIS | SEM-02/07/08 | KAC-02/03/09; SAC-AUT/MIS | Revogação em trânsito NÃO revalida novas ações nem apaga efeitos antigos | linha temporal da revogação, correlação com ato e efeito externo separado | AUT + MIS + EVD + fundador | CG-04/07/11 |
| NPV-03 / CFX-03 | V-RC · AUT/CST | SEM-01/02/04 | KAC-01/02/08; SAC-AUT/CST | Ato reservado ou gasto NÃO é autorizado por silêncio | autorização humana competente, limite material e finalidade | AUT + fundador + finanças | CG-01/07/08/12 |
| NPV-04 / CFX-04 | V-RA · AUT/MIS | SEM-02/07/08 | KAC-03/05/09; SAC-MIS/IC | Replay/duplicação NÃO cria elegibilidade nem ato extra | versões, correlação e fonte do efeito com registros de ordem inconclusiva | AUT + MIS + assurance | CG-04/06/07/11 |
| NPV-05 / CFX-05 | V-RC · MIS/EVD | SEM-03/07 | KAC-05/06; SAC-MIS/EVD | Autorreporte de sucesso NÃO equivale a efeito demonstrado | fonte independente apropriada ao efeito, trilha de contestação | MIS + EVD + revisão independente | CG-03/09/10 |
| NPV-06 / CFX-06 | V-RC · MIS/EVD/AUT | SEM-02/03/08/10 | KAC-03/05/09; SAC-MIS/EVD | Timeout após possível efeito NÃO autoriza reenvio/compensação automática | verificação externa de ocorrência, impacto e decisão competente | MIS + EVD + AUT + humano | CG-06/07/11 |
| NPV-07 / CFX-07 | V-RA · EVD | SEM-03/07/10 | KAC-05/06; SAC-EVD | Hash/log sem fonte independente NÃO prova fato externo | proveniência, integridade versus veracidade e limitação declarada | EVD + assurance | CG-03/04/09/10 |
| NPV-08 / CFX-08 | V-RA · EVD/FCR | SEM-03/05/09 | KAC-06/07/10; SAC-EVD/FCR | Correção/contestação NÃO pode manter projeção antiga como verdade atual | histórico proporcional, versão de correção e sinalização de contestação | EVD + FCR + privacidade | CG-04/07/09/10 |
| NPV-09 / CFX-09 | V-RA · CST | SEM-04/10 | KAC-08; SAC-CST | Ausência de medição NÃO significa zero ou economia Jev | unidade, fonte, período, baseline e classificação de incerteza | CST + finanças | CG-08/09 |
| NPV-10 / CFX-10 | V-RC · CST/AUT | SEM-02/04/10 | KAC-02/08; SAC-CST/AUT | Teto financeiro inválido/indisponível NÃO permite gasto por inferência | fonte e vigência do limite, ato de alçada competente e custo | CST + AUT + fundador | CG-01/07/08/12 |
| NPV-11 / CFX-11 | V-RA · FCR | SEM-05/07/08 | KAC-06/09/10; SAC-FCR | Fonte stale/contraditória NÃO aparece como status atual comprovado | timestamps com limitações, origem e rótulos de defasagem | FCR + donos das fontes | CG-02/04/09/10 |
| NPV-12 / CFX-12 | V-RC · FCR/CH | SEM-05/06/09 | KAC-04/07/10; SAC-FCR/CH | Projeção/exportação NÃO ultrapassa direitos e finalidade | regra de acesso, classificação sensível, titularidade e revisão legítima | FCR + privacidade + AUT | CG-07/10/12 |
| NPV-13 / CFX-13 | V-RC · FCR/AUT | SEM-01/05/06 | KAC-01/02/10; SAC-FCR/AUT | Consulta FCR NÃO converte pedido em comando autorizado | origem do mandato, ausência de delegação, decisão humana explícita | FCR + AUT + fundador | CG-01/02/07/12 |
| NPV-14 / CFX-14 | V-RC · AUT/CH | SEM-02/06/08 | KAC-03/04/09; SAC-IC/CH | Reconexão/cache NÃO restabelece mandato inválido | fonte atual legítima, versão, frescor e recusa segura | AUT + segurança | CG-01/04/06/07 |
| NPV-15 / CFX-15 | V-RC · AUT/MIS/EVD | SEM-02/03/08/09 | KAC-03/06/07/11; SAC-AUT/MIS/EVD | Recuperação NÃO ressuscita revogação nem apaga disputas/efeitos | reconciliação histórica proporcional, impacto, direitos e decisão independente | AUT + MIS + EVD + privacidade | CG-04/07/09/11 |
| NPV-16 / CFX-16 | V-RA · E3/assurance | SEM-11/12 | KAC-11/12; SAC-BLD e especializações | KAC/SEM comum NÃO dispensa SAC, evidência própria ou gate | rastreamento de 99 IDs legados e diferenças semânticas, revisão independente | E3-04 + assurance + donos por domínio | CG-03/09/10/12 |

**Nota de integridade:** cada ID CFX-01..16 tem um NPV correspondente, mas a cobertura 16/16 é **nominal**, não comprova completude, equivalência, legalidade, viabilidade, implementação ou resultado de testes. Alguns riscos se sobrepõem propositalmente; compartilhar artefato não implica compartilhar veredito.

## 3. Critérios candidatos NPV-AC-01..12 (não executados nem aceitos)

| ID | Negativo sob revisão | Requisito de evidência para futura aceitação COMPETENTE |
| --- | --- | --- |
| NPV-AC-01 | A sessão ou canal jamais cria mandato | prova de alçada por fonte legítima e recusa de escalada; AUT/segurança; CG-01/07 |
| NPV-AC-02 | Ato reservado não prossegue sem decisão humana | autorização explícita por finalidade, escopo, instante e competência; AUT/fundador; CG-01/07/12 |
| NPV-AC-03 | Revogação não renova permissão e não reverte efeito externo por suposição | linha temporal e distinção de ações em trânsito; AUT/MIS/EVD; CG-04/07/11 |
| NPV-AC-04 | Duplicação, timeout e replay não implicam ausência de efeito nem reenvio seguro | correlação independente, origem externa e política de decisão proporcional; MIS/EVD; CG-06/09/11 |
| NPV-AC-05 | Relato de agente, log, hash ou check não é prova de efeito externo | evidência independente adequada ao risco e revisão/contestação; EVD; CG-03/09/10 |
| NPV-AC-06 | Fonte EVD contestada não é apresentada como definitiva | integridade e versão, proveniência, direitos, estado INCONCLUSIVO; EVD/privacidade; CG-04/09 |
| NPV-AC-07 | Custo ausente não vira zero; Jev sem baseline não é economia | fonte, unidade, período, medição/estimativa rotuladas; CST/finanças; CG-08/09 |
| NPV-AC-08 | Limite financeiro e responsabilidade não são presumidos | documento de alçada/limite e aceite humano para atos materiais; CST/AUT; CG-07/08/12 |
| NPV-AC-09 | FCR não concede execução e nem exibe estado stale como atual | consulta legitimada, origem e frescor da projeção, ausência de autorização por UI; FCR/AUT; CG-02/07/10 |
| NPV-AC-10 | A recuperação não divulga dados, excede retenção ou ignora retificação | direito de acesso, finalidade e contestação preservados; privacidade/EVD; CG-04/07/10 |
| NPV-AC-11 | Fonte de AUT indisponível não provoca fail-open | negação segura para novos atos relevantes, limites de recuperação e escalada humana; AUT/segurança; CG-01/06/07 |
| NPV-AC-12 | Catálogo, evidência e CI não promovem gate automaticamente | rastreio individual para 99 IDs históricos, CFX/SEM/KAC/SAC, owner e aceite legítimo por CG; E3-04/assurance; CG-03/09/12 |

**NPV-AC-01..12 são propostas de critérios**, não "passed" e não autorizam que um futuro executor produza provas operacionais antes de mandato de fase apropriado. A aprovação D03-19 C recai só sobre a estratégia de documentação.

## 4. Modelo de ficha de prova negativa, NPV-EVD (não registro operacional)

Para futura documentação, cada cenário candidato descreve: `proof_case_id`, `CFX_id`, `SEM_refs`, `KAC/SAC_refs`, `legacy_ids`, `risk_and_rights`, `scope_of_prohibited_claim`, `authoritative_source_candidate`, `source_version_and_time`, `possible_external_effect`, `future_evidence_expected`, `evidence_level_current=L0`, `observability_limitations`, `owner_role_proposed`, `reviewer_independence_needed`, `gate_id`, `criterion_decision=PENDENTE`, `gate_decision=PENDENTE`, `escalation_on_uncertainty`. Não são campos API nem esquema físico.

Uma futura evidência deverá distinguir origem/autoria, integridade de registro, veracidade material, tempo/validade, autorização de acesso, efeito externo e revisão competente. **Nenhum campo se encontra preenchido com dados, usuários, tokens ou valores reais nesta fase.**

## 5. Protocolo de revisão crítica transversal DOCUMENTAL (NPV-RV)

| Revisão independente FUTURA | Pergunta negativa obrigatória | Risco de falso verde |
| --- | --- | --- |
| RV-01 AUT × MIS | Existe caminho de pedido/recebimento/estado stale até permissão sem mandato vigente? | autorização implícita |
| RV-02 MIS × EVD | Um erro/timeout ou mensagem de sucesso é tratado como efeito comprovado ou inexistente? | execução duplicada, dano externo |
| RV-03 MIS × CST | Custo desconhecido, teto ou benefício Jev são assumidos sem fonte? | despesa não autorizada ou economia fictícia |
| RV-04 EVD × FCR | Exposição/relato/estado antigo é representado como fato verificado e acessível a todos? | direito de terceiro comprometido |
| RV-05 FCR × AUT/canais | Aparência de interface ou meio de comunicação aumenta poder? | comando ilegítimo |
| RV-06 AUT/MIS/EVD/CST/FCR × arquitetura | Falha parcial, reconexão, replay e compensação implicam garantia técnica não provada? | rollback inventado |
| RV-07 KAC/SAC/SEM/CFX × legados | Um critério comum faz desaparecer exigência de risco, domínio, canal ou direitos? | obrigação eliminada |
| RV-08 critérios × gates | Revisão do conteúdo foi confundida com aprovação CG/FCG/MG ou autorização Fase IV? | fechamento sem aceitação legítima |

**Independência:** o autor do critério, autor da futura evidência, revisor de conformidade, dono de risco e autoridade de aceite não podem ser tratados como uma única confirmação suficiente quando segregação for necessária. A configuração de equipe/pessoas e seu custo NÃO estão decididos. Uma revisão pelo mesmo assistente é **autoral**, não parecer de avaliador independente.

**Resultado atual do protocolo:** somente estrutura documental L0 proposta; RV-01..08 **NÃO EXECUTADAS COMO TESTES**; revisões substantivas dos riscos/obrigações e legalidade permanecem **PENDENTES**.

## 6. Evidência versus aceite: matriz de estados distintos

| Camada | Estado nesta D03-19 | O que NÃO autoriza |
| --- | --- | --- |
| Direção do fundador D03-19 C | **APROVADA COMO MÉTODO DOCUMENTAL** | desenho concreto, produto, software |
| Catálogo NPV-01..16 | PROPOSTO L0, rastreabilidade nominal | prova de cobertura semântica/exaustividade |
| NPV-AC-01..12, CFX-AC/SEM-AC/KAC/SAC | PROPOSTOS, sem aceite de requisitos | exigir/realizar testes operacionais agora |
| Evidências L1..L4 | NÃO COLETADAS / NOT_RUN | alegar segurança, latência, independência ou efeito |
| Revisão humana/competência legal | PENDENTE, pessoas não nomeadas | delegar alçada, fechar direitos |
| CG-01..12, FCG/MG, STOP E3-01..04 | SEM ACEITE / NÃO ATENDIDAS | transição de fase |
| ADR-C-01..03 | EM ANÁLISE | banco, stack, protocolo, implementação |
| Fase IV | NÃO AUTORIZADA | qualquer código, infraestrutura, bot, API, credencial, teste de sistema, gasto ou deploy |

## 7. Lacunas, DoR/DoD e STOP CONDITION

**DoR para futura revisão MATERIAL (CANDIDATO):** fonte de autoridade legítima identificada, direitos/privacidade avaliados, caso negativo e falha segura descritos, SEM/KAC/SAC/CFX e critérios legados vinculados, dono funcional e revisor competente realmente designados, espécie de prova escolhida e gate indicado.

**DoD de um futuro critério (CANDIDATO e NÃO SATISFEITO):** prova proporcional e independente realmente coletada em fase autorizada, limitações revisadas, aceites individualizados, direitos protegidos, falso verde rejeitado, registro de decisão humana e STOP individual satisfeito quando aplicável. Evidência textual não basta para cumprir isso.

**Pendências:** equivalência semântica dos 99 IDs históricos não demonstrada, fonte/owner concreto não escolhido, critérios negativos sujeitos a revisão legal/segurança, ADRs sem ratificação, custos/Jev não medidos, testes de software não autorizados, nenhuma evidência L2+ coletada. **Nenhum compromisso de teste, execução ou implementação está agendado.**

**STOP CONDITION:** **E3-01..04 EM PLANEJAMENTO; STOP CONDITIONS NÃO ATENDIDAS; ADR-C-01..03 EM ANÁLISE; CG-01..12 SEM ACEITE FINAL; Fase IV NÃO AUTORIZADA.** Próxima **D03-20 A/B/C** permanece SOMENTE PROPOSTA e não pode ser presumida como escolha do fundador.
