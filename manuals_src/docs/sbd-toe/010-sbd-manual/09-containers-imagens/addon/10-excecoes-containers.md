---
id: excecoes-containers
title: Excepções em Containers e Imagens
sidebar_position: 10
description: Especificidades da gestão de excepções no contexto de containers e imagens — admission control, image signing e scanning de vulnerabilidades
tags: [exceções, containers, imagens, admission-control, signing, scanning, opa, kyverno]
---

# Excepções em Containers e Imagens

> Processo base, alçadas, campos obrigatórios, cadeia de autoridade e lifecycle estão definidos em **Cap. 14 — `addon/12-processo-excecoes.md`**. Este ficheiro define apenas as especificidades deste domínio.

---

## Âmbito

Excepções a requisitos do catálogo de containers e imagens: `CNT-001` a `CNT-012`.

---

## Triggers específicos deste domínio

- imagem base legacy sem substituto imediato que cumpra os requisitos de origem aprovada (CNT-001);
- CVE crítico em imagem base sem patch disponível para a versão em uso — distinto das excepções SCA do Cap. 05 por actuar ao nível da imagem e ser verificado por admission controller (CNT-002);
- infraestrutura de assinatura de imagens (Cosign/Sigstore/Notary) ainda não disponível — excepção de migração com prazo definido (CNT-007);
- workload legado incompatível com políticas de admission controller activas — OPA/Gatekeeper, Kyverno — com plano de remediação (CNT-009);
- capacidade kernel ou syscall necessária e justificada tecnicamente que conflitua com o perfil restritivo exigido (CNT-006).

---

## Campos adicionais obrigatórios (containers)

| Campo | Obrigatório | Notas |
|---|---|---|
| Digest da imagem afectada | Sim | `sha256:...` — identificação inequívoca do artefacto |
| Registry de origem | Sim | |
| Admission controller em uso | Sim | OPA/Gatekeeper, Kyverno, ou equivalente |
| Policy / regra violada | Sim | Nome e versão da policy no admission controller |
| Excepção implementada no admission controller? | Sim | Se sim, referência ao objecto de excepção (ex: `PolicyException` Kyverno) |

---

## Excepções no admission controller

Excepções a políticas de admission controller devem ser implementadas como objectos formais no próprio sistema (ex: `PolicyException` em Kyverno, `constraint` com exclusão em OPA/Gatekeeper), não como desactivação da policy. O objecto de excepção no admission controller é um artefacto de evidência obrigatório e deve ser referenciado na cadeia de autoridade.

Excepções implementadas por desactivação global de uma policy são sempre não conformes, independentemente de aprovação organizacional.

---

## Excepções de image signing (migração)

Excepções a CNT-007 por infraestrutura de assinatura ainda não disponível devem incluir:

- plano de implementação com milestones e responsável;
- prazo máximo: 90 dias; extensão exige aprovação GRC/CISO;
- controlos compensatórios activos durante a janela de excepção (ex: verificação de digest, restrição de registries de origem).

---

## Referências cruzadas

| Documento | Relação |
|---|---|
| `00-catalogo-requisitos.md` | Catálogo CNT-001..012 — requisitos que podem ter excepções |
| `03-assinatura-cadeia-trust.md` | Infraestrutura de signing e verificação |
| `05-policies-runtime-opa.md` | Políticas de admission controller e mecanismo de excepção |
| `07-vulnerabilidades-imagens.md` | Scanning e CVEs em imagens |
| Cap. 05 — `addon/09-excecoes-e-aceitacao-risco.md` | Excepções SCA ao nível de pacote — distinto de CVE em imagem |
| Cap. 14 — `addon/12-processo-excecoes.md` | Processo canónico de gestão de excepções |
