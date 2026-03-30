---
id: policy-kpis-governacao
title: Política de KPIs de Governação de Segurança
description: Política organizacional que define os requisitos para a definição, recolha, análise e reporte de KPIs de governação de segurança, incluindo categorias de métricas, cadência de reporting, responsabilidades, thresholds de intervenção e integração com frameworks de maturidade (SAMM, SSDF), proporcional ao nível de criticidade (L1, L2, L3).
tags: [policy, KPIs, governação, métricas, maturidade, SAMM, SSDF, reporting, dashboard, cap14, L1, L2, L3, governance, CISO, GRC]
grupo: governacao
sidebar_position: 35
---

# Política de KPIs de Governação de Segurança

## 1. Objetivo

Esta política define os requisitos para a **definição, recolha, análise e reporte de indicadores-chave de desempenho (KPIs) do programa de governação de segurança** da organização.

Um programa de segurança sem métricas é um programa sem feedback loop - não é possível determinar se está a funcionar, se está a melhorar ou se os recursos estão a ser aplicados nos problemas certos. KPIs de governação de segurança transformam actividade técnica em evidência de desempenho: permitem à gestão executiva tomar decisões estratégicas fundamentadas, identificar desvios sistémicos antes de se tornarem incidentes, e demonstrar maturidade a reguladores e auditores. Métricas mal definidas ou recolhidas sem rigor são tão prejudiciais quanto a ausência de métricas - criam confiança falsa e desviam atenção dos riscos reais.

O objetivo desta política é garantir que:

- O programa de segurança tem um conjunto de KPIs definidos, com fontes, responsáveis e cadência de recolha estabelecidos
- Os KPIs cobrem as dimensões relevantes de governação: conformidade, operações, incidentes, fornecedores e maturidade
- O reporting é realizado com cadência proporcional ao nível de risco e distribuído aos destinatários correctos
- Desvios de KPIs críticos originam acções correctivas com owner e prazo
- O nível de maturidade do programa é avaliado periodicamente com referência a frameworks reconhecidos

---

## 2. Âmbito e obrigatoriedade

| Nível | Obrigatoriedade |
|---|---|
| L1 | Básico; KPIs mínimos de conformidade; reporte anual à gestão |
| L2 | Obrigatório; conjunto de KPIs definido; dashboard recomendado; reporte semestral |
| L3 | Obrigatório; KPIs completos; dashboard configurado; alertas automáticos; reporte trimestral à gestão executiva |

---

## 3. Categorias de KPIs

Os KPIs de governação de segurança devem cobrir as seguintes categorias:

### 3.1 Conformidade e rastreabilidade

| KPI | Descrição | Target |
|---|---|---|
| % de aplicações com repositório de conformidade actualizado | Aplicações com repositório válido (última revisão dentro do período) | > 90% |
| % de aplicações L2/L3 com Security Champion designado | Aplicações com owner formal e formação concluída | 100% |
| % de capítulos SbD-ToE com conformidade verificada por aplicação | Cobertura média dos capítulos aplicáveis | > 80% |
| % de excepções activas dentro do TTL | Excepções não expiradas como proporção do total activo | > 95% |
| % de excepções resolvidas dentro do prazo | Excepções com remediação concluída no prazo aprovado | > 70% |

### 3.2 Qualidade e velocidade de remediação

| KPI | Descrição | Target |
|---|---|---|
| MTTR por severidade | Tempo médio entre identificação e remediação de findings | Critical ≤ 7 dias; High ≤ 30 dias |
| Taxa de reincidência de findings | % de findings do mesmo tipo que reaparecem dentro de 90 dias | &lt; 10% |
| % de findings Critical/High remediados no SLA | Conformidade com SLAs definidos na política de testes | > 90% |
| Taxa de exceções activas vs. findings totais | Indicador de acumulação de risco aceite | Trend descendente |

### 3.3 Operações e resposta a incidentes

