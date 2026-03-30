---
id: checklist-aderencia-sbd-toe
title: Checklist de Aderência ao Modelo SbD-ToE
sidebar_position: 85
description: Instrumento de avaliação de adopção do modelo SbD-ToE - 96 pontos de verificação organizados por domínio e nível de risco, derivados das políticas organizacionais. Responde à pergunta "esta equipa/organização está a fazer SbD-ToE?" e serve como ferramenta de auto-avaliação, auditoria interna e requisito contratual.
tags: [checklist, aderencia, auditoria, governacao, L1, L2, L3, conformidade]
---

<!--template: sbdtoe-addon -->

# Checklist de Aderência ao Modelo SbD-ToE

## Para que serve este documento

Este checklist responde a uma pergunta diferente dos KPIs e KRIs:

| Instrumento | Pergunta |
|-------------|----------|
| **Este checklist** | "Esta equipa/organização está a fazer SbD-ToE?" |
| KPIs de domínio | "Quão bem está a funcionar?" |
| KRIs executivos | "A que risco estamos expostos?" |

O checklist é um instrumento de **adopção** - avalia se os processos, controlos e artefactos existem e estão a ser seguidos. Não mede a qualidade dos resultados - para isso, ver [`kpis-governanca`](./kpis-governanca) e [`kpis-kri-executivo`](./kpis-kri-executivo).

**Usos principais:**
- Auto-avaliação de equipa antes de revisão de segurança
- Auditoria interna de conformidade com o modelo
- Requisito contratual para fornecedores e terceiros
- Onboarding de novas equipas ao programa SbD-ToE

---

## Como usar

**Aplicação:** O checklist é aplicado por aplicação (ou por portfolio para avaliação organizacional). Para cada item, regista-se:

| Resposta | Significado |
|----------|-------------|
| ✔ | Conforme - evidência disponível |
| ✗ | Não conforme |
| ~ | Parcialmente conforme - em curso ou com lacunas identificadas |
| N/A | Não aplicável ao contexto específico (requer justificação) |

**Níveis de risco:** Os itens estão marcados com o nível a partir do qual são obrigatórios:

| Marcação | Obrigatoriedade |
|----------|----------------|
| **S** | Sempre - independente do nível de risco da aplicação |
| **L1+** | Obrigatório a partir de L1 (risco baixo) |
| **L2+** | Obrigatório a partir de L2 (risco médio) |
| **L3** | Apenas para aplicações L3 (risco alto/crítico) |

Os níveis são cumulativos: L3 inclui todos os itens L2+, que incluem todos os itens L1+, que incluem todos os itens S.

**Cadência de avaliação recomendada:** L1 - anual; L2 - semestral; L3 - trimestral.

---

## 1 - Classificação e Gestão de Risco

*Políticas: classificacao-risco, aceitacao-risco, revisao-periodica-risco, gestao-excecoes*

| # | Item | Nível | Política |
|---|------|:-----:|---------|
| 1.01 | Cada aplicação tem nível de risco formal (L1/L2/L3) atribuído, usando os três eixos obrigatórios: Exposição, Dados, Impacto | **S** | pol-02 |
| 1.02 | A classificação é aprovada formalmente (mínimo Tech Lead) | **L1+** | pol-02 |
| 1.03 | A classificação é reavaliada quando ocorrem os triggers definidos: nova integração externa, novo tipo de dado, alteração de exposição, mudança de arquitectura, novo perfil de utilizador | **S** | pol-02, pol-04 |
| 1.04 | A classificação é reavaliada com periodicidade: L1 anual, L2 semestral, L3 trimestral | **L1+** | pol-04 |
| 1.05 | Para L3, a reavaliação periódica requer aprovação AppSec + CISO | **L3** | pol-02 |
| 1.06 | Excepções a controlos têm TTL máximo definido (L1: 90 dias; L2: 60 dias; L3: 30 dias), justificação técnica e mitigação compensatória documentada | **S** | pol-03, pol-05 |
| 1.07 | Excepções são reavaliadas antes da expiração - não existem excepções expiradas sem renovação ou encerramento formal | **S** | pol-05 |

---

## 2 - Requisitos, Ameaças e Arquitectura

*Políticas: requisitos-seguranca, threat-modeling, arquitetura-segura, rastreabilidade*

