---
id: policy-rastreabilidade
title: Política de Rastreabilidade e Auditoria
description: Política organizacional transversal que define os requisitos de rastreabilidade entre requisitos, controlos, evidências de validação, artefactos de build e eventos operacionais, assegurando que a postura de segurança é auditável de forma contínua e proporcional ao nível de risco da aplicação.
tags: [policy, rastreabilidade, auditoria, evidências, logs, WORM, commit, pipeline, release, cap02, cap06, cap07, cap08, cap09, cap12, cap14, L1, L2, L3, governance, transversal]
grupo: governacao
sidebar_position: 6
---

# Política de Rastreabilidade e Auditoria

## 1. Objetivo

Esta política define os requisitos transversais de **rastreabilidade e auditoria** que devem ser satisfeitos ao longo de todo o ciclo de vida de cada aplicação.

Rastreabilidade é a capacidade de reconstituir, a qualquer momento, a cadeia de decisões, evidências e artefactos que suportam a postura de segurança de uma aplicação - desde os requisitos definidos até ao código em produção, passando pelas validações executadas, as exceções aprovadas e os eventos operacionais registados.

Sem rastreabilidade efetiva:

- Auditorias de segurança tornam-se exercícios de reconstrução especulativa
- A investigação de incidentes perde rigor e alcance
- A conformidade regulatória não pode ser demonstrada de forma objetiva
- Decisões de risco ficam sem evidência associada

Esta política é **transversal** - aplica-se a todos os domínios do manual SbD-ToE onde exista produção de evidências, aprovações, artefactos ou eventos auditáveis.

---

## 2. Âmbito

Esta política cobre as seguintes dimensões de rastreabilidade:

| Dimensão | Descrição | Capítulos |
|---|---|---|
| **Requisitos** | Rastreabilidade entre requisitos de segurança, trabalho no backlog e evidências de validação | Cap. 02 |
| **Código e pipeline** | Rastreabilidade commit → build → pipeline → release → deploy | Cap. 07 |
| **Artefactos** | Proveniência e integridade de artefactos de build (SBOM, assinaturas, SCA) | Cap. 05, 07, 09 |
| **Infraestrutura** | Rastreabilidade ficheiro IaC → recurso → ambiente | Cap. 08 |
| **Evidências de validação** | Arquivo de relatórios SAST, DAST, fuzzing, SCA, exceções | Cap. 06, 10 |
| **Eventos operacionais** | Logs estruturados com integridade garantida, correlacionáveis com incidentes | Cap. 12 |
| **Decisões de segurança** | Aprovações, exceções, aceitações de risco, resultados de threat modeling | Cap. 01, 03, 14 |
| **Conformidade regulatória** | Mapeamento entre controlos técnicos e requisitos normativos | Cap. 12, 14 |

---

## 3. Princípios fundamentais

- **Rastreabilidade bidirecional** - deve ser possível navegar do requisito ao código e do código ao requisito
- **Evidência executável** - relatórios produzidos por execução real, nunca por declaração manual sem suporte técnico
- **Imutabilidade** - evidências de auditoria não devem ser alteráveis após produção; armazenamento WORM recomendado em L2/L3
- **Correlação** - eventos de fontes distintas (commit, pipeline, log, incidente) devem ser correlacionáveis por identificadores comuns
- **Proporcionalidade** - o nível de detalhe e formalismo escala com o nível de criticidade da aplicação

---

## 4. Rastreabilidade de requisitos (Cap. 02)

### 4.1 Requisitos por nível

| Prática | L1 | L2 | L3 |
|---|---|---|---|
| Requisitos de segurança no backlog com tags | Recomendado | Obrigatório | Obrigatório |
| Referência cruzada requisito → validação | Recomendado | Obrigatório | Obrigatório |
| Relatório de rastreabilidade exportável | Opcional | Recomendado | Obrigatório |
| Revisão independente de rastreabilidade | Não aplicável | Recomendado | Obrigatório |

### 4.2 Requisitos mínimos

- [ ] Todos os requisitos de segurança aplicáveis identificados com taxonomia rastreável (ex: `SEC-L2-AUT-001`)
- [ ] Cada requisito ligado a pelo menos um item de backlog, PR ou tarefa técnica
- [ ] Evidência de validação (teste, revisão, relatório) associada a cada requisito aplicado
- [ ] Exceções a requisitos registadas formalmente com referência ao requisito excecionado

