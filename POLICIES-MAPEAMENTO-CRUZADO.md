---
id: policies-mapeamento-cruzado
title: Mapeamento Cruzado - Políticas vs Capítulos
description: Análise de políticas mencionadas nos capítulos vs políticas criadas, com identificação de faltas e links
tags: [governança, políticas, mapeamento, asset-inventory]
---

# 📊 Mapeamento Cruzado: Políticas nos Capítulos vs Assets Criados

**Data**: 30 de Março de 2026  
**Status**: Análise Completa  
**Cobertura**: 14 capítulos SbD-ToE + 37 políticas criadas

---

## 📌 Resumo Executivo

| Métrica | Valor | Status |
|---------|-------|--------|
| **Políticas Criadas** | 37 | ✅ Criadas em 020-assets/policies/ |
| **Políticas Mencionadas nos Capítulos** | ~50 | ⚠️ Distribuídas em 14 capítulos |
| **Cobertura** | 74% | Bem coberto, alguns gaps |
| **Políticas Completamente Faltando** | 8–10 | ❌ Ação Requerida |
| **Políticas Parcialmente Cobertas** | ~20 | ⚠️ Consolidadas em "políticas umbrella" |
| **Políticas Órfãs** | 1 | ⚠️ DAST&Fuzzing (não mencionada em nenhum capítulo) |
| **Links nos política-relevantes.md** | 0 | ❌ **CRÍTICO**: Nenhum link hiperativo! |

---

## 🔴 CRÍTICO - Hiperlinks Ausentes

