# NexLabs Technology — Fatia Vertical Documental Orientada a Riscos v0.1

**Work Order:** NX-P3-D03-16 · **Decisão:** D03-16 C, expressamente aprovada pelo fundador em 2026-10-17.
**Status:** MÉTODO DE PLANEJAMENTO DOCUMENTAL L0 APROVADO. A matriz de riscos, donos funcionais, critérios e artefatos abaixo é **PROPOSTA para desenvolvimento e futura aceitação**, não é demonstração de sistema, teste, eficácia, regra legal definitiva ou aceite de gates.
**Autoridade:** [Carta Institucional v1.0](../institutional/CHARTER-v1.0.md), [Registro D03 v0.16](PHASE-III-DECISION-REGISTER-v0.16.md), [Núcleo KAC/SAC v0.2](PHASE-III-ACCEPTANCE-CORE-v0.2.md); D03-02 C (primeira vertical), D03-10 C (gates), D03-11 a 15 C preservadas.
**Fronteira:** E3-01..04 continuam EM PLANEJAMENTO, CG-01..12 SEM ACEITE FINAL, ADR-C-01..03 EM ANÁLISE e Fase IV NÃO AUTORIZADA.

## 1. Estratégia aprovada e limites do escopo

Avançar documentalmente por uma única cadeia conceitual AUT → MIS → EVD/CST → FCR, priorizando riscos críticos, condições de prova, responsáveis funcionais e gates **independentes por pacote/domínio**. Revisar dependências em conjunto sem alegar que os cinco domínios foram projetados em definitivo ou que a cadeia foi executada. A vertical começa em autoridade legítima, mantém identidade de missão e efeito como informações distintas, produz evidências e dados de custo *quando disponíveis* e prevê visualização legítima no FCR. FCR é FUTURA consulta/supervisão, não painel criado ou alçada adicional. Telegram, voz e exports não entram na primeira entrega por inferência.

**Decisões NÃO tomadas:** contratos físicos, esquemas/API, tecnologia, banco, modelo, quantidade de agentes, integrações, identidade real, tokens, orçamento, contratos legais, custos, contratação, implementação, fases IV/V. A aprovação D03-16 C **não satisfaz** STOP CONDITIONS de E3, nem aprova KAC/SAC ou aceite de CG.

## 2. Escala qualitativa CANDIDATA de prioridade documental

| Prioridade proposta | Quando usar para ordenar a análise | Reação documental, não operacional |
| --- | --- | --- |
| V-RC crítica | risco de poder ilegítimo, ato reservado, dano a direitos, exposição sensível, falsificação de efeito ou revogação ignorada | especificar negação/STOP, responsável e prova necessária ANTES de detalhes secundários |
| V-RA alta | temporalidade, replay, divergência, custo material desconhecido, perda de proveniência, falha de reconciliação | explicitar fonte, exceção, incerteza e gate de revisão |
| V-RM moderada | lacunas de estados, observabilidade e correção/retenção de histórico | definir classificação, responsável e dependência |
| V-RB baixa | conveniência de apresentação, formato adicional e relatórios não essenciais | manter fora da primeira vertical até decisão posterior |

Essas prioridades **não fixam tolerância jurídica, quantia, prazo, probabilidade ou gatilho executável**. NÃO se confundem com R0–R3 dos agentes construtores, classificação legal real ou severidade de teste operacional. Uma exceção de proteção humana/privacidade pode sempre elevar uma lacuna a V-RC na análise futura.

## 3. Ordem de elaboração e artefatos DOCUMENTAIS da cadeia

