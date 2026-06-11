---
id: checklist-revisao
title: Checklist - Formação e Onboarding Seguro
sidebar_label: Checklist de Revisão
description: Lista de verificação binária e rastreável da adoção das práticas do Capítulo 13.
tags: [checklist, formacao, onboarding, controlo, validacao, auditoria]
sidebar_position: 20
---


# Checklist de Revisão Periódica - Formação e Onboarding Seguro

Este checklist aplica-se a todos os **colaboradores técnicos, internos ou externos**, com impacto direto no desenvolvimento, operação ou manutenção de software.
Permite avaliar de forma **binária, objetiva e rastreável** a adoção prática das prescrições do **Capítulo 13 - Formação e Onboarding Seguro** (`TRN-001` a `TRN-009`).

> 🛠️ Este mecanismo de controlo é essencial para validar a **formação proporcional ao risco**, a **validação técnica antes de permissões**, a **gestão de terceiros** e a **existência de cultura ativa de segurança**.

---

## 📋 Itens de Verificação

| Item                                                                                                              | Verificado? |
|-------------------------------------------------------------------------------------------------------------------|-------------|
| Existem trilhos formativos definidos por perfil funcional e nível de criticidade (L1–L3), com módulos obrigatórios, duração e periodicidade? (`TRN-001`) | ☐           |
| O trilho é atribuído ao colaborador antes do início de atividade técnica autónoma? (`TRN-002`)                    | ☐           |
| O onboarding de segurança (políticas, manuseamento de segredos, processo de incidentes, controlos do papel) é concluído antes de trabalho autónomo? (`TRN-002`) | ☐           |
| Existe validação objetiva da conclusão com limiar mínimo definido e caminho de remediação para resultados abaixo? (`TRN-003`) | ☐           |
| O resultado da validação é rastreável ao colaborador e à versão do conteúdo, arquivado em repositório institucional? (`TRN-003`) | ☐           |
| O acesso a repositórios, pipelines ou ambientes L2+ está condicionado a evidência de onboarding válido? (`TRN-004`) | ☐           |
| Existe formação contínua diferenciada por nível (L2 ≥ semestral, L3 ≥ trimestral), com participação registada? (`TRN-005`) | ☐           |
| O conteúdo formativo está sob controlo de versão e é revisto após triggers (incidentes, alterações de política, novas classes de vulnerabilidade)? (`TRN-006`) | ☐           |
| Existe processo de onboarding equivalente para terceiros, com termo de responsabilidade e registo (nome, entidade, data, validador)? (`TRN-007`) | ☐           |
| Existe programa formal de Security Champions em equipas L3 (papel documentado, tempo alocado, designação rastreável)? (`TRN-008`) | ☐           |
| Existem KPIs de eficácia formativa definidos e recolhidos, com desvios a gerar ação corretiva (owner e prazo)? (`TRN-009`) | ☐           |
| Existe mecanismo ativo de reforço prático (PR clinics, war rooms, CTFs ou labs) e repositório de boas práticas de PR? | ☐           |
| Existe formação obrigatória em uso seguro de IA e tooling (quando confiar vs. validar outputs, guardrails, validação de código e testes gerados)? | ☐           |
| As equipas têm acesso ao manual de formação por capítulo do SbD-ToE e a um canal formal de apoio (SPOC/Champion) durante o onboarding? | ☐           |
| Existe ambiente sandbox isolado para prática de contractors antes do acesso a sistemas reais? | ☐           |
| Os incidentes com causa-raiz de formação resultam em atualização dos conteúdos formativos? | ☐           |

---

## 🔄 Integração Operacional

- Este checklist pode ser integrado em **fluxos de onboarding, revisões de permissões, PRs iniciais, auditorias internas ou ciclos de segurança trimestrais**.
- A verificação deve ser baseada em **evidência concreta**: quizzes, comentários de PR, registos de LMS ou anexos a tickets.
- Os dados podem ser agregados por projeto, equipa ou fornecedor, alimentando dashboards e relatórios de segurança.

> ⚠️ **Práticas não cumpridas devem ter justificação formal documentada**, aprovada por AppSec, GRC ou gestão técnica (waiver ou exceção temporária).

---

## ✅ Conformidade e KPI

- Este checklist permite declarar **conformidade com as práticas do Capítulo 13** de forma audível e mensurável.
- O número de respostas afirmativas pode ser utilizado como **indicador de maturidade da organização** em segurança baseada em capacitação.
- Os dados gerados devem ser incluídos em **planos de melhoria contínua, auditorias de ciclo de vida e objetivos de qualidade técnica**.

> 📌 Este mecanismo assegura que **a formação é aplicada, validada e rastreada**, sendo uma componente estruturante da segurança organizacional no modelo SbD-ToE.
