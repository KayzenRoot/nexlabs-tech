# NexLabs Technology — Matriz Integrada de Convergência e Prontidão v0.13

**Decisão:** D03-10 C — Fechamento integrado por gates verificáveis, ratificada em 2026-10-15.
**Estado:** **PLANO DOCUMENTAL EM ANDAMENTO**, **NÃO ACEITO COMO CONCLUSÃO DOS PACOTES**.
**Autoridade:** [Carta Institucional v1.0](../institutional/CHARTER-v1.0.md), [Fase II encerrada](../design/PHASE-II-ACCEPTANCE-v1.0.md), [Registro D03 v0.13](PHASE-III-DECISION-REGISTER-v0.22.md), [Carta Fase III v0.13](PHASE-III-CHARTER-v0.22.md).
**Dependências documentais:** [E3-01 v0.13](E3-01-CAPABILITY-MAP-v0.22.md), [E3-02 v0.13](E3-02-ARCHITECTURE-EVALUATION-v0.22.md), [E3-03 v0.13](E3-03-AGENT-FACTORY-EVALUATION-v0.22.md), [E3-04 v0.13](E3-04-READINESS-AND-GATES-v0.22.md), [ADRs convergentes v0.8](PHASE-III-CONVERGENT-ADR-PACK-v0.17.md), [Governança de agentes v0.6](PHASE-III-AGENT-GOVERNANCE-v0.6.md), [Evidências L0–L4](PHASE-III-EVIDENCE-LADDER-v0.1.md).

**Não autorizado:** criação de código, imagens, protótipos, dados sintéticos, testes executáveis, APIs, bots/agentes, integrações, automações, infraestrutura ou implantação. Não selecionar stack, banco, linguagem, modelos, serviços físicos, orquestrador, quantidades de agentes nem orçamento sem análise e ratificação específica.

## 1. Princípio de conclusão: gate documental não é teste aprovado

**D03-10 C ratificou a metodologia; não satisfez os gates por decreto.** Cada gate exige uma afirmação delimitada, evidência documental rastreável, lacunas explícitas e revisor/autoridade apropriada. Classificações admitidas:

- **DEFINIDO:** há regra ou direção ratificada, sem medir funcionamento real;
- **DOCUMENTADO, PENDENTE DE ACEITE:** há proposta verificável, mas premissas ou autoridade ainda faltam;
- **BLOQUEADO:** dependência necessária ainda não foi satisfeita;
- **NÃO APLICÁVEL JUSTIFICADO:** aceito por autoridade legítima e com razão rastreável;
- **ACEITO DOCUMENTALMENTE:** somente com critério específico integralmente atendido e autoridade apropriada;
- **TESTADO / VALIDADO OPERACIONALMENTE:** **não permitido atribuir nesta Fase III** por ausência de implementação, teste ou fonte real autorizada.

A STOP CONDITION de cada pacote deve ser julgada **independentemente**; a matriz é um índice de evidências, não aprovação substitutiva.

## 2. Gates integrados CG-01..CG-12, situação observada no planejamento

| Gate | Critério para aceite documental futuro | Pacote/ADR | Evidência L0 disponível | Lacuna atual | Situação |
| --- | --- | --- | --- | --- | --- |
| **CG-01 Autoridade** | atores, mandatos, reserva humana, delegação e revogação especificados e aprovados | E3-01; C-03 | Carta, D03-08 C, AUT candidato | atores/regras finais e casos aceitos | **PENDENTE** |
| **CG-02 Vertical mínima** | conteúdo específico da primeira entrega, fronteiras e exclusões ratificados | E3-01; C-03 | D03-02 C AUT/MIS/EVD/CST/FCR | D03-11 C definiu prioridade progressiva do FCR; faltam escopo detalhado, atores e aceite do MVP | **PENDENTE** |
| **CG-03 Critérios AC** | AC-01..20, RG-01..09, EL-01..10 racionalizados em DoR/DoD rastreável | E3-01; E3-04 | casos propostos, sem testes | critérios finais, aceitação humana e donos | **PENDENTE** |
| **CG-04 Dados e verdade** | dados mínimos, autoridade da fonte, privacidade, histórico e retenção aprovados | E3-01; E3-02; C-02 | D03-05 C, EVD/AUD/PRV | política real de dados e escolha técnica futura | **PENDENTE** |
| **CG-05 Stack** | comparação de base predominante TS/Python por mesma matriz e ADR ratificado | E3-02; C-01 | D03-04 C, S1..S6 candidatos | custos/fontes/licenças e decisão material | **PENDENTE** |
| **CG-06 Contratos** | semântica de AUT/MIS/EVD/CST/FCR, versões, erros e extraibilidade aceitos | E3-02; C-03 | fronteiras lógicas, tabelas de invariantes | contratos finais, política de evolução e ADR | **PENDENTE** |
| **CG-07 Segurança** | acesso mínimo, risco R0..R3, direitos, classificação, retenção e revisão | E3-04; todos | Carta, princípios D03-03/05/08 | política aplicada, revisão de acesso e sigilo | **PENDENTE** |
| **CG-08 Custo/TCO** | categorias, fontes, unidade, período, incerteza e limites orçamentários aprovados | E3-02/03/04 | taxonomia de custos e Jev; nenhuma medição | preços e orçamento legítimos, baseline comparável | **PENDENTE** |
| **CG-09 Agentes** | papéis, controle de mandatos, STOP, verificação, plano S0..S2/SD e condições de escalada | E3-03; C-03 | D03-08 C e D03-09 C, métodos propostos | modelos, capacidade/limites reais e alçadas futuras | **PENDENTE** |
| **CG-10 Evidências** | regra L0–L4, prova por AC, distinção fictício/real e plano futuro de teste aprovados | E3-01/03/04 | D03-07 C e plano documental v0.1 | critérios finais de aferição/independência e aceite | **PENDENTE** |
| **CG-11 Operação reversível** | migração, rollback, observabilidade, suporte, versões e recuperação planejados | E3-02/04; C-01..03 | requisitos candidatos de extração | escolhas reais, impacto e plano de saída | **PENDENTE** |
| **CG-12 Fronteira de fase** | E3/ADRs aceitos, riscos resolvidos e autorização humana independente para **Fase IV** | E3-04; governança | regra constitucional definida | aceites formais, orçamento/segurança, nova autorização | **NÃO AUTORIZADA** |

