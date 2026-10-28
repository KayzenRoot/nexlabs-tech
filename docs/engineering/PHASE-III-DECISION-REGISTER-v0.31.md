# NexLabs Technology — Registro de Decisões de Engenharia da Fase III v0.31

**Atualizado em:** 2026-10-27. **Fase III iniciada somente para planejamento documental.**
**Autoridade:** [Carta v1.0](../institutional/CHARTER-v1.0.md), [escopo autorizado e atualizado v0.31](PHASE-III-CHARTER-v0.31.md), [encerramento Fase II](../design/PHASE-II-ACCEPTANCE-v1.0.md).
**Regra:** registrar decisão expressa do fundador e seu alcance exato. Recomendação do assistente **não** é ratificação. Proposta técnica não equivale a implementação.

## D03-01 — Escopo da autorização da Fase III

- **Escolha do fundador:** **A — Fase III documental completa**.
- **Estado:** **APROVADA EXPRESSAMENTE** em 2026-10-15.
- **Abrangência:** E3-01 requisitos/primeira entrega, E3-02 arquitetura/stacks, E3-03 agentes e paralelismo, E3-04 prontidão/segurança/custos.
- **Exclusões:** qualquer código, produto, protótipo, imagem, serviço, integração, automação, implementação de agentes, infraestrutura ou seleção não fundamentada de stack e quantidade.
- **Efeito:** abrir fase de estudos e documentos; status dos pacotes **EM PLANEJAMENTO**; sem aprovação de soluções específicas.
- **Fonte de transição:** [Proposta histórica v0.1](../continuity/PHASE-III-TRANSITION-PROPOSAL-v0.1.md).

## D03-02 — Primeiro Ciclo Vertical Verificável (C, APROVADA)

**Decisão do fundador em 2026-10-15:** **alternativa C — Primeiro ciclo vertical verificável**.
**Status:** **APROVADA EXPRESSAMENTE**, exclusivamente para especificação/documentação. Não há implementação, demonstração, protótipo ou fonte de dados conectada.

### Princípio do primeiro incremento

Delimitar a primeira entrega futura como um recorte pequeno, integrado e auditável, que permita percorrer **orientação legítima do fundador → missão de alcance limitado → proveniência e evidência do resultado → indicação de custo efetivo quando mensurável e de seu grau de certeza**. As setas expressam uma **sequência conceitual de responsabilidades**, não workflow operacional aprovado ou software executável.

**Critérios não negociáveis:** uma solicitação não implica autorização, uma intenção não implica execução, um texto convincente não é prova de resultado, e um custo previsto não equivale a gasto efetivo. Toda ação reservada exigirá autoridade humana válida; fontes de dados ausentes devem ser identificadas claramente como indisponíveis.

**Aprova-se a estratégia de recorte, NÃO** layout do Founder Command Center, agentes reais, tecnologia, APIs, banco, modelos, protocolo, nível de automação ou quantidade de executores. Detalhes do alcance ainda passam por critérios e aprovação de requisitos.

### Consequências para os pacotes E3-01 a E3-04

- **E3-01:** definir casos de uso mínimos, papéis, aceitação observável e explícitos itens fora do primeiro incremento, preservando requisitos para fases seguintes.
- **E3-02:** comparar arquitetura e stacks com base nas fronteiras necessárias ao recorte, incluindo separação de autoridade, missão, evidência e medição.
- **E3-03:** dividir futura construção em parcelas independentes e mensuráveis, sem fixar simultaneidade ou orquestrador.
- **E3-04:** exigir riscos, DoR/DoD, segurança, custos, privacidade, aprovações e resultados reais antes de iniciar implementação.

### Proveniência e histórico

Na [v0.1](PHASE-III-DECISION-REGISTER-v0.1.md), a D03-02 estava pendente com alternativas A/B/C. A aprovação posterior do fundador é adicionada nesta v0.2, sem alterar o documento histórico.

## D03-03 — Núcleo Modular Evolutivo com Fronteiras Extraíveis (C, APROVADA)

**Decisão do fundador:** alternativa **C**, aprovada expressamente em 2026-10-15.
**Estado:** **APROVADA PARA PLANEJAMENTO DOCUMENTAL**, sem seleção de frameworks, bancos, repositórios físicos, topologia de implantação, número de agentes ou software.
**Registros históricos:** D03-01 A e D03-02 C preservados; [v0.2](PHASE-III-DECISION-REGISTER-v0.2.md) mantém as três alternativas anteriores e seu status histórico.

### Decisão e limites precisos

A NexLabs planejará o primeiro ciclo D03-02 como **conjunto coerente de capacidades, com responsabilidades, propriedade lógica da informação e contratos estáveis**, evitando tanto um grande conjunto indivisível quanto fragmentação física precoce. Módulos deverão **poder ser extraídos futuramente quando evidências e requisitos legítimos justificarem**, mas extraibilidade é uma qualidade de projeto documental, **não promessa de extração trivial ou de implantação separada**.

Fronteiras candidatas: **AUT (autoridade e mandatos)**, **MIS (missões e intenções)**, **EVD (evidências, proveniência e revisão)**, **CST (medição e custos)** e **FC (consulta/supervisão do fundador)**; segurança, privacidade e trilha de decisões são restrições transversais. Isso **não fixa cinco microsserviços, pastas, APIs, bancos, workers, classes ou equipes**.

Regras de orientação: dependências explícitas, nenhuma elevação implícita de mandato, informação ausente não tratada como zero, evidências com fonte e classificação, contratos sem acesso cruzado indevido a dados internos, nenhum custo Jev sem baseline, e escalabilidade demonstrada antes de extração.

### Efeito nos quatro pacotes documentais

- E3-01: identificar casos e contratos lógicos mínimos do ciclo vertical, com fontes e aceite.
- E3-02: documentar fronteiras e custos de acoplamento; comparar stacks independentemente da topologia e listar gatilhos justificados de eventual extração.
- E3-03: planejar independência das futuras tarefas de desenvolvimento por domínio e contratos, sem fixar concorrência nem sugerir agentes reais já criados.
- E3-04: incorporar limites de autoridade, dados privados, contrato, reversibilidade, riscos de extração e orçamento nos gates.

### O que D03-03 NÃO resolve

Framework principal, linguagem, banco, interfaces técnicas, modelo de implantação, número de serviços, modelo de IA, quantidade/papéis finais de agentes, custo, benchmarks, integrações e implementação permanecem **PENDENTES**. Nenhuma prova de extraibilidade, segurança ou desempenho foi executada.

## D03-04 — Base Principal Única Escolhida por Evidências, com Especializações Condicionais (C, APROVADA)

**Decisão do fundador:** opção **C**, ratificada expressamente em 2026-10-15.
**Estado:** **APROVADA para a estratégia de comparação documental**, não para a adoção de linguagem, framework, banco, topologia, modelo ou fornecedor.
**Histórico:** a [v0.3](PHASE-III-DECISION-REGISTER-v0.3.md) registra as três alternativas em seu estado anterior; seu texto permanece inalterado.

### Sentido da escolha

A NexLabs deverá comparar **TypeScript e Python sob critérios equivalentes**, buscando posteriormente uma **linguagem predominante** coerente com a vertical D03-02 C e as fronteiras extraíveis D03-03 C. Uma segunda linguagem, runtime ou stack só deverá ser justificada por benefício verificável maior do que custos de manutenção, integração, segurança, observabilidade e contexto de agentes de construção.

A decisão **não elege TypeScript, Python, NestJS, FastAPI, banco relacional, Postgres, SQLite, RAG, vetor, modelo de IA ou hospedagem**. Também não exige uma só linguagem para todos os sistemas da NexLabs em definitivo. O termo “única” define **preferência arquitetural inicial por simplicidade**, sujeita a avaliação e exceções justificadas.

### Comparação necessária antes de escolher tecnologia

1. Casos de uso reais do primeiro ciclo, com mandatos, missão, evidências, custo observado/estimado e leitura legítima do fundador.
2. Matriz comum de requisitos e pesos aprovados: segurança/autorização, correção de contratos, produtividade líquida até aceite, manutenção, compatibilidade com IA, portabilidade, custo total e capacidade de testar.
3. Avaliação de documentação, ecossistema, licenças, fornecedores e riscos de dependência; distinguir afirmações de documentação de observações medidas na NexLabs.
4. Persistência, concorrência, integridade da trilha de evidências e custos como **decisões separadas**, não inferidas da linguagem.
5. Critérios e limites de uso de segunda linguagem; decisão material deve ser aprovada com ADR e orçamento apropriados.
6. Comparar experiência real da equipe e recursos disponíveis, sem presumir limite de assinatura, preço de tokens ou disponibilidade de determinado modelo.
7. Manter o escopo puramente documental na Fase III, sem instalar, executar benchmarks ou criar sistemas.

### Efeito nos pacotes

- **E3-01:** fixar parâmetros e casos de aceitação a que as stacks candidatas terão de responder, sem escolher linguagem.
- **E3-02:** aprofundar matriz comparativa, dados/persistência, contratos e extraibilidade sem dar notas numéricas arbitrárias.
- **E3-03:** comparar produtividade de agentes sob uma base principal e especializações com custo de integração explicitado.
- **E3-04:** acrescentar gates para licenças, dependências, classificação de dados, custo e autorização antes de adotar qualquer tecnologia.

### Itens ainda PENDENTES

Seleção final de linguagem, framework, runtime, banco, esquema, protocolos, RAG, ferramenta/cliente de agentes, orquestrador, paralelismo, valores financeiros, infraestrutura, migração ou implementação. Todos requerem evidências, aceites e autorizações apropriadas.

## D03-05 — Fonte de Verdade Verificável com Histórico Proporcional (C, APROVADA)

