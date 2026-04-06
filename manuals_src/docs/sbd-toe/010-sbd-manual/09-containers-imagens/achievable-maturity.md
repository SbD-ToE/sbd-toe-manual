---
id: achievable-maturity
title: Mapeamento de Maturidade - Capítulo 09
sidebar_position: 10
tags: [canon, maturidade, SAMM, SLSA, DSOMM]
---

> **Método:** Ver [Metodologia de Validação de Claims](../00-fundamentos/canon/26-metodologia-validacao-claims.md) para a baseline empírica dos autores, validação por índices semânticos, ontology backtrace e comparação com fontes externas.

# 📈 Maturidade - Containers e Imagens

Este documento apresenta o **grau de alinhamento entre as práticas descritas no Capítulo 09 do SbD-ToE - *Containers e Imagens*** e os principais frameworks de segurança e maturidade de software:

- **OWASP SAMM**
- **OWASP DSOMM**
- **SLSA**

O capítulo aborda **segurança de imagens e containers ao longo de todo o ciclo de vida**, incluindo:
- Construção segura e reprodutível de imagens;
- Assinatura, proveniência e rastreabilidade de artefactos;
- Governação de registos e pipelines;
- Hardening de *runtime* (Docker, Kubernetes, etc.);
- Validação de manifestos e observabilidade de execução.

Estas práticas integram-se diretamente com os capítulos **05 (Dependências e SBOM)** e **08 (IaC)**, reforçando a segurança da *supply chain*.

---

## 🎯 Como interpretar este mapeamento de maturidade

Este documento não mede a maturidade global de uma organização. Mede apenas o contributo deste capítulo para domínios de maturidade reconhecidos nas frameworks selecionadas.

| Framework   | Avaliação usada                 | Justificação                                      |
|-------------|----------------------------------|---------------------------------------------------|
| OWASP SAMM  | `n / 3`                          | Modelo prescritivo com progressão explícita       |
| OWASP DSOMM | `n / m`                          | Níveis formais por domínio técnico                |
| SLSA        | Nível máximo suportado (1–4)     | Leitura bounded de supply chain / build / release |

## 🧭 Visão Geral de Alinhamento

| Framework        | Domínios Relevantes | Práticas ou Objetos Cobertos | Avaliação de Maturidade |
|------------------|--------------------|------------------------------|--------------------------|
| **OWASP SAMM v2.1** | Deployment (DEP 1.2), Verification (2.A/2.B), Governance (GOV 1.2) | Build seguro, _policy-as-code_, assinatura, controlo de registos e validação de manifestos | **3 / 3** |
| **OWASP DSOMM** | Build & Deploy, Supply Chain, Ops Monitoring | Construção determinística, proveniência, hardening e observabilidade de _runtime_ | **3 / 4** |
| **SLSA v1.0** | Build Integrity, Provenance, Source Verification | Assinaturas, _attestations_, pipelines confiáveis e _digest pinning_ | **Nível 3 / 4** |

---

## 🧱 OWASP SAMM - Deployment, Verification e Governance

| Nível | Descrição SAMM | Cobertura pelo Cap. 09 |
|-------|----------------|------------------------|
| 1 | *Deploys* manuais e controlo básico | ✅ Governação mínima de imagens e registos |
| 2 | Pipelines automatizadas e validação de imagens | ✅ _Scanning_ e assinatura no CI/CD |
| 3 | Governação formal e políticas de aprovação automatizadas | ✅ _Policy-as-code_, _admission controllers_, rastreabilidade auditável |

**🧮 Maturidade atingida: 3 / 3**

---

## 🧱 OWASP DSOMM - Build & Deploy / Supply Chain / Ops Monitoring

| Domínio | Nível | Justificação técnica |
|----------|-------|----------------------|
| **Build & Deploy** | 3 / 4 | Pipelines determinísticos, verificação de proveniência e _attestation_. |
| **Supply Chain** | 3 / 4 | Assinatura, rastreabilidade e governação de registos e dependências. |
| **Ops Monitoring** | 3 / 4 | Observabilidade, deteção de _drift_ e _shadow containers_. |

---

## 🧱 SLSA v1.0 - Build Integrity & Provenance

| Nível | Requisitos | Cobertura pelo Cap. 09 |
|-------|-------------|-------------------------|
| 1 | Builds rastreáveis e controlados | ✅ Dockerfiles versionados e CI/CD auditável |
| 2 | Proveniência autenticada | ✅ _Digest pinning_ e _attestation_ de origem |
| 3 | Build isolado e reproduzível | ✅ Assinaturas, _attestations_ e verificação automática |
| 4 | Cadeia totalmente verificada e hermética | ❌ Fora do âmbito (nível de integração infraestrutural) |

**🔐 Nível atingido: SLSA 3 / 4**

---


## ✅ Conclusão

- Este capítulo sustenta uma leitura de maturidade principalmente ancorada em **OWASP SAMM** e **OWASP DSOMM**;
- Quando aplicável, também suporta uma leitura bounded em **SLSA**, sem pretender medir a maturidade global da organização;
- A avaliação apresentada é **chapter-scoped** e contributiva, não substituindo uma avaliação formal framework-native.

