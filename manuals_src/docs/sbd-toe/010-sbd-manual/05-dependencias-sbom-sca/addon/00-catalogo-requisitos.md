---
id: catalogo-requisitos-dependencias
title: Catálogo de Requisitos de Dependências, SBOM e SCA
description: Catálogo canónico de requisitos de segurança para gestão de dependências de terceiros (DEP-001 a DEP-010), com aplicabilidade por nível de risco e critérios de aceitação para SBOM, SCA, governação de bibliotecas e políticas de actualização.
requirement_class: dominio
tags: [tipo:catalogo, classe:dominio, tema:dependencias, DEP, SBOM, SCA, supply-chain, rastreabilidade, L1, L2, L3, auditoria, CycloneDX, SPDX]
sidebar_position: 0
---

<!--template: sbdtoe-addon -->

# Catálogo de Requisitos de Dependências, SBOM e SCA

## Âmbito: gestão da cadeia de fornecimento de software

Este catálogo cobre **requisitos de segurança aplicáveis à gestão de dependências de terceiros** ao longo do ciclo de vida do software - desde a selecção e aprovação de bibliotecas, passando pela geração de SBOM e scanning de vulnerabilidades, até às políticas de actualização e rastreabilidade de correcções.

A dependência de bibliotecas e componentes de terceiros é uma das principais superfícies de risco na cadeia de fornecimento de software: componentes vulneráveis, abandonados ou maliciosos são vectores estabelecidos de ataque (OWASP A06, Log4Shell, XZ Utils, etc.). Estes requisitos estabelecem os controlos mínimos para que essa dependência seja **conhecida, governada e auditável**.