| KPI | Descrição | Target |
|---|---|---|
| % de alertas P1/P2 respondidos dentro do SLA | Conformidade com SLAs da política de gestão de alertas | > 95% |
| Taxa de verdadeiros positivos (alertas P1/P2) | % de alertas P1/P2 que correspondem a incidentes reais | > 70% |
| Número de incidentes de segurança por período | Tendência de ocorrências | Trend descendente ou estável |
| Tempo médio de detecção (MTTD) | Tempo entre início do incidente e detecção | Referência interna por tipo |
| Tempo médio de resolução (MTTR de incidentes) | Tempo entre detecção e resolução de incidentes | Referência interna por severidade |
| % de incidentes com post-mortem realizado no prazo | Post-mortems concluídos em ≤ 5 dias úteis após resolução | 100% para P1; > 80% para P2 |

### 3.4 Pipeline e desenvolvimento

| KPI | Descrição | Target |
|---|---|---|
| % de pipelines com gates de segurança activos | Proporção de pipelines com SAST, SCA e secrets scanning | > 95% em L2/L3 |
| Taxa de bloqueio de pipeline por segurança | % de execuções bloqueadas por gate de segurança | Referência interna; trend descendente desejável |
| % de artefactos com SBOM gerado e assinado | Cobertura de geração de SBOM | 100% em L3 |
| % de segredos em vault vs. hardcoded detetados | Proporção de segredos geridos correctamente | Hardcoded = 0 |

### 3.5 Fornecedores e terceiros

| KPI | Descrição | Target |
|---|---|---|
| % de fornecedores activos com due diligence actualizada | Fornecedores dentro do ciclo de reavaliação | 100% |
| % de contratos com cláusulas de segurança conformes | Contratos que incluem cláusulas mínimas obrigatórias | 100% em L2/L3 |
| % de contractors com onboarding técnico concluído | Contractors activos com trilho formativo e quiz validados | 100% |
| SLA de notificação de incidentes por fornecedores | Taxa de cumprimento do prazo contratual de notificação | > 90% |

### 3.6 Formação e capacitação

| KPI | Descrição | Target |
|---|---|---|
| Taxa de conclusão de formação obrigatória | % de colaboradores com trilho formativo concluído | > 90% |
| Taxa de aprovação em quiz de formação | % de participantes com nota ≥ 80% | > 85% |
| % de Security Champions com formação actualizada | Champions com formação válida e não expirada | 100% |

---

## 4. Fontes de dados e recolha

| Categoria | Fontes primárias | Responsável pela recolha |
|---|---|---|
| Conformidade e rastreabilidade | Repositórios de conformidade; ferramenta GRC; registos de owners | GRC / AppSec |
| Remediação | DefectDojo ou plataforma centralizada de findings; tickets | AppSec / DevOps |
| Operações e incidentes | SIEM; plataforma de on-call (PagerDuty/OpsGenie); registos de IRP | SOC / GRC |
| Pipeline e desenvolvimento | Plataforma CI/CD; registos de pipeline; artefactos assinados | DevOps / AppSec |
| Fornecedores | Registos de contratos; resultados de due diligence; onboarding | GRC / Procurement |
| Formação | LMS; registos de conclusão; quiz scores | GRC / RH |

---

## 5. Cadência de recolha e reporte

| Actividade | L1 | L2 | L3 |
|---|---|---|---|
| Recolha automática de métricas | Não aplicável | Recomendado (mensal) | Obrigatório (contínuo + mensal consolidado) |
| Dashboard actualizado | Não aplicável | Mensal | Contínuo |
| Relatório para Tech Lead / AppSec | Não aplicável | Mensal | Mensal |
| Relatório para CISO / Gestão Executiva | Anual | Semestral | Trimestral |
| Relatório para Auditoria | Anual | Anual | Semestral (ou sob solicitação) |

---

## 6. Thresholds de intervenção

Determinados desvios nos KPIs devem activar acções correctivas imediatas, independentemente do ciclo de reporting regular:

| Condição | Acção |
|---|---|
| % de alertas P1 respondidos dentro do SLA &lt; 80% | Revisão imediata do processo de on-call e escalonamento |
| Taxa de reincidência de findings > 25% | Revisão do processo de remediação e das guidelines de desenvolvimento |
| % de excepções expiradas sem reavaliação > 10% | Auditoria de excepções; escalamento para decisores |
| Contractor activo sem onboarding concluído | Bloqueio de acesso até conclusão do onboarding |
| Fornecedor activo com due diligence expirada em L3 | Revisão imediata; suspensão de novos acessos até reavaliação |
| MTTD de incidente P1 > 24 horas | Revisão de regras de detecção e cobertura de monitorização |

