# NexLabs Technology — Matriz de Prontidão DOCUMENTAL por Gates CG v0.1

**Work Order:** NX-P3-D03-21 · **Decisão expressa do fundador:** D03-21 C (2026-10-27).
**Escopo ratificado:** apenas MÉTODO DOCUMENTAL L0 para descrever o que ainda falta em **CG-01..12**, relacionando E3-01..04, ADR-C-01..03, fonte/requisito, dono funcional PROPOSTO, prova AUSENTE, decisão humana futura e STOP independente. **Nenhum gate é aprovado ou está pronto** por existência deste documento.
**Autoridades:** [Carta Institucional v1.0](../institutional/CHARTER-v1.0.md), [Registro D03 v0.21](PHASE-III-DECISION-REGISTER-v0.21.md), [Matriz CG anterior v0.11](PHASE-III-CONVERGENCE-READINESS-v0.11.md), [Governança EGV v0.1](PHASE-III-EVIDENCE-GOVERNANCE-v0.1.md), [NPV v0.2](PHASE-III-NEGATIVE-PROOF-CATALOG-v0.2.md), [SEM v0.3](PHASE-III-SEMANTIC-CONTRACTS-v0.3.md), [KAC/SAC v0.6](PHASE-III-ACCEPTANCE-CORE-v0.6.md).
**LIMITE:** Fase III de documentação apenas, **Fase IV NÃO AUTORIZADA**, nenhuma credencial, API, banco, sistema, teste, agente, relatório operacional, custo real, deployment ou canal ativado.

## 1. O que significa prontidão DOCUMENTAL e o que ela NÃO significa

A matriz é um **inventário de lacunas**, não uma avaliação verde. O que está disponível neste momento são artefatos textuais **L0** e referências nominais. Ainda não existem provas operacionais L2–L4, revisão humana técnica/legal independente comprovada, designação de donos materiais, critérios finais aprovados ou decisão efetiva sobre ADRs. Ausência de prova, de contraditório ou de check não equivale a evidência satisfatória.

**Estados não transitivos:**
- D03-21 C **APROVADA SOMENTE COMO MÉTODO** de documentação de lacunas.
- Linhas GPR-01..12, GPR-AC-01..08, responsáveis e fontes são **PROPOSTOS L0**.
- Critério legado/SEM/KAC/CFX/NPV/EGV aceito futuramente **não** fecha CG automaticamente.
- Um CG eventualmente aceito **não** fecha outros gates, STOP E3, ADR-C ou autorização da Fase IV.
- Qualquer decisão de aceitação reservada requer pessoa/alçada competente e evidências próprias, ainda **PENDENTES**.

**Código de lacuna deste catálogo (não estado de software):** `DOC_L0` = origem documental existente; `PROVA_AUSENTE` = prova material futura não coletada; `OWNER_NAO_DESIGNADO` = responsável apenas funcional; `REVISAO_PENDENTE` = juízo legítimo/independente não realizado; `DECISAO_PENDENTE` = ato humano/gate não proferido; `STOP_ATIVO` = nenhuma transição, gasto ou implementação autorizados.

## 2. Inventário CG-01..12: fonte, dono, prova faltante, decisor e STOP

**TODAS as linhas abaixo estão `DOC_L0 + PROVA_AUSENTE + OWNER_NAO_DESIGNADO + REVISAO_PENDENTE + DECISAO_PENDENTE + STOP_ATIVO`.** Menções a E3/ADR são **dependências de análise**, não afirmação de que o pacote aprovou o requisito.

