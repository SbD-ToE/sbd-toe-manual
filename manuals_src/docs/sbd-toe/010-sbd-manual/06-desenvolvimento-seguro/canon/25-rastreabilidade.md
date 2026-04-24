---
id: rastreabilidade
title: "Rastreabilidade — Capítulo 06: Desenvolvimento Seguro"
description: Rastreabilidade das práticas de desenvolvimento seguro face a frameworks normativos com pilot formal
tags: [rastreabilidade, desenvolvimento, codificacao, ssdf, asvs, cis, nis2]
sidebar_position: 25

---


> **Método:** Ver [Metodologia de Validação de Claims](../../00-fundamentos/canon/26-metodologia-validacao-claims.md) para a baseline empírica dos autores, validação por índices semânticos, ontology backtrace e comparação com fontes externas.

# Rastreabilidade — Capítulo 06: Desenvolvimento Seguro

Este capítulo define práticas de **codificação segura** — guidelines, linters, revisão de código, controlo automático e humano — integradas no ciclo de desenvolvimento.

---

## Camada AppSec Core

| Slice AppSec Core | Âncora principal | Relevância |
|-------------------|-----------------|-----------|
| ACO-IVF — Input Validation, Safe Parsing & Controlled Failure | Primária | Validação de entrada, injeção, falha segura, gestão de erros — VAL + ERR requirements |
| ACO-SPC — Secret Handling, Protected Configuration & Operational Identities | Primária (bounded) | Segredos, parâmetros sensíveis, material criptográfico e configuração protegida quando esses controlos são implementados, revistos e evidenciados no ciclo de desenvolvimento |
| ACO-SCBI — Supply Chain & Build Integrity | Secundária | Segurança de dependências, proveniência do código |

> **Nota de mapeamento:** ACO-IVF continua a ser o principal espaço de normalização deste capítulo via `CTRL-code-integrity-desenvolvimento-seguro-e-validacao-de-codigo` para VAL + ERR. Na Wave 1 autorizada, `ACO-SPC` é ativado de forma **bounded** para `asvs_v5_0_0` e `pci_dss_v4_0_1`, com carry-forward caveated para `asvs_v4_0_2`, `hipaa_security_rule` e `nist_sp800_53_rev5`, apenas em temas de segredos, configuração protegida, transporte de dados sensíveis e identidades operacionais tratadas no desenvolvimento. `ACO-SCBI` permanece restrito a dependências e proveniência. Rows corrigidas para outros slices, `SP800-53-SC-42.3`, sinais candidate-only e material non-core fora de `03` e `13` não ganham autoridade adicional neste capítulo.

---

## Frameworks normativos — cobertura verificada

> Inclui apenas frameworks com pilot formal publicado no ExternalSourcesInventory.  
> Coluna **Fonte verificada** indica o `document_role` e `normative_weight` do unit que confirma a cobertura.

