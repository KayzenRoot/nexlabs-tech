# E3-04 — Prontidão, Riscos e Gates para Construção v0.16

**Estado:** PLANO DOCUMENTAL PRELIMINAR, NÃO É APROVAÇÃO DE FASE IV.
**Fonte de autoridade:** D03-01 A, [Carta v1.0](../institutional/CHARTER-v1.0.md), [Fase II encerrada](../design/PHASE-II-ACCEPTANCE-v1.0.md).

## 1. Escopo da prontidão

A Fase III deverá produzir condições auditáveis para iniciar implementação **depois de autorização adicional**. A fase atual não pode criar serviços, instalar dependências, executar testes, alterar visibilidade ou registrar credenciais. Critérios de prontidão dizem respeito à **qualidade dos planos**, não à segurança técnica já comprovada.

## 2. Matriz inicial de riscos a esclarecer

| ID | Risco | Situação factual/documental | Ação de engenharia futura |
| --- | --- | --- | --- |
| R-01 | Visibilidade/confidencialidade GitHub | Metadado retornou `private: false` em 2026-10-15 | Rever classificação, escopo de informação e visibilidade antes de segredos ou dados privados |
| R-02 | Acesso excessivo de agentes | Carta proíbe autoelevação de autoridade | Projetar limites de mandato, separação de funções e autorização humana |
| R-03 | Compromissos financeiros | F0–F4 são princípios, sem poderes operacionais | Orçamento, tetos, proteção de reservas e aprovação de gastos |
| R-04 | Custo de IA e paralelismo | Sem dados reais para comparar | Baseline e orçamento de tokens, custos recorrentes, limites de escala |
| R-05 | Evidência/indicadores fictícios | Identidade conceitual ainda sem telemetria | Distinguir estado sem fonte, estimado e validado |
| R-06 | Vazamento por Telegram/voz | Conexões não existentes | Requisitos de autenticação, privacidade, autorização e consentimento |
| R-07 | Dependência excessiva de fornecedor | Cartas exigem continuidade da memória | Critérios de portabilidade, exportação e substituição |
| R-08 | Arquitetura prematura | D03-02 C e D03-03 C aprovaram recorte e direção modular; stack, fronteiras técnicas e implantação continuam sem decisão | Comparar alternativas, aprovar ADRs e verificar custo/segurança antes de implementar |
| R-09 | Confusão de autonomia empresarial/construtora | Papéis distintos e futuro sistema não implantado | Separar domínios, riscos, mandatos e recursos |
| R-10 | Burocracia e retrabalho | Fundador prioriza construção eficiente | Limitar gates essenciais, reviews proporcionais e evidência útil |
| R-11 | Ausência de testes reais | Somente planejamento autorizado | Planejar testes e DoD; executar só após nova autorização |
| R-12 | Suposição de disponibilidade de IA | Modelos e quotas variáveis por cliente/conta | Verificar compatibilidade real antes de fixar uso ou preço |

**Estado:** riscos identificados para análise, não incidentes confirmados (exceto observação de visibilidade pública) nem severidades quantitativamente estimadas.

## 3. Critérios futuros de Definition of Ready (antes da Fase IV)

- Carta, síntese visual e requisitos rastreados para cada entrega aprovada.
- MVP explicitamente escolhido, limites do que não será entregue e dados necessários.
- Arquitetura/stacks justificadas em ADRs aprovados, contratos de fronteira e custos estimados.
- Segurança de identidade, autorização, privacidade e tratamento de segredos definida.
- Orçamento e mecanismos de aprovação financeira aprovados por quem possui autoridade.
- Agentes construtores e concorrência escolhidos com estratégia de avaliação, responsabilidades e controles.
- Plano de testes funcionais, integração, segurança e performance, com evidências esperadas.
- Estratégia de rollout, rollback, migração, observabilidade e incidentes proposta e revisada.
- Riscos impeditivos documentados e resolvidos ou formalmente aceitos por autoridade apropriada.
- **Autorização expressa de implementação da Fase IV** registrada separadamente.

## 4. Definition of Done futura para cada incremento de software

Quando Fase IV for autorizada, uma entrega só poderá ser aceita se:
1. escopo, PR/artefato, responsável e requisitos estiverem identificados;
2. testes proporcionais ao risco tiverem sido realmente executados e seus resultados anexados;
3. não houver vazamento conhecido de segredos nem bypass de proteções relevantes;
4. permissões e mandatos humanos forem respeitados;
5. observabilidade e impactos reais forem reportados com fontes, não estimados como fatos;
6. custo e disponibilidade de integrações externas forem descritos honestamente;
7. revisões/correções e comportamento de falha estiverem registrados;
8. aceitação final estiver fundamentada em evidências de implementação e autorizada.

**Essa DoD é uma proposta para futuros desenvolvimentos; não há teste, PR, pipeline ou implementação realizado aqui.**

## 5. Política documental de checkpoints

Após cada pacote E3, atualizar três itens, sem repetição burocrática:
- **Decidido:** escolhas ratificadas com ID e razão;
- **Pendente:** dados, comparações, riscos que faltam;
- **Gatilho de avanço:** critério objetivo para a próxima aprovação.

Em caso de bloqueio documental, corrigir o que couber no chat/GitHub antes de pedir ferramenta externa. Não relaxar direitos, segurança, escopo, orçamento ou rastreabilidade para desbloquear artificialmente.

## 6. STOP CONDITION da Fase III

**Pendência atual:** D03-02 C (recorte) e D03-03 C (direção modular evolutiva) aprovadas documentalmente; E3-01 a E3-04 ainda em planejamento, e escolhas técnicas, dados e implantação permanecem pendentes. A Fase III **não está pronta para encerramento**, e a Fase IV **não está autorizada**.

A futura ata de encerramento de engenharia deverá listar o que foi aprovado, evidência de comparações, riscos remanescentes, mecanismos de validação e autorização independente para início de código. Encerramento nunca resulta automaticamente da existência destes documentos.

## 7. Gates específicos do primeiro ciclo vertical (NOVO v0.2)

**Critério documental de prontidão** é distinto de conformidade executada ou sistema seguro em produção. O fundador aprovou a estratégia vertical, não soluções técnicas.