**Escolha do fundador:** alternativa **C**, ratificada em 2026-10-15. **Natureza:** princípio de persistência e proveniência no planejamento documental; **não aprova banco, modelo, esquema, infraestrutura, event sourcing nem software**. A [v0.4](PHASE-III-DECISION-REGISTER-v0.4.md) preserva A/B/C em seu estado anterior.

### Critério aprovado

O futuro primeiro ciclo da NexLabs deve dispor conceitualmente de **fontes de verdade identificáveis para fatos, decisões e autorizações**, com **rastro de origem, integridade, versão e histórico suficiente ao risco**. A extensão do histórico deverá ser proporcional à criticidade, aos deveres legais, à privacidade e aos custos. Isso não obriga registrar permanentemente toda leitura, cada evento trivial, conversas privadas ou dados pessoais sem finalidade legítima.

A consistência de mandatos, autorizações, revogações, resultados e custos deve ser distinguida da reconstrução histórica de hipóteses e evidências: **transações, trilhas de alteração, registros imutáveis, event sourcing e mecanismos híbridos permanecem alternativas para comparar**. Sem evidência concreta de necessidade, não adicionar infraestrutura especializada só para ampliar o número de componentes.

### Invariantes semânticos

1. **AUT:** somente ator legitimado pode deliberar/autorizar ou revogar; a proveniência inclui ator, autoridade, contexto e momento, nos limites de privacidade.
2. **MIS:** intenção, proposta, autorização, resultado relatado e resultado comprovado permanecem semanticamente distintos; uma mudança de histórico não legitima ação.
3. **EVD:** fonte, hipótese, evidência, qualidade, contradição e revisão versionada permanecem distinguíveis, inclusive quando o resultado é desconhecido.
4. **CST/Jev:** estimativa, custo medido, ausência de fonte e economia atribuída por baseline não são intercambiáveis. Não converter dados ausentes em zero.
5. **FCR:** supervisão do fundador faz leitura autorizada; não pode contornar mandatos por usar um histórico ou uma projeção.
6. **PRV/AUD:** minimização de dados, proteção de terceiros, controle de acesso, conservação e eliminação legítima prevalecem sobre a metáfora de “memória permanente”. A rastreabilidade não implica acesso ilimitado.
7. **Correção:** correções documentadas preservam razão e vínculo com o registro anterior quando lícito, sem impedir eliminação, retificação e retenção aplicáveis.
8. **Confiabilidade:** histórico, transação e réplica não são provas de autenticidade ou de recuperação técnica se não houver validação independente dos dados.

### Direção para E3-01 a E3-04

- **E3-01:** associar dados mínimos e aceitação à proveniência/consistência sem escolher esquema técnico.
- **E3-02:** comparar relacional transacional, histórico seletivo, event sourcing integral e híbridos sob requisitos iguais; avaliar isolamento, custo, segurança, migração e reversibilidade.
- **E3-03:** planejar partição de trabalho de agentes por domínio com contratos de versionamento e revisão, sem fixar quantidade.
- **E3-04:** documentar riscos de adulteração, divulgação, retenção excessiva, perda de histórico, falha transacional e custo, com gates antes da Fase IV.

**Não escolhidos:** PostgreSQL, SQLite, banco documental, Redis, vetores, filas, bibliotecas, APIs, modelos, linguagens, serviços físicos e fornecedores.

## D03-06 — Pacote Convergente de ADRs Interdependentes (C, APROVADA)

**Escolha expressa do fundador:** **C — Pacote convergente de ADRs interdependentes**, em 2026-10-15.
**Status:** **APROVADA COMO MÉTODO DE PLANEJAMENTO DOCUMENTAL**, não como aprovação de ADR ou tecnologia concreta.
**Histórico anterior:** [registro v0.5](PHASE-III-DECISION-REGISTER-v0.5.md) preservado integralmente, inclusive alternativas A/B/C antes da aprovação.

### Regra aprovada

As decisões sobre **linguagem/stack predominante, persistência e contratos entre domínios** deverão ser elaboradas e avaliadas **como um conjunto interdependente**, usando o mesmo recorte D03-02 C, as mesmas restrições constitucionais e critérios de qualidade, segurança, custos, portabilidade e produtividade. A convergência deve expor acoplamentos e decisões conflitantes, em vez de apresentar escolhas isoladas como prontas.

**A aprovação D03-06 NÃO escolhe** linguagem, framework, banco, ORM, interface/protocolo de comunicação, modelo de agente/LLM, número de agentes, topologia física, fornecedor, orçamento ou qualquer software.

### Pacote documental instituído

[Pacote Convergente de ADRs v0.1](PHASE-III-CONVERGENT-ADR-PACK-v0.1.md), com:
- **ADR-C-01 (EM ANÁLISE):** base principal e custo total das stacks candidatas, TypeScript/Python e exceções justificáveis;
- **ADR-C-02 (EM ANÁLISE):** fonte de verdade, integridade e histórico proporcional; alternativas transacionais, eventos seletivos/integrais e híbridos;
- **ADR-C-03 (EM ANÁLISE):** contratos de fronteira AUT/MIS/EVD/CST/FCR, privacidade, proveniência, evolução e extraibilidade;
- matriz de dependências entre as três decisões, comparações consistentes e critérios de veto;
- custos como categorias e premissas, **sem valores inventados ou benchmarking executado**;
- lacunas e evidências ainda necessárias antes de ratificação material.

As três propostas deverão **convergir em um pacote de recomendação para posterior ratificação humana**, e poderão ser revisadas simultaneamente sem criar três decisões tácitas. Status **EM ANÁLISE** nunca implica **APROVADO**.

### Efeitos em E3-01..04

- E3-01: fornecer uma única matriz de casos AC-01..AC-20, fontes, mandatos e requisitos que todas as alternativas deverão atender.
- E3-02: criar opções combinadas e ADRs com benefícios, riscos, custos e migração comparáveis, sem eleição de vencedora.
- E3-03: separar agentes construtores de agentes institucionais; estimar riscos e custos de execução integrada dos contratos sem fixar número de workers.
- E3-04: identificar gates de privacidade, segurança, legalidade, aceitação, custos e futura implantação; jamais considerar a Fase IV autorizada.

## D03-07 — Evidências em Camadas, do Controlado ao Autorizado (C, APROVADA)

**Escolha expressa do fundador em 2026-10-15: C.** Aprova exclusivamente o **plano documental** de validação progressiva da primeira vertical. Preserva a pergunta histórica da [v0.6](PHASE-III-DECISION-REGISTER-v0.6.md). Não autoriza criar dados sintéticos, executar testes, conectar fontes ou implementar software.

**Cinco níveis sem promoção automática:** L0 requisito escrito (PLANEJADO); L1 cenário sintético explicitamente fictício, apenas futuro; L2 teste controlado realmente executado no futuro, condicionado à autorização; L3 dados reais acessados legalmente com autorização, origem e limites verificáveis; L4 efeito operacional de missão efetivamente comprovado. No momento apenas **L0 documental**. Um L2 não prova L3 ou L4, e a mera realidade da fonte não prova sua exatidão.

**Garantias:** mandatos de AUT precedem ações; MIS distingue intenção/relato/comprovação; EVD identifica fonte, versão e contestação; CST não confunde estimativa, falta de dados, gasto e economia atribuível ao Jev; FCR apresenta incerteza e legitimidade do acesso; dados privados respeitam finalidade, retenção e direitos; resultados futuros exigem método, versão e evidências auditáveis. Nunca anunciar simulações como operação.

[Plano de Evidências em Camadas v0.1](PHASE-III-EVIDENCE-LADDER-v0.1.md), [Pacote ADR v0.2](PHASE-III-CONVERGENT-ADR-PACK-v0.2.md) e E3-01..04 v0.7 detalham os critérios futuros. Nenhum desses documentos implementa testes ou define stack, banco, modelo, agentes, métricas ou infraestrutura.

## D03-08 — Autonomia Graduada por Risco e Evidências (C, APROVADA)

**Ratificação expressa do fundador em 2026-10-15:** **C — Autonomia graduada por risco e evidências**, exclusiva do **planejamento documental da futura fábrica de agentes de construção**.
**Não aprova:** agentes reais, modelos, número ou concorrência de agentes, orquestrador, permissões de GitHub, acesso a serviços, PRs/merges, CI, infraestrutura, dados sintéticos, teste executável ou desenvolvimento da Fase IV. [Registro v0.7](PHASE-III-DECISION-REGISTER-v0.7.md) preserva a pergunta A/B/C antes da aprovação.

### Conteúdo exato da decisão

Planejar uma delegação **proporcional ao risco do trabalho, à legitimidade de seu mandato, às dependências e à qualidade das evidências**. Atividades reversíveis e de baixo risco poderão **ser elegíveis futuramente** a menor fricção, mas sem dispensa de checks essenciais. Trabalho com segurança, dados protegidos, autoridade humana, contratos compartilhados, finanças ou efeitos externos exigirá salvaguardas e decisões humanas nos pontos reservados.

**Autonomia não é consciência, pessoa, poder jurídico nem soberania**. Os futuros agentes **construtores** são diferentes dos agentes **institucionais** da NexLabs (Chief of Staff, núcleos). A Carta v1.0 e suas reservas humanas mantêm precedência.

### Classificação de risco proposta para estudos, sem papéis operacionais concedidos

- **R0 — apenas documentação reversível e pública:** verificação documental proporcional, com fonte, histórico e evidências L0; **a presente Fase III continua somente documental**.
- **R1 — mudanças futuras contidas e reversíveis:** possibilidade de delegação circunscrita e aceitação por checks realmente executados na fase autorizada, sem editar mandatos/segredos/contratos de alto impacto.
- **R2 — alterações de contratos compartilhados, integridade, privacidade, custo significativo ou dependências cruzadas:** planejamento de revisão especializada e autorização apropriada conforme impacto.
- **R3 — ações reservadas/irreversíveis, credenciais, poderes, finanças, informações protegidas, deploy sensível ou mudanças que enfraqueçam controles:** nenhuma delegação pode substituir autorização humana legítima, deveres legais e verificação proporcional.

