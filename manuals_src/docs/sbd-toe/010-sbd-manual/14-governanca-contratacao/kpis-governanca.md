---
id: kpis-governanca
title: KPIs Transversais SbD-ToE - Dashboard de Governação
sidebar_position: 90
description: Seis dimensões transversais de medição da saúde do programa SbD-ToE, agregando indicadores de domínio de todos os capítulos para visibilidade executiva e de gestão de risco.
tags: [kpi, metricas, governanca, transversal, dashboard, executivo, L1, L2, L3]
---

<!--template: sbdtoe-addon -->

# KPIs Transversais SbD-ToE - Dashboard de Governação

Para uma representação visual da arquitectura de medição, ver [`kpis-arquitetura-visao-geral`](./kpis-arquitetura-visao-geral). Para o conjunto curado de indicadores para CISO/direcção/board, ver [`kpis-kri-executivo`](./kpis-kri-executivo). Para avaliar se o modelo está adoptado ("estamos a fazer SbD-ToE?"), ver [`checklist-aderencia-sbd-toe`](./checklist-aderencia-sbd-toe).

---

## Propósito e arquitectura

Este ficheiro define a **estrutura de medição transversal** do programa SbD-ToE em três camadas:

```
Fundação de portfólio (F-01..F-04)          ← denominador comum a todo o programa
        ↓  estabelece
Indicadores de domínio (por capítulo)        ← o que cada domínio mede, com o mesmo denominador
        ↓  alimentam
Dimensões transversais T-01..T-06            ← agregação por perspectiva de risco
        ↓  resumem para
Dashboard executivo (secção final)           ← síntese para gestão e GRC
```

