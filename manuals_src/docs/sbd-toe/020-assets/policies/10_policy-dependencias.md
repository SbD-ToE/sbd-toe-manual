---
id: policy-dependencias
title: Política de Gestão de Dependências
description: Política organizacional que define os critérios de aprovação, pinning, bloqueio, auditing e atualização de dependências externas em projetos de software, proporcional ao nível de criticidade da aplicação (L1, L2, L3), com foco na redução de risco de supply chain e na garantia de rastreabilidade.
tags: [policy, dependências, SCA, supply chain, CVE, licenças, pinning, SBOM, cap05, L1, L2, L3, governance]
sidebar_position: 10
---

# Política de Gestão de Dependências

## 1. Objetivo

Esta política define os requisitos para a **gestão segura de dependências externas** em projetos de software desenvolvidos ou operados pela organização.

Toda a dependência externa é uma extensão da superfície de ataque da aplicação. Componentes de terceiros podem introduzir vulnerabilidades conhecidas, licenças incompatíveis, origens não verificadas ou código abandonado. Sem uma política de gestão formal, as dependências acumulam-se sem auditoria, os CVEs propagam-se silenciosamente e o risco de supply chain cresce de forma invisível.

O objetivo desta política é garantir que:

- Toda a dependência introduzida é aprovada, com origem validada e licença verificada
- Dependências com CVEs ativos são geridas com critérios de severidade proporcionais ao nível de risco
- O inventário de dependências é mantido atualizado e rastreável por build
- A atualização de dependências é monitorizada e gerida de forma controlada
- Bibliotecas locais (copiadas fora de package manager) são proibidas sem exceção formal

---

## 2. Âmbito

Esta política aplica-se a todos os projetos com código de terceiros, independentemente da linguagem ou runtime, incluindo:

- Dependências diretas declaradas em ficheiros de manifesto (`package.json`, `requirements.txt`, `pom.xml`, `go.mod`, etc.)
- Dependências transitivas incluídas através de dependências diretas
- Bibliotecas copiadas localmente fora de package manager (ficheiros `.js`, `.jar`, `.dll`, `.php`, etc.)
- Imagens base de containers (cobertas também pela Política de Containers Seguros)

---

## 3. Critérios de aprovação de dependências

### 3.1 Validação obrigatória por dependência nova

Antes da inclusão de qualquer nova dependência num projeto L2/L3, deve ser realizada uma validação formal que cubra os seguintes critérios:

| Critério | Descrição |
|---|---|
| **Origem e proveniência** | Repositório público de referência (PyPI, npm, Maven Central, etc.) ou repositório interno aprovado |
| **Manutenção activa** | Projeto com manutenção activa; sem sinais de abandono nos últimos 12 meses |
| **Licença compatível** | Licença compatível com a política de licenças da organização (`licenses-whitelist.yaml`) |
| **CVEs conhecidos** | Sem CVEs críticos ou high sem mitigação; CVEs médios avaliados com contexto |
| **Popularidade e reputação** | Indícios de adoção ampla e historico de resposta a vulnerabilidades |
| **Âmbito mínimo** | A dependência resolve o problema sem introduzir funcionalidades excessivas não necessárias |

### 3.2 Registo de aprovação

A aprovação de cada nova dependência deve ser registada em `dependencies-approval.md`, com:

- [ ] Nome, versão e repositório de origem
- [ ] Justificação técnica da necessidade
- [ ] Resultado da validação de licença
- [ ] Resultado da verificação de CVEs à data de aprovação
- [ ] Responsável pela aprovação e data

### 3.3 Proporcionalidade

| Requisito | L1 | L2 | L3 |
|---|---|---|---|
| Aprovação formal de dependências novas | Recomendado | Obrigatório | Obrigatório |
| Validação de licença | Recomendado | Obrigatório | Obrigatório |
| Registo em `dependencies-approval.md` | Opcional | Obrigatório | Obrigatório |
| Validação por AppSec Engineer | Não aplicável | Recomendado | Obrigatório |

---

## 4. Pinning de versões

### 4.1 Obrigatoriedade

Todas as dependências devem ser fixadas a versões específicas (pinning) de forma a garantir reprodutibilidade de build e evitar introdução involuntária de alterações:

| Nível | Requisito de pinning |
|---|---|
| L1 | Recomendado; pelo menos lock file gerado e versionado |
| L2 | Obrigatório; versão exata no manifesto ou lock file versionado no repositório |
| L3 | Obrigatório; versão exata e hash de integridade sempre que o ecossistema suportar |

### 4.2 Lock files

- O lock file (`package-lock.json`, `poetry.lock`, `Pipfile.lock`, `go.sum`, etc.) deve ser versionado no repositório e nunca gerado ad-hoc em ambientes CI
- Alterações ao lock file devem ser revistas como parte da revisão de código

---

## 5. Proibição de bibliotecas locais

A cópia de bibliotecas diretamente para o repositório (fora de package manager) é **proibida** sem exceção formal aprovada. Inclui:

- Ficheiros `.js`, `.min.js` copiados para `vendor/`, `static/` ou equivalente
- Arquivos `.jar`, `.dll`, `.so`, `.dylib` incluídos diretamente no repositório
- Ficheiros `.php` de bibliotecas copiados diretamente

:::warning
A presença de bibliotecas locais impede a detecção automática de CVEs por SCA, quebra a rastreabilidade de proveniência e impossibilita a gestão de atualizações. A deteção de bibliotecas locais não declaradas no package manager deve ser automatizada no pipeline (`.audit-libs.json`/`.audit-libs.yaml`) e bloquear o build em L2/L3.
:::