**R0..R3 são categorias DOCUMENTAIS candidatas** para estimar risco, não alçadas finais, classificações jurídicas automáticas, configurações ou poderes; decisões quantitativas de orçamento e limites são pendentes.

### Condições de delegação futura

Cada unidade de trabalho, se posteriormente autorizada, deverá declarar: fonte da autorização; escopo e responsável; dependências; domínios AUT/MIS/EVD/CST/FCR afetados; arquivos/dados permitidos; risco e reversibilidade; critério AC e nível de evidência L0..L4 exigido; teto de custo **a ser aprovado**; revisão e condição de parada. Entrega aceita requer evidência de validação, não relato do próprio agente.

**Nenhum agente será usado para ampliar seu próprio mandato, aprovar despesa não autorizada, liberar segredo ou superar controle de branches.** Eventual automação de merges precisará de checks realmente configurados, autorização e evidência posterior; nada disso foi criado nesta fase.

### Documentos e efeitos

- [Plano de Governança de Agentes Construtores v0.1](PHASE-III-AGENT-GOVERNANCE-v0.1.md): papéis, risco, revisões, orquestração futura, custo e evidência;
- E3-01..04 v0.8: requisitos do primeiro ciclo, contratos candidatos, fábrica e gates;
- [Pacote de ADRs Convergentes v0.3](PHASE-III-CONVERGENT-ADR-PACK-v0.3.md): risco de alteração de contratos e fontes de verdade sob agentes;
- [Plano de Evidências em Camadas v0.1](PHASE-III-EVIDENCE-LADDER-v0.1.md): histórico D03-07 preservado sem modificação.

## D03-09 — Paralelismo Elástico Guiado por Dependências e Custo Líquido (C, APROVADA)

**Ratificação expressa do fundador:** **alternativa C**, em 2026-10-15. Esta aprovação estabelece um **método de planejamento e futura avaliação de concorrência**, não configuração, modelo ou número real de agentes.

### Decisão e limites

A futura fábrica de agentes construtores da NexLabs deverá avaliar um **baseline de execução sequencial** e cenários de concorrência incremental, respeitando dependências e contratos do núcleo modular evolutivo (D03-03 C), riscos/autonomia graduada (D03-08 C), evidências em camadas (D03-07 C) e custo líquido. Paralelismo somente será recomendado futuramente quando reduzir o **tempo até entrega aceita**, mantendo segurança, testes, qualidade, rastreabilidade e orçamento comparáveis.

**Nenhuma quantidade definitiva de agentes, teto de concorrência, modelo, ferramenta, stack, banco, orquestrador, implantação, benchmark ou valor financeiro foi aprovado.** A comparação de cenários é DOCUMENTAL nesta Fase III; medir executores exige Fase IV ou outra autorização operacional específica. A [v0.8](PHASE-III-DECISION-REGISTER-v0.8.md) permanece como registro histórico anterior.

### Métricas e critérios para futura comparação autorizada

- **DAG de dependências candidata**, sem workflow operacional: AUT/mandatos → MIS/identidade de missão → EVD e CST (candidatos a análise independente após contrato compartilhado) → FCR/leitura autorizada. Privacidade, segurança, auditoria e revisão atravessam o grafo.
- **Produtividade líquida:** resultados aceitos por tempo e custo total; diferenciar tempo de geração, tempo de integração e tempo de aceitação final.
- **Custo total:** consumo de modelos e ferramentas, revisão, testes, integração, conflitos, retrabalho, coordenação, manutenção e riscos de privacidade, conforme fontes que venham a existir.
- **Qualidade e segurança:** falhas/defeitos, regressão, inconsistência de contratos, acesso indevido, evidências faltantes e resultados alegados sem prova. Não compensar risco crítico com ganho de velocidade.
- **Cenários candidatos não quantitativos:** S0 (sequencial como referência), S1 (concorrência limitada com frentes elegíveis), S2 (concorrência ampliada somente quando comprovadamente útil). Os rótulos **não são números de agentes**, orçamentos ou metas de performance.
- **Critérios de escalada futura:** independência realmente comprovada, contratos estáveis, capacidade real das ferramentas/modelos, custo aceitável, qualidade consistente e limites de segurança.
- **Critérios de redução/parada:** conflito de fronteiras, custo sem lastro, perda de qualidade, saturação do integrador, falha de checks, ausência de autorização, indisponibilidade de fonte ou direitos violados.
- **Jev:** economia atribuída depende de baseline reproduzível e separação dos efeitos de paralelismo, escolha de modelo e redução de contexto; não inventar percentuais nem alegar medida.

**R0–R3 são faixas documentais de risco, L0–L4 são classes de evidência.** Fase III produz exclusivamente critérios L0, sem simulações, código ou testes; relato do agente não é prova de conclusão.

### Referências documentais após D03-09

[Plano de Governança dos Agentes Construtores v0.2](PHASE-III-AGENT-GOVERNANCE-v0.2.md); [Plano de Paralelismo Elástico v0.1](PHASE-III-ELASTIC-PARALLELISM-v0.1.md); [Pacote Convergente de ADRs v0.4](PHASE-III-CONVERGENT-ADR-PACK-v0.4.md); E3-01..04 v0.9. Todos seguem DOCUMENTAIS e NÃO EXECUTADOS.

## D03-10 — Fechamento Integrado por Gates Verificáveis (C, APROVADA)

**Ratificação expressa do fundador:** alternativa **C — Fechamento integrado por gates verificáveis**, em 2026-10-15.
**Natureza:** método de **planejamento documental** e organização de lacunas e futuras propostas de decisão, **NÃO** aceitação dos pacotes E3, ratificação de ADR-C-01..03, implementação ou transição de fase.
**Histórico:** a versão [v0.9](PHASE-III-DECISION-REGISTER-v0.9.md) guarda a questão e alternativas anteriormente pendentes.

### Deliberação em vigor

- Consolidar **E3-01 a E3-04**, os três ADRs interdependentes e os requisitos da primeira vertical AUT/MIS/EVD/CST/FCR em **uma matriz única de pré-requisitos, donos de decisão, evidências, custos e risco**.
- Cada pacote tem **STOP CONDITION própria**. Lacuna identificada permanece **ABERTA**, inclusive se outras áreas avançaram; nenhuma palavra como "pronto", "aceito", "validado" ou "encerrado" poderá substituir prova verificável.
- O fechamento é **por verificações objetivas**: escopo/requisitos e AC; arquitetura comparada e ADRs; limites de segurança, privacidade e orçamento; agentes construtores e modelo de validação; documentação rastreável e decisão humana legítima.
- Preparar **recomendações técnicas coerentes entre si** de stack, persistência e contratos, mas suas ratificações materiais ocorrerão por autorização **expressa e identificável**; nenhum pacote engole ou presume os demais.
- E3-03 deve preservar D03-08 C (autonomia por risco) e D03-09 C (paralelismo elástico por custo líquido); modelos, número de agentes, clientes e concorrência real seguem pendentes.
- A régua de evidência D03-07 C permanece **L0 documental** no estágio presente. L1..L4 não existem operacionalmente e **nenhum resultado de teste, custo efetivo ou ganho Jev foi obtido**.
- Requisitos Founder Command Center, Chief of Staff e Telegram bilateral, vozes dos agentes, tokens/Jev, finanças, VPS e relatórios preservados como **requisitos**, sem alegações de funcionamento.
- A Carta Institucional v1.0, Fases I e II encerradas, D02-01..25 e adendos do fundador continuam de autoridade superior. Fase IV exige autorização independente.

### Artefatos de implementação DOCUMENTAL autorizados

- [Matriz de Convergência e Prontidão v0.1](PHASE-III-CONVERGENCE-READINESS-v0.1.md): gates CG-01..CG-12, lacunas com critério, dependências, fontes e responsáveis por futura ratificação, DoR/DoD **candidatos**, riscos e inventário de custos sem valores inventados;
- [Pacote de ADRs Convergentes v0.5](PHASE-III-CONVERGENT-ADR-PACK-v0.5.md): C-01 stack, C-02 persistência, C-03 contratos, todos **EM ANÁLISE**, com dependência explícita de gates;
- E3-01..04 v0.10: anexos de fechamento por pacote com **estado verificável NÃO ATENDIDO**;
- [Governança de Agentes v0.3](PHASE-III-AGENT-GOVERNANCE-v0.3.md): limites de delegação, evidências e medição futura de produtividade integrados a critérios de prontidão.

**Nenhum framework, linguagem, banco, protocolo, modelo, fornecedor, quantidade de agentes, preço, orçamento, arquitetura de serviços ou ferramenta foi selecionado ou aprovado. Nenhum software, imagem, protótipo, agente, teste, dado sintético, automação, integração ou infraestrutura foi executado.**

### Resultado documental e condição de fechamento

**A D03-10 C fica APROVADA como decisão.** Porém os **quatro E3 continuam EM PLANEJAMENTO**, os três ADRs **EM ANÁLISE**, a STOP CONDITION da Fase III **NÃO ATENDIDA**, e a Fase IV **NÃO AUTORIZADA**. A matriz não é prova operacional e não dispensa atos humanos reservados.

## D03-11 — Comando Progressivo com Soberania Explícita (C, APROVADA)

**Ratificação expressa do fundador:** alternativa **C**, em 2026-10-15. **Natureza:** prioridade funcional DOCUMENTAL do futuro Founder Command Center (FCR), sem autorização para programar, projetar telas/imagens, produzir protótipos, executar testes, acessar fontes reais, criar comandos, bots ou integrações. [Registro histórico v0.10](PHASE-III-DECISION-REGISTER-v0.10.md) conserva as alternativas antes da escolha.