| Sequência lógica | Domínio / questão prioritária | Entrada candidata e saída documental | Dono FUNCIONAL PROPOSTO, não designado | Dependências/gates não aceitos |
| --- | --- | --- | --- | --- |
| V-01 | AUT: principal, competência, mandato, limite, direitos, vigência, revogação, negativa segura | intenção humana legítima → estado documentado de mandato/ausência/conflito; sem emissão real | fundador/alçada competente + AUT + privacidade | KAC-01/02/03/04, SAC-AUT-01; CG-01/04/07/12 |
| V-02 | MIS: pedido vs missão autorizada, responsabilidade, início/pausa, consequência de revogação | estado autorizado verificável → ciclo de missão candidato, incluindo NÃO AUTORIZADA e INCONCLUSIVA | MIS + AUT + assurance independente | KAC-03/05/09, SAC-MIS-01; CG-02/03/06/11 |
| V-03 | EVD: proveniência, contestação, evidência de efeito, classificação L0..L4 e revisão | relato/artefato/ausência → alegação classificada como relato, hipótese, prova ou contestação, sem sucesso inventado | EVD + auditoria/revisão independente | KAC-05/06/07, SAC-EVD-01; CG-03/04/09/10 |
| V-04 | CST: consumo, custo medido/estimado/desconhecido, limites financeiros e Jev | observações autorizadas e fontes → custo com unidade, origem e estado de confiabilidade, sem valor numérico fictício | CST + finanças + assurance | KAC-02/07/08, SAC-CST-01; CG-03/07/08/09 |
| V-05 | FCR: leitura autorizada, divergência/defasagem, distinção entre relatório e efeito | projeções legítimas AUT/MIS/EVD/CST → requisito de exibição confiável de estados e incertezas, sem interface criada | FCR + AUT + privacidade + fundador para atos reservados | KAC-05/06/07/10/12, SAC-FCR-01; CG-02/03/07/10/12 |

**A ordem é de especificação, não de execução nem cronograma linear obrigatório.** EVD/privacidade acompanham V-01 e V-02 desde o primeiro cenário, CST é abordado desde riscos financeiros e a avaliação de cenários negativos cruza todas as etapas. A presença do FCR na vertical **não ativa comandos**.

## 4. Casos negativos transversais e rastreio por risco (PROPOSTOS)

| ID | Caso conceitual, sem dado real | Risco prioritário | Resultado DOCUMENTAL requerido, não comprovado | Evidência FUTURA / dono / gates |
| --- | --- | --- | --- | --- |
| VSC-01 | conta ou sessão de canal alega permissão sem mandato | V-RC | NÃO AUTORIZAR; distinguir identidade, sessão e alçada | origem/decisão humana; AUT e privacidade; CG-01/07 |
| VSC-02 | mudança reservada ou gasto material sem consentimento humano competente | V-RC | tratar como PROPOSTO/RECUSADO; nunca como aprovado por silêncio | registro de aprovação legítima e limite; fundador, AUT, finanças; CG-01/07/08/12 |
| VSC-03 | suspensão/revogação concorre com missão em trânsito | V-RC | bloquear novas elegibilidades; distinguir ações em trânsito e efeitos irreversíveis | versões e tempos confiáveis, evidência de consequências; AUT/MIS/EVD; CG-04/07/11 |
| VSC-04 | agente relata missão concluída sem efeito independente comprovado | V-RC | classificar RELATADA/NÃO VERIFICADA; manter possibilidade de contestação | fonte/evidência independente L2+ somente no futuro autorizado; MIS/EVD; CG-03/09/10 |
| VSC-05 | projeção FCR ou canal externo expõe dados protegidos | V-RC | impedir divulgação incompatível com direitos e propósito | direito/acesso/retensão verificados quando apropriado; privacidade/FCR; CG-07/10 |
| VSC-06 | mensuração CST ausente vira zero ou economia Jev | V-RA | manter AUSENTE/INCONCLUSIVA; não declarar causalidade | unidade, fonte e baseline real futuro; CST/finanças; CG-08/09 |
| VSC-07 | duplicidade, replay, relógio inconsistente ou fonte divergente | V-RA | não elevar permissão/efeito; registrar CONFLITANTE e revisão legítima | versão, correlação e condição negativa; AUT/MIS/EVD; CG-04/06/07/11 |
| VSC-08 | evidência corrigida após relatório anterior ou retenção indevida | V-RA | preservar trilha proporcional de versão/contestação, retificação e direitos | fonte, titularidade e revisão; EVD/privacidade; CG-04/07/09 |
| VSC-09 | pedido de comando chega pelo FCR de leitura | V-RC | leitura ≠ poder de executar; decisão humana/etapa futura independente | política de atos reservados e alçada; AUT/FCR; CG-02/07/12 |
| VSC-10 | documento KAC substitui SAC e omite proteção específica | V-RA | não reduzir obrigação; manter gatilho de revisão e STOP documental | referência AC/MC/CH/IC/FCR original; assurance; CG-03/09/12 |

