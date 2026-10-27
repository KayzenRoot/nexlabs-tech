# NexLabs Technology — Matriz Integrada de Conflitos, Recuperação e Contingência v0.2

**Work Order:** NX-P3-D03-18. **Decisão expressa do fundador:** D03-18 C, 2026-10-27.
**Status:** DIREÇÃO DOCUMENTAL L0 **APROVADA** para estudar conjuntamente AUT/MIS/EVD/CST/FCR; regras concretas, critérios, classificações, owners e estratégias abaixo são **CANDIDATOS NÃO ACEITOS**, não implementações, procedimentos de incidente em produção ou garantias de recuperação.
**Autoridades:** [Carta Institucional v1.0](../institutional/CHARTER-v1.0.md), [Registro D03 v0.18](PHASE-III-DECISION-REGISTER-v0.19.md), [Contratos Semânticos v0.2](PHASE-III-SEMANTIC-CONTRACTS-v0.3.md), [Núcleo de Aceitação v0.4](PHASE-III-ACCEPTANCE-CORE-v0.5.md) e [Fatia Vertical por Risco v0.1](PHASE-III-RISK-FIRST-VERTICAL-v0.1.md).
**STOP GLOBAL:** Fase III exclusivamente DOCUMENTAL; E3-01..04 EM PLANEJAMENTO, STOP CONDITIONS NÃO ATENDIDAS; CG-01..12 SEM ACEITE FINAL; ADR-C-01..03 EM ANÁLISE; Fase IV NÃO AUTORIZADA. Nenhum código, agente, identidade digital, serviço, credencial, API, teste operacional, banco ou orçamento criado.

## 1. Escolha estratégica ratificada e escopo conceitual

A D03-18 C exige **UMA MATRIZ DOCUMENTAL INTEGRADA** para conflito de autoridade, mensagens/versões divergentes, efeitos em trânsito, perda de fonte, evidência contestada, custo desconhecido e projeção FCR inadequada. Cada cenário deve explicitar: **fonte**, **classe de risco**, **efeito potencial**, **regra segura futura**, **evidência necessária**, **responsável funcional candidato**, **gate de aceite independente**, **lacuna/contingência** e **estado L0**.

Não converter a aprovação do método em ratificação de idempotência, garantias de entrega, rollback, políticas de retenção, algoritmos de conflito, design operacional de pausa, esquema, comunicação de emergência, SLA, equipe designada ou aceitação de critérios. O fundador reserva decisões materiais conforme risco e lei. Projeções FCR e canais futuros não elevam direitos nem geram confirmação de efeitos.

## 2. Prioridade por risco e semântica de reação CANDIDATAS

| Classe DOCUMENTAL | Impacto priorizado na análise, sem probabilidade presumida | Orientação conceitual segura |
| --- | --- | --- |
| V-RC | alçada ilegítima, ato humano reservado, revogação, terceiro prejudicado, segredo divulgado, efeito falso | **NÃO AUTORIZAR novos atos** sem fonte legítima e decisão humana quando reservada; preservar trilha mínima e escalar |
| V-RA | atraso, replay/duplicidade, versões conflitantes, custo fora de limite ou desconhecido, evidência contestada | reconhecer INCERTEZA, verificar fonte/versão e limitar novas elegibilidades relevantes |
| V-RM | inconsistência de leitura, documentação incompleta, correção legitimamente possível | indicar defasagem e tratamento proporcional de correção |
| V-RB | conveniências de exibição e relatórios adicionais | não priorizar sobre direitos/controles; manter como backlog documental |

**Escala V-RC..V-RB não é a escala R0–R3 dos agentes construtores, nem risco legal medido ou gatilho implementado.** Se um caso atravessar múltiplos domínios, usar o maior impacto plausível até revisão competente; essa é regra de **triagem proposta**, não cálculo de probabilidade.

## 3. Matriz única de cenários negativos CFX-01..16, TODOS PROPOSTOS L0

