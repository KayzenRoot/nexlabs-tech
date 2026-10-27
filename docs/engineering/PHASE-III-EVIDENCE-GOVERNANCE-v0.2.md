# NexLabs Technology — Governança Transversal de Evidências e Aceites v0.2

**Work Order:** NX-P3-D03-20 · **Decisão expressa do fundador:** D03-20 C, 2026-10-27.
**Objeto aprovado:** **MÉTODO DOCUMENTAL L0** de planejar proveniência, segregação de funções, contestação, estados de evidência e decisões de aceite proporcionais ao risco para AUT/MIS/EVD/CST/FCR, com responsáveis e gates independentes.
**Não aprovado:** mecanismos de armazenamento, certificação, APIs, plataformas, pessoas nomeadas, testes, evidências L2–L4, critérios materiais, gestão operacional, custos, automação, Fase IV ou encerramento de gates.
**Autoridades:** [Carta Institucional v1.0](../institutional/CHARTER-v1.0.md), [Registro de Decisões D03 v0.20](PHASE-III-DECISION-REGISTER-v0.21.md), [Catálogo NPV v0.2](PHASE-III-NEGATIVE-PROOF-CATALOG-v0.3.md), [Matriz CFX v0.2](PHASE-III-CONFLICT-RECOVERY-MATRIX-v0.2.md), [Contratos SEM v0.3](PHASE-III-SEMANTIC-CONTRACTS-v0.3.md), [Núcleo KAC/SAC v0.6](PHASE-III-ACCEPTANCE-CORE-v0.7.md).
**Status global:** todos os EGV, GEV-AC e EGV-RV são **PROPOSTOS L0**, NÃO ACEITOS. E3-01..04 EM PLANEJAMENTO e STOP CONDITIONS NÃO ATENDIDAS; CG-01..12 SEM ACEITE FINAL; ADR-C-01..03 EM ANÁLISE; **Fase IV NÃO AUTORIZADA**.

## 1. Separar fatos, prova, revisão e decisão: EGV-GOV (proposta)

| Objeto lógico FUTURO | Significado e limite | Proibição de falso aceite |
| --- | --- | --- |
| Alegação/relato | Mensagem atribuída a fonte e escopo, com versão e finalidade | relatado ≠ ocorrido ≠ autorizado |
| Evidência de suporte | Fonte e método verificáveis, integridade e relação causal delimitadas | um hash/log/review do próprio emissor não comprova efeito externo |
| Contestação/contraprova | Divergência, direito de contestar e necessidade de revisão da origem | corrigir/retificar ≠ apagar indevidamente histórico ou direitos |
| Revisão independente | Análise material proporcional ao risco, distinta de autoria quando necessário | comentário automático ou review do próprio autor não basta |
| Decisão sobre CRITÉRIO | Aceite, rejeição ou não conclusão formal por autoridade competente | critério aceito ≠ gate fechado ≠ Fase IV autorizada |
| Decisão sobre GATE | Veredito CG/FCG/MG específico, com pré-condições, dependências e evidências próprias | gate aceito não decide outros gates nem ratifica tecnologia |
| Ato reservado humano | Fonte de competência e aprovação material separada do canal/assistente | silêncio, sessão, FCR e aprovação documental não autorizam execução |

Esses objetos são **classes conceituais** e não tabelas físicas, estado de CI, workflow instalado, sistema de identidade ou instrumento jurídico já efetivo.

## 2. Funções propostas e separação de alçadas: EGV-ROLE

| Função FUTURA candidata | Produz ou preserva | Pode aconselhar/contestar | Pode aceitar? |
| --- | --- | --- | --- |
| Origem AUT/MIS/EVD/CST/FCR | fatos/alegações de seu domínio com escopo/versão, se autorizados no futuro | sim, dentro do mandato | **não automaticamente**, por produzir a fonte |
| Curadoria EVD | classificação de prova, limites, proveniência e versões | sim, podendo pedir verificação independente | não confere poder humano reservado |
| Gestão de risco e privacidade | análise de direitos, retenção, terceiros e exposição | sim, inclusive levantar STOP e contestar | apenas se legitimamente designada futura e não sob conflito |
| Revisão/assurance independente | análise crítica de suficiência, reprodutibilidade quando autorizada e falsos verdes | sim; exigir contraprova | parecer NÃO é decisão de gate por si |
| Dono funcional do risco | responsabilização pela lacuna, consequência e plano documental | sim | não pode se autoaprovar indiscriminadamente |
| Decisor humano legítimo / fundador quando reservado | alçada de aceite institucional e autorização de atos reservados | ouvir especialistas e registrar divergência | **somente no alcance legal/estatutário/mandato aplicável**, em ato separado |
| Gate owner CG/FCG/MG FUTURO | verificar pacote e evidências por gate próprio | sim | decisão específica apenas quando competente e designado |