### Diretriz de prioridade da primeira vertical

1. **Primeiro recorte a planejar:** supervisão verificável com leitura legitimada de pedido/mandato, missão, responsável, estado reportado, evidência associada, incertezas, custos quando mensuráveis e lacunas declaradas. Sem fonte autorizada ou confirmação, exibir conceitualmente **DESCONHECIDO/NÃO DISPONÍVEL**, nunca inventar valores, status de execução ou taxas.
2. **Soberania desde o desenho:** reservar conceitualmente decisões, intervenções, pausa, revogação, aprovação/recusa e explicação de consequências à autoridade humana apropriada. A **presença de um requisito de controle não significa que o botão, a ação ou a API exista**.
3. **Habilitação posterior condicionada:** delegações e atos interativos só poderão integrar futuro software após contrato de mandato, direitos, segurança, privacidade, custos, idempotência/revogação, evidências e gates ratificados, com autorização separada da Fase IV. O FCR não recebe privilégios adicionais apenas por ser interface de supervisão.
4. **Não dashboard decorativo:** cada indicador futuro deverá apontar a fonte, versão, classificação de confiança L0–L4 e autorização; reservar caminho de retorno à evidência ou ao estado INCONCLUSIVO.
5. **Não ampliar o primeiro ciclo sem justificativa:** Chief of Staff/Telegram bilateral, voz, relatórios PDF/planilhas, finanças, observabilidade de VPS e Jev permanecem requisitos do fundador, com dependências e provas próprias; sua inclusão funcional inicial NÃO foi aprovada por esta D03-11.

### Mínimo semântico do primeiro incremento (não UI/API)

- **FCR-V1**: visão de mandatos e decisões do fundador, com distinção entre solicitado/permitido/negado/revogado.
- **FCR-V2**: missão, responsabilidade, transição de estado e dependências; não tratar relatório de agente como aceitação.
- **FCR-V3**: evidências e respectivas fontes, versão, contestação e grau de verificabilidade.
- **FCR-V4**: custos/consumo somente com fonte e unidade, distinguindo estimado/medido/ausente; Jev requer baseline independente.
- **FCR-V5**: pendências e intervenções humanas reservadas **apenas como exigência documental de futuro fluxo**, sem nenhum comando efetivo.
- **FCR-V6**: política de acesso, minimização, retenção proporcional e não elevação de privilégios na agregação.

[Plano Funcional FCR v0.1](PHASE-III-FOUNDER-COMMAND-CENTER-v0.1.md) detalha fronteiras, rastreabilidade, estados, DoR/DoD, cenários negativos e dependências. [Matriz de Convergência v0.2](PHASE-III-CONVERGENCE-READINESS-v0.2.md) vincula D03-11 aos gates CG-01..12. E3-01..04 v0.11, [Pacote de ADRs v0.6](PHASE-III-CONVERGENT-ADR-PACK-v0.6.md) e [Governança de Agentes v0.4](PHASE-III-AGENT-GOVERNANCE-v0.4.md) continuam **EM PLANEJAMENTO/ANÁLISE**.

**D03-11 C não aprova modelo, frontend, framework, banco, voice/Telegram, número de agentes, serviços, parâmetros de segurança, orçamento, ambiente ou arquitetura física.** Não conclui E3, não valida nenhum gate, não autoriza Fase IV.

## D03-12 — Mandatos Limitados, Revogáveis e Proporcionais ao Risco (C, APROVADA)

**Ratificação expressa do fundador:** alternativa **C**, em **2026-10-16**. Apenas **POLÍTICA DOCUMENTAL para futuras missões de agentes INSTITUCIONAIS**, preservando soberania humana e normas aplicáveis. [Versão histórica v0.11](PHASE-III-DECISION-REGISTER-v0.11.md) mantém a pergunta e as alternativas originais.

**Alcance exato da decisão:** nenhuma missão, agente institucional, executor, credencial, acesso, fonte real, comando, fluxo, ferramenta, custo, aprovação financeira, token, autoridade técnica ou jurídica é criado por este registro. D03-08/09 C continuam dirigindo a **futura fábrica de agentes construtores**, sem transferência de seus mandatos.

### Mandato de missão institucional, sem escolher formato técnico

Uma missão somente poderá ser considerada FUTURAMENTE elegível a autonomia se houver **autoridade de origem legítima e verificável** e mandato delimitado quanto a: ator/principal e responsável; finalidade lícita; atos permitidos e proibidos; alcance de dados, sistemas e terceiros; prazo de validade; risco/impacto e reversibilidade; teto financeiro quando houver consumo relevante (**valor NÃO definido**); condições de revisão e escalada; evidências exigíveis L0..L4; revogação/suspensão; transparência e prestação de contas; direitos aplicáveis e soberania do fundador.

Nenhum mandato admite **ampliação por inferência, autopermissão, subdelegação tácita, substituição de aprovação humana reservada, acesso por disponibilidade técnica ou despesa sem alçada**. Informação confidencial não será registrada em documentação pública. Classificação de risco institucional é **conceitual e deverá ser ratificada**; R0..R3 da fábrica CONSTRUTORA não é automaticamente transferida para negócios.

### Ciclo de autoridade e revogação, apenas requisitos futuros

- **PROPOSTO:** intenção de ação; sem permissão operacional.
- **AUTORIZADO/ATIVO:** somente depois de validação legítima de emissor, escopo, tempo, finalidade, direitos, riscos e limites quando houver sistema implementado.
- **SUSPENSO:** exigir pausa de atos abrangidos e confirmação por autoridade competente; estabelecer comportamento futuro em situações de incerteza ou indisponibilidade.
- **REVOGADO/EXPIRADO:** proibir novas ações com base no mandato e definir política de tratar ações em trânsito, registros e efeitos irreversíveis, sem prometer revogação física que não existe.
- **RECUSADO/INVÁLIDO/INCONCLUSIVO:** distinguir recusa humana, documento ilegítimo, disputa de versões e falta de prova. Falta de informação não equivale à autorização.

A futura fonte de verdade deverá conservar **ordem temporal, versão, motivo permitido, fonte, responsável e histórico proporcional**, sem declarar uma revogação efetiva sem confirmação apropriada.

### Riscos e deveres de aceitação

Mandatos institucionais devem ser testáveis FUTURAMENTE quanto a negação, expiração, revogação durante execução, duplicidade/replay, conflito de autoridades, permissões de dados de terceiros, orçamento desconhecido/excedido, relato sem prova, canais divergentes e ações irreversíveis. Custos estimados não são gastos efetivos; conclusão autorrelatada por agente não é resultado verificado; limites legais e direitos de titulares prevalecem.

[Política Documental de Mandatos v0.1](PHASE-III-INSTITUTIONAL-MANDATES-v0.1.md) reúne campos, transições semânticas, matriz de responsabilidade, riscos, casos negativos MC-01..MC-14, fontes de prova e DoR/DoD. [FCR v0.2](PHASE-III-FOUNDER-COMMAND-CENTER-v0.2.md) descreve supervisão e intervenções humanas como conceitos. [Matriz CG v0.3](PHASE-III-CONVERGENCE-READINESS-v0.3.md), [ADRs v0.7](PHASE-III-CONVERGENT-ADR-PACK-v0.7.md), [Governança dos Construtores v0.5](PHASE-III-AGENT-GOVERNANCE-v0.5.md) e E3-01..04 v0.12 incorporam limites sem declarar gates aceitos.

**D03-12 C APROVADA como norma de planejamento**, não materialização do contrato ou autorização de Fase IV. E3-01..04 seguem EM PLANEJAMENTO, ADR-C-01..03 EM ANÁLISE, CG-01..12 PENDENTES e respectivas STOP CONDITIONS NÃO ATENDIDAS.

## D03-13 — Política de Canais do Founder Command Center e Chief of Staff (C, APROVADA)

**Ratificação expressa do fundador:** **C — Núcleo de mandatos independente do canal e ativação progressiva**, em **2026-10-17**. Esta decisão é **exclusivamente DOCUMENTAL (L0)**. [Registro histórico v0.12](PHASE-III-DECISION-REGISTER-v0.12.md) preserva a pergunta A/B/C e a ausência anterior de aprovação.

### Política ratificada

1. **Autoridade única, sem privilégio por canal:** FCR, Chief of Staff, Telegram, voz, PDFs/relatórios e futuros clientes são meios potenciais de interação, não emissores de competência. Toda missão/ação deverá depender de identidade e mandato legítimos, escopo, risco, vigência e fonte de verdade apropriada, independentemente do meio.
2. **Semântica coerente:** proposta, autorização, negação, expiração, suspensão, revogação, relato, evidência e confirmação devem conservar significado e proveniência entre canais. Informação defasada, conflitante ou não disponível não pode ser tratada como autorização ou execução.
3. **Ativação progressiva condicionada:** priorizar futuramente o **FCR como primeiro canal de supervisão verificável**. Telegram bilateral, voz e relatórios seguem requisitos preservados, para análise e eventual habilitação **somente por autorização separada**, após identidade, privacidade, segurança, direitos, disponibilidade, custo e gates próprios. Nenhum canal futuro está obrigatório no MVP.
4. **Comandos e intervenções reservados:** leitura não autoriza ação. Orientar, aprovar, negar, suspender ou revogar no futuro exige comprovação de autor, intenção, versão do mandato, alçada e confirmação independente. Pedido recebido ≠ execução aceita ≠ efeito comprovado. Retransmissão/replay, duplicidade, disputa de versões e operação parcialmente concluída exigem tratamento documentado e validação futura.
5. **Soberania e proteção:** legalidade e direitos, Carta Institucional v1.0 e as políticas D03-11/12 prevalecem; canais não podem ampliar privilégios, burlar revogações, expor dados sensíveis ou presumir consentimento do silêncio humano.
6. **Neutralidade tecnológica:** a escolha não ratifica stack, banco, contrato/API, SDK, provedor de identidade, Telegram, modelo, agente, orçamento, número de serviços ou implantação.

