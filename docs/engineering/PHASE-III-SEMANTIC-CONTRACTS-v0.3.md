# NexLabs Technology — Contratos Semânticos Integrados da Primeira Vertical v0.3

**Work Order:** NX-P3-D03-17 · **Escolha do fundador:** D03-17 C, ratificada em **2026-10-27**.
**Natureza:** MÉTODO DE ESPECIFICAÇÃO DOCUMENTAL L0 APROVADO. Os campos, interfaces semânticas, invariantes, condições de aceitação, owners e fluxos abaixo são **PROPOSTOS**, não contratos técnicos ratificados nem sistema executável.
**Autoridade:** [Carta Institucional v1.0](../institutional/CHARTER-v1.0.md), [Registro D03 v0.17](PHASE-III-DECISION-REGISTER-v0.19.md), [Fatia Vertical v0.1](PHASE-III-RISK-FIRST-VERTICAL-v0.1.md), [Núcleo KAC/SAC v0.2](PHASE-III-ACCEPTANCE-CORE-v0.2.md).
**STOP:** Fase III somente documental; nenhum código, esquema físico, endpoint, API, autenticação, credencial, stack, provedor, conta, bot, serviço, dado real, teste operacional, deploy ou Fase IV foi autorizado.

## 1. Recorte integrado e fronteiras

A primeira vertical é **AUT → MIS → EVD/CST → FCR de leitura legítima**, preservando D03-02/11/12/13/14/15/16 C. O significado de autoridade, missão, evidência, custo e apresentação precisa ser compatível em todas as fronteiras sem pressupor banco, protocolo, padrão de mensagens, microsserviços ou SDK. FCR é futuro consumidor de projeções autorizadas, não fonte de verdade nem executor de comandos; Telegram, voz e relatórios são extensões condicionais com gates próprios.

**APROVADO como DIREÇÃO pela D03-17 C:** propor conjuntamente contratos mínimos entre os domínios, identificando principal e alçada, versão/tempo, estados e erros, evidência, finalidade/direitos, conflitos e indisponibilidade, responsabilidade por risco e semântica de confirmação. **NÃO APROVADO:** formato de dados/API, garantia distribuída, topologia, SLAs, algoritmos de consenso, tecnologias específicas, owners designados ou aceite dos contratos.

## 2. Envelope SEM-ENV, CAMPOS CANDIDATOS (não esquema nem protocolo)

| Conceito semântico | Regra transversal PROPOSTA | Risco crítico se ausente |
| --- | --- | --- |
| `correlation_context`, `intent_reference` | reconhecer intenção e rastrear etapas sem inferir autorização ou materializar identificadores concretos | confundir pedidos/efeitos ou duplicar ato |
| `principal_claim`, `identity_evidence_ref` | separar identidade alegada, verificação e origem da informação; não incluir credenciais | impersonação |
| `authority_ref`, `mandate_ref`, `scope_ref` | conferir alçada e mandato por fonte legítima, finalidade e atos delimitados | elevação de privilégios |
| `mandate_version`, `validity_context`, `revocation_context` | preservar vigência, versão, suspensão, expiração e efeito de revogação na decisão | decisão baseada em estado defasado |
| `semantic_state`, `prior_state`, `state_provenance` | distinguir solicitação, recebimento, autorização, aceitação para execução, relato, efeito e recusa | falsa conclusão |
| `observed_at`, `effective_at`, `source_freshness` | separar evento, eficácia e idade da informação; relógio não confiável sinaliza INCONCLUSIVO | corrida e ordem temporal falsa |
| `evidence_ref`, `assurance_level`, `review_context` | fonte, contestação, versão, limitação e L0..L4 sem autoatribuição de prova | autorrelato como evidência independente |
| `purpose`, `rights_context`, `sensitivity`, `retention_context` | minimizar conteúdo, finalidade, direito de leitura/retificação/retenção | exposição de terceiros |
| `cost_context`, `unit`, `measurement_status` | distinguir medido/estimado/indisponível; Jev exige baseline lícito e verificável | custo ausente vira zero |
| `decision_owner_role`, `review_route`, `gate_refs` | identificar dono funcional PROPOSTO e aprovação humana competente FUTURA | conflito sem escalada legítima |

**Observação:** nomes entre crases são apenas rótulos de discussão L0, não JSON, esquema de banco, contrato de API, campos obrigatórios de runtime ou decisões de formato. Nenhuma identidade, token ou custo concreto é armazenado neste pacote.

## 3. Fronteiras entre domínios, SEM-01..06 (candidatas)