**Nenhum gate recebeu o status ACEITO nesta matriz.** A ausência de execução ou preço é informação ausente, não zero nem falha de sistema em produção.

## 3. Mapa de dependências e caminho crítico documental

```text
Carta v1.0 e D03-01..10 (já ratificadas como direções)
    │
    ├── CG-01 autoridade + CG-02 recorte de MVP
    │       └── CG-03 AC/DoR/DoD + CG-10 plano de provas
    │
    ├── CG-04 fonte de dados, proveniência, privacidade e retenção
    │       ├── C-02 persistência
    │       └── C-03 contratos e extraibilidade
    │
    ├── CG-05 C-01 stack candidata + CG-06 C-03 contratos
    │       └── CG-08 custos integrais e CG-11 reversibilidade
    │
    ├── CG-07 segurança e riscos ──┬── CG-09 agentes/concorrência
    │                              └── integra os demais gates
    │
    └── CG-12 aceites e autorização humana Fase IV (PENDENTE)
```

Essa representação é **texto documental**, não fluxograma executável, aplicação ou automação. Os estudos de C-01..03 são paralelos no planejamento, mas suas **decisões materiais** precisam ser coerentes em conjunto.

## 4. STOP CONDITIONS por pacote, sem promoção antecipada

| Pacote | Condição necessária de encerramento documental | Evidência faltante principal | Estado |
| --- | --- | --- | --- |
| **E3-01** | requisitos concretos, atores, escopo, AC/DoD/DoR, fontes e autorização conceitual de primeira entrega aceitos pelo fundador | CG-01..04 e CG-10 incompletos; D03-11 C aprovou direção, não AC/atores/DoD | **EM PLANEJAMENTO / STOP NÃO ATENDIDA** |
| **E3-02** | ADR-C-01/02/03 coerentes, comparados por critérios aprovados, riscos, custos, contratos e materialmente ratificados | CG-04..08 e CG-11 incompletos | **EM PLANEJAMENTO / STOP NÃO ATENDIDA** |
| **E3-03** | papéis, políticas, mandatos, contratos de trabalho, custo/revisão, baseline de concorrência e alçadas formalmente aceitos | CG-07..10, ferramentas/capacidade e custos sem confirmação | **EM PLANEJAMENTO / STOP NÃO ATENDIDA** |
| **E3-04** | segurança, privacidade, TCO, DoD e gates de fase avaliados; riscos tratados e condições de autorização de implementação explícitas | CG-07..12 incompletos; Fase IV não autorizada | **EM PLANEJAMENTO / STOP NÃO ATENDIDA** |
| **ADRs C-01..03** | comparação integrada, alternativas, critérios e evidências suficientes, ratificação material separada | dados reais de preço, requisitos aprovados e decisões materiais | **EM ANÁLISE / NÃO RATIFICADOS** |

As STOP CONDITIONS propostas não transformam necessidade de teste operacional futuro em autorização para testá-lo na Fase III. Caso a aceitação documental de E3-04 precise anteceder Fase IV, registrar que **prontidão teórica ≠ implantação aprovada**, e tratar a autorização da Fase IV como gate posterior independente.

## 5. Matriz de comparação técnica integrada (hipóteses L0)

**Todas as opções S1..S6 estão em análise.** Tipo de tecnologia não determina automaticamente privacidade, desempenho ou custo; nenhuma linha é vencedora.

| Combinação candidata | Linguagem predominante | Persistência conceitual | Contratos | Risco a comparar | Custos a estudar |
| --- | --- | --- | --- | --- | --- |
| **S1** | TypeScript | transacional + histórico seletivo | versionáveis por domínio | validação em runtime, isolamento e contratos | toolchain + integrações + manutenção |
| **S2** | Python | transacional + histórico seletivo | mesmos invariantes | concorrência, validação, governança | bibliotecas + integrações + manutenção |
| **S3** | TypeScript | histórico amplo de eventos | temporalidade/projeções | replay, retenção, migração | storage + implementação + operação |
| **S4** | Python | histórico amplo de eventos | temporalidade/projeções | replay, manutenção, consistência | storage + manutenção + suporte |
| **S5** | base ainda a escolher | híbrida justificada por necessidade | direitos de dados e atualização | reconciliação e duplicidade | infra + integrações + dependências |
| **S6** | base ainda a escolher | documentos versionados | relações críticas e segurança | integridade entre domínios | mecanismos complementares de garantia |

**Frameworks/bancos candidatos não são escolhas.** Características observadas em documentação de NestJS/FastAPI ou bancos precisam de revisão atualizada, licenças e adequação ao recorte. Só atribuir scores depois de pesos ratificados e evidências comparáveis. Critérios de veto por mandatos/privacidade superam pontuação de produtividade.

