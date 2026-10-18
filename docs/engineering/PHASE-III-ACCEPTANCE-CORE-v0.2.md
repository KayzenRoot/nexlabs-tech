# NexLabs Technology — Núcleo de Critérios de Aceitação e Especializações v0.2

**Work Order:** NX-P3-D03-15. **Decisão do fundador:** D03-15 C ratificada em 2026-10-17, exclusivamente como método DOCUMENTAL L0.
**Autoridade:** [Carta Institucional](../institutional/CHARTER-v1.0.md) e [Registro D03 v0.15](PHASE-III-DECISION-REGISTER-v0.16.md), com D03-10/11/12/13/14 preservadas.
**Estado:** núcleo candidato, matriz de rastreio e donos RESPONSÁVEIS PROPOSTOS; não é DoD aceito, teste, gate aprovado, fluxo operacional, autorização de Fase IV ou substituição automática dos critérios históricos. Repositório público: nenhum dado pessoal, secreto ou credencial.

## 1. Regra ratificada e modo de migração documental

**Aprovado:** consolidar invariantes repetidos em um **núcleo comum** e manter critérios específicos apenas quando trazem uma propriedade, risco, fonte de evidência ou alçada próprios de determinado domínio/canal. Não apagar, relaxar ou reclassificar como aprovado nenhum AC, MC, FCR-AC, CH-AC, IC-AC, RG, EL, CG, FCG, MG ou IM histórico. Todos os IDs originais continuam referências válidas de origem; este documento é uma **matriz de correspondência e proposta de normalização**, não uma mudança automática de seus estados.

- **Núcleo comum KAC:** propriedade transversal e exigência de prova, sem obrigar tecnologia.
- **Especialização SAC:** diferença relevante de contexto/risco/ator com dono proposto e evidência particular.
- **Referência legada:** fonte, identificador original, justificativa de equivalência ou distinção e status histórico preservados.
- **Gate CG/FCG/MG:** decisão de aceitação separada; um item KAC ou SAC não fecha gate nem pacote E3.
- **Evidência:** fase atual L0 DOCUMENTAL; L1..L4 são categorias futuras sob plano/autorizações específicos, jamais medições ou testes existentes.
- **Risco:** identidade, missão e canal institucionais não herdam automaticamente R0–R3, escala específica dos agentes construtores. Qualquer corte ou exceção precisará de proprietário legítimo e autorização independente.

## 2. Núcleo KAC-01..12 (CRITÉRIOS CANDIDATOS, sem aceite)

| ID | Invariante transversal | Dono funcional FUTURO proposto | Fonte de prova FUTURA / risco protegido | Gates relacionados, NÃO ACEITOS |
| --- | --- | --- | --- | --- |
| KAC-01 | autoridade, principal, legitimidade, escopo e finalidade provados separadamente de canal/sessão | Autoridade humana + função AUT | origem/versionamento do mandato e identidade; elevação indevida | CG-01/07 |
| KAC-02 | atos reservados exigem consentimento explícito, competente, sem autoaprovação ou silêncio | Autoridade humana legítima + compliance | decisão identificável e alçada; ato indevido | CG-01/07/12 |
| KAC-03 | mandato limitado no tempo e revisado/revogado sem autorização retroativa; efeitos em trânsito distinguidos | AUT + risco/compliance | vigência, versão, suspensão, revogação e consequências; replay | CG-01/04/07/11 |
| KAC-04 | identidade declarada ≠ verificada ≠ sessão ≠ delegação; diferenças entre canais não elevam privilégios | AUT + privacidade/segurança | fonte de identidade e autorização; impersonação/acesso indevido | CG-01/04/06/07 |
| KAC-05 | pedido ≠ recebido ≠ autorizado ≠ aceito para execução ≠ relatado ≠ efeito verificado | MIS + EVD | estados versionados e prova independente de resultado; falsa conclusão | CG-02/03/06/09 |
| KAC-06 | evidência com proveniência, versão, limites, contestação/correção; L0 não apresentado como L3/L4 | EVD + revisão independente | origem, revisão, status e verificação; log/autoavaliação indevida | CG-03/04/09 |
| KAC-07 | acesso/retificação/retenção/eliminação compatíveis com direitos, dados mínimos e terceiros | Privacidade/compliance + AUD | base legítima, finalidade, acesso e retenção; exposição | CG-04/07 |
| KAC-08 | custo medido/estimado/desconhecido e Jev distinguíveis, com unidade/fonte/baseline legítimo | CST + finanças + auditoria | fonte datada e comparação válida; custo fictício/limite violado | CG-03/08/09 |
| KAC-09 | divergência, atraso, replay, duplicação, falha de fonte/tempo e recuperação geram estado seguro | AUT + contratos + segurança | conflitos/versionamento e comportamento negativo; ato sem elegibilidade | CG-04/06/07/09/11 |
| KAC-10 | toda representação (FCR/Telegram/voz/relatório) conserva autoridade e direitos e declara defasagem | FCR + AUT + privacidade | fonte legitimada, versão e classificação; canal autônomo | CG-02/06/07/10 |
| KAC-11 | modularidade, extração e correção preservam contratos, direitos, causalidade e recuperação proporcional | Arquitetura C-03 + EVD | plano/versões/rollback futuro e prova independente; migração insegura | CG-05/06/11 |
| KAC-12 | DoR/DoD, risco, responsáveis, evidências, segregação e STOP precisam de aceite próprio; nenhuma decisão sobre desenho equivale a execução | Função de assurance + fundador | fonte de aceite e check real conforme fase; aprovação fictícia | CG-03/07/09/10/12 |

