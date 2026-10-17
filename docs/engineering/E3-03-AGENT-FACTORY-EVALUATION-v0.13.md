# E3-03 — Estratégia Documental da Fábrica de Desenvolvimento com Agentes v0.13

**Estado:** ANÁLISE COMPARATIVA EM PLANEJAMENTO, SEM ORQUESTRADOR/AGENTES IMPLANTADOS.
**Mandato:** D03-01 A, somente documentação.
**Referências:** [Carta v1.0](../institutional/CHARTER-v1.0.md), [E3-01 v0.10](E3-01-CAPABILITY-MAP-v0.12.md), [E3-02 v0.10](E3-02-ARCHITECTURE-EVALUATION-v0.12.md).

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

**E3-03 EM PLANEJAMENTO. D03-07 C APROVADA para planejamento de evidências; D03-08 C APROVADA posteriormente; D03-09 C APROVADA documentalmente; D03-10 C APROVADA documentalmente; D03-11 C APROVADA documentalmente; D03-12 C APROVADA documentalmente; D03-13 C APROVADA documentalmente.** Não houve execução de benchmark, criação de bots ou definição final de orquestrador.

## 14. D03-07 C: evidência de produtividade dos futuros agentes (NOVO v0.7)

A metodologia de [evidências em camadas](PHASE-III-EVIDENCE-LADDER-v0.1.md) é mandatória para **planejar** avaliações futuras: L0 requisitos documentados; L1 cenários fictícios rotulados; L2 testes executados em ambiente futuro autorizado; L3 fontes reais com acesso legítimo; L4 resultados operacionais devidamente comprovados. **Hoje há apenas documentação L0; não foram criados cenários ou testes.**

### 14.1 Distinguir trabalho alegado e entrega aceita

| Afirmação de agente de desenvolvimento | Tipo de evidência necessária futuramente | Conclusão vedada sem prova |
| --- | --- | --- |
| “Implementei o módulo” | código real autorizado, diff, CI/testes efetivos e revisão/aceite | não é entrega aceita pelo relato sozinho |
| “Testes passaram” | registro fiel de execução, versão, ambiente, comandos/resultados | não inferir aprovação de testes por texto gerado |
| “Reduzi tempo/custo” | baseline comparável, custo total de tokens, revisão e integração, qualidade equivalente | não creditar Jev, modelo ou concorrência sem causalidade |
| “Dados reais foram integrados” | acesso autorizado, proveniência, limites e verificação de conexão efetiva | não promover L2 a L3 por simulação |
| “A empresa ganhou produtividade” | efeitos aceitos e medidos sob condições equivalentes | não declarar L4 a partir da contagem de mensagens ou PRs |

### 14.2 Avaliação comparativa de agentes somente no plano

- Propor tarefas futuras equivalentes por fronteira AUT/MIS/EVD/CST/FCR, sem criar work orders executáveis;
- planejar mensuração de tarefas sequenciais e paralelas **até aceitação final**;
- registrar custos de modelo, revisão, integração, conflitos e segurança, todos ainda desconhecidos;
- separar modelo e papel: número de tarefas, número de personas e concorrência real não são a mesma métrica;
- exigir controles humanos em mudanças de permissão, privacidade, finanças, merges reservados e atos irreversíveis;
- considerar reavaliação de conformidade após alteração de modelo, fonte ou contrato de dados;
- preservar diversidade de revisões técnicas quando proporcionais ao risco, sem afirmar independência de verificador inexistente.

### 14.3 Gate para D03-08

A decisão **D03-08 C APROVADA** definiu posteriormente política DOCUMENTAL de autonomia proporcional a risco e evidências; o método de dimensionamento D03-09 C foi APROVADO documentalmente; D03-10 permanece PENDENTE. Não pressupor múltiplos agentes, número padrão, modelo, ferramentas, cloud/local, orçamento ou permissão de execução. Isso não altera o mandato do Chief of Staff institucional nem a Carta v1.0.

**E3-03 NÃO CONCLUÍDO.** Sem agente instalado, teste executado, dado sintético criado ou ganho mensurado.


## 15. D03-08 C: política da fábrica de agentes construtores (NOVO v0.8)

Aprovação expressa da **autonomia graduada por risco e evidências**. [Plano de Governança v0.1](PHASE-III-AGENT-GOVERNANCE-v0.1.md) é a referência detalhada. Nenhum modelo, agente, orquestrador, quantidade ou ferramenta instalada.

### 15.1 Papéis como responsabilidades, não instâncias

**Planejar/coordenação**, **execução delimitada**, **verificação**, **integração** e **análise de custo** são papéis candidatos. Uma mesma instância poderia desempenhar papéis distintos, mas isso não demonstra revisão independente, especialmente em tarefas de alto risco. Os agentes da NexLabs como instituição continuam separados dos agentes que futuramente escreveriam seu software.

