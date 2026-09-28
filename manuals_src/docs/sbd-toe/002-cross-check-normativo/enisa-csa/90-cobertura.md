---
id: cobertura
title: "Cobertura — Regulamento Cibersegurança (CSA)"
description: "O que o Manual cobre, as lacunas declaradas e o que fica fora de âmbito, a partir da matriz de cobertura do Regulamento Cibersegurança (CSA)."
sidebar_position: 90
tags: [cross-check, enisa-csa, cobertura]
sbdtoe_generated: reg-requirements-view
generated_by: scripts/gen_reg_views.py  # não se edita à mão: editar os catálogos, o overlay e a matriz
derived_from:
  - 002-cross-check-normativo/_matriz/csa.yaml
---

# Cobertura: Regulamento Cibersegurança (CSA)

Este regime não tem contexto no overlay regulatório (não eleva nem acrescenta requisitos); responde só nas três categorias.

## O que este Manual cobre e o que fica de fora {#cobertura}

Todas as obrigações do regime, na matriz de cobertura do Manual, em três categorias: o que o Manual **cobre**, e de que forma; as **lacunas declaradas** (o que não cobre por omissão); e o que fica **fora de âmbito**, com a razão. Nenhuma obrigação fica em silêncio. As 19 obrigações dirigidas às autoridades não criam dever para a organização e não entram nas listas.

### Cobre (35) {#cobre}

Força «cobre» ou «apoia evidência». A forma é a resposta do Manual: requisito do catálogo, política, secção, piso ou requisito acrescentado pelo regime.

