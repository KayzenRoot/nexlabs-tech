# E3-03 — Estratégia Documental da Fábrica de Desenvolvimento com Agentes v0.3

**Estado:** ANÁLISE COMPARATIVA EM PLANEJAMENTO, SEM ORQUESTRADOR/AGENTES IMPLANTADOS.
**Mandato:** D03-01 A, somente documentação.
**Referências:** [Carta v1.0](../institutional/CHARTER-v1.0.md), [E3-01 v0.3](E3-01-CAPABILITY-MAP-v0.3.md), [E3-02 v0.3](E3-02-ARCHITECTURE-EVALUATION-v0.3.md).

## 1. Duas populações distintas

1. **Agentes institucionais da NexLabs (futuro produto/organização):** Chief of Staff, núcleos, pesquisa, negócios, finanças, operações etc.; competências, mandatos e número **não definidos**. São requisitos institucionais futuros, não trabalhadores de engenharia atualmente operantes.
2. **Agentes de construção (futura força de desenvolvimento):** papéis técnicos de planejamento, implementação, testes, revisão e integração. A existência conceitual destes papéis não implica instâncias criadas ou ferramentas em execução.

**Não converter a lista de papéis em número de agentes simultâneos.** Uma mesma instância pode desempenhar mais de um papel; algumas funções podem ser determinísticas, humanas ou automatizadas quando autorizadas.

## 2. Papéis possíveis, ainda não aprovados como configuração

| Papel candidato | Responsabilidade | Entrega futura mensurável |
| --- | --- | --- |
| Coordenador | Ler dependências e decompor missões sem alterar autoridade | Tarefas pequenas, proprietários claros e condição de parada |
| Analista de requisitos | Reduzir ambiguidades, mapear decisões e fontes | Critérios de aceite e escopo rastreáveis |
| Engenheiro de arquitetura | Avaliar trade-offs e contratos | ADRs propostos, revisados e aprovados |
| Executor de implementação | Alterar código de escopo isolado (apenas na Fase IV) | Diff verificável e testes |
| Validador automatizado | Verificações determinísticas apropriadas (apenas quando autorizadas) | Resultados de testes reproduzíveis |
| Revisor técnico | Examinar risco, diferenças e requisitos | Achados com evidências e severidade fundamentada |
| Integrador | Preparar compatibilidade entre contribuições autorizadas | Merge verificável, conflitos resolvidos, histórico claro |
| Analista de custo/observabilidade | Estimar e depois medir gasto, tokens e retrabalho | Comparação com baseline, sem percentuais inventados |

Os papéis são alternativas organizacionais; **o fundador mantém decisões reservadas**. Não criar aprovações fictícias de agentes.

## 3. Opções de simultaneidade a comparar no futuro

| Hipótese | Benefício esperado a testar | Risco a medir |
| --- | --- | --- |
| Execução sequencial / um executor | Menos conflitos e menor overhead; serve como baseline | Maior tempo em tarefas independentes |
| Coordenação e dois executores paralelos | Possível redução de prazo em pacotes independentes | Consumo adicional de tokens e integração |
| Coordenação e até quatro executores paralelos | Possível ganho com tarefas bem isoladas | Saturação de contexto, rate limits, conflitos, custo e retrabalho |
| Concurrency variável por missão | Ajustar número de executores ao custo-benefício observado | Maior complexidade decisória e previsibilidade |

**Nada aprovado como quantidade padrão.** Esses são tratamentos a comparar, não promessas de throughput, benchmark executado ou disponibilidade de ferramentas. Contar simultâneos não é o mesmo que contar papéis, prompts ou modelos distintos.

## 4. Método de medição futura (somente plano)