[Política Documental de Canais v0.1](PHASE-III-CHANNEL-GOVERNANCE-v0.1.md) reúne invariantes, riscos, critérios candidatos CH-AC-01..12, fases de habilitação e dependências. Essas provas são apenas exigências futuras; **não há integração, conta, credencial, comando, teste, UI ou bot**.

### Impacto em E3 e convergência

- **E3-01:** manter a primeira vertical AUT/MIS/EVD/CST/FCR sob leitura autorizada; demais canais como extensões condicionais, com estados e direitos equivalentes.
- **E3-02 / ADR-C-01..03:** avaliar neutralidade de canal, contratos semânticos, identidade, consistência, ordem de revogação e direito de leitura; alternativas técnicas permanecem abertas.
- **E3-03:** não confundir agentes institucionais com construtores nem supor orquestrador ou múltiplos canais instalados.
- **E3-04 / CG-01..12:** acrescentar cenários de divergência, revogação, indisponibilidade, duplicidade, privacidade e custo ao futuro DoR/DoD, sem declarar gate aprovado.

**Estado:** D03-13 C APROVADA como política documental; E3-01..04 EM PLANEJAMENTO; CG-01..12 SEM ACEITE FINAL; ADR-C-01..03 EM ANÁLISE; STOP CONDITIONS NÃO ATENDIDAS. **Fase IV NÃO AUTORIZADA.**

## D03-14 — Identidade e Consistência Integradas, Proporcionais ao Risco (C, APROVADA)

**Ratificação expressa do fundador em 2026-10-17:** opção **C**: planejar **conjuntamente identidade, confirmação, revogação e resolução de conflitos**, com exigências proporcionais ao risco. A escolha fecha somente a alternativa estratégica documental da D03-14, preservada historicamente na [v0.13](PHASE-III-DECISION-REGISTER-v0.13.md).

### Decisão materialmente delimitada

- Identidade declarada, identidade verificada, sessão, competência e mandato são conceitos distintos; a existência de canal/conta/sessão não concede autorização.
- Separar solicitação, recebimento, validação, autorização, aceite de execução, relato e efeito comprovado. Confirmação de mensagem ≠ autorização ≠ efeito.
- Revogação, suspensão e expiração são verificadas em fonte legítima e com ordem/versão temporal adequadas; não há retroatividade automática sobre efeitos externos nem consentimento por silêncio.
- Divergência, replay, atraso, duplicidade, fonte indisponível ou incerteza de identidade/tempo devem ter estados seguros; atos relevantes não prosseguem sem elegibilidade verificável.
- Risco e proteção crescem de modo proporcional, preservando direitos, privacidade, reservas humanas, evidência L0..L4 e custos fundamentados; classes institucionais não herdam R0–R3 de agentes construtores.
- D03-13 C segue vigente: FCR primeiro na futura supervisão; Telegram, voz, Chief of Staff e relatórios são projeções futuras, dependentes de autorização individual e gates.

[Política Documental de Identidade e Consistência v0.1](PHASE-III-IDENTITY-CONSISTENCY-v0.1.md) detalha **IC-I01..14** e critérios **IC-AC-01..12 PROPOSTOS (L0)**. Estes não criam identidades reais, autenticação, UI, API, testes, canais, provedores, chaves, orçamentos ou mandatos.

### Gate de prontidão

E3-01..04 **EM PLANEJAMENTO**; ADR-C-01..03 **EM ANÁLISE**; CG-01..12 **SEM ACEITE FINAL**; CH-AC/IC-AC/MC/FCR-AC continuam requisitos propostos, sujeitos a convergência e aceitação. **Fase IV NÃO AUTORIZADA.**

## D03-15 — Núcleo Comum de Aceitação com Especializações por Domínio e Canal (C, APROVADA)

**Ratificação expressa do fundador em 2026-10-17:** C, núcleo comum de critérios de aceitação e apenas especializações necessárias por domínio/canal, **preservando evidências, riscos, responsáveis e gates**. A ratificação é do **MÉTODO DOCUMENTAL**; não é aceite de critérios substantivos, redução automática de proteção, execução ou liberação de Fase IV.

### Norma da decisão

- Formar núcleo KAC de invariantes transversais; exceções especializadas SAC são mantidas se há fonte, risco, alçada, prova ou semântica materialmente diferentes.
- Preservar catálogos legados AC/MC/FCR-AC/CH-AC/IC-AC, RG/EL/IM e gates CG/FCG/MG como origens versionadas, rastreáveis sem apagamento ou aceitação automática.
- Propor proprietários funcionais e evidências de aceitação **futuras**, sujeitos a ratificação material. A mesma evidência reutilizada não aprova domínios ou gates automaticamente.
- Não transferir o risco R0–R3 dos agentes construtores para mandatos institucionais. Direitos/privacidade, autoridade humana, revogação e STOP prevalecem sobre qualquer simplificação.
- [Núcleo de Aceitação v0.1](PHASE-III-ACCEPTANCE-CORE-v0.1.md): KAC-01..12, SAC-AUT/MIS/EVD/CST/FCR/CH/IC/BLD e matriz de correspondência; conteúdo **PROPOSTO L0**, incluindo DoR/DoD e donos candidatos.
- A decisão não ratifica stack, dados, orçamento, agentes, infraestrutura, teste, canal, API ou Fase IV.

**Estado:** D03-15 C APROVADA SOMENTE DOCUMENTALMENTE. E3-01..04 EM PLANEJAMENTO e STOP NÃO ATENDIDO; ADR-C-01..03 EM ANÁLISE; CG-01..12 SEM ACEITE FINAL; CH/IC/MC/FCR/KAC/SAC requisitos ainda PROPOSTOS.

## D03-16 — Fatia Vertical Documental Orientada por Riscos e Evidências (C, APROVADA)

**Ratificação expressa do fundador em 2026-10-17:** opção **C**: avançar por uma fatia vertical documental **AUT → MIS → EVD/CST → FCR**, priorizando riscos críticos, evidências e responsáveis e preservando **gates independentes**. Aprova-se SOMENTE o **MÉTODO DE PLANEJAMENTO L0**.

### Recorte obrigatório do método

- **AUT:** autoridade/identidade humana legítima, mandato/limites, direitos e revogação como dependência de qualquer missão; não instalar autenticação.
- **MIS:** distinguir pedido, mandato válido, missão proposta, relato, interrupção e consequência em trânsito; não criar executores.
- **EVD:** exigir proveniência, gradação L0..L4 e evidência independente do efeito; não tomar log/autoavaliação como prova.
- **CST:** tratar custo observado, estimado e desconhecido; Jev exige baseline causal, nunca assumir valores ou teto não ratificado.
- **FCR:** planejar SOMENTE primeira experiência futura de leitura/supervisão com informação legítima, sem interface, comando ou canal integrado.
- **Risco e responsável:** usar severidades qualitativas PROPOSTAS, funções responsáveis CANDIDATAS e casos negativos (autoridade, direitos, custos, efeitos), sem confundir riscos institucionais com R0..R3 dos construtores.
- **Gates:** CG-01..12, FCG/MG e STOP de E3 continuam independentes, sujeitos a evidência/aceite reais posteriores; status não muda por mera cobertura de documento.
- **Não autorizados:** escolha de stack/ADR, número/modelo de agentes, fontes reais, orçamento, autenticação, interface, protótipo, código, integração, testes de sistema, infraestrutura, implementação ou Fase IV.

[Fatia Vertical Documental v0.1](PHASE-III-RISK-FIRST-VERTICAL-v0.1.md) detalha sequência V-01..05, cenários negativos VSC-01..10, riscos, KAC/SAC, evidência futura, owners funcionais propostos, DoR/DoD candidatos e gates; **a política da D03-16 C está APROVADA, mas os artefatos/cenários e critérios continuam PROPOSTOS L0, não aceitos**.

**Estado invariável:** E3-01..04 EM PLANEJAMENTO; suas STOP CONDITIONS NÃO ATENDIDAS. ADR-C-01..03 EM ANÁLISE; CG-01..12 SEM ACEITE FINAL. Nenhum funcionamento ou teste operacional demonstrado. **Fase IV NÃO AUTORIZADA.**

## D03-17 — Contratos Semânticos Mínimos Integrados da Primeira Vertical (C, APROVADA)

**Ratificação expressa do fundador em 2026-10-27:** C, especificar documentalmente contratos mínimos **integrados entre AUT/MIS/EVD/CST/FCR**, contemplando identidade, versões, transições de estados, evidências, direitos, conflitos, indisponibilidade e responsáveis proporcionais ao risco. Essa ratificação **aprova somente o MÉTODO DE ESPECIFICAÇÃO DOCUMENTAL L0**, sem aceitar contratos técnicos, mecanismos ou critérios substantivos.

### Alcance exato da escolha