**Dono funcional ≠ pessoa nomeada ou equipe contratada.** Nenhum papel confere poderes operacionais; a designação material dos responsáveis ainda é pendente.

## 3. Especializações SAC: manter apenas o que difere do núcleo

| ID | Domínio e obrigação especializada FUTURA | Prova distinta necessária | Dono funcional proposto | Risco e vínculo |
| --- | --- | --- | --- | --- |
| SAC-AUT-01 | emissão/renovação, delegação e reserva humana de mandatos | fonte de autoridade, vigência e limites específicos | AUT + fundador | KAC-01/02/03, MC/IM |
| SAC-MIS-01 | transição de missão e ações em curso, distinguindo proposta/efeito | evidência por missão e consequência externa | MIS + AUT | KAC-03/05, AC/MC |
| SAC-EVD-01 | revisão/contestação, correções e nível de verificabilidade de cada evidência | trilha de versões/classificação e auditoria independente | EVD + assurance | KAC-05/06, AC/FCR-AC |
| SAC-CST-01 | preços, tokens, fontes, orçamento e causalidade das economias Jev | unidades, período, gasto e baseline real, quando disponível | CST + finanças | KAC-08, AC/FCR-AC |
| SAC-FCR-01 | primeira experiência futura de supervisão de leitura, com estados de incerteza visíveis e controle de acesso | proveniência mostrada, não comando funcional | FCR + privacidade | KAC-05/06/07/10, FCR-AC |
| SAC-CH-01 | ativação condicional individual de Telegram/voz/exports sem poder adicional | identificação, privacidade, riscos e aprovação por canal | AUT + segurança + fundador | KAC-04/09/10, CH-AC |
| SAC-IC-01 | sessão/identidade/confirmações/replay e conflito entre meios | contrato semântico e cenários negativos conforme risco | AUT + contratos + segurança | KAC-03/04/05/09, IC-AC |
| SAC-BLD-01 | fábrica de construtores: papéis, execução paralela e risco próprio | DoR/DoD de engenharia, segregação e custo líquido | engenharia + assurance | KAC-11/12, RG/EL |

Não existe implementação real, API, provider, algoritmo de identidade, orçamento ou plataforma escolhida. A primeira vertical segue AUT/MIS/EVD/CST/FCR com o **FCR de leitura/supervisão como futuro recorte inicial**. As especializações são classificações DOCUMENTAIS, não backlog autorizado de software.

## 4. Matriz de rastreabilidade por identificador histórico

Os identificadores abaixo são **índices de origem, não critérios novamente aprovados**. Um vínculo KAC/SAC significa correspondência semântica candidata; direitos e deveres específicos da fonte prevalecem até ratificação do catálogo final.

