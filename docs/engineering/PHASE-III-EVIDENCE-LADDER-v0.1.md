# NexLabs Technology — Plano de Evidências em Camadas v0.1

**Decisão autorizadora:** D03-07 C, 2026-10-15. **Estado:** PLANO DOCUMENTAL, NÃO EXECUTADO.
**Hierarquia:** [Carta Institucional v1.0](../institutional/CHARTER-v1.0.md), [Fase II encerrada](../design/PHASE-II-ACCEPTANCE-v1.0.md), [Registro D03 v0.7](PHASE-III-DECISION-REGISTER-v0.7.md), [E3-01 v0.7](E3-01-CAPABILITY-MAP-v0.7.md), [Pacote de ADRs v0.2](PHASE-III-CONVERGENT-ADR-PACK-v0.2.md).
**Regra:** não criar dados sintéticos, testes, scripts, bases, protótipos, credenciais, integrações, agentes, ambientes ou software. Definir apenas como tais evidências poderão ser classificadas após futura autorização.

## 1. Modelo de cinco níveis, com distinções obrigatórias

| Nível | Classificação | O que pode sustentar no futuro | O que NÃO sustenta | Situação atual |
| --- | --- | --- | --- | --- |
| **L0** | PLANEJADO | requisito e método especificados como intenção documental | existência de dado, teste passado ou recurso funcionando | **apenas nível documentado** |
| **L1** | SINTÉTICO ROTULADO | avaliação futura com cenários/dados artificiais explicitamente identificados | autenticidade externa, custo verdadeiro, efeito operacional | não criado |
| **L2** | TESTADO CONTROLADO | comportamento do sistema futuro em ambiente específico, com versão, método e resultados reais de teste | que as fontes externas estejam conectadas ou que o produto esteja em produção | não testado |
| **L3** | FONTE REAL AUTORIZADA | consulta legítima e validação limitada da fonte externa e proveniência, mediante acesso real verificado | que missões tenham efeitos reais ou que toda informação da fonte seja correta | não conectado |
| **L4** | RESULTADO OPERACIONAL VERIFICADO | efeito realmente observado por evidência adequada à afirmação, autoridade e escopo | garantia global de segurança, alta disponibilidade ou benefícios futuros | não observado |

**Confiança é multidimensional.** Uma fonte ser real não prova que está correta; teste executado não prova operação; log não prova necessariamente evento externo; resultado de uma missão não prova sucesso do sistema inteiro. Avanço de nível requer nova evidência e autorização pertinente. Não há transição automática ou obrigatoriedade de passar por todos os níveis quando a avaliação não é aplicável.

## 2. Campos semânticos do futuro registro de evidência (não esquema técnico)

- Identificador e afirmação específica que se pretende sustentar;
- domínio (AUT, MIS, EVD, CST, FCR) e caso de aceite correspondente;
- nível L0–L4, **com texto explicitando o significado do nível**;
- fonte e titularidade, autorização e finalidade legítima;
- origem temporal, versão e contexto da afirmação;
- método de coleta/verificação e limitações conhecidas;
- dado real, sintético, estimado, relatado, inferido ou indisponível, sem mistura;
- incerteza, contestação, revisão e data da validação quando houver;
- privacidade, retenção e destinatários legitimados;
- decisão de aceite ou rejeição tomada por autoridade apropriada.

Esses campos são **requisitos de documentação futura**, não payloads, classes, tabelas, eventos, APIs, modelos ou armazenamento existente.

## 3. Matriz de cobertura da primeira vertical (planejamento, não execução)

