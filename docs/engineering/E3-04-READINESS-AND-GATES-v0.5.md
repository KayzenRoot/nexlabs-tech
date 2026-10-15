# E3-04 — Prontidão, Riscos e Gates para Construção v0.5

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

**D03-06 PENDENTE:** escolha documental da forma de convergência para stack, persistência e contratos. **E3-04 permanece EM PLANEJAMENTO; Fase IV não autorizada.**