| Framework | Requisito / Prática | Cobertura | Fonte verificada | Nota |
|-----------|--------------------|-----------|----|---|
| SSDF PW.5 | Create Source Code with Secure Coding Techniques | ✅ Explícito | addon (medium): Boas Práticas + Guidelines de Equipa + Linters | Guidelines, linters e práticas proibidas |
| SSDF PW.7 | Review and/or Analyze Human-Readable Code | ✅ Explícito | aplicacao_lifecycle (strong): US-02 Revisão de Código Segura | Revisão estruturada com critérios e rastreabilidade |
| ASVS injection_and_sanitization | Injection prevention | ✅ Explícito | addon (medium): Boas Práticas; req VAL-004 via ACO-IVF-003 | Práticas proibidas + sanitização explícita |
| ASVS input_contract_validation | Input contract validation | ✅ Explícito | requirements_catalog (strong): VAL-001–003 via ACO-IVF-001/002 | Whitelist, schema, validação de entrada |
| ASVS validation_before_internal_use | Validation before use | ✅ Explícito | requirements_catalog (strong): VAL-005 via ACO-IVF-004 | Validação antes de uso interno |
| ASVS secure_coding_discipline | Generic secure coding discipline | ✅ Semântico | addon (medium): Boas Práticas de Escrita; aplicacao_lifecycle (strong): US-13 Anti-patterns | Claim gap resolvido — conteúdo existe em addons |
| ASVS controlled_failure_and_non_revealing_errors | Controlled failure | ✅ Semântico | requirements_catalog (strong): ERR-001–004 via ACO-IVF-005; addon (medium): Boas Práticas | Falha segura e erros não reveladores |
| ASVS error_handling_and_sensitive_logging_hygiene | Error handling hygiene | ✅ Semântico | requirements_catalog (strong): ERR-005–007 via ACO-IVF-006 | Gestão centralizada, logs pseudonimizados |
| ASVS encoding_architecture | Encoding architecture | ⚠️ Parcial | addon (medium): Boas Práticas (cobertura implícita) | Sem secção dedicada a encoding; coberto parcialmente |
| ASVS file_download_content_serving | File download & content serving | ⚠️ Parcial | Sem unit dedicado em Cap. 06 | Mais relevante em Cap. 10 (testes) |
| ASVS secure_coding_architecture_documentation | Secure coding documentation | ✅ Semântico | addon (medium): Anotações e Evidência + Guidelines de Equipa | Documentação de validações e práticas de equipa |
| CIS-16 | Application Software Security | ✅ Explícito | addon (medium): Linters; aplicacao_lifecycle (strong): US-04 CI/CD, US-12 pre-commit | Linters, SAST, validações locais obrigatórias |
| NIS2 | Práticas seguras de desenvolvimento | ✅ Explícito | overlay regulatório publicado | — |
| ASVS v4 | ASVS4-REQ-V5.1.2 | ✅ Semântico | requirements_catalog (strong): Catálogo de Requisitos de Desenvolvimento Seguro | Atribuição massiva de parâmetros é travada por contracts e campos permitidos |
| ASVS v4 | ASVS4-REQ-V5.1.4 | ✅ Semântico | requirements_catalog (strong): Catálogo de Requisitos de Desenvolvimento Seguro | Dados estruturados são validados por schema, tipo, tamanho e padrão |
| ASVS v4 | ASVS4-REQ-V5.2.2 | ✅ Semântico | requirements_catalog (strong): Catálogo de Requisitos de Desenvolvimento Seguro | Input livre passa por sanitização antes de chegar a funções críticas |
| ASVS v4 | ASVS4-REQ-V5.3.9 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Desenvolvimento Seguro | Inclusão de ficheiros inseguros é mitigada por validação, sem secção dedicada |
| ASVS v4 | ASVS4-REQ-V5.4.2 | ✅ Semântico | requirements_catalog (strong): Catálogo de Requisitos de Desenvolvimento Seguro | Funções perigosas não devem receber input hostil nem format strings dinâmicas |
| ASVS v4 | ASVS4-REQ-V5.5.4 | ✅ Semântico | requirements_catalog (strong): Catálogo de Requisitos de Desenvolvimento Seguro | Parsing JSON seguro exclui `eval` e privilegia APIs de parsing dedicadas |
| ASVS v4 | ASVS4-REQ-V11.1.4 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Desenvolvimento Seguro | Anti-automation existe por adjacência, sem surface específico de abuso lógico |
| ASVS v4 | ASVS4-REQ-V12.2.1 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Desenvolvimento Seguro | Tipo real de ficheiros não confiáveis é validado, mas o capítulo não isola uploads |
| ASVS v4 | ASVS4-REQ-V12.3.4 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Desenvolvimento Seguro | Nomes de ficheiro controlados pelo utilizador ainda pedem guidance mais explícita |
| ASVS v4 | ASVS4-REQ-V12.3.6 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Desenvolvimento Seguro | Código ou bibliotecas de origem não confiável ficam mais cobertos em dependências |
| ASVS v4 | ASVS4-REQ-V12.5.2 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Desenvolvimento Seguro | Conteúdo carregado não deveria executar no cliente, mas falta controlo dedicado |
| ASVS v4 | ASVS4-REQ-V12.6.1 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Desenvolvimento Seguro | Allow-lists de destinos e recursos aparecem por adjacência, não por regra própria |
| ASVS v5 | ASVS-REQ-V15.3.1 — V15.3.1 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Desenvolvimento Seguro | Redução do objeto devolvido pede controlo mais fino do que o chapter surface atual |
| ASVS v5 | ASVS-REQ-V15.3.2 — V15.3.2 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Desenvolvimento Seguro | Redirects em chamadas backend ainda não têm regra canónica publicada |
| ASVS v5 | ASVS-REQ-V15.3.3 — V15.3.3 | ✅ Semântico | requirements_catalog (strong): Catálogo de Requisitos de Desenvolvimento Seguro | Campos permitidos por ação bloqueiam mass assignment indesejado |
| ASVS v5 | ASVS-REQ-V15.3.4 — V15.3.4 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Desenvolvimento Seguro | IP de origem confiável para logging e rate limiting não está isolado no capítulo |
| ASVS v5 | ASVS-REQ-V15.3.5 — V15.3.5 | ✅ Semântico | requirements_catalog (strong): Catálogo de Requisitos de Desenvolvimento Seguro | Tipos e comparações estritas seguem a disciplina de validação por schema |
| ASVS v5 | ASVS-REQ-V15.3.6 — V15.3.6 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Desenvolvimento Seguro | Prototype pollution continua implícita nas práticas seguras, sem guidance próprio |
| ASVS v5 | ASVS-REQ-V15.3.7 — V15.3.7 | ✅ Semântico | requirements_catalog (strong): Catálogo de Requisitos de Desenvolvimento Seguro | Poluição de parâmetros é reduzida por validação forte e origem tratada como input |
| ASVS v5 | ASVS-REQ-V16.5.2 — V16.5.2 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Desenvolvimento Seguro | Degradação segura perante falha externa é adjacente, mas não um padrão publicado aqui |
| ASVS v5 | ASVS-REQ-V16.5.3 — V16.5.3 | ✅ Semântico | requirements_catalog (strong): Catálogo de Requisitos de Desenvolvimento Seguro | Exceções não devem abrir caminho nem contornar validações de segurança |
| ASVS v5 | ASVS-REQ-V16.5.4 — V16.5.4 | ✅ Semântico | requirements_catalog (strong): Catálogo de Requisitos de Desenvolvimento Seguro | Handler de último recurso preserva disponibilidade e evidência de erro útil |
| CIS v8.1.2 | CIS-16.9 — Train Developers in Application Security Concepts and Secure Coding | ⚠️ Parcial | addon (medium): 🤖 Uso de GenIA no Desenvolvimento Seguro > 🌐 Para além do desenvolvimento: o papel da IA no Security by Design | Guidelines e curadoria de práticas apoiam treino contínuo, mas a formação estruturada fica mais explícita no Cap. 13 |
| CWE | CWE-212 — The product stores, transfers, or shares a resource that contains sensitive information, but it does not properly remove sensitive information from the resource before being made accessible to unauthorized actors | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Desenvolvimento Seguro | Recursos sensíveis passam por disciplina de validação e tratamento, mas o capítulo não isola remoção de metadados ou resíduos sensíveis |
| CWE | CWE-22 — The product uses external input to construct a pathname that is intended to identify a file or directory that is located underneath a restricted parent directory, but the product does not properly neutralize special elements within the pathname | ⚠️ Parcial | addon (medium): 🛠️ Validação de Código como Controlo de Risco de Processo > Código não é confiança - é input | Paths externos são tratados como input hostil, mas path traversal ainda não aparece como controlo canónico dedicado |
| CWE | CWE-41 — The product is vulnerable to file system contents disclosure through path equivalence | ⚠️ Parcial | legacy_canon (historical): Rastreabilidade — Capítulo 06: Desenvolvimento Seguro > Ligações com outros capítulos | Normalização e validação reduzem disclosure por equivalência de caminho, sem guidance próprio para este padrão |
| CWE | CWE-59 — The product attempts to access a file based on the filename, but it does not properly prevent that filename from identifying a link or shortcut that resolves to an unintended resource | ⚠️ Parcial | legacy_canon (historical): Rastreabilidade — Capítulo 06: Desenvolvimento Seguro > Ligações com outros capítulos | Acesso por nome de ficheiro é mitigado por validação, mas symlinks e atalhos ainda não estão cobertos de forma explícita |
| CWE | CWE-66 — The product does not handle or incorrectly handles a file name that identifies a "virtual" resource that is outside of the intended control sphere | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Desenvolvimento Seguro > Notas explicativas | Nomes virtuais e aliases recebem cobertura adjacente por contracts, mas sem secção própria sobre virtual path handling |
| CWE | CWE-73 — The product allows user input to control or influence paths or file names that are used in filesystem operations | ⚠️ Parcial | addon (medium): 🛠️ Validação de Código como Controlo de Risco de Processo > Código não é confiança - é input | Input do utilizador não deve controlar paths internos, mas a regra ainda não está publicada como requisito reutilizável |
| CWE | CWE-804 — The product uses a CAPTCHA challenge, but the challenge can be guessed or automatically recognized by a non-human actor | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Desenvolvimento Seguro | Há mitigação adjacente contra abuso automatizado, mas CAPTCHA robusto não é um padrão canónico deste capítulo |
| HIPAA | HIPAA-164-312c1 — Integrity | ⚠️ Parcial | legacy_canon (historical): Rastreabilidade — Capítulo 06: Desenvolvimento Seguro > Camada AppSec Core | Integridade lógica é reforçada por validação e revisão, mas o controlo HIPAA cobre alterações indevidas num âmbito mais largo do que este capítulo |
| MCP Official | MCP-AUTH-ERROR-HANDLING — Authorization errors and insufficient-scope responses map to controlled failure and bounded client-visible error behavior | ✅ Semântico | maturity (weak): 📈 Maturidade - Desenvolvimento Seguro > ✅ Conclusão | Erros de autorização e scope insuficiente já seguem o padrão de falha segura e resposta não reveladora deste capítulo |
| NIST SP800-53 | SP800-53-SI-9 | ✅ Semântico | requirements_catalog (strong): Catálogo de Requisitos de Desenvolvimento Seguro | Restrições de input seguem contracts, allow-lists e validação antes de uso interno |
| NIST SP800-53 | SP800-53-SI-16 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Desenvolvimento Seguro | Proteções contra execução não autorizada em memória aparecem por secure coding e hardening adjacente, sem controlo dedicado neste capítulo |
| NIST SP800-53 | SP800-53-SI-17 | ✅ Semântico | requirements_catalog (strong): Catálogo de Requisitos de Desenvolvimento Seguro | Procedimentos de fail-safe já se alinham com degradação segura e handlers de último recurso |
| OWASP MCP Secure Server | OWASP-MCP-DATA-VALIDATION — Strict schema validation, sanitization and safe handling have a clear landing in the validation and parsing controls of this chapter | ✅ Semântico | maturity (weak): 📈 Maturidade - Desenvolvimento Seguro > 🧱 SLSA - Build Validation & Provenance | Validação estrita por schema, sanitização e uso seguro de input já estão cobertos pelo catálogo VAL deste capítulo |
| OWASP MCP Top 10 | MCP10-2025 — Context injection/over-sharing → secret usage isolation | ⚠️ Parcial | aplicacao_lifecycle (strong): ⚙️ Aplicação no Ciclo de Vida - Desenvolvimento Seguro > 📖 User Stories reutilizáveis > US-07 - Governação e Curadoria de Guidelines | Curadoria de guidelines e constrangimentos para GenIA reduzem over-sharing, mas isolamento de segredos ainda não está isolado como regra canónica |
| PCI DSS | PCI-REQ-6 — Develop and Maintain Secure Systems and Software | ✅ Semântico | maturity (weak): 📈 Maturidade - Desenvolvimento Seguro > 🧱 OWASP DSOMM - Design & Development, Tooling, Metrics | O capítulo operacionaliza o Requirement 6 com guidelines, revisão de código, SAST, gates e gestão de exceções |
| PCI DSS | PCI-6.1.1 — All security policies and operational procedures | ✅ Semântico | addon (medium): 🤖 Uso de GenIA no Desenvolvimento Seguro > 🌐 Para além do desenvolvimento: o papel da IA no Security by Design | Políticas, guidelines e constrangimentos versionados garantem atualização e comunicação das práticas de desenvolvimento seguro |
| PCI DSS | PCI-6.1.2 — Roles and responsibilities for performing 6.1.2.a Examine documentation to verify that | ✅ Semântico | aplicacao_lifecycle (strong): ⚙️ Aplicação no Ciclo de Vida - Desenvolvimento Seguro > 👥 Quem executa cada ação | Papéis e responsabilidades do Requirement 6 estão explicitados na matriz de roles e nos gates G1-G3 |
| PCI DSS | PCI-6.2.1 — Bespoke and custom software are developed | ✅ Semântico | maturity (weak): 📈 Maturidade - Desenvolvimento Seguro > 🧱 OWASP DSOMM - Design & Development, Tooling, Metrics | Software custom é desenvolvido sob guidelines curadas, linters, SAST e revisão formal |
| PCI DSS | PCI-6.2.2 — Software development personnel working on 6.2.2.a Examine software dev | ⚠️ Parcial | maturity (weak): 📈 Maturidade - Desenvolvimento Seguro > 🧱 OWASP DSOMM - Design & Development, Tooling, Metrics | Práticas seguras e curadoria existem, mas a formação estruturada de developers fica mais explícita no Cap. 13 |
| PCI DSS | PCI-6.2.3 — Bespoke and custom software is reviewed 6.2.3.a Examine documented sof | ✅ Semântico | advanced (weak): 🧠 Recomendações Avançadas - Desenvolvimento Seguro > 1. ✅ Regras Semgrep customizadas | Revisão de código com checklist de segurança cobre a revisão formal exigida para software bespoke |
| PCI DSS | PCI-6.2.4 — Software engineering techniques or other | ✅ Semântico | aplicacao_lifecycle (strong): ⚙️ Aplicação no Ciclo de Vida - Desenvolvimento Seguro | Técnicas de engenharia segura são operacionalizadas por guidelines, linters, SAST e gates proporcionais |
| PCI DSS | PCI-6.3.1 — Security vulnerabilities are identified and 6.3.1.a Examine policies a | ✅ Semântico | addon (medium): 🤖 Uso de GenIA no Desenvolvimento Seguro > 🌐 Para além do desenvolvimento: o papel da IA no Security by Design | Vulnerabilidades são identificadas e tratadas com validações locais, SAST, SBOM e gate pré-release |
| PCI DSS | PCI-6.3.2 — An inventory of bespoke and custom software, 6.3.2.a Examine documenta | ⚠️ Parcial | advanced (weak): 🧠 Recomendações Avançadas - Desenvolvimento Seguro > 1. ✅ Regras Semgrep customizadas | Há artefactos e evidência de release, mas o capítulo não publica inventário dedicado de software bespoke |
| PCI DSS | PCI-6.3.3 — All system components are protected from 6.3.3.a Examine policies and | ⚠️ Parcial | intro (strong): Desenvolvimento Seguro > 📜 Políticas Organizacionais Relevantes | Patching e atualização aparecem na manutenção, mas a proteção contínua de todos os componentes é mais ampla do que este capítulo |
| PCI DSS | PCI-6.4.1 — For public-facing web applications, new threats 6.4.1 For public-facin | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Desenvolvimento Seguro > Catálogo DEV - Desenvolvimento Seguro | Novas ameaças para aplicações públicas são tratadas por guidelines e revisão, sem superfície específica de exposição web |
| PCI DSS | PCI-6.4.2 — For public-facing web applications, an 6.4.2 For public-facing web app | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Desenvolvimento Seguro > Catálogo DEV - Desenvolvimento Seguro | Revisão de código existe, mas a alternativa WAF e a proteção operacional ficam fora do foco deste capítulo |
| PCI DSS | PCI-6.4.3 — All payment page scripts that are loaded and 6.4.3.a Examine policies | ⚠️ Parcial | intro (strong): Desenvolvimento Seguro > 📜 Políticas Organizacionais Relevantes | Governança de scripts de página de pagamento não está isolada como padrão próprio no capítulo de desenvolvimento |
| PCI DSS | PCI-6.5.1 — Changes to all system components in the 6.5.1.a Examine documented cha | ⚠️ Parcial | addon (medium): 🛠️ Validação de Código como Controlo de Risco de Processo | Mudanças passam por gates, checklist e gestão de exceções, mas o controlo de mudança em produção é mais lato do que o capítulo |
| PCI DSS | PCI-6.5.2 — Upon completion of a significant change, all | ✅ Semântico | aplicacao_lifecycle (strong): ⚙️ Aplicação no Ciclo de Vida - Desenvolvimento Seguro > 📦 Artefactos Esperados | O gate pré-release agrega evidências e revalida requisitos aplicáveis após mudanças significativas |
| PCI DSS | PCI-6.5.3 — Pre-production environments are separated 6.5.3.a Examine policies and | ⚠️ Parcial | intro (strong): Desenvolvimento Seguro > 📜 Políticas Organizacionais Relevantes | Separação entre pré-produção e produção é tratada por adjacência no SDLC, sem controlo dedicado aqui |
| PCI DSS | PCI-6.5.4 — Roles and functions are separated between 6.5.4.a Examine policies and | ⚠️ Parcial | aplicacao_lifecycle (strong): ⚙️ Aplicação no Ciclo de Vida - Desenvolvimento Seguro > 👥 Quem executa cada ação | Separação de funções entre pré-produção e produção é mais forte em governança e deploy do que neste capítulo |
| PCI DSS | PCI-6.5.5 — Live PANs are not used in pre-production 6.5.5.a Examine policies and | ⚠️ Parcial | intro (strong): Desenvolvimento Seguro > ⏱️ Quando aplicar | A proibição de PAN real em pré-produção não está explicitada como requisito canónico deste capítulo |
| PCI DSS | PCI-6.5.6 — Test data and test accounts are removed from 6.5.6.a Examine policies | ⚠️ Parcial | advanced (weak): 🧠 Recomendações Avançadas - Desenvolvimento Seguro > 3. ✅ Análise de fluxo de dados (Data Flow Analysis) | Higiene de dados e contas de teste antes da produção é adjacente ao gate final, mas sem regra publicada própria |

**Legenda:** ✅ Explícito · ✅ Semântico · ⚠️ Parcial · 🔧 Reparação · 🔴 Gap

> **Metodologia:** Cobertura verificada contra `ontology_discovery_units.jsonl` (4139 units, manual completo). "Explícito" = unit de normative_weight strong/medium com heading_path directo. "Semântico" = conteúdo confirmado em addon ou via mapeamento de requisito canónico. "Parcial" = sem unit dedicado no capítulo.

---

## Maturidade — referência separada

A leitura de maturidade deste capítulo é tratada em [achievable-maturity.md](../achievable-maturity.md).

Neste documento, os modelos de maturidade surgem apenas como contexto editorial complementar. A sua normalização formal é apresentada no documento dedicado do capítulo.

---

## Ligações com outros capítulos

- **Cap. 01** — exigência proporcional de práticas com base no nível L1–L3
- **Cap. 02** — requisitos VAL + ERR implementados e verificados neste capítulo; CFG-001–007 como baseline de configuração segura
- **Cap. 05** — componentes usados no desenvolvimento validados via SCA
- **Cap. 07** — práticas de codificação integradas como passos automatizados no pipeline
- **Cap. 10** — validação final com testes; file_download_content_serving mais coberto aqui