| # | Item | Nível | Política |
|---|------|:-----:|---------|
| 2.01 | Os requisitos de segurança aplicáveis ao nível da aplicação estão mapeados e documentados (subconjunto essencial em L1; catálogo completo em L2/L3) | **L1+** | pol-07 |
| 2.02 | Cada requisito tem critério de validação definido | **L2+** | pol-07 |
| 2.03 | A rastreabilidade é bidirecional: requisito ↔ controlo ↔ evidência | **L2+** | pol-06 |
| 2.04 | Os logs de pipeline e relatórios de SAST/SCA/DAST são retidos conforme os prazos mínimos (L2: 90 dias; L3: 1 ano) | **L2+** | pol-06 |
| 2.05 | Threat modeling foi realizado usando STRIDE como metodologia base | **L2+** | pol-08 |
| 2.06 | O threat modeling é reavaliado nos triggers definidos: nova integração, novo tipo de dado, alteração de arquitectura | **L2+** | pol-08 |
| 2.07 | Existe documentação de arquitectura de segurança (solution-architecture.md ou equivalente) actualizada | **L2+** | pol-09 |
| 2.08 | Decisões de arquitectura com impacto de segurança estão documentadas em ADRs com contexto, alternativas consideradas e impacto de segurança | **L2+** | pol-09 |
| 2.09 | O threat modeling inclui LINDDUN para aplicações que tratam dados pessoais | **L3** | pol-08 |
| 2.10 | O threat modeling tem revisão independente (por entidade não envolvida no design) | **L3** | pol-08 |
| 2.11 | Existe gate no pipeline CI/CD que verifica se a documentação de arquitectura está actualizada | **L3** | pol-09 |

---

## 3 - Dependências e SBOM

*Políticas: dependencias, sbom, excecoes-cve, atualizacao-automatica*

| # | Item | Nível | Política |
|---|------|:-----:|---------|
| 3.01 | Lock file está gerado e versionado no repositório | **L1+** | pol-10 |
| 3.02 | SCA está integrado no pipeline e produz resultados por cada build | **L1+** | pol-17 |
| 3.03 | Findings críticos e altos de SCA bloqueiam o pipeline | **L2+** | pol-10, pol-17 |
| 3.04 | Novas dependências requerem aprovação formal com validação de licença | **L2+** | pol-10 |
| 3.05 | SBOM é gerado automaticamente por release, inclui dependências transitivas e está associado ao artefacto com referência ao commit SHA | **L2+** | pol-11 |
| 3.06 | SBOM é arquivado durante o período mínimo obrigatório (L2: 1 ano; L3: 2 anos) | **L2+** | pol-11 |
| 3.07 | Excepções de CVE têm tipo explícito (not affected / fix not available / fix deferred / risk accepted), controlo compensatório e TTL conforme nível | **S** | pol-12 |
| 3.08 | O SLA de triagem de CVE é respeitado: Crítico ≤ 24h, Alto ≤ 48h | **S** | pol-12 |
| 3.09 | Existe processo de actualização automática de dependências (Renovate, Dependabot ou equivalente) activo e configurado | **L2+** | pol-13 |
| 3.10 | SBOM é assinado digitalmente com verificação de assinatura no deploy | **L3** | pol-11 |
| 3.11 | Proveniência completa está registada (SLSA attestation ou equivalente) | **L3** | pol-11 |
| 3.12 | Findings médios de SCA bloqueiam o pipeline | **L3** | pol-10 |

---

## 4 - Desenvolvimento Seguro

*Políticas: guidelines-desenvolvimento, revisao-codigo, uso-ferramentas-apoio*

| # | Item | Nível | Política |
|---|------|:-----:|---------|
| 4.01 | SAST está integrado no pipeline para todos os repositórios activos | **L1+** | pol-19 |
| 4.02 | Secret detection está activo no pipeline e bloqueia qualquer finding | **S** | pol-17, pol-18 |
| 4.03 | Não existem credenciais, tokens, chaves ou passwords hardcoded em código, ficheiros de configuração ou variáveis de ambiente versionadas | **S** | pol-18 |
| 4.04 | Self-approval está bloqueada por configuração do repositório (ninguém aprova o próprio código) | **S** | pol-15 |
| 4.05 | Supressões de regras de SAST (mutes/waives) têm aprovação formal com ID do finding, justificação técnica, responsável e prazo de validade | **S** | pol-14 |
| 4.06 | Existe um conjunto de guidelines de desenvolvimento seguro derivadas de fontes reconhecidas (OWASP, CWE, NIST) e operacionalizadas em linters ou regras de SAST | **L2+** | pol-14 |
| 4.07 | Code review com checklist de segurança explícito é obrigatório para todo o código que vai a produção | **L2+** | pol-15 |
| 4.08 | Findings críticos e altos de SAST bloqueiam o merge | **L2+** | pol-15, pol-17 |
| 4.09 | Revisão de AppSec é obrigatória para código de autenticação, autorização, dados sensíveis e configuração de segurança | **L2+** | pol-15 |
| 4.10 | O uso de ferramentas de IA generativa para produção de código segue política aprovada, com revisão humana obrigatória e sem envio de dados confidenciais | **L2+** | pol-16 |
| 4.11 | Guidelines estão operacionalizadas como policy-as-code e desvios requerem aprovação de AppSec | **L3** | pol-14 |

