---
id: policy-atualizacao-automatica
title: Política de Atualização Automática de Dependências
description: Política organizacional que define os requisitos para a operação de bots de atualização automática de dependências, incluindo critérios de auto-merge, análise de impacto, handoff humano e configuração proporcional ao nível de criticidade da aplicação (L2, L3).
tags: [policy, dependências, atualização, Renovate, Dependabot, auto-merge, impact analysis, handoff, cap05, L2, L3, governance, supply chain]
sidebar_position: 13
---

# Política de Atualização Automática de Dependências

## 1. Objetivo

Esta política define os requisitos para a **operação controlada de bots de atualização automática de dependências** em repositórios de software classificados como L2 ou L3.

Dependências desatualizadas acumulam vulnerabilidades e derivam do estado seguro aprovado. A atualização manual sistemática é ineficiente e propensa a omissões. Ferramentas de automação como Renovate ou Dependabot permitem detetar e propor atualizações de forma contínua — mas, sem critérios de governação claros, podem introduzir alterações breaking sem revisão humana adequada ou, inversamente, criar ruído que leva à desativação dos bots por frustração operacional.

O objetivo desta política é garantir que:

- Bots de atualização estão ativos e configurados em todos os repositórios L2/L3
- O critério de auto-merge é restrito a atualizações de impacto nulo ou mínimo verificado
- Atualizações com potencial de breaking change exigem revisão e aprovação humana
- A cadência e o agrupamento de PRs são configurados para minimizar ruído operacional

---

## 2. Âmbito e obrigatoriedade

| Nível | Obrigatoriedade |
|---|---|
| L1 | Recomendado; configuração mínima sem auto-merge |
| L2 | Obrigatório; bot ativo com auto-merge condicional |
| L3 | Obrigatório; bot ativo com auto-merge restrito e handoff humano para qualquer atualização com impacto |

---

## 3. Ferramentas aceites

A organização aceita as seguintes ferramentas para automação de atualização de dependências:

| Ferramenta | Ecossistemas suportados | Notas |
|---|---|---|
| **Renovate** | npm, pip, Maven, Go, Docker, Terraform, Helm, etc. | Preferida; maior granularidade de configuração |
| **Dependabot** | npm, pip, Maven, Go, Docker, GitHub Actions, etc. | Aceite; integração nativa com GitHub |
| Alternativas equivalentes | Variável | Devem suportar impact analysis, agrupamento e configuração de auto-merge |

---

## 4. Critérios de auto-merge

O auto-merge automático de PRs de atualização só é permitido quando **todos** os seguintes critérios são satisfeitos:

| Critério | Requisito |
|---|---|
| Tipo de atualização | Patch ou minor sem breaking change declarado |
| Análise de impacto | Bot confirma: sem alteração de API pública, sem major semver, sem flags de breaking change em release notes |
| Pipeline CI | Todos os jobs passam (testes, SAST, SCA, linters) |
| Gates de segurança | Nenhum CVE novo introduzido pela atualização |
| Licença | Licença da nova versão idêntica ou equivalente à anterior; sem licença nova adicionada que não esteja na whitelist |

:::warning
Auto-merge em L3 é restrito a atualizações patch. Atualizações minor em L3 requerem revisão humana, mesmo que o CI passe.
:::

### 4.1 Proporcionalidade do auto-merge

| Tipo de atualização | L1 | L2 | L3 |
|---|---|---|---|
| Patch (ex: 1.2.3 → 1.2.4) | Auto-merge se CI verde | Auto-merge se CI verde + gates OK | Requer revisão humana |
| Minor sem breaking (ex: 1.2.x → 1.3.0) | Requer revisão | Requer revisão | Requer revisão + aprovação AppSec |
| Major (ex: 1.x → 2.0.0) | Requer revisão + testes | Requer revisão + AppSec + testes | Requer revisão + AppSec + arquiteto |
| Security patch (CVE fix) | Auto-merge se CI verde | Auto-merge prioritário se CI verde | Revisão acelerada: prazo ≤ 24h |

---

## 5. Handoff humano

Quando a análise de impacto determina que a atualização não é elegível para auto-merge, o bot deve:

- [ ] Abrir PR com label `requires-human-review`
- [ ] Incluir no corpo do PR: versão anterior, versão nova, changelog relevante, breaking changes identificados, guidelines de refactor quando disponíveis
- [ ] Atribuir o PR ao Tech Lead ou Developer responsável pela dependência
- [ ] Não fazer merge sem aprovação explícita