| Origem histórica | IDs preservados integralmente | Correspondências propostas (sem apagar textos de origem) |
| --- | --- | --- |
| [E3-01 v0.14](E3-01-CAPABILITY-MAP-v0.14.md) | AC-01, AC-02, AC-07, AC-09, AC-14 | KAC-01/02/03; SAC-AUT-01 |
| E3-01 | AC-03, AC-04, AC-10, AC-15, AC-19 | KAC-05/06/09; SAC-EVD-01 |
| E3-01 | AC-05, AC-06, AC-11, AC-16 | KAC-08; SAC-CST-01 |
| E3-01 | AC-08, AC-12, AC-17, AC-18 | KAC-07/09/10; SAC-FCR-01 |
| E3-01 | AC-13, AC-20 | KAC-11; SAC-BLD-01 |
| [Mandatos v0.3](PHASE-III-INSTITUTIONAL-MANDATES-v0.3.md) | MC-01, MC-02, MC-03, MC-04, MC-05, MC-06, MC-07 | KAC-01/02/03/09; SAC-AUT-01/SAC-MIS-01 |
| Mandatos | MC-08, MC-09, MC-10, MC-11, MC-12, MC-13, MC-14 | KAC-02/05/06/07/08/09/10; SAC-CST-01/SAC-EVD-01 |
| [FCR v0.4](PHASE-III-FOUNDER-COMMAND-CENTER-v0.4.md) | FCR-AC-01, FCR-AC-02, FCR-AC-03, FCR-AC-04, FCR-AC-05 | KAC-01/03/05/06; SAC-FCR-01/SAC-EVD-01 |
| FCR | FCR-AC-06, FCR-AC-07, FCR-AC-08, FCR-AC-09, FCR-AC-10, FCR-AC-11, FCR-AC-12 | KAC-02/03/07/08/09/10; SAC-CST-01/SAC-FCR-01 |
| [Canais v0.2](PHASE-III-CHANNEL-GOVERNANCE-v0.2.md) | CH-AC-01, CH-AC-02, CH-AC-03, CH-AC-04, CH-AC-05, CH-AC-06 | KAC-01/03/04/05/09/10; SAC-CH-01/SAC-IC-01 |
| Canais | CH-AC-07, CH-AC-08, CH-AC-09, CH-AC-10, CH-AC-11, CH-AC-12 | KAC-02/06/07/08/09/10; SAC-CH-01 |
| [Identidade v0.1](PHASE-III-IDENTITY-CONSISTENCY-v0.1.md) | IC-AC-01, IC-AC-02, IC-AC-03, IC-AC-04, IC-AC-05, IC-AC-06 | KAC-01/03/04/05/06; SAC-IC-01 |
| Identidade | IC-AC-07, IC-AC-08, IC-AC-09, IC-AC-10, IC-AC-11, IC-AC-12 | KAC-02/07/09/10/12; SAC-IC-01/SAC-CH-01 |
| E3-01, agentes construtores | RG-01, RG-02, RG-03, RG-04, RG-05, RG-06, RG-07, RG-08, RG-09 | KAC-01/02/06/07/08/09/11/12; SAC-BLD-01, **sem transferir alçada institucional** |
| E3-01, paralelismo | EL-01, EL-02, EL-03, EL-04, EL-05, EL-06, EL-07, EL-08, EL-09, EL-10 | KAC-01/05/06/07/08/09/10/11/12; SAC-BLD-01 |
| E3-01, mandatos | IM-01, IM-02, IM-03, IM-04, IM-05, IM-06, IM-07, IM-08, IM-09, IM-10 | KAC-01/02/03/04/05/06/07/08/09/10; SAC-AUT/MIS/EVD/CST/FCR/CH |

**Catálogos E3 técnicos, FCG-01..10, MG-01..10 e CG-01..12 continuam referências/GATES próprios, a confrontar na revisão de aceite.** Não duplicar a prova; não eliminar obrigações, inclusive legislação/direitos aplicáveis. Cobertura documental proposta: AC 20/20; MC 14/14; FCR-AC 12/12; CH-AC 12/12; IC-AC 12/12; RG 9/9; EL 10/10; IM 10/10. Cobertura de equivalência **não demonstrada**; não confundir enumeração completa com aceite ou prova de não regressão.

## 5. Regras de não regressão e particularidades de aceitação

1. Uma unificação é legítima apenas se preservar **toda obrigação de segurança, privacidade, autoridade, custo, proveniência e reservas humanas** dos itens fonte; uma diferença material exige SAC próprio.
2. KAC e SAC são propostas L0. Quando houver execução autorizada, cada evidência terá **ID do critério, ID do gate, responsável, risco, fonte de prova, estado, versão, instante e decisão de aceite humana competente**, além de ausência/incerteza explícitas.
3. Evidência compartilhada poderá satisfazer *aspectos* de múltiplos critérios, mas **não herda automaticamente resultados** entre domínios, fases, plataformas ou escalas de risco.
4. Gate CG, STOP de E3, ADR e autorização Fase IV permanecem **decisões distintas**: aceite de requisito ≠ aceite de gate ≠ autorização de implementação ≠ funcionamento.
5. A revisão deve provar integridade de referências, cobertura de obrigações e ausência de perdas; se houver lacuna, **KEEP OPEN** e restaurar especialização antes de qualquer corte documental.
6. Custos/TCO e baseline Jev nunca são inventados. Evidência L0 é documentação, não CI, protótipo, experimento, operação ou resultado técnico.
7. Rótulos de responsáveis aqui são **donos funcionais futuros propostos**, não pessoas nomeadas, entes jurídicos constituídos nem mandatos reais.