- **Identidade/mandato:** separar principal alegado, identidade verificada, alçada humana legítima, versão e vigência de mandato. Canal, sessão ou mensagem não conferem competência.
- **Estados:** pedido, recebimento, validação, autorização, aceitação de execução, relato, efeito comprovado, negativa/suspensão/revogação e INCONCLUSIVO/CONFLITANTE são distintos, com evidência específica.
- **Fronteiras:** AUT → MIS para elegibilidade sem execução; MIS → EVD e CST para alegações/provas e custo; EVD/CST → FCR apenas projeção legítima de supervisão. FCR não controla ou executa por si.
- **Tempo/conflitos:** replay, duplicidade, versões divergentes, fonte indisponível, dado stale, revogação concorrente e efeitos em trânsito requerem negação/escalada proporcional ao risco; não presumir consistência tecnológica escolhida.
- **Direitos/evidência:** proveniência, minimização, retificação/retenção legítima, consentimento humano explícito em atos reservados, L0..L4 sem criar provas reais, custo estimado/medido/desconhecido e baseline Jev válido.
- **Risco e governança:** donos FUNCIONAIS PROPOSTOS, SEM-AC candidatos, rastreio KAC/SAC, VSC, E3 e CG independentes; não transferir R0..R3 dos construtores para mandatos institucionais.
- **Não autorizados:** API, endpoint, código, banco, schemas físicos, stack, fornecedores, orquestração, bots, Telegram, voz, autenticação, conta, gasto, infraestrutura, testes de software, implementação ou Fase IV.

[Contratos Semânticos Integrados v0.1](PHASE-III-SEMANTIC-CONTRACTS-v0.1.md) propõe SEM-ENV, SEM-01..12, SEM-AC-01..10 e cenários negativos; os conteúdos são **CANDIDATOS L0 NÃO RATIFICADOS MATERIALMENTE**. [Fatia Vertical v0.1](PHASE-III-RISK-FIRST-VERTICAL-v0.1.md) permanece orientação sem execução.

**Gates permanecem separados:** E3-01..04 EM PLANEJAMENTO; STOP CONDITIONS NÃO ATENDIDAS; ADR-C-01..03 EM ANÁLISE; CG-01..12 SEM ACEITE FINAL; nenhuma solução/teste real demonstrado. **Fase IV NÃO AUTORIZADA.**

## D03-18 — Matriz Integrada de Conflitos, Efeitos em Trânsito, Recuperação e Contingência (C, APROVADA)

**Ratificação expressa do fundador em 2026-10-27:** opção **C**: planejar documentalmente conflitos, efeitos em trânsito, recuperação e contingência de **AUT/MIS/EVD/CST/FCR**, com prioridade proporcional ao risco, **fonte, evidência, dono e gate independente para cada cenário**. A aprovação é **DO MÉTODO DOCUMENTAL L0**, não de medidas materiais, mecanismos de recuperação, aceites ou autorização de execução.

### Norma da escolha

- Consolidar cenários interdomínios de autoridade ilegítima, revogação concorrente, replay, duplicidade, timeout após possível efeito externo, relato sem prova, correção de evidência, custo ausente, privacidade, fonte stale e canal com mensagens contraditórias.
- Distinguir **intenção/recebimento/autorização/elegibilidade/relato/efeito verificado**. Falha ou timeout não prova que ação externa ocorreu ou deixou de ocorrer; proibir repetição ou compensação automática por mera hipótese.
- Para novo ato relevante, fonte AUT e mandato inconclusivos ou revogados não autorizam permissão; atos reservados exigem decisão humana legítima. Efeito passado não é anulado retroativamente por revogação futura.
- Cada risco deve apontar fonte/versionamento/temporalidade, evidência futura, direitos/privacidade, dono FUNCIONAL PROPOSTO e CG/FCG/MG próprio; nunca tratar um documento como aceite de gate ou teste operacional.
- Preservar FCR como futura supervisão por LEITURA, não executor; Telegram/voz/exports condicionais. Separar V-RC..V-RB (triagem institucional proposta) de R0–R3 (construtores).
- Não fixar arquitetura física, API, schema, banco, stack, modelo, agente, SLA, algoritmo de entrega/consenso, orçamento, conta, teste, deploy, código, serviço, Fase IV ou canal real.

[Matriz de Conflitos e Recuperação v0.1](PHASE-III-CONFLICT-RECOVERY-MATRIX-v0.1.md) propõe **CFX-01..16**, **CFX-AC-01..08**, plano de contingência conceitual e crosswalk SEM/KAC/VSC/CG. **A política de integração está aprovada; os mecanismos, cenários, critérios e owners NÃO ESTÃO ACEITOS**.

**Gates preservados:** E3-01..04 EM PLANEJAMENTO e STOP CONDITIONS NÃO ATENDIDAS; ADR-C-01..03 EM ANÁLISE, CG-01..12 SEM ACEITE FINAL, CFX/KAC/SEM apenas PROPOSTOS. **Fase IV NÃO AUTORIZADA**.

## D03-19 — Catálogo Documental Integrado de Provas Negativas por Risco (C, APROVADA)

**Ratificação expressa do fundador em 2026-10-27:** opção **C**: construir catálogo documental integrado de **provas negativas e critérios de aceitação por risco**, vinculando cada **CFX/SEM/KAC** a fonte, evidência, responsável e **gate independente**, mediante **revisão crítica transversal**. A ratificação é **exclusivamente do MÉTODO DOCUMENTAL L0**. Nenhum teste, controle, eficácia ou critério substantivo foi aprovado/realizado.

### Conteúdo e restrições decorrentes da decisão

- Cobrir CFX-01..16, SEM e KAC/SAC da vertical AUT/MIS/EVD/CST/FCR, mantendo os 99 IDs legados como fontes e diferenças materiais por domínio/canal/risco.
- Requerer definição negativa: o que não pode ser afirmado como autorizado, executado, validado, disponível, seguro ou recuperado sem fonte legítima, prova suficiente e autoridade de aceite.
- Vincular **fonte/versionamento/tempo**, direito e finalidade, classe de risco, evidência FUTURA esperada, revisão independente proporcional, owner FUNCIONAL PROPOSTO e gate individual, sem herança entre verificações, domínios, critérios ou gates.
- Distinguir autorrelato/CI de efeito externo realmente verificado; timeout não prova ausência de efeito; replay/duplicidade não garantem idempotência; revogação impede nova autorização, não anula automaticamente efeitos passados; custo ausente não vira zero ou economia Jev; FCR não adquire poder de comando.
- Separar revisão autoral de revisão independente e proibir classificar conteúdo documental L0 como evidência operacional L2–L4, teste/implantação aprovada ou autorização de Fase IV.
- Não fixar stack, banco, API, algoritmo, perfil de agente, número de revisores, orçamento, contas, canal, automação, teste de software, infraestrutura, deploy nem prazos operacionais.

[Catálogo NPV v0.1](PHASE-III-NEGATIVE-PROOF-CATALOG-v0.1.md) especifica **NPV-01..16 e NPV-AC-01..12**, modelo NPV-EVD, revisão transversal RV-01..08 e relação com CFX/SEM/KAC/CG, sempre **PROPOSTOS L0 E NÃO ACEITOS**.

**Gates intocados:** E3-01..04 EM PLANEJAMENTO, STOP CONDITIONS NÃO ATENDIDAS; ADR-C-01..03 EM ANÁLISE; CG-01..12 SEM ACEITE FINAL, FCG/MG sem aceite; KAC/SAC/SEM/CFX/NPV critérios candidatos. **Fase IV NÃO AUTORIZADA.**

## D03-20 — Matriz Transversal de Proveniência, Segregação e Aceites por Risco (C, APROVADA)

**Ratificação expressa em 2026-10-27:** o fundador aprovou **D03-20 C**: elaborar matriz documental TRANSVERSAL de **proveniência, segregação de funções, contestação, estados de evidência e decisões de aceite**, proporcionais ao risco em AUT/MIS/EVD/CST/FCR, com donos responsáveis e gates independentes. **A aprovação é exclusivamente do MÉTODO DOCUMENTAL L0**, não da implementação de mecanismos, prova operacional, testes, pessoas nomeadas ou aceitação dos critérios.

### Determinações preservadas

- Relato/alegação, evidência, contestação, revisão crítica independente, decisão sobre CRITÉRIO, decisão sobre GATE e ato humano reservado permanecem **distintos**; um documento, autoavaliação, hash, check CI ou merge não prova efeito externo.
- Fonte legítima, autoria, versão/temporalidade, direito de uso, finalidade/privacidade, eventual consequência material, custo e estado de incerteza devem ser rastreáveis por risco e critério.
- Segregação de funções proporcional ao risco; **origem/autor da prova não se torna automaticamente revisor independente ou decisor legitimado**. Owners de domínio, risco, revisão e gate aqui são **funções FUTURAS CANDIDATAS**, não pessoas designadas.
- Contestação, correção, retenção e retificação proporcionais a direitos e lei; estados **PROPOSTA_L0, EVIDENCIA_SUBMETIDA, EM_CONTESTACAO, INCONCLUSIVA, REVISAO_DOCUMENTADA e ACEITE FUTURO** não implicam transições implementadas ou evidência realmente coletada.
- Rastreio NPV-01..16, CFX-01..16 e SEM/KAC/SAC, mais 99 IDs legados versionados, com gate CG/FCG/MG próprio, sem herança de prova ou redução automática de requisito especializado.
- Preservar alçada humana para atos reservados, FCR apenas leitura futura, falta de fonte ≠ autorização/custo zero, revogação ≠ reversão automática de efeito externo, R0..R3 construtores ≠ risco institucional.
- Proibido inferir autorização para banco, API, código, agentes, identidade real, ferramenta, canais, workflow, mecanismo de evidência, testes de software, infraestrutura, custo/gasto, deploy ou **Fase IV**.

[Matriz EGV v0.1](PHASE-III-EVIDENCE-GOVERNANCE-v0.1.md) propõe **EGV-01..16**, **EGV-AC-01..12**, **EGV-RV-01..08**, funções e estados semânticos, fontes e critérios. **Os conteúdos substantivos permanecem PROPOSTOS L0, NÃO ACEITOS.**

**Gates/status INALTERADOS:** E3-01..04 EM PLANEJAMENTO e STOP CONDITIONS NÃO ATENDIDAS; ADR-C-01..03 EM ANÁLISE; CG-01..12 SEM ACEITE FINAL; FCG/MG não aceitos. **Fase IV NÃO AUTORIZADA.**