**Segregação material ainda pendente:** não há pessoas, funções jurídicas, nomeações, matrizes de conflito de interesse ou contratos de serviço efetivamente aprovados. Um mesmo indivíduo poderia ocupar funções futuras apenas após análise legítima de risco e controles compensatórios; **não presumir independência**. A revisão autoral desta PR não se apresenta como revisão independente.

## 3. Ciclo conceitual de estados de evidência EGV-STATE (sem máquina de estados)

| Estado CANDIDATO | Significado | Próximo passo documental admissível | Inferência PROIBIDA |
| --- | --- | --- | --- |
| PROPOSTA_L0 | texto de requisito, exemplo ou hipótese | levantar fonte, risco, rights/owner e gate | chamar de prova testada |
| FONTE_DECLARADA | fonte foi alegada, não necessariamente verificada | conferir legitimidade/escopo e versões | origem = verdade |
| EVIDENCIA_SUBMETIDA | material futuro recebido sob classificação e cadeia de origem | revisar suficiência, integridade, direitos, independência | material = efeito provado |
| EM_CONTESTACAO | contraprova, direito de retificar ou inconsistência relevante | preservar versões de modo proporcional e iniciar revisão competente | divergência resolvida por silêncio |
| INCONCLUSIVA/INDISPONIVEL | lacuna de fonte, tempo, identidade, causalidade ou direitos | manter STOP e dúvida com indicação clara | autorização, custo zero, sucesso ou reversão |
| REVISAO_DOCUMENTADA | parecer e limitações apresentados pelo revisor legítimo | decisão material por alçada separada | parecer = aceite |
| CRITERIO_ACEITO/REJEITADO | futuro ato explícito competente sobre critério, com fonte e escopo | avaliar gate INDIVIDUAL depois, quando aplicável | critério aceito = CG/ADR aceitos |
| GATE_ACEITO/REJEITADO | futuro ato formal do gate específico, com dependências verificadas | tratar autorização de fase/ato reservado separadamente | gate = Fase IV automaticamente |
| SUPERADA/RETIFICADA/REVOGADA | revisão temporal preservando direitos e efeitos já ocorridos | atualizar projeções e reconsiderar decisão quando competente | reescrever passado, renovar mandato ou apagar prova |

**Estado real no momento:** somente `PROPOSTA_L0` documental para este catálogo, NPV/KAC/SEM/CFX e aceites de engenharia; **nenhuma evidência de teste, pessoa nomeada, aprovação de critério ou gate foi criada**. Os rótulos não são valores de um banco ou protocolo.

## 4. Envelope de proveniência EGV-PROV (somente vocabulário candidato)

Uma ficha documental futura deverá *explicitar*, se aplicável: `claim_ref`, `evidence_ref`, `original_source_claim`, `source_authenticity_status`, `source_time_and_version`, `observation_scope`, `rights_purpose_sensitivity`, `collection_authorization`, `integrity_claim_vs_truth`, `external_effect_limitations`, `cost_unit_and_measurement_class`, `challenge_and_correction_refs`, `reviewer_role_and_independence`, `decision_role_and_scope`, `criterion_id`, `gate_id`, `level_L0_to_L4_with_basis`, `decision_state=PENDENTE`.

A ficha não é formato JSON ou schema, não contém dado pessoal, segredo, token, hash real, resultado de teste, evidência privada, identidade/assentimento ou orçamento concreto. A origem de uma alegação e a origem de seu **efeito externo** podem ser diferentes. Ausência de prova **não prova a ausência de efeito**.

## 5. Matriz integrada por risco: EGV-01..16, rastreio nominal CFX/NPV