### 15.2 Matriz de risco para delegação e verificação futura

| Risco candidato | Tratamento de autonomia a considerar | Evidência de aceite futura |
| --- | --- | --- |
| R0 documental | simplificar fluxo, preservar fonte, decisões e histórico | L0 e revisão documental legítima |
| R1 técnico contido | delegação estritamente delimitada e reversível | diff, testes L2 realmente executados, check pertinente |
| R2 contrato/segurança | validação especializada, análise de consumidores e mandatos | critérios AC, proteção de dados, provas específicas e autoridade |
| R3 reservado/irreversível | nenhuma decisão humana reservada é substituída por agente | autorização legítima, auditoria e evidência de execução real |

Estes **não são níveis de acesso implementados**, nem valores legais fixos, nem justificativa para dispensar controles de risco R0/R1.

### 15.3 Orquestração e paralelismo ainda candidatos

Futuro coordenador poderia analisar dependências entre AUT→MIS→EVD/CST→FCR e impedir alterações de contratos compartilhados em paralelo sem revisão, mas isso é apenas definição de responsabilidades. Qualquer número de agentes depende de **D03-09 e comparação futura**, e não deve ser inferido de cinco domínios ou cinco papéis.

Plano de produtividade comparativa, sem execução: baseline sequencial; concorrência incremental somente após contratos estáveis; observar tempo até entrega aceita, tokens e custo efetivo, revisão, retrabalho, conflitos, qualidade e falhas. Limites financeiros, ferramentas/modelos disponíveis, cotas, permissões e revisão de privacidade precisam ser validados.

### 15.4 STOP CONDITION

Missão futura exige escopo, dono, fonte de autorização, critérios de aceite, risco justificado, dados permitidos, dependências, teto de custo aprovado, validação e parada. Se faltar autorização, se a fonte for incerta ou se houver conflito estrutural, **não presumir sucesso nem aprovação**.

**E3-03 EM PLANEJAMENTO; D03-08 C aprovada como direção, D03-09 C APROVADA documentalmente; D03-10 C APROVADA documentalmente; D03-11 C APROVADA documentalmente; D03-12 C APROVADA documentalmente; D03-13 C APROVADA documentalmente. Nenhum agente criado nem produtividade medida.**


## 16. D03-09 C: método do paralelismo elástico (NOVO v0.9)

**Direção ratificada:** concorrência deve ser avaliada por **dependências reais, tempo até entrega aceita, custo líquido e qualidade**, preservando D03-08 C (autonomia por risco), L0–L4 (evidências) e mandatos humanos. Referências: [Paralelismo Elástico v0.1](PHASE-III-ELASTIC-PARALLELISM-v0.1.md), [Governança v0.2](PHASE-III-AGENT-GOVERNANCE-v0.2.md).

### 16.1 Comparação planejada sem números

| Cenário | Intenção para avaliação FUTURA | Condição de preferência |
| --- | --- | --- |
| S0 sequencial | referência de custo/qualidade/tempo | baseline honesto, com DoD equivalente |
| S1 concorrência contida | paralelizar apenas frentes independentes após contratos estabilizados | menor tempo de aceitação com custo/risco aceitáveis |
| S2 expansão condicional | aumentar frentes elegíveis quando houver demanda e recursos | ganho marginal ainda positivo após integração |
| SD redução/STOP | reduzir ou interromper concorrência ao detectar falha material | proteger autoridade, fontes e integridade antes de velocidade |

**S0–S2 são rótulos de cenários, NÃO quantidades de agentes**. A execução, cliente, hardware, orçamento, quotas, modelos, ferramentas, número de fluxos simultâneos e orquestrador seguem pendentes.

### 16.2 Futura orquestração como responsabilidades, não software

Um coordenador hipotético classificaria risco, identificaria dependências AUT→MIS→EVD/CST→FCR, validaria contratos e limites de dados, verificaria tarefas candidatas à concorrência, enviaria propostas de review e produziria prestação de contas **com evidências**. Isso não confere permissão de escrever, abrir PR, fazer merge, usar API ou intervir em finanças.

Planejar proteção de contratos compartilhados: **um responsável lógico por fronteira de alteração**, bloqueio de dependência não cumprida, revisão proporcional, critérios de rollback e opção de serializar tarefas em caso de conflito. Os modelos não podem ratificar seus próprios novos poderes ou declarar sucesso sem prova.

### 16.3 Fórmulas conceituais de comparação, sem calcular resultados

