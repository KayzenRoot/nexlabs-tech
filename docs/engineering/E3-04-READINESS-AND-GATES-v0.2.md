# E3-04 — Prontidão, Riscos e Gates para Construção v0.2

**Estado:** PLANO DOCUMENTAL PRELIMINAR, NÃO É APROVAÇÃO DE FASE IV.
**Fonte de autoridade:** D03-01 A, [Carta v1.0](../institutional/CHARTER-v1.0.md), [Fase II encerrada](../design/PHASE-II-ACCEPTANCE-v1.0.md).

## 1. Escopo da prontidão

A Fase III deverá produzir condições auditáveis para iniciar implementação **depois de autorização adicional**. A fase atual não pode criar serviços, instalar dependências, executar testes, alterar visibilidade ou registrar credenciais. Critérios de prontidão dizem respeito à **qualidade dos planos**, não à segurança técnica já comprovada.

## 2. Matriz inicial de riscos a esclarecer

| ID | Risco | Situação factual/documental | Ação de engenharia futura |
| --- | --- | --- | --- |
| R-01 | Visibilidade/confidencialidade GitHub | Metadado retornou `private: false` em 2026-10-15 | Rever classificação, escopo de informação e visibilidade antes de segredos ou dados privados |
| R-02 | Acesso excessivo de agentes | Carta proíbe autoelevação de autoridade | Projetar limites de mandato, separação de funções e autorização humana |
| R-03 | Compromissos financeiros | F0–F4 são princípios, sem poderes operacionais | Orçamento, tetos, proteção de reservas e aprovação de gastos |
| R-04 | Custo de IA e paralelismo | Sem dados reais para comparar | Baseline e orçamento de tokens, custos recorrentes, limites de escala |
| R-05 | Evidência/indicadores fictícios | Identidade conceitual ainda sem telemetria | Distinguir estado sem fonte, estimado e validado |
| R-06 | Vazamento por Telegram/voz | Conexões não existentes | Requisitos de autenticação, privacidade, autorização e consentimento |
| R-07 | Dependência excessiva de fornecedor | Cartas exigem continuidade da memória | Critérios de portabilidade, exportação e substituição |
| R-08 | Arquitetura prematura | D03-02 C aprovou o recorte vertical, mas stack e escopo detalhado ainda não estão decididos | Decidir D03-03, comparar alternativas e aprovar ADRs antes de implementar |
| R-09 | Confusão de autonomia empresarial/construtora | Papéis distintos e futuro sistema não implantado | Separar domínios, riscos, mandatos e recursos |
| R-10 | Burocracia e retrabalho | Fundador prioriza construção eficiente | Limitar gates essenciais, reviews proporcionais e evidência útil |
| R-11 | Ausência de testes reais | Somente planejamento autorizado | Planejar testes e DoD; executar só após nova autorização |
| R-12 | Suposição de disponibilidade de IA | Modelos e quotas variáveis por cliente/conta | Verificar compatibilidade real antes de fixar uso ou preço |

**Estado:** riscos identificados para análise, não incidentes confirmados (exceto observação de visibilidade pública) nem severidades quantitativamente estimadas.

## 3. Critérios futuros de Definition of Ready (antes da Fase IV)

- Carta, síntese visual e requisitos rastreados para cada entrega aprovada.
- MVP explicitamente escolhido, limites do que não será entregue e dados necessários.
- Arquitetura/stacks justificadas em ADRs aprovados, contratos de fronteira e custos estimados.
- Segurança de identidade, autorização, privacidade e tratamento de segredos definida.
- Orçamento e mecanismos de aprovação financeira aprovados por quem possui autoridade.
- Agentes construtores e concorrência escolhidos com estratégia de avaliação, responsabilidades e controles.
- Plano de testes funcionais, integração, segurança e performance, com evidências esperadas.
- Estratégia de rollout, rollback, migração, observabilidade e incidentes proposta e revisada.
- Riscos impeditivos documentados e resolvidos ou formalmente aceitos por autoridade apropriada.
- **Autorização expressa de implementação da Fase IV** registrada separadamente.

## 4. Definition of Done futura para cada incremento de software

Quando Fase IV for autorizada, uma entrega só poderá ser aceita se:
1. escopo, PR/artefato, responsável e requisitos estiverem identificados;
2. testes proporcionais ao risco tiverem sido realmente executados e seus resultados anexados;
3. não houver vazamento conhecido de segredos nem bypass de proteções relevantes;
4. permissões e mandatos humanos forem respeitados;
5. observabilidade e impactos reais forem reportados com fontes, não estimados como fatos;
6. custo e disponibilidade de integrações externas forem descritos honestamente;
7. revisões/correções e comportamento de falha estiverem registrados;
8. aceitação final estiver fundamentada em evidências de implementação e autorizada.