Para o mapeamento completo de todos os catálogos de requisitos do SbD-ToE por domínio técnico, prefixo canónico e responsável, consultar [Cap. 02 - Mapeamento de Catálogos](/sbd-toe/sbd-manual/requisitos-seguranca/addon/lista-requisitos-base#mapeamento-de-catalogos).

> **Sobre a curadoria:** Consolidado a partir de OWASP Top 10 (A06 - Vulnerable Components), NIST SSDF (PS.3, PW.4), SLSA Supply Chain Framework, CISA SBOM Guidelines, Executive Order 14028 e boas práticas de gestão de dependências por stack. Deve ser adaptado ao contexto tecnológico e revisto com cada ciclo de actualização de política de segurança.

Para instanciação em projecto e nomenclatura operacional (`SEC-Lx-DEP-CODIGO`), ver [Taxonomia e Rastreabilidade](/sbd-toe/sbd-manual/requisitos-seguranca/addon/taxonomia-rastreabilidade).

---

## Convenções

| Símbolo | Significado |
|---------|-------------|
| ✔ | Requisito obrigatório para este nível |
| - | Não aplicável ou não obrigatório a este nível |

Os níveis são cumulativos: L3 inclui todos os requisitos de L1 e L2; L2 inclui todos os de L1.

---

## Catálogo DEP - Dependências, SBOM e SCA

Requisitos que garantem que todas as dependências de terceiros são conhecidas, analisadas, governadas e actualizadas de forma proporcional ao risco.

| ID | Nome | L1 | L2 | L3 | Critério de aceitação |
|----|------|:--:|:--:|:--:|----------------------|
| DEP-001 | SBOM gerado por build, em formato standardizado | ✔ | ✔ | ✔ | SBOM presente e acessível para cada build, em formato CycloneDX ou SPDX; inclui dependências directas e transitivas; artefacto versionado e ligado ao build que o gerou. |
| DEP-002 | SCA integrado em pipeline com bloqueio por política de severidade | ✔ | ✔ | ✔ | Scanner SCA activo no CI/CD; política de severidade documentada; CVEs de severidade crítica ou elevada bloqueiam a promoção; relatório de scan disponível por execução. |
| DEP-003 | Versões de dependências fixas e auditáveis | ✔ | ✔ | ✔ | Lockfile presente, versionado e actualizado; ausência de referências sem versão (`*`, `latest`, ranges não limitados); integridade verificável por hash (ex: `integrity` field em npm, `--hash` em pip). |
| DEP-004 | Proibição de dependências introduzidas por cópia manual | ✔ | ✔ | ✔ | Ausência de bibliotecas de terceiros copiadas directamente para o repositório fora do package manager; verificável por scan de estrutura; processo documentado que o proíbe explicitamente. |
| DEP-005 | Registries e repositórios de origem controlados | - | ✔ | ✔ | Lista de registries e repositórios permitidos definida e enforced; downloads de fontes não aprovadas bloqueados em pipeline ou por política de rede; evidência de enforcement activo. |
| DEP-006 | Aprovação formal para introdução de novas dependências | - | ✔ | ✔ | Processo documentado de aprovação de novas bibliotecas com critérios mínimos: actividade de manutenção, licença compatível, ausência de CVEs activos, popularidade verificada; registo de aprovação disponível por dependência. |
| DEP-007 | Política de actualização com SLA definido por severidade | ✔ | ✔ | ✔ | SLA de actualização definido por nível de severidade de CVE (ex: crítico ≤ 48h, elevado ≤ 7 dias, médio ≤ 30 dias); evidência de cumprimento nos ciclos mais recentes; excepções formalizadas quando aplicável. |
| DEP-008 | Actualização automatizada com análise de impacto | - | ✔ | ✔ | Bot de actualização activo (ex: Dependabot, Renovate); PRs gerados automaticamente com informação de impacto semver, changelogs e testes; intervenção humana obrigatória para breaking changes; PRs não integrados automaticamente sem revisão. |
| DEP-009 | Detecção de dependências não-intencionais ou emergentes | - | - | ✔ | Processo definido para detectar dependências introduzidas via tooling, geração de código, pipelines ou runtime loading; fronteiras de inventário documentadas; desvios detectados e tratados. |
| DEP-010 | Rastreabilidade SBOM → vulnerabilidade → correcção | - | ✔ | ✔ | Evidência rastreável desde o componente identificado no SBOM até à CVE associada e à acção tomada (PR de correcção, actualização de versão ou excepção formalizada com justificação e data de revisão). |
| DEP-011 | Inventário e proveniência de dependências AI/ML | - | ✔ | ✔ | Sistemas com componentes AI/ML têm inventário dedicado de dependências AI: (1) modelos base com versão, hash do artefacto e fonte (model registry, fine-tuning provenance); (2) datasets de treino e fine-tuning com versão, fonte e processo de curadoria; (3) MCP servers e tools expostas a agentes com identificador, versão e scope (`AML.T0110` AI Agent Tool Poisoning); (4) prompts embebidos relevantes para comportamento (system prompts, RAG templates) com versão e owner. O inventário é gerado por build e integrado no SBOM principal (DEP-001); incidentes upstream em modelos, datasets ou MCP servers (LLM03-2025 Supply Chain, `AML.T0010` AI Supply Chain Compromise) accionam o mesmo processo de triagem de DEP-002/DEP-007. |
| DEP-012 | AI BOM gerado por *build* em formato standardizado | - | ✔ | ✔ | O inventário AI/ML (DEP-011) é materializado como **AI BOM** em formato standardizado por *build* — preferimos CycloneDX 1.6 com extensão `ml-bom` (publicada em 2024) ou equivalente reconhecido (`ML-BOM`, `AIBOM`). O AI BOM é artefacto do *build* (não análise separada), versionado, e ligado ao SBOM principal. Inclui modelos, datasets, MCP servers/tools e prompts embebidos com versão *pinned*, hash, *provider* e licença. |
| DEP-013 | Versão *pinned* explícita para modelos AI e providers | - | ✔ | ✔ | Modelos AI usados em produção ou em pipeline têm **versão fixa explícita** — ex.: `claude-opus-4-7@sha:…` em vez de `claude-latest`. Ranges semver, *aliases* dinâmicos (`latest`, `stable`) e referências sem versão são **proibidos** em qualquer ambiente que não seja exploratório. Mudança de versão maior do provider exige nova *eval suite* (Cap. 10 §C5) e revisão do *threat model* (Cap. 03 US-11). Mitiga *AI Supply Chain Rug Pull* (`AML.T0109`). |
| DEP-014 | Lista de *providers* AI aprovados com classificação de risco | - | ✔ | ✔ | Providers de modelos AI (Anthropic, OpenAI, HuggingFace, providers próprios self-hosted) usados pela organização estão numa **lista aprovada** com classificação de risco e cláusulas contratuais aplicáveis (cross-link Cap. 14 — contratação de AI providers). Critérios mínimos de aprovação: zero retention para dados sensíveis quando aplicável; localização de processamento conforme RGPD Art. 44–49; auditoria contratualizada; SLA de notificação prévia de mudanças de versão; conformidade declarada com AI Act Art. 53/55 se fornecer GPAI. Lista revista periodicamente conforme nível de criticidade. |

---

## Notas explicativas

- **DEP-001**: O SBOM deve ser gerado como artefacto do próprio processo de build, não como análise separada. Ferramentas de referência: Syft, Trivy, CycloneDX Maven Plugin, OWASP Dependency Track.
- **DEP-002**: A política de severidade deve ser explícita quanto ao que bloqueia vs. o que apenas alerta. Para L1, o mínimo aceitável é bloqueio em severidade crítica; para L2/L3, severidade elevada ou superior.
- **DEP-004**: Esta proibição estende-se a submódulos Git com código de terceiros, vendor directories sem controlo de versão, e binários de terceiros versionados directamente.
- **DEP-006**: Os critérios de aprovação devem incluir verificação de última actualização do projecto, número de maintainers activos e presença em bases de dados de supply chain incidents (ex: OpenSSF Scorecard, Socket.dev).
- **DEP-008**: A automatização de actualizações deve ser configurada com cautela em ambientes de risco elevado: actualizações automáticas de dependências transitivas ou de componentes de segurança críticos devem sempre requerer revisão humana.
### Nota detalhada — DEP-011 {#dep-011}

Dependências AI/ML não se reduzem a pacotes via package manager — incluem **artefactos opacos** com superfície de ataque distinta. (1) **Modelos**: incluir hash SHA-256 do artefacto, model registry source (HuggingFace, Anthropic, OpenAI), e versão (ex: `claude-sonnet-4-6@sha:…`); ataque típico é AI Supply Chain Rug Pull (`AML.T0109`) — modelo legítimo substituído por variante maliciosa via update. (2) **Datasets**: rastrear fonte, data de obtenção, hash; ataque típico é Publish Poisoned Datasets (`AML.T0019`) — datasets públicos contaminados. (3) **MCP servers e tools**: ataque típico é AI Agent Tool Poisoning (`AML.T0110`) — MCP tool legítimo comprometido para injectar contexto malicioso quando invocado pelo agente. (4) **Embedded prompts**: system prompts e RAG templates são código operacional — alterações exigem PR review como qualquer outra dependência de comportamento. A análise de threat modeling associada vê Cap. 03 §AI/ML; controlos arquitectónicos para isolamento de agentic tool invocation vêm definidos em Cap. 04 [ARC-014](../../arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-014).
### Nota detalhada — DEP-012 {#dep-012}

O AI BOM é a materialização do DEP-011 num **formato standardizado e portável**. Preferimos CycloneDX 1.6 com a extensão `ml-bom` (publicada em 2024) porque preserva a estrutura do SBOM principal (DEP-001) e adiciona campos específicos para componentes AI (modelos, datasets, considerações). Esquemas alternativos (formato proprietário do provider, `ML-BOM` próprio) são aceitáveis desde que cubram os mesmos campos e sejam consumíveis pelo *pipeline* de governança da organização.
### Nota detalhada — DEP-013 {#dep-013}

A regra "sem `latest`" aplica-se literalmente — ranges *semver* (`^4.x`, `>=4.0`), *aliases* dinâmicos e *channels* que se actualizam silenciosamente são fonte directa do incidente classe `AML.T0109` (AI Supply Chain Rug Pull). A política operacional é simétrica àquela que aplicamos a dependências de código (DEP-003): versão fixa e auditável. A diferença é que com modelos AI, a *mesma versão* pode comportar-se diferentemente conforme *fine-tunes* incrementais que o provider possa aplicar — daí a necessidade de cruzamento com eval suite (Cap. 10 §C5) sempre que a versão muda.
### Nota detalhada — DEP-014 {#dep-014}

Aprovar um provider AI não é apenas uma decisão técnica — envolve cláusulas contratuais que o `grc` / `compliance` valida (data retention, training opt-out, localização, audit rights, AI Act Art. 53/55 quando aplicável). A lista aprovada vive em VCS no repositório de governança da organização, junto com a lista de registries DEP-005. Cross-link operacional: Policy 33 (Contratação Segura) §Anexo AI Providers; Cap. 14 US "Contratação de provedores AI".

---

> Para inventário e geração de SBOM, consultar [Inventário de Dependências e SBOM](./inventario-sbom).
> Para análise de vulnerabilidades e processo de SCA, consultar [Análise SCA](./analise-sca).
> Para governação de bibliotecas de terceiros e processo de aprovação, consultar [Governança de Bibliotecas](./governanca-libs-terceiros).
> Para políticas de actualização e SLAs, consultar [Política de Actualizações](./politica-atualizacoes).
> Para gestão de excepções e aceitação de risco, consultar [Excepções e Aceitação de Risco](./excecoes-e-aceitacao-risco).
