# NexLabs Technology — Identidade e Consistência Intercanais v0.2

**Work Order:** NX-P3-D03-14 · **Decisão ratificada:** D03-14 C, 2026-10-17.
**Natureza:** DIRETRIZ DOCUMENTAL L0. Especificações de campos, critérios de aceite e mecanismos continuam PROPOSTOS; nenhuma identidade digital, sessão, credencial, fluxo ou controle real foi criado.
**Precedência:** [Carta Institucional v1.0](../institutional/CHARTER-v1.0.md) > decisões D03-11/12/13/14 > propostas de contratos e critérios. [Registro D03 v0.14](PHASE-III-DECISION-REGISTER-v0.15.md); [Mandatos v0.3](PHASE-III-INSTITUTIONAL-MANDATES-v0.4.md); [Canais v0.2](PHASE-III-CHANNEL-GOVERNANCE-v0.3.md).
**Escopo:** somente planejamento E3-01..04. Fase IV NÃO AUTORIZADA.

## 1. Política aprovada versus opções técnicas ainda abertas

**APROVADO por D03-14 C:** tratar conjuntamente (i) identidade, (ii) confirmação de solicitações/atos, (iii) validade e revogação de mandatos, e (iv) resolução de conflitos entre canais, sempre de forma proporcional ao risco. Isso **não** aprova autenticação, credenciais, registro operacional, fluxo executável, banco, API, SDK, protocolo, fila, provedor, algoritmos criptográficos, serviços ou orçamentos.

FCR será o primeiro **canal futuro de supervisão a planejar**. Telegram, voz, Chief of Staff e relatórios poderão usar a mesma autoridade sem obter novos poderes, mas sua ativação dependerá de autorização humana, provas e gates específicos. A aprovação da política integrada **não antecipa S1/S2/S3** de D03-13.

## 2. Identidade e autorização, camada conceitual

- **IC-I01 Principal e origem:** identificar o sujeito que solicita, sua categoria (humano legítimo, representante autorizado, agente institucional, serviço candidato), origem e contexto. Um nome, número de telefone, avatar, sessão ou controle da conta do canal não constituem identidade/autorização suficiente.
- **IC-I02 Alçada e mandato:** verificar emissor competente, escopo, versão, temporalidade, atos, limitações de dados, orçamento, finalidade, condições de delegação e risco. Identidade autenticada ≠ permissão institucional.
- **IC-I03 Prova independente:** separar evidência de identidade, fonte legítima de autoridade e evidência de resultado; apresentar origem, período, revisão e grau de verificação. Não inferir confiança de logs ou confirmações do próprio agente.
- **IC-I04 Sessão contextual:** sessões futuras poderão representar presença ou canal, mas expiração, encerramento, perda de controle, revogação ou troca de identidade exigirão reavaliação da elegibilidade, sem persistência tácita de autorização.
- **IC-I05 Reserva humana:** alterações constitucionais, despesas materiais, compromissos jurídicos, ampliação de poderes e demais atos reservados exigem pessoa legitimada e aprovação explícita. Silêncio e timeout não autorizam.

## 3. Semântica de confirmações e ciclo de vida

| Estado conceitual | O que pode significar | O que nunca comprova isoladamente |
| --- | --- | --- |
| SOLICITADO | intenção atribuída, ainda não autorizada | mandato, ordem válida, efeito |
| RECEBIDO | canal recebeu representação da solicitação | validação de identidade ou execução |
| IDENTIDADE EM ANÁLISE | prova de identidade não concluída | competência para autorizar |
| AUTORIZAÇÃO VALIDADA | fontes legítimas e versão vigentes verificadas para ato delimitado | início ou êxito da execução |
| RECUSADO / INCONCLUSIVO | violação, falta de fonte, conflito ou incerteza identificados | aceitação tácita ou resultado positivo |
| ACEITO PARA EXECUÇÃO | ação elegível segundo contrato futuro e verificações necessárias | execução efetiva |
| EXECUÇÃO RELATADA | terceiro/agente informa ter agido | comprovação independente |
| EFEITO VERIFICADO | evidência adequada ao impacto comprova resultado específico | sucesso de outras ações ou reversibilidade de efeitos |
| SUSPENSO / REVOGADO / EXPIRADO | autorização futura não utilizável conforme fonte competente | reversão retroativa de efeitos externos |

