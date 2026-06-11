---
id: matriz-verificacao-transversal
title: Matriz Transversal de Verificação
sidebar_position: 17
description: O índice único de toda a verificação de segurança do SbD-ToE — atividade × tipo × oráculo × capítulo × nível de risco — distinguindo teste (oráculo comportamental) de análise/scanning (oráculo de lookup/política).
tags: [verificacao, matriz, testes, sca, sast, dast, iac, oraculo, transversal, L1, L2, L3]
---

<!--template: sbdtoe-addon -->

# Matriz Transversal de Verificação

A verificação de segurança não vive num único capítulo. Distribui-se pelo ciclo de vida — valida-se um requisito em Cap. 02, revê-se um *threat model* em Cap. 03, corre-se SCA em Cap. 05, faz-se *scanning* de IaC em Cap. 08, executa-se DAST em Cap. 10, deteta-se anomalia em runtime em Cap. 12. Cada atividade pertence ao capítulo do seu domínio, onde está prescrita com o seu requisito, a sua aplicabilidade por nível de risco e a sua evidência. Esta página não duplica nenhuma dessas prescrições: é o **índice único** que as reúne, para que seja possível responder de uma só vez à pergunta de auditoria — *"está tudo verificado para este nível de risco?"*.

O que organiza a matriz é o **oráculo**: o referencial contra o qual se confronta o que se observa. Um **teste** tem oráculo *comportamental* — confronta comportamento observado com comportamento esperado (SAST, DAST, IAST, fuzzing, PenTesting). Uma **análise** ou *scanning* tem oráculo de *lookup* (confronta um inventário com uma base de CVE — é o SCA) ou de *política* (confronta uma configuração com uma regra ou *baseline* — secrets, IaC, imagens de container). A **validação funcional** tem oráculo de *critério de aceitação* (confronta o sistema com o requisito funcional de segurança). A **revisão** tem oráculo de *juízo perito* contra padrões (*threat modeling*, arquitetura). A **deteção em runtime** tem oráculo de *sinal* contra uma *baseline* operacional. A distinção não é académica: é o que justifica que o SCA viva no capítulo de dependências e não no de testes.

Cap. 10 (Testes de Segurança) cobre apenas a fatia de **oráculo comportamental** — os testes propriamente ditos. Todo o resto da verificação vive no seu capítulo de origem. Esta matriz é onde as duas metades se voltam a juntar, sem que nenhum controlo seja prescrito em dois sítios.

## A taxonomia de oráculos

| Tipo de verificação | Oráculo | Pergunta que responde | Exemplos |
|---|---|---|---|
| **Teste** | Comportamental — comportamento observado vs. esperado | "O sistema comporta-se de forma insegura quando confrontado?" | SAST, DAST, IAST, fuzzing, PenTesting |
| **Análise / scanning (lookup)** | Base de CVE — inventário vs. vulnerabilidades conhecidas | "Algum componente do inventário tem vulnerabilidade conhecida?" | SCA (*vulnerability verdict*) sobre SBOM, scanning de imagens |
| **Análise / scanning (policy)** | Regra ou *baseline* — configuração vs. política | "A configuração viola alguma regra prescrita?" | Secrets scanning, IaC scanning, *policy-as-code*, *admission control* |
| **Validação funcional** | Critério de aceitação — sistema vs. requisito funcional | "O requisito de segurança está efetivamente satisfeito?" | Validação de requisitos, testes de regressão de segurança |
| **Revisão / design review** | Juízo perito contra padrões | "A conceção introduz risco que o padrão evitaria?" | Revisão de *threat model*, revisão de arquitetura, code review |
| **Deteção em runtime** | Sinal vs. *baseline* operacional | "O comportamento em produção desvia-se do normal?" | Deteção comportamental, correlação SIEM, *detection engineering* |