O PR não deve ficar aberto sem resposta por mais de:

| Severidade | L2 | L3 |
|---|---|---|
| Security patch (CVE) | 48 horas | 24 horas |
| Minor / Major | 14 dias | 7 dias |

PRs de atualização sem resposta dentro do prazo devem gerar alerta para o Tech Lead e AppSec Engineer.

---

## 6. Configuração obrigatória dos bots

### 6.1 Parâmetros mínimos de configuração

A configuração do bot (ex: `renovate.json`, `.github/dependabot.yml`) deve incluir:

- [ ] Agrupamento de dependências relacionadas em PRs únicos (ex: todas as dependências `@types/*` agrupadas)
- [ ] Janela de atualização definida (ex: segunda a sexta, fora de períodos de freeze)
- [ ] Número máximo de PRs simultâneos abertos (recomendado: ≤ 5 por repositório)
- [ ] Labels automáticos por tipo de atualização (`patch`, `minor`, `major`, `security`)
- [ ] Regras de auto-merge explícitas no ficheiro de configuração (não assumidas por defeito)
- [ ] Exclusão de dependências marcadas como geridas manualmente

### 6.2 Repositórios internos como fonte

Em L2/L3, o bot deve resolver pacotes através do repositório interno (proxy/mirror), não diretamente da internet. A configuração do bot deve referenciar os registos internos da organização.

---

## 7. Integração com SCA e gates

A atualização automática não dispensa a análise SCA:

- [ ] Cada PR de atualização despoleta o pipeline CI completo, incluindo SCA
- [ ] O auto-merge é bloqueado se o SCA detetar CVE novo introduzido pela versão proposta
- [ ] O relatório SCA é anexado ao PR como artefacto ou comentário

---

## 8. Freeze periods e exceções

Durante períodos de freeze de releases (ex: pré-release, janelas de manutenção regulamentada), os bots devem:

- Suspender a abertura de novos PRs de atualização não relacionados com segurança
- Permitir PRs de security patches mesmo durante freeze (com revisão humana obrigatória em L3)

A definição de freeze periods deve ser configurada no ficheiro de configuração do bot ou gerida por variável no pipeline.

---

## 9. Monitorização e métricas

Os seguintes indicadores devem ser monitorizados para avaliar a saúde do processo de atualização:

| Métrica | Descrição |
|---|---|
| Taxa de auto-merge | % de PRs de atualização resolvidos por auto-merge vs. revisão humana |
| Tempo médio de resolução de PRs de segurança | MTTR para security patches |
| PRs de atualização abertos há mais de 14 dias | Indicador de acumulação de dívida técnica |
| CVEs detetados pós-merge | Atualizações que introduziram CVEs não detetados antes do merge |

---

## 10. Responsabilidades

| Role | Responsabilidade |
|---|---|
| Developer | Responder a PRs de handoff humano dentro do prazo; rever breaking changes |
| Tech Lead | Configurar e manter o ficheiro de configuração do bot; gerir PRs com impacto major |
| AppSec Engineer | Definir critérios de auto-merge; validar PRs de atualização com impacto de segurança; rever configuração periodicamente |
| DevOps / SRE | Integrar bot no repositório; configurar repositórios internos como fonte; monitorizar métricas |

---

## 11. Revisão e auditoria desta política

Esta política deve ser **revista anualmente** ou após qualquer um dos seguintes eventos:

- Incidente causado por atualização automática que introduziu regressão ou vulnerabilidade
- Alteração significativa nas capacidades das ferramentas de automação utilizadas
- Alteração de política de freeze de releases que afete a operação dos bots

---

## 12. Referências normativas e técnicas

| Referência | Relevância |
|---|---|
| SbD-ToE Cap. 05 — Dependências, SBOM e SCA | Automação de atualização, impact analysis, handoff |
| Política de Dependências (`10_policy-dependencias.md`) | Aprovação de dependências e pinning |
| Política de Exceções a CVEs (`12_policy-excecoes-cve.md`) | Gestão de CVEs detetados durante atualização |
| Renovate Documentation | Configuração de bots de atualização |
| Dependabot Documentation | Configuração alternativa em ecossistemas GitHub |
| Semantic Versioning (semver.org) | Base para análise de impacto por tipo de versão |
| NIST SP 800-161 | Supply Chain Risk Management — atualização de componentes |