| Gate | Verificação exigida na futura definição pronta | Estado atual |
| --- | --- | --- |
| G-01 Autoridade | atores, limites, revogação e atos humanos reservados descritos e aceitos | EM PLANEJAMENTO |
| G-02 Missão | identidade de missão, responsabilidade, distinção entre proposta/execução | EM PLANEJAMENTO |
| G-03 Evidência | proveniência, classificação de alegação vs. fato, histórico de revisões | EM PLANEJAMENTO |
| G-04 Custo e Jev | custo observado vs. estimado vs. desconhecido; baseline explícito antes de economia | EM PLANEJAMENTO |
| G-05 Privacidade | categoria de dado, necessidade de tratamento, autorização e retenção | EM PLANEJAMENTO |
| G-06 Arquitetura | direção modular aprovada, mas alternativas/ADRs/contratos/custo de integração carecem de aceite | DIREÇÃO D03-03 C APROVADA; OUTROS PENDENTES |
| G-07 Agentes construtores | papéis/concorrência e método de benchmark justificados | PENDENTE |
| G-08 Plano de testes | casos AC-01..08 de E3-01 revisados, método de prova e DoD | EM PLANEJAMENTO |
| G-09 Segurança do repositório | avaliar `private: false` e decisão sobre classificação/visibilidade antes de dados sensíveis | PENDENTE DE TRATAMENTO |
| G-10 Autorização de implementação | fundador aceita Fase IV expressamente com escopo e riscos | NÃO AUTORIZADO |

### 7.1 Registro de risco para a vertical

1. **Falso positivo de resultado:** relato sem prova pode parecer missão executada. Mitigação proposta: diferenciação explícita das categorias e fonte.
2. **Bypass de mandato:** uma ordem legítima de consultar pode ser confundida com poder de executar. Mitigação: aprovação humana separada para atos reservados.
3. **Custo enganoso:** zero, ausente, orçamento e gasto efetivo podem ser confundidos. Mitigação: campos semânticos distintos como requisito, sem definir esquema implementado.
4. **Dependência externa prematura:** prometem-se Telegram, nuvem, VPS, voz e finanças sem conexão existente. Mitigação: interfaces apenas candidatas e escopo inicial enxuto.
5. **Concorrência mal dimensionada:** aumento de agentes cria conflitos e custo oculto. Mitigação: critérios quantitativos posteriores e papéis isolados.
6. **Publicação sensível:** GitHub reportou repositório público durante a auditoria. Mitigação: evitar segredos e decidir classificação/visibilidade em gate próprio.

### 7.2 Próximas evidências documentais necessárias

- **Concluído documentalmente:** D03-03 C como direção modular evolutiva; pendentes ADRs de topologia física, stacks, persistência, contratos e riscos de extração;
- aceitação dos casos de uso e suas informações de origem;
- cenários de negação/revogação, evidência ausente e custo indisponível;
- matriz de licenças, riscos e gastos;
- autorização separada de qualquer dado confidencial e de toda implementação futura.

**STOP CONDITION E3-04: NÃO ATENDIDA. FASE IV continua NÃO AUTORIZADA.** Nenhum gate foi validado por execução de software, teste de segurança ou benchmark.

## 8. Prontidão da arquitetura evolutiva e extraibilidade (NOVO v0.3)

**D03-03 C determina direção de projeto, não segurança ou interoperabilidade já testadas.** Antes de permitir construção de um domínio, tratar os seguintes gates no plano futuro:

| Gate de arquitetura | Critério documental a ser aceito | Situação após D03-03 |
| --- | --- | --- |
| AR-01 Mandatos | AUT é autoridade de referência e ações reservadas requerem validação explícita | princípio decidido; contrato técnico pendente |
| AR-02 Responsabilidade | MIS não confere permissão; EVD não altera autorização; CST não inventa medição | princípio decidido; implementação pendente |
| AR-03 Dados | domínio responsável, visibilidade, consistência, histórico e proteção definidos | pendente |
| AR-04 Compatibilidade | versão/revisão de contratos sem perda de proveniência ou segurança | pendente |
| AR-05 Possibilidade de extração | teste de equivalência de mandatos e dados, estratégia de rollback e custo total | pendente |
| AR-06 Fornecedores | custos, disponibilidade, licenças e risco de lock-in avaliados comparativamente | pendente |
| AR-07 Equipe de agentes | concorrência limitada por independência, permissões e capacidade real | pendente |
| AR-08 Prontidão técnica | ambientes, CI, testes e verificações reais exigidos após autorização | Fase IV não autorizada |

### 8.1 Ameaças e falhas que exigirão cobertura futura

- Elevação indireta de autoridade ao separar ou reutilizar domínio;
- Divergência entre estado de missão e afirmação de evidência;
- Dados privados compartilhados entre módulos sem necessidade e mandato;
- Efeitos duplicados ou perda de atribuição durante futura comunicação assíncrona, se for escolhida;
- Dados de custo incompletos, preços variáveis e confusão de desconhecido com zero;
- Indisponibilidade de fornecedor ou recuperação presumida sem verificação;
- Adoção de múltiplas stacks sem valor demonstrável e aumento oculto de suporte;
- Confusão entre progresso relatado por agentes construtores e entrega aceita.

### 8.2 Modelo de avaliação financeira sem números fictícios

Para cada alternativa de stack ou extração considerar:
- esforço inicial para entregar o primeiro ciclo;
- custo recorrente de execução, manutenção e armazenamento;
- custo de integração entre domínios e de permissões;
- custo de medição, registro de evidências e testes;
- custo de agentes desenvolvedores, reexecuções e merges;
- risco de lock-in e custo/viabilidade de migração;
- cenários locais, remotos e híbridos somente com estimativas fundamentadas.

Registrar hipóteses e intervalos com fontes e data; **não atribuir qualquer economia ao Jev sem baseline reproduzível**.

### 8.3 Condição de implementação

- **Repo observado público** durante auditoria de Fase II: revisar antes de qualquer dado sensível ou segredos; nenhuma mudança de privacidade efetuada neste turno.
- Fase III permite comparar e registrar opções, não usar credenciais ou ativar integrações.
- **D03-04 C APROVADA:** estratégia de uma base principal a selecionar por evidência, admitindo especializações condicionais; linguagem, framework e banco continuam não escolhidos.
- Fase IV exigirá aprovação humana específica e verificação dos gates pertinentes.