> **O SCA tem duas faces.** A *composition analysis* — gerar o SBOM, inventariar dependências diretas e transitivas — **não tem oráculo**: é levantamento, não verificação. O *vulnerability verdict* — confrontar esse inventário com uma base de CVE — **tem oráculo de lookup**. É a segunda face que faz do SCA uma *análise* e não um *teste*: não há comportamento confrontado, há um inventário comparado com uma lista. Por isso o SCA vive em Cap. 05, ancorado em [`DEP-001`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias) (SBOM, inventário) e [`DEP-002`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias) (*verdict* e bloqueio por severidade), e não em Cap. 10.

## A matriz

Cada linha é uma atividade de verificação prescrita num capítulo. As colunas L1/L2/L3 indicam a aplicabilidade por nível de risco — `✔` obrigatório, `rec.` recomendado, `—` não exigido —, exatamente como consta no catálogo de origem. A coluna *Grounding* cita o requisito que prescreve a atividade. As linhas seguem a ordem do ciclo de vida.

| Atividade | Tipo | Oráculo | Capítulo | L1 | L2 | L3 | Grounding |
|---|---|---|---|---|---|---|---|
| Validação funcional de requisitos de segurança | Validação funcional | Critério de aceitação | [Cap. 02](/sbd-toe/sbd-manual/requisitos-seguranca/intro) | ✔ | ✔ | ✔ | `REQ-001`, `REQ-002` |
| Revisão formal de segurança dos requisitos | Revisão | Juízo perito | [Cap. 02](/sbd-toe/sbd-manual/requisitos-seguranca/intro) | ✔ | ✔ | ✔ | `REQ-002` |
| Rastreabilidade requisito → ameaça → teste | Validação funcional | Critério de aceitação | [Cap. 02](/sbd-toe/sbd-manual/requisitos-seguranca/intro) | — | ✔ | ✔ | `REQ-006` |
| Revisão de *threat model* formal (STRIDE/LINDDUN/PASTA) | Revisão | Juízo perito contra padrões | [Cap. 03](/sbd-toe/sbd-manual/threat-modeling/intro) | — | ✔ | ✔ | `THR-001`, `THR-003` |
| Revisão independente de *threat model* por AppSec antes de go-live | Revisão | Juízo perito | [Cap. 03](/sbd-toe/sbd-manual/threat-modeling/intro) | — | ✔ | ✔ | `THR-007` |
| Validação de evidência do *threat model* (DFDs, *trust boundaries*) | Revisão | Juízo perito contra padrões | [Cap. 03](/sbd-toe/sbd-manual/threat-modeling/intro) | — | ✔ | ✔ | `THR-002`, `THR-004` |
| Revisão de arquitetura com foco em segurança | Revisão | Juízo perito contra padrões | [Cap. 04](/sbd-toe/sbd-manual/arquitetura-segura/intro) | — | ✔ | ✔ | `ARC-003` |
| Validação de zonas de confiança e isolamento entre domínios | Revisão | Juízo perito | [Cap. 04](/sbd-toe/sbd-manual/arquitetura-segura/intro) | ✔ | ✔ | ✔ | `ARC-001`, `ARC-006` |
| Validação automática de topologia (*diagrams-as-code*, Cartography) | Análise (policy) | Regra / *baseline* | [Cap. 04](/sbd-toe/sbd-manual/arquitetura-segura/intro) | — | — | ✔ | `ARC-013` |
| Linters e *rulesets* de segurança *enforced* | Análise (policy) | Regra / *ruleset* | [Cap. 06](/sbd-toe/sbd-manual/desenvolvimento-seguro/intro) | ✔ | ✔ | ✔ | `DEV-002` |
| SAST como *gate* de integração | Teste | Comportamental (estático) | [Cap. 06](/sbd-toe/sbd-manual/desenvolvimento-seguro/intro) | ✔ | ✔ | ✔ | `DEV-003`, `TST-002` |
| Code review com checklist de segurança em componentes críticos | Revisão | Juízo perito contra padrões | [Cap. 06](/sbd-toe/sbd-manual/desenvolvimento-seguro/intro) | ✔ | ✔ | ✔ | `DEV-004` |
| Perfis de qualidade com *thresholds* mínimos por nível de risco | Análise (policy) | *Baseline* de qualidade | [Cap. 06](/sbd-toe/sbd-manual/desenvolvimento-seguro/intro) | — | ✔ | ✔ | `DEV-008` |
| Geração de SBOM por *build* (*composition analysis*) | Análise (sem oráculo) | Inventário | [Cap. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro) | ✔ | ✔ | ✔ | `DEP-001` |
| SCA — *vulnerability verdict* com bloqueio por severidade | Análise (lookup) | Base de CVE | [Cap. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro) | ✔ | ✔ | ✔ | `DEP-002` |
| Verificação de versões fixas e integridade de dependências | Análise (policy) | Regra (*lockfile*, *hash*) | [Cap. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro) | ✔ | ✔ | ✔ | `DEP-003`, `DEP-004` |
| Rastreabilidade SBOM → CVE → correção | Análise (lookup) | Base de CVE | [Cap. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro) | — | ✔ | ✔ | `DEP-010` |
| Inventário e proveniência de dependências AI/ML (AI BOM) | Análise (sem oráculo) | Inventário | [Cap. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro) | — | ✔ | ✔ | `DEP-011`, `DEP-012` |
| Versão *pinned* e *providers* AI aprovados (anti *rug-pull*) | Análise (policy) | Política (versão fixa / lista aprovada) | [Cap. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro) | — | ✔ | ✔ | `DEP-013`, `DEP-014` |
| Secrets scanning no código e no pipeline | Análise (policy) | Regra (padrões de segredo) | [Cap. 06](/sbd-toe/sbd-manual/desenvolvimento-seguro/intro) | ✔ | ✔ | ✔ | `IAC-011`, `CIC-003` |
| *Gates* de segurança bloqueantes antes de promoção (SAST, SCA, lint, secrets) | Análise (policy) | Política de pipeline | [Cap. 07](/sbd-toe/sbd-manual/cicd-seguro/intro) | ✔ | ✔ | ✔ | `CIC-004` |
| Verificação de integridade e proveniência de artefactos (assinatura, *hash*) | Análise (policy) | Política (assinatura / proveniência) | [Cap. 07](/sbd-toe/sbd-manual/cicd-seguro/intro) | — | ✔ | ✔ | `CIC-007` |
| Verificação de *triggers* e fontes autorizadas do pipeline | Análise (policy) | Regra de fonte autorizada | [Cap. 07](/sbd-toe/sbd-manual/cicd-seguro/intro) | ✔ | ✔ | ✔ | `CIC-002` |
| IaC scanning (tfsec, checkov) obrigatório em pipeline | Análise (policy) | Regra / *baseline* de configuração | [Cap. 08](/sbd-toe/sbd-manual/iac-infraestrutura/intro) | ✔ | ✔ | ✔ | `IAC-003` |
| *Policy-as-code* — *enforcement* automático de políticas (OPA/Rego, Sentinel) | Análise (policy) | Política codificada | [Cap. 08](/sbd-toe/sbd-manual/iac-infraestrutura/intro) | — | — | ✔ | `IAC-009` |
| Verificação de *plan* aprovado antes de *apply* | Análise (policy) | Regra de aprovação | [Cap. 08](/sbd-toe/sbd-manual/iac-infraestrutura/intro) | — | ✔ | ✔ | `IAC-007` |
| Deteção de *drift* entre IaC e estado real | Deteção em runtime | Sinal vs. estado declarado | [Cap. 08](/sbd-toe/sbd-manual/iac-infraestrutura/intro) | — | ✔ | ✔ | `IAC-012` |
| Scanning de vulnerabilidades em imagens de container | Análise (lookup) | Base de CVE | [Cap. 09](/sbd-toe/sbd-manual/containers-imagens/intro) | ✔ | ✔ | ✔ | `CNT-002` |
| SBOM por imagem publicada | Análise (sem oráculo) | Inventário | [Cap. 09](/sbd-toe/sbd-manual/containers-imagens/intro) | — | ✔ | ✔ | `CNT-008` |
| Verificação de assinatura e proveniência de imagens (Cosign/Notary) | Análise (policy) | Política de assinatura | [Cap. 09](/sbd-toe/sbd-manual/containers-imagens/intro) | — | ✔ | ✔ | `CNT-007` |
| *Admission control* — *policy-as-code* sobre containers (OPA/Gatekeeper, Kyverno) | Análise (policy) | Política codificada | [Cap. 09](/sbd-toe/sbd-manual/containers-imagens/intro) | — | ✔ | ✔ | `CNT-009` |
| Verificação de *hardening* de container (não-root, *readonly FS*, *capabilities*) | Análise (policy) | Regra / *baseline* de configuração | [Cap. 09](/sbd-toe/sbd-manual/containers-imagens/intro) | rec. | ✔ | ✔ | `CNT-004`, `CNT-005`, `CNT-006` |
| DAST em *staging* antes de promoção | Teste | Comportamental (dinâmico) | [Cap. 10](/sbd-toe/sbd-manual/testes-seguranca/intro) | — | ✔ | ✔ | `TST-005` |
| IAST instrumentado em *staging* | Teste | Comportamental (runtime instrumentado) | [Cap. 10](/sbd-toe/sbd-manual/testes-seguranca/intro) | — | — | ✔ | `TST-010` |
| Fuzzing de componentes de processamento de input complexo | Teste | Comportamental (input adversarial) | [Cap. 10](/sbd-toe/sbd-manual/testes-seguranca/intro) | — | — | ✔ | `TST-009` |
| PenTesting periódico com escopo e metodologia definidos | Teste | Comportamental (exploração real) | [Cap. 10](/sbd-toe/sbd-manual/testes-seguranca/intro) | — | ✔ | ✔ | `TST-008` |
| Testes de regressão de segurança para vulnerabilidades corrigidas | Validação funcional | Critério de aceitação | [Cap. 10](/sbd-toe/sbd-manual/testes-seguranca/intro) | — | ✔ | ✔ | `TST-006` |
| *Eval suite* como gate de release de sistemas agentic | Teste | Comportamental (*eval* offline) | [Cap. 11](/sbd-toe/sbd-manual/deploy-seguro/intro) | — | ✔ | ✔ | `DPL-010` |
| Deteção de eventos críticos de segurança em runtime | Deteção em runtime | Sinal (catálogo de eventos) | [Cap. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro) | ✔ | ✔ | ✔ | `OPS-002`, `OPS-005` |
| Correlação de eventos entre múltiplas fontes (SIEM) | Deteção em runtime | Sinal correlacionado | [Cap. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro) | — | — | ✔ | `OPS-008` |
| Deteção comportamental contra *baseline* de atividade normal (UEBA) | Deteção em runtime | Sinal vs. *baseline* | [Cap. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro) | — | — | ✔ | `OPS-009` |
| Observabilidade e audit de sistemas AI/agentic em runtime (*tool-call audit*, *token runaway*) | Deteção em runtime | Sinal vs. *baseline* / *mandate* | [Cap. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro) | — | ✔ | ✔ | `OPS-011`, `OPS-012`, `OPS-013` |
| Deteção de *jailbreak* e *off-policy actions* em agentes AI | Deteção em runtime | Sinal vs. *mandate* / padrão adversarial | [Cap. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro) | — | — | ✔ | `OPS-014` |
| Revisão periódica de acesso de terceiros (*least privilege*) | Análise (policy) | Política (*least privilege*) | [Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro) | ✔ | ✔ | ✔ | `GOV-014` |

