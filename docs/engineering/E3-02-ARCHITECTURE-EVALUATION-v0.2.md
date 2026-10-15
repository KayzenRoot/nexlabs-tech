# E3-02 — Avaliação de Arquitetura, Modularização e Stacks v0.2

**Estado:** ANÁLISE DOCUMENTAL. **NENHUMA STACK, LINGUAGEM OU PADRÃO ARQUITETURAL ESCOLHIDO.**
**Autorização:** D03-01 A, sem implementação.
**Depende de:** [E3-01 v0.2](E3-01-CAPABILITY-MAP-v0.2.md); **D03-02 C JÁ APROVOU** o recorte vertical, não a topologia arquitetural.

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

**Comparação qualitativa e condicionada**, não benchmark, ranking ou escolha. A **D03-03 permanece pendente**.

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

**STOP CONDITION E3-02: NÃO ATENDIDA.** Necessárias D03-03 (princípio de fronteiras) e ADRs comparativos de stack com dados suficientes.