**Todos VSC são cenários de análise L0, não testes executados, checks CI ou prova L2–L4.** A prioridade é hipotética para planejamento e requer ratificação/avaliação jurídica conforme o caso futuro.

## 5. Contrato de evidência mínimo CANDIDATO por lacuna

Para cada item aberto (não inserir dados sensíveis reais em repo público): `id_criterio_original`, `id_KAC/SAC`, `id_VSC`, `dominio`, `acao/risco`, `direito_ou_alcada`, `dono_funcional_proposto`, `fonte_pretendida`, `estado` (PROPOSTO/PENDENTE/INCONCLUSIVO), `classe_evidencia` (L0 até prova distinta), `versao_fonte`, `tempo_relevante`, `excecao`, `gate_aplicavel`, `decisor_humano_legitimo`, `decisao_aceite` (vazia até ato futuro). Essa lista é **especificação conceitual**, não esquema técnico ou registro preenchido.

**Distinguir quatro avaliações:** (1) completude da documentação; (2) aceite material do critério; (3) fechamento de gate de prontidão; (4) autorização separada de Fase IV. **Nenhuma herda o estado da outra.**

## 6. DoR/DoD por fatia e gates preservados

| Pacote | DoR documental CANDIDATO | DoD documental CANDIDATO, ainda NÃO ATENDIDO | Gate de aceite independente |
| --- | --- | --- | --- |
| E3-01 | domínio/risco/direitos/IDs KAC/SAC e fontes propostos | escopo da vertical e negativos sem lacunas essenciais, revisão do fundador | CG-01/02/03/04/07/10 |
| E3-02 | opções de contrato/stack/fontes com critérios comparáveis | ADR-C-01/02/03 comparados e ratificados por atos adequados, prova documental de limites | CG-04/05/06/07/08/11 |
| E3-03 | regimes de agentes separados, critérios RG/EL e custos declarados | engenharia de agentes justificada com independência/revisão e regras proporcionais, sem implantação | CG-07/08/09/10/12 |
| E3-04 | matriz de riscos/owners/fontes e estratégias de provas L0–L4 | gates rastreados a evidência e aceites futuros, sem falsos sucessos; autorização de transição separada | CG-01..12, FCG/MG aplicáveis |

**Nada nesta tabela aprova DoR, DoD, E3, CG, ADR ou Phase IV.** Direitos e obrigações de domínios/canais continuam preservados por [Mapa KAC/SAC v0.2](PHASE-III-ACCEPTANCE-CORE-v0.2.md); credenciais, serviços, contas, fontes reais e atos financeiros NÃO foram criados. A evidência real de operação e testes só poderá ser requerida em fases devidamente autorizadas.

## 7. Revisão e STOP CONDITION

**Riscos de governança:** priorização crítica transformar-se em permissão; assumir que estatística ausente é zero; confundir parecer de agente com review independente; tratar 99 IDs mapeados como equivalência comprovada; usar relatório FCR como comprovação de ação externa; fechar CG em lote. **Mitigação documental:** fonte, risco, responsável funcional, evidência futura e gate individual rastreáveis, inclusive lacunas e reservas humanas.

**STOP CONDITION VIGENTE:** D03-16 C APROVADA SOMENTE COMO MÉTODO DOCUMENTAL L0, enquanto V-01..05, VSC-01..10, KAC/SAC, DoR/DoD e owners são PROPOSTOS e não aceitos. **E3-01..04 EM PLANEJAMENTO; STOP CONDITIONS NÃO ATENDIDAS; ADR-C-01..03 EM ANÁLISE; CG-01..12 SEM ACEITE FINAL; Fase IV NÃO AUTORIZADA.** D03-17 A/B/C é a próxima deliberação estratégica apenas PROPOSTA, sem escolha.