| Rastro proposto | Domínio e classe DOCUMENTAL | Alegação contestável / negativo | KAC/SEM/NPV cruzados | Fonte/prova FUTURA, não coletada | Responsabilidades FUNCIONAIS PROPOSTAS | CG(s) independentes, NÃO ACEITOS |
| --- | --- | --- | --- | --- | --- | --- |
| EGV-01 / CFX-01 / NPV-01 | AUT · V-RC | Mandato e identidade legítimos, sem elevação por canal | KAC-01/04; SEM-01/02; NPV-01 | origem de competência, mandato/versão e consulta legítima; recusa como negativo futuro | AUT (custódia); segurança/assurance (revisão independente proposta) | CG-01/07/12 |
| EGV-02 / CFX-02 / NPV-02 | AUT/MIS/EVD · V-RC | Revogação e efeito em trânsito não confundidos | KAC-02/03/05/09; SEM-02/07/08; NPV-02 | linha temporal de elegibilidade/revogação e evidência separada de consequência externa | AUT/MIS (fontes); EVD (prova); autoridade humana para atos reservados | CG-04/07/11 |
| EGV-03 / CFX-03 / NPV-03 | AUT/CST · V-RC | Gasto/ato reservado só por alçada explícita | KAC-01/02/08; SEM-01/02/04; NPV-03 | registro autorizado de limites, competência, finalidade e decisão humana | AUT/CST (origem); finanças/assurance (revisão) | CG-01/07/08/12 |
| EGV-04 / CFX-04 / NPV-04 | AUT/MIS · V-RA | Duplicidade/replay e causa de efeito incerto | KAC-03/05/09; SEM-02/07/08; NPV-04 | evidência de origem/versão/ordem e resultado externo independente, sem prometer idempotência | AUT/MIS (origem); assurance (revisão) | CG-04/06/07/11 |
| EGV-05 / CFX-05 / NPV-05 | MIS/EVD · V-RC | Relato não prova execução bem-sucedida | KAC-05/06; SEM-03; NPV-05 | prova externa verificável apropriada ao risco, distinta de log ou autorrelato | MIS (alegação); EVD (custódia); revisor independente | CG-03/09/10 |
| EGV-06 / CFX-06 / NPV-06 | MIS/EVD/AUT · V-RC | Timeout após possível efeito não permite reenvio presumido | KAC-03/05/09; SEM-02/03/10; NPV-06 | prova de ocorrência/ausência conforme possibilidade de observação; decisão competente antes de reparação | MIS/EVD (fontes); AUT/humano (decisão) | CG-06/07/11 |
| EGV-07 / CFX-07 / NPV-07 | EVD · V-RA | Hash/log não estabelece veracidade externa | KAC-05/06; SEM-03/07/10; NPV-07 | proveniência, integridade, critério do efeito externo e contestação | EVD (curadoria); assurance independente | CG-03/04/09/10 |
| EGV-08 / CFX-08 / NPV-08 | EVD/FCR · V-RA | Correção ou contestação não permanece como projeção definitiva | KAC-06/07/10; SEM-03/05/09; NPV-08 | linha de versões, ressalvas e acesso por direito; prova de atualização futura | EVD/FCR (custódia); privacidade/revisor | CG-04/07/09/10 |
| EGV-09 / CFX-09 / NPV-09 | CST · V-RA | Custo desconhecido não vira zero/economia Jev | KAC-08; SEM-04/10; NPV-09 | origem, período, unidade, classificações e baseline causal legítimo | CST (fonte); finanças (validação independente) | CG-08/09 |
| EGV-10 / CFX-10 / NPV-10 | CST/AUT · V-RC | Limite não comprovado não vira orçamento autorizado | KAC-02/08; SEM-02/04/10; NPV-10 | mandato financeiro, limite/vigência, custo e ato humano competente | CST/AUT (fontes); finanças/fundador (aceite reservado) | CG-01/07/08/12 |
| EGV-11 / CFX-11 / NPV-11 | FCR · V-RA | Fonte obsoleta não vira estado atual certificado | KAC-06/09/10; SEM-05/07/08; NPV-11 | origem/versão/frescor e indicação de incompletude, direitos de leitura | FCR (projeção); donos das fontes (verificação) | CG-02/04/09/10 |
| EGV-12 / CFX-12 / NPV-12 | FCR/CH · V-RC | Consulta/exportação não expõe terceiro sem direito | KAC-04/07/10; SEM-05/06/09; NPV-12 | finalidade, minimização, titularidade, direito e retenção adequada | FCR (projeção); privacidade/autoridade de acesso | CG-07/10/12 |
| EGV-13 / CFX-13 / NPV-13 | FCR/AUT · V-RC | Painel de leitura não autoriza comando | KAC-01/02/10; SEM-01/05/06; NPV-13 | mandato/consentimento humano competente; ausência de alçada de interface | FCR (solicitação); AUT/fundador (decisão reservada) | CG-01/02/07/12 |
| EGV-14 / CFX-14 / NPV-14 | AUT/CH · V-RC | Cache/reconexão não recria autoridade vencida | KAC-03/04/09; SEM-02/06/08; NPV-14 | validade fonte/versionamento, marca temporal e negação de ato | AUT (fonte); segurança/assurance (verificação) | CG-01/04/06/07 |
| EGV-15 / CFX-15 / NPV-15 | AUT/MIS/EVD · V-RC | Recuperação não reativa revogação nem apaga disputa | KAC-03/06/07/11; SEM-02/03/08/09; NPV-15 | história proporcional, efeitos externos, direito de correção e revisão material | AUT/MIS/EVD (fontes); privacidade/revisor independente | CG-04/07/09/11 |
| EGV-16 / CFX-16 / NPV-16 | E3/assurance · V-RA | Critério comum não substitui obrigação especializada ou gate | KAC-11/12; SEM-11/12; NPV-16 | crosswalk de fontes legadas, diferenças de risco e decisões por gate | E3-04/assurance (rastreio); cada autoridade humana de gate | CG-03/09/10/12 |