**IC-I06 Confirmação graduada:** futuras confirmações distinguirão recebimento, validação, autorização, aceitação de execução, efeito e comunicação ao fundador; estado desconhecido é DESCONHECIDO, não zero nem sucesso.
**IC-I07 Correlação e duplicidade:** planejar identidade conceitual por solicitação/intenção e tratamento de retransmissão, replay, edição, atraso, duplicidade e mensagens fora de ordem. Não selecionar UUID, protocolo ou persistência agora.
**IC-I08 Término da execução:** uma revogação impede novas elegibilidades; ações já em trânsito exigem análise de consequência, compensação lícita quando possível e registro proporcional, sem prometer interrupção real instantânea.

## 4. Ordem temporal, conflitos e recuperação

- **IC-I09 Fonte prevalente:** um canal apresenta projeções derivadas de fonte legítima; a projeção atrasada não modifica mandato, alçada ou evidência. Semântica comum é necessária, mas o modelo de consistência técnico permanece em análise nos ADRs.
- **IC-I10 Conflito de versões:** divergência sobre principal, mandato, limite, revogação, execução ou resultado gera condição **CONFLITANTE/INCONCLUSIVA**. Planejar investigação com proveniência, ordem temporal, fonte e decisão humana quando reservada; não resolver pelo canal mais recente ou por votação de agentes.
- **IC-I11 Tempo confiável:** datas/relógios inconsistentes, validade não verificável, expiração ou atraso não podem revalidar permissão. Nenhum serviço de relógio, mecanismo de ordenação ou consenso foi escolhido.
- **IC-I12 Falha segura:** canal indisponível, autenticação não verificável, evidência adulterada ou fonte fora do ar bloqueia **novos atos com risco relevante**; leituras não sensíveis em cache poderão ser estudadas quando legítimas, claramente marcadas como desatualizadas e sem autoridade para comandos.
- **IC-I13 Retomada:** após reconexão, reavaliar identidade, versão, mandato e efeitos antes de reapresentar ações pendentes. Reenvio não equivale a nova autorização. Tratar pendências irreversíveis separadamente.
- **IC-I14 Privacidade:** mínimo necessário, finalidade, direitos de acesso, contestação, retenção e exclusão legítima prevalecem sobre logs, relatórios exportados e memórias de longo prazo. Repositório público: nenhum dado pessoal, credencial ou identificador real neste documento.

## 5. Proporcionalidade por risco, sem converter R0–R3 da fábrica de construção

| Classe qualitativa PROPOSTA | Exemplo de categoria (NÃO caso real) | Verificação que uma fase futura deverá definir |
| --- | --- | --- |
| Baixo impacto e leitura autorizada | consulta informativa reversível | legitimidade de leitura, fonte e sinalização de defasagem |
| Impacto relevante ou dado protegido | emissão de instrução, alteração de missão, relatório privado | revalidação de identidade, direitos, mandato, confirmação e revisão proporcional |
| Reservado, financeiro material ou irreversível | aprovar gasto superior à alçada, comprometer terceiros ou elevar permissões | autorização humana competente e salvaguardas reforçadas; sem execução se faltar prova |

As classes são **candidatas**, sem mapeamento automático para R0–R3 (risco dos agentes construtores), nem thresholds financeiros, quantidade de etapas, fatores de autenticação, SLA, tempo de expiração, orçamentos ou regras jurídicas definitivas. Custos de autenticação/recuperação/revisão deverão ser avaliados por evidência, sem estimativas inventadas.

## 6. Critérios futuros de aceitação IC-AC-01..12, PROPOSTOS L0

