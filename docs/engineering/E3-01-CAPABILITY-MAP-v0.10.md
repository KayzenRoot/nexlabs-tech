# E3-01 — Mapa de Capacidades e Escopo do Primeiro Incremento v0.10

**Estado:** D03-02 C, D03-03 C, D03-04 C, D03-05 C, D03-06 C e D03-07 C APROVADAS como diretrizes documentais. Nenhum caso executado, fonte externa conectada, stack, persistência, contrato técnico ou topologia aprovados.
**Autorização:** D03-01 A permite documentar requisitos e alternativas.
**Fontes:** [Carta Institucional v1.0](../institutional/CHARTER-v1.0.md), [Síntese da Fase II](../design/PHASE-II-CANONICAL-SYNTHESIS-v1.0.md), [adendos completos v0.2](../design/VISUAL-CONCEPT-DECISIONS-v0.2.md), [registro D03 v0.10](PHASE-III-DECISION-REGISTER-v0.10.md).

## 1. Objetivo

Delimitar **a menor entrega futura capaz de provar valor para o fundador**, preservando mandatos, conhecimento verificável, custo, segurança e expansão. Este documento **não declara serviços existentes**, integrações disponíveis, dados acessíveis ou prioridade aprovada. A D03-02 C escolheu o **princípio de recorte vertical verificável**; o alcance material e os requisitos de aceite da primeira entrega continuam em planejamento.

## 2. Classes de requisitos

| Tipo | Significado | Exemplo de fonte |
| --- | --- | --- |
| CONSTITUCIONAL | Exigência de lei, direitos, soberania humana e Carta v1.0 | Fundador mantém decisões reservadas |
| FUNDADOR-EXPRESSO | Intenção funcional aspiracional registrada nos adendos D02-AD-01..05 | Founder Command Center, Telegram, voz, Jev, custos, finanças, VPS |
| QUALIDADE | Atributo necessário à confiabilidade da futura construção | segurança, desempenho, rastreabilidade, portabilidade |
| PROPOSTA | Possível solução candidata sem aprovação | recorte vertical, módulos específicos, modo de implantação |
| DESCONHECIDO | Informação ainda não verificável | APIs disponíveis, latência, custos efetivos, limite de modelos |

Nenhuma categoria constitui software funcionando.

## 3. Inventário rastreável de capacidades candidatas

| ID | Domínio funcional candidato | Evidência de necessidade | Critério de aceitação futuro (não teste executado) |
| --- | --- | --- | --- |
| CAP-01 | Identidade, soberania e mandatos | Carta seções 2–4; D02-09, D02-15 | Delegações e atos reservados distinguíveis; acesso indevido não permitido |
| CAP-02 | Founder Command Center | D02-AD-01 | Fundador pode compreender agentes, missões, contexto e poderes legitimamente disponíveis |
| CAP-03 | Núcleos, agentes, papéis e missões | Carta seções 3–4; D02-02, 03, 10, 11 | Funções e responsabilidades rastreáveis; não atribuir agência inexistente |
| CAP-04 | Evidências, conhecimento e memória | Carta seção 6; D02-12, 13, 16, 23 | Origem, revisão, hipótese e resultado distinguíveis |
| CAP-05 | Consumo, roteamento, tokens, custos e Jev | Carta seção 7; D02-AD-02 | Custos realmente apurados; economias comparadas com baseline |
| CAP-06 | Receitas, despesas, compromissos e reservas | Carta seção 5; D02-AD-02 | Registros financeiros protegidos, reconciliáveis e de origem conhecida |
| CAP-07 | VPS e infraestrutura observável | D02-AD-02 | Métricas reais somente se coletadas de fontes consentidas e verificadas |
| CAP-08 | Chief of Staff e Telegram | D02-10; D02-AD-03 | Identidade, autorização e auditabilidade adequadas à finalidade |
| CAP-09 | Relatórios, PDFs e planilhas | D02-AD-03 | Documentos distinguem fonte, data, observação e inferência |
| CAP-10 | Voz e identidades vocais | D02-AD-04 | Custo, qualidade, autorização e privacidade validados antes de ativação |
| CAP-11 | Identidade institucional e experiência | D02-01..24, síntese canônica | Fidelidade simbólica e acessibilidade sem alegação enganosa de implementação |
| CAP-12 | Segurança, auditoria e integridade transversais | Carta seções 2, 4, 6, 9 | Responsabilização, limites, logs apropriados, tratamento lícito dos dados |
| CAP-13 | Evolução e análise de melhoria | Carta seções 6–7; requisitos do fundador | Melhoria sustentada por experimentos comparáveis, e não simples atividade |

## 4. Primeiras dependências candidatas

