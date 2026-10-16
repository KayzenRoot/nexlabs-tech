# E3-02 — Avaliação de Arquitetura, Modularização e Stacks v0.8

**Estado:** D03-03 C, D03-04 C, D03-05 C, D03-06 C e D03-07 C APROVADAS como direções documentais. Nenhuma linguagem, framework, banco, contrato técnico, topologia, fonte externa, teste ou implementação selecionados/executados.
**Autorização:** D03-01 A, sem implementação.
**Depende de:** [E3-01 v0.7](E3-01-CAPABILITY-MAP-v0.8.md); **D03-02 C JÁ APROVOU** o recorte vertical, não a topologia arquitetural.

## 1. Questões arquiteturais a resolver

1. Qual menor conjunto de capacidades merece fronteiras independentes sem criar complexidade artificial?
2. Quais dados podem ser armazenados, por quem e sob qual autorização?
3. Quais capacidades dependem de serviços externos? Há alternativas offline e modo de degradação honesto?
4. Quais ações precisam ser verificadas, registradas e sujeitas a aprovação humana?
5. Quais custos são fixos ou variáveis por missão, usuário, modelo, volume e armazenamento?
6. Como preservar conhecimento institucional quando agentes, modelos ou fornecedores mudarem?

## 2. Candidatos a avaliar, não decisões

| Alternativa | Potencial benefício | Risco/limite | Evidência exigida |
| --- | --- | --- | --- |
| Monólito modular | Integração simples, menos custo operacional inicial | Acoplamento se fronteiras forem mal definidas | Contratos e prova de isolamento de responsabilidades |
| Serviços desacoplados | Isolamento e escalabilidade independentes quando necessários | Overhead de operação, autenticação distribuída, consistência e custos | Justificativa específica por necessidade comprovada |
| Abordagem híbrida evolutiva | Evolução gradual de módulos para serviços onde necessário | Complexidade de transição | Plano de migração e contratos verificáveis |
| Banco relacional como fonte principal | Integridade e modelo transacional coerente | Modelagem e migração exigem cuidado | Consultas e carga representativas |
| Componentes especializados de busca/contexto | Recuperação de informação específica | Indexação, custo, privacidade, consistência | Qualidade comprovável contra baseline e controles |
| Processamento local, hospedagem remota ou híbrida | Diferentes perfis de custo, privacidade e escala | Disponibilidade, hardware, implantação, segurança | Orçamento comparável e restrições reais |

**Nenhum item é adotado neste documento.** RAG, vetores, filas, containers, modelos e provedores são hipóteses a discutir, não requisitos automáticos.

## 3. Domínios candidatos e contratos conceituais

| Domínio candidato | Responsabilidade a delimitar | Contratos que exigirão estudo |
| --- | --- | --- |
| Autoridade e identidade | Controle de atores, delegações, revogação, atos reservados | Quem pode propor, autorizar, executar, verificar |
| Missões e agentes | Papéis, escopo, objetivos e consequências | Intenção, andamento relatado, prova, revisão |
| Conhecimento institucional | Fontes, validade, proveniência, deduplicação e histórico | Direitos de leitura, retenção, versão, contradições |
| Medição e eficiência | Tokens, custos, baselines, avaliação do Jev | Unidade de medida, origem, comparador, qualidade |
| Financeiro e infraestrutura | Dados econômicos e saúde de recursos | Proveniência, segregação, retenção, falhas de conexão |
| Canais e relatórios | Telegram, voz, PDFs e planilhas | Identidade, consentimento, autorização e limitações |
| Apresentação institucional | Conceitos visuais ratificados da Fase II | Significados acessíveis sem falsa indicação de ação |

Estes são **limites de responsabilidade em discussão**, não módulos aprovados, pastas de código, endpoints, esquemas, telas nem decisões técnicas.

## 4. Método obrigatório de comparação de tecnologias

Antes de selecionar cada família de tecnologia, registrar:
- problema real e alternativas viáveis;
- requisitos que a tecnologia precisa satisfazer;
- maturidade, documentação, licenças, suporte, portabilidade;
- segurança, privacidade e modelo de autorização;
- custo total estimado e condições que alteram o custo;
- complexidade de operação e manutenção por uma equipe humana reduzida;
- limites de integração e dependência de fornecedor;
- desempenho e qualidade que **precisarão** ser medidos após autorização de testes;
- risco de adoção/migração e possibilidade de reversão;
- decisão explícita do fundador quando material.