## 6. Contratos semânticos e fonte de verdade (não API)

| Domínio | Informação e autoridade lógica | Dependência | Modo de falha obrigatório no plano |
| --- | --- | --- | --- |
| AUT | mandato, legitimidade, revisão e revogação | Carta e atores | concessão implícita, revogação tardia, privilégio excessivo |
| MIS | intenção, responsabilidade e estados relatado/verificado | AUT | missão executada sem autorização ou marcada concluída sem prova |
| EVD | fonte, qualidade, revisão e histórico proporcional | MIS e política de dados | fonte contestada, duplicata, mudança silenciosa, acesso ilegítimo |
| CST/Jev | custo observado, estimativa, desconhecido e baseline | MIS e fontes de preço | orçamento excedido, ausência equiparada a zero, economia falsa |
| FCR | leitura legítima, incerteza e supervisão pelo fundador | AUT, MIS, EVD, CST | resumo desatualizado, ampliação de direito pela agregação |
| AUD/PRV | classificação, finalidades e retenção/eliminação lícitas | transversal | log permanente ilegal, vazamento, dado pessoal exposto |

Não foram escolhidos endpoints, tabelas, eventos, bancos, filas, protocolos, modelos, layouts ou permissões reais.

## 7. Matriz de TCO, sem números inventados

Cada futura estimativa deverá ter **fonte, data, região, moeda, unidade, hipótese de carga, confiança e horizonte**, separando custo publicado, estimativa e gasto medido. Categorias:

| Área | Componentes a levantar | Dados reais disponíveis aqui |
| --- | --- | --- |
| Engenharia inicial | especificação, implementação futura, revisão, aceitação e integração | NÃO MEDIDOS |
| Modelos e agentes | tokens, cliente, plano, concorrência, falhas, retries, contexto | NÃO MEDIDOS |
| Dados e serviços | storage, backups, retenção, logs, operação, credenciais | NÃO MEDIDOS |
| Segurança e conformidade | análise de riscos, auditoria, privacidade, manutenção | NÃO MEDIDOS |
| Desenvolvimento contínuo | regressões, testes, upgrades, integração e reversões | NÃO MEDIDOS |
| Jev | comparação independente, escopo/qualidade iguais, causalidade | BASELINE NÃO DISPONÍVEL |
| Custo humano | revisão do fundador, operações, decisões, suporte | NÃO MEDIDO |

**Sem orçamento ratificado, não há teto numérico presumido.** Uma fórmula ou score abstrato não é resultado operacional.

## 8. Política da fábrica, custos e revisão

- R0–R3: risco da tarefa, **não** poderes concedidos; L0–L4: qualidade/alcance da prova;
- S0/S1/S2/SD: cenários de comparação de concorrência, **não** quantidades de agentes;
- apenas propor independência de tarefas quando os contratos AUT→MIS→EVD/CST→FCR e autorização forem suficientes;
- propor STOP para mudança de contrato compartilhado não combinada, dado sensível, custo excedido, falha de segurança ou ausência de evidência;
- comparar **tempo até aceite final, custo completo e qualidade**, não produção bruta de código;
- Chief of Staff institucional e agentes construtores são populações distintas;
- nenhum framework de agentes, cliente, modelo padrão, número de executores, ACL, CI ou workflow implantado.

## 9. Requisitos do fundador preservados

**Founder Command Center, Telegram bilateral com Chief of Staff, relatórios PDF/planilhas, vozes distintas de agentes, tokens/custos/Jev, finanças e observabilidade de VPS** seguem registrados como possibilidades e requisitos futuros, não integrações criadas ou fontes monitoradas. A **D03-11 C aprovou a prioridade funcional progressiva** do Founder Command Center em [Plano FCR v0.1](PHASE-III-FOUNDER-COMMAND-CENTER-v0.12.md), sem aprovar sistemas, APIs, telas ou operações.

**Confidencialidade:** o repositório foi observado público em auditorias anteriores. Antes de dados ou credenciais protegidos, avaliar política e visibilidade; não alterar visibilidade sem autorização adequada.

## 10. Próximas ações DOCUMENTAIS e STOP geral

1. D03-11 C aprovada como prioridade funcional do Founder Command Center; detalhar e ratificar fontes, FCR-AC, atores e recorte específico; D03-12 C foi aprovada documentalmente, mas faltam atores, casos MC/AC ratificados e contratos institucionais; D03-13 C APROVADA documentalmente;
2. harmonizar e obter aceites de escopo, atores, AC/DoR/DoD, mandatos e política de dados;
3. levantar informação técnica verificável e custos de candidatos, mantendo ADR-C-01..03 separados para ratificação material;
4. amadurecer os critérios de governança, orçamento, limites e qualidade de agentes sem os criar;
5. revisar segurança, privacidade, riscos e confidencialidade;
6. apresentar propostas de decisão humana com lacunas explícitas e uma possível ata de encerramento **somente após** as condições objetivas satisfeitas.

**STOP CONDITION DESTA MATRIZ: DEFINIÇÃO DOCUMENTAL CONCLUÍDA; FECHAMENTO DOS E3 E FASE III NÃO AUTORIZADO NEM ATINGIDO. Fase IV NÃO AUTORIZADA.** Nenhuma alegação de funcionamento de sistema, teste, modelo, controle ou infraestrutura pode ser derivada desta matriz.

## 11. D03-11 C: atualização auditável dos gates da primeira capacidade FCR (NOVO v0.2)