**Cobertura EGV-01..16 ↔ CFX-01..16 ↔ NPV-01..16 é NOMINAL.** Não comprova equivalência de critério, ausência de lacunas, completude legal, conformidade, segurança, efeito, cobertura de teste ou capacidade operacional. Os 99 IDs históricos AC/MC/FCR-AC/CH-AC/IC-AC/RG/EL/IM continuam intactos como fontes versionadas; uma equivalência semântica material ainda não foi ratificada.

## 6. Contestação, retificação e prova contrária: EGV-CHAL (candidatos)

1. **Quem pode contestar FUTURAMENTE:** titulares/detentores legítimos de direitos quando cabível, dono funcional, revisor independente, autoridade humana competente; a definição real depende de governança e lei.
2. **Hipóteses:** fonte falsa/desatualizada, erro de versão/tempo, efeito em trânsito, alçada/revogação, medição ausente, violação de direito ou evidência contraditória.
3. **Conduta conceitual:** preservar a alegação e sua revisão no limite legítimo de retenção, classificar **EM_CONTESTACAO/INCONCLUSIVA** onde adequado, negar novas ações relevantes sem legitimidade e procurar fonte competente.
4. **Não regressão:** contestação não autentica nem invalida por decreto efeito externo, não autoriza novo gasto, não garante rollback, não elimina direito de retificação ou objeção e não legitima acesso indevido a terceiro.
5. **Desfecho futuro:** aceitar ou rejeitar critério requer prova suficiente, independência proporcional, direitos e decisor competente; um gate poderá permanecer aberto mesmo após aceitar determinado critério.
6. **Reabertura:** nova prova, revogação, incidente relevante ou alteração da fonte poderá requerer nova avaliação e invalidar justificativas obsoletas, sem afirmar um mecanismo existente de revogação de evidência.

## 7. Revisão crítica transversal EGV-RV-01..08, futura

| ID | Pergunta de revisão por risco | Responsável PROPOSTO / gate a não automatizar |
| --- | --- | --- |
| EGV-RV-01 | Quem escreveu o relato também assinou seu efeito ou revisou sem independência? | MIS/EVD/assurance; CG-03/09 |
| EGV-RV-02 | Identidade/sessão/alçada foram confundidas na origem da prova? | AUT/segurança; CG-01/07 |
| EGV-RV-03 | Uma revogação/timeout/replay foi tratada como prova de ausência de consequência? | AUT/MIS/EVD; CG-04/06/11 |
| EGV-RV-04 | Direito de terceiro, finalidade ou retenção legítima foram ignorados pela evidência/contestação? | privacidade + EVD/FCR; CG-04/07/10 |
| EGV-RV-05 | CST não medido virou zero/Jev, ou limite sem fonte foi aprovado? | CST/finanças/AUT; CG-07/08/09 |
| EGV-RV-06 | FCR/canal exibiu dado defasado como atual ou recebeu alçada de execução? | FCR/AUT; CG-02/07/10 |
| EGV-RV-07 | KAC/NPV/CFX/SEM compartilhados apagaram diferenças SAC ou dos 99 IDs legados? | E3-04/assurance + donos de risco; CG-03/09/12 |
| EGV-RV-08 | Um parecer, CI de docs, merge ou decisão de método foi confundido com critério/gate ou Fase IV aprovada? | gate owner competente + fundador; CG-12 |

**EGV-RV são perguntas DOCUMENTAIS CANDIDATAS**, NÃO executadas como testes, due diligence, auditoria legal, revisão de especialista independente ou medição externa.