Após autorização de implementação e ambiente apropriado, comparar tarefas de natureza e complexidade semelhantes:
- baseline sequencial, depois concorrência baixa, depois maior apenas quando justificado;
- tempo total até aceitação, não apenas conclusão nominal dos agentes;
- tokens de entrada/saída e **custo total** (inclusive reexecuções, integração, ferramentas e serviços);
- falhas de testes, defeitos encontrados depois da integração e alterações revertidas;
- quantidade de conflitos de escrita, dependências cruzadas e tempo perdido em revisão;
- qualidade do resultado conforme DoD idêntico e critérios estabelecidos;
- disponibilidade efetiva de conta, cliente de IA, modelo, limites e permissões.

Exemplo **de fórmula, não resultado medido**:
`Ganho líquido de prazo = 1 - (tempo aceito em paralelo / tempo aceito sequencial)`.
**Não apresentar porcentagens nem ROI sem dados realmente coletados.** Resultados de tarefas não equivalentes devem ser marcados como inconclusivos.

## 5. Redução de custo de tokens e retrabalho

- Contexto mínimo suficiente, com links para fontes canônicas em vez de colar todo o histórico.
- Tarefa com escopo, entradas, arquivos permitidos, dependências, aceitação e condição de parada.
- Reuso de decisões e resultados verificáveis, com controle de mudanças e proveniência.
- Papel de coordenação encaminha a ferramenta/modelo adequado ao risco e ao custo **após verificar disponibilidade e política aplicável**.
- Reservar raciocínio profundo e múltiplas passagens para decisões com risco/ambiguidade material.
- Preferir lints e verificações determinísticas quando forem adequados; não substituir validações obrigatórias.
- Evitar que dois executores alterem arquivos críticos em paralelo sem estratégia explícita de isolamento.
- Não comprar serviços ou ativar ferramentas sem autorização financeira apropriada.

## 6. Governança enxuta

Propõe-se um modelo de mudanças isoladas, revisão proporcional a risco e controles automáticos mínimos quando a engenharia estiver autorizada. A existência de um único administrador humano não exige conta revisora adicional se o sistema puder manter evidências e aceitação adequada. **Não desabilitar segurança, controle de acesso, testes ou checks necessários para ganhar velocidade.**

Todo conjunto de trabalho terá: contexto, dono responsável, arquivos/áreas permitidos, dependências, verificação, artefatos de evidência e condição explícita de parada. Merges automáticos futuros seriam condicionados a proteção efetiva e autorização, não promessa de merges irrestritos.

## 7. Diferenças entre coordenação e autonomia empresarial

O orquestrador construtor não é Chief of Staff institucional nem soberano. A autonomia dos futuros agentes **corporativos** exige mandatos diferentes dos agentes **desenvolvedores**. Registrar cada uma dessas concepções em documentos distintos quando o desenho avançar.

## 8. Pendências E3-03 e STOP CONDITION

- Definir recursos e ferramentas realmente disponíveis para desenvolvimento e limites reais dos modelos.
- Escolher modelo de orquestração e isolamento só após comparar alternativas e custo.
- Aprovar política de autorização e gastos máximos, adequando-a à Carta.
- Planejar benchmarks experimentais permitidos apenas em fase com execução autorizada.
- **Parcialmente delimitado:** papéis candidatos alinhados ao recorte D03-02 C, ainda sem fixar número de agentes.
- Concluir plano de avaliação com critérios, thresholds a aprovar e estratégia de rollback.

**E3-03 NÃO CONCLUÍDO.** Nenhum agente, workflow GitHub, sistema de orquestração ou benchmark foi criado/rodado.

## 9. Otimização documental da construção do primeiro ciclo D03-02 C (NOVO v0.2)

### 9.1 Fatiamento por responsabilidades, não por número de bots

O primeiro ciclo exige **quatro fronteiras candidatas** para planejamento de trabalho futuro: **autoridade**, **missão e delegação**, **proveniência/evidências**, **medição e custo**. Segurança, contratos e aceitação atravessam todas. Isso não impõe quatro executores, quatro serviços ou quatro repositórios.

