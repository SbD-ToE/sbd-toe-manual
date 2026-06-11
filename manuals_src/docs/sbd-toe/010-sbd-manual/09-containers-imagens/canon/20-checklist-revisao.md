---
id: checklist-revisao
title: Checklist - Containers e Imagens
sidebar_label: Checklist de Revisão
description: Checklist binário e auditável para avaliar a adoção prática das práticas prescritas no Capítulo 09 - Containers e Imagens
tags: [checklist, containers, imagens, supply chain, kubernetes, auditoria]
sidebar_position: 20
---

# Checklist de Revisão Periódica - Containers e Imagens

Este checklist aplica-se a todos os projetos e pipelines que **constroem, distribuem ou executam containers e imagens** no âmbito do Capítulo 09 - Containers e Imagens (`CNT-001` a `CNT-012`).
Serve como instrumento de verificação binária e auditável da **adoção prática das prescrições deste capítulo**, permitindo:

- Controlo sistemático da segurança na cadeia de construção e execução de containers;
- Verificação por projeto em momentos-chave do ciclo de vida (build, deploy, operação);
- Geração de indicadores de conformidade técnica e maturidade de *supply chain security*.

> 🗓️ **Recomenda-se a sua aplicação a cada release significativa**, ou sempre que existirem alterações nas imagens base, pipelines, registos ou configurações de *runtime*.

---

## 📋 Itens de Verificação

| Item                                                                                                           | Verificado? |
|----------------------------------------------------------------------------------------------------------------|-------------|
| As imagens base provêm de uma lista de origens aprovada e mantida, e as imagens de origem não aprovada são rejeitadas? (`CNT-001`) | ☐           |
| Cada imagem é referenciada por digest SHA imutável, sem tags flutuantes? (`CNT-001`)                          | ☐           |
| As imagens são minimalistas (sem binários interativos não justificados), com rebuild periódico por SLA de patching? (`CNT-003`/`CNT-010`) | ☐           |
| Existe catálogo versionado de Golden Base Images com estados de aprovação, depreciação e revogação?           | ☐           |
| Existe allowlist de registries com bloqueio por origem, acesso autenticado com logs retidos e aprovação para publicação em registries públicos? (`CNT-011`) | ☐           |
| Existe scanner de vulnerabilidades ativo no CI/CD e as de severidade igual ou superior ao limiar bloqueiam o build ou deploy? (`CNT-002`) | ☐           |
| É gerado e anexado SBOM (CycloneDX ou SPDX) a cada imagem publicada, acessível para auditoria? (`CNT-008`)    | ☐           |
| Os containers executam como utilizador não-root? (`CNT-004`)                                                  | ☐           |
| As capabilities do kernel são restringidas (`drop: ALL` + adições justificadas) e existe perfil seccomp/AppArmor ativo? (`CNT-006`) | ☐           |
| O sistema de ficheiros root está configurado como read-only em runtime? (`CNT-005`)                          | ☐           |
| A execução privilegiada e o acesso ao Docker socket / hostPID / hostNetwork estão bloqueados, e o estado efetivo de hardening é verificado contra o declarado (drift)? (`CNT-006`) | ☐           |
| As imagens são assinadas (com transparency log) e a assinatura/proveniência é verificada por admission controller antes do deploy? (`CNT-007`) | ☐           |
| O admission controller está em modo enforce e valida os manifestos contra políticas versionadas (OPA/Kyverno), com logs de admissão e rejeição? (`CNT-009`) | ☐           |
| Os workloads usam ServiceAccount dedicada com RBAC mínimo e NetworkPolicy com deny-all default e egress controlado, com workloads críticos em namespaces dedicados? (`CNT-012`) | ☐           |
| As imagens estão livres de credenciais embebidas (verificado por secret scanning no build) e os containers obtêm credenciais via identidade efémera? | ☐           |
| Para workloads críticos L3, é usado sandboxing avançado (gVisor/Kata/Firecracker via RuntimeClass) e os runners/builders são efémeros, assinados e com limites de recursos? | ☐           |
| Existe rastreabilidade commit → pipeline → imagem → decisão → execução, com registo da decisão humana de promoção, retenção/limpeza de imagens obsoletas e exceções com TTL e objeto formal no admission controller? | ☐           |
| Os runtimes de inferência AI self-hosted protegem os pesos do modelo (encriptação at-rest com chaves no cofre, verificação de integridade por hash, acesso auditado), com isolamento de GPU e separação de workloads sensíveis? | ☐           |
| As APIs de inferência AI exigem autenticação, rate limiting por consumo e limites de `max_tokens`/prompt/timeout, com auditoria por principal, network policy restritiva e runtime pinned com SCA? | ☐           |

---

## 🔄 Notas de aplicação prática

- Este checklist pode ser convertido em **etapa automatizada de CI/CD**, formulário digital de validação ou dashboard de conformidade de containers.
- Cada item deve ser tratado como **indicador binário (sim/não)**, permitindo cálculo de KPIs de adoção por projeto, pipeline ou equipa.
- A validação completa deste checklist confirma **conformidade técnica com o Capítulo 09**, sustentando auditorias de segurança e avaliações de maturidade SbD-ToE.
- Os resultados podem ser correlacionados com o **Capítulo 05 - Dependências e SBOM**, garantindo rastreabilidade total da cadeia de fornecimento.

> ❗ Este capítulo é **essencial para a integridade e segurança da cadeia de construção e entrega de software**.
> A ausência destas práticas compromete a confiança nos artefactos distribuídos e a conformidade com requisitos de *supply chain security* previstos em NIS 2 e DORA.
