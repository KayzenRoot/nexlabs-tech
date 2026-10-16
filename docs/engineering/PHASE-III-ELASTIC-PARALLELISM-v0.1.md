# NexLabs Technology — Plano Documental de Paralelismo Elástico v0.1

**Decisão:** D03-09 C, aprovada expressamente pelo fundador em 2026-10-15.
**Estado:** APENAS PLANEJAMENTO DOCUMENTAL; a metodologia foi ratificada, não a operação.
**Referências:** [Carta Institucional v1.0](../institutional/CHARTER-v1.0.md), [Registro D03 v0.9](PHASE-III-DECISION-REGISTER-v0.9.md), [Carta da Fase III v0.9](PHASE-III-CHARTER-v0.9.md), [Governança de Agentes v0.2](PHASE-III-AGENT-GOVERNANCE-v0.2.md), [Evidências L0–L4](PHASE-III-EVIDENCE-LADDER-v0.1.md).

**Proibição:** não criar agentes, workflow, CI, infraestrutura, scripts, testes, benchmarks, dados sintéticos ou sistemas. Nenhum modelo, fornecedor, stack, orçamento, tamanho de equipe ou número de agentes simultâneos está aprovado.

## 1. Objetivo

Projetar um mecanismo **futuro e eventual**, sob autorização apropriada, que escolha a concorrência pela **independência real de tarefas, custos totais e risco da alteração**, sem presumir que adicionar executores aumenta a produtividade. Quantidades, horários, limites de API, disponibilidade de modelos e ferramentas permanecem indeterminados.

**Fonte de verdade do sucesso:** entrega aceita com requisitos, revisão e evidências adequadas. Não conta como sucesso a mera geração de linhas de código, a quantidade de PRs, o término autorrelatado por agente ou horas de modelo consumidas.

## 2. Dependências de negócio e possíveis frentes (sem DAG operacional)

| Faixa lógica candidata | Depende de | Trabalho que poderia ter independência futura | Condição bloqueadora |
| --- | --- | --- | --- |
| AUT: identidade, autoridade e revogação | Carta, mandatos e atores legítimos | revisão de limites de delegação e dados | poder humano reservado ou fonte não aceita |
| MIS: escopo e estado de missão | semântica AUT e contrato aprovado | detalhamento da missão | contrato de autorização ambíguo |
| EVD: proveniência, evidência e revisão | identidade MIS e política de privacidade | requisitos de rastreabilidade | fonte de verdade ou autorização ausente |
| CST: consumo e custo observado/estimado | identidade MIS, proveniência da métrica | critérios de medição, independentemente de EVD após contrato | unidade/fonte de preço ausentes |
| FCR: visão do fundador | AUT + MIS + EVD + CST | descrição de leitura legítima após contratos | permissão ou qualidade de dados não verificada |
| AUD/PRV, contratos e segurança | todas | análise transversal desde o início | cláusula crítica, exposição de segredo ou direito violado |

A tabela descreve **dependências candidatas**, não ordenação computável nem interface de agente. EVD e CST são potenciais frentes paralelizáveis somente quando a versão do contrato MIS estiver estável e riscos forem controlados.

## 3. Cenários de concorrência para comparação posterior, sem quantidades

| Cenário | Ideia | Custo potencial | Critério de preferência |
| --- | --- | --- | --- |
| **S0, baseline** | executar tarefas comparáveis sequencialmente | espera em itens independentes | referência de qualidade/custo/tempo |
| **S1, concorrência contida** | executar simultaneamente apenas frentes com contratos estáveis e propriedade distinta | revisão e integração adicionais | tempo total menor sem piora material de custo/risco |
| **S2, expansão condicional** | aumentar concorrência se houver tarefas independentes, capacidade e orçamento | saturação da integração, limites de ferramenta, conflitos | ganho marginal líquido e riscos aceitáveis |
| **SD, redução/pausa** | reduzir concorrência ou interromper quando condições falharem | possível prazo maior | proteger mandatos, qualidade, orçamento e rastreabilidade |

**S0–S2 não correspondem a 1, 2, 3 ou qualquer número prescrito de agentes.** Quantidade por cenário dependerá de verificação de ferramentas, recursos disponíveis, contexto, licenças e plano aprovado em etapa posterior.

## 4. Comparação honesta: definições de métrica futuras

