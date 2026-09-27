---
id: excecoes-e-aceitacao-risco
title: Exceptions and Risk Acceptance for Dependency Vulnerabilities
description: Specifics of exception management in the context of SCA/CVE findings
tags: [dependencias, sbom, sca, exceptions, cve]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/05-dependencias-sbom-sca/addon/09-excecoes-e-aceitacao-risco.md
  source_sha256: b4449a510d89391a1b2001b3b0bc42f02d9dc75126479826607bfcab09288cf4
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 4173375fbdf3248ca49424168cf09e0b701181b107955eba0550d11827db0256
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 0594036caa5df5f000ba40e62fe5e20f348d76f6f2035281e833391c2c9abd3a
  glossary_keys: [alcada, verification_taxonomy]
  glossary_sha256: ca57fbded2cb330dec602db86ba3c90758836012e798bdeea36a2461df38dae5
  translated_at: 2026-09-26T08:45:26Z
  reviewed_by: null
---

# Exceptions and Risk Acceptance for Dependency Vulnerabilities

> The base process, approval authorities, mandatory fields, chain of authority and lifecycle are defined in **Ch. 14 - `addon/12-processo-excecoes.md`**. This file defines only the specifics of this domain.

---

## Scope {#âmbito}

Exceptions to software composition analysis (SCA) findings - vulnerabilities in dependencies identified by a scanner, referenced by CVE or equivalent.

---

## Triggers specific to this domain {#triggers-específicos-deste-domínio}

An SCA exception requires that **all** of the following criteria be analysed and documented:

- the vulnerability has no direct impact on the application's execution context (e.g. a dependency used only in the build, not at runtime);
- there is no viable alternative version with the same expected behaviour;
- there are effective and verifiable compensating controls (e.g. sandboxing, WAF, build isolation);
- the residual risk is explicitly documented and formally accepted.

The absence of an available patch is a necessary but not sufficient condition for approval of the exception.

---

## Additional mandatory fields (SCA) {#campos-adicionais-obrigatórios-sca}

| Field | Mandatory | Notes |
|---|---|---|
| CVE / vulnerability ID | Yes | |
| Affected component | Yes | Exact name and version (e.g. `lib-legacy@1.0.4`) |
| Context of use | Yes | `runtime` / `build-only` / `test-only` |
| Fixed version available? | Yes | If so, justification for not applying it |

---

## YAML template {#template-yaml}

```yaml
- cve: CVE-YYYY-NNNNN
  componente: nome-do-pacote@versao
  contexto: build-only | runtime | test-only
  motivo: "Justificação técnica objectiva"
  controlo_compensatorio: "Controlo alternativo aplicado"
  aprovado_por: "nome@funcao"
  validade: "YYYY-MM-DD"
  revisao_agendada: true
```

Suggested location: `/security/excecoes-sca.yaml` in the repository, or a centralised system with traceable equivalence.

---

## Cross-references {#referências-cruzadas}

| Document | Relation |
|---|---|
| `02-analise-sca.md` | Origin of the findings that may give rise to an exception |
| `04-integracao-ci-cd.md` | Verification of the validity of exceptions in the pipeline |
| `08-rastreabilidade-vulnerabilidades.md` | Recording of the risk acceptance decision as a final state |
| Ch. 14 - `addon/12-processo-excecoes.md` | Canonical exception management process |