## D03-21 — Matriz de Prontidão DOCUMENTAL por CG e Dependências E3/ADR (C, APROVADA)

**Ratificação expressa do fundador em 2026-10-27:** opção **C**: preparar uma matriz de prontidão estritamente **DOCUMENTAL** dos 12 gates CG-01..12, cruzando E3-01..04 e ADR-C-01..03 com **fontes, responsáveis FUNCIONAIS PROPOSTOS, evidências AUSENTES, decisões humanas necessárias e STOP próprios**. **Todos os gates permanecem PENDENTES até aceites legítimos independentes.** A decisão ratifica SOMENTE o MÉTODO DE PLANEJAMENTO L0, não uma conclusão material de prontidão.

### Escopo autorizado e não autorizado

- Identificar **lacunas por gate** em autoridade, direito/privacidade, requisitos e especializações, integridade de fonte, alternativas arquiteturais, contratos/falhas, alçada humana, custos/Jev, prova independente, FCR/canais, recuperação e transição.
- Distinguir inventário textual L0, prova material futura, designação real de responsáveis, revisão competente, aceite de CRITÉRIO e decisão de GATE, sem herança automática.
- Preservar condições STOP de cada E3-01..04, gates CG-01..12/FCG/MG e análise ADR-C-01..03. Uma coluna com fonte ou link não é evidência validada; um owner funcional não está nomeado.
- Integrar conceitualmente CFX/NPV/SEM/KAC/EGV e os 99 IDs históricos, sem declarar equivalência semântica provada, direitos resguardados em runtime, completude ou teste realizado.
- Requerer decisão humana competente futura e separada para atos reservados e para qualquer transição, mesmo que todo o inventário documental venha a ficar completo.
- NÃO aprovar software, código, agentes, APIs, contas, infraestrutura, fornecedores, padrões técnicos, orçamento, medição financeira real, testes, deploy, execução ou **Fase IV**.

[Matriz de Prontidão v0.1](PHASE-III-GATE-READINESS-v0.1.md) registra **GPR-01..12** por CG, **GPR-AC-01..08** e dependências de E3/ADR, cada qual com estado **PROPOSTO L0 / PROVA_AUSENTE / OWNER_NAO_DESIGNADO / DECISAO_PENDENTE / STOP_ATIVO**, sem falsos verdes.

**STOP inalterado:** E3-01..04 EM PLANEJAMENTO com STOP CONDITIONS NÃO ATENDIDAS; ADR-C-01..03 EM ANÁLISE; CG-01..12 SEM ACEITE FINAL; FCG/MG não aceitos; Fase IV NÃO AUTORIZADA.

## D03-22 — Matriz DOCUMENTAL de Deliberação Humana e Resolução de Lacunas CG (C, APROVADA)

**Ratificação expressa do fundador em 2026-10-27:** opção **C** para produzir uma matriz **estritamente DOCUMENTAL** de deliberação humana, dependências e prioridades qualitativas de resolução das lacunas **CG-01..12**, com **fonte, risco, responsável FUNCIONAL PROPOSTO, impedimentos e escalada**. Manter **todos os aceites E3/CG/ADR e STOPs pendentes**; sem software, testes, gastos ou Fase IV. **Aprovação restrita ao MÉTODO DOCUMENTAL L0**, não aos elementos materiais da tabela.

### Alcance e proibições explícitas

- [Matriz HDM v0.1](PHASE-III-HUMAN-DELIBERATION-v0.1.md) documenta **HDM-01..12 ↔ CG-01..12**, D-HUM-01..08, HDM-AC-01..08 e conflitos de competência com política de escalada SOMENTE PROPOSTA.
- Estabelecer prioridade de investigação/documentação **por classe qualitativa de risco V-RC/V-RA**, sem rankings vinculantes, probabilidade, SLA, cronograma, operação ou reclassificação automática de direitos.
- Relacionar E3-01..04 e ADR-C-01..03 com fontes/contratos KAC/SAC/SEM/CFX/NPV/EGV/GPR e os 99 IDs históricos, sem presumir equivalência material, aceites ou decisão de tecnologia.
- Distinguir produtor de relato, curador de evidência, revisor crítico independente, owner funcional, decisor competente de critério, gate owner e fundador em atos reservados, todos PAPÉIS FUTUROS NÃO NOMEADOS.
- Divergência de competência ou prova, falta de fonte, autoridade revogada, direitos inconclusivos ou efeito externo incerto mantêm `PENDENTE/CONFLITANTE/INCONCLUSIVO` e STOP, **sem concessão de poderes, reenvio ou compensação automática**.
- **Nenhuma decisão material ou implementação** autorizada: nomeação, alçada jurídica, stack, API, serviço, banco, agente, ferramenta, conta, notificação, teste, gasto, deploy e **Fase IV** seguem fora de escopo.

**STOP inalterado:** CG-01..12 e FCG/MG SEM ACEITE FINAL; E3-01..04 EM PLANEJAMENTO com STOP CONDITIONS NÃO ATENDIDAS; ADR-C-01..03 EM ANÁLISE; HDM/EGV/GPR/KAC e critérios materiais PROPOSTOS L0; Fase IV NÃO AUTORIZADA.

## D03-23 — Dossiê único de impasses, contraprovas e decisões humanas FUTURAS (C, APROVADA DOCUMENTALMENTE)
**Ratificação expressa do fundador (2026-10-27): D03-23 C APROVADA somente como método documental L0.** A escolha autoriza apenas o MÉTODO DOCUMENTAL L0 de um dossiê único organizado por risco, dependência, plano condicional de resolução, contraprova FUTURA, papel FUNCIONAL PROPOSTO e decisão humana ainda necessária por CG-01..12. A opção ratificada **não** concede nomeações, mandatos reais, aceites de critério/gate, orçamento, escolhas de stack ou execução; não há transição para Fase IV.
O [Dossiê integrado v0.1](PHASE-III-IMPASSE-DOSSIER-v0.1.md) define IMP-01..12, CONTRA-01..12, PLANO-01..12, DSS-AC-01..10 e impasses IMP-X01..08, **TODOS PROPOSTOS L0**, com fonte, risco, STOP próprio, contraprovas futuras **NOT_RUN**, owner funcional não designado e decisor humano futuro não nomeado. Sem equivalência provada dos 99 IDs históricos e sem aceites de KAC/SAC, E3 ou CG.
**STOP GLOBAL INALTERADO:** CG-01..12/FCG/MG SEM ACEITE; E3-01..04 EM PLANEJAMENTO/STOP CONDITIONS NÃO ATENDIDAS; ADR-C-01..03 EM ANÁLISE; revisão material independente AUSENTE; Fase IV NÃO AUTORIZADA.

## D03-24 — Agenda DOCUMENTAL L0 de caminhos de evidência e decisões humanas por risco/gate (C, APROVADA)
**Ratificação expressa do fundador (2026-10-27): D03-24 C APROVADA SOMENTE COMO MÉTODO DOCUMENTAL L0.** A decisão permite construir uma agenda integrada de perguntas, precedências INFORMACIONAIS, impasses, contraprovas futuras NOT_RUN, donos FUNCIONAIS PROPOSTOS e decisões humanas FUTURAS por CG-01..12. Ela não aprova uma ordem operacional, fonte material, pessoas, critério, gate, arquitetura, ferramenta, orçamento ou nova fase.
[Agenda Integrada v0.1](PHASE-III-EVIDENCE-DECISION-AGENDA-v0.1.md) documenta **AEV-01..12** ↔ **IMP/CG/CONTRA/PLANO-01..12**, **AGE-T01..06** transversalmente, **AGE-AC-01..10 CANDIDATOS**, arestas informacionais PROPOSTAS sem ciclos (e sem herança de aceite), owners NÃO DESIGNADOS e proibições de promoção automática de status.
**STOP GLOBAL INALTERADO:** CG-01..12/FCG/MG SEM ACEITE FINAL; E3-01..04 EM PLANEJAMENTO/STOP CONDITIONS NÃO ATENDIDAS; ADR-C-01..03 EM ANÁLISE; revisores humanos reais e provas materiais AUSENTES. **Fase IV NÃO AUTORIZADA.**

## D03-25 — Inventário de proof obligations por CG e especializações (C, APROVADA DOCUMENTALMENTE)
**Ratificação expressa do fundador (2026-10-27): D03-25 C APROVADA SOMENTE COMO MÉTODO DOCUMENTAL L0.** Autoriza produzir um inventário das provas futuras necessárias por CG e especialização, com fonte candidata, prova AUSENTE, negativa/contraprova NOT_RUN, limitação e revisão humana independente FUTURA, sem aceitar gates, critérios ou permitir implementação.
[Inventário de Proof Obligations v0.1](PHASE-III-PROOF-OBLIGATIONS-v0.1.md): **OPR-01..12** por CG, **OPR-K01..12** por KAC, **8 OPR-SAC** por especializações AUT/MIS/EVD/CST/FCR/CH/IC/BLD, com contraprovas OPN FUTURAS NOT_RUN e **PO-AC-01..10 PROPOSTOS L0**. O conjunto histórico de 99 IDs é mantido sem cotejo individual material, deduplicação ou equivalência presumida. Pessoas e revisores não nomeados; evidência real ausente.
**STOP:** CG-01..12/FCG/MG SEM ACEITE FINAL, E3-01..04 EM PLANEJAMENTO/STOP CONDITIONS NÃO ATENDIDAS, ADR-C-01..03 EM ANÁLISE. **Fase IV NÃO AUTORIZADA.**

