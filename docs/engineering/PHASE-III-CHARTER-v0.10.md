# NexLabs Technology — Carta de Escopo da Fase III v0.10

**Decisões:** D03-01 A — escopo de planejamento documental AUTORIZADO; D03-02 C — primeiro ciclo vertical verificável; D03-03 C — núcleo modular evolutivo com fronteiras extraíveis; e D03-04 C — base principal a escolher por evidências, com especializações condicionais; e D03-05 C — fonte de verdade verificável com histórico proporcional; e D03-06 C — pacote convergente de ADRs interdependentes; e D03-07 C — evidências em camadas, do controlado ao autorizado; e D03-08 C — autonomia graduada por risco e evidências; e D03-09 C — paralelismo elástico guiado por dependências e custo líquido; e D03-10 C — fechamento integrado dos pacotes por gates verificáveis. As dez decisões estão APROVADAS, exclusivamente no plano documental.
**Estado:** FASE III INICIADA, EXCLUSIVAMENTE PLANEJAMENTO DOCUMENTAL. **Nenhum software, infraestrutura ou integração foi autorizado.**
**Repositório canônico:** `KayzenRoot/nexlabs-tech` / `main`.
**Base histórica:** [Carta Institucional v1.0](../institutional/CHARTER-v1.0.md), [Ata de encerramento Fase II](../design/PHASE-II-ACCEPTANCE-v1.0.md), [Síntese canônica da Fase II](../design/PHASE-II-CANONICAL-SYNTHESIS-v1.0.md) e [Proposta de Transição v0.1](../continuity/PHASE-III-TRANSITION-PROPOSAL-v0.1.md).

## 1. Mandato ratificado

O fundador escolheu expressamente a alternativa **A** para D03-01: **autorizar o planejamento documental completo de E3-01, E3-02, E3-03 e E3-04**, sem implementação e sem escolher stack, número de agentes ou arquitetura antes de análises comparativas. Isso substitui somente o *status de autorização* da proposta anterior, não reescreve a proposta histórica nem as decisões D02.

A Fase III está **iniciada** na acepção de documentação. Seus quatro pacotes passam a **EM PLANEJAMENTO**, não a concluídos. Novas escolhas materiais serão registradas com justificativa e aprovação humana quando apropriado.

## 2. Precedência e limites

1. Legislação e direitos, Carta v1.0 e diretrizes ratificadas nas Fases I e II permanecem superiores.
2. Fundador conserva soberania humana legítima e decisões reservadas; Chief of Staff não detém soberania, agentes não são pessoas.
3. Preservar hipóteses, evidências, custo, privacidade, controles legítimos, rastreabilidade e memória como requisitos, não fatos técnicos já operantes.
4. **Permitido:** inventário de requisitos, análises, matrizes e ADRs propostos, avaliação documental de alternativas, mapas de capacidades e módulos candidatos, papéis propostos de agentes construtores, riscos e plano de implantação futuro.
5. **Não permitido:** código, scripts, automações operacionais, protótipos, imagens, assets, telas, implementação de bots ou agentes, RAG, conexão de serviços, alteração de configuração GitHub, credenciais, infraestrutura, CI funcional, execução de benchmarks, instalação de ferramentas ou provisionamento.
6. Não dispensar revisões de segurança, testes e limites de autorização em nome de velocidade.

## 3. Pacotes autorizados

| ID | Pacote | Estado | Referência |
| --- | --- | --- | --- |
| E3-01 | Escopo e capacidades da primeira entrega | EM PLANEJAMENTO | [Mapa v0.10](E3-01-CAPABILITY-MAP-v0.10.md) |
| E3-02 | Fronteiras arquiteturais, stacks e alternativas | EM PLANEJAMENTO | [Arquitetura comparativa v0.10](E3-02-ARCHITECTURE-EVALUATION-v0.10.md) |
| E3-03 | Fábrica de desenvolvimento com agentes e paralelismo | EM PLANEJAMENTO | [Estratégia comparativa v0.10](E3-03-AGENT-FACTORY-EVALUATION-v0.10.md) |
| E3-04 | Segurança, custo, prontidão e gate para implementação | EM PLANEJAMENTO | [Prontidão v0.10](E3-04-READINESS-AND-GATES-v0.10.md) |

## 4. Critérios de saída da Fase III

O encerramento futuro requer cumulativamente:
- decisão expressa do fundador sobre escopo do primeiro incremento e aceitação, com requisitos rastreados à fonte;
- módulos e limites de responsabilidade documentados, com dependências e interfaces definidas apenas como contratos de planejamento;
- tecnologias e arquitetura **selecionadas depois de comparação** de alternativas, risco, custo e migração, com ADRs aprovados;
- agentes de construção, restrições de simultaneidade e custo definidos **depois de avaliação**, sem promessas de ganhos inventados;
- critérios de privacidade, segurança, orçamento, testes, desempenho e evidências para a futura implementação;
- checkpoint consolidado, pendências e riscos explícitos, com recomendação de aceitar/rejeitar prontidão;
- **autorização humana independente para Fase IV**. A conclusão da Fase III não inicia software automaticamente.

## 5. Estado do risco de confidencialidade

Em 2026-10-15 a consulta ao GitHub respondeu `private: false` para este repositório. O trabalho documental pode prosseguir sem dados sensíveis; **a revisão de visibilidade e da classificação dos dados é requisito de prontidão antes de publicar material sensível ou realizar desenvolvimento que o contenha**. Não mudar visibilidade nem expor segredos sem autorização própria.

## 6. Política de velocidade e controle

