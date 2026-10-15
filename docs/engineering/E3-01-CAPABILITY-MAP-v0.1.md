# E3-01 — Mapa de Capacidades e Escopo do Primeiro Incremento v0.1

**Estado:** ANÁLISE INICIAL, NÃO APROVADO COMO ESCOPO FUNCIONAL FINAL.
**Autorização:** D03-01 A permite documentar requisitos e alternativas.
**Fontes:** [Carta Institucional v1.0](../institutional/CHARTER-v1.0.md), [Síntese da Fase II](../design/PHASE-II-CANONICAL-SYNTHESIS-v1.0.md), [adendos completos v0.2](../design/VISUAL-CONCEPT-DECISIONS-v0.2.md), [registro D03](PHASE-III-DECISION-REGISTER-v0.1.md).

## 1. Objetivo

Delimitar **a menor entrega futura capaz de provar valor para o fundador**, preservando mandatos, conhecimento verificável, custo, segurança e expansão. Este documento **não declara serviços existentes**, integrações disponíveis, dados acessíveis ou prioridade aprovada. A primeira entrega será escolhida na D03-02 após comparar cenários.

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

## 5. Três hipóteses de recorte inicial, nenhuma escolhida

**A. Central de supervisão:** validar necessidades do fundador e descrição conceitual dos agentes primeiro; risco de produzir uma camada de apresentação sem fontes reais.

**B. Fundação cognitiva:** definir governança de memória/evidências/mandatos antes da supervisão; risco de prolongar trabalho de infraestrutura sem valor visível.

**C. Recorte vertical verificável:** especificar um ciclo mínimo **orientação legítima → missão delimitada → evidência/resultado → explicação rastreável de custo quando medível**; risco de integração prematura, a controlar por contratos e escopo curto.

Escolha específica **D03-02 PENDENTE**; não usar preferência editorial como prioridade ratificada.

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

- Ratificação D03-02 sobre princípio do primeiro incremento.
- Definir atores reais iniciais e fluxos legítimos, sem supor disponibilidade de dados.
- Delimitar o que será demonstrável sem dependências externas.
- Elaborar casos de aceite, riscos e termos que nunca devem parecer operacionais quando não o forem.
- Aprovar backlog curto do primeiro incremento e mapa de dependências.

**STOP CONDITION:** valor inicial e limites comprováveis documentalmente, aprovado pelo fundador, sem dependências essenciais ocultas. **E3-01 ainda não está concluído.**