| Indicador | Definição pretendida | Interpretação indevida a evitar |
| --- | --- | --- |
| Tempo até aceite | tempo entre início legitimamente autorizado e aceitação final, incluindo correção, revisão e integração | tempo de geração de código ≠ prazo de entrega |
| Custo total | gastos observados de modelos/ferramentas + encargos de integração, testes, operação e revisão apropriados | tokens estimados ≠ custo real |
| Retrabalho | esforço de correção e integração frente ao esforço total de entrega aceita, com unidade consistente | contagem de commits ≠ complexidade |
| Eficiência de integração | tempo/volume de conflitos, filas de merge, dependências e reprises | mais PRs ≠ maior produção |
| Qualidade e segurança | defeitos relevantes, regressões, violações de escopo, dados, autorizações e contratos | velocidade não compensa falha crítica |
| Economia atribuída ao Jev | comparação controlada de trabalhos equivalentes com baseline, qualidade e causalidade definidas | ganho de paralelismo não vira ganho Jev |
| Confiança da prova | L0–L4 conforme método, versão, fonte, autorização e escopo | narrativa de agente não prova L2–L4 |

**Não há valores observados, preços, percentuais, taxas ou estimativas confiáveis nesta etapa.** Nenhuma previsão numérica deve ser tratada como resultado da NexLabs.

## 5. Gatilhos qualitativos candidatos de escalada, redução e parada

**Considerar escalada futura apenas se:** contratos entre domínios estiverem aceitos; fronteiras e revisores definidos; tarefas independentes identificadas; custo marginal justificável; segurança e dados protegidos; disponibilidade de ferramenta/modelo verificada; evidências L2 ou superiores obtidas quando realmente autorizadas; nenhum controle legal/constitucional dispensado.

**Reduzir paralelismo se:** aumentarem conflitos, refações, atrasos de integração ou custos sem contrapartida; revisores se tornarem gargalo; comportamento do modelo/ferramenta for incerto; orçamento se aproximar do limite legítimo.

**STOP imediato para atos reservados se:** houver revogação/mandato incerto, vazamento de dados, falha crítica, desacordo de contrato, resultado sem evidência, gasto não autorizado, rollback impossível ou ausência de permissão apropriada.

Os critérios são apenas **candidatos documentais** e necessitam especificação de alçadas e limiares pelo fundador antes de execução.

## 6. Governança R0–R3 e evidência L0–L4

D03-08 C governa **risco da tarefa**; D03-07 C governa **evidência da alegação**. Trabalho R0 documental não autoriza automaticamente edição de decisões ratificadas. Para mudanças R1 ou mais em eventual Fase IV, exigem-se evidências reais pertinentes. Trabalho R2/R3 de autorização, sigilo, finanças, contratos críticos ou efeitos irreversíveis requer decisão humana na reserva aplicável. **Não escolher número de agentes para escapar desses controles.**

Os futuros papéis conceituais de planejador, executor, integrador, verificador e analista de custo **não são instâncias de agente** e não exigem um agente independente por papel.

## 7. Interdependência com ADR-C-01..03

- C-01: custo de uma ou duas linguagens e infraestrutura necessária a ferramentas de agentes; não selecionar stack por suposta rapidez de IA.
- C-02: integridade de mandatos, proveniência e custos sob concorrência; não presumir isolamento ou transação que não foi escolhida.
- C-03: versionamento de contratos, propriedade de dados e alteração simultânea; contratos compartilhados exigem regra de coordenação.
- Qualquer configuração futura de paralelismo depende dos ADRs materiais, dados e condições de segurança ratificados separadamente.

## 8. Evidências pendentes e STOP CONDITION

**Concluído:** estratégia documental D03-09 C, registrada e mapeada em opções e critérios. **Não concluído:** dimensionamento real, benchmarking, métricas, estimativa validada, seleção de modelos/ferramentas, agentes instalados, contratos implementados, custo autorizado, CI e aprovação da Fase IV.

Antes de implantar no futuro: ratificar AC, escopo/DoR/DoD, fontes, alçadas, custo, capacidades reais, plano de medição, integração, segurança e rollback. Todas as comparações nesta fase são **L0, documentais**.

**Próximo checkpoint D03-10 (PENDENTE A/B/C):** estratégia para finalizar a prontidão documental dos E3 e apresentar recomendações técnicas separadas para aprovação material, sem iniciar implementação.