| ID / fronteira | Falha e risco | Fonte candidata e efeito externo incerto | Resposta segura CONCEITUAL / contingência | Prova FUTURA e owner FUNCIONAL PROPOSTO | Gate próprio, NÃO ACEITO |
| --- | --- | --- | --- | --- | --- |
| CFX-01 AUT | principal/sessão/canal alega poder sem mandato, V-RC | cadastro legítimo de competências/mandatos indisponível; nenhum poder presumido | negar novos atos relevantes; consulta a autoridade humana competente | fonte e versão do mandato; AUT + fundador + segurança | CG-01/07/12 |
| CFX-02 AUT↔MIS | revogação/suspensão no intervalo entre elegibilidade e ato, V-RC | fonte AUT/temporalidade; ato em trânsito pode ter efeito parcial irreversível | suspender novas elegibilidades; identificar atos já aceitos e efeitos potencialmente ocorridos; escalar sem prometer rollback | versão de revogação, correlação de missão, fontes de efeito; AUT/MIS/EVD + humano | CG-04/07/11 |
| CFX-03 AUT | ato reservado ou gasto sem aprovação humana apropriada, V-RC | fonte de decisão, alçada e limite; custo/efeito não conhecido | manter PROPOSTO/RECUSADO, nunca aprovar por silêncio ou canal | decisão humana competente e limite antes do ato; fundador/AUT/CST | CG-01/07/08/12 |
| CFX-04 AUT↔MIS | replay/duplicidade ou mensagem fora de ordem, V-RA | referência de intenção, versões e estados; execução duplicada possível | não presumir idempotência; bloquear reautorização não comprovada, classificar CONFLITANTE | correlação/tempo/fonte e reconciliação futura; AUT/MIS + assurance | CG-04/06/07/11 |
| CFX-05 MIS↔EVD | executor declara conclusão sem prova independente, V-RC | relato, prova EVD ausente/contestada; efeito fora do sistema é incerto | manter EXECUCAO_RELATADA/NÃO_VERIFICADO, nunca concluir ou pagar por inferência | evidência do efeito com fonte e nível adequado, revisão independente; MIS/EVD | CG-03/09/10 |
| CFX-06 MIS | falha/timeout após potencial efeito externo, V-RC | fonte externa indisponível; não se sabe se repetição duplicará consequência | não repetir ato automaticamente; registrar INCONCLUSIVO e revisão legitimada | prova externa de ocorrência/compensabilidade; MIS/AUT/EVD + humano | CG-06/07/11 |
| CFX-07 EVD | fonte de evidência indisponível ou hash/log apresentado como prova suficiente, V-RA | prova com origem/versão desconhecida; status não verificável | exibir NÃO_VERIFICADO e limites da prova, preservar contestação | origem, integridade de registro ≠ veracidade externa; EVD/assurance | CG-03/04/09/10 |
| CFX-08 EVD↔FCR | evidência corrigida/contestada após visualização anterior, V-RA | versões e revisão, risco de informação obsoleta | manter histórico proporcional e sinalizar substituição/discordância | origem, razão de correção, acesso legítimo; EVD/FCR/privacidade | CG-04/07/09/10 |
| CFX-09 CST | fonte de custo ausente transforma desconhecido em zero, V-RA | observações de consumo; nenhum gasto real medido | rotular INDISPONÍVEL/ESTIMADO e evitar inferir economia Jev | unidade, período, fonte e classificação; CST/finanças | CG-08/09 |
| CFX-10 CST↔AUT | limite financeiro indefinido, ultrapassado ou não verificável, V-RC | teto/competência financeira não ratificados; efeito material possível | não presumir orçamento nem renovar autorização; exigir decisão competente | aprovação do limite, fonte do gasto, causalidade; CST/AUT/fundador | CG-01/07/08/12 |
| CFX-11 FCR | projeção stale ou origem conflitante exibida como fato atual, V-RA | versão/frescor de AUT/MIS/EVD/CST; condição externa incerta | indicar DESATUALIZADO/CONFLITANTE, não promover status | proveniência, instante e política de leitura; FCR + origem | CG-02/04/09/10 |
| CFX-12 FCR/CH | canal expõe dado de terceiro ou extrapola direito de leitura, V-RC | políticas de finalidade, titulares e exportação; dano a terceiros | negar projeção/exportação inadequada, escalar privacidade | propósito/direito/retenção e decisão competente; FCR/privacidade/AUT | CG-07/10/12 |
| CFX-13 FCR↔AUT | solicitação de comando chega por painel de leitura, V-RC | canal sem alçada e sem contrato de execução | tratar como pedido NÃO AUTORIZADO; nenhuma execução automática | fonte de poderes, ato humano reservado; FCR/AUT/fundador | CG-01/02/07/12 |
| CFX-14 todos | falha de fonte de autoridade/versão durante reconexão, V-RC | cache, sessão e divergência; validade não demonstrada | não conceder novas ações relevantes; leitura stale somente se direitos permitirem e com aviso | validade do mandato e momento de revalidação; AUT/segurança | CG-01/04/06/07 |
| CFX-15 todos | recuperação reintroduz mandato revogado ou apaga rastro de disputa, V-RC | histórico/revisões e compensações desconhecidos | preservar invalidade futura, manter alegações separadas dos efeitos passados | linha de versões, impacto e direito de retificação; AUT/MIS/EVD/privacidade | CG-04/07/09/11 |
| CFX-16 todos | requisito comum KAC/SEM substitui especialização e cria gate verde falso, V-RA | matriz de origem AC/MC/FCR-AC/CH-AC/IC-AC e SEM-AC | manter STOP, lacuna aberta, aceite por gate/risco separado | fonte do requisito, owner, revisão de equivalência; E3-04/assurance | CG-03/09/10/12 |