| ID / fronteira | Pré-condição SEMÂNTICA | Saída lógica candidata, sem serviço real | Dono FUNCIONAL proposto | Falha segura / risco |
| --- | --- | --- | --- | --- |
| **SEM-01** Humano/FCR → AUT | finalidade conhecida, principal/alçada sujeita a prova, leitura ≠ poder de ação | pedido classificado como SOLICITADO, INCONCLUSIVO ou RECUSADO; sem mandato inferido | fundador + AUT + segurança | canal/sessão não concede competência; VSC-01/09 |
| **SEM-02** AUT → MIS | mandato legítimo, escopo/versão/vigência/direitos verificáveis e não revogados para ato específico | elegibilidade ou negação, referenciando proveniência e limite; não missão executada | AUT + MIS + risco/compliance | falha de fonte, revogação concorrente e ato reservado exigem STOP; VSC-02/03/07 |
| **SEM-03** MIS → EVD | distinguir pedido, ação aceita, relato e consequência; fonte identificada | relato ou artefato candidato classificado, contestável, sem efeito presumido | MIS + EVD + revisão independente | autodeclaração ≠ verificação; VSC-04/08 |
| **SEM-04** MIS → CST | observações de consumo com fonte legítima, unidade, período, versão e privacidade | MEDIDO, ESTIMADO ou INDISPONÍVEL, sem conversão tácita em economia Jev | MIS + CST + finanças | gasto falso, teto presumido, causalidade não demonstrada; VSC-02/06 |
| **SEM-05** EVD/CST → FCR | leitura legitimamente autorizada, evidência/custos/atualidade e direitos preservados | projeção INFORMATIVA com fonte, versão, grau de prova e lacunas | EVD/CST + FCR + privacidade | exportação/visão não é mandato, dado stale não é atual; VSC-05/09 |
| **SEM-06** AUT/MIS/EVD/CST ↔ FCR/Chief of Staff/canal futuro | somente quando individualmente autorizado, significado de status e proveniência sem alteração | proposta de explicação/consulta, sem ativar canal, sem elevação de privilégios | AUT + segurança + FCR + fundador | disputa entre canais e replay requer negação/escalada legítima; VSC-01/07/10 |

**SEM-06 não inclui outro canal no MVP nem ratifica ativação S1/S2/S3.** SEM-01..06 não constituem interfaces implementadas ou contratos C-03 formalmente aceitos.

## 4. Estados e transições conceituais, SEM-07

A sequência abaixo é *classificação de estados* e não máquina de estados executável nem promessa de processamento contínuo.

| Estado lógico CANDIDATO | Evidência mínima FUTURA para afirmá-lo | Transição inadmissível sem nova prova |
| --- | --- | --- |
| SOLICITADO | intenção com origem e propósito, não validade | SOLICITADO → EXECUTADO |
| RECEBIDO | recebimento de mensagem documentado | RECEBIDO → AUTORIZADO |
| IDENTIDADE_INCONCLUSIVA | autenticidade/alçada não verificáveis | → AUTORIZADO por sessão ou silêncio |
| AUTORIZACAO_VALIDADA | fonte legítima do mandato, tempo, versão, ato, direito e risco | → EFEITO_VERIFICADO |
| RECUSADO / EXPIRADO / REVOGADO / SUSPENSO | restrição e fonte competente consideradas | → nova aceitação baseada em versão inválida |
| ACEITO_PARA_EXECUCAO | elegibilidade/revalidação em momento necessário | → efeito afirmado sem fonte independente |
| EXECUCAO_RELATADA | declaração atribuível à origem | → EFEITO_VERIFICADO automaticamente |
| EFEITO_VERIFICADO | evidência apropriada ao impacto, revisão/contestação e escopo específico | → prova de efeitos colaterais ou reversão geral |
| INCONCLUSIVO / CONFLITANTE / INDISPONIVEL | falta, divergência ou atraso com proveniência | → autorização implícita ou sucesso |

**SEM-07 regra de não regressão:** atos reservados exigem confirmação humana explícita, nenhum status vira permissão pela interface ou canal; revogação de autorização futura não desfaz necessariamente efeito material anterior.

## 5. Temporalidade, idempotência conceitual e conflitos, SEM-08

- Distinguir tempo de evento, confirmação, validação, revogação eficaz, projeção e observação. Não decidir precedente por relógio local de canal.
- Reenvio, duplicidade, replay, mensagem fora de ordem ou versão divergente exigem consulta à fonte legítima e classificação **CONFLITANTE/INCONCLUSIVA**, inclusive nas ações em trânsito.
- Uma referência de intenção serve apenas ao raciocínio sobre deduplicação; o mecanismo de idempotência, ordenação/consenso, transações, armazenamento e latência permanece em ADR-C-02/C-03 **EM ANÁLISE**, não escolhido.
- Fonte de autoridade indisponível ou versão inconclusiva **não autoriza novo ato relevante**. Uma leitura de cache futuramente permitida requer direitos legítimos e indicação de desatualização; não sustenta comando.
- Retomada após reconexão não é autorização renovada. Avaliar efeitos já possivelmente ocorridos e consequências externas de forma separada, preservando dados mínimos necessários.