[Plano Funcional Founder Command Center v0.1](PHASE-III-FOUNDER-COMMAND-CENTER-v0.12.md) registra recorte progressivo com autoridade explícita. Isso resolve a **escolha direcional D03-11**, mas **NÃO encerra o CG-02 ou qualquer outro gate**.

| Gate existente | Efeito efetivo da D03-11 C | Lacuna impeditiva | Estado |
| --- | --- | --- | --- |
| **CG-01** autoridade | decisão humana concebida como origem legítima e revogável | detalhes de atores/mandato e aceitação, D03-12 C aprovada como diretriz, sem contrato material; D03-13 C APROVADA documentalmente | **PENDENTE** |
| **CG-02** primeira vertical | direção FCR progressivo aprovada; requisitos FCR-01..06 descritos | definição final do MVP, exclusões, responsáveis e aceite de AC | **PENDENTE** |
| **CG-03** aceitação | FCR-AC-01..12 candidatos somados a AC/RG/EL históricos | consolidar critérios, eliminar duplicidades, ratificar DoR/DoD | **PENDENTE** |
| **CG-04** fonte e histórico | entrada FCR requer origem/versão/privacidade explícitas | dados e fontes autorizados, política jurídica e mecanismo material | **PENDENTE** |
| **CG-05/06** stack e contratos | condições novas da leitura FCR para ADR-C-01..03 | comparações, versionamento técnico, aprovação de ADR | **PENDENTE** |
| **CG-07** segurança | FCR não amplia privilégio da fonte; supervisão e atos reservados | direitos, ameaça, retenção, alçadas e revisão aceitos | **PENDENTE** |
| **CG-08** custo | distinguir estimado/medido/ausente; Jev com baseline | fontes de custo, moeda/unidade, orçamento, TCO | **PENDENTE** |
| **CG-09** agentes | construtores e institucionais não são a mesma fábrica | papéis e limites reais/ratificação, sem agentes escolhidos | **PENDENTE** |
| **CG-10** evidência | planos L0..L4 sem fingir dados L2/3/4 | aceitação de provas por AC e método de verificação futuro | **PENDENTE** |
| **CG-11** reversibilidade | futuras ações FCR precisam de parada/revogação e estado temporal | plano técnico, contrato, migração e recuperação | **PENDENTE** |
| **CG-12** Fase IV | preserva necessidade de autorização adicional | nenhum aceite global, nenhuma autorização de implementação | **NÃO AUTORIZADA** |

### 11.1 Atualização das STOP CONDITIONS

- **E3-01:** recorte progressivo definido por princípio, mas faltam mandato/atores, direitos, FCR-AC/AC/DoR/DoD ratificados. **NÃO ATENDIDA**.
- **E3-02:** contratos FCR adicionados como candidatos, mas os três ADRs continuam sem decisão material, preço e desenho técnico. **NÃO ATENDIDA**.
- **E3-03:** FCR institucional não pode conferir poder a agentes construtores; aguardam-se limites de autonomia, validação, modelos e custos legítimos. **NÃO ATENDIDA**.
- **E3-04:** privacidade, fontes, alçadas humanas, orçamento e gates de fase sem aceite, implementação proibida. **NÃO ATENDIDA**.

**D03-12 C APROVADA documentalmente** como política dos mandatos institucionais; **D03-13 C APROVADA documentalmente** exclusivamente para política documental dos canais FCR/Chief of Staff. **STOP CONDITIONS E3-01..04 NÃO ATENDIDAS; os 12 gates permanecem sem aceite documental final**; uma direção aprovada não é software, dado ou teste. Nenhum requisito da Carta ou dos adendos foi alterado.

## 12. D03-12 C: matriz de mandatos institucionais e impacto nos CG (NOVO v0.3)

**[Política de Mandatos v0.1](PHASE-III-INSTITUTIONAL-MANDATES-v0.11.md):** autorização legítima, finalidade, escopo, vigência, risco, custo e revogação futuros. **Decisão do método aprovada, mas nenhum dos 12 gates CG foi aceito**. Os níveis L0..L4 continuam sem resultados operacionais.

| Gate | Critério adicional derivado da D03-12 C | Evidência atual | Lacuna para o aceite |
| --- | --- | --- | --- |
| **CG-01** | ator emissor/competência, direitos, mandato temporal e revogação | campos e MC-01..14 propostos | atores concretos, hierarquia material, conflitos e aceite humano |
| **CG-02** | missão inicial sob finalidade delimitada | FCR v0.2 e vertical D03-02/11 C | conteúdo da primeira missão, exclusões, critérios ratificados |
| **CG-03** | conciliar MC-01..14 com AC/RG/EL e FCR-AC | listas L0 documentais | aprovação de DoR/DoD e conflitos/duplicidades resolvidos |
| **CG-04** | versionamento/proveniência/retention lícitos do mandato | D03-05 C e conceitos | política de dados, consentimentos e origem real |
| **CG-05** | avaliar implementação futura de autorização sob stacks candidatas | ADR-C-01 em análise | custos, segurança e comparação material |
| **CG-06** | negar autoelevação, representar expiração, concorrência e revogação | ADR-C-03 em análise | contrato semântico aceito, sem API ainda |
| **CG-07** | mínimo privilégio, poderes reservados, revogação e falhas | política L0, sem controles | política final de identidade/segurança, privacidade, revisores |
| **CG-08** | limites financeiros/fonte, custos de governança e revisões | taxonomia de custos | orçamento/limiar/viabilidade com fonte não conhecidos |
| **CG-09** | distinguir mandato institucional de tarefas dos construtores | D03-08/09 C e política v0.1 | papéis, limites e ferramentas concretos não ratificados |
| **CG-10** | avaliar provas de autorizações, recusa e efeitos | L0, cenários MC escritos | critério e futura validação real sob autorização |
| **CG-11** | expiração/revogação e efeitos em trânsito | descrição de estados | risco de efeitos irreversíveis/compensação/rollback a definir |
| **CG-12** | implementação só após aceites e autorização humana separada | Fase III documental | **Fase IV NÃO AUTORIZADA** |

