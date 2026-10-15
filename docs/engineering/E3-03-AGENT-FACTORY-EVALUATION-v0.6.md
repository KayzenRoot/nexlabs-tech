# E3-03 — Estratégia Documental da Fábrica de Desenvolvimento com Agentes v0.6

**Estado:** ANÁLISE COMPARATIVA EM PLANEJAMENTO, SEM ORQUESTRADOR/AGENTES IMPLANTADOS.
**Mandato:** D03-01 A, somente documentação.
**Referências:** [Carta v1.0](../institutional/CHARTER-v1.0.md), [E3-01 v0.6](E3-01-CAPABILITY-MAP-v0.6.md), [E3-02 v0.6](E3-02-ARCHITECTURE-EVALUATION-v0.6.md).

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

**Premissas ratificadas:** D03-03 C define responsabilidades extraíveis; D03-04 C escolhe uma base principal por evidência futuramente, sem fixar linguagem ou criar processos/serviços físicos. O número de domínios **não** é o número de agentes. Ainda não existe orquestrador, agente executor ou CI implantado.

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

## 11. Produtividade dos agentes sob a estratégia D03-04 C (NOVO v0.4)

**Objetivo:** avaliar futura produtividade de agentes construtores em **uma linguagem principal** antes de decidir se múltiplas stacks e maior concorrência agregam resultado líquido. Nenhum modelo, papel definitivo, número de executores ou sistema foi selecionado.

### 11.1 Comparações documentais de fábrica de desenvolvimento

| Hipótese a avaliar | Potencial ganho | Custos e riscos de integração | Evidência que faltará medir |
| --- | --- | --- | --- |
| Uma base predominante, execução sequencial | consistência de toolchain, documentação e contratos; baseline operacional simples | pode alongar prazo quando houver tarefas independentes | tempo até aceitação e custo end-to-end |
| Uma base predominante, execução paralela controlada | compartilhamento de convenções e dependências, divisão por domínio | conflitos em contratos centrais, limites reais dos clientes, custo de review | retrabalho e custo de coordenação |
| Base predominante mais especialização pontual | biblioteca especializada quando justificável, domínio isolado | interfaces interlinguagem, testes, CI, segurança, logging e onboarding duplicados | ganho líquido suficiente para superar overhead |
| Múltiplas bases por padrão | flexibilidade local para times especializados | custo estrutural de integração elevado para equipe pequena | necessidade comprovada, não preferência estética |

**Orquestrador, revisores e executores são papéis possíveis**, não entidades já criadas. Agentes institucionais da NexLabs continuam separados da futura força construtora.

### 11.2 Critérios de produtividade comparáveis

Para qualquer alternativa de linguagem/ferramenta/agente, usar **mesma definição de pronto**: requisitos aceitos, direitos/mandatos preservados, testes realmente executados quando autorizados, evidências reproduzíveis, correções integradas e custos totais de ciclos. A comparação futura deve anotar:
- tempo total **até aceitação**, e não tempo em geração de código isolada;
- tokens de entrada/saída e custo efetivo, incluindo retrabalho, agentes de revisão e interfaces;
- custo de testes, manutenção de dependências e suporte a duas linguagens;
- quantidade de alterações rejeitadas/revertidas e divergências de contrato;
- falhas de autorização, privacidade ou proveniência, com veto a ganhos de velocidade que violem a Carta;
- impacto de rate limits, disponibilidade de modelos e compatibilidade das ferramentas reais;
- risco de perda de contexto, alinhamento entre agentes e saturação de integração.

### 11.3 Fórmulas de avaliação, NÃO números medidos

- **Custo total por entrega aceita** = soma dos custos efetivos de modelos, ferramentas, integração, verificação e correção / entregas aceitas.
- **Tempo de ciclo aceito** = instante de aceitação final − instante de início autorizado.
- **Taxa de retrabalho** = esforço de correção após integração / esforço total aceito (definir unidade antes de medir).
- **Economia Jev** = comparar medidas equivalentes do mesmo tipo de trabalho, baseline claro e qualidade equivalente, **sem atribuir ganhos ao Jev apenas por usar menos agentes**.