Propor matriz de avaliação (escala e pesos **a aprovar depois**) sem inventar notas, preços ou benchmarks. Não transformar avaliação preliminar em ranking comprovado.

## 5. ADRs futuros e documentação mínima

Formato recomendado de decisão arquitetural:
- ID, estado (PROPOSTO/ANALISADO/APROVADO);
- contexto, requisitos e fontes;
- duas ou mais alternativas com trade-offs;
- impactos em custo, segurança, velocidade e portabilidade;
- decisão humana expressa e data;
- implicações, plano de migração ou saída;
- condições de revisão, evidência esperada.

Preferir poucos ADRs substantivos a centenas de decisões microscópicas.

## 6. Condições críticas

- O repositório consultado indicou `private: false`. Não armazenar dados sensíveis, chaves, credenciais ou detalhamento confidencial aqui sem decisão de visibilidade e classificação da informação.
- Não alegar que modelos, agentes, serviços ou dados de VPS estão conectados.
- Não aprovar orçamento, servidor, fornecedor, framework ou layout sem análise.
- Reserva de decisões humanas prevista pela Carta é parte do critério de arquitetura.
- Esforço de implementação, testes e migração são desconhecidos até o escopo ser definido.

**STOP CONDITION de E3-02:** ADRs técnicos aprovados, fronteiras e dependências suficientemente claras para orçamento e construção posterior, sem ferramentas instaladas nesta fase. **Ainda não satisfeito.**

## 7. Comparação orientada pelo ciclo vertical, sem escolha de stack (NOVO v0.2)

O recorte D03-02 C introduz necessidades que devem ser satisfeitas independentemente da linguagem: **fronteiras de autoridade, missão, proveniência, classificação de evidências e custo verificado**. O foco de E3-02 é descobrir **qual desenho torna tais fronteiras testáveis e reversíveis com menor custo total**.

### 7.1 Topologias concorrentes para decisão D03-03

| Candidata | Forças qualitativas | Riscos / trade-offs | Condição de avaliação |
| --- | --- | --- | --- |
| A. Monólito modular disciplinado | implantação inicialmente unificada, menos interfaces remotas, configuração mais simples | acoplamento e expansão dependem de contratos internos fortes | responsabilidades isoláveis, menor custo de suporte |
| B. Serviços independentes | isolamentos/deploys separados, escalonamento específico de partes | autenticação distribuída, latência, consistência, operações e CI mais complexos | exigência real de isolamento/escalabilidade independente |
| C. Núcleo modular evolutivo com fronteiras extraíveis | separação lógica sem predeterminar topologia, transição avaliada por evidências | disciplina de contratos e migração futura precisam ser bem definidas | limites mensuráveis de extração e decisão futura justificável |

**Comparação qualitativa histórica:** D03-03 C foi posteriormente APROVADA como direção, sem evidenciar benchmark ou fixar topologia física. As opções A/B permanecem no registro histórico para rastreabilidade.

### 7.2 Linguagens e frameworks candidatos para análise posterior

| Família candidata | Motivo para investigar | Aspecto crítico a validar |
| --- | --- | --- |
| TypeScript + NestJS | arquitetura com módulos, provedores e dependências explícitas, útil para comparar fronteiras de domínio | tempo de entrega real, consumo, interoperabilidade com IA, custo de manutenção |
| Python + FastAPI | validação de contratos HTTP/OpenAPI e possível proximidade com ecossistema científico/IA | padrões de modularidade da equipe, integração, validação, concorrência e manutenção |
| Composição TypeScript/Python | permitir especialização quando mensuravelmente útil, mantendo contrato de integração | custo de duplicar toolchains, observabilidade, testes e operações |