### 12.1 Critérios de prova e STOP CONDITION

MC-01..14 constituem **hipóteses de aceitação propostas, não aceitas nem executadas**. Nenhum custo observado, agente, tecnologia de autorização, banco ou mecanismo de revogação foi instalado. D03-12 resolve **política de concessão** em alto nível, não os detalhes técnicos, jurídicos ou operacionais.

**Estado:** CG-01..12 PENDENTES; E3-01..04 EM PLANEJAMENTO, STOP CONDITIONS NÃO ATENDIDAS; ADR-C-01..03 EM ANÁLISE, sem ratificação. **D03-13 C APROVADA documentalmente** para política documental de consistência entre canais. Fase IV NÃO AUTORIZADA.

## D03-13 C — Delta de convergência: canais neutros em mandatos (2026-10-17)

**Diretriz APROVADA SOMENTE DOCUMENTALMENTE.** FCR é a primeira experiência futura de supervisão; Chief of Staff, Telegram, voz e relatórios são posteriores e condicionados. Todos devem compartilhar fonte legitimada de autoridade/versão, estados, revogação e direitos. Ver [Política de Canais v0.1](PHASE-III-CHANNEL-GOVERNANCE-v0.9.md).

| Gate existente | Novo ponto de verificação documental ainda ABERTO |
| --- | --- |
| CG-01 | identidade, origem do mandato e impossibilidade de elevação por canal |
| CG-02 | FCR primeiro; demais canais fora da primeira vertical e sem obrigação operacional |
| CG-03 | integrar CH-AC-01..12 com MC/FCR-AC sem redundâncias ou falsas aprovações |
| CG-04 | fonte de verdade, temporalidade, estado defasado, conflito, histórico e privacidade |
| CG-05/06 | ADRs comparáveis também por neutralidade, contrato de confirmações e custo total |
| CG-07 | controle de acesso, exportação, replay, revogação, validação humana e resposta segura a falhas |
| CG-08 | custo de mensagens, identidade, auditoria, canal, armazenamento e suporte sem inventar valores |
| CG-09/10/11 | estratégia de testes futuros, integração e prova de efeito por canal/risco |
| CG-12 | autorização humana de transição por etapa; sem migração automática para Fase IV |

**CH-AC-01..12 são critérios propostos L0; nenhum CG-01..12 passou a aceito**. E3-01..04 continuam EM PLANEJAMENTO e com STOP CONDITIONS NÃO ATENDIDAS. C-01..03 EM ANÁLISE; Fase IV NÃO AUTORIZADA; D03-14 C APROVADA documentalmente.

## D03-14 C — Delta da matriz de gates por identidade, confirmação, revogação e conflito

D03-14 C foi ratificada em **2026-10-17** como **método documental integrado e proporcional ao risco**, sem gates concluídos. [Política IC v0.1](PHASE-III-IDENTITY-CONSISTENCY-v0.8.md) propõe IC-AC-01..12. Todas as lacunas abaixo continuam ABERTAS.

| Gate | Evidência adicional FUTURA que falta | Status |
| --- | --- | --- |
| CG-01 | diferenciar identidade, sessão, principal, competência e mandato verificados; reserva humana | PENDENTE |
| CG-02 | preservar primeira vertical de leitura FCR sem comandos presumidos | PENDENTE |
| CG-03 | racionalizar CH-AC/IC-AC/MC/FCR-AC com AC principais e donos sem perder cobertura | PENDENTE |
| CG-04 | fonte, versões e temporalidade verificáveis com privacidade/histórico proporcional | PENDENTE |
| CG-05 | stack comparada em matriz de segurança, custo, evolução e verificabilidade | PENDENTE |
| CG-06 | semântica de pedido, recebimento, autorização, execução, efeito, erro/replay e conflito nos contratos | PENDENTE |
| CG-07 | negação segura, dados protegidos, atos reservados, revogação concorrente, avaliação proporcional ao risco | PENDENTE |
| CG-08 | custos mensurados/fundamentados de verificações, canais, revisão, auditoria e recuperação | PENDENTE |
| CG-09/10 | estratégia de evidência/testes realmente autorizados para condições negativas, com L0 atual | PENDENTE |
| CG-11 | tratamento de efeitos em trânsito e compensações sem prometer reversão física | PENDENTE |
| CG-12 | autorização independente de Fase IV, sem promoção por completar documentação | PENDENTE |

**IC-AC-01..12 são candidatos documentais L0, não gates aceitos.** E3-01..04 EM PLANEJAMENTO, STOP CONDITIONS NÃO ATENDIDAS; ADR-C-01..03 EM ANÁLISE; Fase IV NÃO AUTORIZADA. **D03-15 C ratificada posteriormente somente como método de racionalização de AC; KAC/SAC continuam PROPOSTOS.**

## D03-15 C — Delta da matriz CG: núcleo KAC e especializações SAC (2026-10-17)