---

## 7. Avaliação de maturidade

Além dos KPIs operacionais, a organização deve avaliar periodicamente o nível de maturidade do programa de segurança com referência a frameworks reconhecidos:

| Framework | Dimensões avaliadas | Cadência |
|---|---|---|
| OWASP SAMM | Governance, Design, Implementation, Verification, Operations | Anual |
| NIST SSDF | Prepare, Protect, Produce, Respond | Anual |
| BSIMM (opcional) | Benchmark com indústria | Cada 2 anos |

O resultado da avaliação de maturidade deve:

- Ser documentado e comparado com a avaliação anterior (evolução)
- Identificar as dimensões com maior gap face ao target de maturidade da organização
- Originar um plano de melhoria com prioridades, owners e prazos
- Ser apresentado à gestão executiva como parte do relatório anual de segurança

:::note
A avaliação de maturidade não substitui os KPIs operacionais - são perspectivas complementares. Os KPIs medem desempenho corrente; a avaliação de maturidade mede a capacidade instalada para manter esse desempenho ao longo do tempo.
:::

---

## 8. Formato e distribuição de relatórios

| Tipo de relatório | Destinatários | Conteúdo mínimo |
|---|---|---|
| Relatório mensal operacional | AppSec, Tech Leads, DevOps | Estado de KPIs operacionais; desvios; acções em curso |
| Relatório trimestral / semestral | CISO, Gestão Executiva | Visão agregada do portfólio; tendências; KPIs estratégicos; plano de acção |
| Relatório para auditoria | Auditores internos / externos | Estado de conformidade por capítulo; evidências; excepções activas; histórico |
| Dashboard contínuo | AppSec, GRC, CISO | Estado em tempo real de KPIs operacionais críticos; alertas activos |

---

## 9. Responsabilidades

| Role | Responsabilidade |
|---|---|
| GRC / Compliance | Definir e manter o conjunto de KPIs; coordenar recolha de dados; produzir relatórios; gerir alertas de threshold |
| AppSec Engineer | Fornecer dados de findings, pipeline e conformidade técnica; validar qualidade das métricas; apoiar avaliação de maturidade |
| DevOps / SRE | Fornecer dados de pipeline, alertas e operações; configurar automação de recolha |
| Security Champion | Fornecer dados de conformidade da aplicação; actualizar repositório de conformidade |
| CISO / Gestão Executiva | Analisar relatórios; aprovar targets de KPIs; tomar decisões estratégicas com base em dados; garantir recursos para acções correctivas |

---

## 10. Revisão e auditoria desta política

Esta política deve ser **revista anualmente** ou após qualquer um dos seguintes eventos:

- Alteração significativa do programa de segurança que torne os KPIs actuais inadequados
- Resultado de avaliação de maturidade que identifique lacunas nos KPIs definidos
- Alteração regulatória que imponha novos requisitos de medição ou reporte

---

## 11. Referências normativas e técnicas

| Referência | Relevância |
|---|---|
| SbD-ToE Cap. 14 - Governança & Contratação | US-05: KPIs de governação; US-11: consolidação de KPIs e maturidade |
| Política de Rastreabilidade Organizacional (`34_policy-rastreabilidade-organizacional.md`) | Fonte de dados para KPIs de conformidade |
| Política de Gestão de Alertas (`31_policy-gestao-alertas.md`) | KPIs de qualidade de alertas e SLAs |
| Política de IRP (`32_policy-irp.md`) | KPIs de resposta a incidentes (MTTD, MTTR) |
| OWASP SAMM v2 | Software Assurance Maturity Model - framework de maturidade |
| NIST SSDF (SP 800-218) | Secure Software Development Framework - práticas e maturidade |
| BSIMM | Building Security In Maturity Model - benchmark de indústria |
| ISO/IEC 27001 - A.18 | Compliance; security reviews and audits |
| DORA - Art. 6, 17 | ICT risk management and reporting requirements |
| NIS2 - Art. 21 | Security measures and governance obligations |