**Essa DoD é uma proposta para futuros desenvolvimentos; não há teste, PR, pipeline ou implementação realizado aqui.**

## 5. Política documental de checkpoints

Após cada pacote E3, atualizar três itens, sem repetição burocrática:
- **Decidido:** escolhas ratificadas com ID e razão;
- **Pendente:** dados, comparações, riscos que faltam;
- **Gatilho de avanço:** critério objetivo para a próxima aprovação.

Em caso de bloqueio documental, corrigir o que couber no chat/GitHub antes de pedir ferramenta externa. Não relaxar direitos, segurança, escopo, orçamento ou rastreabilidade para desbloquear artificialmente.

## 6. STOP CONDITION da Fase III

**Pendência atual:** D03-02 C aprovada como recorte; E3-01 a E3-04 ainda em planejamento, com D03-03 e escolhas técnicas pendentes. A Fase III **não está pronta para encerramento**, e a Fase IV **não está autorizada**.

A futura ata de encerramento de engenharia deverá listar o que foi aprovado, evidência de comparações, riscos remanescentes, mecanismos de validação e autorização independente para início de código. Encerramento nunca resulta automaticamente da existência destes documentos.

## 7. Gates específicos do primeiro ciclo vertical (NOVO v0.2)

**Critério documental de prontidão** é distinto de conformidade executada ou sistema seguro em produção. O fundador aprovou a estratégia vertical, não soluções técnicas.

| Gate | Verificação exigida na futura definição pronta | Estado atual |
| --- | --- | --- |
| G-01 Autoridade | atores, limites, revogação e atos humanos reservados descritos e aceitos | EM PLANEJAMENTO |
| G-02 Missão | identidade de missão, responsabilidade, distinção entre proposta/execução | EM PLANEJAMENTO |
| G-03 Evidência | proveniência, classificação de alegação vs. fato, histórico de revisões | EM PLANEJAMENTO |
| G-04 Custo e Jev | custo observado vs. estimado vs. desconhecido; baseline explícito antes de economia | EM PLANEJAMENTO |
| G-05 Privacidade | categoria de dado, necessidade de tratamento, autorização e retenção | EM PLANEJAMENTO |
| G-06 Arquitetura | alternativas e ADRs, contratos e custo de integração aprovados | PENDENTE DE D03-03 E OUTROS |
| G-07 Agentes construtores | papéis/concorrência e método de benchmark justificados | PENDENTE |
| G-08 Plano de testes | casos AC-01..08 de E3-01 revisados, método de prova e DoD | EM PLANEJAMENTO |
| G-09 Segurança do repositório | avaliar `private: false` e decisão sobre classificação/visibilidade antes de dados sensíveis | PENDENTE DE TRATAMENTO |
| G-10 Autorização de implementação | fundador aceita Fase IV expressamente com escopo e riscos | NÃO AUTORIZADO |

### 7.1 Registro de risco para a vertical

1. **Falso positivo de resultado:** relato sem prova pode parecer missão executada. Mitigação proposta: diferenciação explícita das categorias e fonte.
2. **Bypass de mandato:** uma ordem legítima de consultar pode ser confundida com poder de executar. Mitigação: aprovação humana separada para atos reservados.
3. **Custo enganoso:** zero, ausente, orçamento e gasto efetivo podem ser confundidos. Mitigação: campos semânticos distintos como requisito, sem definir esquema implementado.
4. **Dependência externa prematura:** prometem-se Telegram, nuvem, VPS, voz e finanças sem conexão existente. Mitigação: interfaces apenas candidatas e escopo inicial enxuto.
5. **Concorrência mal dimensionada:** aumento de agentes cria conflitos e custo oculto. Mitigação: critérios quantitativos posteriores e papéis isolados.
6. **Publicação sensível:** GitHub reportou repositório público durante a auditoria. Mitigação: evitar segredos e decidir classificação/visibilidade em gate próprio.

### 7.2 Próximas evidências documentais necessárias

- D03-03 e ADRs de topologia, stacks, persistência e contratos;
- aceitação dos casos de uso e suas informações de origem;
- cenários de negação/revogação, evidência ausente e custo indisponível;
- matriz de licenças, riscos e gastos;
- autorização separada de qualquer dado confidencial e de toda implementação futura.

**STOP CONDITION E3-04: NÃO ATENDIDA. FASE IV continua NÃO AUTORIZADA.** Nenhum gate foi validado por execução de software, teste de segurança ou benchmark.