**CFX-01..16 documentam cenários de raciocínio**, não falhas realmente observadas, incidentes reais, testes rodados, controles existentes, níveis L2–L4 ou medidas de custo. **Nenhum cenário é aceito por constar da matriz.**

## 4. Semântica de estados e efeitos em trânsito, CFX-ST (PROPOSTA)

Distinguir, sem propor máquina de estados funcional:
1. **SOLICITADO/RECEBIDO:** contato registrado ≠ autorização.
2. **ELEGIBILIDADE_VALIDADA:** avaliação sobre fonte legítima, mandato, escopo, tempo e direitos ≠ ato executado.
3. **ACEITO_PARA_EXECUCAO/EM_TRANSITO:** ato pode ter sido tentado; uma revogação posterior impede novas elegibilidades, **não garante desfazer efeito externo**.
4. **EXECUCAO_RELATADA/NAO_VERIFICADO:** mensagem de sucesso ou timeout não prova efeito nem ausência de efeito.
5. **EFEITO_VERIFICADO:** evidência externa apropriada e revisão independente proporcionais ao risco, sem afirmar reversibilidade universal.
6. **CONFLITANTE/INCONCLUSIVO/INDISPONIVEL/REVOGADO:** proibir inferir consentimento, elevação de privilégios, resultado ou custo zero.

Nenhum commit, resposta de SDK, log imutável, assinatura de requisição ou mensagem entregue deve ser apresentado como prova suficiente de um efeito externo por si só. Idempotência, outbox, saga, rollback e modelos de consistência são **alternativas técnicas não escolhidas** em ADR-C-02/C-03.

## 5. Política DOCUMENTAL de contingência e retorno, CFX-REC (NÃO EXECUTADA)

