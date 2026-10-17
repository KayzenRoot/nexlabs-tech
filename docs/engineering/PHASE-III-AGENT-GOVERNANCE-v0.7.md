# NexLabs Technology — Governança Documental de Agentes Construtores v0.7

**D03-08 C APROVADA em 2026-10-15:** autonomia graduada por risco e evidências para **agentes de desenvolvimento futuros**.
**Estado:** PROJETO DE POLÍTICA E CRITÉRIOS EM ANÁLISE. **SEM AGENTES CRIADOS, CONFIGURADOS OU AUTORIZADOS A EXECUTAR.**
**Precedência:** [Carta Institucional v1.0](../institutional/CHARTER-v1.0.md), [Fase II encerrada](../design/PHASE-II-ACCEPTANCE-v1.0.md), [Registro D03 v0.13](PHASE-III-DECISION-REGISTER-v0.13.md), [Escopo Fase III v0.13](PHASE-III-CHARTER-v0.13.md).
**Evidências:** [Plano L0–L4 v0.1](PHASE-III-EVIDENCE-LADDER-v0.1.md); [ADRs v0.5](PHASE-III-CONVERGENT-ADR-PACK-v0.5.md).
**Proibido nesta fase:** criar código, scripts, infraestrutura, bot, automação operacional, testes, dados sintéticos, fluxos GitHub, integração ou acesso a segredos; selecionar modelo, quantidade ou orquestrador.

## 1. Princípios constitucionais

A Carta v1.0 prevalece sobre metas de produtividade e autonomia. Agentes construtores não são o Chief of Staff nem os agentes institucionais futuros e não possuem consciência, personalidade jurídica, nem poderes humanos reservados. Mandatos de construção serão delimitados por finalidade, domínio, direitos e orçamento **a ratificar futuramente**.

**Não conceder poder por inferência:** escrever sobre delegação não cria credencial, ACL ou autorização. Autonomia significa liberdade de método apenas dentro de limites explicitamente aceitos, caso a Fase IV seja autorizada.

## 2. Taxonomia de risco candidata R0–R3

| Nível | Exemplos de atividades que seriam avaliadas no futuro | Política conceitual de revisão | Decisão humana reservada |
| --- | --- | --- | --- |
| **R0, documental reversível** | redação não sensível, referência e interpretação sujeitas a verificação | conferência de fonte e escopo L0, controle de alterações | alterar Carta ou decisões ratificadas continua reservado |
| **R1, técnico isolado reversível** | mudança de baixo impacto em um domínio com contratos já aceitos | validação determinística e revisão proporcional, quando realmente executáveis | criação de autorização operacional segue fase separada |
| **R2, alto impacto ou dependência cruzada** | segurança, dados protegidos, integridade, custos relevantes, contratos compartilhados | verificação especializada, provas reais e ratificação quando necessária | não promover alterações sem autoridade apropriada |
| **R3, reservado ou irreversível** | segredos, privilégios, finanças, publicação sensível, deploy e alterações destrutivas | sujeito a ato humano legítimo e controles pertinentes, sem bypass por agente | **sim; não delegável fora dos limites legais e constitucionais** |

**R0–R3 são critérios candidatos, não regras operacionais implementadas**. Os exemplos não fixam thresholds, alçadas financeiras, escopos editáveis, aprovação de PR, rótulos automáticos nem quantidade de agentes.

## 3. A unidade mínima de uma missão construtora futura

Cada tarefa, somente depois de autorização operacional pertinente, precisaria conter:
1. **mandato** e fonte da autorização, validade, ator responsável e atos explicitamente reservados;
2. **objetivo verificável** e critérios AC/DoD com fonte canônica e versão;
3. **risco R0–R3 justificado**, reversibilidade e impactos de segurança/privacidade;
4. **fronteira AUT/MIS/EVD/CST/FCR** e direitos sobre arquivos e informações;
5. **dependências e contratos**, especificando o que outro agente não pode mudar unilateralmente;
6. **limites de recursos/custos**, ferramentas e modelos somente após aprovação e disponibilidade efetiva;
7. **evidência L0–L4 exigida**, sem falsear ausência de execução;
8. **validação/aceitação proporcional** e humano legitimado para atos reservados;
9. **condição de parada e rollback proposto**, inclusive resposta a conflito e ambiguidade;
10. **trilha de revisão e resultado**, distinguindo relato, prova e aceite.

