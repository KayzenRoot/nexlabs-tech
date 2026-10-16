# NexLabs Technology — Matriz Integrada de Convergência e Prontidão v0.2

**Decisão:** D03-10 C — Fechamento integrado por gates verificáveis, ratificada em 2026-10-15.
**Estado:** **PLANO DOCUMENTAL EM ANDAMENTO**, **NÃO ACEITO COMO CONCLUSÃO DOS PACOTES**.
**Autoridade:** [Carta Institucional v1.0](../institutional/CHARTER-v1.0.md), [Fase II encerrada](../design/PHASE-II-ACCEPTANCE-v1.0.md), [Registro D03 v0.11](PHASE-III-DECISION-REGISTER-v0.11.md), [Carta Fase III v0.11](PHASE-III-CHARTER-v0.11.md).
**Dependências documentais:** [E3-01 v0.11](E3-01-CAPABILITY-MAP-v0.11.md), [E3-02 v0.11](E3-02-ARCHITECTURE-EVALUATION-v0.11.md), [E3-03 v0.11](E3-03-AGENT-FACTORY-EVALUATION-v0.11.md), [E3-04 v0.11](E3-04-READINESS-AND-GATES-v0.11.md), [ADRs convergentes v0.6](PHASE-III-CONVERGENT-ADR-PACK-v0.6.md), [Governança de agentes v0.4](PHASE-III-AGENT-GOVERNANCE-v0.4.md), [Evidências L0–L4](PHASE-III-EVIDENCE-LADDER-v0.1.md).

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

**Founder Command Center, Telegram bilateral com Chief of Staff, relatórios PDF/planilhas, vozes distintas de agentes, tokens/custos/Jev, finanças e observabilidade de VPS** seguem registrados como possibilidades e requisitos futuros, não integrações criadas ou fontes monitoradas. A **D03-11 C aprovou a prioridade funcional progressiva** do Founder Command Center em [Plano FCR v0.1](PHASE-III-FOUNDER-COMMAND-CENTER-v0.1.md), sem aprovar sistemas, APIs, telas ou operações.

**Confidencialidade:** o repositório foi observado público em auditorias anteriores. Antes de dados ou credenciais protegidos, avaliar política e visibilidade; não alterar visibilidade sem autorização adequada.

## 10. Próximas ações DOCUMENTAIS e STOP geral

1. D03-11 C aprovada como prioridade funcional da primeira capacidade do Founder Command Center; detalhar e ratificar fontes, FCR-AC, atores e recorte; D03-12 pendente para política de mandatos institucionais;
2. harmonizar e obter aceites de escopo, atores, AC/DoR/DoD, mandatos e política de dados;
3. levantar informação técnica verificável e custos de candidatos, mantendo ADR-C-01..03 separados para ratificação material;
4. amadurecer os critérios de governança, orçamento, limites e qualidade de agentes sem os criar;
5. revisar segurança, privacidade, riscos e confidencialidade;
6. apresentar propostas de decisão humana com lacunas explícitas e uma possível ata de encerramento **somente após** as condições objetivas satisfeitas.

**STOP CONDITION DESTA MATRIZ: DEFINIÇÃO DOCUMENTAL CONCLUÍDA; FECHAMENTO DOS E3 E FASE III NÃO AUTORIZADO NEM ATINGIDO. Fase IV NÃO AUTORIZADA.** Nenhuma alegação de funcionamento de sistema, teste, modelo, controle ou infraestrutura pode ser derivada desta matriz.

## 11. D03-11 C: atualização auditável dos gates da primeira capacidade FCR (NOVO v0.2)

[Plano Funcional Founder Command Center v0.1](PHASE-III-FOUNDER-COMMAND-CENTER-v0.1.md) registra recorte progressivo com autoridade explícita. Isso resolve a **escolha direcional D03-11**, mas **NÃO encerra o CG-02 ou qualquer outro gate**.

| Gate existente | Efeito efetivo da D03-11 C | Lacuna impeditiva | Estado |
| --- | --- | --- | --- |
| **CG-01** autoridade | decisão humana concebida como origem legítima e revogável | detalhes de atores/mandato e aceitação, D03-12 ainda pendente | **PENDENTE** |
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

**D03-12 PENDENTE** apenas para decisão documental da política de mandatos de missões institucionais. Os **12 gates permanecem não aceitos documentalmente**; uma direção aprovada não é software, dado ou teste. Nenhum requisito da Carta ou dos adendos foi alterado.