| Situação | Trilha candidata de recuperação segura | Limite / autorização independente |
| --- | --- | --- |
| Perda de AUT/mandato | manter novas ações relevantes sem autorização, buscar fonte legítima, não usar último canal como autoridade | fundador/alçada competente em ato material; sem tempo de fallback presumido |
| Falha MIS em trânsito | classificar efeito desconhecido, buscar prova apropriada antes de eventual reenvio/compensação | consequências irreversíveis podem existir; compensação demanda decisão e direitos |
| EVD contestada | registrar divergência e corrigir com versões e retenção proporcional, sem apagar fato histórico indevidamente | revisão de prova independente e política de dados |
| CST sem base | divulgar desconhecido/estimado, não imputar gasto, teto ou economia sem fonte | nenhum débito/pagamento/reembolso automático |
| FCR inconsistente | degradar para leitura com incerteza ou negar leitura indevida, sem fabricar controles | privacidade e acesso precedem transparência de terceiros |
| Falha simultânea de domínios | preservar negação de ações novas, classificar estado como INCONCLUSIVO e escalar riscos materiais | não pressupor recuperação global/zero perda, SLA, quorum ou gerente operacional já designado |

**Escalada e notificação:** apontar função legítima responsável, impacto potencial, fonte e incerteza; evitar revelar segredos em relatórios. Nenhuma automação, notificação, plantão, runbook operacional, bot, webhook, orçamento ou integração foi criada.

## 6. Template CFX-EVD para evidenciação futura, ainda vazio

Campos **meramente descritivos**: `scenario_ref`, `source_claim`, `source_version`, `authority_scope`, `mission_ref`, `potential_effect`, `observed_effect_state`, `evidence_class`, `uncertainty`, `rights_context`, `cost_status`, `risk_class_candidate`, `owner_role_candidate`, `applicable_gate_refs`, `decision_history`, `resolution_status`.

- **Estado desta Fase III:** L0 (texto). Não armazenar PII, senha, chave, tokens, dados financeiros privados ou fontes pessoais.
- **Prova futura:** autoria e versão não bastam para autenticar efeitos. Exigir revisão proporcionada ao risco, direitos, fonte independente quando necessário, aceite humano do critério e do gate.
- **Ausência:** `PENDENTE`, `CONFLITANTE` ou `INCONCLUSIVO`; não simular dados nem publicar sucesso fictício.
- **Responsabilidade:** funções AUT, MIS, EVD, CST, FCR, segurança, privacidade, finanças, assurance e fundador são donos candidatos, **não pessoas contratadas ou poderes delegados**.

## 7. Crosswalk de contratos e riscos sem aceite implícito

| Padrão em análise | Fontes documentais | Gate(s) NÃO ACEITOS |
| --- | --- | --- |
| Autoridade, reserva humana, identidade e validade | SEM-ENV, SEM-01/02/07/08; KAC-01..04, SAC-AUT/IC; VSC-01/02/03 | CG-01/04/07/12 |
| Incerteza em ações em trânsito, replay e idempotência | SEM-02/03/07/08/10; KAC-03/05/09, SAC-MIS; VSC-03/04/07 | CG-03/04/06/07/09/11 |
| Correção de evidência e relato ≠ efeito | SEM-03/07/09/10; KAC-05/06/07; VSC-04/08 | CG-03/04/07/09/10 |
| Custos, limites e Jev | SEM-04/10; KAC-08; VSC-02/06 | CG-01/07/08/09 |
| FCR, canal, direitos e fonte desatualizada | SEM-05/06/09/10; KAC-07/10; VSC-05/09 | CG-02/04/07/10/12 |
| Governança, DoR/DoD e não regressão | SEM-11/12, SEM-AC-01..10; KAC-12; AC/MC/CH/IC/FCR-AC | CG-03/09/10/12 |

Essa cobertura é **nominal e conceitual**. Não demonstra equivalência material de critérios e não autoriza reduzir especializações, gates ou obrigações legais.

## 8. DoR/DoD, evidências e gates independentes