Nesta fase **não abrir tarefas executáveis**. Documentar o conceito não equivale a expedir ordem de desenvolvimento.

## 4. Orquestração futura: plano lógico, sem sistema

A eventual função coordenadora deverá **analisar dependências, identificar conflito de propriedade, propor tarefas e riscos, relacionar resultados a evidências e encaminhar decisões reservadas ao fundador**. Nenhum algoritmo de scheduling, cliente, modelo, runtime, servidor ou ferramenta foi escolhido.

### 4.1 Fronteiras de responsabilidade

| Papel candidato | Finalidade | Restrição |
| --- | --- | --- |
| Planejador / coordenador | decompor trabalho aprovado e analisar dependências | não altera sozinho mandato, orçamento ou critérios |
| Executor especializado | produzir alteração futura de escopo isolado | não aprova próprio resultado nem muda contratos partilhados sem revisão |
| Verificador | confrontar artefato, diff, evidência e AC | não declarar testes realizados quando não o foram |
| Integrador | confrontar compatibilidade e checks, preparar aceite | não bypassar proteção de branch, revisão legítima ou autoridade |
| Analista de custo | atribuir custo e retrabalho a fontes comparáveis | não estimar como medido, nem alegar economia Jev sem baseline |

**Papéis ≠ número de agentes executando ao mesmo tempo.** Uma entidade pode exercer mais de um papel em contextos distintos, porém não se deve simular segregação de funções quando a independência for material. Revisão automatizada não substitui um revisor humano legalmente exigido.

### 4.2 Dependências e paralelismo planejados

- AUT e contratos de mandatos precisam ser estáveis antes de mudanças que dependam deles em MIS/FCR;
- MIS define vínculo antes de EVD e CST relatarem evidências/custos;
- EVD/CST podem ser **candidatos** a trabalho paralelo depois de interfaces aceitas, sem simultaneidade implícita;
- FCR somente poderá apresentar leituras de fonte legítima e limites de evidência;
- segurança, retenção, proveniência e controle de custo atravessam todos os domínios;
- conflito de contrato, acesso, validação ou orçamento impõe **STOP**, replanejamento e autoridade apropriada, não fusão forçada.

**Nenhuma quantidade, modelo, runtime ou concorrência foi fixada.** A D03-09 C foi ratificada posteriormente como MÉTODO documental de avaliação elástica, sem fixar valores. Ver [Plano v0.1](PHASE-III-ELASTIC-PARALLELISM-v0.1.md).

## 5. Revisão por risco, sem burocracia desnecessária

| Faixa | Prova e aceite futuro candidato | Intervenção humana |
| --- | --- | --- |
| R0 | qualidade documental, fonte, revisão versionada e L0 | necessário se mexer em norma/decisão reservada |
| R1 | requisitos aceitos, diff e checks realmente executados na futura Fase IV | conforme alçada e risco efetivos |
| R2 | revisão especializada de mandatos/contratos/dados, testes e impacto | exigida para decisões reservadas e conforme regulamentação |
| R3 | identidade/mandato e ato humano explícito, justificativa, trilha e medidas de proteção | **condição obrigatória onde a Carta e lei reservarem** |

As faixas **não dispensam controles mandatórios**; “autonomia graduada” não significa merges sem checks, teste opcional ou aprovação financeira tácita. Propõe-se evitar reviews redundantes quando o mesmo risco já estiver controlado e a duplicação não agregar evidência.

