---
id: tlpt-readiness
title: TLPT — Readiness e Enquadramento Regulatório (DORA)
description: Pré-condições técnicas e de governança para Threat-Led Penetration Testing (TLPT) em contexto DORA, e como o SbD-ToE suporta a preparação e documentação de base para attestation regulatório.
tags: [tlpt, dora, pentest, threat-intelligence, resiliência, regulatório, attestation, tiber-eu]
---

# 🎯 TLPT — Readiness e Enquadramento Regulatório (DORA)

O **Threat-Led Penetration Testing (TLPT)** é o nível mais exigente de validação ofensiva previsto no quadro regulatório europeu. Ao contrário do PenTest convencional — descrito no [addon 11](./11-pen-testing.md) —, o TLPT não é uma prática opcional de maturidade: é uma **obrigação regulatória** para entidades identificadas pela autoridade competente, com requisitos específicos de âmbito, metodologia, qualificação de executores e attestation formal pela autoridade TLPT designada.

Este addon define o que é o TLPT, o que o SbD-ToE já cobre como base de preparação, e o que está **explicitamente fora do âmbito do manual** — sendo da responsabilidade das equipas jurídicas, de compliance e de relação com o supervisor.

> **Convenção usada neste documento:**
> - 📜 **Regulatório** — requisito ou disposição directamente previsto no DORA ou nos RTS
> - 🛠️ **Boa prática SbD-ToE** — recomendação de maturidade técnica que suporta o processo TLPT, sem ser obrigação legal explícita

---

## 1) Enquadramento normativo

### Regulamento DORA

O TLPT está regulado pelo **Regulamento (UE) 2022/2554** (DORA), em vigor desde 17 de janeiro de 2025:

| Artigo | Conteúdo |
|--------|----------|
| **Art. 26** | Requisitos de TLPT — âmbito, ambiente de produção, frequência, pooled testing, attestation |
| **Art. 27** | Requisitos para os executores de TLPT (testers) — independência, competências, qualificação |

As normas técnicas de regulamentação (RTS) que detalham a metodologia TLPT foram publicadas como **Regulamento Delegado (UE) 2025/1190** da Comissão, em vigor desde **8 de julho de 2025**.

### Base metodológica: TIBER-EU

O TLPT previsto no DORA é compatível com o **framework TIBER-EU** (Threat Intelligence-Based Ethical Red Teaming), publicado pelo Banco Central Europeu (BCE, 2018). Vários bancos centrais nacionais publicaram variantes nacionais (ex: TIBER-PT, TIBER-NL, TIBER-DE).

> O TIBER-EU não é substituído pelo DORA — é a referência metodológica de base que os RTS formalizam. Entidades que já tenham conduzido exercícios TIBER podem utilizar esses resultados como contributo para o processo DORA, **desde que os exercícios sejam reconhecidos como alinhados com o Reg. Delegado (UE) 2025/1190 e aceites pela autoridade TLPT designada**. Esta equivalência não é automática.

### Quem está sujeito a TLPT

📜 O TLPT **não se aplica a todas as entidades financeiras** abrangidas pelo DORA. A sujeição é determinada pelas autoridades competentes com base em critérios de risco e impacto sistémico, nos termos do Art. 26 DORA e dos RTS:

- A identificação é feita pela autoridade competente, não pela entidade;
- Os critérios incluem dimensão, perfil de risco, impacto sistémico e interconexão;
- A obrigação tem periodicidade mínima de **3 em 3 anos** (Art. 26 DORA);
- As autoridades podem ajustar a frequência com base no perfil de risco da entidade.

> ⚠️ **Lacuna explícita do SbD-ToE:** Os critérios de identificação de entidades sujeitas a TLPT e o processo de notificação pela autoridade competente estão fora do âmbito deste manual. Consultar o supervisor nacional e o Reg. Delegado (UE) 2025/1190.

---

## 2) O que distingue TLPT de PenTest convencional

