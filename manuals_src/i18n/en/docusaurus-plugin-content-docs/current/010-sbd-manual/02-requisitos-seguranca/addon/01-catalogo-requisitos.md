---
id: catalogo-requisitos
title: Defining the Application Requirements Catalogue
description: Essential list of security requirements organised by category and risk level
tags: [tipo:catalogo, tema:requisitos, rastreabilidade, criticidade, ASVS]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/02-requisitos-seguranca/addon/01-catalogo-requisitos.md
  source_sha256: b232a9e943ac6c8520ddde171823146e7c5e853f57b7034b00f3b94130ccffe0
  source_commit: 28f13ce4d7e0acbbdc6a21d6cf195544784b0b07
  target_sha256: 37db3f883222001722d4078e2acb2ea3caac31ccf7f6d7f3931869a54e696e57
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [chapter_role, cycle_iteration, lifecycle_phase, requirement_runtime, risk_level, sbdtoe_sbd, traceability, validation_evaluation]
  glossary_sha256: 8f820b66eb2dbb337220a7ce2bca1caf2cae8800a17edd10978069b3e2e0ab1d
  translated_at: 2026-09-26T10:39:34Z
  stamped_at: 2026-09-26T18:32:58Z
  reviewed_by: null
---

<!--template: sbdtoe-addon -->

# Application Requirements Catalogue

The **security requirements catalogue** is one of the pillars of the SbD-ToE model. It works as a structured reference that ensures every application, project or system adopts controls suited to its risk level, type and operational context.
The SbD-ToE catalogue provides the **canonical reference identifiers** (`AUT-001`, `LOG-003`, etc.) - stable, project-independent and aligned with external frameworks. Each organisation must build its own catalogue from this base, and each project instantiates the applicable requirements as **traceable operational tags** (`SEC-L2-AUT-MFA`). The distinction between the two systems and the instantiation model are described in [Taxonomy and Traceability](./taxonomia-rastreabilidade).

A formal catalogue makes it possible to:
- Guarantee **proportionality** of the demands (L1, L2, L3), avoiding both overload and gaps;
- Ensure **traceability** between risk, requirement, control and evidence;
- Integrate security requirements into the development, audit and maintenance processes;
- Serve as a common base for curation, evolution and organisational adaptation.

This chapter includes a catalogue consolidated from multiple recognised sources (ASVS, MSTG, NIST SSDF, IEC 62443, among others). It is meant to be **adapted and curated by each organisation or project**, so as to stay aligned with the context and the state of the art. It is not immutable: it is a living document and must be maintained regularly and kept up to date. 

---

## 📌 How to apply this catalogue in SbD-ToE {#-como-aplicar-este-catálogo-no-sbd-toe}

1. **Proportional selection**:  
   Each requirement indicates the risk level(s) at which it is mandatory or recommended (L1, L2, L3).

2. **Continuous curation**:  
   Periodic review and adaptation of these requirements is recommended, adding or adjusting according to the type of application, emerging threats and business context.

3. **Operational integration**:  
   The catalogue must be incorporated into the backlog processes, the definition of acceptance criteria, testing and validation, as well as into technical documentation and audits.

4. **Evolution and coverage**:  
   New requirements can (and must) be added on the basis of lessons learned, incidents, new standards or changes of context.

---

## 📚 Quick reference to the base requirements {#-consulta-rápida-dos-requisitos-base}

The proportional application of requirements by technical domain can be consulted in the  
[Base Requirements Catalogue (annex to this chapter)](/sbd-toe/sbd-manual/requisitos-seguranca/addon/lista-requisitos-base):

- [AUT - Authentication and Identity](lista-requisitos-base#aut) 
- [ACC - Access Control](lista-requisitos-base#acc) 
- [LOG - Logging and Monitoring](lista-requisitos-base#log)
- [SES - Sessions and State](lista-requisitos-base#ses) 
- [VAL - Data Validation](lista-requisitos-base#val)
- [ERR - Error Handling](lista-requisitos-base#err)
- [CFG - Secure Configuration](lista-requisitos-base#cfg)
- [ENC - Sensitive Data and Cryptography](lista-requisitos-base#enc)
- [API - API Security](lista-requisitos-base#api)
- [INT - Messaging and Integrations](lista-requisitos-base#int)
- [REQ - Requirements Definition](lista-requisitos-base#req)
- [DST - Artefact Distribution](lista-requisitos-base#dst)
- [IDE - Development Tools](lista-requisitos-base#ide)

For a quick reference to the proportional application of requirements by risk level, see the annex “Base Requirements Catalogue” at the end of this chapter.

---

## 📌 Closing Note {#-nota-final}

The catalogue must be understood as a **living, adaptable reference** - the starting point for defining the concrete requirements of each organisation or project, and for the effective integration of security across the entire software lifecycle.

> For validation, acceptance criteria and evidence, see the [requirements validation](./validacao-requisitos) section.