## 6. Relação com a escada L0–L4

- **L0:** somente documentação; situação atual de toda a Fase III.
- **L1:** futuro cenário sintético rotulado; não demonstra desempenho real de agente.
- **L2:** futura execução realmente demonstrada com testes e revisão; não prova dados de terceiros ou integração externa.
- **L3:** eventual acesso real e consentido a fonte com proveniência, privacidade e limites; não implica efeito operacional.
- **L4:** resultado operacional comprovado e aceito com fonte e escopo; autorrelato do agente não é prova.

**R0–R3 indicam risco/controle da mudança; L0–L4 indicam evidência da afirmação.** Não confundir escala de risco com escala de evidências.

## 7. Economia de construção, custo de tokens e Jev

Comparar futuramente trabalho equivalente em:
- tempo até **entrega aceita** inclusive coordenação, revisão, conflitos e correção;
- consumo por modelo/cliente/ferramenta, preços datados, limites de conta e orçamento real;
- custo de contexto, duplicação de ferramentas, integração de múltiplas stacks e suporte;
- qualidade, regressões, incidentes de segurança, mudanças revertidas e explicações sem fontes;
- capacidade limitada da equipe de integrar paralelismo crescente.

**Ganhos de produtividade, economia Jev, custo por agente e ROI NÃO foram medidos.** O princípio da D03-08 é delegação proporcional a risco, não promessa de economia nem liberação de despesa.

## 8. Riscos e limites especiais do fundador

Requisitos preservados **somente como futura intenção**: Founder Command Center; consulta/controle legítimo; Telegram bilateral com Chief of Staff; relatórios PDF/planilhas; vozes distintas; tokens/custos e Jev; finanças; VPS. Nenhum dado operacional dessas fontes está conectado ou verificado. O orquestrador de **construção** não assume o mandato do Chief of Staff **institucional**.

O repositório foi observado como público em revisão anterior. **Não inserir segredos, dados privados, tokens, custos confidenciais, dados de VPS pessoais ou documentos financeiros reservados** sem política de tratamento e configuração legitimamente autorizadas.

## 9. Próximos gates e STOP CONDITION

D03-08 C está **CONCLUÍDA COMO DIRETRIZ**, mas plano de fábrica permanece **EM ANÁLISE**. Faltam: seleção/contratação concreta de ferramentas e modelos; desenho de política com limites reais de permissões, segurança e custo; avaliação concreta futura de concorrência sob método D03-09 C, sem quantidades aprovadas; revisão de proteção do repositório; ADR-C-01..03; orçamento; AC finais; autorização de Fase IV; testes/integração efetivos quando autorizados.

**Nenhum agente, orquestrador, serviço, CI, permissões, teste, mock, dado sintético ou automação foi implantado.**

## 10. D03-09 C: dimensionamento elástico, aprovado somente como método (NOVO v0.2)

A estratégia do fundador é avaliar **baseline sequencial e concorrência variada conforme dependências reais e ganho líquido**, não adotar uma quantidade fixa, um orquestrador específico ou automação imediata. Consultar [Plano de Paralelismo Elástico v0.1](PHASE-III-ELASTIC-PARALLELISM-v0.1.md).

### 10.1 Matriz de autoridade × independência

| Classe de trabalho futuro | Elegibilidade candidata de execução concorrente | Dependência que exige serialização ou revisão | Evidência futura |
| --- | --- | --- | --- |
| R0 documentação pública reversível | possível, sob fonte e escopo isolados | Carta, decisões ratificadas e arquivos de governança não podem ser reescritos sem autoridade | L0 documentação e revisão |
| R1 tarefa técnica confinada a fronteira | possível somente sob contratos estáveis | mudanças de contrato central e falhas de testes interrompem | L2 com testes reais, quando autorizados |
| R2 contratos/autorização/dados privados | concorrência condicionada à revisão especializada e direitos | compartilhamento de contrato e privacidade | evidência adequada e aprovação humana pertinente |
| R3 ato reservado, credenciais, efeitos irreversíveis | nenhuma concorrência substitui autorização humana | mandato, alçada financeira, segurança, execução externa | ato legítimo mais prova do resultado quando ocorrer |