---

## 5. Rastreabilidade de código e pipeline (Cap. 07)

### 5.1 Cadeia obrigatória

A rastreabilidade deve cobrir a cadeia completa:

```
commit SHA → execução de pipeline → artefacto produzido → release tag → deployment
```

### 5.2 Requisitos por nível

| Elemento | L1 | L2 | L3 |
|---|---|---|---|
| Commit SHA associado ao artefacto | Recomendado | Obrigatório | Obrigatório |
| Logs de pipeline retidos | Básico | Obrigatório (90 dias) | Obrigatório (1 ano) |
| Resultados de scanners correlacionados com commit | Opcional | Obrigatório | Obrigatório |
| Export imutável de logs de pipeline | Não aplicável | Recomendado | Obrigatório |
| Não-repúdio de promoções irreversíveis | Não aplicável | Recomendado | Obrigatório |

### 5.3 Requisitos mínimos

- [ ] ID de correlação único por execução de pipeline
- [ ] Relatórios de segurança (SAST, DAST, SCA) arquivados como artefactos do pipeline com referência ao commit
- [ ] Logs de pipeline retidos conforme tabela acima
- [ ] Promoções a produção associadas a aprovação humana rastreável (nome, timestamp, contexto)

---

## 6. Rastreabilidade de artefactos (Cap. 05, 07, 09)

### 6.1 Requisitos por nível

| Elemento | L1 | L2 | L3 |
|---|---|---|---|
| SBOM gerado por build | Recomendado | Obrigatório | Obrigatório |
| Assinatura de artefacto | Não aplicável | Obrigatório | Obrigatório |
| Proveniência registada (who/when/how) | Não aplicável | Obrigatório | Obrigatório |
| Verificação de assinatura no deploy | Não aplicável | Obrigatório | Obrigatório |
| Digest-only para imagens de container | Recomendado | Obrigatório | Obrigatório |

### 6.2 Requisitos mínimos

- [ ] SBOM em formato CycloneDX ou SPDX, gerado automaticamente por build e arquivado
- [ ] Artefactos de release assinados com chave gerida e rotacionada periodicamente
- [ ] Metadados de proveniência (quem construiu, quando, a partir de que commit) associados ao artefacto

---

## 7. Rastreabilidade de infraestrutura (Cap. 08)

### 7.1 Requisitos mínimos

- [ ] Cada ficheiro IaC rastreável ao recurso que provisiona e ao ambiente em que foi aplicado
- [ ] Histórico de `plan` e `apply` retido e auditável
- [ ] Alterações de infraestrutura associadas a PR com revisão documentada
- [ ] Drift detetado e registado com referência ao estado esperado

---

## 8. Arquivo de evidências de validação (Cap. 06, 10)

### 8.1 Requisitos por nível

| Evidência | L1 | L2 | L3 |
|---|---|---|---|
| Relatórios SAST arquivados | Recomendado | Obrigatório | Obrigatório |
| Relatórios DAST arquivados | Opcional | Obrigatório | Obrigatório |
| Relatórios SCA arquivados | Recomendado | Obrigatório | Obrigatório |
| Relatórios de fuzzing arquivados | Opcional | Obrigatório | Obrigatório |
| Armazenamento WORM ou equivalente | Não aplicável | Recomendado | Obrigatório |
| Índice de evidências por aplicação/release | Opcional | Recomendado | Obrigatório |

### 8.2 Requisitos mínimos

- [ ] Repositório de evidências definido, com controlo de acesso adequado
- [ ] Export automático por build/release para o repositório de evidências
- [ ] Evidências retidas conforme prazos de retenção definidos (ver secção 10)
- [ ] Evidências não alteráveis após arquivo (WORM ou equivalente em L2/L3)

---

## 9. Rastreabilidade de eventos operacionais (Cap. 12)

### 9.1 Requisitos mínimos