**Invariantes para qualquer cenário futuro:** legitimidade de identidade/mandatos, honestidade sobre dados e evidências, tratamento de informação sensível, critérios de verificação, custo estimável, ações humanas reservadas e possibilidade de auditar resultados.

Candidatas que podem ser adiadas para incremento posterior, **sujeitas a ratificação**: voz, Telegram operacional, métricas de VPS reais, dados financeiros reais, dashboards completos e mecanismos de autoaperfeiçoamento. O adiamento de implementação não revoga requisito histórico.

## 5. Três hipóteses históricas de recorte inicial; alternativa C escolhida na D03-02

**A. Central de supervisão (não escolhida):** validar necessidades do fundador e descrição conceitual dos agentes primeiro; risco de produzir uma camada de apresentação sem fontes reais.

**B. Fundação cognitiva (não escolhida):** definir governança de memória/evidências/mandatos antes da supervisão; risco de prolongar trabalho de infraestrutura sem valor visível.

**C. Recorte vertical verificável (aprovada):** especificar um ciclo mínimo **orientação legítima → missão delimitada → evidência/resultado → explicação rastreável de custo quando medível**; risco de integração prematura, a controlar por contratos e escopo curto.

**D03-02 C APROVADA**: primeiro ciclo vertical verificável. Os cenários A e B permanecem alternativas históricas, não escolhas atuais. As capacidades concretas abaixo são candidatas, não funcionalidades ratificadas em detalhe.

## 6. Priorização sugerida como método

Após D03-02, avaliar capacidades por:
- valor direto ao fundador e redução de incerteza;
- obrigação constitucional/segurança;
- dependências e possibilidade de teste isolado;
- custo estimado de implantação/uso, com faixa e fonte;
- complexidade de integração e risco;
- oportunidade de aprendizado com evidência;
- reversibilidade e facilidade de entrega incremental.

Propor matriz **Must/Should/Later** apenas quando o escopo tiver sido deliberado. Não fixar percentuais, custos ou marcos fictícios.

## 7. Pendências para fechar E3-01

- **Concluído:** ratificação D03-02 C sobre princípio do primeiro incremento.
- Definir atores reais iniciais e fluxos legítimos, sem supor disponibilidade de dados.
- Delimitar o que será demonstrável sem dependências externas.
- Elaborar casos de aceite, riscos e termos que nunca devem parecer operacionais quando não o forem.
- Aprovar backlog curto do primeiro incremento e mapa de dependências.

**STOP CONDITION:** valor inicial e limites comprováveis documentalmente, aprovado pelo fundador, sem dependências essenciais ocultas. **E3-01 ainda não está concluído.**

## 8. Delimitação vertical autorizada pela D03-02 C (NOVO v0.2)

O fundador aprovou a orientação **primeiro ciclo vertical verificável**, não a arquitetura nem a execução. O recorte abaixo é **proposta documental de requisitos e aceite**, sujeita à revisão antes da Fase IV.

### 8.1 Finalidade observável

Provar futuramente, por evidências autênticas, que a instituição pode **receber instrução legítima do fundador; distinguir intenção de autorização; atribuir finalidade e limites a uma missão; relacionar relato a evidências; e indicar custo real ou ausência de dados com honestidade**. O ciclo deve ser útil mesmo que funções secundárias não estejam disponíveis.

### 8.2 Mínimo candidato por capacidade

| Faixa | Capacidades/IDs do catálogo | Delimitação candidata do primeiro ciclo | Excluído do primeiro ciclo, mas não do projeto |
| --- | --- | --- | --- |
| Essencial constitucional | CAP-01, CAP-12 | identidade, mandato, escopo e ato reservado; reconhecer negação e falta de autorização | não conceder poderes constitucionais a bots |
| Núcleo verificável | CAP-03, CAP-04 | missão identificável, fonte/alegação/evidência, revisão e resultado distinguíveis | pesquisa autônoma irrestrita e RAG instalado |
| Supervisão mínima | CAP-02 | **necessidade funcional** de compreensão do fundador, sem layout ou dashboard final | aparência final do Founder Command Center |
| Medição restrita | CAP-05 | origem e natureza de registros de tokens/custo quando realmente disponíveis; estado explícito de desconhecido | economia Jev demonstrada sem baseline e roteamento automático |
| Futuro posterior | CAP-06 a CAP-11, CAP-13 | preservar requisitos e contratos candidatos de integração | finanças, VPS real, Telegram, PDFs/planilhas, voz e aprimoramento autônomo operacionais |

**Não é autorização para excluir requisitos do fundador**, somente para ordenar sua possível implementação futura.

### 8.3 Casos de aceitação propostos (cenários textuais, NÃO testes)

