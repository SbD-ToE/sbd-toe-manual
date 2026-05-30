---
id: rastreabilidade-controlo
title: Modelo de Rastreabilidade entre Riscos, Requisitos e Controlos
description: Como construir e manter uma matriz de rastreabilidade que liga riscos identificados, requisitos canónicos, tags operacionais de projeto, controlos técnicos e evidência auditável.
tags: [tipo:modelo, tema:rastreabilidade, requisitos, controlos, evidencia, ALM, auditoria]
---

<!--template: sbdtoe-addon -->

# Modelo de Rastreabilidade entre Riscos, Requisitos e Controlos

## Objetivo

Ao longo do ciclo de vida do software, garantir que um requisito de segurança foi efectivamente implementado exige mais do que a sua definição - exige que a ligação entre risco, requisito, controlo técnico e evidência seja explícita, rastreável e auditável.

Este modelo descreve como construir essa cadeia de rastreabilidade, articulando os dois sistemas de identificação do SbD-ToE:

- O **ID canónico** (`AUT-001`, `LOG-003`) - referência normativa estável proveniente do catálogo;
- A **tag operacional** (`SEC-L2-AUT-MFA`) - instância contextualizada adoptada pelo projecto.

A distinção e a relação entre ambos estão detalhadas em [Taxonomia e Rastreabilidade](./taxonomia-rastreabilidade).

Este modelo apoia:

- A verificação sistemática da cobertura de segurança ao longo do ciclo de vida;
- A preparação de auditorias internas, externas e regulatórias;
- A integração com ferramentas ALM (Jira, ADO, Confluence, GitHub), gestão de risco e conformidade.

---

## Estrutura da Matriz de Rastreabilidade

Cada linha da matriz representa a ligação directa entre um risco identificado e o requisito de segurança que o endereça, com o respectivo controlo, método de validação e evidência esperada.

### Colunas recomendadas

| Coluna | Conteúdo | Exemplo |
|--------|----------|---------|
| **Risco** | Identificador e descrição sumária do risco (proveniente da análise de ameaças) | `RISK-AUTH-01` - acesso não autorizado por ausência de MFA |
| **ID Canónico** | Referência normativa do catálogo SbD-ToE | `AUT-001` |
| **Tag Operacional** | Instanciação do requisito no contexto do projecto | `SEC-L2-AUT-MFA` |
| **Tipo de Controlo** | Classificação do controlo: `Preventivo`, `Detetivo` ou `Corretivo` | `Preventivo` |
| **Validação** | Método objectivo de verificação | Teste automatizado em CI/CD |
| **Evidência** | Artefacto auditável produzido | Log de falha de autenticação sem MFA |

---

## Exemplo de Matriz

O seguinte é um exemplo de instanciação do catálogo de requisitos a um projecto concreto. O catálogo completo pode ser consultado em [Lista de Requisitos Base](./lista-requisitos-base).

| Risco | ID Canónico | Tag Operacional | Tipo de Controlo | Validação | Evidência |
|-------|-------------|-----------------|------------------|-----------|-----------|
| Acesso não autorizado por ausência de 2.º factor | `AUT-001` | `SEC-L2-AUT-MFA` | Preventivo | Teste funcional - login sem MFA falhado | Log de autenticação falhada; captura de ecrã |
| Registo insuficiente para resposta a incidentes | `LOG-002` | `SEC-L2-LOG-DETALHE` | Detetivo | Revisão de logs em runtime | Exemplo de log com campos quem/quando/o quê/onde |
| Injecção SQL por ausência de validação de input | `VAL-004` | `SEC-L2-VAL-SQLI` | Preventivo | Testes SAST + teste funcional com payload | Relatório de scanner; código com prepared statements |
| Passwords armazenadas em claro | `AUT-006` | `SEC-L1-AUT-PLAIN` | Preventivo | Auditoria de configuração + scan | Evidência de hashing; ausência de credenciais em texto claro |

---

## Exemplos por Domínio Técnico