Nenhuma simulação com números inventados deve ser exibida como resultado da NexLabs.

### 11.4 Critérios para exceção à base predominante

Uma linguagem/stack secundária só deve ser considerada depois de documentar:
1. capacidade indispensável, biblioteca ou restrição de licença que a base predominante não atende de modo satisfatório;
2. alternativa sem segunda linguagem e respectiva limitação comprovável;
3. efeito na superfície de vulnerabilidade e nos acessos a dados;
4. manutenção, custo de contexto de agentes, CI e contratos duplicados;
5. estratégia de reversão/migração e custo de substituição;
6. aceite humano de trade-offs e eventual novo orçamento.

**D03-04 C NÃO autoriza Python+TypeScript como stack dual.** D03-05 C foi aprovada como estratégia de fonte de verdade verificável e histórico proporcional, mas não decidiu banco, event sourcing, RAG ou tecnologia concreta. O próximo gate proposto é D03-06, forma de convergência documental de escolhas técnicas.

**E3-03 ainda EM PLANEJAMENTO**, sem benchmark de agentes, ROI, limite de simultaneidade ou modelo ratificados.

## 12. D03-05 C: produtividade dos agentes sem corromper fonte de verdade (NOVO v0.5)

**Princípio:** quando diferentes agentes de construção contribuírem para o primeiro ciclo, o trabalho de um não poderá redefinir unilateralmente o significado, proveniência ou autoridade dos dados de outro. Isso é uma regra de *planejamento futuro*, não implementação de controle de acesso.

### 12.1 Particionamento candidato de estudos e mudanças futuras

| Área de estudo | Responsável conceitual | Trabalho paralelizável depois de contratos ratificados | Risco de integração |
| --- | --- | --- | --- |
| AUT/MIS | mandatos, autoridade humana, missão e transições legítimas | algumas análises podem ser independentes, mas dependências são fortes | estados de autorização contraditórios |
| EVD | semântica da prova, origem, revisão, retenção | estudo de evidências em paralelo com custos, após identidade de missão | histórico inconsistente ou reescrito |
| CST/Jev | unidade, custo observado/estimado, baseline, origem | avaliação independente de custos após contrato comum | atribuições falsas, “ausente = zero” |
| Dados e persistência | alternativas e integridade por risco | comparação documental independente TypeScript/Python e opções de armazenamento | decisões conflitantes sobre versão e fonte |
| FCR + segurança | leitura legítima, dados protegidos, explicação de limitações | validação dos requisitos desde cedo, integração posterior | acesso indevido ou conclusão sem evidência |

**Quantidade de domínios ou contratos não equivale ao número de agentes ativos.** A alocação futura depende de risco, orçamento, modelos reais e ganho líquido demonstrado.

### 12.2 Contrato de trabalho de agentes construtores proposto

Uma tarefa futura deverá documentar: objetivo e decisão origem; fronteira/arquivos sob responsabilidade; fontes canônicas imutáveis; condição de autorização; hipóteses não comprovadas; contrato de dados aplicável; testes exigidos; evidências de conclusão; limite de custo; e condição de parada. **Não criar tarefas executáveis agora.**

### 12.3 Plano comparativo contra burocracia e custo oculto

- **Baseline sequencial:** tarefa equivalente sob uma linguagem predominante futura, com aceite real.
- **Execução independente:** apenas quando contratos mínimos estiverem estabilizados e riscos de escrita concorrente controlados.
- **Integração:** tempo de revisão, resolução de conflitos e retrabalho entram no custo/tempo final.
- **Segurança:** alterações de mandatos e dados sensíveis exigem validação apropriada, mesmo se forem rápidas.
- **Escalada de concorrência:** considerar aumento só se taxa de defeitos, custo de tokens, divergência de contratos e tempo líquido forem aceitáveis.
- **Retenção mínima de contexto:** apontar para documentos da fonte de verdade, não copiar dados confidenciais para prompts e logs irrestritos.

