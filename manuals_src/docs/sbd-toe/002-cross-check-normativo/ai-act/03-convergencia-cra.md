---
id: convergencia-cra
title: Nota - Convergência AI Act & CRA
description: Orientação para produtos que são simultaneamente sistema de IA de alto risco (AI Act) e produto com elementos digitais (CRA) - presunção de conformidade do Art. 12 do CRA e avaliação de conformidade única no eixo cibersegurança
sidebar_position: 3
tags: [ai-act, cra, convergencia, presuncao-conformidade, ciberseguranca]
---

# Nota: Produtos abrangidos por AI Act e CRA

## Âmbito

Esta nota destina-se a fabricantes de **produtos com elementos digitais** que são, em simultâneo, **sistemas de IA de alto risco** (AI Act, Art. 6) e produtos abrangidos pelo **Cyber Resilience Act** (Regulamento (UE) 2024/2847). Ao contrário da relação NIS2 ↔ DORA - dois regimes de gestão de risco organizacional resolvidos por *lex specialis* -, aqui a relação é de **presunção de conformidade** e **avaliação de conformidade única** no eixo da cibersegurança.

Os dois regulamentos aplicam-se **cumulativamente**, mas o legislador construiu uma ponte explícita no plano técnico da cibersegurança para evitar trabalho em duplicado.

## A relação não é *lex specialis* - é presunção de conformidade

O **Art. 12 do CRA** estabelece que um produto classificado como sistema de IA de alto risco ao abrigo do Art. 6 do AI Act é **presumido conforme com os requisitos de cibersegurança do Art. 15 do AI Act** quando se verifiquem, cumulativamente, três condições:

| Condição (CRA Art. 12) | O que exige | Onde o SbD-ToE entra |
|---|---|---|
| Anexo I, **Parte I** do CRA | Requisitos essenciais de cibersegurança do **produto** | [Cap. 04](/sbd-toe/sbd-manual/arquitetura-segura/intro) (arquitetura), [Cap. 10](/sbd-toe/sbd-manual/testes-seguranca/intro) (testes), [Cap. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro) |
| Anexo I, **Parte II** do CRA | Requisitos de **tratamento de vulnerabilidades** (processos do fabricante) | [Cap. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro) (SBOM/SCA), [Cap. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro) |
| Declaração UE de conformidade | Demonstrar nela o nível de cibersegurança exigido pelo Art. 15 do AI Act | Evidência técnica agregada (Cap. 03–12) |

Verificadas as três, **não é necessário demonstrar separadamente** o Art. 15 do AI Act: a conformidade com o CRA, declarada, vale como conformidade com aquele requisito do AI Act.

## Avaliação de conformidade única

O CRA Art. 12 remete a avaliação para o **procedimento de avaliação de conformidade do Art. 43 do AI Act**. Além disso, os **organismos notificados** competentes para o sistema de IA de alto risco ao abrigo do AI Act são também competentes para controlar a conformidade com o Anexo I do CRA (sujeito ao Art. 39 do CRA). Resultado prático: **uma avaliação, um organismo, uma declaração** - cobrindo o eixo cibersegurança de ambos os regulamentos.

> ⚖️ **Derrogação.** Determinados produtos importantes e críticos (CRA, Anexos III e IV) podem seguir procedimentos de avaliação de conformidade alternativos previstos no CRA, em função da sua classificação e de eventuais certificados. A escolha do procedimento é matéria de compliance/jurídico.

## Onde os âmbitos se cruzam e onde divergem

| Tema | AI Act | CRA | Convergência |
|---|---|---|---|
| Cibersegurança do produto | Art. 15 | Anexo I, Partes I e II | **Presunção** (CRA Art. 12) |
| Tratamento de vulnerabilidades | Implícito no Art. 15 | Anexo I, Parte II (detalhado) | Base técnica comum — a presunção (CRA Art. 12) é o mecanismo de conformidade, não a mera adoção do processo |
| Cadeia de fornecimento / SBOM | Art. 15 (integridade) | Anexo I | SBOM único ([Cap. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro)) |
| Reporte | Art. 73 (incidentes graves) | Art. 14 (vulnerabilidades ativamente exploradas / incidentes graves a ENISA) | Circuitos **distintos**, base de deteção partilhada ([Cap. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)) |
| Marcação CE / declaração | Art. 43, 47–49 | Avaliação CRA | Coordenadas via Art. 12 |
| Governação de dados, supervisão humana, transparência, FRIA | Art. 10, 13, 14, 27 | — | **Só AI Act** (fora do CRA e do SbD-ToE) |