## 6. Gates de convergência e riscos ainda ABERTOS

| Gate | Efeito candidato desta política | Lacuna remanescente |
| --- | --- | --- |
| CG-01/02/03 | KAC + SAC tornam responsabilidades e invariantes mais rastreáveis | autoridade, escopo MVP, donos humanos legítimos e DoR/DoD finais |
| CG-04/05/06 | fonte, contratos e dados aparecem em núcleo + especialização | ADR-C-01..03 não ratificados e políticas materiais pendentes |
| CG-07/08 | segurança, privacidade e TCO não se perdem com deduplicação | revisão legal, orçamento, limites, riscos e custos não aceitos |
| CG-09/10/11 | evidência, integração e reversibilidade rastreadas | nenhum teste autorizado/medido e sem prova de resultado |
| CG-12 | distinção expressa entre política L0 e implementação | Fase IV requer nova autorização explícita |

**Riscos documentais:** falsa equivalência, critérios de alto risco absorvidos por genéricos, direitos de terceiros omitidos, prova circulando entre gates, custos desconhecidos apresentados como ganhos, identidade de canal confundida com mandato. Tratar com matriz de rastreio, dono proposto, revisão humana competente e STOP.

## 7. Definition of Ready / Done e STOP CONDITION

**DoR CANDIDATO para um futuro catálogo aceito:** catálogo de origens versionado; equivalência por risco revisada; diferença SAC justificada; donos materiais e critérios específicos atribuídos; fontes/evidências disponíveis e classificação legal/privacidade definida; CG/ADR apropriados revisados.

**DoD CANDIDATO para o DOCUMENTO:** princípios ratificados, cobertura dos IDs históricos, matriz núcleo/especialização, relação com gates, riscos/semântica e handoff; revisão documental e aprovação humana do conteúdo pelo processo futuro. Produzir a proposta e o merge documental **não equivale a cumprir DoD de E3 nem a ratificar o conteúdo completo do catálogo**.

**STOP CONDITION VIGENTE:** E3-01..04 EM PLANEJAMENTO e STOP CONDITIONS NÃO ATENDIDAS; ADR-C-01..03 EM ANÁLISE; CG-01..12 SEM ACEITE FINAL; FCR-AC/MC/CH-AC/IC-AC, KAC/SAC e demais critérios técnicos como propostas; **Fase IV NÃO AUTORIZADA**. Próxima **D03-16 C APROVADA documentalmente** para ordem de tratamento das lacunas de aceitação documental, ainda não escolhida.

## 8. D03-16 C — Ancoragem por risco da fatia AUT/MIS/EVD/CST/FCR

**APROVADO SOMENTE O MÉTODO DOCUMENTAL L0** de analisar uma fatia vertical completa começando por riscos críticos, sem transformar KAC/SAC em critérios aceitos. A [Fatia Vertical v0.1](PHASE-III-RISK-FIRST-VERTICAL-v0.1.md) relaciona V-01..05 com VSC-01..10, riscos V-RC/V-RA/V-RM/V-RB CANDIDATOS, alçada, direitos, dono FUNCIONAL PROPOSTO, fonte de evidência futura e gate independente.

| Família de critério CANDIDATA | Etapa principal, sem quebrar dependências entre etapas | Cenários de atenção |
| --- | --- | --- |
| KAC-01/02/03/04, SAC-AUT/IC | V-01 AUT | VSC-01/02/03/07, poderes ilegítimos e revogação |
| KAC-03/05/09, SAC-MIS | V-02 MIS | VSC-03/04/07, ação em trânsito e falso efeito |
| KAC-05/06/07, SAC-EVD | V-03 EVD | VSC-04/08/10, proveniência e correção |
| KAC-02/07/08, SAC-CST | V-04 CST | VSC-02/06, teto/medição/causalidade de Jev |
| KAC-05/06/07/10/12, SAC-FCR/CH | V-05 FCR | VSC-05/09, consulta, privacidade e proibição de comando |

**Integridade histórica:** os 99 identificadores AC/MC/FCR-AC/CH-AC/IC-AC/RG/EL/IM continuam preservados nos arquivos de origem. Um cenário ou KAC compartilhado não aprova especialização, gate CG, evidência L2+, teste operacional ou transição de fase. **D03-17 PENDENTE; E3 EM PLANEJAMENTO; CG sem aceite; ADRs em análise; Fase IV NÃO AUTORIZADA.**