| ID | Situação | Resultado correto exigido em futura validação |
| --- | --- | --- |
| AC-01 | Fundador com autoridade comprovada apresenta objetivo dentro do mandato | intenção, responsável e limite identificáveis; autorização não inferida |
| AC-02 | Solicitação implica gasto, privilégio ou mudança reservada sem aprovação | proposta permanece não autorizada; nenhum resultado fictício declarado |
| AC-03 | Missão é relatada como concluída, mas não há evidências verificáveis | relato classificado como não verificado, não como sucesso |
| AC-04 | Evidência possui origem, versão ou data conflitante | contradição preservada; conclusão suspensa/revista com justificativa |
| AC-05 | Custo por modelo/tarefa está indisponível | dado ausente claramente declarado; não imputar zero nem economia |
| AC-06 | Registro de custo existe com fonte mas sem baseline Jev | gasto observável diferente de economia atribuível ao Jev |
| AC-07 | Mandato revogado ou expirado | atos posteriores não se tornam autorizados pela continuidade visual do agente |
| AC-08 | Dados privados de terceiros constam de uma possível evidência | preservar limitações de acesso e não publicar conteúdo protegido indevidamente |

Esses casos serão criteriosamente revisados antes da Fase IV; **não foram executados**.

### 8.4 Dependências candidatas por responsabilidade

- **Autoridade** precede qualquer reivindicação de missão autorizada. Dados ausentes devem permanecer explicitamente ausentes.
- **Missão** possui responsável, finalidade, contexto e escopo conhecidos apenas após origem legítima.
- **Evidência** precisa de proveniência, versão e vinculação ao que pretende demonstrar.
- **Custo** não pode ser transformado em métrica de economia sem comparador real.
- **Visão do fundador** deve distinguir observado, estimado, informado e não verificável.
- **Auditoria e privacidade** atravessam todas essas responsabilidades, sem depender de stack escolhida.

### 8.5 Fora do MVP proposto, não revogados

Não prometer telemetria VPS, acesso financeiro, bot Telegram, síntese de voz, núcleo de pesquisa autônoma, autoaprendizado, sistema de alertas, visão 3D, navegação completa, custos de todos os provedores ou resultados automáticos. As capacidades históricas permanecem no catálogo para priorização futura.

### 8.6 Qualidade de aceitação documental

Antes de fechar E3-01 ainda é necessário: identificar atores reais, delimitar o primeiro caso de uso e suas fontes, definir o grau de dados legítimos disponíveis, aprovar conjunto final de AC, estimar esforço **com premissas explícitas** e documentar itens fora do incremento.

**STOP CONDITION E3-01: NÃO ATENDIDA.** D03-02 C resolve a direção do primeiro incremento, não todos os requisitos.

## 9. E3-01 sob D03-03 C: contratos de responsabilidade (NOVO v0.3)

**Status:** mapa de **responsabilidades e interdependências candidatas**, não APIs reais, esquema de banco, classes, pastas ou módulos físicos já ratificados. D03-03 C aprova que fronteiras conceituais sejam extraíveis por contrato, não como serviços distribuídos hoje.

| Fronteira lógica candidata | Responsabilidade de negócio do recorte | Posição de autoridade/dados | Contrato semântico a detalhar |
| --- | --- | --- | --- |
| AUT — Autoridade | validar mandatos, reservas de decisão, revogações e alcance de delegação | decisões normativas e autorizações; fonte de verdade futura a definir | requisição legítima e decisão explícita autorizada/negada/desconhecida com proveniência |
| MIS — Missão | definir intenção, finalidade, titularidade, progressão e estado de comprovação | eventos/alegações da missão, sem poder conceder mandatos | declaração de objetivo, referência ao mandato, alterações e estado reportado |
| EVD — Evidências | associar fonte, versão, proveniência e incertezas a afirmações | controla o significado das evidências, não o poder de execução | referência rastreável à missão, material probatório, critérios de revisão |
| CST — Custo | distinguir uso medido, preço previsto, gasto efetivo e dado ausente; Jev depende de baseline | contabilidade técnica de consumo quando disponível, sem assumir provedor | vínculo de uso a missão/modelo/intervalo, unidade, origem e nível de confiança |
| FCR — Compreensão do fundador | descrever estado da missão, mandato, confiança e custo com honestidade | leituras autorizadas de informação legitimamente acessível, sem elevação | visão coerente agregada, com ausências, divergências e fontes identificáveis |
| Transversal: AUD/PRV | auditoria, privacidade, proteção, rastreabilidade e princípios constitucionais | obrigações por domínio e por ator | requisitos comuns, não um serviço técnico obrigatório |

### 9.1 Regras de dependência