Referências oficiais revisadas em 2026-10-15: [NestJS Modules](https://docs.nestjs.com/modules), [FastAPI Features](https://fastapi.tiangolo.com/features/) e [FastAPI OpenAPI](https://fastapi.tiangolo.com/tutorial/metadata/). São **informações sobre alternativas possíveis**, não aprovação de frameworks, execução de testes ou avaliação de desempenho.

### 7.3 Persistência, interface e observabilidade como escolhas separadas

- **Persistência:** comparar relacional transacional, documentos e alternativas híbridas pela consistência de autorização, proveniência, revisão e custo; não instalar PostgreSQL, document store nem vetores por presunção.
- **Contexto/RAG:** distinguir persistência canônica de recuperação assistida; definir critérios de utilidade, acesso e precisão antes de incluir vetores, índices, cache ou memória inteligente.
- **Experiência do fundador:** a escolha do recorte não decide React, Next.js, Vue, Nuxt, aplicações desktop ou layout. Avaliar alternativas só após casos de uso e limitações de dados.
- **Telemetria:** investigar desenho portátil e rastreabilidade baseada em padrões, como [OpenTelemetry](https://opentelemetry.io/docs/), sem afirmar instrumentação real nem escolha de fornecedor.
- **Deploy/ambiente:** comparar local, nuvem, VPS e híbrido quando existir orçamento, disponibilidade técnica, segurança e metas de recuperação definidas.

### 7.4 Pesos e decisões ainda necessários

Na próxima análise completa, pontuar alternativas com **pesos aprovados futuramente**, por categorias: correção/autorização, segurança/privacidade, custo inicial+recorrente, integração com IA, velocidade de desenvolvimento, facilidade de teste, complexidade operacional, portabilidade e reversibilidade. Informar intervalos e confiança das estimativas. Até lá, **não calcular score numérico, ROI ou preço imaginário**.

**STOP CONDITION E3-02: NÃO ATENDIDA.** As direções D03-03 C e D03-04 C foram aprovadas; faltam comparações conclusivas, ADRs, seleção explícita de tecnologias e validação de contratos/dados.

## 8. Direção arquitetural ratificada D03-03 C (NOVO v0.3)

**Aprovado:** núcleo modular evolutivo com fronteiras extraíveis. **Não aprovado:** monólito implantado, microserviços como forma inicial, distribuição de banco, REST/gRPC/event-bus obrigatórios, containerização, linguagem, ORM, filas, infraestrutura e frameworks.

### 8.1 Responsabilidades candidatas e limites

| Domínio | De que é dono no sentido lógico | O que NÃO pode assumir | Contrato de referência |
| --- | --- | --- | --- |
| AUT | mandatos, autorização, revogação, escopo | decisão de execução ou evidência científica | proposta/autorização/negação com sujeito, finalidade e fonte |
| MIS | intenção e estado reportado de missão | elevar permissões, inventar resultado | missão vinculada a mandato e histórico |
| EVD | fonte, alegação, contradição, avaliação e revisão | declarar custo conhecido sem medição, reautorizar ação | referência a alegação, prova e confiabilidade |
| CST | consumo, origem, estimativa, custo observado, atribuição Jev | equivaler falta de dado a zero e afirmar economia sem baseline | observação com unidade e fonte |
| FCR | consulta contextual e supervisão legítima | contornar domínio AUT ou ler dados fora do mandato | resumo autorizado de missão, fonte, estado e custo |
| AUD/PRV | princípios transversais de rastreio e privacidade | compartilhar dados/segredos sem legitimidade | obrigação e evidência de cumprimento futuro |

As siglas identificam áreas conceituais para avaliação, **não nomes técnicos definitivos de pacotes**. Referências: [E3-01 v0.3](E3-01-CAPABILITY-MAP-v0.3.md).

### 8.2 Critérios para extrair um domínio futuramente

A extração é candidata **somente se houver uma necessidade observada e uma avaliação comparativa**: isolamento comprovadamente insuficiente para segurança; escala ou latência distintas persistentes; custo operacional inferior após separação; ritmo de mudanças realmente desacoplado; necessidade legal ou organizacional; fronteiras de dados testadas; portabilidade e migração controladas.

Antes de qualquer decisão futura de extração, documentar:
- necessidade, alternativa sem extração e baseline verificável;
- contrato, versionamento e comportamento em falha/retry/idempotência (ainda não especificados tecnicamente);
- direitos de acesso, auditoria, consistência, latência e proteções de dados;
- custos de rede, implantação, suporte, teste e rollback;
- verificação de equivalência das regras constitucionais e do vínculo entre missão/evidência/custo.

**Ausência de indicador medido implica manter a questão em análise, não fabricar ganhos percentuais.**

### 8.3 Comparação de stacks candidatas, não seleção

| Dimensão | TypeScript + NestJS como candidato | Python + FastAPI como candidato | Núcleo com base única e especializações condicionais |
| --- | --- | --- | --- |
| Organização modular | módulos/providers e exportações explícitas documentadas pelo projeto NestJS | organização e separação definidas pela equipe, com DI e tipos no FastAPI | fronteiras de responsabilidade independem da linguagem |
| Contratos/documentação | integrações e contratos serão avaliados por ferramentas de tipos e API, sem versão escolhida | especificação OpenAPI e validação documentadas no FastAPI | contratos entre linguagens exigem governança adicional |
| Relação com IA/ciência | acesso via interfaces/SDKs a avaliar | ecossistema científico Python candidato | especialização só quando benefício e custo forem medidos |
| Contrapartida | complexidade de runtime/dependências e competências do time a avaliar | disciplina de modularidade e gestão de dependências a avaliar | custo de dupla cadeia de ferramentas e integração |
| Custo total | desconhecido até cenário, ambiente e preços reais | desconhecido até cenário, ambiente e preços reais | depende de quantos ambientes/idiomas forem necessários |
| Decisão | PENDENTE | PENDENTE | PENDENTE |

**Fontes oficiais para verificação qualitativa de capacidades:** [NestJS Modules](https://docs.nestjs.com/modules), [NestJS Providers](https://docs.nestjs.com/providers), [FastAPI Features](https://fastapi.tiangolo.com/features/). Documentação oficial informa recursos, **não prova ganho de desempenho NexLabs**.

### 8.4 ADRs necessários antes da Fase IV

- ADR-3-01: limites de responsabilidades, forma de extração e acoplamento aceitos conforme D03-03 C;
- ADR-3-02: direção de linguagem/stack principal com alternativas, custos, licenças e disponibilidade;
- ADR-3-03: persistência/consistência e propriedade lógica de dados, com alternativas e segurança;
- ADR-3-04: contratos entre domínios, falhas e migrabilidade, sem protocolo antecipado;
- ADR-3-05: observabilidade, roteamento de IA e custo/Jev, com modelos reais e comparação;
- ADR-3-06: canais futuros, segurança e acesso, incluindo limites para Telegram/voz/VPS/finanças.

**Todos são pendências documentais; nenhum ADR acima é aprovado somente por constar desta lista.**

### 8.5 Histórico da questão D03-04

A decisão D03-04 C foi **APROVADA posteriormente** em [Registro D03 v0.4](PHASE-III-DECISION-REGISTER-v0.4.md), estabelecendo base principal a escolher por evidência e especializações condicionais. Nenhuma tecnologia foi adotada. O registro anterior permanece intacto.

**E3-02 segue EM PLANEJAMENTO. Nenhum benchmark, framework ou topologia física validada.**

## 9. Estratégia de seleção da base principal após D03-04 C (NOVO v0.4)

### 9.1 Protocolo comparativo

Para TypeScript e Python, comparar **o mesmo recorte vertical D03-02 C**, mesmos cenários SR-01..09 de [E3-01 v0.4](E3-01-CAPABILITY-MAP-v0.4.md), riscos, mandatos, dados, complexidade esperada e disponibilidade do time. Usar documentação e análise para qualificar alternativas nesta fase; aferição prática só após autorização apropriada.

Nenhuma vantagem teórica pode receber classificação de desempenho/custo **VALIDADA** sem medição. Não inventar limites de modelos, tempos, memória, preços nem ROI.

| Critério comum | TypeScript (família candidata) | Python (família candidata) | Prova necessária para decisão |
| --- | --- | --- | --- |
| Modularidade e contratos | NestJS documenta módulos/providers e DI; outras opções TS também são possíveis | FastAPI documenta dependências e OpenAPI; modularidade exige convenções explícitas | fronteiras AUT/MIS/EVD/CST/FCR respeitadas |
| Tipagem e validação | tipos estáticos em TS, validação de entrada/execução ainda precisa estratégia | tipos opcionais/gradativos e bibliotecas de validação a avaliar | contratos, entrada malformada e versões de esquema avaliados |
| IA e bibliotecas científicas | compatibilidade por SDKs/integrações a comprovar | compatibilidade por SDKs/bibliotecas a comprovar | requisitos reais e versões suportadas |
| Construção assistida por agentes | toolchain, contexto e lint/teste a estudar | toolchain, contexto e lint/teste a estudar | tempo e custo líquido até aceite |
| Transações e persistência | bibliotecas/clientes a comparar após D03-05 | bibliotecas/clientes a comparar após D03-05 | integridade de mandatos, versões, concorrência e auditoria |
| Suporte/segurança | cadeia de dependências, licenças e correções a estudar | cadeia de dependências, licenças e correções a estudar | política de atualização e vulnerabilidades verificadas |
| Operação | runtime/hospedagem/logging a comparar | runtime/hospedagem/logging a comparar | custo total sob mesma carga/ambiente |
| Portabilidade | contratos, APIs e reversibilidade exigidos | contratos, APIs e reversibilidade exigidos | plano de migração, custos e limitações |
| Resultado | **PENDENTE** | **PENDENTE** | seleção requer ADR e aprovação específica |

**Referências de características, não seleção de stack:** [NestJS Modules](https://docs.nestjs.com/modules), [NestJS Providers](https://docs.nestjs.com/providers), [FastAPI Features](https://fastapi.tiangolo.com/features/). Conferir compatibilidade de versões antes de qualquer desenvolvimento.

### 9.2 Segunda linguagem: exceção condicionada

Aceitar especialização adicional apenas mediante justificativa expressa de:
- uma necessidade técnica do primeiro ciclo não satisfatória de modo economicamente razoável pela base predominante;
- benefício líquido verificável em custo, qualidade, segurança, disponibilidade de biblioteca ou manutenção;
- preço de duplicar dependências, modelos mentais, pipelines, testes, monitoramento e integração;
- contratos que conservem direitos, mandatos, proveniência, sigilo e reversibilidade;
- ADR documentando por que manter uma única linguagem não atende adequadamente.

**Não autorizar automaticamente Python para IA nem TypeScript para interfaces.** A orientação é por evidência, não por convenção de mercado.

### 9.3 Persistência: opções comparadas, nenhuma escolhida

| Alternativa | Força potencial no recorte | Risco/obrigação a analisar | Estado |
| --- | --- | --- | --- |
| Persistência transacional relacional | integridade de relações entre mandatos, missões e custo | modelo de transações, concorrência, migrações e retenção | EM AVALIAÇÃO |
| Histórico de eventos / registro append-only | origem, alterações e histórico de alegações | reconstrução consistente de estado, evolução de eventos e duplicatas | EM AVALIAÇÃO |
| Dados orientados a documentos | objetos/contextos flexíveis, alterações de formato | consistência entre autoridade, missão e evidência, consultas e índices | EM AVALIAÇÃO |
| Modelo híbrido por necessidade justificada | adequação distinta a fonte operacional e histórico | sincronização, custo e complexidade adicional | EM AVALIAÇÃO |
| Recuperação/contexto vetorial como acessório futuro | semântica textual quando comprovadamente útil | acesso, qualidade de recuperação, avaliação e custo; não substitui fonte de verdade | NÃO DECIDIDO |

**PostgreSQL, SQLite, bancos documentais, vetores ou event sourcing são apenas alternativas para análise**, não escolha da NexLabs. O princípio de escolha está proposto para D03-05.

### 9.4 Contratos e segurança independentes do ecossistema

- Semântica de identidade/mandato e reserva de atos AUT como condição de MIS;
- domínios não compartilham implicitamente segredo, armazenamento nem privilégios;
- alegações EVD sempre ligadas a fonte ou declaradas não verificadas;
- informações CST nunca rotulam estimativa como custo real nem economia do Jev sem comparador;
- FCR observa legitimamente dados de fontes identificadas, com transparência sobre ausência/erro;
- observabilidade futura de rastros, métricas e logs deve respeitar proteção de dados e definição de fonte; [OpenTelemetry Signals](https://opentelemetry.io/docs/concepts/signals/) ilustra padrões a avaliar, **não significa adoção**;
- evolução ou extração de domínio exige proposta de migração, versão de contrato, custo, segurança e rollback.

### 9.5 Método de custo e decisão

**Custos a estimar documentalmente**: horas de construção e integração, dependências/licenças, suporte, hospedagem, operação, armazenamento, credenciais e privilégios, observabilidade, regressões, tempo do fundador e consumo de agentes construtores. Estimativas devem indicar período, região, base de comparação e confiança. **Sem orçamento aprovado nem medição real, não existem números da NexLabs a divulgar.**

**Critério de decisão futura:** matriz qualitativa rastreável, pesos e comparações aceitos pelo fundador, ADR com recomendações, riscos e alternativa de saída. Depois disso, seleção expressa de linguagem/framework/banco pode ocorrer, ainda sem código na Fase III.

**Histórico da decisão D03-05:** opção C ratificada posteriormente neste ciclo, registrada em [decisões v0.5](PHASE-III-DECISION-REGISTER-v0.5.md). **E3-02 permanece EM PLANEJAMENTO**, sem banco escolhido.

## 10. Persistência e proveniência após D03-05 C (NOVO v0.5)

**Aprovado como estratégia, não como tecnologia:** fonte de verdade identificável, consistência dos dados críticos e histórico proporcional ao risco, direito e finalidade. Não há obrigatoriedade de event sourcing, uma tabela global de auditoria, Kafka, PostgreSQL, SQLite, NoSQL, logs perenes ou banco vetorial.

### 10.1 Alternativas a comparar com os mesmos invariantes

| Alternativa | Pontos fortes teóricos | Complexidades ou riscos | Critério de decisão |
| --- | --- | --- | --- |
| Fonte transacional + histórico seletivo | decisões e mandatos sob integridade central; trilhas proporcionais | projeto disciplinado de versionamento, retenção e auditoria | consistência e rastreabilidade suficientes com custo menor |
| Event sourcing abrangente | reconstrução de histórico quando eventos são fonte de verdade | evolução de esquema de eventos, replay, duplicatas, privacidade, snapshots e consistência | necessidade justificável de reconstrução completa e custo aceitável |
| Modelo orientado a documentos + controle de versões | flexibilidade de dados heterogêneos | integridade interdomínios, consultas complexas, governança de esquema | adequação comprovável com AUT/MIS/EVD/CST |
| Híbrido controlado | tratamentos específicos para históricos e dados críticos | sincronização, reconciliação, superfície de segurança e operação ampliadas | benefício líquido superior a solução mais simples |
| Índices semânticos/vetoriais auxiliares | busca aproximada quando realmente útil | proveniência, obsolescência, acesso, custo e avaliação de relevância | não substituir nem alterar fontes canônicas |

**Matriz qualitativa preliminar**, não pontuação, benchmark, TCO medido ou adoção. Caso haja conteúdo apagável por direito, “imutabilidade” deve ser tratada com estratégia jurídica/técnica de retenção proporcional, e não como obrigação cega de nunca apagar.

### 10.2 Protocolo semântico de fronteiras, ainda não API

| Relacionamento | Invariante | Falha a tratar futuramente |
| --- | --- | --- |
| AUT → MIS | só autorização válida permite atos que a exigem; revogação tem efeito conforme regra legítima | privilégio obsoleto ou acesso cruzado |
| MIS → EVD | prova vincula alegação, ator e versão sem converter relato em fato | referência ausente, fraude ou evidência contestada |
| MIS → CST | custo mede atividade com unidade e fonte; não cria autorização | falta de preço, duplicata, custo atribuído à missão errada |
| EVD/CST → FCR | resumo autorizado distingue observado, inferido, relatado e não disponível | projeção desatualizada ou transparência enganosa |
| AUD/PRV transversal | retenção e acesso são limitados por finalidade, direitos e autoridade | exposição indevida ou histórico ilegalmente perene |

Não escolher protocolo HTTP, mensagem, transação distribuída ou esquema de eventos nesta etapa.

### 10.3 Contratos, integridade e testes futuros

Antes de selecionar produto de persistência, comparar:
- atomicidade/consistência sob mudanças concorrentes de autorização, missões e custos;
- versão de fonte e histórico de correção sem inventar causalidade;
- políticas de retenção e minimização por categoria, inclusive dados financeiros e documentos de terceiros;
- consulta autorizada e rastreabilidade em domínios posteriormente extraíveis;
- falha/repetição/duplicata, recuperação, reconciliação e migração com custo explicitado;
- confidencialidade: GitHub observado público, não guardar credenciais, dados de clientes ou segredos em documentação aberta;
- necessidade e custo de operação 24/7 apenas quando comprovados, sem confundir requisitos aspiracionais da VPS com disponibilidade real.

### 10.4 Seleção técnica continua pendente

Mesmo que uma abordagem pareça atraente, escolher PostgreSQL, SQLite, documentos, filas ou base vetorial exige ADR próprio com requisitos, alternativas, licença, custos verificáveis e aprovação expressa. **D03-05 C não é preferência ratificada por nenhuma dessas tecnologias.**

**D03-06 C APROVADA:** organizar comparação conjunta de stack, persistência e contratos, documentada no pacote convergente v0.1. E3-02 segue EM PLANEJAMENTO sem tecnologia escolhida.

## 11. Avaliação convergente de ADRs após D03-06 C (NOVO v0.6)

**Referência canônica de análise:** [Pacote Convergente de ADRs v0.1](PHASE-III-CONVERGENT-ADR-PACK-v0.1.md). **ADR-C-01 (stack), ADR-C-02 (persistência) e ADR-C-03 (contratos) estão EM ANÁLISE, não aprovados.**

### 11.1 Visão sintética de alternativas combinadas

| Conjunto comparável | Base candidata | Persistência candidata | Contrato candidato | Trade-off central |
| --- | --- | --- | --- | --- |
| S1 | TypeScript | transacional com histórico seletivo | domínios AUT/MIS/EVD/CST/FCR versionáveis | integração e isolamento vs. complexidade |
| S2 | Python | transacional com histórico seletivo | mesmos invariantes | adequação e manutenção com equipe reduzida |
| S3 | TypeScript | histórico amplo de eventos | semântica temporal e replay | esforço e riscos de privacidade |
| S4 | Python | histórico amplo de eventos | semântica temporal e replay | custo de evolução de eventos e de projeções |
| S5 | base ainda a decidir | híbrido por necessidade | contratos com dono de informação identificável | reconciliação e custo de infraestrutura |
| S6 | base ainda a decidir | documentos versionados | garantias de relacionamento | integridade interdomínios e retenção |

A abordagem conjunta evita **decidir por familiaridade** e depois descobrir que escolha de persistência e contratos cria manutenção ou risco incompatíveis. Nenhuma das seis opções constitui plano ratificado. Não atribuir scores ou percentuais sem informação de custo e requisitos verificados.

### 11.2 Análise de ameaça e consistência por combinação

Todas as opções têm de demonstrar futuramente: impossibilidade de aumento implícito de privilégio; versionamento e revogação de mandato; distinção entre relato e evidência; atomicidade ou compensação justificada quando relevante; cuidado com duplicatas e repetição; dados privados sob tratamento lícito; rastreio do custo com fonte; capacidade de cancelar/reverter mudança; integridade após extração de domínios.

**Event sourcing completo não foi aprovado. Monólito físico, microserviços, APIs, protocolos de mensagens e bancos específicos também não.**

### 11.3 Custos para comparação e fontes necessárias

Comparar, no mínimo: custo de licença e suporte, tempo de engenharia, integração, retenção, armazenamento, testes, autenticação, revisão, tokens de agentes, correção e rollback, migração e operação em ambiente que vier a ser autorizado. Anotar preço/unidade, região, período, data, fonte e estimativa de incerteza. Atualmente todos os números reais de TCO e produtividade da NexLabs estão **indisponíveis**.

### 11.4 Gates do ADR conjunto

- Sem dados, atores e casos de uso aceitos, **não** indicar ranking como resultado verificado.
- Se uma alternativa contradiz mandatos constitucionais ou impossibilita proteção adequada de informações, excluir apenas após fundamentação técnica/jurídica adequada.
- Estabelecer critérios e pesos aceitos antes de pontuar opções.
- Decisão material exige **ratificação humana explícita**, mesmo com a D03-06 já aprovada.
- A Fase IV exigirá autorização distinta e nenhum benchmark real foi autorizado na Fase III.

**D03-07 C APROVADA:** plano de validação em camadas L0–L4, sem criar dados, executar testes ou integrar fontes. **E3-02 EM PLANEJAMENTO.**

## 12. E3-02: critérios de prova por ADR convergente após D03-07 C (NOVO v0.7)

**Fontes atuais:** [Pacote Convergente v0.2](PHASE-III-CONVERGENT-ADR-PACK-v0.2.md) e [Plano de Evidências em Camadas v0.1](PHASE-III-EVIDENCE-LADDER-v0.1.md). São planos de aceitação, não testes executados.

| ADR em análise | L0: o que documentamos | L1/L2: futuros testes autorizados (hipóteses) | L3/L4: prova externa futura, quando aplicável |
| --- | --- | --- | --- |
| C-01 stack | documentação oficial de TypeScript/Python e seus limites; critérios de custo/produtividade | mesmos casos AC, erros, validade de contratos, manutenção sob ambiente equivalente | custo/latência real, disponibilidade de serviços e aceite com fonte |
| C-02 persistência | consistência necessária a AUT/MIS/EVD/CST e política proporcional de histórico | conflitos temporais, versão, revogação, correção, retenção, acesso | integridade/qualidade da informação real, sem converter log em prova do evento externo |
| C-03 contratos | invariantes semânticos, propriedade e extraibilidade | rejeição de autorização indevida, duplicatas, versões incompatíveis, erros e sigilo | confiabilidade de autorização real e evidências efetivamente obtidas sob escopo legítimo |

**L0 não permite ranquear opções como mais rápidas ou confiáveis em produção.** Nem modelos de linguagem nem documentos oficiais constituem benchmark da NexLabs.

### 12.1 Tabela de riscos e custos de prova

- **Custo de testes futuros:** tempo de preparação, execução, revisão, ambiente autorizado, licenças e custo de agentes, não disponível nesta Fase III.
- **Dependência externa:** permissão, estabilidade de API, classificação de dados e preços reais, ainda não verificados.
- **Segurança:** L3 não se inicia só por disponibilidade técnica; exigir titularidade, acesso legítimo, privacidade e aprovação apropriada.
- **Reversibilidade:** contratos e persistência deverão preservar invariantes de mandatos e histórico em qualquer cenário de extração ou migração.
- **Confiabilidade:** mesmo que um cenário controlado passe, a inferência a ambiente operacional é limitada até evidência adequada.
- **Dados sensíveis:** repositório observado público; documentação não deverá incluir chaves, planilhas privadas ou resultados operacionais protegidos.

### 12.2 Próximas pendências materiais

C-01..03 permanecem **EM ANÁLISE e não aprovados**. Faltam critérios finais de aceitação, custos fundamentados, candidatos tecnicamente compatíveis com ferramentas reais, decisões de privacidade, documentação integrada para ratificação material e autorização futura de testes. **D03-08 C APROVADA** posteriormente como política documental; D03-09 PENDENTE. Nenhum framework/banco/contrato técnico foi escolhido.


## 13. D03-08 C: efeitos da autonomia por risco sobre arquitetura e contratos (NOVO v0.8)

**Risco de mudança não implica topologia escolhida.** D03-03 C continua defendendo fronteiras extraíveis, D03-04 C base principal a selecionar por evidências, D03-05 C persistência com histórico proporcional e D03-06 C [ADRs convergentes v0.3](PHASE-III-CONVERGENT-ADR-PACK-v0.3.md). D03-08 C acrescenta deveres de revisão proporcionais, sem selecionar linguagem, banco, protocolo ou serviço.

| Tipo de mudança futura | Risco conceitual | Contrato/segurança a preservar | Política de validação candidata |
| --- | --- | --- | --- |
| documentação isolada | R0 se não alterar norma | histórico e fonte; não reescrever decisões do fundador | revisão documental L0 |
| componente reversível com fronteira estável | R1 apenas após classificação legítima | versão, acesso, testes e dependência | checks realmente executados na futura Fase IV |
| contrato AUT↔MIS ou MIS↔EVD/CST | R2/R3 conforme efeitos | mandato, identidade, temporalidade, propriedade de dados | revisão e autorização proporcionais; testes de falha |
| persistência/retificação/eliminação | R2/R3 conforme dados | integridade, direitos de titulares, proveniência e recuperação | comparações C-02 e revisão de privacidade |
| credenciais, dados sensíveis, deploy/finanças | R3 conforme reserva legal | direito, credencial mínima, orçamento e rollback | decisão humana reservada e verificação adequada |

### Metodologia de contratos interdependentes

- Alteração de contrato shared só deve ser proposta com **matriz de consumidores e impactos**, não por posse de um único agente.
- Extração futura de um domínio depende de equivalência verificável de autenticação, mandato, semântica de evidência, custo e privacidade.
- Compare alternativas S1–S6 também pelo esforço de manter segurança e revisão sob construção concorrente.
- Custos de SDK, migração, armazenamento, revisão, ferramentas e agentes são desconhecidos sem orçamentos e testes permitidos; não inventar TCO.
- Segurança e fonte de verdade têm prioridade sobre velocidade de merge; recusar promessa de integração automática sem CI/controle efetivos.
- Escolha de stack e contrato técnico continua condicionada à posterior ratificação dos ADRs C-01..03 e Fase IV.

**E3-02 EM PLANEJAMENTO. D03-09 PENDENTE.** Não há linguagem, banco, serviços ou APIs aprovados.