| Casos do histórico | Intenção de demonstração futura | Primeiro nível que poderia dar evidência útil | Condição de passagem legítima |
| --- | --- | --- | --- |
| AC-01,02,07,09,14 | autoridade, negatória e revogação | L1 ou L2 em cenário autorizado | antes de L3/L4 provar mandatos e origem autênticos |
| AC-03,04,10,15,19 | alegação vs prova, revisão e contestação | L1/L2 | validar fonte e veracidade independentemente |
| AC-05,06,11,16 | consumo, custo, preço e baseline Jev | L1 para regras; L2 se sistema existir | apenas L3 com fonte real de custo; economia exigirá baseline comparável |
| AC-08,12,17,18 | privacidade, acesso e estado desatualizado | L1 para casos negativos; L2 para mecanismos | L3 exige autorização, classificação de dados, minimização e sigilo |
| AC-13,20 | extração, compatibilidade e consistência | L0 como plano; L2 em teste futuramente autorizado | equivalência de direitos, migração e resultado efetivamente verificados |

**AC-01..20 permanecem casos de aceitação documentais propostos, não execução ou aceite funcional.** A matriz não gera exemplos sintéticos ou dados pessoais.

## 4. Critérios futuros para ingresso e revisão de um nível

### L0 → L1, se aprovado futuramente
Finalidade e casos aceitos, rotulagem de fictício inequívoca, proteção contra confusão com dados reais e critérios de exclusão de informação de terceiros; requer autorização da fase de execução.

### L1 → L2, se aplicável
Sistema e testes realmente existentes em ambiente autorizado, configuração/versionamento, evidência de execução, falhas, resultados e revisão. Sem inventar passes.

### L2 → L3, se aplicável
Legalidade de uso, permissões e autorizações, autenticação, dados classificados, termos do serviço/fonte, segregação e verificação de identidade e proveniência; medição da qualidade da fonte.

### L3 → L4, se aplicável
Ação realmente autorizada e executada, consequência observável, prova externa adequada, ausência de falhas materiais não tratadas e transparência sobre a cobertura. **Sem L4 derivado apenas de resposta de modelo, bot ou log.**

## 5. Casos negativos que devem ser planejados

Revogação concorrente; permissão negada; documento sem origem; evidência adulterada ou contraditória; replay ou registro duplicado; fonte indisponível; custo desconhecido; preço sem data; economia Jev sem baseline; missão marcada concluída por relato; exposição de segredo; perda de integridade na migração; agente declarando sozinho seu próprio sucesso.

Cada caso deverá preservar **ausência como ausência, dúvida como dúvida e falha como falha**, sem buscar sucesso sintético enganoso.

## 6. Impacto na comparação dos ADRs

- **C-01 Stack:** avaliar como cada alternativa permitiria futura instrumentação e validação reproduzíveis **após autorização**, sob requisitos idênticos;
- **C-02 Persistência:** preservar proveniência e histórico legítimo de níveis/afirmações, com retenção proporcional; logs não viram prova por definição;
- **C-03 Contratos:** definir limites semânticos entre alegação, mandato, fonte, custo e leitura do fundador; um módulo não pode autopromover evidência;
- **E3-03 Agentes:** agente gerador de conteúdo não é automaticamente revisor imparcial nem fonte do resultado; papéis e custos serão avaliados posteriormente;
- **E3-04 Segurança:** futura promoção depende dos gates de autoridade, sigilo, privacidade, custo e aceitação independente.

## 7. Fontes institucionais e requisitos do fundador preservados

Founder Command Center, Telegram/Chief of Staff, vozes, tokens/custos, Jev, finanças, VPS e relatórios PDF/planilhas são **aspirações registradas**, não fontes conectadas ou recursos já comprovados. Nenhuma indicação L3/L4 é permitida para essas capacidades enquanto não houver observação real apropriada. A Carta v1.0 governa atos humanos reservados.

## 8. STOP CONDITION

**Cumprido somente o objetivo de definir a estratégia documental D03-07 C. Não concluídos:** validação dos casos AC pelo fundador, escolha de stacks/bancos/contratos e agente(s), acesso seguro a fontes, testes e execução. Todos os quatro E3 continuam **EM PLANEJAMENTO**. Fase IV NÃO AUTORIZADA. [Próxima D03-08](PHASE-III-DECISION-REGISTER-v0.7.md) permanece PENDENTE.