**E3-04 EM PLANEJAMENTO. Nenhuma segurança, custo, disponibilidade ou extraibilidade foi validada experimentalmente.**

## 9. Prontidão de escolha tecnológica e custos após D03-04 C (NOVO v0.4)

**D03-04 C aprova uma estratégia de seleção e não constitui aprovação técnica de produto ou segurança demonstrada.** A Fase IV permanece proibida sem autorização específica.

| Gate | Condição documental para futura ratificação de tecnologia | Estado |
| --- | --- | --- |
| ST-01 Mesma régua | critérios/definição de pronto equivalentes para TypeScript e Python | CRITÉRIOS PROPOSTOS; NÃO RATIFICADOS EM DETALHE |
| ST-02 Direitos e segurança | mandatos, privilégios, acesso, revogação, segregação e proveniência avaliados | AINDA PENDENTE |
| ST-03 Persistência | D03-05 C define fonte de verdade verificável e histórico proporcional; escolher mecanismo, política de retenção e tecnologia requer comparação | ESTRATÉGIA APROVADA; MECANISMO PENDENTE |
| ST-04 Custo integral | licenças, operação, manutenção, observabilidade, agentes e migração documentados com premissas | PENDENTE DE DADOS REAIS |
| ST-05 Base única | justificar linguagem predominante e eventuais exceções multi-stack | D03-04 C DIREÇÃO APROVADA; TECNOLOGIA PENDENTE |
| ST-06 Extraibilidade | fronteiras, controle de acesso, versionamento, testes de compatibilidade e rollback planejados | PARCIALMENTE DELIMITADO |
| ST-07 Ferramentas reais | verificar versões, cotas, limites dos modelos/clientes e política de fornecedores | PENDENTE |
| ST-08 Escopo mínimo | aceitar requisitos e fonte legítima de dados do primeiro ciclo | PENDENTE |
| ST-09 Confidencialidade | rever visibilidade `private: false` e classificação antes de informações reservadas | PENDENTE |
| ST-10 Fase IV | aceitação final e autorização humana independente | NÃO AUTORIZADA |

### 9.1 Riscos específicos da D03-04

- **R-13, preferência prematura:** inferir escolha de linguagem pela existência de bibliotecas; mitigação: matriz neutra, requisitos claros e aprovação separada.
- **R-14, custo oculto de segunda stack:** manutenção, autenticação, licenças e integração se multiplicam; mitigação: justificativa de benefício líquido e estratégia de saída.
- **R-15, conclusão falsa de benchmark:** converter características da documentação pública em medição da NexLabs; mitigação: rotular DOCUMENTADO, PROPOSTO, ESTIMADO, TESTADO ou VALIDADO conforme evidência.
- **R-16, trilha de dados inconsistente:** escolher banco por preferência sem revisar mandatos/evidências/custo; mitigação: D03-05 com critérios de integridade e rastreabilidade.
- **R-17, custos de agentes extrapolados:** calcular ROI sem disponibilidade, consumo real ou escopo equivalente; mitigação: baseline real sob autorização futura.

### 9.2 Tratamento financeiro e observabilidade

A classificação de custo será distinta para:
- **preço publicado por fornecedor**, sujeito a data, plano, região e limites;
- **estimativa da NexLabs**, derivada de hipóteses declaradas;
- **consumo efetivamente observado**, só se fonte operacional válida existir;
- **economia atribuível**, só com baseline, comparação equivalente e controle de qualidade;
- **dado indisponível**, que jamais significa zero.