| Domínio | ID Canónico | Tag Operacional (exemplo L2) | Tipo de Controlo | Validação | Evidência |
|---------|-------------|------------------------------|------------------|-----------|-----------|
| Autenticação | `AUT-005` | `SEC-L2-AUT-IDLE` | Preventivo | Teste de timeout por inactividade | Log de sessão expirada; configuração do servidor |
| Controlo de Acesso | `ACC-002` | `SEC-L2-ACC-LEASTPRIV` | Preventivo | Revisão de roles + teste com utilizador restrito | Matriz de permissões; log de acesso negado |
| Logging | `LOG-003` | `SEC-L2-LOG-INTEGRIDADE` | Detetivo | Tentativa de alteração de log; verificação de permissões | Evidência de protecção (read-only, syslog remoto, WORM) |
| Gestão de Erros | `ERR-001` | `SEC-L1-ERR-EXPOSICAO` | Preventivo | Induzir erro; verificar resposta ao cliente | Mensagem genérica no cliente; stack trace apenas em log interno |
| Configuração Segura | `CFG-003` | `SEC-L1-CFG-HARDCODE` | Preventivo | Análise estática + revisão do repositório | Ausência de segredos no código fonte; uso de cofre |
| Dependências e SDKs | `API-006` | `SEC-L2-API-SDK` | Preventivo/Corretivo | Scan SCA; verificação de SBOM | SBOM gerado; relatório de dependências auditado |
| Dados sensíveis | `ENC-002` | `SEC-L2-ENC-REST` | Preventivo | Revisão de configuração de base de dados e storage | Screenshot de políticas de encriptação; output de KMS/Vault |
| Comunicação segura | `INT-003` | `SEC-L1-INT-TLS` | Preventivo | Teste de TLS; scanner de certificados | TLS 1.2+ activo; certificado válido; `Strict-Transport-Security` |

---

## Como aplicar este modelo

- Cada linha representa a ligação entre um **risco identificado** e o **requisito canónico** que o endereça;
- A **tag operacional** é o identificador que transita para o backlog, o código e o pipeline - é ela que torna o requisito rastreável ao artefacto de ciclo de vida;
- O **tipo de controlo** classifica a natureza da medida: `Preventivo` (impede o incidente), `Detetivo` (detecta quando ocorre) ou `Corretivo` (mitiga as consequências);
- A **validação** deve ser objectiva e reproduzível - teste automatizado, análise estática, revisão manual documentada;
- A **evidência** é o artefacto que comprova, num contexto de auditoria, que o controlo está activo e efectivo.

---

## Organização recomendada por projecto

Cada projecto deve manter a sua própria matriz de rastreabilidade, organizada por:

1. **Cabeçalho** - identificação da aplicação, nível de risco (L1/L2/L3) e data de revisão;
2. **Mapeamento de riscos** - proveniente da análise de ameaças (threat modeling);
3. **Tabela rastreável** - com os campos descritos acima;
4. **Referência cruzada** ao [Catálogo Base de Requisitos](./lista-requisitos-base) e ao [Plano de Validação](./validacao-requisitos);
5. **Apontadores para evidência** - directórios, commits, screenshots, relatórios de pipeline.

**Formatos sugeridos:**

- `.md` versionado em Git - para rastreabilidade nativa no repositório;
- `.csv` / `.xlsx` - para exportação e análise rápida;
- Campos personalizados em Jira, ADO, Confluence ou ferramentas ALM equivalentes.

---

## Integração no ciclo de vida

A matriz deve ser revisitada:

- Em **revisões de requisitos** no início de cada ciclo;
- Durante **gates de release** e processos de go/no-go;
- Como suporte à **aceitação formal de risco** e documentação de excepções;
- Em checkpoints de auditoria - ISO 27001, PCI-DSS, DORA, ou equivalentes.

---

## Ferramentas de suporte

| Finalidade | Ferramenta sugerida |
|------------|---------------------|
| Versionamento leve | Git + Markdown |
| Análise e filtros | Excel / CSV |
| Integração ALM | Jira, Azure DevOps, GitHub Issues |
| Análise estática (SAST) | SonarQube, Semgrep, CodeQL |
| Teste dinâmico (DAST) | OWASP ZAP, Burp Suite |
| Análise de dependências (SCA) | Trivy, Snyk, Dependabot |
| Gestão de segredos | HashiCorp Vault, AWS Secrets Manager, Azure Key Vault |
| Centralização de logs / alertas | SIEM (ELK Stack, Splunk, Microsoft Sentinel) |

---

## Boas práticas

- Manter **uma matriz por aplicação ou sistema crítico**, não uma única matriz global;
- Usar a matriz como **trilho de auditoria interno** - actualizá-la em cada release;
- **Versionar todas as alterações** à matriz e à evidência associada;
- Referenciar sempre o **ID canónico** (`AUT-001`) e a **tag operacional** (`SEC-L2-AUT-MFA`) - o primeiro para rastreabilidade normativa, o segundo para rastreabilidade operacional;
- Documentar **excepções** com justificação e aprovação formal; ver [Gestão de Excepções](./gestao-excecoes).

---

> Para a lista completa dos requisitos canónicos com critérios de aceitação por domínio, consultar o [Catálogo Base de Requisitos](./lista-requisitos-base).
> Para os métodos de validação recomendados e evidências esperadas por domínio, consultar o [Plano de Validação de Requisitos](./validacao-requisitos).