| Dimensão | PenTest (addon 11) | TLPT |
|----------|-------------------|------|
| **Origem dos cenários** | Âmbito técnico definido internamente | 📜 Cenários derivados de threat intelligence real sobre o setor e a entidade |
| **Ambiente de execução** | Preferencialmente staging | 📜 **Produção real** — obrigatório (Art. 26(2) DORA) |
| **Executores** | Internos ou externos sem requisito formal | 📜 Testers qualificados segundo Art. 27 DORA e RTS; interno possível com salvaguardas específicas |
| **Confidencialidade** | Processo documentado normalmente | 📜 **Need-to-know restrito** — um número muito limitado de pessoas sabe que o exercício está a decorrer |
| **Terceiros fornecedores** | Fora de âmbito | 📜 Podem ser incluídos via **pooled testing** com consentimento (Art. 26 DORA) |
| **Resultado** | Relatório interno + remediação | 📜 Relatório + **attestation formal pela autoridade TLPT designada** (Art. 26(7) DORA) |
| **Frequência** | Recomendada (L3: anual) | 📜 Obrigatória — mínimo cada 3 anos |
| **Base regulatória** | Boa prática / requisito interno | 📜 Obrigação legal (DORA) |

---

## 3) Pré-condições de readiness

O SbD-ToE não estabelece o TLPT em si, mas a maturidade técnica e documental que produz **é relevante para a qualidade e sustentação do exercício**. Esta secção distingue explicitamente o que é obrigação regulatória do que é boa prática de preparação.

### 3.1 Threat Model → Cap. 03

🛠️ O TLPT é "threat-led" porque os cenários são derivados de threat intelligence real. Para que esses cenários sejam aplicáveis à entidade com eficácia, é útil ter:

- Um threat model baseline aprovado (ver US-09, Cap. 03);
- Identificação das funções críticas e ativos de alto valor (*crown jewels*);
- Mapeamento de superfície de ataque atualizado.

> Não existe disposição nos RTS que exija formalmente um threat model interno como pré-condição. No entanto, a sua ausência tende a produzir cenários TLPT genéricos com menor cobertura dos riscos reais da entidade.

### 3.2 Programa de testes de segurança aplicacional → Cap. 10

🛠️ A existência de um programa de testes — SAST, DAST, IAST, fuzzing, PenTest — não é pré-condição regulatória para realizar TLPT. Uma entidade é identificada para TLPT pela sua relevância sistémica e perfil de risco ICT, independentemente do estado do seu programa de testes.

O que o TLPT faz, entre outras coisas, é **tornar esse estado visível**: expõe lacunas de cobertura, mede a eficácia real dos controlos em produção e fundamenta o plano de remediação. Nesse sentido, o exercício tem também uma função diagnóstica.

Compreender o que cada técnica de teste cobre — e o que não cobre — ajuda a interpretar os resultados do TLPT com mais precisão e a estruturar a remediação de forma mais dirigida. Os addons 01–08 e 11 deste capítulo fornecem esse enquadramento técnico.

> A ausência de SAST, DAST, PenTest etc. não impede legalmente a realização de TLPT — ficará, no entanto, reflectida nos resultados do exercício e no plano de remediação exigido para attestation.

### 3.3 Monitorização e resposta a incidentes → Cap. 12

🛠️ O TLPT é executado em produção real. A presença de monitorização operacional permite distinguir actividade do exercício de uma ameaça real, e é condição de segurança para a execução controlada:

- SIEM/log aggregation em produção;
- Playbooks de IR documentados e testados;
- Alertas críticos com SLA de resposta definido.

> A existência de monitorização em produção não é requisito formal nos RTS para a realização de TLPT, mas é uma salvaguarda operacional que as equipas de segurança e os testers qualificados considerarão na fase de planeamento.

### 3.4 Framework contratual com terceiros → Cap. 14

📜 O TLPT envolve testers qualificados externos e, potencialmente, fornecedores ICT via pooled testing. Os RTS estabelecem requisitos de independência e qualificação para os executores (Art. 27 DORA).

🛠️ O framework de governança contratual do Cap. 14 pode suportar a preparação de:

- NDA e acordos de acesso para testers;
- Cláusulas de segurança em contratos com ICT third-party providers relevantes;
- Processo de gestão de acesso privilegiado temporário.

---

## 4) O que o TLPT exige além do SbD-ToE

Os seguintes elementos são **obrigações do processo TLPT** (📜 regulatório) que estão fora do âmbito de cobertura do SbD-ToE e devem ser geridos pelas equipas de compliance, GRC e relação com o supervisor:

| Elemento | Descrição | Responsável |
|----------|-----------|-------------|
| **Identificação de sujeição** | 📜 Notificação pela autoridade competente de que a entidade está sujeita a TLPT | Compliance / Direção |
| **Threat intelligence provider** | 📜 Provider qualificado e validado segundo os critérios do Reg. Delegado (UE) 2025/1190 | GRC / CISO |
| **Qualificação dos testers** | 📜 Verificação de conformidade com Art. 27 DORA e RTS (experiência, referências, certificações, avaliação pela entidade e autoridade) | GRC / Legal |
| **Notificação à autoridade** | 📜 Comunicação formal antes do início do exercício | Compliance |
| **Processo de pooled testing** | 📜 Coordenação com fornecedores ICT em âmbito, com consentimento (Art. 26 DORA) | GRC / Legal |
| **Plano de remediação com SLAs** | 📜 Documentação pós-exercício exigida para attestation | CISO / Direção |
| **Attestation** | 📜 Validação formal do exercício e resultado pela **autoridade TLPT designada** (Art. 26(7) DORA) | Autoridade TLPT + Direção |

> Os relatórios e evidências produzidos no âmbito do SbD-ToE (threat model, findings de testes, release gates, evidências de remediação) **podem suportar a documentação de base** do processo de attestation. A rastreabilidade que o manual estabelece é adequada para contextualizar a postura de segurança da entidade perante o supervisor — não substitui os artefactos regulatórios específicos do processo TLPT.

---

## 5) Integração explícita com este capítulo

Este addon articula-se com o restante Cap. 10 da seguinte forma:

| Addon / secção | Contribuição para TLPT readiness |
|----------------|----------------------------------|
| **00 — Estratégia de testes** | 🛠️ Define programa base; TLPT é camada de topo |
| **01–04 (SAST/DAST/IAST/Fuzzing)** | 🛠️ Maturidade técnica que facilita a interpretação de resultados TLPT |
| **08 — Gestão de findings** | 🛠️ Registo auditável que pode suportar documentação para attestation |
| **11 — PenTest** | 🛠️ Metodologia e governança base reutilizáveis na preparação do exercício |
| **10 — Evidência e reprodutibilidade** | 🛠️ Princípio transversal ao exercício TLPT |

---

## 6) Checklist de readiness (binário)

| Item | Regulatório / Boa prática | Sim/Não |
|------|:-------------------------:|:-------:|
| Sujeição a TLPT confirmada pela autoridade competente | 📜 | |
| Threat intelligence provider qualificado identificado e validado segundo RTS | 📜 | |
| Testers externos verificados quanto a requisitos de qualificação (Art. 27 DORA + RTS) | 📜 | |
| Processo de notificação à autoridade TLPT preparado | 📜 | |
| Processo de pooled testing avaliado (ICT providers relevantes identificados) | 📜 | |
| Plano de remediação pós-exercício com SLAs definido | 📜 | |
| Processo de need-to-know definido (quem sabe, quando e como) | 📜 | |
| Threat model baseline aprovado com funções críticas identificadas (Cap. 03) | 🛠️ | |
| Crown jewels / ativos de alto valor documentados | 🛠️ | |
| Programa de testes de segurança aplicacional avaliado — nível de maturidade documentado (Cap. 10) | 🛠️ | |
| Monitorização e IR em produção com playbooks testados (Cap. 12) | 🛠️ | |
| Evidências SbD-ToE organizadas como suporte documental ao processo de attestation | 🛠️ | |

---

## ✅ Conclusão

O TLPT é a expressão mais exigente do princípio *"testar como o adversário ataca"*. A dimensão regulatória — identificação pela autoridade, qualificação de testers e providers, attestation — é estritamente da competência do supervisor e das equipas de compliance, e está fora do âmbito do SbD-ToE.

O papel do SbD-ToE é diferente mas complementar: **construir e documentar a base técnica** que torna um exercício TLPT com substância — cenários mais realistas, cobertura mais dirigida, remediação mais fundamentada.

> 📌 Os relatórios e evidências produzidos ao longo do ciclo SbD-ToE (threat model aprovado, findings rastreados, release gates, planos de remediação) são adequados para suportar a documentação de contexto no processo de attestation DORA. Manter rastreabilidade desde o início não é overhead — é o que torna o TLPT auditável e a remediação credível.