**Jev:** economia de tokens só poderá ser atribuída se houver baseline comparável e metodologia controlada, separadamente de ganhos oriundos de paralelismo ou simplificação de contexto.

### 12.4 Gate para agentes e decisões ainda pendentes

D03-05 **não** aprovou orquestrador, agente de revisão, modelo padrão, número simultâneo, frameworks, implantação local/cloud ou conta conectada. O plano de testes de concorrência só poderá virar execução com autorização apropriada da Fase IV. Todos os dados de produtividade continuam **não medidos**.

**E3-03 EM PLANEJAMENTO.** A estratégia de fonte de verdade é aplicada como requisito de trabalho e integração futura, não como serviço atual.

## 13. D03-06 C: estratégia de construção futura sob ADRs convergentes (NOVO v0.6)

**Fonte:** [Pacote Convergente de ADRs v0.1](PHASE-III-CONVERGENT-ADR-PACK-v0.1.md). Coordenador, executores, agentes institucionais e testes são conceitos distintos. Nenhuma instalação, modelo, número de agentes, regra de merge ou ferramenta operacional foi aprovada.

### 13.1 Critério de independência do trabalho

Uma futura tarefa de agente de desenvolvimento poderá ser paralelizável **somente se** seu contrato lógico (AUT, MIS, EVD, CST ou FCR) estiver suficientemente estável, seu dono for conhecido, seu acesso for legítimo e sua saída não exigir mudança simultânea em outra área ainda não aceita.

| Atividade de engenharia candidata | Possível paralelismo futuro | Dependência | Risco principal |
| --- | --- | --- | --- |
| Revisar ADR-C-01 | análise documental em paralelo com C-02 e C-03 | requisitos compartilhados | selecionar tecnologia sem persistência adequada |
| Revisar ADR-C-02 | análise documental em paralelo com C-01 e C-03 | semântica de histórico, privacidade | violar retenção ou integridade |
| Revisar ADR-C-03 | análise documental em paralelo com C-01 e C-02 | mandatos e invariantes | impor API com segurança insuficiente |
| AUT/MIS futura implementação | trabalho inicialmente condicionado por mandato | contrato aprovado pelo fundador | conflitos em autorização |
| EVD/CST futura implementação | candidato a paralelismo após identidade MIS | fonte de dados e contratos | dados fictícios apresentados como reais |
| Integração FCR futura | após dependências e dados autorizados | AUT+MIS+EVD+CST | painel aparentemente preciso sem fontes |

As três revisões de ADR podem compartilhar uma matriz sem precisar ser três equipes ou três agentes. O estudo não estabelece quantidade de agentes simultâneos.

### 13.2 Custo líquido por combinação de stack e agentes

Futura comparação deve manter mesmo escopo, testes, restrições constitucionais e condição de aceite. Medir:
- tempo total até validação, incluindo integração e correções;
- tokens/custo de todos os modelos e passes, com preço efetivo quando conhecido;
- manutenção de contextos e dependências duplicadas entre linguagens;
- conflitos, regressões e incidentes de permissão;
- custo de monitorar e operar ferramentas, e qualidade de evidência do resultado;
- capacidade real das ferramentas instaladas e do hardware, sem presumir cotas de conta.

**Não anunciar ganho de 2x, 4x, porcentagem, ROI ou economia Jev.** Números de executores e de papéis continuam a comparar e ratificar separadamente.

### 13.3 Condição de prontidão da fábrica

Antes da Fase IV: contrato de tarefa, limites de escrita e acesso, revisão proporcional a risco, orçamentos autorizados, gate de testes, critérios de merge, isolamento e responsável legítimo. **O uso de agente não torna verdadeiro o próprio relato de conclusão.** Evidências de testes e integração são necessárias quando forem permitidos.

**E3-03 EM PLANEJAMENTO. D03-07 PENDENTE.** Não houve execução de benchmark, criação de bots ou definição final de orquestrador.
