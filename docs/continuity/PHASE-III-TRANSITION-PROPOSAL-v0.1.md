# NexLabs Technology — Proposta de Transição para a Fase III v0.1

**Estado:** PROPOSTA DOCUMENTAL, NÃO RATIFICADA, NÃO EXECUTÁVEL.
**Data:** 2026-10-15
**Origem:** D02-25 C, fechamento da Fase II mediante auditoria.
**Autoridade:** [Carta Institucional v1.0](../institutional/CHARTER-v1.0.md) e [síntese visual da Fase II](../design/PHASE-II-CANONICAL-SYNTHESIS-v1.0.md).
**Fase II:** encerrada documentalmente após aceite e verificação.
**Fase III:** **não iniciada**. Depende de autorização expressa para **planejamento de engenharia**, sem direito automático de implementar.

## 1. Objetivo da Fase III proposta

Transformar os princípios institucionais, o histórico de identidade e os requisitos aspiracionais do fundador em um **plano técnico viável e orçamentariamente controlado**, antes de programar. Encerrar a Fase III com arquitetura, prioridades, fronteiras dos módulos, escolhas de tecnologia justificadas, estratégia de construção paralela e definição mensurável de pronto.

Nenhuma linguagem, framework, plataforma, banco de dados, mecanismo de agentes, modelo de IA, VPS ou serviço é selecionado agora. Todas as alternativas deverão ser comparadas na Fase III com critérios explícitos e decisões humanas.

## 2. Pacotes concentrados de decisões e entregáveis

| Pacote | Questões para decidir na futura Fase III | Entregável proposto | Condição de saída |
| --- | --- | --- | --- |
| E3-01 — Escopo do primeiro produto | Usuários, missão, funções mínimas, requisitos do fundador, critérios de prioridade, dados realmente necessários | Mapa de capacidades e backlog priorizado | Escopo enxuto, fronteiras e resultados verificáveis |
| E3-02 — Arquitetura e stacks | Modular monolith vs. serviços desacoplados, linguagem, frameworks, dados, APIs, modelo de segurança, observabilidade, implantação, licenças, portabilidade | ADRs comparativos, mapa de módulos e contratos de interfaces | Escolhas documentadas com custo/risco/migração e aprovação |
| E3-03 — Fábrica de desenvolvimento | Agentes construtores, responsabilidades, orquestrador, contexto e memória, isolamento de tarefas, paralelismo, revisão, CI, integração e custo de tokens | Plano de execução e benchmark de paralelismo | Ganhos reais e limites demonstrados antes de escalar |
| E3-04 — Prontidão de construção | Plano de incrementos, riscos, segurança, dados, ambientes, orçamento, critérios de aceite e STOP CONDITION | Plano de Fase IV e gate de autorização | Critérios verificáveis, sem dependências abertas impeditivas |

**Regra anti-burocracia:** não criar dezenas de decisões quando uma matriz objetiva ou um ADR consolidado resolver a escolha. Documentar somente o necessário para evitar retrabalho material.

## 3. Áreas de módulos candidatos, não aprovados

As seguintes áreas são **domínios de discussão**, não autorização de software ou arquitetura definitiva:
- Direção e supervisão do fundador, identidade e mandatos dos agentes;
- Missões, coordenação, registros e intervenções sob autoridade legítima;
- Contexto, memória, evidências, versionamento e rastreabilidade;
- Consumo de modelos, tokens, custos e avaliação de eficiência do Jev;
- Visão econômica: despesas, receitas, compromissos, reservas e orçamento;
- Saúde e recursos de infraestrutura/VPS com informação realmente disponível;
- Canal remoto bidirecional Chief of Staff/Telegram, relatórios, PDFs e planilhas;
- Identidades vocais de agentes e possíveis fornecedores ou soluções internas;
- Identidade e experiência de apresentação aprovadas na Fase II;
- Segurança, identidade, autorização, registros, privacidade e auditoria transversal.

Cada domínio poderá ser agrupado, adiado ou separado na Fase III conforme dependências, risco e custo. Evitar fragmentação artificial por microserviços e evitar monólito indistinto: **a arquitetura será decidida comparativamente, não por preferência prévia**.

## 4. Seleção de stacks: método, não decisão agora

Para cada capacidade escolher candidatas e comparar:
1. **Compatibilidade com os requisitos reais** e com a Carta;
2. **Custo inicial e recorrente**, incluído uso de modelos, servidores, licenças, armazenamento e manutenção;
3. **Complexidade de desenvolvimento e operação**, avaliando a realidade de uma equipe humana pequena apoiada por IA;
4. **Segurança, privacidade e tratamento de dados**;
5. **Portabilidade, qualidade das bibliotecas e maturidade**;
6. **Desempenho e limites identificáveis por benchmarks**;
7. **Integração e independência de fornecedores**;
8. **Capacidade de testar e reverter mudanças com segurança**.