**Não há agentes criados, filas, limites de simultaneidade, perfis de acesso ou alçadas numéricas definidos.**

### 10.2 Métricas de decisão (sem valores)

- tempo até a entrega realmente **aceita**;
- custo total de tokens, ferramentas, revisão, integração, manutenção e retrabalho;
- qualidade, defeitos, violação de mandatos, privacidade e contratos;
- custo marginal da concorrência e saturação do integrador;
- economia Jev só com baseline independente e metodologia reprodutível.

Promover S0→S1→S2 apenas quando a análise **futura e autorizada** provar benefício líquido e riscos aceitáveis. Recuar/STOP em caso de vazamento, custo não autorizado, violação constitucional, falha de revisão ou conflito não solucionado.

### 10.3 Fatores que ainda precisam de ratificação

Disponibilidade efetiva de modelos e clientes, limites financeiros, permissão, quantidade de agentes, prioridade e volume de tarefas, fonte de métricas, política de revisão e critérios quantitativos permanecem **indeterminados**. D03-08 permanece em vigor como política documental. **D03-10 C APROVADA posteriormente** como método documental de fechamento integrado por gates; **D03-11 C APROVADA documentalmente; D03-12 C APROVADA documentalmente; D03-13 C APROVADA documentalmente**. Nenhum pacote E3 foi encerrado.

**Sem instalação, workflow, autorização operacional, benchmark ou resultado de produtividade.**

## 11. Governança de agentes no fechamento integrado D03-10 C (NOVO v0.3)

**Artefato central:** [Matriz de Convergência e Prontidão v0.1](PHASE-III-CONVERGENCE-READINESS-v0.4.md). O plano da fábrica não está pronto para execução; CG-07/08/09/10/12 permanecem PENDENTES. A D03-10 C estabelece o método de tratamento das lacunas, sem fornecer evidências operacionais.

### 11.1 Requisitos de prontidão verificável da futura fábrica

| ID | Requisito de aceitação documental futura | Dependência | Lacuna |
| --- | --- | --- | --- |
| AGF-01 | funções planejamento/execução/revisão/integração/custos e alçadas propostas com segregação adequada | Carta e AUT; R0..R3 | atribuição e aceite humanos específicos |
| AGF-02 | contrato de unidade de trabalho e domínio definidos | MIS, EVD, CST; C-03 | contratos e responsáveis não ratificados |
| AGF-03 | critério de revisão, validação e evidências L0..L4 por risco | D03-07/08 C | provas e testes não executados |
| AGF-04 | metodologia S0/S1/S2/SD e travas de concorrência | D03-09 C | sem disponibilidade, cargas, limites e métricas |
| AGF-05 | custos totais, modelo/cliente e teto de despesa aprovados | CG-08 | valores e ferramenta não escolhidos |
| AGF-06 | proteção de dados, segredos e direitos sobre repositórios | CG-07 | política final e permissões ausentes |
| AGF-07 | regra STOP, rollback e decisão humana sobre atos reservados | CG-01/07/12 | aceite/revisores e sistema não existem |
| AGF-08 | critérios de aceitação do trabalho de código sem autorrelato | CG-03/10 | DoD final, testes e controles ainda pendentes |

**Estado de AGF-01..08: PROPOSTOS, NÃO ACEITOS COMO PRONTIDÃO.** Não confundir papel lógico com funcionário digital existente ou mecanismo de segurança implantado.

### 11.2 TCO e medição sem valores inventados