- **Prazo real**: início legitimamente autorizado até aceite final, incluindo revisão, integração, regressão e correção.
- **Custo líquido de trabalho aceito**: custos reais de modelos/ferramentas e integração/revisão/retorno divididos por entregas aceitas, na mesma unidade.
- **Ganho líquido futuro**: diferença versus S0, após contabilizar overhead e qualidade; não atribuir ganho ao Jev sem baseline causal separado.
- **Custo marginal de escalada**: comparação da concorrência adicional versus benefício adicional mensurado, mantendo contratos e segurança.

### 16.4 Critérios de STOP CONDITION

Sem dados operacionais não declarar melhor número, ganho, preço, modelo ou ROI. Falta de autorização, contrato não estabilizado, dado sensível inseguro, custo não aprovado, testes ausentes, revisão insuficiente ou resultado inconclusivo impede promover a entrega.

**E3-03 EM PLANEJAMENTO, D03-09 C concluída apenas documentalmente e D03-10 C APROVADA documentalmente; D03-11 C APROVADA documentalmente; D03-12 C APROVADA documentalmente; D03-13 C APROVADA documentalmente. Sem agentes criados e sem benchmark executado.**


## 17. D03-10 C: fábrica de agentes e gates de prontidão (NOVO v0.10)

**Fonte:** [Governança documental v0.3](PHASE-III-AGENT-GOVERNANCE-v0.3.md), com critérios AGF-01..AGF-08; [Matriz CG-01..CG-12](PHASE-III-CONVERGENCE-READINESS-v0.4.md). A fábrica está **EM PLANEJAMENTO**, sem modelo, número de agentes, cliente, orquestrador, orçamento, CI, execução ou benchmark aprovados.

### 17.1 Gate por função candidata

| Papel (não instância) | Limite e dependência | Prova futura necessária |
| --- | --- | --- |
| Coordenador | missão com mandato, fronteiras e dependências aceitas | tarefas legítimas, evidências/STOP e conflitos identificados |
| Executor | alterar apenas contratos/domínios permitidos | diff e testes realmente executados após autorização |
| Verificador | critérios de aceite, riscos, privacidade e independência proporcionais | resultados verificáveis, não autorrelato |
| Integrador | versões, regressões, qualidade e custo, com proteção de branch quando houver | CI/revisão realmente existente, não documento declarativo |
| Analista de custo | preços, tokens, retrabalho, modelo e fonte do gasto | comparação com baseline de mesmo escopo e qualidade |

### 17.2 DoR/DoD da fábrica candidata

**DoR:** unidade de trabalho definida, autoridade, dono, dependência, contrato estável, risco R0..R3, evidência L0..L4 pretendida, limite financeiro/ferramenta ratificados, revisor, dados permitidos e STOP. Um papel pode existir sem instância de agente correspondente.

**DoD documental:** matriz de papéis e segregação/autoridade aceita; critérios de custo e qualidade completos; S0/S1/S2/SD definidos sem número final; condições de paralelismo ligadas a dependências; modelo de revisão, dados e direitos aceito; reversibilidade e interrupção previstas; ausência de stack/modelo/cliente tratada como pendência em vez de preenchimento fictício.

**DoD operacional permanece futuro e proibido nesta fase**. Não inferir qualidade de agentes a partir de prompts exemplares ou quantidade de PRs.

### 17.3 Custo líquido, throughput e segurança

Comparação futura e somente se autorizada deve usar **tempo de início autorizado até aceite final**, gastos medidos de modelos, ferramentas, revisão, retrabalho, integração, privacidade e manutenção; determinar efeito marginal de ampliar concorrência contra S0, com qualidade equivalente. Jev exige baseline e atribuição independente. Sem métrica real e orçamento, nenhum ganho percentual é declarado.

### 17.4 Estado e bloqueios

**CG-07/08/09/10/12 PENDENTES; STOP CONDITION E3-03: NÃO ATENDIDA.** Modelos, agentes, número simultâneo, ferramentas, cotas e custos não aprovados. O Command Center/Chief of Staff institucional e a fábrica de construção permanecem distintos. D03-11 C APROVADA documentalmente; D03-12 C APROVADA documentalmente; D03-13 C APROVADA documentalmente.


## 18. D03-11 C: distinguir factory construtora de operações institucionais (NOVO v0.11)

D03-11 C define experiência de **Founder Command Center institucional**, mas a D03-08 C rege apenas agentes **construtores**. As duas categorias não herdam escopo, modelos, permissões ou orçamento entre si. [Governança v0.4](PHASE-III-AGENT-GOVERNANCE-v0.4.md) e [FCR v0.1](PHASE-III-FOUNDER-COMMAND-CENTER-v0.2.md).