- [ ] Logs em formato estruturado (JSON ou equivalente) com campos mínimos: timestamp, nível, evento, origem, contexto
- [ ] Identificador de correlação (`request_id` ou equivalente) propagado em todos os logs do mesmo fluxo
- [ ] Logs enviados para sistema centralizado (L2/L3)
- [ ] Acesso a logs restrito e auditado - sem acesso direto por funções de produção
- [ ] Integridade de logs verificável (hash ou assinatura) em L2/L3
- [ ] Retenção WORM ativada no armazenamento em L3

---

## 10. Prazos de retenção mínimos

| Tipo de evidência | L1 | L2 | L3 |
|---|---|---|---|
| Logs de aplicação | 30 dias | 90 dias | 1 ano |
| Logs de pipeline CI/CD | 30 dias | 90 dias | 1 ano |
| Relatórios de segurança (SAST/DAST/SCA) | 30 dias | 90 dias | 1 ano |
| Artefactos de build e SBOM | Por release | 1 ano | 2 anos |
| Registos de aprovações e exceções | 1 ano | 2 anos | 3 anos |
| Registos de classificação e reavaliação | 2 anos | 3 anos | 5 anos |

:::note
Em contextos regulados (RGPD, DORA, NIS2, saúde, financeiro), os prazos de retenção podem ser superiores aos definidos nesta tabela. Prevalecem sempre os requisitos regulatórios aplicáveis.
:::

---

## 11. Rastreabilidade de decisões de segurança

As seguintes decisões devem ser sempre registadas com rastreabilidade completa:

| Decisão | Elementos mínimos do registo |
|---|---|
| Aprovação de exceção | Quem aprovou, quando, para que controlo, com que prazo |
| Aceitação de risco residual | Quem aprovou, severidade, mitigação, TTL |
| Override de gate de pipeline | Quem autorizou, contexto, timestamp |
| Alteração de nível de classificação | Quem decidiu, justificação, data |
| Aprovação de release | Quem aprovou, checklist executada, findings em aberto |
| Resultado de threat modeling | Ameaças identificadas, decisões de mitigação ou aceitação, aprovação |

---

## 12. Responsabilidades

| Role | Responsabilidade |
|---|---|
| Developer / Tech Lead | Garantir tags de rastreabilidade no backlog e PRs; produzir evidências de validação |
| DevOps / SRE | Configurar arquivo automático de artefactos e logs; garantir retenção e imutabilidade |
| AppSec Engineer | Verificar completude da rastreabilidade em revisões de segurança e auditorias |
| GRC / Compliance | Manter o índice centralizado de evidências; emitir relatórios de conformidade |
| CISO | Supervisionar o programa de rastreabilidade; garantir alinhamento com requisitos regulatórios |

---

## 13. Revisão e auditoria desta política

Esta política deve ser **revista anualmente** ou após qualquer um dos seguintes eventos:

- Incidente em que a ausência de rastreabilidade dificultou a investigação
- Alteração regulatória com impacto nos prazos de retenção ou requisitos de evidência
- Alteração significativa da arquitetura de pipeline ou de logging

O índice de evidências e os logs de auditoria devem ser disponibilizados integralmente em auditorias internas e externas.

---

## 14. Referências normativas e técnicas

| Referência | Relevância |
|---|---|
| SbD-ToE Cap. 02 - Requisitos de Segurança | Rastreabilidade requisito → controlo → validação |
| SbD-ToE Cap. 06 - Desenvolvimento Seguro | Arquivo central de evidências de validação |
| SbD-ToE Cap. 07 - CI/CD Seguro | Rastreabilidade commit → pipeline → release |
| SbD-ToE Cap. 08 - IaC e Infraestrutura | Rastreabilidade ficheiro → recurso → ambiente |
| SbD-ToE Cap. 09 - Containers e Imagens | Proveniência e assinatura de imagens |
| SbD-ToE Cap. 12 - Monitorização e Operações | Integridade e retenção de logs |
| SbD-ToE Cap. 14 - Governança e Contratação | Rastreabilidade organizacional e conformidade |
| ISO/IEC 27001 - Cláusula 9.1 | Monitorização, medição, análise e avaliação |
| NIST SP 800-92 | Guide to Computer Security Log Management |
| SSDF PW.8 | Archive and protect each software release |
| NIS2 - Artigo 21 | Obrigações de registo e notificação |
| DORA - Artigo 10 | Rastreabilidade de eventos e logs |