1. MIS **não decide** se o fundador ou agente dispõe de poder jurídico, administrativo ou técnico: consulta decisão AUT sob autoridade apropriada.
2. EVD não modifica a autorização da missão; seu vínculo é a alegação e a prova do fato ou da ausência de prova, preservando versões.
3. CST vincula medição à operação/atividade identificada; não recebe autoridade para inferir aprovação de gasto ou economia Jev.
4. FCR não acessa armazenamentos internos de qualquer domínio sem contrato legítimo; comunica explicitamente **autorizado**, **negado**, **não verificado** ou **indisponível** conforme o conceito.
5. Domínios não compartilham acesso indiscriminado a dados privados; a extração posterior não pode mudar o sentido constitucional das regras.
6. AUD/PRV representam exigências transversais; seu posicionamento técnico e propriedade de dados continuam a definir.

### 9.2 Aceitação documental complementar ao AC-01..08

| AC | Cenário a especificar | Risco mitigado |
| --- | --- | --- |
| AC-09 | Pedidos de missão sem decisão explícita de autoridade não podem parecer aprovados | elevação indireta de privilégios |
| AC-10 | EVD registra contestação e revisão de evidência sem alterar status de execução por si só | fabricação de êxito |
| AC-11 | CST distingue custo estimado, custo medido e ausência de dados, com unidade e proveniência | métrica enganosa |
| AC-12 | FCR comunica divergência ou fonte ausente de modo compreensível e sem acesso indevido | falsa confiança |
| AC-13 | Fronteira futuramente extraída conserva invariantes e histórico versionado sem alegar equivalência não testada | migração insegura |

Nenhuma dessas condições foi testada; são critérios futuros de aceitação sujeitos à revisão.

### 9.3 Dependências e ordem sugerida para a primeira entrega

- Definir antes o significado constitucional de autorização, dados e responsabilidades.
- Estabelecer contrato **lógico** entre AUT e MIS, sem protocolos.
- Precisar vínculos entre MIS, EVD e CST; EVD e CST podem ser analisados em paralelo **após** definições compartilhadas.
- FCR consolida leitura, não governa a autoridade dos outros domínios.
- Critérios de segurança, observabilidade e transparência atravessam todos os pacotes.

A ordem é sugestão de **planejamento e decomposição de requisitos**, não work order implementável nem cronograma aprovado.

### 9.4 Preservação integral dos requisitos fundadores

Founder Command Center completo, visualização e intervenção legítima, tokens/custos por agente, comparação Jev, finanças, VPS, Chief of Staff, Telegram, relatórios PDF/planilha, voz e aprendizagem institucional permanecem futuros. O recorte vertical seleciona **o que validar primeiro**, não retira esses requisitos. Carta Institucional v1.0 e síntese visual da Fase II mantêm precedência.

**E3-01: EM PLANEJAMENTO.** Ainda faltam aprovação dos requisitos detalhados, classificação e fonte de dados inicial, análise de custos e critérios finais do fundador.

## 10. Perfil de requisitos para avaliar stacks pela mesma régua (NOVO v0.4)

D03-04 C determina **igualdade de critérios**, não igualdade presumida de desempenho entre ecossistemas. Os casos AC-01..AC-13 e domínios AUT/MIS/EVD/CST/FCR orientam os critérios comuns. Nenhum teste ou benchmark foi executado.

### 10.1 Exigências invariantes, independentes de tecnologia

| ID | Propriedade que a futura stack deverá sustentar | Evidência exigida futuramente |
| --- | --- | --- |
| SR-01 | Mandatos humanos e negação explícita de poderes não concedidos | resultados de AC-01,02,07,09 em condições autorizadas |
| SR-02 | Separação lógica de intenção, missão, relato e evidência | casos AC-03,04,10 com proveniência preservada |
| SR-03 | Custos reais, estimativas e ausências distinguíveis | AC-05,06,11; unidade, provedor e fonte conhecida |
| SR-04 | Fronteiras evolutivas sem acesso cruzado ilegítimo | AC-08,12,13, contratos versionados e privacidade |
| SR-05 | Reproducibilidade de testes e migrações | relatório de aceitação de mesma carga/casos por alternativa |
| SR-06 | Manutenção e construção com equipe reduzida apoiada por IA | comparação real de custo e tempo líquido até aceitação |
| SR-07 | Continuidade e portabilidade | caminho de saída e substituição de componentes documentado |
| SR-08 | Dados e histórico consistentes sem inventar fontes | definição de fonte de verdade, retenção e falhas |
| SR-09 | Dados sensíveis fora de repositório público | política de acesso aprovada antes de informações reservadas |

### 10.2 Perfis de avaliação documentais (não pilotos executados)

- **Perfil P-A, integridade:** autorização/negação, revisão de evidência, missão e custos sob mesmas condições e mesma política.
- **Perfil P-B, manutenção:** evolução de um contrato de domínio e necessidade de atualização/validação cruzada.
- **Perfil P-C, integração de IA:** compatibilidade com provedores e ferramentas realmente disponíveis; tratamento de erros, tokens e limites de preço.
- **Perfil P-D, reversibilidade:** troca justificada de mecanismo de persistência ou extração futura com preservação de evidência, sem afirmar migração simples.
- **Perfil P-E, produtividade:** tempo e custos até aceitação comparados em tarefas equivalentes e critérios de pronto idênticos.