O princípio central desta arquitectura é que **o denominador de todos os KPIs de domínio é o mesmo**: o conjunto de aplicações classificadas ao nível de risco relevante, definido pela Fundação de portfólio. "80% dos sistemas L3 têm threat model" só é interpretável se o denominador (# sistemas L3 classificados) for partilhado por todos os capítulos.

Os KPIs transversais não substituem os indicadores de domínio - complementam-nos com uma perspectiva de segunda ordem: *o que é que o conjunto dos domínios diz sobre a saúde do programa?*

---

## Fundação de portfólio

A Fundação de portfólio é a camada zero do dashboard - as métricas absolutas que tornam todas as percentagens de domínio interpretáveis. Sem esta camada, os percentuais dos capítulos de domínio carecem de denominador partilhado e não permitem responder à pergunta fundamental: *o SbD-ToE está a ser aplicado na organização?*

### Funil de adoptabilidade SbD-ToE

```
F-01: Total de aplicações no portfólio
  └─ F-02: Aplicações com classificação de risco formal (L1 / L2 / L3)
        └─ F-03: Aplicações com requisitos de segurança formalmente mapeados
              └─ F-04: Aplicações com controlos de pelo menos um domínio validados com evidência
```

Cada camada do funil é o denominador da camada seguinte. A diferença entre camadas revela onde a adopção perde tração.

### Métricas de fundação

| ID | Métrica | Tipo | Threshold | Período |
|----|---------|:----:|-----------|---------|
| F-01 | # total de aplicações no portfólio organizacional (inventário activo) | Q# | Inventário completo obrigatório - ausência de dados invalida todos os KPIs subsequentes | Trimestral |
| F-02 | # aplicações com classificação de risco formal, por nível (L1 / L2 / L3) | Q# | = F-01 (toda a aplicação deve estar classificada) | Trimestral |
| F-03 | # aplicações com requisitos SbD-ToE formalmente mapeados ao nível de risco | Q# | L1: ≥ 80% de F-02(L1); L2: ≥ 95% de F-02(L2); L3: 100% de F-02(L3) | Semestral |
| F-04 | # aplicações com evidência de controlos validados em pelo menos um domínio técnico | Q# | L1: ≥ 70% de F-03; L2: ≥ 90% de F-03; L3: 100% de F-03 | Semestral |

**Nota sobre o denominador dos KPIs de domínio:** cada capítulo (Cap. 01–13) define indicadores do tipo "% aplicações com X". O denominador dessas percentagens é sempre F-02 segmentado pelo nível de risco relevante. Os ficheiros `addon/XX-kpis-metricas.md` de cada capítulo assumem este denominador como base - a sua validade depende de F-01 e F-02 estarem completos e actualizados.

### Interpretação do funil

| Situação | Diagnóstico | Acção |
|----------|-------------|-------|
| F-01 desconhecido ou incompleto | Inventário de aplicações inexistente - base de governação inválida | Prioridade zero: estabelecer inventário |
| F-02 &lt; F-01 | Aplicações sem classificação - os KPIs de domínio não têm denominador | Completar classificação antes de reportar |
| F-03 &lt;&lt; F-02 | Requisitos não mapeados - domínios técnicos funcionam sem referência normativa | Alinhamento Cap. 01 → Cap. 02 |
| F-04 &lt;&lt; F-03 | Requisitos mapeados mas sem validação - conformidade declarativa | Activar processos de validação por domínio |
| F-04 ≈ F-03 | Controlos aplicados e evidenciados - programa em maturidade operacional | Foco em melhoria contínua e T-06 |

---

## Convenções de tipo

| Código | Significado |
|--------|-------------|
| Q% | Quantitativo percentual - agrega percentagens de domínio |
| Qt | Quantitativo temporal - agrega ou compara tempos |
| Ord | Qualitativo ordinal - agrega níveis de maturidade (1–3) |
| Comp | Composto - combina múltiplos indicadores de domínio numa métrica derivada |

---

## Dimensões transversais

### T-01 - Cobertura de Controlos

**Definição:** percentagem de aplicações, por nível de risco (L1/L2/L3), que têm os controlos obrigatórios de cada domínio aplicados e verificados.

**Interpretação:** T-01 responde à pergunta *"o modelo está a ser aplicado?"*. Uma cobertura alta em todos os domínios indica que os requisitos estão a ser cumpridos. Lacunas por domínio revelam onde a adopção é mais fraca.

| Threshold | L1 | L2 | L3 |
|-----------|:--:|:--:|:--:|
| Cobertura mínima por domínio | ≥ 60% | ≥ 85% | ≥ 95% |
| Cobertura global (média ponderada) | ≥ 65% | ≥ 88% | ≥ 97% |

**Indicadores de domínio que alimentam T-01:**

| Capítulo | Indicador de referência |
|----------|------------------------|
| Cap. 01 - Classificação | CLA-K01 (classificação documentada), CLA-K02 (revisões no ciclo) |
| Cap. 02 - Requisitos | RQS-K01 (requisitos mapeados), RQS-K02 (evidência de implementação) |
| Cap. 03 - Threat Modeling | THR-K01 (threat model actualizado), THR-K03 (revisão AppSec) |
| Cap. 04 - Arquitectura | ARC-K01 (threat model), ARC-K04 (revisão com AppSec) |
| Cap. 05 - Dependências | DEP-K01 (SBOM), DEP-K05 (SCA com gate) |
| Cap. 06 - Desenvolvimento | DEV-K06 (SAST activo), DEV-K03 (code review com segurança) |
| Cap. 07 - CI/CD | CIC-K01 (gates em modo bloqueio), CIC-K04 (segredos via cofre) |
| Cap. 08 - IaC | IAC-K01 (policy-as-code), IAC-K07 (plan+review antes de apply) |
| Cap. 09 - Containers | CNT-K04 (admission controller), CNT-K05 (imagens base actualizadas) |
| Cap. 10 - Testes | TST-K01 (SAST por build), TST-K02 (DAST por release) |
| Cap. 11 - Deploy | DPL-K01 (checklist pré-deploy), DPL-K06 (evidência rastreável) |
| Cap. 12 - Operações | OPS (logging centralizado, alertas testados) |
| Cap. 14 - Governação | GOV-K07 (rastreabilidade organizacional completa) |

**Frequência de medição:** mensal por domínio; trimestral para síntese transversal.

---

### T-02 - Saúde de Excepções

**Definição:** estado qualitativo e quantitativo das excepções activas no programa - cobertura de cadeia de autoridade, validade temporal, e taxa de excepções em não conformidade (expiradas ou sem aprovação formal).

**Interpretação:** T-02 responde à pergunta *"os desvios ao modelo estão controlados?"*. Um programa com muitas excepções não é necessariamente inseguro - é inseguro quando essas excepções estão incompletas, expiradas, ou sem compensação documentada. A saúde das excepções é um proxy da maturidade do processo de gestão de risco.

| Indicador composto | Threshold |
|-------------------|-----------|
| % excepções com cadeia de autoridade completa | 100% (absoluto - não existe threshold inferior) |
| % excepções com prazo e reavaliação agendada | ≥ 80% (L1), 100% (L2/L3) |
| # excepções expiradas sem renovação | = 0 (absoluto - excepção expirada é não conformidade activa) |
| % bypasses de gate com aprovação formal | 100% (L2/L3) |
| % deploys de emergência com aprovação post-facto &lt; 24h | 100% (absoluto) |

**Indicadores de domínio que alimentam T-02:**

| Capítulo | Indicador de referência |
|----------|------------------------|
| Cap. 06 - Desenvolvimento | DEV-K04 (excepções SAST com aprovação) |
| Cap. 07 - CI/CD | CIC-K02 (bypasses com aprovação formal) |
| Cap. 08 - IaC | IAC-K04 (excepções de policy com registo) |
| Cap. 11 - Deploy | DPL-K02, DPL-K03, DPL-K07 (break-glass) |
| Cap. 14 - Governação | GOV-K02, GOV-K03, GOV-K04, GOV-K08 |

**Frequência de medição:** semanal para excepções expiradas (automatizável); mensal para estado geral.

---

### T-03 - Velocidade de Resolução

**Definição:** tempo médio de resolução (MTTR) de findings críticos e altos, agregado por origem (SAST, SCA, containers, testes, operações), ponderado pelo nível de risco das aplicações afectadas.

**Interpretação:** T-03 responde à pergunta *"a organização reage com rapidez adequada ao risco?"*. MTTR elevado em domínios críticos indica bottlenecks no processo de remediação - falta de capacidade, de priorização, ou de processo formal. A comparação entre domínios revela onde a resposta é mais lenta.

| Threshold MTTR - findings críticos | L1 | L2 | L3 |
|------------------------------------|:--:|:--:|:--:|
| SCA/Dependências (CVE ≥ 9.0) | 30 dias | 14 dias | 5 dias |
| SAST (severidade crítica) | 30 dias | 14 dias | 7 dias |
| Containers (CVE ≥ 9.0 em imagem) | 14 dias | 7 dias | 3 dias |
| Pipeline (detecção → mitigação) | 14 dias | 7 dias | 3 dias |
| Operações (alerta → mitigação) | - | 4h | 1h |

**Indicadores de domínio que alimentam T-03:**

| Capítulo | Indicador de referência |
|----------|------------------------|
| Cap. 05 - Dependências | DEP-K02, DEP-K03 (MTTR CVEs por severidade) |
| Cap. 06 - Desenvolvimento | DEV-K01 (MTTR SAST), DEV-K05 (taxa de regressão) |
| Cap. 07 - CI/CD | CIC-K05 (MTTR pipeline) |
| Cap. 09 - Containers | CNT-K02 (MTTR CVE em imagem) |
| Cap. 10 - Testes | TST-K03 (% findings no SLA), TST-K04 (taxa de regressão) |
| Cap. 11 - Deploy | DPL-K04 (rollbacks por segurança) |
| Cap. 12 - Operações | MTTR operacional (MTTD + tempo de mitigação) |

**Frequência de medição:** contínua (por evento para findings críticos); mensal para tendências.

---

### T-04 - Cobertura de Ownership

**Definição:** percentagem de aplicações, por nível de risco, com owner de segurança formalmente designado, activo e com formação válida. Inclui também a cobertura de aprovadores e revisores em processos críticos (excepções, releases, revisões de arquitectura).

**Interpretação:** T-04 responde à pergunta *"existe responsabilidade formal por cada activo?"*. Ownership sem formação válida é um controlo parcial. Aplicações sem owner designado são pontos cegos de governação - desvios nessas aplicações não têm destinatário, e decisões não têm autoridade legitimada.

| Threshold | L1 | L2 | L3 |
|-----------|:--:|:--:|:--:|
| % aplicações com owner designado e activo | 100% | 100% | 100% |
| % owners com formação SbD válida (&lt; 12 meses) | ≥ 80% | ≥ 95% | 100% |
| % revisões de arquitectura com AppSec formal | - | ≥ 80% | 100% |
| % PRs L2/L3 com reviewer de segurança | - | ≥ 80% | 100% |

**Indicadores de domínio que alimentam T-04:**

| Capítulo | Indicador de referência |
|----------|------------------------|
| Cap. 04 - Arquitectura | ARC-K04 (AppSec em revisões) |
| Cap. 06 - Desenvolvimento | DEV-K03 (code review com segurança) |
| Cap. 13 - Formação | TRN-K02 (owners com formação válida), TRN-K07 (champions activos) |
| Cap. 14 - Governação | GOV-K01, GOV-K07 |

**Frequência de medição:** trimestral para cobertura de ownership; mensal para formação.

---

### T-05 - Cadeia de Fornecimento

**Definição:** estado de segurança da cadeia de fornecimento de software - cobertura de SBOM, conformidade contratual com fornecedores, validação de fornecedores L3, e cobertura de assinatura de artefactos.

**Interpretação:** T-05 responde à pergunta *"a organização conhece e controla o que terceiros introduzem nos seus sistemas?"*. A cadeia de fornecimento é um vector de risco que atravessa múltiplos domínios: dependências (cap. 05), containers (cap. 09), e contratos (cap. 14). A dimensão T-05 agrega esses sinais numa perspectiva de supply chain security.

| Indicador composto | Threshold L1 | Threshold L2 | Threshold L3 |
|-------------------|:------------:|:------------:|:------------:|
| % aplicações com SBOM actualizado | ≥ 50% | ≥ 90% | 100% |
| % contratos L2/L3 com cláusulas de segurança | ≥ 80% | 100% | 100% |
| % fornecedores L3 com validação anual | - | - | 100% |
| % imagens de produção assinadas e verificadas | - | ≥ 70% | 100% |
| # dependências EOL sem mantedor activo em produção | ≤ 5 | ≤ 2 | = 0 |

**Indicadores de domínio que alimentam T-05:**

| Capítulo | Indicador de referência |
|----------|------------------------|
| Cap. 05 - Dependências | DEP-K01 (SBOM), DEP-K04 (EOL), DEP-K06 (licenças) |
| Cap. 09 - Containers | CNT-K03 (assinatura), CNT-K05 (base images), CNT-K06 (SBOM de imagem) |
| Cap. 14 - Governação | GOV-K05 (cláusulas contratuais), GOV-K06 (validação de fornecedores) |

**Frequência de medição:** mensal para SBOM e imagens; semestral para contratos; anual para validação de fornecedores.

---

### T-06 - Maturidade SbD-ToE

**Definição:** nível de maturidade por domínio (escala 1–3, alinhada com L1/L2/L3), derivado de avaliação estruturada anual. A evolução face ao ciclo anterior é componente obrigatória.

**Interpretação:** T-06 responde à pergunta *"o programa está a evoluir?"*. Os níveis de maturidade não são objetivos finais - são estados de um continuum. Um domínio que permanece no mesmo nível durante dois ciclos consecutivos sem plano de evolução activo representa estagnação, não estabilidade.

| Nível | Caracterização |
|-------|---------------|
| 1 | Controlos aplicados de forma pontual e dependente de indivíduos; rastreabilidade mínima |
| 2 | Processo definido e em uso; owners designados; excepções com registo; KPIs recolhidos |
| 3 | Processo automatizado onde possível; rastreabilidade completa; KPIs com thresholds e acção correctiva; evolução comparada com ciclo anterior |

**Escala de maturidade por domínio (referência de avaliação):**

| Domínio | Nível mínimo esperado L1 | Nível mínimo esperado L2 | Nível mínimo esperado L3 |
|---------|:------------------------:|:------------------------:|:------------------------:|
| Cap. 04 - Arquitectura | 1 | 2 | 3 |
| Cap. 05 - Dependências | 1 | 2 | 3 |
| Cap. 06 - Desenvolvimento | 1 | 2 | 3 |
| Cap. 07 - CI/CD | 1 | 2 | 3 |
| Cap. 08 - IaC | 1 | 2 | 3 |
| Cap. 09 - Containers | 1 | 2 | 3 |
| Cap. 10 - Testes | 1 | 2 | 3 |
| Cap. 11 - Deploy | 1 | 2 | 3 |
| Cap. 12 - Operações | 1 | 2 | 3 |
| Cap. 14 - Governação | 1 | 2 | 3 |

**Frequência de medição:** anual - avaliação estruturada com evidência por domínio; comparação obrigatória com ciclo anterior.

---

## Dashboard executivo - síntese

O dashboard executivo é uma vista condensada das seis dimensões, orientada à comunicação com gestão, GRC e CISO. Não introduz novos dados - resume os KPIs transversais num formato de síntese.

| Dimensão | Indicador síntese | Frequência de reporte |
|----------|-------------------|----------------------|
| T-01 Cobertura | % médio de cobertura de controlos por domínio e nível de risco | Trimestral |
| T-02 Excepções | # excepções activas / # expiradas sem renovação / % com cadeia de autoridade completa | Mensal |
| T-03 Velocidade | MTTR médio ponderado por severidade e nível de risco | Mensal |
| T-04 Ownership | % aplicações com owner e formação válida | Trimestral |
| T-05 Supply Chain | % SBOM activos / % contratos conformes / % fornecedores L3 validados | Semestral |
| T-06 Maturidade | Nível médio por domínio + delta face ao ciclo anterior | Anual |

**Critérios de alerta para reporte executivo:**

- T-01: qualquer domínio abaixo do threshold mínimo por nível de risco → **alerta vermelho**
- T-02: qualquer excepção expirada sem renovação → **alerta vermelho imediato**
- T-03: MTTR de finding crítico acima do dobro do threshold definido → **alerta vermelho**
- T-04: % de owners com formação válida abaixo de 80% em qualquer nível → **alerta amarelo**
- T-05: qualquer fornecedor L3 sem validação anual → **alerta vermelho**
- T-06: qualquer domínio abaixo do nível mínimo esperado para o nível de risco dominante da organização → **alerta amarelo com plano obrigatório**

---

## Recolha e responsabilidades

| Dimensão | Owner de recolha | Suporte de instrumentação |
|----------|-----------------|--------------------------|
| T-01 | AppSec | Auditoria de pipeline + inventário de aplicações |
| T-02 | GRC / AppSec | Sistema de gestão de excepções (alertas automáticos) |
| T-03 | AppSec | Plataforma de findings (DefectDojo, Vulcan) + pipeline logs |
| T-04 | GRC | Registo de owners + plataforma de formação |
| T-05 | AppSec + Procurement | SBOM registry + repositório de contratos |
| T-06 | CISO / GRC | Avaliação estruturada anual com evidência por domínio |

---

## Referências cruzadas

| Documento | Relação |
|-----------|---------|
| `addon/13-kpis-dominio-gov.md` | KPIs de domínio GOV que alimentam T-02, T-04, T-05 |
| Cap. 01 `addon/12-kpis-metricas.md` | Indicadores CLA → T-01, T-06 |
| Cap. 02 `addon/16-kpis-metricas.md` | Indicadores RQS → T-01, T-06 |
| Cap. 03 `addon/11-kpis-metricas.md` | Indicadores THR → T-01, T-06 |
| Cap. 04 `addon/10-kpis-metricas.md` | Indicadores ARC → T-01, T-04, T-06 |
| Cap. 05 `addon/10-kpis-metricas.md` | Indicadores DEP → T-01, T-03, T-05 |
| Cap. 06 `addon/11-kpis-metricas.md` | Indicadores DEV → T-01, T-02, T-03 |
| Cap. 07 `addon/13-kpis-metricas.md` | Indicadores CIC → T-01, T-02, T-03 |
| Cap. 08 `addon/12-kpis-metricas.md` | Indicadores IAC → T-01, T-02 |
| Cap. 09 `addon/11-kpis-metricas.md` | Indicadores CNT → T-01, T-03, T-05 |
| Cap. 10 `addon/15-kpis-metricas.md` | Indicadores TST → T-01, T-03 |
| Cap. 11 `addon/10-kpis-metricas.md` | Indicadores DPL → T-01, T-02 |
| Cap. 12 `addon/07-metricas-indicadores.md` | Indicadores OPS → T-03 |
| Cap. 13 `addon/91-kpis-metricas.md` | Indicadores TRN → T-04 |
| `addon/00-catalogo-requisitos.md` | Requisitos GOV-011 (KPIs definidos e reportados) |