| Área candidata | Trabalho de engenharia futuro | Dependências essenciais | Critério de entrega futura |
| --- | --- | --- | --- |
| AUT | Regras de quem pode pedir, autorizar, negar, revogar | Carta, tipos de atores e mandatos | atos reservados não executáveis sem autorização |
| MIS | Identidade de missão, intenção, responsável, limites | AUT para ações legitimadas | missão e autorizações rastreáveis |
| EVD | Fonte, histórico, afirmação, contradição, revisão | vínculo com MIS | alegação não confundida com prova |
| CST | Proveniência de tokens, preço e custo observado/estimado | dados realmente disponíveis | desconhecido ≠ zero; Jev sem baseline ≠ economia |
| CROSS | Auditoria, segurança, contratos e qualidade | definição comum das quatro áreas | testes futuros de conformidade e privacidade |

Essas fronteiras são **uma proposta de divisão de trabalho**, não contratos de código nem modularização ratificada.

### 9.2 Estratégias alternativas de desenvolvimento a comparar

| Organização candidata | Vantagem provável | Custo/risco |
| --- | --- | --- |
| Executor único sequencial | coordenação simples; baseline comparável | pode alongar tempo em tarefas independentes |
| Execução paralela por responsabilidade | potencial ganho entre AUT/EVD/CST se contratos estiverem estáveis | integração frequente e conflitos de fronteiras |
| Paralelismo adaptativo por dependência | concorrência variável segundo gargalos | orquestração e previsão de custo mais complexas |

**Nenhuma alternativa selecionada e nenhum número definitivo aprovado.** O piloto citado na proposta histórica de dois executores, e uma expansão hipotética para quatro, continuam hipóteses a validar, não metas obrigatórias. Agentes institucionais da NexLabs são categoria separada dos agentes construtores.

### 9.3 Medição e gate de paralelismo (futuramente, somente sob autorização da Fase IV)

Usar tarefas comparáveis e mesmo Definition of Done para medir:
- **Tempo total aceito:** do início até merge/validação final, não o instante em que o agente diz “feito”;
- **Custo total:** tokens, modelos, ferramentas, integração e reexecuções, mais revisões humanas quando relevantes;
- **Qualidade:** falhas, regressões, retrabalho pós-integração, cobertura relevante de testes;
- **Contenção:** conflitos de edição, esperas, dependências bloqueadas;
- **Produtividade líquida:** entregas aceitas por unidade de gasto e tempo.

**Hipótese de comparação, não experimento executado:** sequencial (referência) vs concorrência baixa vs concorrência maior, sem escalar até que o custo de integração deixe de dominar e os resultados sejam auditáveis. Modelos, limites reais e preço precisam ser verificados no ambiente autorizado.

### 9.4 Estratégia anti-retrabalho e governança proporcional

1. Requisitos e contratos comuns aprovados **antes** de entregar arquivos compartilhados a agentes distintos.
2. Pacotes de execução isoláveis, com dono único de cada área e critério de aceite verificável.
3. Contexto suficiente **referenciando documentos canônicos**, evitando retransmitir todo histórico irrelevante.
4. Revisão orientada a diffs e criticidade, sem inventar certificação nem exigir um revisor humano adicional não existente.
5. CI proposto somente para Fase IV: checks determinísticos de integridade, segurança, contratos e regressões; nunca dispensar controles mandatórios.
6. Registrar custo por rodada e comparação com baseline antes de afirmar economia do Jev ou aceleração.
7. Encerrar tarefas apenas com verificação final e evidência, não por total de tokens consumidos ou duração de prompt.

### 9.5 Pontos ainda abertos

- **Concluído como direção:** D03-03 C aprovada: núcleo modular evolutivo com fronteiras extraíveis, sem topologia física definida.
- Verificação de disponibilidade real dos clientes, ferramentas, modelos, limites de concorrência e regras de acesso.
- Seleção justificada de papéis e quantidade depois de avaliar custo e dependências.
- Critérios de segurança, orçamentos e autorização de Fase IV antes de testar qualquer piloto.

**STOP CONDITION E3-03: NÃO ATENDIDA.** Não houve agente criado, benchmark executado, teste de paralelismo ou economia comprovada.