| Objeto | DoR FUTURO CANDIDATO | DoD FUTURO CANDIDATO, NÃO SATISFEITO |
| --- | --- | --- |
| Documento CFX | fonte/escopo, cenário, direitos, risco, owner funcional, evidência futura e gate mapeados | revisão dos conflitos e não regressão por responsável competente, fonte e incerteza documentadas |
| AUT/MIS | legitimidade, revogação, ato reservado e efeitos em trânsito delineados | aceita semântica de decisão segura com provas e responsáveis materiais ratificados |
| EVD/CST | integridade/revisão de evidências e origem/limites de custo definidos | fontes reais e métodos de aferição validados em fase autorizada |
| FCR/canais | política de acesso e informação stale, canal independente da alçada | critérios de leitura/privacidade e gates por canal individualmente aceitos |
| E3-01..04 | lacunas, dependências e riscos identificados | STOP próprio satisfeito, cada CG/FCG/MG aceito com evidência independente, e autorização de fase adicional separada |

**CFX-AC-01..08 CANDIDATOS** (não testes):
- CFX-AC-01 autoridade e revogação não podem ser bypassadas por falhas/defasagem de canal.
- CFX-AC-02 efeito em trânsito/timeout não gera reenvio nem compensação automática por pressuposição.
- CFX-AC-03 relato do agente não vira prova independente do efeito.
- CFX-AC-04 custos ausentes não viram zero nem economia Jev.
- CFX-AC-05 privacidade/direitos restringem recuperação, exportação e retenção.
- CFX-AC-06 conflito/indisponibilidade mantém estado seguro, fonte/tempo e dono visíveis.
- CFX-AC-07 rollback futuro requer demonstração de compensabilidade, alçada e tratamento de efeito irreversível.
- CFX-AC-08 aceite de CFX/KAC/SEM e cada gate CG/FCG/MG são independentes da aprovação do método D03-18 C.

## 9. Pendências e STOP CONDITION final

**Ratificado pelo fundador:** D03-18 C, MÉTODO DOCUMENTAL integrado por riscos. **Não ratificados materialmente:** CFX-01..16, CFX-REC, CFX-AC-01..08, donos reais, classificação final de risco, decisões de recuperação, tempos, tecnologias e testes. Qualquer autorização operacional futura requer governança humana legítima, orçamento/direitos e gate correspondente.

**STOP CONDITION VIGENTE:** E3-01..04 EM PLANEJAMENTO, STOP CONDITIONS NÃO ATENDIDAS; ADR-C-01..03 EM ANÁLISE; CG-01..12 SEM ACEITE FINAL; KAC/SAC, SEM-AC e CFX-AC PROPOSTOS L0. **Fase IV NÃO AUTORIZADA.** D03-19 C foi posteriormente ratificada somente como MÉTODO DOCUMENTAL L0; NPV/CFX e critérios permanecem PROPOSTOS, sem aceite material.

## 10. D03-19 C — Provas negativas para cada CFX (somente catálogo documental)

D03-19 C aprovou a **estratégia DOCUMENTAL** de cruzar fontes, riscos, evidência FUTURA, dono e CG individuais. O [Catálogo NPV v0.1](PHASE-III-NEGATIVE-PROOF-CATALOG-v0.1.md) vincula **CFX-01↔NPV-01, ..., CFX-16↔NPV-16** e NPV-AC-01..12 a SEM/KAC, com RV-01..08 para rejeitar falsa equivalência e autoaprovação.

A cobertura nominal **16/16 não demonstra completude semântica**. Cada cenário ainda exige fonte legítima, revisão independente futura e decisão humana competente por risco. Timeout não prova ausência de efeito; compensação não é automática; revogação não reverte consequência passada; custo ausente não vira zero; FCR não ativa comando.

**CFX-01..16, CFX-AC-01..08, NPV-01..16 e NPV-AC-01..12 continuam PROPOSTOS L0. E3/CG/ADR sem aceite; D03-20 PENDENTE; Fase IV NÃO AUTORIZADA.**
