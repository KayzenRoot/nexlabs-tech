# E3-04 — Prontidão, Riscos e Gates para Construção v0.1

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
| R-08 | Arquitetura prematura | Stack não decidida nem MVP delimitado | Aprovar D03-02, comparar alternativas, fazer ADRs curtos |
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

**Pendência atual:** E3-01 a E3-04 ainda em planejamento e D03-02 não escolhido. A Fase III **não está pronta para encerramento**, e a Fase IV **não está autorizada**.

A futura ata de encerramento de engenharia deverá listar o que foi aprovado, evidência de comparações, riscos remanescentes, mecanismos de validação e autorização independente para início de código. Encerramento nunca resulta automaticamente da existência destes documentos.