---

## 5 - CI/CD e Pipeline

*Políticas: cicd-seguro, gestao-segredos*

| # | Item | Nível | Política |
|---|------|:-----:|---------|
| 5.01 | A configuração do pipeline está versionada como código e sujeita a code review | **L2+** | pol-17 |
| 5.02 | Os security gates estão em modo bloqueante (não apenas report / continue-on-error) | **L2+** | pol-17 |
| 5.03 | Os thresholds dos gates estão documentados e versionados (ex: gates-config.yaml) | **S** | pol-17 |
| 5.04 | A identidade do pipeline é dedicada com mínimo de privilégios - sem permissão de auto-merge | **S** | pol-17 |
| 5.05 | Bypasses de gates de segurança têm aprovação formal registada: responsável, justificação técnica, referência a ticket/excepção, timestamp | **S** | pol-17 |
| 5.06 | Artefactos estão associados ao commit SHA que os produziu e são reprodutíveis | **S** | pol-17 |
| 5.07 | Segredos de pipeline são injectados via cofre centralizado (Vault, AWS Secrets Manager, Azure Key Vault ou equivalente) com auditoria de acesso | **L2+** | pol-18 |
| 5.08 | Existe segregação de segredos entre ambientes de produção e não-produção | **L2+** | pol-18 |
| 5.09 | O pipeline usa OIDC / workload identity com TTL curto (≤ 1h) em vez de credenciais de longa duração | **L3** | pol-18 |
| 5.10 | Rotação automática de credenciais de pipeline está configurada | **L3** | pol-18 |
| 5.11 | Artefactos são assinados digitalmente e a assinatura é verificada antes do deploy | **L3** | pol-17, pol-25 |

---

## 6 - IaC e Containers

*Políticas: iac-seguro, aprovacao-plan-iac, containers-seguros, golden-base-images*

| # | Item | Nível | Política |
|---|------|:-----:|---------|
| 6.01 | IaC é gerida como código: versionada, revista e aplicada via pipeline - nunca manualmente em produção | **S** | pol-21 |
| 6.02 | O princípio de mínimo privilégio é aplicado: sem wildcards em políticas de IAM em produção | **S** | pol-21 |
| 6.03 | Linting e scanning de IaC estão integrados no pipeline, com findings críticos e altos a bloquearem o apply | **L2+** | pol-21 |
| 6.04 | O apply de IaC requer aprovação formal antes de execução, registada com identidade e timestamp | **L2+** | pol-22 |
| 6.05 | Imagens de container usam bases de origem verificada, referenciadas por digest (nunca por tag mutável como `latest`) | **L2+** | pol-23, pol-24 |
| 6.06 | Imagens são construídas com multi-stage build e correm como utilizador não-root | **L2+** | pol-23 |
| 6.07 | Secrets não estão presentes em ARG, ENV do Dockerfile, nem em camadas da imagem | **S** | pol-23, pol-18 |
| 6.08 | Scanning de vulnerabilidades de imagens está integrado no pipeline com findings críticos e altos a bloquearem | **L2+** | pol-23 |
| 6.09 | Existe catálogo de golden base images com SLAs de patching definidos e processo de depreciação | **L2+** | pol-24 |
| 6.10 | Existe separação de funções no apply de IaC: autor ≠ revisor ≠ executor | **L3** | pol-22 |
| 6.11 | Admission controller está activo em modo de bloqueio (enforce / Deny) - não apenas audit ou warn | **L3** | pol-23 |
| 6.12 | Findings médios de IaC e containers bloqueiam o pipeline | **L3** | pol-21, pol-23 |

---

## 7 - Testes de Segurança

*Políticas: dast-fuzzing, estrategia-testes, release-seguro, aprovacao-release, pentesting*