| Gate (SEM ACEITE) | Questão e risco · E3 dependente | Fontes/IDs candidatos | Dependências ADR EM ANÁLISE | Provas NECESSÁRIAS FUTURAS, AUSENTES | Dono FUNCIONAL PROPOSTO, não nomeado | Decisão humana competente FUTURA, não concedida | Regra STOP proposta, sem mecanismo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| GPR-01 / CG-01 | Autoridade e mandato · V-RC; E3-01/04 | AUT, MC/IM, KAC-01/02/04, SEM-01/02, EGV-01/03/14 | C-02/C-03: versão da fonte e significado de alçada | prova de fonte e competência, revogação, limites e titularidade; casos negativos AUT verificados apenas em fase autorizada | AUT + segurança + fundador em decisões reservadas | autoridade humana competente ratifica separadamente escopo, direitos, reservas e evidência | poder alegado por canal, origem indisponível ou mandato inconclusivo: negar novos atos relevantes |
| GPR-02 / CG-02 | Escopo da primeira vertical e FCR somente leitura · V-RA/V-RC; E3-01/04 | MIS/FCR, FCR-AC, CH-AC, KAC-10, SEM-05, EGV-11/13 | C-03: limites de fronteira sem interface física | escopo/atores da vertical, direitos de consulta, demonstração futura de que leitura não é comando; especializações de canais não dispensadas | E3-01 + FCR + AUT + privacidade | fundador/alçada competente ratifica limites e autorizações dos canais individualmente | canal, sessão ou tela insinuando comando: não ampliar MVP nem poder |
| GPR-03 / CG-03 | Critérios, evidências e não regressão · V-RA/V-RC; E3-01/04 | KAC/SAC e 99 IDs AC/MC/FCR-AC/CH-AC/IC-AC/RG/EL/IM, NPV-16, EGV-16 | C-01/C-03: testabilidade e fronteiras sem equivalência presumida | comparação semântica linha a linha, critérios especializados, fontes de prova e aceites individualizados; falta revisão independente | E3-04 + assurance + donos funcionais dos domínios | revisores competentes e decisores de cada critério aprovam somente seu alcance, em atos próprios | mapeamento nominal de IDs não prova suficiência nem permite remover requisito |
| GPR-04 / CG-04 | Fonte de verdade, versões e direitos · V-RC/V-RA; E3-02/04 | AUT/EVD, SEM-07/08/09, CFX-02/08/15, EGV-02/08/15 | C-02: persistência, proveniência, correção e revogação | escolha documentada de políticas legítimas de versão, temporalidade, correção e retenção; fontes/validações reais futuras | E3-02 + AUT + EVD + privacidade | autoridade de dados/privacidade e fundador conforme ato reservado ratificam políticas e direitos | cache, versão conflitante ou retenção indevida: INCONCLUSIVO, sem autorização inferida |
| GPR-05 / CG-05 | Alternativas técnicas e custo de arquitetura · V-RA; E3-02/03/04 | cenários NPV/CFX de falha; custos Jev/CST; exigências de direitos e manutenção | C-01: stack; também depende de C-02/C-03 para comparação | matriz de alternativas comparáveis por TCO, riscos, manutenção, acesso, licença e provas, sem benchmark/gasto atuais | E3-02 + E3-03 + segurança/finanças | fundador e alçadas técnicas/financeiras legitimamente designadas aprovam ADR-C-01 separadamente | nenhuma alternativa/stack escolhida por default ou recomendação textual |
| GPR-06 / CG-06 | Semântica interdomínio e falhas parciais · V-RC/V-RA; E3-01/02/04 | SEM-ENV, SEM-01..12, CFX-04/06/14, NPV-04/06, EGV-04/06 | C-03: contratos e estado; C-02: fontes e recuperação | prova futura de tratamento de replay, timeout, duplicidade, revogação, divergência e consequências externas; desenho físico NÃO escolhido | E3-02 + AUT/MIS/EVD + assurance | responsáveis de fronteira e autoridade legítima aceitam contrato material e ADR-C-03 em decisões separadas | timeout não prova ausência de efeito; evitar retry/rollback presumidos |
| GPR-07 / CG-07 | Reserva humana, riscos e privacidade · V-RC; E3-01/03/04 | AUT/MIS/EVD/FCR, NPV-01/02/03/12/13, EGV-01/02/12/13 | C-01..03 somente quando direitos/controle influenciam opções | análise de direitos, titularidade, alçada, revogação, conflitos de interesse e casos adversos com parecer legal quando aplicável | fundador + AUT + segurança + privacidade | decisores humanos legitimados aceitam riscos residuais e atos reservados em separado, não por delegado automático | direitos inconclusivos, pedido sem mandato, exposição de terceiros: STOP |
| GPR-08 / CG-08 | Custos, limites e Jev · V-RC/V-RA; E3-02/03/04 | CST, KAC-08, SEM-04, NPV-09/10, EGV-09/10 | C-01 custo/TCO, C-02 origem e confiabilidade, C-03 contratos | fontes de consumo/custo com unidade/período, classificação MEDIDO/ESTIMADO/INDISPONIVEL, limite humano autorizado e baseline causal Jev | CST + finanças + AUT + assurance | fundador/autoridade financeira decide orçamento, teto e causalidade em atos independentes | ausência de medição, limite ou alçada não é zero/economia/autorização |
| GPR-09 / CG-09 | Provas negativas e review independente · V-RC/V-RA; E3-01..04 | NPV-01..16, NPV-AC, EGV-AC/RV, CFX-AC, KAC/SAC | C-01 testabilidade, C-03 legibilidade de contratos | critérios materiais aceitos, plano futuro autorizado, evidências independentes proporcionais ao risco, limitações/contestação e conflitos de interesse tratados | E3-04 + assurance independente + donos por risco | autoridade competente julga suficiência de cada critério e gate; não confundir parecer com ato decisório | documento, log, check CI, hash ou autorrelato não prova efeito externo |
| GPR-10 / CG-10 | FCR/canais, direitos e identidade consistente · V-RC/V-RA; E3-01/02/04 | FCR-AC/CH-AC/IC-AC, SEM-05/06/09, NPV-08/11/12/13, EGV-08/11/12 | C-02 origem e correção; C-03 fronteira de apresentação | autorização legítima de leitura, direitos de terceiros, atualização/defasagem, contestação, escopo por canal, identidades | FCR + AUT + privacidade + assurance | alçadas por canal/privacidade e fundador ratificam separadamente quando devido | visualização defasada, acesso indevido ou comando na consulta: negar/exibir incerteza |
| GPR-11 / CG-11 | Efeitos em trânsito e recuperação prudente · V-RC; E3-01/02/04 | MIS/EVD/AUT, SEM-02/03/08/10, CFX-02/04/06/15, EGV-02/06/15 | C-02 continuidade/versionamento; C-03 contratos de efeito e falha | avaliação externa de efeitos, compensabilidade, revogação, reconciliação e direitos; estratégia técnica só após ADR e fase autorizados | MIS + AUT + EVD + privacidade + assurance | autoridade humana legitimada decide risco de recuperação/compensação por efeito específico | não reenviar/compensar sem prova e alçada; revogação não é rollback |
| GPR-12 / CG-12 | Decisão de gates e autorização de transição · V-RC; E3-01..04 | EGV-AC-12, NPV-AC-12, KAC-12, registro D03 e STOP de E3 | C-01..03 ainda EM ANÁLISE | dossiês por CG, responsabilidades efetivas, fonte/evidência real pertinente, aceites E3/ADR por atos separados e autorização humana expressa de fase | fundador + owner futuro de cada gate + assurance independente | fundador decide Fase IV SEPARADAMENTE após requisitos materiais e proteções, nunca por merge documental | qualquer CG/ADR/E3 sem aceite ou falta de autorização de fase: STOP |