| Obrigação | Referência | Força | Forma |
|---|---|---|---|
| CSA-51-a | Art. 51.º, alínea a) | Cobre | `ENC-001`; `ENC-002`; `ACC-001`; `ACC-006` |
| CSA-51-b | Art. 51.º, alínea b) | Cobre | `ENC-009`; `LOG-003`; `DPL-005`; [Política 27 §3.3](/sbd-toe/assets/policies/policy-rollback#33-rollback-de-base-de-dados); `OPS-016` |
| CSA-51-c | Art. 51.º, alínea c) | Cobre | `ACC-001`; `ACC-002`; `ACC-003` |
| CSA-51-d | Art. 51.º, alínea d) | Cobre | `DEP-001`; `DEP-010`; [Política 10 §8](/sbd-toe/assets/policies/policy-dependencias#8-alertas-de-vulnerabilidades-em-produção) |
| CSA-51-e | Art. 51.º, alínea e) | Cobre | `LOG-001`; `LOG-002`; `OPS-002` |
| CSA-51-f | Art. 51.º, alínea f) | Cobre | `LOG-003`; [Política 29 §8](/sbd-toe/assets/policies/policy-logging-estruturado#8-integridade-e-imutabilidade) |
| CSA-51-g | Art. 51.º, alínea g) | Cobre | `DEP-002`; `DPL-003`; `TST-005`; [Política 20 §5.1](/sbd-toe/assets/policies/policy-release-seguro#51-critérios-de-bloqueio-automático-no-go) |
| CSA-51-h | Art. 51.º, alínea h) | Cobre | `DPL-005`; [Política 32 §4.5](/sbd-toe/assets/policies/policy-irp#45-recuperação); `OPS-015`; `OPS-016`; `OPS-017` |
| CSA-51-i | Art. 51.º, alínea i) | Cobre | [Política 09 §3](/sbd-toe/assets/policies/policy-arquitetura-segura#3-princípios-de-arquitetura-segura); [Política 09 §3](/sbd-toe/assets/policies/policy-arquitetura-segura#3-princípios-de-arquitetura-segura); `CFG-001`; `THR-001` |
| CSA-51A-a | Art. 51.º-A, alínea a) | Apoia evidência | `TRN-001`; `GOV-001` |
| CSA-51A-b | Art. 51.º-A, alínea b) | Apoia evidência | `GOV-001`; `GOV-010` |
| CSA-51A-c | Art. 51.º-A, alínea c) | Cobre | `ENC-001`; `ENC-002`; `ACC-006` |
| CSA-51A-d | Art. 51.º-A, alínea d) | Cobre | `DPL-005`; [Política 32 §4.5](/sbd-toe/assets/policies/policy-irp#45-recuperação); `OPS-016`; `OPS-017` |
| CSA-51A-e | Art. 51.º-A, alínea e) | Cobre | `ACC-001`; `ACC-002` |
| CSA-51A-f | Art. 51.º-A, alínea f) | Cobre | `LOG-001`; `LOG-002`; `LOG-003` |
| CSA-52-1 | Art. 52.º, n.º 1 | Apoia evidência | `CLA-001`; `CLA-003` |
| CSA-52-6 | Art. 52.º, n.º 6 | Apoia evidência | `DEP-002`; [Política 20 §5.1](/sbd-toe/assets/policies/policy-release-seguro#51-critérios-de-bloqueio-automático-no-go); `TST-002`; `TST-005`; [Política 19 §5](/sbd-toe/assets/policies/policy-estrategia-testes#5-rastreabilidade-e-evidência-por-release) |
| CSA-52-7 | Art. 52.º, n.º 7 | Apoia evidência | `TST-008` |
| CSA-53-3 | Art. 53.º, n.º 3 | Apoia evidência | [Política 06 §10](/sbd-toe/assets/policies/policy-rastreabilidade#10-prazos-de-retenção-mínimos); [Política 20 §7](/sbd-toe/assets/policies/policy-release-seguro#7-rastreabilidade-ponta-a-ponta) |
| CSA-55-1-c | Art. 55.º, n.º 1, alínea c) | Cobre | `GOV-015` |
| CSA-56-7 | Art. 56.º, n.º 7 | Apoia evidência | [Política 19 §5](/sbd-toe/assets/policies/policy-estrategia-testes#5-rastreabilidade-e-evidência-por-release); [Política 20 §7](/sbd-toe/assets/policies/policy-release-seguro#7-rastreabilidade-ponta-a-ponta); `ARC-010` |
| CSA-56-8 | Art. 56.º, n.º 8 | Cobre | [Política 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória) |
| CSA-EUCC-7-1 | Art. 7.º, n.º 1 | Apoia evidência | `TST-001`; `TST-008`; `CIC-005`; `ARC-004` |
| CSA-EUCC-8-2 | Art. 8.º, n.º 2 | Apoia evidência | `ARC-010`; `ARC-004`; [Política 20 §7](/sbd-toe/assets/policies/policy-release-seguro#7-rastreabilidade-ponta-a-ponta); `CIC-005` |
| CSA-EUCC-8-5 | Art. 8.º, n.º 5 | Apoia evidência | `DEP-001` |
| CSA-EUCC-8-6-b | Art. 8.º, n.º 6, alínea b) | Cobre | [Política 12 §5.1](/sbd-toe/assets/policies/policy-excecoes-cve#51-etapas-obrigatórias); [Política 19 §4.2](/sbd-toe/assets/policies/policy-estrategia-testes#42-triagem-formal); `DEP-010`; `GOV-015` |
| CSA-EUCC-9-2-e | Art. 9.º, n.º 2, alínea e) | Cobre | [Política 20 §6](/sbd-toe/assets/policies/policy-release-seguro#6-imutabilidade-do-artefacto); `DPL-002`; `CIC-007` |
| CSA-EUCC-27-1-a | Art. 27.º, n.º 1, alínea a) | Cobre | [Política 10 §8](/sbd-toe/assets/policies/policy-dependencias#8-alertas-de-vulnerabilidades-em-produção); [Cap. 05 US-11](/sbd-toe/sbd-manual/dependencias-sbom-sca/aplicacao-lifecycle#us-11---alertas-sobre-vulnerabilidades-em-componentes-usados); `DEP-002`; [KEV — exploração confirmada](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/epss-kev-priorizacao#kev--exploração-confirmada); `GOV-015` |
| CSA-EUCC-27-1-b | Art. 27.º, n.º 1, alínea b) | Apoia evidência | [Política 08 §4.2](/sbd-toe/assets/policies/policy-threat-modeling#42-cadência-periódica); `GOV-010`; [Política 04 §1](/sbd-toe/assets/policies/policy-revisao-periodica-risco#1-objetivo) |
| CSA-EUCC-33-2 | Art. 33.º, n.º 2 | Cobre | `GOV-015` |
| CSA-EUCC-33-5 | Art. 33.º, n.º 5 | Apoia evidência | `DEP-010`; [Política 12 §5.1](/sbd-toe/assets/policies/policy-excecoes-cve#51-etapas-obrigatórias) |
| CSA-EUCC-35-7 | Art. 35.º, n.º 7 | Cobre | [Política 12 §6.2](/sbd-toe/assets/policies/policy-excecoes-cve#62-reavaliação); [Política 12 §6](/sbd-toe/assets/policies/policy-excecoes-cve#6-prazos-máximos-e-reavaliação) |
| CSA-EUCC-36 | Art. 36.º | Apoia evidência | `TST-003`; `DEP-010`; `TST-006` |
| CSA-EUCC-AnxIV-2-1 | Anexo IV, ponto IV.2, n.º 1 | Apoia evidência | [Política 08 §4.2](/sbd-toe/assets/policies/policy-threat-modeling#42-cadência-periódica); `CLA-004` |
| CSA-EUCC-AnxIV-3-1 | Anexo IV, ponto IV.3, n.º 1 | Apoia evidência | `ARC-009`; [Cap. 11 US-09](/sbd-toe/sbd-manual/deploy-seguro/aplicacao-lifecycle#us-09---versionamento-semântico-e-changelog-técnico) |

### Lacuna declarada (23) {#lacuna}

Força «parcial» ou «lacuna»: o Manual não cobre, ou cobre só em parte, e diz o que falta. As lacunas pendentes de uma ronda do AppSec Core estão marcadas com o nome da ronda.

| Obrigação | Referência | Força | Como o Manual responde | O que falta |
|---|---|---|---|---|
| CSA-51-j | Art. 51.º, alínea j) | Parcial | `DEP-002`; [Política 20 §5.1](/sbd-toe/assets/policies/policy-release-seguro#51-critérios-de-bloqueio-automático-no-go); `DST-003`; `DPL-002` | Sem vulnerabilidades conhecidas à saída e integridade dos artefactos; o mecanismo de atualização segura no produto entregue ao utilizador só está prescrito para produtos CRA (CTX-CRA-R02); não há contexto CSA. |
| CSA-51A-g | Art. 51.º-A, alínea g) | Parcial | `DEP-002`; [Política 09 §3](/sbd-toe/assets/policies/policy-arquitetura-segura#3-princípios-de-arquitetura-segura) | Aplica-se aos produtos próprios; não exige que as ferramentas de TIC de terceiros usadas na prestação do serviço sejam avaliadas como seguras desde a conceção e sem vulnerabilidades conhecidas. |
| CSA-55-1-a | Art. 55.º, n.º 1, alínea a) | Lacuna | — | Sem guia de configuração, instalação, implantação, funcionamento e manutenção seguros para utilizadores finais (lacuna idêntica à do CRA, anexo II, ponto 8, al. a)). |
| CSA-55-1-b | Art. 55.º, n.º 1, alínea b) | Lacuna | — | Sem definição nem publicação do período de apoio de segurança (o Manual só usa «período de apoio» como referência de retenção CRA). |
| CSA-55-1-d | Art. 55.º, n.º 1, alínea d) | Lacuna | [Cap. 11 US-09](/sbd-toe/sbd-manual/deploy-seguro/aplicacao-lifecycle#us-09---versionamento-semântico-e-changelog-técnico) | Sem referência pública a repositórios de vulnerabilidades do produto nem avisos de segurança; existe apenas a secção de segurança do changelog técnico (L2/L3). |
| CSA-55-2 | Art. 55.º, n.º 2 | Lacuna | — | Sem informação complementar publicada, logo sem regra de formato eletrónico e atualização até à caducidade. |
| CSA-EUCC-8-6-a | Art. 8.º, n.º 6, alínea a) | Lacuna | — | Depende das informações complementares do art. 55.º, que o Manual não prevê (CSA-55-1-a…d). |
| CSA-EUCC-8-7 | Art. 8.º, n.º 7 | Parcial | [Política 06 §10](/sbd-toe/assets/policies/policy-rastreabilidade#10-prazos-de-retenção-mínimos); [Política 06 §10](/sbd-toe/assets/policies/policy-rastreabilidade#10-prazos-de-retenção-mínimos) | Prazos de retenção do Manual (máx. 3 anos em L3) inferiores a 5 anos após a caducidade; a cláusula de precedência faz prevalecer o prazo EUCC, mas o mapa de retenção não o identifica. |
| CSA-EUCC-33-1 | Art. 33.º, n.º 1 | Parcial | [Política 12 §5.1](/sbd-toe/assets/policies/policy-excecoes-cve#51-etapas-obrigatórias); [Política 19 §4.2](/sbd-toe/assets/policies/policy-estrategia-testes#42-triagem-formal); `TST-003`; `DEP-010`; `GOV-015` | Processo interno e receção de relatos externos prescritos (TST-003, GOV-015); sem alinhamento explícito à EN ISO/IEC 30111. |
| CSA-EUCC-33-3 | Art. 33.º, n.º 3 | Parcial | [Política 12 §6](/sbd-toe/assets/policies/policy-excecoes-cve#6-prazos-máximos-e-reavaliação); [Política 19 §4.2](/sbd-toe/assets/policies/policy-estrategia-testes#42-triagem-formal); `DEP-010` | Registo e triagem de vulnerabilidades detetadas (testes, SCA) prescritos; as comunicadas por terceiros não têm entrada. |
| CSA-EUCC-33-4 | Art. 33.º, n.º 4 | Parcial | `DST-007` | A notificação a dependentes está prevista só para versões comprometidas (DST-007); não para vulnerabilidades que afetam produtos compostos com certificado próprio. |
| CSA-EUCC-34-1 | Art. 34.º, n.º 1 | Parcial | [Política 12 §6](/sbd-toe/assets/policies/policy-excecoes-cve#6-prazos-máximos-e-reavaliação); [Política 19 §4.3](/sbd-toe/assets/policies/policy-estrategia-testes#43-slas-de-triagem-e-resolução); [Integração na priorização de remediação](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/epss-kev-priorizacao#integração-na-priorização-de-remediação) | Prazos de triagem e remediação segundo severidade/exploração (KEV, EPSS); a análise não é referida ao alvo de avaliação nem às declarações do certificado. |
| CSA-EUCC-34-2 | Art. 34.º, n.º 2 | Lacuna | — | Sem cálculo do potencial de ataque segundo CC/CEM (o Manual usa CVSS/EPSS/KEV). |
| CSA-EUCC-35-1 | Art. 35.º, n.º 1 | Parcial | [Política 12 §5.1](/sbd-toe/assets/policies/policy-excecoes-cve#51-etapas-obrigatórias); [Política 19 §4.2](/sbd-toe/assets/policies/policy-estrategia-testes#42-triagem-formal) | Existe justificação técnica documentada por CVE/finding; não há relatório de análise do impacto na conformidade com o certificado. |
| CSA-EUCC-35-2 | Art. 35.º, n.º 2 | Parcial | [Política 12 §5.1](/sbd-toe/assets/policies/policy-excecoes-cve#51-etapas-obrigatórias); [Política 12 §4](/sbd-toe/assets/policies/policy-excecoes-cve#4-tipos-de-exceção); [Integração na priorização de remediação](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/epss-kev-priorizacao#integração-na-priorização-de-remediação) | Impacto, exploitabilidade e mitigação são avaliados; faltam proximidade/exequibilidade do ataque em termos CC e a conclusão sobre corrigibilidade face ao certificado. |
| CSA-EUCC-35-3 | Art. 35.º, n.º 3 | Parcial | [Política 36 §4.2](/sbd-toe/assets/policies/policy-pentesting#42-regras-de-engajamento) | A confidencialidade é prescrita para relatórios de pentest (incluindo PoC); não para meios de exploração em relatórios de vulnerabilidade em geral nem com distribuição limitada. |
| CSA-EUCC-39 | Art. 39.º | Lacuna | [Cap. 11 US-09](/sbd-toe/sbd-manual/deploy-seguro/aplicacao-lifecycle#us-09---versionamento-semântico-e-changelog-técnico) | Sem divulgação pública de vulnerabilidades corrigidas nem inscrição na base de dados europeia de vulnerabilidades (art. 12.º NIS2). |
| CSA-EUCC-41-1 | Art. 41.º, n.º 1 | Lacuna | — | Depende das informações do art. 55.º, inexistentes (CSA-55-1-a…d). |
| CSA-EUCC-41-2 | Art. 41.º, n.º 2 | Parcial | [Política 20 §6](/sbd-toe/assets/policies/policy-release-seguro#6-imutabilidade-do-artefacto); [Política 06 §10](/sbd-toe/assets/policies/policy-rastreabilidade#10-prazos-de-retenção-mínimos) | Artefactos imutáveis e retidos, mas por 1–2 anos (artefactos de build/SBOM); não se prevê conservar um exemplar do produto certificado e os registos da certificação ≥ 5 anos após a retirada. |
| CSA-EUCC-AnxIV-3-2 | Anexo IV, ponto IV.3, n.º 2 | Parcial | `ARC-004`; `ARC-009`; [Cap. 11 US-09](/sbd-toe/sbd-manual/deploy-seguro/aplicacao-lifecycle#us-09---versionamento-semântico-e-changelog-técnico) | Alterações descritas (ADR, changelog) e revisão por alteração significativa; falta identificar alterações aos elementos de prova do criador e concluir sobre o impacto na garantia. |
| CSA-EUCC-AnxIV-4-4 | Anexo IV, ponto IV.4, n.º 4 | Parcial | `DEP-007`; [Política 20 §6](/sbd-toe/assets/policies/policy-release-seguro#6-imutabilidade-do-artefacto); `DPL-002`; `TST-006` | Desenvolvimento e lançamento de correções controlados e testes de regressão; falta o mecanismo técnico de adoção das atualizações no produto e a avaliação da sua eficácia. |
| CSA-EUCC-AnxIV-4-5 | Anexo IV, ponto IV.4, n.º 5 | Parcial | `DPL-002`; `DST-003` | Integridade e proveniência dos artefactos de atualização verificáveis; sem descrição do procedimento nem separação dos limites do TOE. |
| CSA-EUCC-AnxIV-4-6 | Anexo IV, ponto IV.4, n.º 6 | Lacuna | — | Sem rota de atualização corretiva consciente da certificação (classificação fora do TOE / alteração menor / vulnerabilidade crítica e submissão ao ITSEF em 5 dias úteis). |

### Fora de âmbito (22) {#fora-de-ambito}

Obrigações que o Manual declara fora de âmbito, com a razão.

| Obrigação | Referência | Razão |
|---|---|---|
| CSA-53-1 | Art. 53.º, n.º 1 | Disposição sobre a arquitetura do sistema de certificação (autoavaliação, níveis, retirada); não cria dever de engenharia. |
| CSA-53-2 | Art. 53.º, n.º 2 | Declaração UE de conformidade e assunção de responsabilidade: plano jurídico da conformidade. |
| CSA-EUCC-6 | Art. 6.º | Disposição sobre a arquitetura do sistema de certificação (autoavaliação, níveis, retirada); não cria dever de engenharia. |
| CSA-EUCC-8-1 | Art. 8.º, n.º 1 | Relação formal com o organismo de certificação/ITSEF/autoridade nacional (plano da certificação), fora do âmbito de um manual de engenharia; o cross-check ENISA/CSA remete-a para o dossiê de certificação. |
| CSA-EUCC-9-2-a | Art. 9.º, n.º 2, alínea a) | Relação formal com o organismo de certificação/ITSEF/autoridade nacional (plano da certificação), fora do âmbito de um manual de engenharia; o cross-check ENISA/CSA remete-a para o dossiê de certificação. |
| CSA-EUCC-9-2-b | Art. 9.º, n.º 2, alínea b) | Promoção, marca e rótulo do certificado: plano jurídico-comercial da certificação. |
| CSA-EUCC-9-2-c | Art. 9.º, n.º 2, alínea c) | Promoção, marca e rótulo do certificado: plano jurídico-comercial da certificação. |
| CSA-EUCC-9-2-d | Art. 9.º, n.º 2, alínea d) | Promoção, marca e rótulo do certificado: plano jurídico-comercial da certificação. |
| CSA-EUCC-9-2-f | Art. 9.º, n.º 2, alínea f) | Promoção, marca e rótulo do certificado: plano jurídico-comercial da certificação. |
| CSA-EUCC-11-1 | Art. 11.º, n.º 1 | Promoção, marca e rótulo do certificado: plano jurídico-comercial da certificação. |
| CSA-EUCC-11-2 | Art. 11.º, n.º 2 | Promoção, marca e rótulo do certificado: plano jurídico-comercial da certificação. |
| CSA-EUCC-11-3 | Art. 11.º, n.º 3 | Promoção, marca e rótulo do certificado: plano jurídico-comercial da certificação. |
| CSA-EUCC-11-4 | Art. 11.º, n.º 4 | Promoção, marca e rótulo do certificado: plano jurídico-comercial da certificação. |
| CSA-EUCC-16 | Art. 16.º | Certificação de perfis de proteção: atividade de quem desenvolve perfis, não do processo de engenharia do produto. |
| CSA-EUCC-27-2 | Art. 27.º, n.º 2 | Relação formal com o organismo de certificação/ITSEF/autoridade nacional (plano da certificação), fora do âmbito de um manual de engenharia; o cross-check ENISA/CSA remete-a para o dossiê de certificação. |
| CSA-EUCC-28-3 | Art. 28.º, n.º 3 | Relação formal com o organismo de certificação/ITSEF/autoridade nacional (plano da certificação), fora do âmbito de um manual de engenharia; o cross-check ENISA/CSA remete-a para o dossiê de certificação. |
| CSA-EUCC-29-1 | Art. 29.º, n.º 1 | Relação formal com o organismo de certificação/ITSEF/autoridade nacional (plano da certificação), fora do âmbito de um manual de engenharia; o cross-check ENISA/CSA remete-a para o dossiê de certificação. |
| CSA-EUCC-30-3 | Art. 30.º, n.º 3 | Comunicação da suspensão do certificado a adquirentes e ao público: plano jurídico-comercial da certificação. |
| CSA-EUCC-35-4 | Art. 35.º, n.º 4 | Relação formal com o organismo de certificação/ITSEF/autoridade nacional (plano da certificação), fora do âmbito de um manual de engenharia; o cross-check ENISA/CSA remete-a para o dossiê de certificação. |
| CSA-EUCC-35-6 | Art. 35.º, n.º 6 | Disposição sobre a arquitetura do sistema de certificação (autoavaliação, níveis, retirada); não cria dever de engenharia. |
| CSA-EUCC-41-3 | Art. 41.º, n.º 3 | Conservação conjunta de documentação de certificados: plano documental da certificação. |
| CSA-EUCC-41-4 | Art. 41.º, n.º 4 | Relação formal com o organismo de certificação/ITSEF/autoridade nacional (plano da certificação), fora do âmbito de um manual de engenharia; o cross-check ENISA/CSA remete-a para o dossiê de certificação. |