Quando a inclusão local é tecnicamente inevitável, deve ser formalizada como exceção nos termos da Política de Gestão de Exceções de Segurança, com:

- [ ] Justificação técnica
- [ ] Hash de integridade do ficheiro incluído
- [ ] CVEs verificados manualmente
- [ ] TTL da exceção e plano de substituição

---

## 6. Bloqueio de fontes externas diretas

Em L2/L3, dependências não devem ser resolvidas diretamente da internet em tempo de build. O pipeline deve:

- [ ] Utilizar repositório interno (proxy/mirror) como única fonte de resolução
- [ ] Bloquear acesso direto a repositórios públicos durante o build (onde tecnicamente viável)
- [ ] Verificar integridade dos pacotes por hash antes da instalação

A configuração do repositório interno deve ser registada em `repo-config.yaml` e revista periodicamente.

---

## 7. SCA - Análise de composição de software

### 7.1 Integração no pipeline

O pipeline CI/CD deve incluir análise SCA automática em cada build, cobrindo dependências diretas e transitivas:

| Nível | Requisito SCA |
|---|---|
| L1 | Alerta; não bloqueia |
| L2 | Bloqueia findings High e Critical sem exceção aprovada |
| L3 | Bloqueia findings Medium, High e Critical sem exceção aprovada |

### 7.2 Ferramentas de referência

Ferramentas aceites para SCA: OWASP Dependency-Check, Trivy, Grype, Snyk, ou equivalente com suporte a NVD/OSV.

### 7.3 Artefacto de evidência

O relatório SCA (`sca-report.html` ou JSON) deve ser arquivado como artefacto do pipeline com referência ao commit, nos termos da Política de Rastreabilidade.

---

## 8. Alertas de vulnerabilidades em produção

Para sistemas em produção, deve existir um mecanismo de correlação entre o SBOM da versão implantada e CVEs publicados após o deploy:

- [ ] Inventário de componentes implantados por serviço e ambiente (`inventario-runtime-<servico>-<ambiente>.json`)
- [ ] Integração com feed de vulnerabilidades (NVD, OSV, GitHub Advisory Database)
- [ ] Alerta gerado quando CVE afeta versão implantada, com componente, versão, ambiente e severidade
- [ ] SLA de resposta definido por severidade (ver Política de Exceções a CVEs)

---

## 9. Auditoria periódica

Independentemente dos gates de build, as dependências devem ser auditadas periodicamente:

| Nível | Cadência mínima |
|---|---|
| L1 | Semestral ou por cada release major |
| L2 | Trimestral ou por cada release major |
| L3 | Mensal ou por cada release |

A auditoria deve cobrir:
- [ ] Dependências sem uso ativo (podem ser removidas)
- [ ] Versões significativamente desatualizadas face à versão estável mais recente
- [ ] CVEs publicados após a última auditoria
- [ ] Licenças que mudaram nas versões mais recentes
- [ ] Bibliotecas locais existentes com estado de exceção

---

## 10. Artefactos

| Artefacto | Descrição | Retenção |
|---|---|---|
| `dependencies-approval.md` | Registo de aprovação de dependências | Enquanto a dependência estiver em uso |
| `sbom.json` / `sbom.xml` | Inventário por build (CycloneDX/SPDX) | Ver Política de SBOM |
| `sca-report.html` / JSON | Relatório de vulnerabilidades por build | 90 dias (L2), 1 ano (L3) |
| `inventario-runtime-*.json` | Componentes implantados por serviço/ambiente | Enquanto o deploy estiver ativo |
| `repo-config.yaml` | Configuração de repositórios internos | Versão ativa no repositório |
| `.audit-libs.json` | Resultados de auditoria de libs locais | Por release |
| `licenses-whitelist.yaml` | Lista de licenças aprovadas pela organização | Versão ativa no repositório |

---

## 11. Responsabilidades

| Role | Responsabilidade |
|---|---|
| Developer | Identificar e submeter novas dependências para aprovação; manter lock files atualizados |
| Tech Lead | Validar necessidade e âmbito de novas dependências; conduzir auditoria periódica |
| AppSec Engineer | Aprovar dependências em L3; configurar e calibrar SCA; gerir política de licenças |
| DevOps / SRE | Manter repositório interno de packages; configurar gates SCA no pipeline; monitorizar alertas em produção |
| GRC / Compliance | Verificar cobertura de SCA; auditar registos de aprovação; emitir relatórios de conformidade |

---

## 12. Revisão e auditoria desta política

Esta política deve ser **revista anualmente** ou após qualquer um dos seguintes eventos:

- Incidente com origem em dependência vulnerável não detetada
- Alteração significativa no ecossistema de package managers utilizado
- Alteração regulatória com impacto na gestão de supply chain de software

---

## 13. Referências normativas e técnicas

| Referência | Relevância |
|---|---|
| SbD-ToE Cap. 05 - Dependências, SBOM e SCA | Inventário, SCA, alertas, artefactos, user stories |
| SbD-ToE Cap. 07 - CI/CD Seguro | Integração SCA no pipeline e gates |
| SbD-ToE Cap. 09 - Containers e Imagens | Dependências em imagens base |
| Política de SBOM (`11_policy-sbom.md`) | Geração e retenção de SBOM por build |
| Política de Exceções a CVEs (`12_policy-excecoes-cve.md`) | Gestão de CVEs sem fix disponível |
| OWASP Dependency-Check | Ferramenta SCA de referência |
| CycloneDX / SPDX | Formatos de SBOM |
| NIST SP 800-161 | Cybersecurity Supply Chain Risk Management |
| SSDF PW.4 | Reuse of existing, well-secured software |
| SLSA (Supply chain Levels for Software Artifacts) | Framework de integridade de supply chain |