D03-15 C aprova **somente a política DOCUMENTAL L0 de racionalizar critérios comuns sem perda de proteção**. [Núcleo KAC/SAC v0.2](PHASE-III-ACCEPTANCE-CORE-v0.8.md) apresenta KAC-01..12 e SAC específicas, com rastreabilidade dos IDs históricos. **Nenhuma equivalência de prova foi validada, nenhum responsável real designado e nenhum gate promovido.**

| Gates PENDENTES | Rastreio documental proposto | Lacuna que continua ABERTA |
| --- | --- | --- |
| CG-01/02/03 | KAC-01/02/03/05/12 e SAC-AUT/MIS/FCR | donos competentes, recorte MVP e DoR/DoD finais |
| CG-04/05/06 | KAC-04/06/07/09/11 + SAC-IC/EVD | fonte de verdade, stack, contratos e versões não ratificados |
| CG-07/08 | KAC-02/03/07/08 e SAC-CST/AUT | direitos, risco, orçamento e custos sem fontes/aceite |
| CG-09/10/11 | KAC-05/06/09/11/12 e SAC-FCR/BLD | evidência real/testes, integrações e reversibilidade |
| CG-12 | KAC-12, STOP de E3 e autorização humana independente | implementação não autorizada |

**Risco de aceitação aparente:** a redução de duplicações por KAC/SAC NÃO diminui os deveres de evidência, nem aprova CG, FCG, MG, MC, IC, CH ou FCR-AC. Exigir auditoria do mapeamento, diferenciação de responsável e fonte de prova nas especializações antes da eventual consolidação material.

**E3-01..04 EM PLANEJAMENTO, STOP CONDITIONS NÃO ATENDIDAS; ADR-C-01..03 EM ANÁLISE; CG-01..12 SEM ACEITE FINAL; D03-16 C APROVADA documentalmente; Fase IV NÃO AUTORIZADA.**

## D03-16 C — Delta de convergência por fatia vertical e risco (2026-10-17)

A [Fatia Vertical v0.1](PHASE-III-RISK-FIRST-VERTICAL-v0.1.md) foi elaborada sob método D03-16 C **APROVADO somente documentalmente L0**, com etapas V-01..05 e cenários VSC-01..10. Não há gate CG aprovado nem teste de sistema. O risco crítico lidera a análise, mas direitos e obrigações transversais continuam em toda etapa.

| Gate, TODOS PENDENTES | Etapas e lacunas documentais priorizadas | Exigência independente antes de futuro aceite |
| --- | --- | --- |
| CG-01 | V-01; VSC-01/02/03 e identidade/mandato | alçada legítima e reserva humana, fonte e escopo ratificados |
| CG-02 | V-02/V-05; limites da primeira vertical | missão e FCR de leitura claramente definidos sem comandos |
| CG-03 | V-02..05; KAC/SAC e correlação de evidência | rastreio de origem, ausência de critérios perdidos e aceites individualizados |
| CG-04 | V-01/V-03; versões, retenção, revogação | fonte de verdade e risco temporal/privacidade avaliados |
| CG-05 | V-01..05 como requisitos | alternativas de stack comparáveis sem vencedor presumido |
| CG-06 | estados entre V-01..05; VSC-03/07 | contratos e conflitos definidos, ADR-C-03 ainda não ratificado |
| CG-07 | VSC-01/02/03/05/07/09 | direitos, atos reservados, revogação e negativa segura revisados |
| CG-08 | V-04, VSC-02/06 | custos/limites/baselines com fontes, não quantias inventadas |
| CG-09 | VSC-01..10, efeitos negativos | estratégia de evidência e validação futura com L0 atual explícito |
| CG-10 | V-05 e integrações condicionais | aceites próprios de canal/identidade e direitos sem ativação |
| CG-11 | V-02/V-03, VSC-03/07/08 | consequências em trânsito, correção e possível compensação |
| CG-12 | todos os V e E3; soberania humana | transição por autorização separada, nunca aprovação tácita |

**DoR/DoD documental por pacote é PROPOSTO**, não está comprovado; owners funcionais não são nomeados. A prioridade V-RC/V-RA não transfere risco R0..R3 dos agentes construtores. **E3-01..04 EM PLANEJAMENTO, STOP CONDITIONS NÃO ATENDIDAS; ADR-C-01..03 EM ANÁLISE; CG-01..12 SEM ACEITE; D03-17 C APROVADA documentalmente; Fase IV NÃO AUTORIZADA.**

## D03-17 C — Delta de convergência dos contratos semânticos (2026-10-27)

**Aprovado o MÉTODO DOCUMENTAL L0**, nunca gate ou implementação. [SEM v0.1](PHASE-III-SEMANTIC-CONTRACTS-v0.3.md) acrescenta SEM-ENV, SEM-01..12 e SEM-AC-01..10 CANDIDATOS, cruzando V-01..05, VSC-01..10 e KAC/SAC.

| Gate CG (TODOS SEM ACEITE) | Contratos e evidência FUTURA exigida | Lacuna não resolvida |
| --- | --- | --- |
| CG-01/02 | SEM-01/02, direitos, alçada, leitura FCR | identidade material e MVP/atores ainda não ratificados |
| CG-03/04 | SEM-03/07/08, origem/versão/limites de evidência | fonte de verdade e aceites de dados históricos pendentes |
| CG-05/06 | SEM-ENV/02..06/08, comparação de contratos e alternativas | ADR-C-01..03 em análise, sem tecnologia nem API definida |
| CG-07 | SEM-02/06/08/09/10, reserva humana, replay, privacidade | legislação, responsáveis, controles e testes futuros ausentes |
| CG-08 | SEM-04, custo medido/estimado/ausente e Jev | fontes, valores e limites financeiros não aprovados |
| CG-09/10 | SEM-03/05/11/12, prova independente e canais autorizados | evidência operacional L2+ e avaliação de canal não executadas |
| CG-11 | SEM-02/03/08/10, revogação em trânsito e consequência | reversibilidade/recuperação material não comprovadas |
| CG-12 | todos os SEM, DoR/DoD e ato fundador | fase IV depende de autorização independente explícita |