Esses perfis são **roteiros de futura comparação**, não testes em execução ou serviços selecionados.

### 10.3 Dependências de E3-01 ainda não satisfeitas

- aprovação dos atores iniciais e modelo legítimo de mandatos;
- decisão sobre a fonte mínima de dados e sua classificação;
- definição da fronteira entre dado real, cenário controlado e ausência de informação;
- acordo sobre privacidade, retenção e direitos de consulta por ator;
- aprovação de AC-01..13 e SR-01..09 como critérios finais, ainda candidatos;
- custos e suporte aferidos antes da escolha de stack e de qualquer promessa de desempenho.

**E3-01 permanece EM PLANEJAMENTO.** A D03-04 não escolheu framework, persistência, fonte nem recurso construído.

## 11. Invariantes de dados, fontes e histórico após D03-05 C (NOVO v0.5)

**Decisão já ratificada:** dados que sustentam mandatos, missões, evidências e custos exigem fontes verificáveis e histórico proporcional ao risco, aos direitos de titulares, à finalidade e ao custo. **Não é especificação de banco, esquema ou produto.**

### 11.1 Matriz mínima de requisitos semânticos

| Domínio | Que afirmação exige fonte de verdade | Histórico proporcional a analisar | Limites de integridade, acesso e retenção |
| --- | --- | --- | --- |
| AUT (autoridade) | identidade e mandato do sujeito que propõe/autoriza/revoga | decisões e revogações relevantes com origem e temporalidade | atos reservados, menor privilégio, direitos e correção legítima |
| MIS (missão) | intenção, mandato aplicável, responsabilidade e estado reconhecido | transições materiais sem equiparar relato a conclusão | nunca converter intenção em ação autorizada sem fundamento |
| EVD (evidências) | versão, origem e credibilidade de afirmações | revisões e relações entre versões quando justificadas | informações pessoais e material protegido não devem ser replicados sem base legal |
| CST (custos/Jev) | consumo medido, fonte do preço, estimativa e comparador | retificações relevantes e atribuições auditáveis | ausência de observação difere de zero; Jev não recebe crédito sem baseline |
| FCR (visão do fundador) | informações consultadas dos domínios sob autoridade legítima | rastro de decisões humanas quando necessário | leitura derivada não ganha poder de sobrescrever fonte de verdade |
| AUD/PRV (transversal) | legitimidade da finalidade e acesso a informações | trilha seletiva orientada ao risco, não coleta infinita | retenção, minimização, retificação/eliminação e proteção aplicáveis |

### 11.2 Critérios de aceitação adicionais (propostos, não testados)

| ID | Situação futura de validação | Resultado esperado |
| --- | --- | --- |
| AC-14 | Autorizações distintas entram em conflito temporal | é possível identificar precedência sem criar privilégio implícito |
| AC-15 | Uma evidência é corrigida após relatório de missão | versões e motivo da revisão ficam rastreáveis; resultado anterior não se reescreve silenciosamente |
| AC-16 | Medição de tokens/custo é substituída por informação melhor | origem, unidade, data e razão da correção ficam distinguíveis |
| AC-17 | Dados privados deixam de ter finalidade legítima de retenção | política aplicável governa retificação, expiração/eliminação e registros mínimos legalmente necessários |
| AC-18 | Leitura derivada está desatualizada ou fonte de origem indisponível | FCR expõe a limitação, nunca a apresenta como fato atual verificado |
| AC-19 | Registro histórico informa mudança mas não comprova autenticidade | classificar como registro, não como prova criptográfica ou científica de sua veracidade |
| AC-20 | Proposta de separação entre módulos altera consistência | preservar mandatos, versões, causalidade e limites de dados antes de aprovar extração |

A lista complementa AC-01 a AC-13 do histórico; sua redação final depende de revisão e aceite dos dados realmente disponíveis. Nenhum cenário foi executado.

### 11.3 Classificação de criticidade candidata para retenção

- **CRÍTICA:** mandatos, autorizações, revogações e atos com efeitos importantes; integridade, justificação e auditoria necessárias conforme obrigações legais.
- **ALTA:** fontes de evidência, correções relevantes e custos que sustentam decisões; histórico suficiente para explicar alterações.
- **CONTEXTUAL:** versões de hipóteses, metadados e relatórios, com finalidade e prazo definidos.
- **EFÊMERA:** intermediários, leituras transitórias e dados desnecessários à decisão; não presumir retenção por conveniência.