| ID | Critério FUTURO sujeito a aceite específico |
| --- | --- |
| IC-AC-01 | distinguir identidade declarada, identidade verificada e alçada efetiva |
| IC-AC-02 | tratar mandatos, sessões e direitos com escopo/tempo/versão próprios |
| IC-AC-03 | impedir promoção automática de RECEBIDO a AUTORIZADO ou EXECUTADO |
| IC-AC-04 | separar aceite para execução, relato e efeito verificável por fonte |
| IC-AC-05 | rejeitar novos atos com mandato suspenso, revogado, expirado ou inconclusivo |
| IC-AC-06 | documentar efeitos em trânsito, revogação concorrente e impossibilidade de reversão |
| IC-AC-07 | tratar replay, duplicidade, atraso e mensagens fora de ordem conforme impacto |
| IC-AC-08 | resolver conflito sem elevar poderes e preservar justificativa/proveniência |
| IC-AC-09 | falhar com segurança quando fonte, identidade ou relógio não são verificáveis |
| IC-AC-10 | preservar direitos e minimização de informação em canais e relatórios |
| IC-AC-11 | exigir confirmação humana explícita para decisões legal/constitucionalmente reservadas |
| IC-AC-12 | exigir autorização por etapa/canal e provas L2+ futuras quando cabíveis, sem deduzir L3/L4 |

**IC-AC-01..12 não são novos gates aceitos, nem testes realizados.** Consolidar possíveis duplicatas de CH-AC, MC, FCR-AC e demais AC antes da ratificação de DoR/DoD: proposta de racionalização é a D03-15, ainda pendente.

## 7. Encaixe E3, ADR, riscos e STOP CONDITION

- **E3-01:** primeira vertical mantém apenas FCR de supervisão (leitura legitimada) e estados explícitos; nenhuma interação operacional passa a obrigatória.
- **E3-02 / ADR-C-01..03:** comparar escolhas de stack/persistência/contrato por capacidades de revalidação, rastreabilidade, consistência e custo, sem produto escolhido.
- **E3-03:** agentes construtores e institucionais permanecem regimes distintos; nenhum executor ganha acesso/autoridade por participar deste planejamento.
- **E3-04 / CG-01..12:** refletir cenários IC-AC em riscos, responsáveis, evidência e futura aceitação sem declarar gates atendidos.
- **Riscos abertos:** impersonação, acesso indevido, dados stale, inconsistência temporal, replay, dupla execução, falsa confirmação, revogação em trânsito, custos de verificações e exposição de dados.

**STOP CONDITION:** D03-14 C aprovada como DIRETRIZ DOCUMENTAL; E3-01..04 EM PLANEJAMENTO; ADR-C-01..03 EM ANÁLISE; CG-01..12 SEM ACEITE FINAL; IC-AC/CH-AC/MC/FCR-AC ainda PROPOSTOS; **FASE IV NÃO AUTORIZADA**. Nenhum sistema, agente, UI, autenticação, conta, Telegram, voz, API, teste, rede ou infraestrutura criado.

## 8. D03-15 C — Identidade e coerência em KAC/SAC (2026-10-17)

Método aprovado SOMENTE DOCUMENTAL: KAC-01..05/09/10 compartilham legitimidade, confirmação, revogação, estados seguros e limites do canal. SAC-IC-01 preserva requisitos específicos de sessões, mensagens duplicadas, relógios/temporalidade, reconexão e análise de efeitos em trânsito. [Mapa v0.1](PHASE-III-ACCEPTANCE-CORE-v0.1.md).

**IC-AC-01..12 continuam PROPOSTOS L0** e não podem ser removidos ou marcados como satisfeitos porque um KAC os indexou. Se a especialização exigir fonte, contexto, segurança ou responsável distinto, registrar prova própria. Sem autenticação, conta, agente, serviço, testes ou autorização de Fase IV. **D03-16 PENDENTE, E3/CG e ADRs sem aceite.**