## 6. Direitos, retenção e proteção de dados, SEM-09

A futura transmissão de conceitos não concede direito de acesso por si só. Cada fronteira deverá avaliar finalidade legítima, minimização, sensibilidade, direitos de terceiros, restrição de exportação, retificação/eliminação e retenção proporcional ao direito aplicável. A auditoria conceitual preserva proveniência sem impor retenção ilimitada. Sem dados reais, PII, custos financeiros privados, segredos, credenciais, logs pessoais ou tokens no repositório público.

## 7. Política de falhas e retorno SEM-10 (não operacional)

| Condição negativa | Estado documental seguro CANDIDATO | Dono funcional e gate independente |
| --- | --- | --- |
| identidade/alçada não verificável ou mandato revogado | RECUSADO/INCONCLUSIVO para novos atos relevantes | AUT + humano competente; CG-01/07 |
| autorização concorrente com efeito em trânsito | suspender novas elegibilidades; consequências externas sob revisão | AUT/MIS/EVD; CG-04/07/11 |
| fonte EVD indisponível ou prova contestada | RELATADO/NÃO_VERIFICADO/CONFLITANTE | EVD + assurance; CG-03/09/10 |
| fonte CST indisponível, baseline Jev ausente | INDISPONÍVEL/ESTIMADO sem declarar economia | CST + finanças; CG-08/09 |
| projeção FCR atrasada ou sem permissão de leitura | DESATUALIZADO ou acesso negado; nenhuma ação | FCR/AUT/privacidade; CG-02/07/10 |
| divergência de canal, duplicidade e replay | não elevar privilégios; revisão pela fonte/autoridade legítima | AUT + contratos/segurança; CG-04/06/07 |

A designação "dono" é **função futura proposta**, não pessoa nomeada ou mandato real.

## 8. Rastreabilidade, evidência e DoR/DoD, SEM-11

| Pacote | Evidência documental L0 gerada por este arquivo | PENDÊNCIA de aceite e gate |
| --- | --- | --- |
| E3-01 | SEM-01..07, vertical V-01..05, KAC/SAC, VSC-01..10 alinhados | domínio, atores, direitos e critérios AC/MC/FCR-AC ainda não aceitos; CG-01/02/03 |
| E3-02 | restrições de fonte, versão, falha e fronteiras para comparação de ADRs | ADR-C-01/02/03 sem ratificação, alternativas não escolhidas; CG-04/05/06 |
| E3-03 | separação de atores institucionais e agentes construtores | RG/EL, execução e independência por risco ainda propostas; CG-07/08/09 |
| E3-04 | cenário negativo, fonte futura, owner proposto e efeito esperado para assurance | nenhum teste L2+, revisão operacional nem aceite CG-01..12; CG-09/10/11/12 |

**DoR CANDIDATO:** sujeito, escopo, classe de risco, fonte legítima, propósito, versão, estado, direito, responsável e gate definidos/aceitos com rastreabilidade. **DoD CANDIDATO:** contratos semânticos revistos quanto a exceções e direitos, equivalência especializada examinada, prova e donos materiais ratificados, opções ADR-C comparadas e gates aceitos independentemente. **Não alcançado** por este documento.

## 9. Critérios SEM-AC-01..10 (somente propostos), SEM-12

| ID | Verificação FUTURA (sem testes nesta fase) |
| --- | --- |
| SEM-AC-01 | sessão, identidade alegada, principal verificado e competência não se confundem |
| SEM-AC-02 | revogação, expiração e reserva humana barram nova elegibilidade indevida |
| SEM-AC-03 | estado RECEBIDO não vira AUTORIZADO; relato não vira efeito comprovado |
| SEM-AC-04 | duplicidade/replay/versões conflitantes produzem classificação segura sem ato duplicado |
| SEM-AC-05 | fonte, tempo e validade indisponíveis geram INCONCLUSIVO e não autorização tácita |
| SEM-AC-06 | evidência de efeito e revisão humana independentes de autorrelato, conforme risco |
| SEM-AC-07 | custo com unidade, fonte e status MEDIDO/ESTIMADO/INDISPONÍVEL e Jev sem baseline fabricado |
| SEM-AC-08 | privacidade, finalidade, retificação/retenção e direitos sobreviverão a cada fronteira |
| SEM-AC-09 | FCR/canal preserva semântica e sinaliza estado stale sem gerar privilégio |
| SEM-AC-10 | cada CG e STOP de E3 exige própria fonte, responsável, aceite, sem herança por documento |