Níveis são **rótulos de análise**, não classificações jurídicas finais nem configurações automáticas de storage. A disciplina exige minimizar dados e respeitar direitos, inclusive exclusão, retenção legal e confidencialidade conforme aplicáveis.

### 11.4 Pendências impeditivas de aprovação final de E3-01

Fontes reais de identidade/mandato e custos, política de dados, atores e direitos de consulta, definição final de aceitação, orçamento e critérios de privacidade permanecem desconhecidos ou não ratificados. A primeira vertical D03-02 C e a modularidade D03-03 C não autorizam uma base de dados real.

**STOP CONDITION E3-01: NÃO ATENDIDA.** D03-05 C é princípio aprovado, não funcionalidade construída.

## 12. E3-01: matriz de requisitos comum ao pacote convergente D03-06 C (NOVO v0.6)

**Referência:** [Pacote de ADRs convergentes v0.1](PHASE-III-CONVERGENT-ADR-PACK-v0.1.md). A análise integrada C-01 (base principal), C-02 (persistência), C-03 (contratos) deve tomar **os mesmos critérios funcionais e os mesmos casos de aceite**, sem eleger vencedores.

| Fonte de requisito / teste futuro | Aspecto do ADR-C-01 | Aspecto do ADR-C-02 | Aspecto do ADR-C-03 |
| --- | --- | --- | --- |
| AC-01,02,07,09,14 | proteção de mandatos por runtime e testes | integridade e precedência temporal de decisões | AUT/MIS, revogação, ato reservado |
| AC-03,04,10,15,19 | verificação de tipos, validação e rastreio | histórico proporcional e revisão rastreável | MIS/EVD, alegação ≠ resultado confirmado |
| AC-05,06,11,16 | disponibilidade de observação de tokens/custo | integridade e correção de medição | MIS/CST, observado vs. estimado vs. desconhecido |
| AC-08,12,17,18 | mecanismos de segurança e privacidade a estudar | retenção, correção e eliminação legítima | FCR/AUD/PRV com acesso delimitado |
| AC-13,20 | modularidade extraível e reversibilidade | consistência de migração entre domínios | versão do contrato e direitos preservados |

**Todos os AC continuam candidatos a aceite**, não cenários executados nem certificados. A integridade da Carta prevalece sobre qualquer combinação que falhe critério eliminatório.

### 12.1 Definição documental de completude do recorte

Para declarar E3-01 pronto no futuro, o pacote de recomendação deverá conter: sujeitos e mandatos iniciais; finalidade específica; fronteira entre cenário controlado e fonte real; critérios de privacidade, consulta e retenção; mapeamento AUT/MIS/EVD/CST/FCR; conjunto de AC aceito; dados mínimos; lacunas; dependências com ADR-C-01..03; estimativa com premissas, segurança e condições de aceitação.

**D03-07 C APROVADA POSTERIORMENTE:** evidências em camadas L0–L4, com dados sintéticos futuros explicitamente identificados. Os AC históricos não foram executados. Ver [Plano v0.1](PHASE-III-EVIDENCE-LADDER-v0.1.md).

### 12.2 Riscos de escopo a vigiar

Apressar a escolha de tecnologia pode provocar interfaces incompatíveis, dados não legitimados, custos fictícios ou uma central visual convincente sem evidências. Por isso a direção C da D03-06 mantém decisões interdependentes em **ANÁLISE**, sem adiantar Fase IV.

**STOP CONDITION E3-01: NÃO ATENDIDA.** Os requisitos foram aprofundados sem aprovação final de dados, AC ou MVP implementável.

## 13. E3-01: D03-07 C e aceitação da vertical por evidências em camadas (NOVO v0.7)

**Aprovado:** plano de avaliação progressiva **L0 especificado → L1 cenário sintético rotulado → L2 resultado real de teste controlado → L3 fonte externa autorizada e verificada → L4 efeito operacional efetivamente comprovado**. Essa sequência descreve categorias de provas futuras, não execução nem promoção automática de confiança. **Somente L0 existe em termos documentais**. Consulte [Plano de Evidências v0.1](PHASE-III-EVIDENCE-LADDER-v0.1.md).

### 13.1 Critérios de rastreabilidade para AC-01..20

| Conjunto de AC existente | Requisito de origem e distinção de níveis | Cuidado de aceitação futuro |
| --- | --- | --- |
| AC-01,02,07,09,14 | mandatos, autorização, negação e revogação rastreados à autoridade legítima | testabilidade controlada não substitui autorização real |
| AC-03,04,10,15,19 | separação entre relato, hipótese, contradição, fonte e resultado | log de teste não atesta fato externo nem prova de operação |
| AC-05,06,11,16 | fonte, unidade, baseline e incerteza de custo | custo sintético não é gasto real nem economia do Jev |
| AC-08,12,17,18 | restrições de privacidade, leitura, retenção e erro de fonte | uso de dados reais somente com legitimidade e controles |
| AC-13,20 | compatibilidade, versão e regras de extraibilidade | migração ou extração futura não pode invalidar direitos |