| # | Item | Nível | Política |
|---|------|:-----:|---------|
| 7.01 | Existe uma plataforma centralizada de gestão de findings (DefectDojo ou equivalente) para consolidar SAST, DAST e SCA | **L2+** | pol-19 |
| 7.02 | SLAs de resolução de findings estão definidos por severidade e os findings são acompanhados contra esses SLAs | **L2+** | pol-19 |
| 7.03 | Falsos positivos de severidade Alta/Crítica têm evidência técnica e aprovação de AppSec antes de serem descartados | **S** | pol-19 |
| 7.04 | DAST está integrado em ambiente de staging com cobertura dos endpoints prioritários | **L2+** | pol-01, pol-19 |
| 7.05 | Existe gate de pré-release que agrega SAST/DAST/SCA/secret detection com resultado APROVADO/REJEITADO antes de qualquer deploy a produção | **L2+** | pol-20, pol-26 |
| 7.06 | Findings críticos ou altos em aberto bloqueiam a release (salvo excepção formal activa) | **L2+** | pol-20 |
| 7.07 | A aprovação de release está formalmente registada: quem aprovou, quando, referência ao gate report | **L2+** | pol-26 |
| 7.08 | Aplicações L3 têm pentest realizado antes da primeira colocação em produção | **L3** | pol-36 |
| 7.09 | Aplicações L3 têm pentest anual com autorização formal assinada (escopo, período, regras de engajamento) | **L3** | pol-36 |
| 7.10 | Findings críticos de pentest bloqueiam a ida a produção e têm retest obrigatório após remediação | **L3** | pol-36 |
| 7.11 | DAST cobre ≥ 80% dos endpoints em produção | **L3** | pol-01 |

---

## 8 - Deploy e Operações

*Políticas: deploy-seguro, rollback, monitorizacao-pos-deploy, logging-estruturado, monitorizacao-seguranca, gestao-alertas, irp*

| # | Item | Nível | Política |
|---|------|:-----:|---------|
| 8.01 | Deploys usam o artefacto produzido pelo pipeline, nunca reconstruído (digest imutável) | **S** | pol-25 |
| 8.02 | Segredos de produção são injectados em runtime via cofre (não em configuração estática versionada) | **S** | pol-18, pol-25 |
| 8.03 | Critérios de activação de rollback estão definidos (taxa de erros, latência, falhas de health check, alerta de segurança) | **S** | pol-27 |
| 8.04 | Deploys de emergência (fora do processo normal) têm aprovação post-facto registada em menos de 24h | **S** | pol-25, pol-26 |
| 8.05 | Existe estratégia de rollback documentada, testada e executável via pipeline (nunca manualmente directo) | **L2+** | pol-27 |
| 8.06 | Existe período de observação pós-deploy com métricas monitorizadas e critérios formais de fecho (L2: 30 min; L3: 60 min) | **L2+** | pol-28 |
| 8.07 | Logs de eventos de segurança estão em formato estruturado (JSON) com schema mínimo obrigatório (timestamp UTC, level, event.action, application, trace.id) | **L2+** | pol-29 |
| 8.08 | Logs não contêm passwords, tokens completos, dados de cartão ou PII não mascarada | **S** | pol-29 |
| 8.09 | Logs de segurança estão centralizados com retenção mínima de 1 ano (L2) / 2 anos para segurança e 3 anos para auditoria (L3/DORA) | **L2+** | pol-29 |
| 8.10 | Eventos de segurança críticos têm alertas definidos com runbooks (diagnóstico, acções imediatas, escalamento) | **L2+** | pol-30, pol-31 |
| 8.11 | Cada alerta tem SLA de resposta e encaminhamento automático definidos | **L2+** | pol-31 |
| 8.12 | Existe Incident Response Plan com critérios de activação, fases estruturadas e playbooks | **L2+** | pol-32 |
| 8.13 | Incidentes de segurança têm post-mortem realizado em menos de 5 dias úteis | **L2+** | pol-32 |
| 8.14 | Rollback automático está configurado para todos os tipos de artefacto com RTO ≤ 15 minutos | **L3** | pol-27 |
| 8.15 | Notificações regulatórias (RGPD ≤ 72h, DORA ≤ 4h alerta inicial, NIS2 ≤ 24h) são cumpridas dentro dos prazos legais | **L3** | pol-32 |

---

## 9 - Governação e Formação

*Políticas: contratacao-segura, rastreabilidade-organizacional, kpis-governacao, formacao-seguranca*

