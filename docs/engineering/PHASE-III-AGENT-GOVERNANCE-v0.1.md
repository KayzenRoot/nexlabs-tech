# NexLabs Technology — Governança Documental de Agentes Construtores v0.1

**D03-08 C APROVADA em 2026-10-15:** autonomia graduada por risco e evidências para **agentes de desenvolvimento futuros**.
**Estado:** PROJETO DE POLÍTICA E CRITÉRIOS EM ANÁLISE. **SEM AGENTES CRIADOS, CONFIGURADOS OU AUTORIZADOS A EXECUTAR.**
**Precedência:** [Carta Institucional v1.0](../institutional/CHARTER-v1.0.md), [Fase II encerrada](../design/PHASE-II-ACCEPTANCE-v1.0.md), [Registro D03 v0.8](PHASE-III-DECISION-REGISTER-v0.8.md), [Escopo Fase III v0.8](PHASE-III-CHARTER-v0.8.md).
**Evidências:** [Plano L0–L4 v0.1](PHASE-III-EVIDENCE-LADDER-v0.1.md); [ADRs v0.3](PHASE-III-CONVERGENT-ADR-PACK-v0.3.md).
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

**Nenhuma quantidade, modelo, runtime ou concorrência foi fixada.** A D03-09 definirá o método documental de avaliação de concorrência.

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

D03-08 C está **CONCLUÍDA COMO DIRETRIZ**, mas plano de fábrica permanece **EM ANÁLISE**. Faltam: seleção/contratação concreta de ferramentas e modelos; desenho de política com limites reais de permissões, segurança e custo; escolha de estratégia D03-09 de concorrência; revisão de proteção do repositório; ADR-C-01..03; orçamento; AC finais; autorização de Fase IV; testes/integração efetivos quando autorizados.

**Nenhum agente, orquestrador, serviço, CI, permissões, teste, mock, dado sintético ou automação foi implantado.**