A definição exata de provas específicas de cada AC ainda exigirá revisão humana e critérios de ambiente quando houver implementação autorizada. Não criar exemplos de dados, mocks, fixtures ou cenários executáveis nesta fase.

### 13.2 Semântica de estados e compromisso de clareza

- **PLANEJADO:** documentação da intenção; não significa código nem teste.
- **SINTÉTICO:** cenário artificial e explicitamente identificado, ainda inexistente.
- **TESTADO CONTROLADO:** resultado de teste com versão/configuração/método, somente quando houver execução futura real.
- **FONTE REAL AUTORIZADA:** proveniência, permissão e qualidade verificadas para o escopo da consulta, não necessariamente resultado correto da missão.
- **OPERACIONAL VERIFICADO:** efeito de missão demonstrado pela evidência apropriada, sem extrapolação para capacidades não medidas.
- **DESCONHECIDO/INCONCLUSIVO:** não substituir por zero, aprovação tácita ou êxito.

### 13.3 Critérios que faltam

Aceitar casos e atores iniciais, definir o limite mínimo de dados com privacidade e retenção, mapear proprietário de cada alegação, selecionar critérios de comprovação e revisar estratégia de autorização antes de qualquer teste futuro. **D03-08 C APROVADA** posteriormente como política documental de agentes construtores; D03-09 C APROVADA documentalmente; D03-10 C APROVADA documentalmente; D03-11 PENDENTE. **E3-01 segue EM PLANEJAMENTO**.


## 14. D03-08 C: requisitos de autorização para agentes construtores (NOVO v0.8)

[Política documental de agentes v0.1](PHASE-III-AGENT-GOVERNANCE-v0.1.md) estabelece delegação proporcional a risco e provas futuras, sem agentes reais. Os agentes construtores e os agentes institucionais continuam populações distintas; funções de Chief of Staff, finanças, voz, Telegram, Founder Command Center, Jev e VPS permanecem como necessidades futuras.

| Requisito candidato | Dependência de domínio do primeiro ciclo | Critério de aceitação futura |
| --- | --- | --- |
| RG-01 mandato explícito | AUT e MIS | proposta de tarefa não eleva permissão e identifica ator responsável |
| RG-02 escopo e propriedade | MIS/EVD/CST/FCR | tarefa isolada não modifica contratos externos sem revisão |
| RG-03 risco classificado | AUT/AUD/PRV | R0–R3 justificado por impacto e reversibilidade, sem automatismo jurídico |
| RG-04 fonte da prova | EVD e níveis L0–L4 | relatório de agente não se converte em aceite sem evidência verificável |
| RG-05 despesas | CST/Jev e direitos do fundador | teto futuro ratificado antes de consumo sujeito a aprovação; sem valor presumido |
| RG-06 segregação de funções | AUT e segurança transversal | agente não pode ampliar seu próprio mandato nem burlar verificação reservada |
| RG-07 parada e correção | MIS/EVD | ambiguidade, quebra de contrato, conflito e falta de dados exigem status explícito e replanejamento |
| RG-08 não exposição | AUD/PRV | nenhum dado financeiro, senha, token, VPS ou cliente exposto no repositório público |
| RG-09 futuro paralelismo | MIS, EVD, CST | só considerar independência após contratos minimamente estáveis, sem quantidade aprovada |

### Rastreio da primeira vertical

Orientação do fundador define o pedido, não aprova toda ação; missão candidata recebe escopo; evidência proveniente de fonte válida permite distinguir relato, teste e êxito; custo permanece desconhecido até medição real. O agente **construtor** apenas prepara futura implementação sob alçada, e não se transforma em emissário institucional.

**E3-01 EM PLANEJAMENTO:** requer aceitação dos casos AC-01..20 e RG-01..09, dados/atores reais definidos e autorização separada para qualquer teste ou código. **D03-09 C APROVADA documentalmente; D03-10 C APROVADA documentalmente; D03-11 PENDENTE.**


## 15. D03-09 C: requisitos de execução futura sob paralelismo elástico (NOVO v0.9)

**Status:** D03-09 C aprova o MÉTODO documental de dimensionamento adaptativo guiado por dependências e custo líquido. [Plano de Paralelismo Elástico v0.1](PHASE-III-ELASTIC-PARALLELISM-v0.1.md). Não há número de agentes, tarefas executáveis, cronograma de implementação, fontes reais ou medição.

