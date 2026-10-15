# NexLabs Technology — Registro de Decisões de Engenharia da Fase III v0.3

**Data:** 2026-10-15. **Fase III iniciada somente para planejamento documental.**
**Autoridade:** [Carta v1.0](../institutional/CHARTER-v1.0.md), [escopo autorizado v0.3](PHASE-III-CHARTER-v0.3.md), [encerramento Fase II](../design/PHASE-II-ACCEPTANCE-v1.0.md).
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

## D03-04 — Direção de Seleção da Stack Principal (PENDENTE A/B/C)

**Pergunta:** considerando a primeira vertical e a direção modular evolutiva, que estratégia de linguagem-base deverá orientar a comparação final das stacks, sem confundir preferência preliminar com framework contratado ou implementado?

- **A. Base TypeScript prioritária:** investigar primeiro opções de núcleo TypeScript (incluindo NestJS como candidato), valorizando consistência de tipos e integração com ferramentas web; admitir componentes especializados somente se comprovadamente necessários.
- **B. Base Python prioritária:** investigar primeiro opções de núcleo Python (incluindo FastAPI como candidato), valorizando bibliotecas de IA/ciência e validação de contratos; admitir componentes especializados somente se comprovadamente necessários.
- **C. Base única escolhida por evidência, especializações condicionais:** comparar primeiro TypeScript e Python pelos mesmos critérios do ciclo, escolher futuramente **uma** base predominante a partir de evidências e justificar uma segunda linguagem apenas quando benefício líquido superar custo de integração. Não adotar stack poliglota por padrão.

**Recomendação editorial C, NÃO APROVADA.** Alternativas qualitativamente comparadas em [E3-02 v0.3](E3-02-ARCHITECTURE-EVALUATION-v0.3.md); faltam aferição de contexto real, custos e disponibilidade de ferramentas. A confirmação de D03-04 será decisão sobre estratégia de avaliação, **não implantação nem seleção automática de frameworks**.

## Decisões materiais posteriores ainda não aprovadas

- Priorização de capacidades e formato de MVP; dependências e requisitos de dados reais;
- **Direção modular D03-03 C aprovada**, mas contratos detalhados, serviços físicos, fronteiras de dados e topologia não ratificados;
- Linguagens, frameworks, banco(s) de dados, vetores/RAG, modelos e hospedagem;
- Tipo, papéis, modelo e número de agentes de engenharia; limite de concorrência;
- Segurança, auditabilidade, privacidade, custos, produtividade, testes e integração;
- Autorização de Fase IV.

**Regra de progresso:** análises E3-01..04 podem continuar documentalmente. D03-01 A, D03-02 C e D03-03 C estão aprovadas. A D03-04 A/B/C permanece **PENDENTE** de escolha expressa; nenhuma sugestão editorial autoriza stack definitiva ou implementação.