Preferir **quatro pacotes concentrados**, ADRs mínimos para decisões materiais, um único registro canônico de decisões e revisões proporcionais a risco. Não criar novas work orders burocráticas quando a decisão pode ser registrada claramente em um único documento. Distinguir **PROPOSTO**, **ANÁLISE**, **DECIDIDO** e **VALIDADO**. Meta de desenvolvimento rápido é aspiração a ser medida, não autorização para sacrificar direitos e correção.

## 7. Consolidação após D03-02 C

O primeiro incremento foi **delimitado por estratégia vertical**, ligando orientação do fundador, mandato, evidência e custo com verificabilidade. Essa escolha não decide funcionalidades completas ou módulos físicos. Fonte corrente: [Registro de decisões v0.10](PHASE-III-DECISION-REGISTER-v0.10.md). O registro v0.1 permanece imutável.

## 8. Consolidação após D03-03 C

Aprovada como direção documental: **núcleo modular evolutivo e fronteiras potencialmente extraíveis**, em conformidade com D03-02 C. Não equivale a monólito implantado, microserviços construídos ou contratos técnicos finalizados. Mapas e alternativas detalhados em E3-01..04 v0.3; versões anteriores preservadas.

## 9. Consolidação após D03-04 C

A estratégia documental aprovada favorece **uma base principal selecionada futuramente por critérios e evidências equivalentes entre TypeScript e Python**, com especializações apenas quando justificadas por benefício líquido. Não estabelece linguagem padrão, stack, framework ou número de agentes. Os critérios comparativos e os requisitos de dados constam em E3-01..04 v0.4. As versões históricas continuam preservadas.

## 10. Consolidação após D03-05 C

Foi ratificada a direção de **fonte de verdade verificável e histórico proporcional ao risco e à finalidade**. Integridade de mandatos, proveniência, privacidade e retenção deverão orientar comparações entre dados transacionais, trilhas seletivas e histórico de eventos, sem escolher um banco nem impor event sourcing completo. A comparação será detalhada em E3-01..04 v0.5. As versões históricas permanecem intactas.

## 11. Consolidação após D03-06 C

O fundador aprovou **comparação integrada de stack, persistência e contratos**, documentada em [Pacote Convergente de ADRs v0.4](PHASE-III-CONVERGENT-ADR-PACK-v0.4.md). Os ADR-C-01, ADR-C-02 e ADR-C-03 são **PROPOSTAS EM ANÁLISE**, não escolhas ratificadas. E3-01..04 v0.6 contêm matriz compartilhada de requisitos, dependências e gates. A Fase III continua exclusivamente documental.

## 12. D03-07 C — Evidências em camadas (APROVADA)

A validação futura deverá distinguir requisitos L0, cenários sintéticos rotulados L1, testes controlados realmente executados L2, fontes reais autorizadas L3 e efeitos operacionais comprovados L4. Os níveis **não se promovem automaticamente** e dependem de qualidade, autorização e fontes verificáveis. [Plano documental v0.1](PHASE-III-EVIDENCE-LADDER-v0.1.md). O [Pacote Convergente v0.4](PHASE-III-CONVERGENT-ADR-PACK-v0.4.md) e E3-01..04 v0.7 incorporam os critérios. Nesta fase não foram criados dados nem realizados testes.

## 13. D03-08 C — Autonomia graduada dos agentes construtores

O fundador ratificou planejamento de delegação proporcional a risco, legitimidade e evidência, com salvaguardas humanas reservadas. [Plano de Governança dos Agentes Construtores v0.2](PHASE-III-AGENT-GOVERNANCE-v0.2.md), [ADR Convergente v0.4](PHASE-III-CONVERGENT-ADR-PACK-v0.4.md) e E3-01..04 v0.8 aprofundam níveis R0..R3 candidatos, critérios de aceite L0..L4, dependências, limites de custo e autorização. Nada está implantado e os ADR-C-01..03 seguem EM ANÁLISE.

## 14. D03-09 C — Paralelismo elástico por dependências e custo líquido

O fundador ratificou um **método documental de avaliação** de um baseline sequencial e concorrência variável; a futura escalada depende de contratos estáveis, segurança, capacidade real e redução do tempo até aceitação final com custo total justificado. Referência: [Plano de Paralelismo Elástico v0.1](PHASE-III-ELASTIC-PARALLELISM-v0.1.md); [Governança de Agentes v0.2](PHASE-III-AGENT-GOVERNANCE-v0.2.md); [ADRs Convergentes v0.4](PHASE-III-CONVERGENT-ADR-PACK-v0.4.md); E3-01..04 v0.9.

## 15. D03-10 C — Fechamento integrado por gates verificáveis

Foi ratificado um **método documental** de convergência dos quatro E3, três ADRs interdependentes e limites constitucionais, sem encerrar qualquer pacote por antecipação. A [Matriz de Convergência e Prontidão v0.1](PHASE-III-CONVERGENCE-READINESS-v0.1.md) mantém critérios CG-01..CG-12 e lacunas abertas com evidência L0; [ADRs v0.5](PHASE-III-CONVERGENT-ADR-PACK-v0.5.md), [Governança de Agentes v0.3](PHASE-III-AGENT-GOVERNANCE-v0.3.md) e E3-01..04 v0.10 descrevem recomendações em avaliação e STOP CONDITIONS não atendidas.

**Próximo checkpoint D03-11 (PENDENTE A/B/C):** prioridade da primeira capacidade do Founder Command Center, sem criação de tela ou software. Nenhuma stack, banco, modelo, quantidade, orçamento, agente, serviço, teste, protótipo ou infraestrutura aprovada ou implementada. Fase IV NÃO AUTORIZADA.