Registro de telemetria por padrão como [OpenTelemetry Signals](https://opentelemetry.io/docs/concepts/signals/) é objeto de comparação, não instrumentação existente. Não captar dados sensíveis em logs sem base legítima e controles apropriados.

### 9.3 Condições de saída

D03-05 C já aprovou o princípio de fonte de verdade com histórico proporcional. É necessário ainda definir estratégia D03-06, seleção futura de stack/banco específicos após ADRs, casos de teste e segurança, política de classificação/acesso, validação de custos, papéis e limites de agentes construtores, e autorização expressa de Fase IV.

**E3-04: EM PLANEJAMENTO. Nenhum teste, benchmark, integração ou serviço foi executado, e nenhuma tecnologia foi aprovada.**

## 10. D03-05 C: proteção, integridade e custo de histórico proporcional (NOVO v0.5)

O objetivo documental é garantir que a futura fonte de verdade sirva à **soberania humana, integridade científica e prestação de contas**, sem justificar retenção ilimitada de dados ou custo de operações desproporcional.

### 10.1 Gates complementares para armazenamento e proveniência

| Gate | Condição exigida em decisão técnica futura | Estado atual |
| --- | --- | --- |
| DT-01 Fonte identificável | AUT/MIS/EVD/CST têm propriedade lógica e origem de fatos definida | princípio aprovado; detalhamento pendente |
| DT-02 Integridade | transições críticas e conflitos concorrentes não produzem autorização/êxito inventados | critérios documentados, nenhum teste |
| DT-03 Proveniência | fonte, versão, contexto e correção distinguíveis para registros relevantes | princípio aprovado, modelo pendente |
| DT-04 Minimização | finalidade legítima, privacidade, período de retenção e descarte considerados | política final pendente |
| DT-05 Acesso e sigilo | direitos de leitura/alteração, resguardo de terceiros e acesso do fundador | controles futuros não projetados nem testados |
| DT-06 Histórico proporcional | trilha suficiente ao risco, sem logging integral ou event sourcing obrigatório | direção aprovada, abordagem pendente |
| DT-07 Continuidade | cópia, migração, recuperação e integridade precisam de prova quando incluídas | nenhuma capacidade validada |
| DT-08 Custos | comparar armazenamento, operações, backups futuros, auditoria, manutenção e retenção | sem números reais e sem orçamento aprovado |
| DT-09 Extraibilidade | separação posterior mantém versões, relações, mandatos e direitos | somente diretriz modular; testes pendentes |
| DT-10 Fonte de verdade do repositório | não publicar dados pessoais/financeiros/segredos em repo identificado público | risco observado; mitigação pendente |

### 10.2 Riscos específicos a tratar antes da Fase IV

- **R-18 Histórico excessivo:** armazenar todos os eventos aumenta custo e risco de privacidade sem necessidade legítima. Mitigação: classificação e período de retenção justificáveis.
- **R-19 Histórico insuficiente:** mudanças de mandato ou de evidência ficam sem explicação. Mitigação: definir trilha mínima por criticidade.
- **R-20 Estado conflitante:** autorização revogada convive com uma projeção de missão obsoleta. Mitigação futura: contratos de consistência, validação e estado temporal.
- **R-21 Identidade falsa da evidência:** log de alteração é tomado como prova de fato externo. Mitigação: distinguir proveniência documental, autenticidade e verificação científica.
- **R-22 Custos ocultos de persistência:** complexidade de eventos, duplicação, snapshots e infraestrutura não estimados. Mitigação: TCO comparável e fontes com data.
- **R-23 Dados sensíveis em documentação/IA:** exposição de informações financeiras ou privadas. Mitigação: classificação, mínimo necessário e reavaliação da visibilidade GitHub antes de registrar conteúdo reservado.
- **R-24 Perda de direitos em migração:** extração/arquivamento futuro desrespeita retenção legal ou eliminação legítima. Mitigação: decisões de privacidade e revisão jurídica quando aplicável.

### 10.3 Critérios finais que ainda faltam

Exigir plano aceito de: dados mínimos, autorização e revogação, classificação de histórico, retenção e eliminação legítima, contratos de proveniência, custos verificáveis, ADR de tecnologia, plano de migração e teste futuro de consistência. **Não inferir disponibilidade, segurança, backup ou recuperação a partir da aprovação conceitual.**

**D03-06 C APROVADA:** comparação conjunta de ADRs técnicos de stack, persistência e contratos, todos ainda EM ANÁLISE. **E3-04 permanece EM PLANEJAMENTO; Fase IV não autorizada.**

## 11. D03-06 C: gates de decisão para pacote convergente (NOVO v0.6)

**Referência:** [Pacote Convergente de ADRs v0.1](PHASE-III-CONVERGENT-ADR-PACK-v0.1.md); não substitui [Carta Institucional v1.0](../institutional/CHARTER-v1.0.md).

| Gate | Exigência antes de seleção material e prontidão | Status |
| --- | --- | --- |
| CV-01 Escopo | mesmo primeiro ciclo, mesmos dados, mandatos e aceite AC-01..20 para todas as combinações | proposta, aceitação final pendente |
| CV-02 Riscos | veto fundamentado para falha constitucional, acesso indevido ou histórico enganoso | critérios propostos, sem teste |
| CV-03 Stack | comparar TypeScript/Python e exceções pelo mesmo custo total/risco | análise, sem vencedor |
| CV-04 Persistência | preservar fonte de verdade, integridade e retenção proporcional | estratégia aprovada, tecnologia pendente |
| CV-05 Contratos | evitar elevação de AUT, integridade de MIS/EVD/CST e consultas FCR legítimas | semântica candidata, implementação pendente |
| CV-06 Interdependências | ADR-C-01..03 conjuntamente consistentes e com migração/reversibilidade | pacote aberto, sem aprovação |
| CV-07 Custos | período, fonte, unidade, incerteza, operações, revisão e tokens de agentes | números ainda não coletados |
| CV-08 Privacidade | classificação de dados e visibilidade do repositório antes de conteúdo sensível | pendente; repo informado público na auditoria |
| CV-09 Evidências | D03-07 C: evidências L0–L4, sintético rotulado e dados externos apenas com autorização; testes futuros exigem prova de execução | ESTRATÉGIA APROVADA, NENHUMA PROVA OPERACIONAL |
| CV-10 Implementação | autorização independente para Fase IV e testes em ambiente aprovado | NÃO AUTORIZADO |

### 11.1 Riscos adicionais a registrar

- **R-25, decisão combinada opaca:** um pacote integrado pode ocultar escolhas individuais; mitigação: C-01..03 mantêm seus próprios riscos, alternativas e estado de ratificação explícita.
- **R-26, falso consenso:** inferir que compatibilidade conceitual prova compatibilidade operacional; mitigação: classificar ANALISADO vs. TESTADO, sem promover ambos automaticamente.
- **R-27, custo de complexidade:** ferramentas/event sourcing/poliglotismo impostos pelo desenho sem TCO; mitigação: alternativas simples e reversíveis obrigatórias na comparação.
- **R-28, agente como auditor de si mesmo:** validação insuficiente ou resultados relatados sem prova; mitigação: checks independentes quando disponíveis, critérios de aceitação e autoridade do fundador.
- **R-29, privacidade em exemplos:** informações reais sensíveis usadas indevidamente em documentos e prompts; mitigação: minimizar dados, não publicar segredos, rotular cenários hipotéticos.
- **R-30, risco de fornecedor:** presumir modelos e preços atuais sem verificação; mitigação: registrar disponibilidade, contratos, licenças e custos com fonte e data quando avaliar materialmente.

### 11.2 STOP CONDITION vigente

E3-04 **não está concluído**: faltam dados, estimativas confiáveis, aprovação do escopo e de critérios detalhados, proposta convergente madura, decisões materiais de stack/persistência/contratos, papéis de agentes e sua concorrência, política de segurança/confidencialidade, plano de testes e autorização independente de Fase IV. **D03-07 C APROVADA** somente como estratégia documental; **D03-08 C e D03-09 C APROVADAS somente documentalmente; D03-10 C APROVADA documentalmente; D03-11 C APROVADA documentalmente; D03-12 C APROVADA documentalmente; D03-13 C APROVADA documentalmente** para política de canais FCR/Chief of Staff.

Nenhum teste, protótipo, ambiente, integração ou sistema foi implementado neste pacote documental.

## 12. Gates da D03-07 C: prova progressiva, segurança e consentimento (NOVO v0.7)

**Referência:** [Plano de Evidências em Camadas v0.1](PHASE-III-EVIDENCE-LADDER-v0.1.md). Esses gates são **planos de exigências futuras**, não controles ativados ou auditoria técnica concluída.

| Gate | Regra de prontidão para futuras validações | Estado |
| --- | --- | --- |
| EV-01 classificação | evidência rotulada L0–L4 e distinção real/sintética/estimada/desconhecida | princípio aprovado, execução ausente |
| EV-02 autorização | mandatos humanos e atos reservados validados antes de qualquer ação real | regras conceituais, sem acesso real |
| EV-03 dados fictícios | cenários L1 claramente identificados, separados de resultados reais | não criados, Fase IV não autorizada |
| EV-04 teste controlado | L2 requer versão, ambiente, método, resultados realmente executados e revisados | não executado |
| EV-05 fonte externa | L3 exige legitimidade, privacidade, limites da fonte e verificação de conexão | nenhuma integração |
| EV-06 resultado efetivo | L4 requer prova apropriada ao impacto real, sem confiar em autoavaliação do agente | nenhum resultado operativo |
| EV-07 dados e retenção | mínimo necessário, direito de acesso e descarte/retificação legal aplicável | análise pendente |
| EV-08 custo/receita | preço, consumo, gasto e comparador Jev distinguíveis | números reais indisponíveis |
| EV-09 contrato e histórico | versões/correções preservadas, sem alegar autenticidade por log isolado | ADRs não aprovados |
| EV-10 implantação | aprovação expressa de Fase IV, ambiente e permissões, antes de software e testes | NÃO AUTORIZADO |

### 12.1 Novos riscos e mitigação documental

- **R-31, simulação enganosa:** resultados sintéticos mostrados como operação; exigir marcação clara de nível e fonte.
- **R-32, promoção indevida:** teste controlado usado para afirmar integração externa; exigir prova própria de L3.
- **R-33, fonte real incorreta:** autenticidade de origem confundida com precisão factual; validar qualidade e limite da fonte.
- **R-34, prova autodeclarada:** agente assina sua própria aceitação sem checagem; exigir evidência e autoridade apropriada.
- **R-35, dados privados fora de escopo:** cenários ou fontes inserem informações confidenciais no repositório público; não criar exemplos reais sensíveis e preparar política de dados.
- **R-36, custo inflado ou fictício:** custos estimados e indicadores Jev anunciados como medidos; controlar origem, preço, período e baseline.
- **R-37, retenção excessiva de logs:** registrar tudo como prova, sem finalidade e direitos; aplicar D03-05 C e minimização proporcional.

### 12.2 Fronteira inequívoca com a Fase IV

Nem D03-07 C nem o plano de evidências autorizam mocks, fixtures, repositórios de dados, CI, APIs, modelos, scripts, testes, conexões, credenciais ou operações. O risco já registrado de visibilidade pública do repositório deve ser tratado antes de quaisquer dados confidenciais. A futura comprovação precisa de plano aceito, limites de risco, proteção de dados e autorização humana independente.

**E3-04 EM PLANEJAMENTO, STOP CONDITION NÃO ATENDIDA. Fase IV NÃO AUTORIZADA. D03-08 C APROVADA documentalmente; D03-09 C APROVADA documentalmente; D03-10 C APROVADA documentalmente; D03-11 C APROVADA documentalmente; D03-12 C APROVADA documentalmente; D03-13 C APROVADA documentalmente.**


## 13. Gates documentais da D03-08 C (NOVO v0.8)

**D03-08 C não é autorização de execução.** Os gates são requisitos de planejamento para futura revisão por risco, conformidade e evidências [L0–L4](PHASE-III-EVIDENCE-LADDER-v0.1.md); referência [Governança de Agentes v0.1](PHASE-III-AGENT-GOVERNANCE-v0.1.md).

| Gate | Condição mínima a revisar futuramente | Estado |
| --- | --- | --- |
| AG-01 mandato | finalidade, identidade e alçada legítima verificáveis | princípio documental, nenhuma permissão concedida |
| AG-02 classificação | risco R0–R3 justificado por reversibilidade/impacto | escala candidata, thresholds não decididos |
| AG-03 escopo | domínio, arquivos/dados e dependências permitidos | contrato técnico e acesso pendentes |
| AG-04 revisão | check e segregação de funções proporcionais, sem aceitar autorrelato | nenhuma automação instalada |
| AG-05 prova | L0 não se apresenta como L2/L3/L4; resultados futuros exigem execução real | somente documentos L0 |
| AG-06 custos | limite/mandato financeiro e fontes de gasto definidos | nenhum orçamento nem custo observado |
| AG-07 privacidade | repositório público, acesso a segredos, retenção e direitos tratados | risco aberto |
| AG-08 integração | proteção de contratos e alterações concorrentes, merge só com condições reais | nenhuma CI/merge instalada |
| AG-09 interrupção | condições de STOP, conflito, revogação, rollback e intervenção humana | critérios documentais |
| AG-10 autoridade final | atos reservados e Fase IV exigem decisão humana separada | implementação NÃO AUTORIZADA |

### Riscos complementares em análise

- **R-38, autonomia excessiva:** tarefa com escopo limitado muda autorização ou financeiro; mitigar com mandatos e revisões.
- **R-39, revisão fictícia:** agente aprova a própria entrega como se fosse independente; exigir evidência e autoridade pertinentes.
- **R-40, custo oculto de coordenação:** concorrência aumenta tokens/retrabalho sem reduzir tempo de aceite; exigir baseline comparável.
- **R-41, permissão propagada:** coordenação transmite credenciais/dados além do necessário; restrição e classificação antes de executar.
- **R-42, políticas sem execução:** afirmar proteção de branch, gates e testes apenas por constarem em documentos; classificar L0.
- **R-43, perda de rastreabilidade:** múltiplos escritores alteram fronteiras e fonte de verdade sem controle; exigir versionamento e compatibilidade.

Os antigos riscos e critérios permanecem vigentes. A escolha D03-08 **não elimina** decisões técnicas pendentes, testes efetivos, critérios legais ou necessidade de proteção de informações.

**E3-04 EM PLANEJAMENTO. Fase IV NÃO AUTORIZADA. D03-09 C APROVADA documentalmente; D03-10 C APROVADA documentalmente; D03-11 C APROVADA documentalmente; D03-12 C APROVADA documentalmente; D03-13 C APROVADA documentalmente.**


## 14. D03-09 C: critérios de prontidão para elasticidade e custo líquido (NOVO v0.9)

A aprovação da política de concorrência variável é **somente documental**. Antes de qualquer teste de agentes ou escalada de concorrência será preciso autorização operacional separada e comprovação de que o risco não foi ampliado indevidamente.

| Gate | Condição necessária numa futura implementação autorizada | Estado |
| --- | --- | --- |
| EP-01 mandatos | fonte de autoridade, escopo, revisão R0–R3 e revogação | PLANEJADO, sem permissão real |
| EP-02 contratos | interfaces e dependências estáveis, responsáveis por mudanças | ADR-C-01..03 ainda não aprovados |
| EP-03 baseline | custo e prazo sequencial com mesmo AC/DoD e fonte L2+ real | SEM MEDIÇÃO |
| EP-04 elasticidade | S1/S2 condicionados à independência, ganho líquido e custos reais | APENAS MÉTODO APROVADO |
| EP-05 segurança | nenhum bypass de autorização, branch/checks, segredo ou privacidade | CONTROLES NÃO IMPLANTADOS |
| EP-06 evidência | L0–L4 utilizados com semântica adequada, sem relato como prova | SOMENTE DOCUMENTAÇÃO L0 |
| EP-07 finanças | limite aprovado, preços/consumo reais e orçamento rastreável | NÃO APROVADOS |
| EP-08 integração | custo de merge/review/retrabalho incluído; conflito implica revisão ou STOP | SEM TESTES |
| EP-09 capacidade | cliente/modelos/disponibilidade/cotas validados no ambiente legítimo | INDISPONÍVEL PARA MEDIÇÃO |
| EP-10 entrada na Fase IV | autorização humana específica, requisitos e controles aceitos | **NÃO AUTORIZADO** |

### Riscos adicionais

- **R-44, saturação do integrador:** acrescentar agentes aumenta fila de integração/revisão.
- **R-45, paralelismo ilusório:** múltiplos autores editam o mesmo contrato e aumentam retrabalho.
- **R-46, custo de tokens oculto:** custo de coordenação, refações e validação omitido no cálculo.
- **R-47, escala que enfraquece controle:** acelerar merges ou delegar atos reservados para cumprir prazo.
- **R-48, baseline não equivalente:** comparar modelos/escopos diferentes e alegar ganho sem causalidade.
- **R-49, dados sensíveis propagados:** compartilhamento desnecessário de segredos ao escalar agentes.

Mitigação proposta: contratos aceitos, segregação de dados, revisão proporcional, medição total e política de pausa/redução. Nenhum gate foi testado e nenhum desses riscos foi eliminado empiricamente.

**E3-04 EM PLANEJAMENTO. D03-10 C APROVADA documentalmente; D03-11 C APROVADA documentalmente; D03-12 C APROVADA documentalmente; D03-13 C APROVADA documentalmente para política dos canais FCR/Chief of Staff. Fase IV NÃO AUTORIZADA.**


## 15. D03-10 C: auditoria de prontidão e STOP CONDITION consolidada (NOVO v0.10)

**Fonte:** [Matriz de Convergência CG-01..CG-12 v0.1](PHASE-III-CONVERGENCE-READINESS-v0.7.md). D03-10 C aprovou **processo de fechamento**, não a prontidão técnica; esta seção não valida hardware, CI, permissões, segurança ou operação.

### 15.1 Inventário de bloqueios reais

| Classe de bloqueio | Evidência existente | Falta para encerramento | Resultado |
| --- | --- | --- | --- |
| AUT/escopo/aceite | direção vertical D03-02 C e casos AC candidatos | atores, mandatos e MVP final ratificados; AC/DoR/DoD aceitos | **ABERTO** |
| Stack/persistência/contratos | ADR-C-01..03 EM ANÁLISE e S1..S6 propostas | comparações com fontes/custos + atos separados de ratificação | **ABERTO** |
| Segurança/dados | Carta, governança R0..R3 e princípios de privacidade | classificação de dados, políticas de acesso/retention, riscos revistos | **ABERTO** |
| Evidências/testes | D03-07 C e plano L0..L4 documentados | critérios de aferição e validações futuras realmente autorizadas | **ABERTO** |
| Custo/viabilidade | taxonomia TCO e Jev, nenhum dado medido | fonte/preço/data, orçamento humano, riscos de suporte | **ABERTO** |
| Agentes | D03-08 C e D03-09 C, S0..S2/SD conceituais | papéis/limites ratificados, ferramentas, modelos, número e custeio | **ABERTO** |
| Confidencialidade | GitHub observado público em auditoria anterior | política e revisão da visibilidade antes de dados sensíveis | **ABERTO** |
| Fronteira de implementação | Carta exige autorização expressa | Fase IV não autorizada; nenhuma execução permitida | **NÃO AUTORIZADA** |

### 15.2 Segurança e governança

As salvaguardas documentadas incluem menor privilégio, reserva de mandatos humanos, proteção de terceiros, rastreabilidade proporcional, revogação, dependências, revisão proporcional por risco e STOP para falha material. **Nenhuma dessas salvaguardas está tecnicamente instalada ou testada** por ter sido escrita aqui. Não publicar credenciais, dados privados, custos sigilosos ou informações financeiras restritas no repositório público.

### 15.3 DoR/DoD da fase e critérios para eventual ata

**DoR para ratificação material:** candidatos e alternativas com requisitos aceitos, fontes e custos verificáveis, impacto na Carta, benefícios/riscos, trade-offs explícitos, veto/privacidade, compatibilidade entre ADRs e decisão humana identificada.

**DoD documental E3-04:** risco e privacidade revisados com políticas aceitas; matriz de gates com critério e prova; TCO demonstrado com premissas e fonte; preparação de execução reversível, critérios de teste, segurança e observabilidade; dependências e condições de Fase IV claras; aceite formal independente. **Nenhuma dessas condições pode ser presumida cumprida pela existência da matriz.**

**STOP CONDITION E3-04: NÃO ATENDIDA.** CG-07..12 permanecem pendentes; D03-11 C aprovou apenas a diretriz; D03-12 C aprovada como política documental; D03-13 C APROVADA documentalmente. A Fase III **não foi encerrada** e a Fase IV **NÃO AUTORIZADA**.


## 16. D03-11 C: gates de soberania do Founder Command Center (NOVO v0.11)

**Direção do recorte aprovada, prontidão NÃO aprovada.** O FCR futuro deverá ser demonstravelmente confiável quanto à fonte, à autoridade e ao estado desconhecido; existência de documentos L0 não implica controle de acesso, dados reais, proteção legal, testes ou funcionalidade.

| Gate FCR | Critério para aceite DOCUMENTAL futuro | Situação |
| --- | --- | --- |
| **FCG-01** mandatos | ator, poder/limite/revogação e reserva humana definidos | PENDENTE |
| **FCG-02** missão | pedido, execução relatada e efeito verificado distinguíveis | PENDENTE |
| **FCG-03** prova | fonte, nível L0..L4, contestação e atualização declarados | PENDENTE |
| **FCG-04** custo | unidade/tempo/origem e medido/estimado/desconhecido separados | PENDENTE |
| **FCG-05** direitos | FCR não amplia acesso por agregação; dados e terceiros protegidos | PENDENTE |
| **FCG-06** ação humana | intervenções e revogações previstas com alçada, sem ações implementadas | PENDENTE |
| **FCG-07** risco | controle proporcional e STOP para falta de mandato, evidência ou orçamento | PENDENTE |
| **FCG-08** integração | dependências de Telegram, voz, finanças e VPS explícitas sem prometer disponibilidade | PENDENTE |
| **FCG-09** ADRs/custo | C-01..03, TCO, privacidade e revisão técnica separados para ratificação | PENDENTE |
| **FCG-10** fase | gates e STOP aceitos, Fase IV autorizada independentemente | NÃO AUTORIZADA |

### 16.1 Riscos específicos adicionais

- **R-50, aparência de comando sem poder:** projetar futuras ações do fundador sem contrato/autorização efetivos; não apresentar botão ou comando como existente.
- **R-51, falsa transparência:** exibir custo/missão/evidência sem fonte/tempo/qualidade; declarar desconhecido.
- **R-52, abuso de agregação:** painel institucional atravessar controle de acesso, dados financeiros privados ou limites legais; revisar direitos.
- **R-53, revogação desatualizada:** apresentar uma autorização inativa como válida; exigir temporalidade e precedência.
- **R-54, expansão precoce:** conectar Telegram/voz/VPS/finanças antes de garantir fonte, direitos, custo e autorização; manter como requisito futuro.

**Gates FCG-01..10 são especificações L0 NÃO VALIDADAS, não controles técnicos operacionais. D03-11 C foi somente decisão de prioridade. CG-01..12 seguem sem aceite final, E3-04 STOP CONDITION NÃO ATENDIDA, Fase IV NÃO AUTORIZADA, D03-12 C APROVADA documentalmente; D03-13 C APROVADA documentalmente.**


## 17. D03-12 C: novos gates de mandato e revogação (NOVO v0.12)

O fundador aprovou uma **política documental**, não controles em funcionamento. [Mandatos v0.1](PHASE-III-INSTITUTIONAL-MANDATES-v0.1.md), [CG v0.3](PHASE-III-CONVERGENCE-READINESS-v0.7.md).

| Gate candidato | Critério exigido antes de eventual execução futura | Estado |
| --- | --- | --- |
| **MG-01 origem** | emissor/titular competente e mandato verificáveis | NÃO ACEITO |
| **MG-02 escopo** | finalidade, atos permitidos/proibidos e mínimo privilégio | NÃO ACEITO |
| **MG-03 tempo** | início/expiração e tratamento de versões/relógio | NÃO ACEITO |
| **MG-04 revogação** | efeito de suspensão, término e ações em trânsito definido | NÃO ACEITO |
| **MG-05 risco** | ações humanas reservadas, reversibilidade, escalada | NÃO ACEITO |
| **MG-06 finanças** | unidade/custo/teto aprovado sem inferir valor | NÃO ACEITO |
| **MG-07 privacidade** | consentimentos quando aplicáveis, finalidade e retenção | NÃO ACEITO |
| **MG-08 evidência** | MC-01..14 e L0..L4 validados conforme autorização | SOMENTE L0 DOCUMENTADO |
| **MG-09 separação** | construtores sem autoridade institucional automática | DIRETRIZ DOCUMENTAL, NÃO CONTROLE |
| **MG-10 implantação** | autorização humana Fase IV, testes e fontes legítimos | **NÃO AUTORIZADA** |

### Riscos específicos acrescentados

- **R-55:** mandato sem competência verdadeira, ocultação de titular.
- **R-56:** revogação/expiração atrasada ou estado temporal conflitante.
- **R-57:** autopermissão, subdelegação ou canal ampliando alçada.
- **R-58:** efeito irreversível declarado cancelado sem prova.
- **R-59:** ausência de orçamento e custo desconhecido interpretados como permissão ilimitada.
- **R-60:** evidência sintética/autorrelato confundidos com resultado institucional real.
- **R-61:** retenção excessiva ou exposição de dados protegidos no repositório/canal.

Mitigar documentalmente com fontes, revogação, STOP, revisão humana e classificação de evidência; não afirmar testes, controles reais nem autorização.

**MG-01..10 não são gates tecnicamente implantados. CG-01..12 continuam SEM ACEITE FINAL. E3-04 STOP CONDITION NÃO ATENDIDA. D03-13 C APROVADA documentalmente. Fase IV NÃO AUTORIZADA.**

## D03-13 C — Gates documentais adicionais para canais (2026-10-17)

A aprovação de D03-13 C **não fecha** qualquer gate. [Política de Canais v0.1](PHASE-III-CHANNEL-GOVERNANCE-v0.3.md) especifica CH-AC-01..12 (PROPOSTOS L0). **Dependências necessárias antes de implementação futura:**
1. Identidade, papéis, alçadas e mandatos autorizados; canal jamais aumenta privilégios.
2. Fonte de verdade, versões/ordem de revogação, atraso, conflito, indisponibilidade e tempo.
3. Contrato explícito que distinga pedido/recebimento de autorização/execução/resultado comprovado; duplicidade/replay e ações em trânsito.
4. Privacidade, minimização, relatórios exportados e proteção de terceiros; revisar visibilidade pública do repositório antes de dados protegidos.
5. Critérios CH-AC reconciliados com MC-01..14, FCR-AC-01..12 e demais AC sem redundância; plano de testes e evidência real futura L2..L4 quando autorizados.
6. Custos/TCO com fontes, limites financeiros ratificados, fornecedores/licenças, segurança e autorização individual por canal.
7. D03-14 C foi aprovada exclusivamente como POLÍTICA DOCUMENTAL; não presumir controles operacionais.

**CG-01..12 SEM ACEITE FINAL; E3-04 STOP CONDITION NÃO ATENDIDA; E3-01..04 EM PLANEJAMENTO; ADR-C-01..03 EM ANÁLISE; Fase IV NÃO AUTORIZADA.** Nenhum CI, teste, bot, conta, segredo, integração ou deployment decorreu desta decisão.

## D03-14 C — Plano de assurance documental integrado (2026-10-17)

**Sem validação operacional:** [Política IC v0.1](PHASE-III-IDENTITY-CONSISTENCY-v0.2.md) define IC-I01..14 e critérios IC-AC-01..12 como PROPOSTOS L0.

| Cenário futuro a demonstrar, quando autorizado | Critério de segurança e prova exigível |
| --- | --- |
| conta de canal válida, mas mandato ausente | impedir nova ação relevante; separar identidade de alçada |
| mesmo pedido recebido duas vezes / fora de ordem | não atribuir efeito duplicado sem verificação independente |
| revogação no meio do ato | bloquear novas ações e examinar efeitos em trânsito sem retroatividade presumida |
| relógio divergente, fonte indisponível, sessão encerrada | INCONCLUSIVO ou negação segura, revalidação antes de novos atos |
| relatórios exportados com privacidade ou dados de terceiros | minimização, finalidade, acesso e retenção legítimos |
| FCR/Telegram/voz apresentam versões distintas | conflito explicitado; fonte legítima e escalada humana quando reservada |
| custo de validação não medido | AUSENTE/ESTIMATIVA fundamentada, nunca economia Jev inventada |

**Gates:** CG-01..12 e FCG/MG não aceitos; ADR-C-01..03 EM ANÁLISE; E3-01..04 EM PLANEJAMENTO e suas STOP CONDITIONS NÃO ATENDIDAS. Critérios IC-AC/CH-AC/MC/FCR-AC são indexados conforme a D03-15 C, método documental APROVADO, mas seguem dependentes de revisão e aceite material independentes. Sem testes L2+, CI de implementação, modelos, tokens, contas, chaves, integrações, infraestrutura ou Fase IV autorizada.

## D03-15 C — Assurance de não regressão dos critérios consolidados

**DIRETRIZ DOCUMENTAL APROVADA em 2026-10-17:** [Núcleo de Aceitação v0.1](PHASE-III-ACCEPTANCE-CORE-v0.2.md) estabelece KAC-01..12 e SAC por domínio como proposta L0, sem aceite material de nenhuma evidência.

| Verificação documental futura antes de ratificar critérios | Evidência mínima exigida |
| --- | --- |
| cobertura de identificadores históricos | AC/MC/FCR-AC/CH-AC/IC-AC/RG/EL/IM mapeados individualmente e lacunas visíveis |
| nenhuma obrigação eliminada | distinções SAC preservam risco, fonte, dono, direito, reversibilidade e ato humano reservado |
| regra de prova proporcional | estado L0 atual explícito, L1..L4 sem alegar testes/execuções |
| critério especializado por canal | contratos, privacidade, temporalidade e aprovação individual permanecem independentes |
| dono e aprovação | dono funcional proposto ≠ autoridade nomeada; gates CG/FCG/MG aceitos independentemente |
| teste/risco/STOP | desenho não promove aceitação nem Fase IV; validação operacional posterior requer novo mandato |

**Não foi executado** teste de código, identidade, canal, API, segurança, benchmark ou CI neste pacote documental. **CG-01..12, FCG/MG e STOP CONDITIONS de E3-01..04 NÃO ATENDIDOS; ADR-C-01..03 EM ANÁLISE; D03-16 C APROVADA documentalmente; Fase IV NÃO AUTORIZADA.**

## D03-16 C — Plano de assurance L0 por risco e evidência da vertical

**MÉTODO DOCUMENTAL APROVADO, evidência operacional NÃO COLETADA.** [Fatia v0.1](PHASE-III-RISK-FIRST-VERTICAL-v0.1.md) descreve V-01..05, VSC-01..10, criticidade qualitativa candidata, owners FUNCIONAIS PROPOSTOS e cruzamento KAC/SAC/CG. Aceitar cenário, evidência, gate ou implementação ainda exige processo e autoridade separados.

| Prioridade documental candidata | Cenários sem testes | Pacote/gate a manter ABERTO |
| --- | --- | --- |
| crítica V-RC | VSC-01/02/03/04/05/09 | E3-01/E3-04, AUT/MIS/EVD/FCR; CG-01/02/07/09/10/11/12 |
| alta V-RA | VSC-06/07/08/10 | E3-01/02/04; CG-03/04/06/08/09/11 |
| moderada/baixa V-RM/V-RB | observabilidade/forma e conveniências complementares | revisar sem superar direitos ou promover gates |

**DoR:** mapear risco, fonte, responsável e critérios históricos/KAC/SAC. **DoD:** revisão documental e aceites futuros de responsáveis competentes para cada domínio e CG, com limitações L0 claras. Nenhum DoD material foi satisfeito, e não existem testes L2–L4 realmente realizados nem controles implantados. O plano de provas da implementação fica condicionado à Fase IV devidamente autorizada.

**E3-04 EM PLANEJAMENTO; CG-01..12/FCG/MG SEM ACEITE; ADR-C-01..03 EM ANÁLISE; STOP CONDITIONS NÃO ATENDIDAS; D03-17 PENDENTE; Fase IV NÃO AUTORIZADA.**
