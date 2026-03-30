---
id: catalogo-requisitos-iac
title: Catálogo de Requisitos de Infraestrutura como Código
description: Catálogo canónico de requisitos de segurança para projectos IaC (IAC-001 a IAC-013), organizados por nível de risco, com critérios de aceitação para governação de repositórios, pipelines, estado, módulos e drift de configuração.
requirement_class: dominio
tags: [tipo:catalogo, classe:dominio, tema:iac, IAC, rastreabilidade, L1, L2, L3, terraform, state-management, drift, supply-chain, auditoria]
sidebar_position: 8
---

<!--template: sbdtoe-addon -->

# Catálogo de Requisitos de Infraestrutura como Código

## Âmbito: o projecto IaC como produto de software

Este catálogo define **requisitos de segurança aplicáveis ao projecto IaC em si** - tratando o código de infraestrutura como um produto de software com riscos próprios, que deve ser governado, validado e auditado com o mesmo rigor que qualquer aplicação.

Os requisitos cobrem: gestão de estado remoto, segregação de ambientes, validações automáticas em pipeline, rastreabilidade de módulos e sua proveniência, versionamento de artefactos, gestão segura de segredos, detecção de drift e revisão periódica de templates.

Para o mapeamento completo de todos os catálogos de requisitos do SbD-ToE por domínio técnico, prefixo canónico e responsável, consultar [Cap. 02 - Mapeamento de Catálogos](/sbd-toe/sbd-manual/requisitos-seguranca/addon/lista-requisitos-base#mapeamento-de-catalogos).

> **Nota:** Estes requisitos governam **como a infraestrutura é definida e gerida como código** - não as propriedades de segurança da infraestrutura provisionada em si (configurações de rede, permissões IAM, encriptação de buckets, etc.), que são resultado do que o código IaC define e estão sujeitas às políticas de cada organização.

> **Sobre a curadoria:** Consolidado a partir de NIST SSDF, SLSA (Supply Chain Levels for Software Artefacts), CIS Benchmarks para IaC, OWASP SAMM e boas práticas de Terraform, Pulumi e plataformas cloud. Deve ser adaptado ao contexto e às ferramentas IaC utilizadas pela organização.

Para instanciação em projecto e nomenclatura operacional (`SEC-Lx-IAC-CODIGO`), ver [Taxonomia e Rastreabilidade](/sbd-toe/sbd-manual/requisitos-seguranca/addon/taxonomia-rastreabilidade).

---

## Convenções

| Símbolo | Significado |
|---------|-------------|
| ✔ | Requisito obrigatório para este nível |
| - | Não aplicável ou não obrigatório a este nível |

Os níveis são cumulativos: L3 inclui todos os requisitos de L1 e L2; L2 inclui todos os de L1.

---

## Catálogo IAC - Infraestrutura como Código

Requisitos que garantem que o projecto IaC é desenvolvido, versionado, validado e operado com controlos de segurança proporcionais ao risco da infraestrutura que gere.

| ID | Nome | L1 | L2 | L3 | Critério de aceitação |
|----|------|:--:|:--:|:--:|----------------------|
| IAC-001 | Backend remoto autenticado com locking activo | - | ✔ | ✔ | `backend` configurado com autenticação e locking; tentativa de `apply` concorrente resulta em bloqueio; logs de lock disponíveis. |
| IAC-002 | Ambientes segregados e versionados | ✔ | ✔ | ✔ | Configurações de `dev`, `staging` e `prod` distintas, versionadas em directórios ou workspaces separados; deploy não pode cruzar ambientes sem aprovação explícita. |
| IAC-003 | Validações automáticas obrigatórias em pipeline | ✔ | ✔ | ✔ | Pipeline com etapas de lint, análise de segurança (ex: tfsec, checkov) e validação de política; falha em qualquer etapa bloqueia o `apply`. |
| IAC-004 | Módulos reutilizados com origem confiável e versão imutável | - | ✔ | ✔ | Referências de módulos com versão semântica fixa ou hash; ausência de referências sem versão (`latest`, `master`, `HEAD`); origem documentada. |
| IAC-005 | Histórico completo com versionamento, tags e releases | ✔ | ✔ | ✔ | Repositório Git com histórico intacto, tags semânticas por release e notas de versão; sem squash obrigatório em branches principais. |
| IAC-006 | Convenções formais de naming, tagging e layout | - | ✔ | ✔ | Linter ou política automática que valida convenções de nomes e tags obrigatórias; recursos sem tags de identificação obrigatórias são rejeitados. |
| IAC-007 | Plan rastreável e aprovado antes de qualquer apply | - | ✔ | ✔ | PR com output de `plan` anexado e revisível; aprovação registada antes de `apply`; evidência de que o `apply` ocorreu após aprovação e sobre o mesmo `plan`. |
| IAC-008 | Rastreabilidade ficheiro → recurso → ambiente | - | ✔ | ✔ | Possível identificar, para qualquer recurso provisionado, o ficheiro IaC de origem, o ambiente e o pipeline que o criou; evidência disponível em auditoria. |
| IAC-009 | Enforcement automático de políticas em pipeline | - | - | ✔ | Regras de política (ex: OPA/Rego, Sentinel) activas no pipeline; logs de bloqueio por violação de política disponíveis; política versionada com o código. |
| IAC-010 | Artefactos de plan e manifests versionados e com hash | - | ✔ | ✔ | Plans e manifests armazenados com hash verificável; integridade confirmada antes do `apply`; artefactos não reutilizáveis entre ambientes distintos. |
| IAC-011 | Gestão segura de segredos - proibição de hardcoding | ✔ | ✔ | ✔ | Ausência de segredos em código, variáveis de ambiente não protegidas ou ficheiros versionados; integração com cofre de segredos (Vault, KMS, OIDC) verificável; scan automatizado de segredos no pipeline. |
| IAC-012 | Detecção automatizada de drift entre IaC e estado real | - | ✔ | ✔ | Relatórios periódicos de drift disponíveis; alertas activos para divergência entre estado definido em IaC e estado real da infraestrutura. |
| IAC-013 | Revisão periódica formal de módulos e templates | - | - | ✔ | Registos de revisão com data, responsável e findings; ciclo de revisão definido e evidência de cumprimento; módulos obsoletos ou com vulnerabilidades conhecidas retirados de serviço. |

---

## Notas explicativas

- **IAC-001**: Aplica-se sempre que exista colaboração entre múltiplos engenheiros, pipelines partilhados ou mais de um ambiente gerido pelo mesmo estado. Em contextos de operador único e pipeline isolado, o locking pode ser dispensado com justificação documentada.
- **IAC-004**: Qualquer dependência de módulo externo deve ser tratada como código não confiável por origem até validação explícita. Módulos internos partilhados estão também sujeitos a este requisito.
- **IAC-007**: Materializa o princípio de *change control* técnico em IaC: nenhum `apply` deve ocorrer sem rastreabilidade directa a uma aprovação humana sobre um `plan` verificável.
- **IAC-009**: Requisito estrutural para ambientes de risco elevado (L3) onde a dependência de revisão manual é insuficiente para garantir cobertura contínua de política.
- **IAC-011**: O scan de segredos deve cobrir código, histórico Git e variáveis de pipeline; ferramentas de referência: TruffleHog, GitLeaks, detect-secrets.
- **IAC-012**: Drift é tratado como uma falha de segurança, não como excepção operacional - infraestrutura que diverge do estado definido em IaC representa risco não auditável.

---

> Para princípios de Security by Design aplicados especificamente a projectos IaC, consultar [Princípios SbD para IaC](./principios-sbd-iac).
> Para validações e checks automáticos recomendados, consultar [Validações e Checks](./validacoes-e-checks).
> Para gestão de excepções a estes requisitos, consultar [Gestão de Excepções](./gestao-excecoes).
> Para rastreabilidade e tagging de recursos, consultar [Rastreabilidade e Tags](./rastreabilidade-e-tags).