## Leitura por oráculo

### Comportamental — os testes propriamente ditos

Confrontam comportamento observado com comportamento esperado. SAST (`DEV-003`/`TST-002`) sobre o código estático; DAST (`TST-005`) sobre a aplicação em execução; IAST (`TST-010`) instrumentado em runtime; fuzzing (`TST-009`) com input adversarial; PenTesting (`TST-008`) com exploração real. É a fatia que vive em Cap. 10 — e quase a única que aí vive: a *eval suite* como gate de release de sistemas agentic (`DPL-010`) é também oráculo comportamental, mas executa-se no *deploy* (Cap. 11), porque é aí que a mudança de modelo/*prompt* entra em produção.

### Lookup — confronto com base de CVE

Confrontam um inventário com vulnerabilidades conhecidas. O *vulnerability verdict* do SCA (`DEP-002`), a rastreabilidade SBOM → CVE → correção (`DEP-010`) e o scanning de imagens de container (`CNT-002`). Não há comportamento confrontado: há um inventário comparado com uma lista. É por isto que o SCA é **análise** e não teste — o oráculo é a base de CVE, não o comportamento do sistema.

### Política — confronto com regra ou *baseline*

Confrontam uma configuração com uma regra prescrita. Secrets scanning (`IAC-011`/`CIC-003`), IaC scanning (`IAC-003`), *policy-as-code* (`IAC-009`, `CNT-009`), verificação de assinatura e proveniência (`CIC-007`, `CNT-007`), *hardening* de container (`CNT-004`/`CNT-005`/`CNT-006`), *gates* de pipeline (`CIC-004`), linters (`DEV-002`) e a revisão periódica de acesso de terceiros (`GOV-014`), que confronta o acesso concedido com a regra de *least privilege*. O oráculo é a regra ou *baseline*, não o comportamento.

### Critério de aceitação — confronto com o requisito funcional

Confrontam o sistema com o requisito funcional de segurança. Validação de requisitos (`REQ-001`/`REQ-002`), rastreabilidade requisito → ameaça → teste (`REQ-006`) e testes de regressão de segurança (`TST-006`), que confirmam que a correção satisfaz o critério e previnem recorrência.

### Sinal / runtime — confronto com *baseline* operacional

Confrontam comportamento em produção com uma *baseline*. Deteção de eventos críticos (`OPS-002`/`OPS-005`), correlação SIEM (`OPS-008`), deteção comportamental (`OPS-009`) e deteção de *drift* de IaC (`IAC-012`). O oráculo é o sinal operacional contra o estado esperado. Em sistemas AI/agentic, este oráculo estende-se ao *mandate*: a observabilidade dedicada e o *audit* por *tool invocation* (`OPS-011`/`OPS-012`/`OPS-013`) confrontam a ação real com a intenção declarada, e a deteção de *jailbreak* e *off-policy actions* (`OPS-014`, obrigatória em L3) confronta o comportamento do agente com o *scope* assinado no seu *mandate* — a contraparte operacional do `intent declaration` exigido em requisitos.

### Juízo perito — revisão e design review

Confrontam a conceção com padrões, mediados por perícia humana. Revisão de *threat model* (`THR-001`/`THR-003`/`THR-007`), revisão de arquitetura (`ARC-001`/`ARC-003`/`ARC-006`) e code review com checklist (`DEV-004`). O oráculo é o juízo perito contra padrões estabelecidos.

## Como usar a matriz

**Para o auditor.** Lê-se de cima para baixo, fixando uma coluna de risco: para um sistema L2, todas as linhas com `✔` na coluna L2 têm de ter evidência; as marcadas `rec.` são recomendadas mas não bloqueantes; as `—` não se exigem. A resposta a *"está tudo verificado para este nível de risco?"* obtém-se sem percorrer dez capítulos.

**Para o capítulo de Testes.** O *item de fronteira* da checklist de revisão de Cap. 10 aponta para aqui: Cap. 10 verifica o oráculo comportamental, e remete a verificação restante para esta matriz, que a reúne sem a duplicar.

**Sobre duplicação.** Nenhum controlo é prescrito em dois sítios. Cada atividade tem um único requisito de origem, no seu capítulo. Esta matriz é índice, não fonte — altera-se o requisito no capítulo, e a matriz limita-se a referenciá-lo.

:::tip Proporcionalidade L1–L3
A matriz não exige tudo a todos. As colunas L1/L2/L3 são a expressão da proporcionalidade: L1 concentra-se na verificação de base de baixo custo e alto retorno (SBOM, SCA, SAST, linters, eventos críticos); L2 acrescenta a profundidade da revisão (*threat model*, arquitetura, DAST, PenTesting); L3 acrescenta a verificação de exceção (fuzzing, IAST, correlação, *policy-as-code* de exceção). Verificar é proporcional ao risco — esta matriz mostra, de uma só vez, onde está esse limiar para cada atividade.
:::