| Requisito candidato | Fronteira/dependência | Critério de aceitação futura |
| --- | --- | --- |
| EL-01 autorização | AUT, política R0–R3 | mandato válido antes de delegar qualquer ação futura |
| EL-02 identidade de missão | AUT→MIS | contrato claro antes de trabalhos dependentes |
| EL-03 evidência | MIS→EVD | resultado de agente não substitui prova de tarefa concluída |
| EL-04 medição | MIS→CST | preço estimado ≠ gasto e baseline Jev deve ser independente |
| EL-05 visualização fundadora | AUT/MIS/EVD/CST→FCR | leitura autorizada, atualidade, ausências e grau L0–L4 visíveis |
| EL-06 tarefas paralelizáveis | versões de fronteiras e responsabilidade | independência legitimamente reconhecida, sem escritor concorrente não coordenado |
| EL-07 variação de concorrência | contratos, cotas e integração | melhoria líquida somente se comprovada sob critérios equivalentes |
| EL-08 regressão e STOP | revisão, segurança, risco e falha | reduzir/parar concorrência diante de desvio constitucional, financeiro ou de qualidade |
| EL-09 dados e direitos | AUD/PRV transversal | nenhuma informação privada/segredo transferida por conveniência de concorrência |
| EL-10 entrega aceita | AC-01..20 e DoD futuro | testes e revisão realmente executados em fase autorizada, não relato sem fonte |

**Rastreabilidade:** AC-01..20 e RG-01..09 permanecem propostas de aceitação; a nova lista EL-01..10 é complementar, não uma implementação. A Carta v1.0, Fase II encerrada e adendos do fundador prevalecem.

**E3-01 segue EM PLANEJAMENTO.** Faltam requisitos específicos e fontes, políticas reais, ratificação de AC/RG/EL e autorização operacional. **D03-10 C APROVADA documentalmente; D03-11 PENDENTE.**


## 16. D03-10 C: fechamento E3-01 por gates verificáveis (NOVO v0.10)

**Direção aprovada:** elaborar conclusão documental somente quando a [Matriz CG-01..CG-12 v0.1](PHASE-III-CONVERGENCE-READINESS-v0.1.md) demonstrar aceite dos requisitos relevantes. **E3-01 não foi encerrado; nenhum dos requisitos AC/RG/EL foi testado**.

| Gate de E3-01 | Conteúdo documental parcialmente existente | Evidência/decisão que falta |
| --- | --- | --- |
| CG-01 AUT/mandatos | D03-01, D03-08 C e regras de autoridade humana | atores, competências/limites, revogação e aceite da semântica |
| CG-02 recorte vertical | D03-02 C aprovou AUT/MIS/EVD/CST/FCR | prioridade funcional exata do Founder Command Center, D03-11 PENDENTE |
| CG-03 aceitação | AC-01..20, RG-01..09 e EL-01..10 propostos | consolidar duplicidades, responsáveis, critérios verificáveis e ratificação |
| CG-04 dados | fontes identificáveis, retenção proporcional D03-05 C | dados mínimos autorizáveis, direitos, fontes, classificação |
| CG-10 provas | L0..L4 definido pela D03-07 C | plano final de provas por requisito e quando será necessária execução futura |
| CG-07 segurança | soberania humana, sigilo e controle proporcional de agentes | política final de acesso, dados protegidos e revisão |

### 16.1 DoR e DoD documentais candidatos

**DoR de futura primeira vertical:** escopo exato e exclusões ratificados; atores/mandatos definidos; fontes necessárias e qualidade conhecida; dados e retenção classificados; AC final rastreável; riscos/contratos dependentes mapeados; meios de reversão propostos; orçamento/segurança com decisão humana apropriada.

**DoD documental E3-01:** mapa de capacidades e MVP aceito pelo fundador, requisitos e critérios de aceitação por fronteira sem contradições, prioridades de adendos/Command Center explicadas, dados mínimos e política de autoridade/privacidade especificados, evidências L0 com fontes e lacunas, dependências dos ADRs explicitadas e STOP CONDITION satisfeita por avaliação.

**DoD de SOFTWARE é futuro e não executado**; especificar testes necessários não os executa e não antecipa Fase IV.

### 16.2 FCR e adendos do fundador

O Command Center deverá refletir soberania, missões, evidências, custos, intervenção humana e explicação de incertezas. Telegram bilateral, vozes, PDFs/planilhas, Jev, finanças e VPS devem ser tratados como requisitos separados com fonte e dependências, nunca como integrações instaladas. A D03-11 definirá apenas o **recorte prioritário** do FCR, sem telas criadas.

### 16.3 Situação

**CG-01/02/03/04/10 e partes CG-07 continuam PENDENTES. STOP CONDITION E3-01: NÃO ATENDIDA.** D03-10 C aprovada como método; D03-11 ainda PENDENTE. Nenhum dado sintético, protótipo, software ou teste criado.