**Rastreabilidade:** CG-01..12 (12/12 IDs) cruzados a E3/ADR, mas a associação ainda exige revisão semântica de cada contrato, legislação, direito, owner e gate. A matriz não prova completude de riscos ou equivalência dos 99 identificadores históricos.

## 3. Dependência horizontal dos pacotes E3 e ADRs

| Pacote/decisão material | Estado REAL preservado | Fontes L0 já existentes | Lacuna objetiva e STOP não satisfeito |
| --- | --- | --- | --- |
| **E3-01** escopo/capacidades da vertical | **EM PLANEJAMENTO; STOP NÃO ATENDIDO** | [E3-01 v0.21](E3-01-CAPABILITY-MAP-v0.21.md), NPV/SEM/KAC/CFX/EGV | escopo/donos e critérios materiais AUT/MIS/EVD/CST/FCR ainda não aceitos; CG-01/02/03/04/07/10 não encerrados |
| **E3-02** avaliação de arquitetura e contratos | **EM PLANEJAMENTO; STOP NÃO ATENDIDO** | [E3-02 v0.21](E3-02-ARCHITECTURE-EVALUATION-v0.21.md), pacote ADR-C | comparação formal de alternativas C-01..03 não ratificada, proveniência/recuperação/contratos físicos não decididos; CG-04/05/06/07/08/11 abertos |
| **E3-03** avaliação da fábrica construtora | **EM PLANEJAMENTO; STOP NÃO ATENDIDO** | [E3-03 v0.21](E3-03-AGENT-FACTORY-EVALUATION-v0.21.md), RG/EL | funções independentes, regime de risco distinto e limites/custos/aceites reais ainda não decididos; CG-07/08/09/10/12 abertos |
| **E3-04** assurance e gates | **EM PLANEJAMENTO; STOP NÃO ATENDIDO** | [E3-04 v0.21](E3-04-READINESS-AND-GATES-v0.21.md), NPV/EGV/CG | evidência L2+ não gerada, reviewers/decisores não nomeados, CG/FCG/MG sem aceite; autorização de fase não concedida |
| **ADR-C-01** stack | **EM ANÁLISE** | [Pacote ADR v0.16](PHASE-III-CONVERGENT-ADR-PACK-v0.16.md) | custo/TCO, risco, direitos e opções não comparados/ratificados |
| **ADR-C-02** fonte de verdade | **EM ANÁLISE** | [Pacote ADR v0.16](PHASE-III-CONVERGENT-ADR-PACK-v0.16.md) | política de versão, tempo, correção e retenção sem decisão material |
| **ADR-C-03** contratos | **EM ANÁLISE** | [Pacote ADR v0.16](PHASE-III-CONVERGENT-ADR-PACK-v0.16.md) | fronteiras físicas, duplicação, timeout, idempotência e consequências ainda em comparação documental |

**Esta matriz não define ordem de execução, solução técnica nem novo cronograma.** FCG/MG, stop de cada E3 e direitos mantêm decisões independentes.

## 4. Crosswalk negativo, proveniência e direitos por gate (GPR-EVD)