## 8. Critérios EGV-AC-01..12 (PROPOSTOS, SEM ACEITE)

| ID | Dever material FUTURO a demonstrar antes de aceitação competente |
| --- | --- |
| EGV-AC-01 | proveniência aponta autor, fonte legítima, versão, escopo e validade separados de resultado |
| EGV-AC-02 | agente/fonte de relato não é seu único revisor material em ato de alto risco |
| EGV-AC-03 | decisor de critério e gate está legitimamente designado, com alçada, conflitos e ato separados |
| EGV-AC-04 | prova independente proporcional ao dano demonstra efeito externo quando exigido, sem inventar zero/ausência |
| EGV-AC-05 | contestação, retificação e direitos de terceiros não são anulados por integridade de log |
| EGV-AC-06 | revogação, expiração e tempo da fonte não elevam permissão de novos atos |
| EGV-AC-07 | timeout, replay, duplicação e ação em trânsito são classificados com incerteza e sem retry presumido |
| EGV-AC-08 | custo medido/estimado/indisponível e Jev causal são diferenciados com fonte/unidade válida |
| EGV-AC-09 | FCR/canais conservam alçada de origem, privacidade e defasagem sem inferir comando |
| EGV-AC-10 | grau L0..L4 corresponde à evidência realmente disponível e suas limitações |
| EGV-AC-11 | relações NPV/CFX/SEM/KAC/SAC e 99 históricos não apagam obrigações específicas |
| EGV-AC-12 | critério, gate, ADR, STOP E3 e autorização de Fase IV são aceites distintos, não transitivos |

**Todos EGV-AC são critérios apenas propostos L0**. Não foram executados, testados nem aceitos; nenhum DoR/DoD, CG, FCG/MG ou ADR foi satisfeito com sua redação.

## 9. Plano de decisão e limites de implementação

**DoR de uma futura revisão material, CANDIDATO:** papel de origem, dono do risco, direitos, legitimidade de acesso, versão/tempo, classe de evidência e fonte externa, critérios específicos, independência do revisor, autoridade de aceite e gate individual legitimados. **DoD FUTURO CANDIDATO:** prova suficiente e efetivamente coletada em fase autorizada, contestação e privacidade consideradas, revisão materialmente independente quando exigida, veredito explícito por critério e por gate, sem lacunas críticas não resolvidas. **Nenhum DoD material foi atingido.**

**Gates PENDENTES:** CG-01..12, FCG/MG e STOP CONDITIONS dos E3. **ADRs EM ANÁLISE:** C-01/02/03. **Autorização de Fase IV AUSENTE**, logo não criar software, testes de código, bancos, identidade real, serviços, apps, APIs, agentes, acesso a fontes, automações, notificações ou gastos. A D03-21 C foi posteriormente ratificada SOMENTE COMO MÉTODO DOCUMENTAL L0; CG, evidências e owners continuam não aceitos/não designados.

**STOP CONDITION:** D03-20 C RATIFICADA APENAS COMO MÉTODO DOCUMENTAL L0. EGV-01..16, EGV-AC-01..12, EGV-RV-01..08, responsáveis e estados de evidência seguem **PROPOSTOS L0/NÃO ACEITOS**. E3-01..04 EM PLANEJAMENTO, STOP CONDITIONS NÃO ATENDIDAS; ADR-C-01..03 EM ANÁLISE; CG-01..12 SEM ACEITE FINAL. **Fase IV NÃO AUTORIZADA.**

## 10. D03-21 C — Proveniência por gate pendente, não parecer independente

[Matriz GPR v0.1](PHASE-III-GATE-READINESS-v0.1.md) identifica GPR-01..12 com dependências E3/ADR, prova FUTURA ainda não coletada e decisão humana específica por CG. O método D03-21 C está aprovado como **DOCUMENTAÇÃO L0**; EGV-01..16, EGV-AC-01..12, EGV-RV-01..08 e GPR-AC-01..08 continuam propostas, e uma revisão autoral não equivale a parecer independente.

**Estados distintos:** fonte alegada ≠ prova suficiente ≠ critério aceito ≠ CG aceito ≠ transição. Donos FUNCIONAIS não são pessoas nomeadas. Direito de contestação, retenção proporcional e fontes de efeito/custo permanecem lacunas materiais. **CG-01..12/FCG/MG SEM ACEITE, E3 EM PLANEJAMENTO, ADR-C EM ANÁLISE, D03-22 PENDENTE; Fase IV NÃO AUTORIZADA.**