## 10. Plano de construção modular evolutiva após D03-03 C (NOVO v0.3)

**Premissa ratificada:** separar responsabilidades antes de criar processos ou serviços físicos. O número de domínios **não** é o número de agentes. Ainda não existe orquestrador, agente executor ou CI implantado.

### 10.1 Critério de elegibilidade para futura execução paralela

| Trabalho futuro candidato | Independência documental | Pode avançar simultaneamente em fase de construção? | Dependência-chave |
| --- | --- | --- | --- |
| Padrões de autoridade e mandatos (AUT) | Requisitos constitucionais especificáveis isoladamente | após critérios comuns aprovados | Carta, direitos e ator legítimo |
| Estado e escopo de missão (MIS) | Fluxo conceitual definido parcialmente | só após contrato de decisão de autoridade | AUT |
| Proveniência de evidência (EVD) | Semântica analisável separadamente | possivelmente, após contrato mínimo de vínculo de missão | MIS |
| Medição e custo (CST) | Comparadores e semântica de dados analisáveis isoladamente | possivelmente, após identidade de missão, unidades e fontes | MIS e fonte de custo |
| Visão de supervisão (FCR) | Exige agregação e autorização prévia | mais tarde, após semântica dos quatro domínios | AUT, MIS, EVD, CST |
| Segurança e validação | Requisitos transversais | pode ser planejada em paralelo, mas não delegada sem evidência | todas as fronteiras |

A expressão “possivelmente” é **hipótese a testar**, não estimativa de ganho.

### 10.2 Modos de distribuição de trabalho a comparar na Fase IV, caso autorizada

**M0: uma sequência de desenvolvimento**, como baseline em tarefa de aceitação real.

**M1: dois fluxos de domínio condicionados a contratos**, com coordenador somente quando necessário. Não equivale a três agentes permanentes.

**M2: concorrência maior dirigida por independência demonstrada**, limitada por cotas, custos, conflitos, regressões e capacidade de integração; o número concreto ainda exige aferição.

**M3: concorrência variável por janela e prioridade**, adotável apenas se benefício líquido comparável superar overhead operacional.

Nenhum modo aprovado como configuração real. A seleção de modelos de IA, versões, ferramentas e quantidade de agentes simultâneos permanece condicionada à verificação efetiva dos ambientes e à autorização financeira/operacional correspondente.

### 10.3 Riscos concretos do paralelismo a serem evitados

- Alterações simultâneas do mesmo contrato de autoridade podem invalidar todos os domínios;
- Integrar leitura FCR antes de provar AUT e EVD pode aparentar dados verificados que não existem;
- Evidência artificial ou indicadores simulados não podem ser utilizados como se fossem operação real;
- Múltiplos agentes com acesso ao mesmo segredo ou repositório público podem ampliar risco de divulgação;
- Grande volume de PRs não mede trabalho aceito nem tempo líquido;
- Dois agentes que propõem alterações opostas exigem validação de contrato e revisão humana nos atos reservados.

### 10.4 Pacote mínimo de execução futura, ainda não criado

Cada unidade de trabalho futura deverá especificar: **responsável, dependência e fronteira, permissão para alterar, objetivo verificável, testes que deverão passar, limite de custo autorizado, evidência de integração e STOP CONDITION**. Documentar diferenças e reuso de contexto sem alegar memória técnica/RAG disponível.

### 10.5 Comprovação de velocidade e custo

Indicadores que deverão ser medidos após autorização: tempo sequencial vs. paralelo **até aceitação final**, tempo de integração, custo de tokens+ferramentas, regressões, retrabalho, integridade da segurança e qualidade. **A economia Jev requer baseline próprio**, e não poderá ser confundida com economia por paralelismo de agentes.

**E3-03 EM PLANEJAMENTO.** Não fixar quantidade final de executores, orquestrador, modelo padrão, limite de concorrência ou porcentagem de ganho sem comparação e autorização.