Para uma decisão FUTURA por gate, exigir um dossiê **conceitual** com: `gate_id`, `criterion_refs`, `legacy_requirement_refs`, `E3_ref`, `ADR_dependency`, `risk_rights_and_scope`, `source_claim`, `source_legitimacy_and_version`, `evidence_expected`, `evidence_current_level=L0`, `material_effect_proof_status=NOT_COLLECTED`, `negative_scenarios`, `owner_function_proposed`, `actual_owner=PENDENTE`, `independent_review=PENDENTE`, `human_decision=PENDENTE`, `STOP_ACTIVE=true`. **Esses nomes são vocabulário L0, não payload/schema/tabela implantada.**

**Evidências inadmissíveis como confirmação exclusiva:** texto do próprio executor, hash/log/CI de documentação, relato de aprovação, mensagem recebida, ausência de erro, ausência de custo, timeout, repetição de execução, merge de PR ou screenshot de FCR. Quando o efeito é externo, requer comprovação material proporcionada ao risco e fonte independente quando cabível. Provas de terceiros e dados pessoais requerem finalidade, minimização, retenção legítima e alçada.

## 5. Checkpoints transversais GPR-AC-01..08 (PROPOSTOS, não gates)

| ID | Critério candidato para revisões FUTURAS | Falha que mantém STOP |
| --- | --- | --- |
| GPR-AC-01 | fonte de mandato/identidade legítima e reserva humana demonstradas | AUT sem autoridade, revogação ou validade claras |
| GPR-AC-02 | decisão individual separa requisito, risco, direito, critério e gate | deduplicação KAC/SAC sem revisão das especializações |
| GPR-AC-03 | versão/proveniência e contestação de EVD preservadas proporcionalmente | correção, falsa evidência de efeito e retenção indevida |
| GPR-AC-04 | custo observado/estimado/indisponível e Jev causal legitimados | custo ausente vira zero, teto de gastos presumido |
| GPR-AC-05 | replay/timeout e consequências externas sob prova proporcional, sem rollback presumido | ato duplicado ou efeito em trânsito não investigado |
| GPR-AC-06 | leitura legítima de FCR/canais preserva origem e não adquire poderes | exposição de terceiro ou comando implícito |
| GPR-AC-07 | donos materiais e revisores independentes realmente designados e sem conflito indevido | parecer autoral ou ferramenta declara aceite próprio |
| GPR-AC-08 | CG-01..12, E3-01..04, ADR-C-01..03, FCG/MG e transição de fase aceitos cada qual por ato legítimo | merge/documento/progresso transforma-se em falsa aprovação |

**GPR-AC são itens de PLANEJAMENTO L0.** O valor de revisão da PR GitHub não se confunde com prova material; nenhum teste, read-back de sistema real, assinatura de autoridade de gate ou aceite operacional foi gerado.

## 6. Regras de decisão humana e de STOP

1. **Fonte:** cada afirmação de aptidão material tem que apontar origem legítima, versão/tempo e prova admissível, com direitos/retificação. Fontes FUTURAS permanecem `NÃO DISPONÍVEIS` neste documento.
2. **Responsáveis:** papel funcional PROPOSTO ≠ pessoa designada, competência legal ou mandato conferido. Revisor crítico do autor não é automaticamente independente.
3. **Decisão:** um gate específico só muda de estado mediante revisão competente, evidência realmente suficiente, aceitação explícita individual e read-back autorizado; esta D03 **não propõe executar esse ato**.
4. **Divergência/indisponibilidade:** `INCONCLUSIVO` não vira sucesso ou autorização por falta de dado. Efeito em trânsito pode existir após timeout, e revogação não o desfaz retroativamente.
5. **STOP:** nenhum novo serviço, código, API, autenticação, ferramenta, bot, agente, identidade real, canal, workflow, teste de software, gasto, contrato técnico ou deploy sem autorização de fase separada e requisitos aplicáveis.
6. **Próximo checkpoint:** D03-22 A/B/C é somente proposta de aprofundamento DOCUMENTAL, sem escolha presumida.

## 7. Veredito documental atual

**D03-21 C APROVADA APENAS COMO ESTRATÉGIA DOCUMENTAL L0.** As 12 linhas CG e oito GPR-AC são estruturas CANDIDATAS de identificação de lacunas. **Todos CG-01..12 SEM ACEITE FINAL; todos E3-01..04 EM PLANEJAMENTO e STOP CONDITIONS NÃO ATENDIDAS; ADR-C-01..03 EM ANÁLISE; FCG/MG NÃO ACEITOS; critérios AC/MC/KAC/SAC/SEM/NPV/CFX/EGV/GPR não aceitos**. Evidência técnica/independente e pessoas legitimamente designadas não foram criadas. **Fase IV NÃO AUTORIZADA.**