Na comparação futura: custo por tarefa **aceita** inclui tokens, uso real de ferramentas, rate limits, revisão, testes, conflitos, manutenção, segurança e tempo humano. Medição efetiva só com autorização posterior, baseline S0, mesmos requisitos e evidência. Indicadores Jev requerem isolação causal: paralelismo, prompt, modelo e economia de contexto não podem receber o mesmo crédito sem método.

### 11.3 Governança institucional e limites

Agentes **construtores** não recebem automaticamente autoridade de agentes **institucionais**. O Chief of Staff, Telegram, vozes, relatório PDF/planilha, Founder Command Center, observação de finanças e VPS são requisitos futuros, não funções disponíveis. Não selecionar modelo, ferramenta, número, concorrência, orçamento ou stack. Não alterar a Carta.

**STOP CONDITION E3-03: NÃO ATENDIDA. D03-10 C aprovado somente como estratégia. D03-11 C APROVADA documentalmente; D03-12 C APROVADA documentalmente; D03-13 C APROVADA documentalmente. Fase IV NÃO AUTORIZADA.**


## 12. D03-11 C: fronteira entre agentes construtores e agentes institucionais (NOVO v0.4)

**Princípio aprovado:** [Plano FCR v0.1](PHASE-III-FOUNDER-COMMAND-CENTER-v0.3.md) orienta o desenho de supervisão verificável, com **ações humanas previstas como futura necessidade**, não botões, ferramentas ou mandatos reais. O plano de agentes construtores permanece separado.

| Responsabilidade futura candidata | Agentes CONSTRUTORES | Agentes INSTITUCIONAIS |
| --- | --- | --- |
| Missão | criar futuramente software dentro de tarefas autorizadas da Fase IV | executar eventualmente missões organizacionais sob mandatos institucionais ainda não ratificados |
| Prova | diff, teste real, revisão e aceite de engenharia quando autorizados | origem/resultado da missão, prova externa e custo legitimamente medido |
| Autoridade | não aprovar a própria entrega, custos ou poderes | não adquirir poderes humanos por acesso ao FCR ou por aparência cognitiva |
| Dados | arquivos de projeto sob limites, com privacidade e segredos protegidos | informações empresariais conforme finalidade, direitos e política específica futura |
| Supervisão | governança de revisão R0–R3 da construção | Founder Command Center e política institucional de mandatos D03-12 C (APROVADA documentalmente) |
| Orçamento | limites de tokens/modelos/ferramentas, somente quando aprovados | alçadas institucionais da Carta, sem ligação automática a tokens de construção |

**D03-08 C e D03-09 C não autorizam agentes institucionais.** O FCR não delega automaticamente aos construtores, e a fábrica de software não se torna Chief of Staff.

### 12.1 Custos, privacidade e validação

A futura construção de FCR-01..06 deve incluir esforço de contratos de leitura, proteção de mandatos, testes de revogação e fonte, custo total e verificação de ausência/qualidade dos dados na comparação S0/S1/S2/SD. Nenhuma métrica da VPS, receita, custo real ou economia Jev foi observada; o critério L0 documental se aplica. Segurança deve evitar credenciais em documentação pública e impedir permissão herdada de qualquer papel.

### 12.2 Gate

[Convergência v0.3](PHASE-III-CONVERGENCE-READINESS-v0.4.md): CG-01/07/08/09/10/12 continuam sem aceite, modelos/ferramentas/número de agentes não decididos. **E3-03 STOP CONDITION NÃO ATENDIDA. D03-12 C APROVADA documentalmente; D03-13 C APROVADA documentalmente. Sem agentes, orquestrador ou workflows implantados.**


## 13. D03-12 C: separação entre a fábrica construtora e mandatos INSTITUCIONAIS (NOVO v0.5)

A D03-12 C **não concede poderes aos agentes construtores**. Seu escopo documental é a eventual atuação de agentes **institucionais** sob mandatos limitados, revogáveis e por risco. A construção de software segue sob D03-08 C, D03-09 C, requisitos E3-03 e autorização futura distinta. [Mandatos v0.1](PHASE-III-INSTITUTIONAL-MANDATES-v0.2.md); [CG v0.3](PHASE-III-CONVERGENCE-READINESS-v0.4.md).