## O que continua próprio de cada regulamento

**Só o AI Act** (não coberto pela presunção do CRA): gestão de risco (Art. 9), governação de dados e enviesamento (Art. 10), supervisão humana (Art. 14), transparência (Art. 13 e 50), avaliação de impacto sobre direitos fundamentais (Art. 27) e as obrigações GPAI (Art. 53/55). A presunção do Art. 12 do CRA **cobre apenas o Art. 15** (cibersegurança) - todas as restantes obrigações de alto risco do AI Act mantêm-se integralmente.

**Só o CRA**: tratamento de vulnerabilidades ao longo de todo o ciclo de vida (Anexo I, Parte II), divulgação coordenada de vulnerabilidades, obrigação de atualizações de segurança e período de suporte, e o reporte de vulnerabilidades ativamente exploradas a ENISA/CSIRT (Art. 14).

## Riscos de Duplicação (Evitar)

| Duplicação potencial | Porque evitar | Forma única recomendada |
|---|---|---|
| Duas avaliações de conformidade de cibersegurança | Custo e inconsistência | Acionar a presunção do CRA Art. 12; uma só avaliação (Art. 43 AI Act) |
| Dois processos de *vulnerability handling* | Divergência de SLAs/registos | Implementar o do CRA (Anexo I, Parte II); serve também o Art. 15 |
| Dois SBOM | Overhead, deriva | SBOM/AI-BOM único ([Cap. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro)) |
| Duas bases de evidência técnica | Re-trabalho | Evidência de cibersegurança única ([Cap. 03](/sbd-toe/sbd-manual/threat-modeling/intro), [04](/sbd-toe/sbd-manual/arquitetura-segura/intro), [10](/sbd-toe/sbd-manual/testes-seguranca/intro), [12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)) marcada por fonte |

## Estratégia de Implementação Única (SbD-ToE)