**SEM-AC, CG, FCG/MG, KAC/SAC NÃO ACEITOS.** E3-01..04 EM PLANEJAMENTO e STOP CONDITIONS NÃO ATENDIDAS; ADR-C-01..03 EM ANÁLISE; D03-18 C ratificada posteriormente como método documental; **Fase IV NÃO AUTORIZADA**.

## D03-18 C — Critérios de prontidão perante conflitos e recuperação interdomínios (2026-10-27)

[Matriz CFX v0.1](PHASE-III-CONFLICT-RECOVERY-MATRIX-v0.2.md) aplica o método DOCUMENTAL aprovado D03-18 C, com CFX-01..16 e CFX-AC-01..08 PROPOSTOS. **Nenhum gate passou a aceito**. Fonte, evidência FUTURA, dono FUNCIONAL PROPOSTO e aceitação independente são requisitos para cada caso.

| Gate CG (TODOS PENDENTES) | Lacuna crítica acrescentada | Prova FUTURA e aceite independente |
| --- | --- | --- |
| CG-01 | CFX-01/03/14: fonte de AUT ilegítima/indisponível | alçada humana e estado válido, sem canal conceder poder |
| CG-02 | CFX-11/13: FCR apenas leitura e exibição stale | escopo de MVP, direitos e estados reconhecíveis |
| CG-03 | CFX-05/07/16: relato vs efeito e equivalência falsa | origem, critério histórico e revisão de não regressão |
| CG-04 | CFX-02/04/08/15: temporalidade, versão e retificação | fonte, histórico proporcional e direitos |
| CG-05 | CFX-04/06/15: alternativas de controle de falhas | comparação ADR-C-01 com custo/segurança e riscos |
| CG-06 | CFX-04/06/14: mensagens duplicadas, timeouts e indisponibilidade | semântica de conflitos/retries sem promessa de atomicidade |
| CG-07 | CFX-01/02/03/12/13: atos reservados, revogação, privacidade | negação segura, revisão humana, direitos e riscos |
| CG-08 | CFX-09/10: custo desconhecido e limites sem fonte | unidade/competência financeira/baseline sem inventar valores |
| CG-09 | CFX-05/07/08/16: prova independente e revisão negativa | estratégia de teste FUTURO, sem alegar L2–L4 |
| CG-10 | CFX-08/11/12/13: apresentação/canal e acesso | gates por canal, proteção de terceiros e incerteza visível |
| CG-11 | CFX-02/04/06/15: ação em trânsito e efeito irreversível | plano de consequências/compensação CONCEITUAL e direitos |
| CG-12 | todos, sobretudo CFX-03/13/16 | autorização Fase IV separada e aceites legitimados |

**E3-01..04 EM PLANEJAMENTO; STOP CONDITIONS NÃO ATENDIDAS; ADR-C-01..03 EM ANÁLISE; CG-01..12 SEM ACEITE FINAL.** CFX/KAC/SEM/FCG/MG não aceitos. Próxima D03-19 C APROVADA documentalmente; Fase IV NÃO AUTORIZADA.

## D03-19 C — Provas negativas candidatas, sem herança de aceite (2026-10-27)

[Catálogo NPV v0.1](PHASE-III-NEGATIVE-PROOF-CATALOG-v0.4.md) é produto do método DOCUMENTAL D03-19 C APROVADO, mas **NPV-01..16, NPV-AC-01..12 e RV-01..08 NÃO ACEITOS/NÃO EXECUTADOS**. Cada CG abaixo requer sua própria avaliação competente e fontes FUTURAS, não apenas um documento ou uma única evidência.

| Gate, todos PENDENTES | Negativos NPV candidatos e riscos | Provas/aceites MATERIAIS faltantes |
| --- | --- | --- |
| CG-01 | NPV-01/03/10/14, poder e alçada | fonte de identidade/mandato competente e reserva humana |
| CG-02 | NPV-11/13, limites da primeira vertical FCR | recorte, leitura legítima e estados de incerteza aprovados |
| CG-03 | NPV-05/07/16, autorrelato/equivalência | fontes e critérios históricos com revisão de não regressão |
| CG-04 | NPV-02/04/08/15, versão/retificação | fonte verdadeira, causalidade temporal e direitos |
| CG-05 | NPV-04/06/15, arquitetura perante falha | opções ADR-C-01 realmente comparadas e ratificadas |
| CG-06 | NPV-04/06/14, replay/timeout/cache | contratos e alternativas ADR-C-03 julgadas por risco |
| CG-07 | NPV-01/02/03/10/12/13, soberania e direitos | revisão legal/humana competente e negação segura |
| CG-08 | NPV-09/10, custos e limites | fontes e valores medidos/estimados válidos, baseline legítimo |
| CG-09 | NPV-05/07/08/16, evidência e testes | programa futuro autorizado e revisão independente |
| CG-10 | NPV-08/11/12/13, informações e canais | proteção de terceiros, acesso, aceites por canal |
| CG-11 | NPV-02/04/06/15, efeitos em trânsito | consequência externa, compensabilidade, versão/reversão |
| CG-12 | NPV-03/13/16, separação de gates | ato humano específico e autorização autônoma de Fase IV |

