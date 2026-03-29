---
id: catalogo-requisitos-cicd
title: Catálogo de Requisitos de CI/CD Seguro
description: Catálogo canónico de requisitos de segurança para pipelines de integração e entrega contínua (CIC-001 a CIC-010), com aplicabilidade por nível de risco e critérios de aceitação para design de pipelines, gestão de segredos, isolamento de runners, integridade de artefactos e gates de segurança.
requirement_class: dominio
tags: [tipo:catalogo, classe:dominio, tema:cicd, CIC, pipeline, rastreabilidade, L1, L2, L3, runners, segredos, proveniencia, gates, auditoria]
sidebar_position: 0
---

<!--template: sbdtoe-addon -->

# Catálogo de Requisitos de CI/CD Seguro

## Âmbito: o pipeline como produto de engenharia com risco próprio

Este catálogo cobre **requisitos de segurança aplicáveis ao design, operação e auditoria de pipelines de CI/CD** — tratando o pipeline como um produto de engenharia crítico que, se comprometido, compromete todo o software que por ele transita.

Os pipelines são hoje a fronteira onde confluem código, credenciais, artefactos e decisões de promoção. Um pipeline inseguro não é apenas um risco de processo: é um vector de ataque sobre toda a cadeia de entrega. Estes requisitos estabelecem os controlos mínimos para que o pipeline seja **íntegro, rastreável, auditável e resistente a manipulação**.