> ✏️ **Refresh 2026-05-30.** Estratégia actualizada após o *release agentic* — várias peças que eram "a implementar" estão agora dentro do canon ([`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015), [`DEP-012`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-012), `OPS-012..014`, Policy 38, Policy 39).

1. **Evidência de cibersegurança única** ([Cap. 03 playbook agentic](/sbd-toe/sbd-manual/threat-modeling/addon/metodologias-e-ferramentas#playbook-agentic), [Cap. 04 `ARC-014`/`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015), [Cap. 10 §C5](/sbd-toe/sbd-manual/testes-seguranca/addon/ia-nos-testes#c5-eval-suites), [Cap. 12 + `OPS-011..014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle)) — serve simultaneamente o Art. 15 do AI Act e o Anexo I (Partes I e II) do CRA.
2. **Processo único de tratamento de vulnerabilidades** ([Cap. 05 `DEP-011..014`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-011), [Cap. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro), [Policy 39 §7](/sbd-toe/assets/policies/policy-ai-bom-supply-chain)) conforme o Anexo I (Parte II) do CRA — cobre também a robustez exigida pelo Art. 15, incluindo a resposta a incidentes *upstream* em supply chain AI (`AML.T0019`, `AML.T0109`, `AML.T0110`).
3. **SBOM + AI BOM único** ([Cap. 05 `DEP-012`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-012) em formato CycloneDX 1.6 *ml-bom*, [Policy 39](/sbd-toe/assets/policies/policy-ai-bom-supply-chain)) a alimentar ambos os regulamentos — satisfaz CRA Anexo I Parte II(1) (SBOM) **e** AI Act Art. 10 (dados/proveniência) **e** Art. 11/Anexo IV (lista de componentes).
4. **Declaração UE de conformidade** que demonstra o nível de cibersegurança do Art. 15, acionando a presunção do Art. 12 do CRA. Cláusulas contratuais com *providers* AI (Cap. 14 US-21 + Policy 33 §10) declaram conformidade Art. 53/55 quando GPAI.
5. **Avaliação de conformidade única** pelo organismo notificado AI Act (Art. 43), estendida ao Anexo I do CRA.
6. **Matriz de origem regulatória** — no catálogo do [Cap. 02](/sbd-toe/sbd-manual/requisitos-seguranca/intro), coluna `Fonte` com enum `AI Act`, `CRA`, `Ambos`, `Outras`.
7. ⚡ **Camada agentic transversal** — [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015) (agente como *principal*), `REQ-AGN-001..004` (mandate, *kill-switch*, *intent*), `OPS-012..014` (audit per *tool*, *budget*, *jailbreak detection*) e Policy 38 (*mandates lifecycle*) fornecem controlos técnicos relevantes para o Art. 14, o Art. 15 e o Art. 26 do AI Act e para o Anexo I (Partes I e II) do CRA (*cybersec by design*). Estes controlos são **evidência técnica, não uma declaração de conformidade**: o **CRA (Art. 12) estabelece** uma presunção de conformidade **apenas com o Art. 15** do AI Act (cibersegurança) quando o Anexo I é cumprido e demonstrado na declaração UE de conformidade. O Art. 14 (supervisão humana) e o Art. 26 (deployer) **não** estão abrangidos por essa presunção — mantêm-se como obrigações próprias.

## Checklist de Convergência (SIM = pronto)

- [ ] Evidência de cibersegurança mapeada simultaneamente ao Art. 15 (AI Act) e ao Anexo I, Partes I e II (CRA) — incluindo [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015) e *eval suites* (Cap. 10 §C5).
- [ ] Processo de *vulnerability handling* conforme o Anexo I, Parte II (CRA) documentado, com extensão para *upstream* AI supply chain (Policy 39 §7).
- [ ] Declaração UE de conformidade demonstra o nível de cibersegurança do Art. 15 (CRA Art. 12).
- [ ] Avaliação de conformidade única (Art. 43 AI Act) acordada com o organismo notificado.
- [ ] SBOM + AI BOM único (CycloneDX 1.6 `ml-bom` para a parte AI) cobre ambos os regulamentos.
- [ ] Circuitos de reporte distintos (AI Act Art. 73 / CRA Art. 14) com base de deteção técnica partilhada ([`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014) + Policy 30 §9.3).
- [ ] Catálogo do Cap. 02 com coluna `Fonte` preenchida (AI Act / CRA / Ambos).
- [ ] *Mandates* (Policy 38) declaram simultaneamente nível A0–A4 (AI Act Art. 14) e *cybersec measures* (CRA Anexo I Parte I).
- [ ] Não existem processos paralelos divergentes de cibersegurança.

## Perguntas Frequentes

**Q1. Preciso de fazer duas avaliações de conformidade de cibersegurança?**
Não. O CRA Art. 12, conjugado com o Art. 43 do AI Act, permite uma avaliação única - o mesmo organismo notificado pode controlar ambos.

**Q2. O CRA substitui o Art. 15 do AI Act?**
Não substitui. Cria uma **presunção de conformidade** com o Art. 15 quando cumpres o Anexo I (Partes I e II) e o demonstras na declaração. As restantes obrigações de alto risco do AI Act mantêm-se.

**Q3. E o tratamento de vulnerabilidades?**
Implementa o do CRA (Anexo I, Parte II) - é o mais detalhado e, por construção, satisfaz a robustez/cibersegurança esperada pelo Art. 15.

**Q4. Os reportes são os mesmos?**
Não. O AI Act (Art. 73, incidentes graves) e o CRA (Art. 14, vulnerabilidades ativamente exploradas/incidentes graves a ENISA) têm gatilhos, prazos e circuitos distintos. Partilham a **deteção técnica** ([Cap. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)); a submissão é parametrizada por regulamento.

## Referências

- Regulamento (UE) 2024/1689 (AI Act) - Art. 6, 15, 43.
- Regulamento (UE) 2024/2847 (CRA) - Art. 12, Art. 14, Anexo I (Partes I e II), Anexos III/IV.
- [Cross-check AI Act](/sbd-toe/cross-check-normativo/ai-act/intro) e [Cross-check CRA](/sbd-toe/cross-check-normativo/cra/intro) (deste capítulo).
- SbD-ToE Manual ([Cap. 01](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro)–[Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro)).

## Nota Final

O SbD-ToE já abstrai os controlos técnicos de cibersegurança. A convergência AI Act/CRA concretiza-se ao **usar a mesma evidência técnica para ambos** e ao acionar a presunção do Art. 12 do CRA: **uma avaliação, uma declaração, dois regulamentos satisfeitos no eixo cibersegurança** - sem redundância, mantendo as obrigações próprias de cada regime.