Os dez SEM-AC são especializações candidatas a racionalizar depois com KAC, SAC, AC/MC/FCR-AC/CH-AC/IC-AC e **não gates novos aceitos**. "12" identifica o bloco de critérios deste documento, **não significa SEM-AC-11/12**.

## 10. Dependências e STOP CONDITION

**Aprovado:** D03-17 C como estratégia DOCUMENTAL para especificar contratos semânticos mínimos integrados. **Ainda PROPOSTOS:** SEM-ENV, SEM-01..12, SEM-AC-01..10, owners funcionais, evidências, cenários, transições, DoR/DoD, modelo de dados e tratamento de inconsistências. **PENDENTE:** ratificação material de ADR-C-01..03, escopo de canais, identidade operacional, escolha de stack/banco, custos/limites reais e critérios finais.

**STOP CONDITION vigente:** E3-01..04 EM PLANEJAMENTO e respectivas STOP CONDITIONS NÃO ATENDIDAS; CG-01..12 SEM ACEITE FINAL; ADR-C-01..03 EM ANÁLISE; KAC/SAC e todos SEM-AC propostos L0; **Fase IV NÃO AUTORIZADA**. A proposta D03-18 C foi ratificada posteriormente apenas como MÉTODO DOCUMENTAL; artefatos CFX não aceitos.

## 11. D03-18 C — Cenários CFX sobre os contratos semânticos (2026-10-27)

A D03-18 C ratifica SOMENTE a integração DOCUMENTAL dos conflitos e recuperação entre AUT/MIS/EVD/CST/FCR. Os significados SEM-ENV, SEM-01..12 e SEM-AC-01..10 continuam **PROPOSTOS L0**, sem API, entrega confiável, transação, idempotência ou rollback implementado.

| Fronteira SEM CANDIDATA | Classes de falha CFX PROPOSTAS | Invariante e evidência FUTURA |
| --- | --- | --- |
| SEM-01/02 AUT→MIS | CFX-01/02/03/04/14 | legitimidade, vigência, alçada humana, não repetir/revalidar por estado stale; fonte AUT |
| SEM-03 MIS→EVD | CFX-05/06/07/08 | relato ≠ efeito, consequência em trânsito e revisão independente; fontes de efeito |
| SEM-04 MIS→CST | CFX-09/10 | medido ≠ estimado ≠ indisponível, limite/consumo exigem fonte e humano competente |
| SEM-05 EVD/CST→FCR | CFX-08/11/12/13 | projeção datada, direitos e sem comando; fonte EVD/CST e acesso legítimo |
| SEM-06..10 todos | CFX-04/14/15/16 | replay/versões, retenção/correção e prevenção de gate falso com fonte, owner e critério próprio |

**Semântica de timeout/efeito:** evento em trânsito pode ter causado consequência externa mesmo sem retorno. Não afirmar inexistência do efeito nem reiterar execução automaticamente. **CFX não prova recuperação e SEM não vira ADR-C-03 ratificado**. D03-19 C APROVADA documentalmente; CG/E3/ADRs SEM ACEITE; Fase IV NÃO AUTORIZADA.

## 12. D03-19 C — Provas negativas SEM/CFX/KAC na mesma vertical

[Catálogo NPV v0.1](PHASE-III-NEGATIVE-PROOF-CATALOG-v0.1.md) é um **crosswalk documental CANDIDATO**: vincula os contratos SEM-01..12 e SEM-AC-01..10 a CFX-01..16, KAC/SAC e gates distintos, para que uma negativa futura seja julgada com fonte e efeito em trânsito adequados. **D03-19 C APROVOU MÉTODO L0**, não protocolos, schemas físicos, endpoint, API ou aceitação de contratos ADR-C-03.

Casos críticos: SEM-01/02 não confere alçada por canal; SEM-03 relato não é prova; SEM-04 não transforma custo desconhecido em zero; SEM-05/06 não transformam exibição em execução; SEM-07/08 falha de tempo, replay e revogação não significa rollback. Evidência de um domínio não promove gate de outro.

**SEM-AC/NPV-AC CANDIDATOS NÃO TESTADOS, owners FUNCIONAIS PROPOSTOS, ADR-C-01..03 EM ANÁLISE, CG sem aceite, E3 EM PLANEJAMENTO, D03-20 PENDENTE, Fase IV NÃO AUTORIZADA.**