Gerar ADR curto por decisão material: contexto, alternativas, critérios, decisão, custos, riscos, plano de reversibilidade e aprovação. **Não anunciar stack preferencial nesta proposta.**

## 5. Agentes de construção e paralelismo

### Hipótese inicial a testar, não configuração ratificada

- Um papel de **coordenação e decomposição de trabalho**;
- **Dois executores paralelos no piloto**, cada um em tarefa e isolamento próprios;
- Ampliação experimental para **até quatro executores** apenas se ganho líquido e qualidade forem demonstrados;
- Funções de teste, revisão e integração podem ser automatizadas ou exercidas por agente especializado, sem implicar todos ativos ao mesmo tempo.

**Quantidade total de agentes e quantidade simultânea são decisões diferentes.** Uma biblioteca de papéis pode ser extensa, mas a concorrência deve ser limitada por riscos de conflito, restrições do modelo/cliente, orçamento e capacidade de integrar resultados.

Exigir antes de aumentar paralelismo:
- Backlog com tarefas independentes e dependências mapeadas;
- Contratos estáveis entre módulos e responsáveis por arquivos;
- Contexto mínimo por tarefa e definição de pronto uniforme;
- Comparação do piloto contra execução sequencial com escopo semelhante;
- Métricas **reais** de tempo de ciclo, retrabalho, falha de testes, custo de tokens e latência de integração;
- Redução comprovada do custo total, não só aumento do volume produzido.

### Regras de aceleração propostas

1. **Tronco estável e mudanças isoladas:** trabalho paralelo por branch/PR ou equivalente autorizado, evitando escrita concorrente em arquivos críticos.
2. **Trabalho em pacotes independentes:** não separar tarefas para apenas aumentar o número de agentes.
3. **CI e aceitação mínima suficientes:** checagens automáticas de segurança e corretude sem burocracia redundante; não dispensar barreiras necessárias.
4. **Revisão direcionada:** revisões baseadas em risco e diffs, preservando inspeção humana em atos reservados.
5. **Contexto reutilizável e verificável:** documentação canônica e histórico, sem inventar memória operante; evitar repetir prompts longos irrelevantes.
6. **Uma meta por iteração:** entregas demonstráveis, checklists de prontidão e STOP CONDITION clara.
7. **Monitorar gargalo real:** mais paralelismo somente se a integração não se tornar o gargalo.
8. **Custo controlado:** determinar orçamento de token/missão, políticas de escolha de modelo após disponibilidade real e medições honestas.

## 6. Restrição financeira e preferência de ambiente

Dar preferência a opções de baixo custo e implantação gradual, avaliando desenvolvimento local e sincronização Git como alternativas. Decisões sobre nuvem, VPS ou serviços pagos são condicionadas a comparação real, disponibilidade, riscos e aprovação. Evitar premissas sobre cotas de planos de IA ou sobre desempenho de modelos não verificados. Nenhuma instalação está autorizada.

## 7. Risco documentado: visibilidade do repositório

O metadado de GitHub lido durante a auditoria informou `private: false` para `KayzenRoot/nexlabs-tech`. **Antes de adicionar dados de finanças, identidades privadas, prompts proprietários, custos sensíveis ou segredos, reavaliar formalmente a visibilidade, a política de dados e os repositórios adequados.** Nunca inserir credenciais em Markdown ou histórico Git. Essa é uma preocupação para a engenharia, não uma autorização para alterar acesso agora.

## 8. Propostas de fases seguintes

- **Fase IV:** desenvolvimento, integração e validação por incrementos curtos e verificáveis, somente após autorização expressa ao encerrar Fase III.
- **Fase V:** verificação operacional, segurança real, custos e disponibilidade medidos, implantação gradual e aprendizado observável.

Não confundir o encerramento conceitual da Fase II com liberação de Fase III ou IV. O fundador deverá aprovar de modo específico o **início da Fase III (planejamento técnico)**. Qualquer criação de software, imagens, produto, conexão externa, infra ou automação exigirá autorização própria e respeitará Carta v1.0.

## 9. Primeiro checkpoint sugerido para próxima autorização

**D03-01 — Autorizar o início do planejamento de engenharia da Fase III, exclusivamente documental, com quatro pacotes E3-01 a E3-04?**

Somente após confirmação: levantar restrições e mapear requisitos, mantendo **todas as stacks, números finais de agentes, tecnologias e decisões de implementação PENDENTES** até análise comparativa. Nenhuma autorização é implícita.
