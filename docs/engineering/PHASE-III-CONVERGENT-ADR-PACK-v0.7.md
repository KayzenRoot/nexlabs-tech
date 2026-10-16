# NexLabs Technology — Pacote Convergente de ADRs v0.7

**Autorização documental:** D03-06 C, aprovada expressamente pelo fundador em 2026-10-15.
**Estado:** **PACOTE EM ANÁLISE**. **ADR-C-01, ADR-C-02 e ADR-C-03 NÃO APROVADOS.**
**Autoridade:** [Carta Institucional v1.0](../institutional/CHARTER-v1.0.md), [aceite da Fase II](../design/PHASE-II-ACCEPTANCE-v1.0.md), [Registro D03 v0.10](PHASE-III-DECISION-REGISTER-v0.12.md), [Escopo Fase III v0.10](PHASE-III-CHARTER-v0.12.md).
**Proibição explícita:** nenhum código, script, protótipo, imagem, CI funcional, integração, RAG, API operacional, agente, infraestrutura, banco ou software criado.

## 1. Critério da convergência

A NexLabs adotou como princípios:
- D03-02 C: primeira vertical verificável entre intenção/autoridade, missão, evidências e custos quando mensuráveis;
- D03-03 C: núcleo modular evolutivo com fronteiras extraíveis, sem escolher topologia física;
- D03-04 C: base principal única **a escolher por evidências**, especializações somente com benefício líquido;
- D03-05 C: fonte de verdade verificável com histórico proporcional;
- D03-06 C: analisar **em conjunto** as opções de stack, persistência e contratos, revelando dependências e custos.

**A escolha de um candidato em uma tabela abaixo NÃO é adoção, nem previsão de vencedor.** Notas, percentuais de produtividade, tempos, preços, taxas, cotas, scores e ganhos são **não medidos**.

## 2. Uma matriz de requisitos comum

| ID | Necessidade do primeiro ciclo | Critério de veto qualitativo |
| --- | --- | --- |
| RQ-C01 | Fundador/atores e mandatos reais separados de solicitações e permissões | autorizações ou revogações contornáveis |
| RQ-C02 | Missão com responsável e estados de intenção, relato e comprovação distinguíveis | relato equiparado a execução sem prova |
| RQ-C03 | EVD preserva origem e revisão da evidência com retenção legítima | adulteração silenciosa, proveniência atribuída falsamente |
| RQ-C04 | CST distingue estimado, medido, desconhecido e economia Jev com baseline | ausência de dado = zero ou economia inventada |
| RQ-C05 | FCR acessa apenas informações com legitimidade e comunica incerteza | privilégios ampliados por agregação |
| RQ-C06 | Extraibilidade não corrompe mandatos, histórico ou direitos | dependência oculta sem caminho de migração aceitável |
| RQ-C07 | Proteção da informação, minimização e direitos de terceiros | armazenamento público de segredo/dado sensível |
| RQ-C08 | Custo de implantação, operação, licenças e agentes mensurável futuramente | orçamento implícito ou custo alegado sem fonte |
| RQ-C09 | Validação futura com casos AC-01..AC-20 e critérios idênticos | alternativa incapaz de dar suporte à aceitação |
| RQ-C10 | Portabilidade, reversibilidade e manutenção por equipe enxuta | fornecedor/stack irreversível sem justificativa |

**Veto é regra de análise documental proposta**, a ratificar junto à recomendação técnica final, não bloqueio implementado nem teste de segurança executado.

## 3. ADR-C-01 — Estratégia da stack predominante (EM ANÁLISE)

**Problema:** entregar a primeira vertical com integridade e velocidade, sem duplicar ferramentas nem limitar futuras especializações justificáveis.

