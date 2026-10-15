# E3-03 — Estratégia Documental da Fábrica de Desenvolvimento com Agentes v0.1

**Estado:** ANÁLISE COMPARATIVA EM PLANEJAMENTO, SEM ORQUESTRADOR/AGENTES IMPLANTADOS.
**Mandato:** D03-01 A, somente documentação.
**Referências:** [Carta v1.0](../institutional/CHARTER-v1.0.md), [E3-01](E3-01-CAPABILITY-MAP-v0.1.md), [E3-02](E3-02-ARCHITECTURE-EVALUATION-v0.1.md).

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
- Definir papéis necessários para o recorte D03-02 sem fixar número de agentes antecipadamente.
- Concluir plano de avaliação com critérios, thresholds a aprovar e estratégia de rollback.

**E3-03 NÃO CONCLUÍDO.** Nenhum agente, workflow GitHub, sistema de orquestração ou benchmark foi criado/rodado.