**Problema**: Os ficheiros `policies-relevantes.md` em cada capítulo **mencionam políticas mas NÃO linkam para 020-assets/policies/**.

**Impacto**: 
- Utilizadores não conseguem navegar das políticas recomendadas para o conteúdo real
- Políticas cridas "invisíveis" no portal

**Necessário**: Atualizar 14 ficheiros `**/politicas-relevantes.md` para incluir links como:

```markdown
| [Política de Classificação de Risco Aplicacional](/sbd-toe/assets/policies/02_policy-classificacao-risco) | ✅ Sim | ... |
```

---

## 📋 CAPITULO 1: Classificação de Aplicações

### Políticas Mencionadas na Tabela
| Nome | Obrigatória? | Ficheiro Esperado | Status | Ação |
|------|--------------|------------------|--------|------|
| Política de Classificação de Risco Aplicacional | ✅ Sim | 02_policy-classificacao-risco.md | ✅ **CRIADA** | Adicionar link em 01-classificacao-aplicacoes/policies-relevantes.md |
| Política de Aceitação de Risco Residual | ✅ Sim | 03_policy-aceitacao-risco.md | ✅ **CRIADA** | Adicionar link |
| Política de Revisão Periódica de Risco | ✅ Sim | 04_policy-revisao-periodica-risco.md | ✅ **CRIADA** | Adicionar link |
| Política de Rastreabilidade de Decisões de Segurança | ⚠️ Opcional | 06_policy-rastreabilidade.md | ✅ **CRIADA** | Adicionar link |

**Ação**: Adicionar 4 links no ficheiro `01-classificacao-aplicacoes/policies-relevantes.md`

---

## 📋 CAPÍTULO 2: Requisitos de Segurança

### Políticas Mencionadas
| Nome | Obrigatória? | Status | Observação |
|------|--------------|--------|-----------|
| Política de Requisitos de Segurança | ✅ Sim | ✅ **CRIADA** (07_policy-requisitos-seguranca.md) | Adicionar link |
| **Política de Integração de Requisitos no Backlog** | ✅ Sim | ❌ **FALTA** | **Ação Requerida**: Criar ficheiro |
| **Política de Validação de Requisitos em Pipelines** | ✅ Sim | ❌ **FALTA** | **Ação Requerida**: Criar ficheiro |

**Ação**: 
- ✅ Adicionar 1 link para 07_policy-requisitos-seguranca.md
- ❌ Criar 2 policies faltando

---

## 📋 CAPÍTULO 3: Threat Modeling

### Políticas Mencionadas
| Nome | Status | Ficheiro |
|------|--------|----------|
| Política de Threat Modeling | ✅ **CRIADA** | 08_policy-threat-modeling.md |
| **Política de Validação de Modelos de Ameaça** | ❌ **FALTA** | (não existe) |
| **Política de Reutilização de Modelos de Ameaça** | ❌ **FALTA** | (não existe) |

**Ação**:
- ✅ Adicionar link para 08_policy-threat-modeling.md
- ❌ Criar 2 policies técnicas específicas de TM

---

## 📋 CAPÍTULO 4: Arquitetura Segura

### Políticas Mencionadas
| Nome | Status |
|------|--------|
| Política de Arquitetura Segura | ✅ **CRIADA** (09_policy-arquitetura-segura.md) |
| **Política de Aprovação Técnica de Design** | ⚠️ **PARCIALMENTE COBERTA** (em 09) |
| **Política de Documentação e Versionamento Arquitetural** | ⚠️ **PARCIALMENTE COBERTA** (em 09) |

**Ação**: Adicionar link para 09_policy-arquitetura-segura.md e documentar consolidação

---

## 📋 CAPÍTULO 5: Dependências (SBOM/SCA)

### Políticas Mencionadas
| Nome | Status |
|------|--------|
| Política de Dependências | ✅ **CRIADA** (10_policy-dependencias.md) |
| Política de SBOM | ✅ **CRIADA** (11_policy-sbom.md) |
| Política de Exceções CVE | ✅ **CRIADA** (12_policy-excecoes-cve.md) |
| Política de Atualizações Automáticas | ✅ **CRIADA** (13_policy-atualizacao-automatica.md) |
| **Política de Avaliação de Vulnerabilidades (SCA específico)** | ❌ **FALTA** | Distinta de "Exceções CVE" |
| **Política de Repositórios e Registos de Origem** | ⚠️ **PARCIAL** (em 10) |

**Ação**:
- ✅ Adicionar 4 links existentes
- ❌ Criar 1 policy específica de SCA

---

## 📋 CAPÍTULO 6: Desenvolvimento Seguro

### Políticas Mencionadas
| Nome | Status |
|------|--------|
| Política de Guidelines de Desenvolvimento | ✅ **CRIADA** (14_policy-guidelines-desenvolvimento.md) |
| Política de Revisão de Código | ✅ **CRIADA** (15_policy-revisao-codigo.md) |
| Política de Uso de Ferramentas de Apoio (GenAI) | ⚠️ **CRIADA** (16_policy-uso-ferramentas-apoio.md) — mas escopo ambíguo |
| **Política de Justificação de Exceções Técnicas** | ⚠️ **PARCIAL** (em 05_policy-gestao-excecoes.md) |

**Ação**:
- ✅ Adicionar 3 links
- ⚠️ Clarificar se 16_policy-uso-ferramentas-apoio.md cobre GenAI explicitamente

---

## 📋 CAPÍTULO 7: CI/CD Seguro

### Políticas Mencionadas
| Nome | Status |
|------|--------|
| Política de CI/CD Seguro | ✅ **CRIADA** (17_policy-cicd-seguro.md) |
| Política de Gestão de Segredos | ✅ **CRIADA** (18_policy-gestao-segredos.md) |
| **Política de Aplicação Proporcional por Risco** | ❌ **FALTA** (regras de risk-based gating explícitas) |
| **Política de Revisão de Pipelines** | ⚠️ **PARCIAL** (em 17) |

**Ação**:
- ✅ Adicionar 2 links
- ❌ Criar 1 policy sobre aplicação proporcional de controles por risco

---

## 📋 CAPÍTULO 8: IaC & Infraestrutura

### Políticas Mencionadas
| Nome | Status |
|------|--------|
| Política de IaC Seguro | ✅ **CRIADA** (21_policy-iac-seguro.md) |
| Política de Aprovação de Plans IaC | ✅ **CRIADA** (22_policy-aprovacao-plan-iac.md) |
| Política de Gestão de Módulos e Reutilização | ⚠️ **PARCIAL** (em 21) |
| **Política de Observabilidade e Auditoria de Alterações** | ⚠️ **PARCIAL** (em 21) |
| Política de Rollback e Recuperação | ✅ **CRIADA** (27_policy-rollback.md) |

**Ação**: Adicionar 4 links; documentar consolidação em 21

---

## 📋 CAPÍTULO 9: Containers e Imagens

### Políticas Mencionadas
| Nome | Status |
|------|--------|
| Política de Containers Seguros | ✅ **CRIADA** (23_policy-containers-seguros.md) |
| Política de Golden Base Images | ✅ **CRIADA** (24_policy-golden-base-images.md) |
| **Política de Gestão de Imagens Obsoletas** | ⚠️ **PARCIAL** (em 23) |
| **Política de Validação de Manifestos de Deploy** | ⚠️ **PARCIAL** (em 23) |
| **Política de Observabilidade de Containers** | ⚠️ **PARCIAL** (em 23) |

**Ação**: Adicionar 2 links; documentar cobertura de 3 sub-políticas em 23

---

## 📋 CAPÍTULO 10: Testes de Segurança

### Políticas Mencionadas
| Nome | Status |
|------|--------|
| Política de Estratégia de Testes | ✅ **CRIADA** (19_policy-estrategia-testes.md) |
| Política de PenTesting | ✅ **CRIADA** (36_policy-pentesting.md) |
| **Cobertura de Testes de Segurança** | ⚠️ **PARCIAL** (em 19) |
| **Integração de Testes com Ciclo de Vida** | ⚠️ **PARCIAL** (em 19) |
| **Revalidação e Obs. de Testes** | ⚠️ **PARCIAL** (em 19) |

**Ação**: Adicionar 2 links; documentar sub-políticas (cobertura, integração, revalidação) em 19

---

## 📋 CAPÍTULO 11: Deploy Seguro

### Políticas Mencionadas
| Nome | Status |
|------|--------|
| Política de Deploy Seguro | ✅ **CRIADA** (25_policy-deploy-seguro.md) |
| Política de Aprovação de Release | ✅ **CRIADA** (26_policy-aprovacao-release.md) |
| Política de Rollback e Recuperação | ✅ **CRIADA** (27_policy-rollback.md) |
| **Política de Gating e Automatismo** | ⚠️ **PARCIAL** (em 25) |
| **Política de Autonomia e Responsabilidade** | ⚠️ **PARCIAL** (em 25) |

**Ação**: Adicionar 3 links; documentar 2 sub-políticas em 25

---

## 📋 CAPÍTULO 12: Monitorização e Operações

### Políticas Mencionadas
| Nome | Status |
|------|--------|
| Política de Logging Estruturado | ✅ **CRIADA** (29_policy-logging-estruturado.md) |
| Política de Monitorização de Segurança | ✅ **CRIADA** (30_policy-monitorizacao-seguranca.md) |
| Política de Gestão de Alertas | ✅ **CRIADA** (31_policy-gestao-alertas.md) |
| Política de Incident Response Playbook | ✅ **CRIADA** (32_policy-irp.md) |
| Política de Monitorização Pós-Deploy | ✅ **CRIADA** (28_policy-monitorizacao-pos-deploy.md) |
| **Observabilidade de Serviços** | ⚠️ **PARCIAL** (em 30) |
| **Cobertura de Agentes e Instrumentação** | ⚠️ **PARCIAL** (em 30) |

**Ação**: Adicionar 5 links; documentar 2 sub-políticas em 30

---

## 📋 CAPÍTULO 13: Formação e Onboarding

### Políticas Mencionadas
| Nome | Status |
|------|--------|
| Política de Formação de Segurança | ✅ **CRIADA** (37_policy-formacao-seguranca.md) |
| **Gestão de Conteúdos Formativos** | ⚠️ **PARCIAL** (em 37) |
| **Indicadores de Formação** | ⚠️ **PARCIAL** (em 35_policy-kpis-governacao.md) |

**Ação**: Adicionar 1 link; documentar consolidação com KPIs

---

## 📋 CAPÍTULO 14: Governança e Contratação

### Políticas Mencionadas
| Nome | Status |
|------|--------|
| Política de Contratação Segura | ✅ **CRIADA** (33_policy-contratacao-segura.md) |
| Política de Rastreabilidade Organizacional | ✅ **CRIADA** (34_policy-rastreabilidade-organizacional.md) |
| Política de KPIs de Governança | ✅ **CRIADA** (35_policy-kpis-governanca.md) |
| Política de Formação para Aprovadores | ⚠️ **PARCIAL** (em 37) |
| **Ciclo de Revisão de Exceções e Contratos** | ⚠️ **PARCIAL** (em 05_policy-gestao-excecoes.md) |

**Ação**: Adicionar 3 links; documentar 2 sub-políticas

---

## 🔴 RESUMO DE AÇÕES REQUERIDAS

### **CRÍTICO** (Bloqueadores)

1. **Adicionar Hiperlinks em 14 ficheiros `policies-relevantes.md`**
   - Impacto: **MÁXIMO** — Torna políticas descobríveis
   - Tempo: ~2 horas
   - Ficheiros afetados:
     ```
     01-classificacao-aplicacoes/policies-relevantes.md
     02-requisitos-seguranca/policies-relevantes.md
     03-threat-modeling/policies-relevantes.md
     04-arquitetura-segura/policies-relevantes.md
     05-dependencias-sbom-sca/policies-relevantes.md
     06-desenvolvimento-seguro/policies-relevantes.md
     07-cicd-seguro/policies-relevantes.md
     08-iac-infraestrutura/policies-relevantes.md
     09-containers-imagens/policies-relevantes.md
     10-testes-seguranca/policies-relevantes.md
     11-deploy-seguro/policies-relevantes.md
     12-monitorizacao-operacoes/policies-relevantes.md
     13-formacao-onboarding/policies-relevantes.md
     14-governanca-contratacao/policies-relevantes.md
     ```

### **ALTO** (Faltas de Conteúdo)

2. **Criar 8–10 Políticas Faltando** (ordem de prioridade)
   - [ ] Integração de Requisitos no Backlog (Cap 2)
   - [ ] Validação de Requisitos em Pipelines (Cap 2)
   - [ ] Validação de Modelos de Ameaça (Cap 3)
   - [ ] Reutilização de Modelos de Ameaça (Cap 3)
   - [ ] Avaliação de Vulnerabilidades SCA (Cap 5)
   - [ ] Aplicação Proporcional de Controles por Risco (Cap 7)
   - [ ] Gestão de Imagens Obsoletas (Cap 9, referência)
   - [ ] Observabilidade e Auditoria de Alterações IaC (Cap 8, clarificação)

   **Tempo estimado**: ~16 horas
   **Prioridade**: Integrar até Q2 2026

### **MÉDIO** (Clarificações)

3. **Documentar Consolidações de Políticas "Umbrella"**
   - Ficheiros como `09_policy-arquitetura-segura.md` cobrem múltiplas sub-políticas
   - Ação: Adicionar secção "Escopo & Subsecções" em cada ficheiro consolidador
   - Exemplo:
     ```markdown
     ## Escopo desta Política
     Esta política consolidada cobre:
     - [ ] Documentação e Versionamento Arquitetural
     - [ ] Aprovação Técnica de Design
     - [ ] Rastreabilidade de Decisões
     ```

4. **Esclarecer Escopo de Políticas Ambíguas**
   - `16_policy-uso-ferramentas-apoio.md` — Covers GenAI? Ferramentas gerais? Ambos?
   - Ação: Revisar e deixar claro no intro

### **BAIXO** (Órfão)

5. **Integrar DAST & Fuzzing (01_policy-dast-fuzzing.md)**
   - Status: Criada mas nunca referenciada
   - Ação: Adicionar referência em Cap 10 (Testes de Segurança) **ou** verificar se é intencionalmente um "asset adicional"

---

## 📊 Tabela de Implementação

| Ação | Prioridade | Tempo (hours) | Ficheiros | Status |
|------|-----------|---------------|-----------|--------|
| Adicionar hyperlinks em 14 policies-relevantes.md | 🔴 CRÍTICO | 2 | 14 | ❌ Não iniciado |
| Criar 8 policies faltando | 🟠 ALTO | 16 | 8 | ❌ Não iniciado |
| Documentar consolidações | 🟡 MÉDIO | 4 | 12 | ❌ Não iniciado |
| Esclarecer ambiguidades | 🟡 MÉDIO | 2 | 1 | ❌ Não iniciado |
| Integrar ou documentar órfão (DAST) | 🟢 BAIXO | 0.5 | 1 | ❌ Não iniciado |
| **Total** | — | **24.5 horas** | **~37** | ❌ **0% completo** |

---

## 📝 Próximas Etapas

1. **Fase 1 (Esta semana)**: Adicionar hyperlinks em 14 ficheiros
2. **Fase 2 (Próxima semana)**: Criar 8 policies faltando
3. **Fase 3 (2 semanas)**: Validação de links + build web final

---

## 📎 Referências

- **020-assets/**: `/manuals_src/docs/sbd-toe/020-assets/`
- **Policies criadas**: `/manuals_src/docs/sbd-toe/020-assets/policies/`
- **Capítulos**: `/manuals_src/docs/sbd-toe/010-sbd-manual/*/policies-relevantes.md` (14 ficheiros)

**Último Report**: 30 de Março de 2026, 23:45