Para o mapeamento completo de todos os catálogos de requisitos do SbD-ToE por domínio técnico, prefixo canónico e responsável, consultar [Cap. 02 — Mapeamento de Catálogos](/sbd-toe/sbd-manual/requisitos-seguranca/addon/lista-requisitos-base#mapeamento-de-catalogos).

> **Sobre a curadoria:** Consolidado a partir de OSC&R (CI/CD Attack Framework), CISA Top 10 CI/CD Security Risks, SLSA (Supply Chain Levels for Software Artefacts), NIST SSDF (PW.5, PW.6), OWASP Top 10 CI/CD Security Risks e práticas estabelecidas para GitHub Actions, GitLab CI, Azure DevOps e Jenkins. Deve ser adaptado à plataforma CI/CD em uso e revisto com cada ciclo de arquitectura de pipeline.

Para instanciação em projecto e nomenclatura operacional (`SEC-Lx-CIC-CODIGO`), ver [Taxonomia e Rastreabilidade](/sbd-toe/sbd-manual/requisitos-seguranca/addon/taxonomia-rastreabilidade).

---

## Convenções

| Símbolo | Significado |
|---------|-------------|
| ✔ | Requisito obrigatório para este nível |
| — | Não aplicável ou não obrigatório a este nível |

Os níveis são cumulativos: L3 inclui todos os requisitos de L1 e L2; L2 inclui todos os de L1.

---

## Catálogo CIC — CI/CD Seguro

Requisitos que garantem que o pipeline de integração e entrega é concebido, operado e auditado com controlos proporcionais ao risco do software que processa.

| ID | Nome | L1 | L2 | L3 | Critério de aceitação |
|----|------|:--:|:--:|:--:|----------------------|
| CIC-001 | Pipelines como código, versionados e sujeitos a revisão | ✔ | ✔ | ✔ | Definição de pipeline em ficheiros versionados no repositório (YAML, HCL, etc.); alterações sujeitas a pull request com revisão; sem pipelines geridos manualmente fora do controlo de versão. |
| CIC-002 | Triggers controlados e restritos a fontes autorizadas | ✔ | ✔ | ✔ | Execuções desencadeadas apenas por eventos de fontes autorizadas (branches protegidos, tags assinadas, merges aprovados); execuções originadas em forks externos desactivadas ou mediadas por aprovação manual. |
| CIC-003 | Gestão segura de segredos no pipeline | ✔ | ✔ | ✔ | Segredos injectados via cofre ou variáveis de ambiente protegidas pela plataforma; ausência de segredos em YAML de pipeline, logs ou ficheiros versionados; mascaramento de valores sensíveis activo nos logs. |
| CIC-004 | Gates de segurança obrigatórios antes de promoção entre ambientes | ✔ | ✔ | ✔ | Etapas de validação de segurança (SAST, SCA, lint, secrets scan) configuradas como bloqueantes; promoção de artefactos entre ambientes requer aprovação humana explícita para acções irreversíveis; sem bypass automatizado. |
| CIC-005 | Rastreabilidade completa de cada execução de pipeline | ✔ | ✔ | ✔ | Cada execução identificável por ID único; logs retidos pelo período definido em política; possível reconstruir o que correu, quando, com que inputs, com que resultado e quem aprovou. |
| CIC-006 | Isolamento de runners e ambientes de execução | — | ✔ | ✔ | Runners sem acesso directo a dados ou credenciais de produção; execução em ambientes efémeros ou isolados; sem partilha de estado persistente entre jobs de repositórios distintos. |
| CIC-007 | Integridade e proveniência verificável dos artefactos produzidos | — | ✔ | ✔ | Artefactos assinados digitalmente ou com hash verificável gerado no momento do build; proveniência (commit SHA, pipeline run ID, build environment) associada ao artefacto e verificável antes de promoção. |
| CIC-008 | Separação de responsabilidades entre build, test e deploy | — | ✔ | ✔ | Jobs distintos para as fases de build, test e deploy; sem permissões cruzadas desnecessárias entre stages; identidade e âmbito de credenciais por stage documentados e enforced. |
| CIC-009 | Credenciais do pipeline com âmbito mínimo e rotação definida | — | ✔ | ✔ | Tokens e credenciais usados pelo pipeline com âmbito mínimo necessário; rotação periódica definida e evidenciada; sem credenciais partilhadas entre pipelines de aplicações distintas. |
| CIC-010 | Protecção contra execução de código não autorizado em runners | — | — | ✔ | Runners com isolamento forte (containers efémeros, VMs descartáveis); sem acesso ao Docker socket por jobs não privilegiados; sem capacidades de escalonamento de privilégios; logs de tentativas bloqueadas disponíveis. |

---

## Notas explicativas

- **CIC-001**: O pipeline-como-código (Pipeline as Code) é condição necessária para rastreabilidade e revisão — um pipeline editável apenas na UI da plataforma é inauditável por definição.
- **CIC-002**: O risco de envenenamento de pipeline via forks (ex: GitHub Actions pull_request_target) é um vector estabelecido; triggers de pull requests de forks externos devem ser tratados como não confiáveis por omissão.
- **CIC-003**: A confidencialidade dos segredos deve ser preservada mesmo em caso de falha ou abort do pipeline; segredos nunca devem aparecer em outputs de debug ou em artefactos gerados.
- **CIC-004**: "Aprovação humana para acções irreversíveis" inclui: promoção para produção, deploy, publicação em registry público, e quaisquer operações de modificação de estado externo não revertíveis automaticamente.
- **CIC-007**: Ferramentas de referência: Sigstore/Cosign para assinatura, SLSA Provenance Generator, GitHub Artifact Attestations, in-toto framework. A proveniência deve ser verificada downstream, não apenas gerada.
- **CIC-010**: O acesso ao Docker socket por jobs de pipeline é um vector de escalonamento de privilégios frequentemente subestimado — um job com acesso ao socket tem controlo efectivo do host.

---

> Para design seguro de pipelines e controlo de triggers, consultar [Design Seguro dos Pipelines](./design-seguro-pipelines).
> Para gestão e injecção segura de segredos, consultar [Gestão de Segredos no Pipeline](./gestao-segredos-pipeline).
> Para isolamento de runners, consultar [Isolamento de Runners](./isolamento-runners).
> Para integridade e proveniência de artefactos, consultar [Integridade e Proveniência](./integridade-proveniencia).
> Para políticas e gates de pipeline, consultar [Políticas e Gates](./politicas-gates-pipeline).