| Opção candidata | Potenciais benefícios a estudar | Custos/risco a considerar | Dependência de ADR-C-02/C-03 |
| --- | --- | --- | --- |
| Base TypeScript (famílias com NestJS ou alternativas) | linguagem compartilhável com ecossistema web, ferramentas de tipagem e módulos explícitos quando aplicáveis | validação runtime, bibliotecas IA, licenças, consumo e operação reais desconhecidos | clientes de persistência, semântica e versionamento do contrato |
| Base Python (famílias com FastAPI ou alternativas) | ferramentas de IA/ciência e contratos web tipados como candidatos | disciplina de separação lógica, uso de runtimes, dependências e custos desconhecidos | transações, isolamento, contratos e persistência |
| Base predominante + especialização futura | colocar ferramenta específica apenas onde houver ganho líquido | dupla cadeia de CI, segurança, observabilidade e contexto, risco de aumento de custo | fronteira extraível, ADR de exceção e budget |

**Recomendação de tecnologia:** NENHUMA. **Método D03-04 C já aprovado; produto concreto NÃO.** Fontes de capacidade para avaliação técnica futura: [NestJS Modules](https://docs.nestjs.com/modules), [FastAPI Features](https://fastapi.tiangolo.com/features/). Documentação não é benchmark.

## 4. ADR-C-02 — Persistência e proveniência (EM ANÁLISE)

**Problema:** decisões e mandatos íntegros, versões de evidência verificáveis e custo observável, com privacidade e histórico proporcional.

| Opção candidata | Pontos fortes teóricos | Riscos e custos devidos | Dependência de ADR-C-01/C-03 |
| --- | --- | --- | --- |
| Fonte transacional + histórico seletivo | integridade de mudanças críticas, histórico restrito por risco | desenho e consistência da trilha, política de retenção, migrações | clientes, testes de concorrência, contrato de alteração |
| Event sourcing amplo | reconstrução orientada a eventos | schema evolution, replay, duplicatas, projeções, direitos de exclusão, operação | versão/evento, semântica temporal, custos |
| Modelo documental com versionamento | flexibilidade por tipo de dado | relação AUT/MIS/EVD/CST, controle de acesso/consulta e integridade | transações/compensações a justificar |
| Híbrido seletivo | otimização por necessidade legítima de domínios distintos | duplicação, reconciliação, segurança e custo de suporte | contratos de projeção, fonte principal e falhas |

**Banco escolhido:** NENHUM. **D03-05 C aprova princípio, não PostgreSQL, SQLite, MongoDB, Redis, event sourcing, vetores ou filas.**

## 5. ADR-C-03 — Contratos e fronteiras entre domínios (EM ANÁLISE)

**Problema:** representar papéis e evidências sem que uma fronteira ganhe autoridade ou propriedade de dados que não lhe pertence.

| Fronteira candidata | Entrada semântica mínima futura | Saída/garantia conceitual | Restrição de segurança |
| --- | --- | --- | --- |
| AUT | ator, finalidade, mandato e contexto legítimo | decisão/negação/revogação rastreável, **não executada aqui** | só autoridade válida pode reservar ou delegar |
| MIS | objetivo, referência ao mandato, responsável | identidade de missão e estado distinto de fato comprovado | intenção não é permissão nem êxito |
| EVD | alegação de missão, fonte, versão, revisão | classificação de evidência e origem reconhecível | provas não concedem mandato |
| CST | uso, unidade, fonte de preço e comparador quando houver | custo observado/estimado/desconhecido | não atribuir economia Jev sem baseline |
| FCR | leitura autorizada das fontes dos domínios | estado com atribuição e incerteza | não elevar permissões de leitura |
| AUD/PRV | finalidade, retenção, direitos e controles | registro proporcional de legitimidade e decisão | acesso, correção, eliminação e sigilo aplicáveis |

**Semântica é candidata:** não existem payloads, mensagens, endpoints, schemas, infraestrutura, formatos de versão nem protocolos aprovados. Ainda avaliar compatibilidade, idempotência, temporalidade, revogação, replay, limites de autoridade e caminhos de erro. Se houver extração futura, manter contratos e equivalência de segurança demonstráveis.

## 6. Matriz de combinações e inconsistências (qualitativa)

As linhas representam **alternativas combinadas para estudar**, não stacks reais escolhidas.

| Conjunto candidato | Stack predominante | Estratégia de dados | Contrato | Risco central a testar |
| --- | --- | --- | --- | --- |
| S1 | TypeScript candidato | transação + histórico seletivo | fronteiras lógicas versionáveis | disciplina de isolamento, consistência e custos |
| S2 | Python candidato | transação + histórico seletivo | mesmos requisitos contratuais | integridade, concorrência e manutenção |
| S3 | TypeScript candidato | registro de eventos amplo | contratos temporais/projeções | evolução, replay, privacidade e suporte |
| S4 | Python candidato | registro de eventos amplo | contratos temporais/projeções | custos, consistência e reprocessamento |
| S5 | base predominante a decidir | híbrido seletivo | limites de propriedade claros | reconciliação, acesso e dependências |
| S6 | base predominante a decidir | documentos versionados | validação de vínculos críticos | perda de integridade, indexação e histórico |

**Não há pontuação nem vencedor.** Antes de eliminar uma alternativa, conferir dados de equipe, segurança, licenças, suporte, capacidades de cliente/LLM, tratamento legal, esforço e orçamento; quando necessário, reconhecer que a informação está indisponível.

## 7. Matriz de dependências dos ADRs

| Decisão | Precisa conhecer | Risco de decidir isoladamente | Como convergir |
| --- | --- | --- | --- |
| Stack C-01 | contratos, padrão de acesso e custo da persistência | escolha por SDK sem provar segurança e dados | comparar S1..S6 sob RQ-C01..10 |
| Persistência C-02 | invariantes AUT/MIS/EVD/CST, retenção e custo | banco eleito por preferência e não por consistência | examinar modos de falha e histórico proporcional |
| Contratos C-03 | autoridade, fontes de dados e grau de consistência | interfaces impossíveis de validar ou extrair | relacionar propriedade lógica, semântica e falhas |
| Agentes E3-03 | contratos estáveis, ferramentas disponíveis e orçamento | agentes em conflito e retrabalho superior ao ganho | plano de piloto só após autorização |
| Segurança E3-04 | fontes, acesso, privacidade e custos | perda de mandato, dados públicos ou logs inseguros | gates de veto e aceite independente |

## 8. Avaliação do custo total (sem valores fictícios)

Antes de escolher qualquer conjunto, levantar e documentar **preço, unidade, região, data, confiança e fonte** para:
1. tempo de especificar/implementar e integrar as fronteiras;
2. custos de licenças/SDKs, runtime e dependências;
3. infraestrutura, armazenamento, histórico, backup e recuperação **quando houver autorização operacional**;
4. auditoria, privacidade, migração, manutenção e operação;
5. agentes de desenvolvimento: tokens, modelos, revisão, retrabalho, conflitos e integração;
6. riscos de fornecedor, reversão e suporte;
7. custo de assegurar o mesmo nível de qualidade em todas as opções.

A medição real só poderá ocorrer após autorização de execução. **Não atribuir economia ao Jev, aumento de velocidade ou ROI sem baseline real.**

## 9. Evidências e gates ainda faltantes

- atores reais, dados autorizados e casos AC-01..20 revisados;
- acordos de privacidade/retenção, mandato, histórico, segurança e acesso;
- matriz de custo com premissas verificáveis e critérios para decisão;
- disponibilidade, versões, limites, suporte e licenças dos candidatos;
- ADRs conjuntamente coerentes, com risco de migração e plano de saída;
- avaliação separada de papéis, cotas e quantidade de agentes construtores;
- aceite do fundador da **seleção material futura**;
- autorização separada da Fase IV e solução do risco de confidencialidade do repositório (consultado público anteriormente).

**STOP CONDITION DO PACOTE: NÃO ATENDIDA.** Comparações preliminares documentadas; **ADR-C-01..03 EM ANÁLISE**. A D03-07 C já aprovou a estratégia de evidências em camadas, sem testes executados. D03-08 C APROVADA posteriormente como política DOCUMENTAL de agentes. A seleção material de tecnologias ainda depende de evidências e ratificação.

## 10. D03-07 C: a mesma escada de evidências para todos os ADRs (NOVO v0.2)

**D03-07 C APROVADA como metodologia DOCUMENTAL**, detalhada no [Plano de Evidências em Camadas v0.1](PHASE-III-EVIDENCE-LADDER-v0.1.md). Não existe dado sintético, ambiente de testes, fonte externa autorizada ou prova operacional criada.

### 10.1 Requisitos de evidências por ADR

| Decisão técnica candidata | L0: evidência disponível nesta fase | L1/L2: prova futura, somente se autorizada | L3/L4: prova real futura condicionada | Status |
| --- | --- | --- | --- | --- |
| ADR-C-01, stack | documentação oficial, critérios e análises identificadas | cenários sintéticos rotulados e testes futuros equivalentes de contrato, qualidade, manutenção e custos | métricas operacionais e disponibilidade real de fornecedores, sem presumir ganhos | EM ANÁLISE |
| ADR-C-02, persistência | invariantes de dados, classificação e comparação de riscos/custo | futuros casos de consistência, revogação, histórico seletivo e dados ausentes | proveniência, retenção e integridade de fontes reais, se autorizadas | EM ANÁLISE |
| ADR-C-03, contratos | limites AUT/MIS/EVD/CST/FCR, requisitos AC-01..20 | futuros testes de negação, versão, compatibilidade e autorização | prova legítima de que fontes e operações respeitam mandatos reais | EM ANÁLISE |

**Nenhuma nota de documentação é benchmark**. Cenários artificiais não comprovam desempenho real. Dados reais sem validação não comprovam operação correta.

### 10.2 Convergência sem falsa promoção de evidência

Ao comparar S1..S6:
- registrar **mesmo conjunto de requisitos e casos** para todas as alternativas;
- classificar a evidência de cada alegação como **L0 PLANEJADA**, **L1 SINTÉTICA**, **L2 TESTADA CONTROLADA**, **L3 FONTE REAL AUTORIZADA** ou **L4 RESULTADO OPERACIONAL VERIFICADO**, com o significado correto;
- não atribuir pontuação de confiabilidade a tecnologia por popularidade ou por possuir documentação extensa;
- distinguir custo previsto de gasto real; sem baseline legítimo, não alegar economia Jev;
- respeitar diferenças de privacidade, direitos de titulares e mandatos humanos reservados;
- evitar somar provas parciais em uma alegação de aceitação integral;
- planejar revisões independentes/proporcionais a risco, sem criar agentes ou revisão operacional nesta fase.

### 10.3 Estado antes da futura recomendação técnica

Ainda faltam ratificação dos dados e casos AC, autorização de avaliações reais quando apropriada, matriz de custos com fontes, seleção de ferramentas e fornecedores, comparação de opções sob critérios aceitos, aprovação material dos ADRs e autorização específica para implementação. **ADR-C-01..03: NÃO APROVADOS.**

**D03-08 C APROVADA POSTERIORMENTE:** autonomia graduada por risco/evidências, registrada no [Plano de Governança v0.5](PHASE-III-AGENT-GOVERNANCE-v0.5.md), sem autorizar agentes ou tecnologia. D03-09 C foi posteriormente APROVADA como método documental de avaliação elástica; D03-10 C foi posteriormente APROVADA como método documental por gates, sem ratificar tecnologia ou quantidades concretas; D03-11 C APROVADA documentalmente; D03-12 C APROVADA documentalmente; D03-13 PENDENTE.

## 11. D03-08 C — Governança da análise e construção sob ADRs convergentes (NOVO v0.3)

**Diretriz aprovada:** risco e evidências determinam futuramente níveis proporcionais de delegação e revisão para agentes de CONSTRUÇÃO, conforme [Plano de Governança v0.1](PHASE-III-AGENT-GOVERNANCE-v0.1.md). **ADR-C-01, C-02 e C-03 permanecem EM ANÁLISE, não aprovados**. Nenhum agente, modelo, stack, banco ou protocolo adotado.

| ADR técnico em análise | Natureza do risco de alteração futura | Checagem futura necessária, proporcional | Decisão atualmente vedada |
| --- | --- | --- | --- |
| **C-01 Stack** | dependências vulneráveis, custo e runtime, efeitos em contratos entre domínios | documentação de licença/segurança, testes L2 reais e revisões quando autorizados | adoção tácita de TypeScript, Python, NestJS, FastAPI, modelo ou segunda stack |
| **C-02 Persistência** | integridade de AUT, revogação, corrupção/retificação de EVD, dados protegidos | semântica e testes de concorrência, proveniência, retenção e privacidade | banco, evento ou migração selecionado sem ADR ratificado |
| **C-03 Contratos** | mudança unilateral de interface, privilégios, dados, fontes e custo | compatibilidade, autenticação, autorização, provas de versão e erro | contrato técnico, API, serviço ou protocolo implantado |

### 11.1 Critérios independentes de risco e evidência

- **R0–R3** classificam criticidade de uma alteração proposta e futura necessidade de controle;
- **L0–L4** descrevem a natureza da prova de sua execução/resultado;
- revisão própria do agente não prova independência nem aceitação;
- proteger alterações de mandato, finanças, dados privados, critérios de aceite e integridade da Carta;
- nenhum agente, executor ou orquestrador tem poder de ratificar sua própria arquitetura, gasto ou ampliação de privilégios;
- conflito entre C-01..03 retorna à comparação e à decisão humana apropriada, sem unificação forçada.

### 11.2 Custo conjunto e futura produtividade

Adicionar às comparações S1..S6 o custo de revisão de contratos, segregação de acesso, coordenação, tokens, conflitos, integração e testes de segurança. Preferir cenários com fronteiras claras, mas não assumir que múltiplos agentes ou múltiplas linguagens são mais rápidos. Medição só pode ocorrer em fase operacional autorizada, com mesma definição de pronto e baseline.

**D03-09 C APROVADA POSTERIORMENTE:** método documental de paralelismo elástico baseado em dependências e custo líquido, registrado no [Plano v0.1](PHASE-III-ELASTIC-PARALLELISM-v0.1.md). Quantidade, modelo e fornecedor seguem pendentes. **D03-10 C APROVADA posteriormente como método documental; D03-11 C APROVADA documentalmente; D03-12 C APROVADA documentalmente; D03-13 PENDENTE; Fase IV NÃO AUTORIZADA.**

## 12. D03-09 C — Paralelismo elástico em ADRs interdependentes (NOVO v0.4)

**Método ratificado:** comparar opções de stack, persistência e contratos também pelo custo de construção sequencial e paralela, dependências, integração e qualidade, **sem atribuir números nem selecionar a tecnologia**. [Plano de Paralelismo Elástico v0.1](PHASE-III-ELASTIC-PARALLELISM-v0.1.md); [Governança de Agentes v0.2](PHASE-III-AGENT-GOVERNANCE-v0.2.md).

| ADR em análise | Fatores de dependência e concorrência futura | Custo ou risco potencial a levantar | Prova ainda ausente |
| --- | --- | --- | --- |
| ADR-C-01: stack | uma linguagem principal vs. especializações, ferramentas/CI, compatibilidade de SDKs e agentes | duas toolchains, duplicação de contexto, testes e suporte | duração/custo de aceite sob condições comparáveis |
| ADR-C-02: persistência | integridade concorrente AUT/MIS/EVD/CST, revogação, mudanças e retenção | custo de transações, correção, sincronização e migração | medidas de consistência e cargas autorizadas |
| ADR-C-03: contratos | estabilidade das fronteiras, versões, consumidores, direitos de dados | conflitos de integração, compatibilidade, revisão e rollback | testes reais de contratos e falhas, quando permitidos |

**D03-09 C não decide se execução será centralizada, com serviços físicos ou quantos agentes trabalharão.**

### 12.1 Critérios de comparação de S1..S6

Para cada combinação candidata do pacote, avaliar qualitativamente:
1. capacidade de isolar unidades de trabalho sem reescrever contratos compartilhados;
2. pontos de dependência e serialização, especialmente AUT→MIS→EVD/CST→FCR;
3. segurança, retenção, rastreabilidade e legitimidade de acesso por agente;
4. custo de prompts, modelos, revisões, retrabalho, CI futuro e testes pertinentes;
5. comparação com **S0 baseline sequencial**, e hipóteses de concorrência controlada e ampliada, todas **sem números de executores**;
6. regras de STOP ao detectar falha de contrato, autorização, privacidade, custo ou evidência;
7. reversibilidade e lock-in operacional, inclusive substituição de agente/modelo.

### 12.2 Incertezas honestas

Não há benchmark, preço coletado, custo médio, timebox observado, medição de limites de modelo/cliente, qualidade testada ou ganho causal do Jev. Tabela comparativa **L0 documental**, ainda sem classificação de vencedor. O princípio de segurança pode vetar uma alternativa mesmo se futuramente houver ganho de prazo.

### 12.3 D03-10 C aprovada posteriormente como método de fechamento

A D03-10 C determina consolidar lacunas e verificações no [Plano de Convergência e Prontidão v0.3](PHASE-III-CONVERGENCE-READINESS-v0.3.md), sem antecipar escolhas nem executar pilotos. **ADR-C-01..03 continuam NÃO APROVADOS.** D03-11 C APROVADA documentalmente; D03-12 C APROVADA documentalmente; D03-13 PENDENTE.

## 13. D03-10 C — Pré-ratificação integrada, não escolha de tecnologias (NOVO v0.5)

**Governo documental:** [Matriz de Convergência e Prontidão v0.1](PHASE-III-CONVERGENCE-READINESS-v0.3.md). A D03-10 C autoriza **organizar recomendações coerentes** e apresentar deliberações materiais posteriores. **Não ratifica C-01/02/03.** Todos os pontos abaixo estão no nível **L0 DOCUMENTAL**, não TESTADOS.

### 13.1 Fichas candidatas de decisão

| ADR | Objeto específico futuro | Alternativas mantidas | Gates mínimos que devem amadurecer | Status |
| --- | --- | --- | --- | --- |
| **C-01** | linguagem/framework predominantes, exceções e caminho de saída | famílias TypeScript (incl. NestJS como exemplo) e Python (incl. FastAPI como exemplo); outras opções só se justificadas | CG-02,03,05,06,07,08,11 | **EM ANÁLISE** |
| **C-02** | tipo de fonte de verdade, histórico proporcional, integridade e retenção | transacional + trilha seletiva, eventos amplos, documentos versionados e híbridos | CG-01,03,04,06,07,08,11 | **EM ANÁLISE** |
| **C-03** | semântica, propriedade e evolução de contratos AUT/MIS/EVD/CST/FCR | contratos lógicos versionáveis e variantes futuras de interface/protocolo, não escolhidas | CG-01,02,03,04,06,07,10,11 | **EM ANÁLISE** |

**Propostas separadas, coerência conjunta:** se um ADR não preservar os invariantes de outro, nenhum será promovido a materialmente recomendado até documentar resolução e risco residual. Uma recomendação não aprova o conjunto; cada ratificação precisa identificar o objeto exato.

### 13.2 Modelo de análise comparativa qualitativa por candidato

Para cada candidato, registrar:
- requisitos da primeira vertical e critérios AC/DoR/DoD efetivamente aceitos;
- capacidade técnica **documentada** vs. capacidade **medida** (ainda nenhuma medida);
- segurança (autoridade, dados protegidos, dependências e vulnerabilidades a revisar);
- integridade de dados e compatibilidade de contrato (incluindo revogação temporal);
- manutenção, testes, ecossistema e experiências disponíveis, sem inventar disponibilidade;
- custo TCO incluindo licenças, implementação, agentes, integração, observabilidade, migração e suporte;
- contexto de agentes R0–R3, L0–L4 e S0/S1/S2/SD, sem quantidades, modelos ou preços arbitrários;
- reversibilidade, lock-in, licença, alternativa mais simples e condição objetiva de veto.

Não atribuir pontuação numérica até que critérios/pesos e fontes de custo tenham sido aceitos. A marca **DOCUMENTADO** nunca significa **APROVADO/IMPLEMENTADO**.

### 13.3 Contratos e segurança com falhas obrigatórias na comparação

| Fronteira | Condição de segurança futura a demonstrar | Tipo de prova L0 atual |
| --- | --- | --- |
| AUT→MIS | autorização e revogação legítimas, sem autoelevação de poder | regras e casos candidatos |
| MIS→EVD | relatar ≠ verificar, origem e versão vinculáveis | narrativa de contrato, não API |
| MIS→CST | estimativa, medição, preço, baseline e ausência distintos | requisitos, não custo medido |
| AUT/MIS/EVD/CST→FCR | consulta do fundador dentro de mandatos, fonte e atualização declaradas | requisitos de supervisão |
| transversal AUD/PRV | minimização, finalidade, retenção, confidencialidade e direitos | diretriz, não controles testados |

### 13.4 Decisões explícitas que ainda faltam

- escopo FCR-01..06, atores, fontes e FCR-AC após direção D03-11 C aprovada;
- critérios de aceite e atores, classificação e política de dados;
- escolhas concretas de stack, persistência e contratos por ratificação posterior;
- custos, licenças e versões verificáveis; orçamento e riscos residuais aceitos;
- modelos/ferramentas e concorrência de agentes após comparação e alçada;
- autorização separada para iniciar Fase IV e testes reais.

**STOP CONDITION DO PACOTE ADR: NÃO ATENDIDA.** Nenhum candidato venceu, e nenhuma escolha, agente, protótipo ou benchmark foi realizado.


## 14. D03-11 C: contratos candidatos do Founder Command Center progressivo (NOVO v0.6)

**Fonte:** [Plano Funcional FCR v0.1](PHASE-III-FOUNDER-COMMAND-CENTER-v0.2.md), [Matriz CG v0.2](PHASE-III-CONVERGENCE-READINESS-v0.3.md). D03-11 C **não aprova stack, banco, banco vetorial, UI, protocolo, autenticação ou implementação**.

| ADR em análise | Dependência trazida pelo FCR | Alternativas/riscos ainda abertos |
| --- | --- | --- |
| **C-01 stack** | projetar futura leitura autorizada, explicação de incerteza, suporte a supervisão e possíveis controles humanos | TS/Python e especializações condicionais, manutenção, licenças, custo de observabilidade e validação; sem vencedor |
| **C-02 persistência** | fonte de verdade AUT/MIS/EVD/CST com versão, revogação, correção e histórico proporcional para consultas | transacional+histórico seletivo, eventos completos, documentos versionados ou híbridos; integridade/retention/custo ainda comparáveis |
| **C-03 contratos** | distinguir pedido, autorização, missão, resultado relatado/verificado, origem de provas, custo e consultas FCR | consistência de mandatos temporais, revogação, estado desconhecido, autorização, autorização futura de comando, segregação de domínio |

### 14.1 Semântica do contrato de leitura FCR, sem endpoint ou esquema

**FCR←AUT:** leitura filtrada por legitimidade do sujeito; apresentação da autoridade e temporalidade da decisão sem conceder privilégio novo. **FCR←MIS:** identificador, responsável e transições com status alegado ≠ verificado. **FCR←EVD:** evidência por afirmação, fonte, versão, limites e classe L0–L4. **FCR←CST:** unidade/fonte, estimado/medido/desconhecido, baseline Jev apenas verificável. **AUD/PRV:** política de acesso, minimização e retenção. **Controle FCR→AUT/MIS:** somente necessidade conceitual futura, proibida agora, dependente de ratificação de contratos de autorização e revisão de risco.

### 14.2 Critérios de veto e TCO adicionais

Recusar candidato que dependa de elevar direitos de consulta, marque relatos como comprovação, suprima ausência de custo, não represente revogação, gere retenção injustificada ou exija infraestrutura onerosa sem benefício explicável. Comparar o custo de fontes, ingestão, verificação de consistência, privacidade, testes e observabilidade com evidências L0 atuais e preços reais somente quando apurados; sem benchmark nem score numérico fictício.

### 14.3 Gates para ratificação material ainda em aberto

CG-01, CG-02, CG-03, CG-04, CG-05, CG-06, CG-07, CG-08, CG-10 e CG-11 precisam de aceite conforme aplicável. A D03-12 C foi aprovada como política documental para **política de mandatos institucionais**, distinta dos agentes construtores da D03-08. **ADR-C-01..03 NÃO APROVADOS; E3-02 NÃO CONCLUÍDO; Fase IV NÃO AUTORIZADA.**


## 15. D03-12 C: contratos de mandato, revogação e rastreabilidade (NOVO v0.7)

**D03-12 C ratificou uma POLÍTICA DOCUMENTAL, NÃO UM ADR MATERIAL.** [Mandatos Institucionais v0.1](PHASE-III-INSTITUTIONAL-MANDATES-v0.1.md), [FCR v0.2](PHASE-III-FOUNDER-COMMAND-CENTER-v0.2.md) e [CG v0.3](PHASE-III-CONVERGENCE-READINESS-v0.3.md) estabelecem requisitos novos. Todos os três ADRs continuam EM ANÁLISE e sem vencedor.

| ADR candidato | Exigência institucional derivada de D03-12 C | Alternativas e riscos ainda em aberto |
| --- | --- | --- |
| **C-01 stack** | suportar verificação legítima de competências, validade temporal, decisões humanas, controles futuros e revisão | TypeScript/Python/frameworks apenas candidatos; licenças, segurança, manutenção e custos a comparar |
| **C-02 persistência** | registrar mandato/versão/decisão, revogação e histórico proporcional, com direitos e finalidade | abordagem transacional com histórico seletivo vs. eventos amplos vs. documentos versionados vs. híbrida; integridade e retenção a estudar |
| **C-03 contratos** | exigir origem, objeto, escopo, expiração, revogação, resultado e escalada; separar proposta de autorização efetiva | semântica de autorização e consistência entre consumidores ainda sem protocolo/schema decidido |

### 15.1 Invariantes de autoridade em exame

- **Proposta não concede autoridade** e acesso ao FCR não gera privilégio.
- **Emissor deve ter competência legitimamente verificada**, inclusive em alteração/renovação.
- **Revogação, suspensão e expiração** precisam de tratamento temporal; a política não promete reversão automática de efeitos já produzidos.
- **Subdelegação e ampliação tácita não são permitidas**; atos reservados dependem de autoridade humana.
- **Restrições de custo, dados e finalidade** condicionam qualquer ação futura; ausência de limite não equivale a autonomia ilimitada.
- **Evidências do cumprimento** devem ser independentes do autorrelato e ter classificação L0..L4 adequada.
- **Consistência entre canais** é uma questão documental futura D03-13; não se pressupõe mecanismo de sincronização ou bus de eventos escolhido.

### 15.2 Matriz de avaliação, sem preço ou decisão inventada

C-01..03 deverão ser comparados conjuntamente por segurança, consistência temporal, direitos de dados, esforço de integração, reversibilidade, histórico, custo de revisão, manutenção, agentes e fontes de evidência. Não usar uma escolha de framework/banco como solução automática de autorização. Critérios, pesos, fornecedores, benchmarks e orçamento precisam de avaliação e aprovação posterior.

**E3-02 STOP CONDITION NÃO ATENDIDA. ADR-C-01..03 NÃO RATIFICADOS. CG-01..12 PENDENTES. Fase IV NÃO AUTORIZADA. D03-13 PENDENTE.**