**Fonte de autoridade, dono FUNCIONAL PROPOSTO, evidência futura e gate são necessários por linha.** Conexão CFX/SEM/KAC não prova equivalência nem aceite. E3-01..04 EM PLANEJAMENTO, STOP CONDITIONS NÃO ATENDIDAS; ADR-C-01..03 EM ANÁLISE; CG-01..12 SEM ACEITE, FCG/MG pendentes. **D03-20 C APROVADA documentalmente; Fase IV NÃO AUTORIZADA.**

## D03-20 C — Matriz de evidências e aceites distintos por CG (2026-10-27)

[Matriz EGV v0.1](PHASE-III-EVIDENCE-GOVERNANCE-v0.3.md) foi elaborada sob método DOCUMENTAL D03-20 C aprovado. Seus EGV-01..16, EGV-AC-01..12 e EGV-RV-01..08 são **PROPOSTOS L0**, com donos funcionais e fontes FUTURAS não designados/medidos. Cada **CG continua SEM ACEITE FINAL**, mesmo que compartilhe alegação ou referência.

| Gate CG PENDENTE | Questão de governança da prova e independência | Lacuna aberta de aceite MATERIAL |
| --- | --- | --- |
| CG-01 | EGV-01/03/10/14: principal e competência independentes de canal/relato | fonte AUT legítima e alçada humana nomeada |
| CG-02 | EGV-11/13: fonte da projeção FCR e limites de leitura | escopo MVP/participantes com direitos aprovados |
| CG-03 | EGV-05/07/16: prova de efeito e manutenção dos legados | revisão de equivalência, owners de risco e DoR/DoD |
| CG-04 | EGV-02/04/08/15: tempo, contestação e retenção | política efetiva de dados, direitos e fonte de verdade |
| CG-05 | EGV-04/06/15: opções técnicas para não regressão | ADR-C-01 comparado e ratificado, sem stack escolhida |
| CG-06 | EGV-04/06/14: proveniência em replay/indisponibilidade | contratos de falha e ADR-C-03 não ratificado |
| CG-07 | EGV-01/02/03/12/13: alçada e privacidade | reserva humana e critérios legais aceitos |
| CG-08 | EGV-09/10: custos, limite e Jev sem inferências | medição/autorização/baseline válidos e revisados |
| CG-09 | EGV-05/07/08/16: efetividade e revisão independente | provas L2+ futuras autorizadas e juízo de assurance |
| CG-10 | EGV-08/11/12/13: leitura e canal condicionado | direitos, proveniência, estados e aceites próprios |
| CG-11 | EGV-02/04/06/15: efeitos em trânsito/reversibilidade | evidência externa de consequência e decisão competente |
| CG-12 | todos: gate ≠ critério ≠ autorização de fase | decisão soberana específica, STOP dos pacotes não resolvidos |

**Revisão autoral de documentos não é review independente; status CI de Markdown não prova controle.** E3-01..04 EM PLANEJAMENTO, STOP CONDITIONS NÃO ATENDIDAS; ADR-C-01..03 EM ANÁLISE; CG-01..12/FCG/MG NÃO ACEITOS, D03-21 C APROVADA documentalmente; Fase IV NÃO AUTORIZADA.

## D03-21 C — Inventário de lacunas de prontidão dos 12 CG, todos SEM ACEITE (2026-10-27)

A [Matriz GPR v0.1](PHASE-III-GATE-READINESS-v0.2.md) é o novo recorte de prontidão **DOCUMENTAL L0**: **GPR-01..12 ↔ CG-01..12** cada qual associado a fontes, pacotes E3, dependências ADR, prova ainda AUSENTE, dono FUNCIONAL PROPOSTO, decisão humana futura e STOP explícito. A D03-21 C ratifica APENAS O MÉTODO de mapear essas lacunas; nenhuma delas foi resolvida por nomear uma fonte.

**Quadro de dependências reais:** E3-01..04 **EM PLANEJAMENTO/STOP CONDITIONS NÃO ATENDIDAS**; ADR-C-01..03 **EM ANÁLISE**; CG-01..12 e FCG/MG **SEM ACEITE**; GPR-AC-01..08 propostos L0, evidências operacionais NOT_RUN, revisores e autoridades não nomeados. **Fonte escrita/CI/revisão autoral não é prova técnica nem revisão independente.** D03-22 C APROVADA documentalmente; **Fase IV NÃO AUTORIZADA**.

## D03-22 C — Prioridades de deliberação HUMANA com todos os CG abertos (2026-10-27)

[Matriz HDM v0.1](PHASE-III-HUMAN-DELIBERATION-v0.1.md) cruza **HDM-01..12 / CG-01..12** às lacunas GPR, fontes, risco V-RC/RA, dependências E3/ADR, owner FUNCIONAL PROPOSTO, competência humana futura e política de escalada L0. **Não** classificar "prioridade alta" como autorização de fazer, nem designar pessoa real por inferência; as questões D-HUM e critérios HDM-AC também são CANDIDATOS.

Para TODOS os CG, preservar `PROVA_AUSENTE / OWNER_NAO_DESIGNADO / REVISAO_PENDENTE / DECISAO_PENDENTE / STOP_ATIVO`. **CG-01..12/FCG/MG SEM ACEITE FINAL; E3-01..04 EM PLANEJAMENTO e STOP CONDITIONS NÃO ATENDIDAS; ADR-C-01..03 EM ANÁLISE; D03-23 A/B/C PENDENTE; Fase IV NÃO AUTORIZADA.**