| Responsabilidade | Construtor futuro | Institucional futuro |
| --- | --- | --- |
| Origem da missão | tarefa de engenharia aprovada com AC/DoD e escopo | mandato de negócio por ator competente |
| Autoridade | limites de edição/revisão e atos de merge legítimos, se aprovados | finalidade, duração, direitos e limite de custo da missão, se aprovados |
| Prova de entrega | alteração de código, diffs, testes reais e aceite | evidência da ação/resultado institucional e legitimidade da fonte |
| Negação/revogação | interrupção por conflito de governança ou autorização de desenvolvimento | revogação/expiração do mandato institucional e tratamento temporal |
| Dados | repositórios de projeto dentro de permissões futuras | dados empresariais/terceiros somente com direitos e finalidade |
| Custo | modelos/tokens, revisão, integração, retrabalho | despesas empresariais e mandatos financeiros, sem teto ainda definido |

Nenhum agente institucional recebe por padrão poderes do Chief of Staff, direitos da conta GitHub, acesso à VPS, finanças, Telegram, voz ou arquivos. Nenhum construtor pode emitir ou ampliar mandato institucional. A D03-12 C não modifica número, modelo, custo, ferramenta, paralelismo S0/S1/S2/SD ou orçamento da fábrica.

### 13.1 Interface da futura engenharia com o primeiro FCR

Construtores poderão ser responsáveis apenas futuramente por implementar capacidades FCR-01..06 e contratos de autoridade MC-01..14, se houver autorização de Fase IV. Revisão do próprio agente não substitui evidência. Negação/revogação e proteção de segredos são futuros casos a demonstrar, não checks disponíveis agora.

**E3-03 EM PLANEJAMENTO; CG-07/08/09/10/12 SEM ACEITE; sem agentes ou tarefas criadas. D03-13 C APROVADA documentalmente para política de canais futuros.**

## D03-13 C — Limite entre canais institucionais e desenvolvimento (2026-10-17)

O futuro **Chief of Staff** e seus meios de interação (FCR, Telegram, voz, relatórios) seguem uma autoridade de mandato INSTITUCIONAL independente do canal, segundo [Política v0.1](PHASE-III-CHANNEL-GOVERNANCE-v0.1.md). Agentes CONSTRUTORES não herdam alçada empresarial ou permissão de instalação e integração por projetarem requisitos.

Qualquer trabalho futuro de construção de canais exigirá Work Order, autorização da Fase IV, risco, contratos, critérios de aceitação, evidência e revisão externa proporcional. **D03-13 C é documental; D03-14 ainda pendente; nenhuma execução, ferramenta ou agente criado.**
## 15. D03-15 C — Aceitação partilhada, deveres de construtores independentes (2026-10-17)

A decisão **DOCUMENTAL L0** permite reutilização proposta de KAC-01..12 como invariantes de autoridade, privacidade, evidência, qualidade, custo e gates, mantendo **SAC-BLD-01** e os critérios de engenharia RG-01..09 e EL-01..10 como obrigações específicas. [Matriz KAC/SAC v0.1](PHASE-III-ACCEPTANCE-CORE-v0.1.md).

Agentes CONSTRUTORES não recebem mandato INSTITUCIONAL por uma referência comum. A autonomia/riscos R0..R3 da fábrica de software não definem poderes de agentes de negócios. Prova de pipeline, autorrelato, artefato documental ou checksum não satisfaz sem revisão um efeito corporativo; evidência e critérios de aceite permanecem independentes.

**D03-15 C APROVADA SOMENTE COMO MÉTODO DOCUMENTAL. D03-16 PENDENTE. E3-01..04 EM PLANEJAMENTO; CG/ADRs SEM ACEITE; Fase IV NÃO AUTORIZADA.**