## D03-26 — Matriz transversal documental de suficiência/contestação OPR (C, APROVADA)
**Ratificação expressa (2026-10-27): D03-26 C APROVADA SOMENTE COMO MÉTODO DOCUMENTAL L0.** A [Matriz SUF v0.1](PHASE-III-SUFFICIENCY-CONTESTATION-v0.1.md) planeja SUF-01..12/OPR/CG, SUF-K01..12/KAC e oito SUF-SAC, com fonte/limite FUTUROS, contestação NOT_RUN, função de revisor humano independente NÃO DESIGNADA e atos por critério/gate independentes FUTUROS. **SUF-AC-01..10 PROPOSTOS L0**, não aceites. Os 99 IDs históricos seguem sem reconciliação semântica/aceite material. Nenhuma prova, parecer independente, pessoa, gasto ou execução autorizados.
**STOP GLOBAL:** CG-01..12/FCG/MG SEM ACEITE FINAL; E3-01..04 EM PLANEJAMENTO / STOP CONDITIONS NÃO ATENDIDAS; ADR-C-01..03 EM ANÁLISE; KAC/SAC e 99 IDs históricos SEM ACEITE MATERIAL; fontes, provas e revisão humana independente AUSENTES; pessoas NÃO DESIGNADAS. **Fase IV NÃO AUTORIZADA.**

## D03-27 — Registro documental de divergências e escalada humana FUTURA (C, APROVADA DOCUMENTALMENTE)
**Ratificação expressa do fundador (2026-10-27): D03-27 C APROVADA SOMENTE COMO MÉTODO DOCUMENTAL L0.** [Registro DIV v0.1](PHASE-III-DIVERGENCE-ESCALATION-v0.1.md) organiza **DIV-01..12** por CG/OPR/SUF, **DIV-K01..12** por KAC, **8 DIV-SAC** e **DIV-AC-01..10 PROPOSTOS L0**, classes qualitativas de divergência, fontes e negativas FUTURAS NOT_RUN, revisores independentes apenas FUNÇÕES NÃO DESIGNADAS e atos humanos por critério/gate SEPARADOS. Nenhum conflito material foi julgado, nenhuma pessoa nomeada, nenhuma prova coletada, nenhum gate/critério aceito.
**STOP:** CG-01..12/FCG/MG SEM ACEITE FINAL, E3-01..04 EM PLANEJAMENTO / STOP CONDITIONS NÃO ATENDIDAS, ADR-C-01..03 EM ANÁLISE; universo de 99 legados sem reconciliação material. **Fase IV NÃO AUTORIZADA.**

## D03-28 — Dossiê de preparação das deliberações humanas por gate (C, APROVADA DOCUMENTALMENTE)
**Ratificação expressa do fundador (2026-10-27): D03-28 C APROVADA SOMENTE COMO MÉTODO DOCUMENTAL L0.** O [Dossiê DEL v0.1](PHASE-III-HUMAN-DELIBERATION-DOSSIER-v0.1.md) relaciona 12 DEL-CG, 12 DEL-KAC, oito DEL-SAC e **DEL-AC-01..10 PROPOSTOS L0**. Registra alternativas NÃO ESCOLHIDAS, objeções, risco residual qualitativo, fonte/contraprova AUSENTE/NOT_RUN, competências A_DEMONSTRAR e razões explícitas para manter STOP em cada gate. Nenhuma revisão independente REAL foi conduzida nem qualquer critério/gate/ADR aprovado.
**STOP GLOBAL INALTERADO:** CG-01..12/FCG/MG **SEM ACEITE FINAL**; E3-01..04 **EM PLANEJAMENTO / STOP CONDITIONS NÃO ATENDIDAS**; ADR-C-01..03 **EM ANÁLISE**; KAC/SAC e universo declarado de 99 IDs históricos **SEM ACEITE MATERIAL**, sem cotejo semântico individual; fontes e provas materiais AUSENTES, revisores humanos independentes e autoridades reais NÃO DESIGNADOS. **Fase IV NÃO AUTORIZADA.**

## D03-29 — Síntese integrada de razões de NÃO ACEITE (C, RATIFICADA SOMENTE DOCUMENTALMENTE)
**Aprovação expressa do fundador (2026-10-27): D03-29 C SOMENTE MÉTODO DOCUMENTAL L0.** A [Síntese NAC v0.1](PHASE-III-NON-ACCEPTANCE-SYNTHESIS-v0.1.md) consolida NAC-01..12 por CG, NAC-K01..12, oito NAC-SAC, E3-01..04, ADR-C-01..03 e NAC-AC-01..10 CANDIDATOS. Razões explícitas de NÃO ACEITE, fontes/provas AUSENTES, OPN NOT_RUN, risco qualitativo, competências humanas FUTURAS NÃO DESIGNADAS. O método não confere aceite individual/material e não reconcilia os 99 IDs históricos.
**STOP GLOBAL INALTERADO:** CG-01..12/FCG/MG SEM ACEITE FINAL; E3-01..04 EM PLANEJAMENTO / STOP CONDITIONS NÃO ATENDIDAS; ADR-C-01..03 EM ANÁLISE; KAC/SAC e universo declarado de 99 IDs históricos SEM ACEITE MATERIAL, sem reconciliação individual; provas L2–L4 AUSENTES, revisores humanos reais NÃO DESIGNADOS. **Fase IV NÃO AUTORIZADA.**

## D03-30 — Mapa L0 de dependências bloqueantes e NÃO TRANSIÇÃO (C, RATIFICADA SOMENTE DOCUMENTALMENTE)
**Aprovação expressa do fundador (2026-10-27): D03-30 C SOMENTE MÉTODO DOCUMENTAL L0.** O [Mapa BLK v0.1](PHASE-III-BLOCKING-DEPENDENCY-MAP-v0.1.md) organiza **12 BLK-CG, 12 BLK-KAC, oito BLK-SAC, 5 fronteiras NT-01..05, E3-01..04 e ADR-C-01..03**, com obrigações independentes e vetos. Relações de dependência são CANDIDATAS, NÃO são precedências técnicas, aceites herdados ou condições suficientes. **BLK-AC-01..10 PROPOSTOS L0**, nenhum aceite material, revisor independente ou 99 IDs históricos reconciliados.
**STOP GLOBAL INALTERADO:** CG-01..12/FCG/MG SEM ACEITE FINAL; E3-01..04 EM PLANEJAMENTO / STOP CONDITIONS NÃO ATENDIDAS; ADR-C-01..03 EM ANÁLISE; KAC/SAC e universo declarado de 99 IDs históricos SEM ACEITE MATERIAL, sem reconciliação individual; provas L2–L4 AUSENTES, revisores humanos REAIS NÃO DESIGNADOS; Fase IV NÃO AUTORIZADA.

## D03-31 — Inventário documental de atos HUMANOS FUTUROS por NT (C RATIFICADA SOMENTE L0)
**Aprovação expressa do fundador (2026-10-27): D03-31 C APROVADA EXCLUSIVAMENTE COMO MÉTODO DOCUMENTAL L0.** O [Inventário HAT v0.1](PHASE-III-FUTURE-HUMAN-ACTS-INVENTORY-v0.1.md) registra **HAT-01..05 / NT-01..05**, **HAT-CG01..12**, **HAT-K01..12**, **oito HAT-SAC**, quatro E3, três ADR e atos FCG/MG/fase como hipóteses independentes. Fontes e contraprovas AUSENTES/NOT_RUN, revisores independentes apenas FUNÇÕES PROPOSTAS e competência A_DEMONSTRAR. **HAT-AC-01..10 são critérios editoriais L0 PROPOSTOS.** Nenhuma pessoa foi designada ou ato material realizado.
**STOP GLOBAL INALTERADO:** CG-01..12/FCG/MG SEM ACEITE FINAL; E3-01..04 EM PLANEJAMENTO / STOP CONDITIONS NÃO ATENDIDAS; ADR-C-01..03 EM ANÁLISE; KAC/SAC e o universo declarado dos 99 IDs históricos SEM ACEITE MATERIAL, sem cotejo/reconciliação individual; fontes/provas materiais L2–L4 AUSENTES, revisores humanos independentes REAIS NÃO DESIGNADOS. **Fase IV NÃO AUTORIZADA.**

## D03-32 — Legitimidade, independência e contraprova por ato futuro (PENDENTE A/B/C)
- **A:** aprofundar fontes de legitimidade/autoridade AUT/FCR/direitos de terceiros, apenas documental.
- **B:** aprofundar conflitos de efeito externo/recuperação/custo, sem testes ou medições.
- **C:** matriz DOCUMENTAL de requisitos de legitimidade, independência e contraprova por HAT/NT, com fonte ausente, STOP e decisão humana distinta, sem materialidade.
**Recomendação editorial C, NÃO RATIFICADA.** Sem Fase IV, nomeações, gastos ou execução.

## Decisões materiais posteriores ainda não aprovadas

- Priorização de capacidades e formato de MVP; dependências e requisitos de dados reais;
- **Direção modular D03-03 C aprovada**, mas contratos detalhados, serviços físicos, fronteiras de dados e topologia não ratificados;
- **D03-04 C e D03-05 C aprovadas como estratégias:** comparar linguagens com mesmos critérios e fontes de verdade com histórico proporcional; escolhas concretas de linguagem, framework, banco, vetores/RAG, modelos e hospedagem seguem pendentes;
- Tipo, papéis, modelo e número de agentes de engenharia; limite de concorrência;
- Segurança, auditabilidade, privacidade, custos, produtividade, testes e integração;
- Autorização de Fase IV.

**Regra de progresso:** D03-01 A e D03-02..31 C APROVADAS como diretrizes documentais; **D03-32 PENDENTE (A/B/C, somente proposta)**. E3-01..04 EM PLANEJAMENTO, ADR-C-01..03 EM ANÁLISE, CG-01..12 sem aceite final e STOP CONDITIONS NÃO ATENDIDAS. Nenhum mandato real, stack, modelo, agente, quantidade, orçamento ou implementação ratificado.