| Fluxo de trabalho FUTURO hipotético | Construtores | Institucionais |
| --- | --- | --- |
| missão/escopo | tarefa de engenharia com AC/DoR/DoD, quando Fase IV autorizada | missão de negócio e mandato próprio após D03-12 e aprovação posterior |
| verificação | revisão de artefato, diffs, contratos e CI executada | fontes/evidências de resultados corporativos, atos humanos reservados |
| custo | tokens, modelos, ferramentas e integração do desenvolvimento | custo de execução empresarial e alçadas financeiras legítimas |
| risco | R0..R3, delegação D03-08 C | mandato institucional distinto, sem alçada automaticamente transferida |
| interação com FCR | jamais fazer do FCR aprovação de PR sem permissão | FCR lê/explica, planeja intervenção humana, não executa ações agora |

**Produtividade:** comparar S0/S1/S2/SD sob baseline até entrega **aceita** e custos totais de agentes, incluindo futura dificuldade de implementar FCR-01..06, risco de contrato/autorização, privacidade, revisão e integração. Não atribuir economia a Jev sem baseline; nenhum modelo, número ou orçamento escolhido.

**Gate:** antes de qualquer teste futuro, exigir papéis autorizados, risco legítimo, controles realmente instalados e evidências L2 quando aplicáveis, sem confundir discurso com execução. FCR-AC são requisitos documentais L0. **E3-03 STOP CONDITION NÃO ATENDIDA; CG-07/08/09/10/12 pendentes; D03-12 C APROVADA documentalmente; D03-13 C APROVADA documentalmente.**


## 19. D03-12 C: autoridade institucional ≠ autonomia da construção (NOVO v0.12)

Agentes CONSTRUTORES continuam regidos pelos princípios D03-08/09 C de delegação de engenharia por risco, revisão e custo líquido. Agentes INSTITUCIONAIS só poderiam futuramente atuar com mandato empresarial limitado, legítimo e revogável segundo D03-12 C. A **fábrica de software não pode emitir poderes institucionais**. [Governança v0.5](PHASE-III-AGENT-GOVERNANCE-v0.5.md) e [Mandatos v0.1](PHASE-III-INSTITUTIONAL-MANDATES-v0.1.md).

| Comparação de responsabilidades | Engenharia/construção | Missão institucional |
| --- | --- | --- |
| Artefato base | tarefa de desenvolvimento, DoR/DoD e contrato | mandato empresarial legítimo, propósito, escopo, prazo e limites |
| Prova | diff, CI, revisão e testes somente se executados | fonte de resultado externo, direitos e prova L0..L4 |
| Interrupção | política de STOP por segurança, custo, falha e contrato | suspensão/revogação temporal com revisão de efeitos |
| Responsável pela autorização | alçada legítima de desenvolvimento | autoridade competente conforme Carta/lei |
| Indicador econômico | custo total até artefato aceito | consumo/custo/efeito legítimos por missão |
| Segredos e direitos | repositório e dados autorizados | dados institucionais e de terceiros com acesso específico |

A eventual criação de agentes construtores para implementar AUT/FCR/mandatos exigirá outra autorização operacional. MC-01..14 são critérios potenciais para especificar tarefas, **não testes rodados**. Não confundir papel de coordenador de engenharia com Chief of Staff institucional.

**DoR/DoD adicionais candidatos:** escopo e papel de cada população, fronteira de responsabilidades, limites financeiros e de acesso, independência de revisão e plano de rollback/STOP claros, sem escolher modelos, clientes, orquestrador, instâncias ou concorrência.

**E3-03 EM PLANEJAMENTO; CG-07/08/09/10/12 sem aceite. Sem agentes, economia Jev, custos medidos ou benchmarks. D03-13 C APROVADA documentalmente. Fase IV NÃO AUTORIZADA.**

## D03-13 C — Canal institucional não autoriza agentes construtores (2026-10-17)

A política de canais neutros de D03-13 C vale para futuras missões **INSTITUCIONAIS**, em continuidade a D03-12 C. Agentes **CONSTRUTORES** seguem regime de planejamento de engenharia D03-08/09 C; não podem instalar Telegram, voz, autenticação ou FCR por iniciativa própria, elevar mandatos institucionais ou alegar autorização da Fase IV.

Em qualquer futura divisão de trabalho, avaliar dependências AUT/MIS/EVD/CST/FCR e mudanças de direitos e contratos antes de paralelizar; atos reservados exigem revisão humana legítima. CH-AC-01..12 são critérios candidatos para canais futuros, não tarefas operacionais liberadas. [Política de Canais v0.1](PHASE-III-CHANNEL-GOVERNANCE-v0.1.md).

**E3-03 EM PLANEJAMENTO.** Nenhum modelo, agente, quantidade, ferramenta, token, orçamento ou benchmark aprovado. CG pendentes; STOP CONDITION NÃO ATENDIDA; Fase IV NÃO AUTORIZADA; D03-14 PENDENTE.