| # | Item | Nível | Política |
|---|------|:-----:|---------|
| 9.01 | Cada aplicação tem um responsável de segurança (Security Champion ou equivalente) formalmente designado | **L2+** | pol-34 |
| 9.02 | Existe registo de conformidade por aplicação com campos mínimos: nível, owner, capítulos verificados, excepções activas, data de última validação e data da próxima | **L2+** | pol-34 |
| 9.03 | Desvios identificados no registo de conformidade têm acção correctiva com owner e prazo | **S** | pol-35 |
| 9.04 | Existe programa de formação em segurança com trilhos definidos por perfil (developer, QA, DevOps, PO, Tech Lead) | **L2+** | pol-37 |
| 9.05 | Onboarding de novas pessoas inclui formação em segurança com avaliação mínima de 80% | **L2+** | pol-37 |
| 9.06 | Existe conjunto de KPIs de segurança definidos com fontes de dados, responsáveis e cadência de recolha | **L2+** | pol-35 |
| 9.07 | Fornecedores e terceiros têm due diligence de segurança realizado antes de contrato (política de segurança, gestão de vulnerabilidades, incidentes nos últimos 12 meses) | **L2+** | pol-33 |
| 9.08 | Contratos com fornecedores incluem cláusulas SbD-ToE (notificação de incidentes, proibição de subcontratação sem aprovação, rescisão por incumprimento) | **L2+** | pol-33 |
| 9.09 | Offboarding de fornecedores e colaboradores inclui revogação de todos os acessos em menos de 2 horas (imediato em caso de incidente de segurança) | **S** | pol-33 |
| 9.10 | Fornecedores L3 entregam SBOM por release e relatórios de testes de segurança periódicos | **L3** | pol-33 |
| 9.11 | Existe Security Champion com formação específica, com participação activa em comunidade de champions (reuniões mensais) | **L3** | pol-37 |
| 9.12 | Exercícios práticos de segurança são realizados periodicamente (labs, CTF ou tabletop de incidente) | **L3** | pol-37 |

---

## Resumo e scorecard

Use esta tabela para calcular a aderência por domínio após completar o checklist.

| Domínio | Items S | Items L1+ | Items L2+ | Items L3 | Total |
|---------|:-------:|:---------:|:---------:|:--------:|:-----:|
| 1 - Classificação e Risco | 4 | 2 | 0 | 1 | 7 |
| 2 - Requisitos e Ameaças | 0 | 0 | 7 | 3 | 11 |
| 3 - Dependências e SBOM | 2 | 2 | 5 | 3 | 12 |
| 4 - Desenvolvimento Seguro | 5 | 1 | 4 | 1 | 11 |
| 5 - CI/CD e Pipeline | 4 | 0 | 4 | 3 | 11 |
| 6 - IaC e Containers | 3 | 0 | 5 | 3 | 12 |
| 7 - Testes de Segurança | 1 | 0 | 6 | 4 | 11 |
| 8 - Deploy e Operações | 4 | 0 | 8 | 3 | 15 |
| 9 - Governação e Formação | 2 | 0 | 7 | 3 | 12 |
| **Total** | **25** | **5** | **46** | **24** | **96** |

### Leitura do score

| Score em items S | Interpretação |
|-----------------|---------------|
| &lt; 70% | O modelo não está adoptado - controlos fundamentais em falta |
| 70% – 89% | Adopção parcial - lacunas em controlos absolutos que requerem remediação prioritária |
| ≥ 90% | Linha de base respeitada - avaliar agora os items por nível |

| Score total por nível (S + L1+ + L2+ + L3) | Interpretação |
|--------------------------------------------|---------------|
| ≥ 80% em S + L1+ | Conforme para aplicações L1 |
| ≥ 80% em S + L1+ + L2+ | Conforme para aplicações L2 |
| ≥ 80% em todos os items | Conforme para aplicações L3 |

**Nota:** Itens marcados como S com resposta ✗ não são compensáveis por score noutras áreas - representam controlos absolutos que devem ser resolvidos independentemente do score global.

---

## Referências

| Documento | Relação |
|-----------|---------|
| [`kpis-governanca`](./kpis-governanca) | KPIs de domínio para medir a eficácia (complemento a este checklist) |
| [`kpis-kri-executivo`](./kpis-kri-executivo) | KRIs para reporte CISO/board |
| `020-assets/policies/` | Texto completo das 37 políticas que fundamentam este checklist |
| [`addon/12-processo-excecoes`](./addon/processo-excecoes) | Processo canónico de gestão de excepções (items 1.06, 1.07, 3.07, 4.05) |
