---
id: playbook
title: "SbD-ToE 4 CRA: Playbook de Implementação"
description: Roadmap prático para usar SbD-ToE como base técnica do CRA em contexto de produto, com formalização regulatória complementar
tags: [playbook, cra, implementacao, roadmap, produtos-digitais]
sidebar_position: 6
---

# SbD-ToE 4 CRA: Playbook de Implementação

## Visão Geral {#visão-geral}

Objetivo: Transformar requisitos CRA em ações concretas usando controlos existentes do SbD-ToE.

Princípio: Reutilizar > Inventar. Muitas capacidades (SBOM, patching, testes) já existem, mas a conformidade `CRA` exige também contexto de produto (contexto `CTX-CRA`, com os seus pisos e acrescentos), período de apoio (`CTX-CRA-R01`), reporting formal e rota documental própria. O papel de operador económico é uma qualificação jurídica, fora do âmbito do Manual.

O que o Manual cobre, o que é lacuna declarada e o que fica fora de âmbito está na [análise normativa](./intro#o-que-este-manual-cobre-e-o-que-fica-de-fora) e, obrigação a obrigação, em [Requisitos aplicáveis](./requisitos-aplicaveis#cobertura).

Este playbook é mais defensável quando aplicado a:

- fabricante de produto com elementos digitais
- fornecedor que precisa de organizar evidência técnica para uma leitura `CRA`
- contextos com produto versionado, contacto de segurança, período de suporte e responsabilidades de operador económico

Fora desse contexto, o SbD-ToE continua útil como base técnica, mas a leitura já não é uma leitura `CRA` completa.

> 📚 **Recursos de Suporte:** Para templates práticos e exemplos de implementação, consultar [Exemplo-Playbook](/sbd-toe/cross-check-normativo/exemplo-playbook/exemplo-toolchain-options) com toolchains, KPIs, RACI e processos de vulnerability handling reutilizáveis.

## Mapa Rápido CRA → SbD-ToE {#mapa-rápido-cra--sbd-toe}

| Área CRA | SbD-ToE | Ação | Evidência |
|----------|---------|------|----------|
| Ciclo de Vida Seguro | [Cap. 02](/sbd-toe/sbd-manual/requisitos-seguranca/intro), [Cap. 06](/sbd-toe/sbd-manual/desenvolvimento-seguro/intro), [Cap. 07](/sbd-toe/sbd-manual/cicd-seguro/intro), [Cap. 11](/sbd-toe/sbd-manual/deploy-seguro/intro) | Política ciclo de vida, período de apoio (`CTX-CRA-R01`) e gates | Política aprovada; pipeline YAML; registo do período de apoio |
| Vulnerability Handling | [Cap. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro), [Cap. 10](/sbd-toe/sbd-manual/testes-seguranca/intro), [Cap. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro) | Processo triagem + SLA | Registos triagem; métricas SLA |
| SBOM | [Cap. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro) | Geração contínua + export | Ficheiros CycloneDX por release |
| Patching Rápido | [Cap. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro), [Cap. 07](/sbd-toe/sbd-manual/cicd-seguro/intro) | Workflow patch automático | Pull requests patch + tempos |
| Reporte Exploração | [Cap. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro), [Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro), [Política 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória), `CTX-CRA-R05` | Runbook técnico + interface de notificação regulatória | Runbook; matriz de comunicação; JSON exemplo |
| Documentação Segurança | [Cap. 04](/sbd-toe/sbd-manual/arquitetura-segura/intro), [Cap. 11](/sbd-toe/sbd-manual/deploy-seguro/intro) | Guia de segurança do produto + ponto de contacto (`GOV-015`, piso `CTX-CRA-P04`) + fim do apoio (`CTX-CRA-R01`) | PDF/Markdown guia publicado; tabela de suporte |
| Exceções | [Cap. 02](/sbd-toe/sbd-manual/requisitos-seguranca/intro) addon 08, [Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro) | [Política 12 §4](/sbd-toe/assets/policies/policy-excecoes-cve#4-tipos-de-exceção) com o piso `CTX-CRA-P02` (sem exceção para vulnerabilidade explorável conhecida na colocação no mercado) | Registos exceções + aprovadores |
| Cadeia Fornecimento | [Cap. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro), [Cap. 09](/sbd-toe/sbd-manual/containers-imagens/intro), [Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro) | `DEP-006` com o piso `CTX-CRA-P03`; comunicação ao mantenedor (`CTX-CRA-R04`) | Registo de aprovação de dependências |

---

## Fases de Implementação (≈ 6–9 meses) {#fases-de-implementação--69-meses}

### Fase 1 (M0–M1): Fundamentos, Scope Gate & Governance {#fase-1-m0m1-fundamentos-scope-gate--governance}
1. Designar Owner CRA (GRC + AppSec)  
2. Criar Política "Segurança de Produto & CRA" (aprovada por gestão)  
3. Mapear roles SbD-ToE → papéis CRA (fabricante, importador, distribuidor, substantial modification quando aplicável); a qualificação é jurídica e fica fora do âmbito do Manual  
4. Declarar o contexto `CTX-CRA` por aplicação ou produto e classificar o risco em L1–L3 (Cap. 01). A categoria do produto nos anexos III e IV é outra classificação, que o L1–L3 não substitui (lacuna declarada: o Manual não a identifica)  
5. Determinar o período de apoio conforme `CTX-CRA-R01` (critérios do art. 13.º, n.º 8, pelo menos cinco anos salvo utilização prevista inferior, fundamentação registada, notificação do fim do apoio)  
**Evidências:** Ata aprovação; classificação L1–L3 e declaração do contexto; política versão 1.0; registo de papéis e do período de apoio

### Fase 2 (M1–M2): SBOM & Inventário {#fase-2-m1m2-sbom--inventário}
1. Ativar geração automática SBOM (build pipeline)  
2. Validar cobertura (≥95% componentes listados; meta indicativa, escolha do Manual)  
3. Criar export sanitized CycloneDX  
4. Repositório "SBOM Releases" (controlado, versionado)  
**Evidências:** SBOM v1; relatório cobertura; script export

### Fase 3 (M2–M3): Vulnerability Handling & SLAs {#fase-3-m2m3-vulnerability-handling--slas}
1. Definir severidade (Critical/High/Medium/Low)  
2. Adotar a escada interna de remediação da Política 19 §4.3 (escolha do Manual, não prazo do CRA)  
3. Automatizar criação de issue para CVE crítico  
4. Dashboard patch compliance  
**Evidências:** Política SLA; dashboard inicial; issues exemplo

### Fase 4 (M3–M4): Testes & Gate Release {#fase-4-m3m4-testes--gate-release}
1. Integrar SAST/DAST/fuzzing pipeline  
2. Gate que bloqueia qualquer vulnerabilidade explorável conhecida, em qualquer nível (`DEP-002`, piso `CTX-CRA-P01`)  
3. Exceções para vulnerabilidades exploráveis conhecidas: não admitidas na colocação no mercado (piso `CTX-CRA-P02`)  
4. Template relatório qualidade release  
**Evidências:** Logs pipeline; configuração gate; relatório release #1

### Fase 5 (M4–M5): Disclosure & Comunicação Externa {#fase-5-m4m5-disclosure--comunicação-externa}
O Manual prescreve a política de divulgação coordenada e o canal de receção (`GOV-015`); no contexto CRA são obrigatórios em qualquer nível, com ponto de contacto único (piso `CTX-CRA-P04`). Os passos abaixo implementam esse requisito.

1. Publicar security.txt + chave PGP  
2. Página "Vulnerability Disclosure Policy"  
3. Runbook triagem reporte externo  
4. Canal email/portal dedicado  
5. Identificar ponto de contacto de segurança para utilizadores e investigadores  
**Evidências:** Página pública; registo primeiro teste reporte; contacto publicado

### Fase 6 (M5–M6): Reporte de Exploração Ativa {#fase-6-m5m6-reporte-de-exploração-ativa}
1. Definir critérios de "explorada ativamente" (IOC, telemetria confirmada)  
2. Criar script export JSON incidente + SBOM componente afetado  
3. Runbook de notificação à CSIRT designada como coordenadora e à ENISA, através da plataforma única (alerta precoce ≤24 h, notificação ≤72 h e relatório final (art. 14.º; aplicável desde 11.9.2026)), e matriz de comunicação a utilizadores (art. 14.º, n.º 8). Base no Manual: [Política 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória) e o critério de incidente grave `CTX-CRA-R05`; o conteúdo mínimo de cada notificação e o relatório intercalar são lacuna declarada  
4. Simulação exercício interno  
**Evidências:** Script; runbook; relatório exercício; matriz de comunicação

### Fase 7 (M6–M7): Documentação de Segurança do Produto {#fase-7-m6m7-documentação-de-segurança-do-produto}
1. Escrever Guia Segurança (instalação segura, atualização, contacto, período de apoio e data do seu fim conforme `CTX-CRA-R01`). A instalação e utilização seguras, o efeito de alterações na segurança dos dados e a desativação e remoção de dados são lacuna declarada do Manual (anexo II, ponto 8)  
2. Validar com AppSec + engenharia  
3. Publicar versão 1.0 (Markdown/PDF)  
4. Processo atualização por release  
**Evidências:** Guia v1; diff v1→v2 (exemplo)

### Fase 8 (M7–M8): Cadeia Fornecimento Expandida {#fase-8-m7m8-cadeia-fornecimento-expandida}
Firmware e hardware estão fora do âmbito do Manual, que é centrado na aplicação; esta fase só se aplica se a organização tiver processo próprio. A integridade dos componentes de software de terceiros é `DEP-006` (piso `CTX-CRA-P03`).

1. Inventariar firmware/hardware (se aplicável)  
2. Checklist integridade (hash, assinatura, origem)  
3. Processo atualização segura (secure channel)  
4. Métrica cobertura supply chain (≥90%; meta indicativa, escolha do Manual)  
**Evidências:** Checklist preenchida; métrica cobertura

### Fase 9 (M8–M9): Métricas & Melhoria Contínua {#fase-9-m8m9-métricas--melhoria-contínua}
1. Métricas: MTTP (Mean Time To Patch), % SLA cumprido, vulns abertas por severidade  
2. Reunião retrospectiva trimestral  
3. Plano melhoria (top 3 blockers)  
4. Ajuste políticas conforme revisão legal/regulatória  
**Evidências:** Dashboard; ata retrospectiva; plano melhoria

---

## Checklists {#checklists}

### Checklist SBOM {#checklist-sbom}
- [ ] Pipeline gera SBOM automaticamente
- [ ] Formato CycloneDX/SPDX validado
- [ ] Export sanitized criado
- [ ] Versão SBOM associada a release
- [ ] Cobertura ≥95% componentes
- [ ] Processo atualização documentado

### Checklist Vulnerability Handling {#checklist-vulnerability-handling}
- [ ] Severidade definida (Critical/High/Medium/Low)
- [ ] SLA patch documentado
- [ ] Issues automáticas para críticos
- [ ] Dashboard patch compliance ativo
- [ ] Política exceções CRA publicada, com o piso `CTX-CRA-P02`
- [ ] Nenhuma exceção para vulnerabilidade explorável conhecida em release para o mercado (piso `CTX-CRA-P02`)

### Checklist Release Gate {#checklist-release-gate}
- [ ] SAST integrado
- [ ] DAST integrado
- [ ] Fuzzing (se aplicável)
- [ ] Gate bloqueia vulnerabilidade explorável conhecida (anexo I, parte I, ponto 2, al. a)), não só CVE crítico
- [ ] Relatório qualidade release arquivado
- [ ] Processo de exceção formal restrito a vulnerabilidades com análise documentada de não explorabilidade no produto (piso `CTX-CRA-P02`)

### Checklist Disclosure {#checklist-disclosure}
- [ ] security.txt publicado
- [ ] Chave PGP acessível
- [ ] Página política disclosure publicada
- [ ] Canal reporte funcional (email/portal)
- [ ] Runbook triagem interna
- [ ] Ponto de contacto de segurança identificado
- [ ] Tempo resposta médio `<`5 dias úteis para reportes sem indício de exploração; com indício de exploração ativa, triagem ≤4 h e trilho do art. 14.º (escolha do Manual)

### Checklist Reporte Exploração {#checklist-reporte-exploração}
- [ ] Critérios "explorada ativamente" definidos
- [ ] Script export JSON pronto
- [ ] Runbook de notificação do art. 14.º (24 h / 72 h / relatório final)
- [ ] Conteúdo mínimo de cada notificação (Estados-Membros, natureza, medidas, sensibilidade da informação) — lacuna declarada no Manual
- [ ] Relatório intercalar a pedido da CSIRT — lacuna declarada no Manual
- [ ] Percurso rápido: triagem ≤ 4 h com indício de exploração ativa (escolha do Manual); alerta precoce ≤ 24 h após o conhecimento
- [ ] Matriz de comunicação a utilizadores
- [ ] Simulação concluída
- [ ] Evidência testes arquivada

### Checklist Documentação Segurança {#checklist-documentação-segurança}
- [ ] Guia instalação segura
- [ ] Guia atualização + rollback
- [ ] Contacto segurança (security@)
- [ ] Período de apoio determinado e fundamentado (`CTX-CRA-R01`)
- [ ] Data de fim de suporte comunicável
- [ ] Recomendações configuração endurecida
- [ ] Secção gestão de vulnerabilidades
- [ ] Versão e data
- [ ] Documentação técnica (incluindo a SBOM) e declaração de conformidade UE conservadas por pelo menos 10 anos após a colocação no mercado ou pelo período de apoio, consoante o que for mais longo (art. 13.º, n.º 13). Lacuna declarada: o Manual aplica os 10 anos à SBOM e ao pacote de evidências, mas não ainda às versões do threat model nem aos registos de aprovação; a declaração UE é do fabricante e fica fora do âmbito do Manual

### Checklist Supply Chain Física (se aplicável) {#checklist-supply-chain-física-se-aplicável}
Fora do âmbito do Manual; incluir apenas se a organização tiver processo próprio.

- [ ] Lista firmware/hardware
- [ ] Hashes/assinaturas verificados
- [ ] Canal atualização seguro
- [ ] Processo de validação integridade
- [ ] Registos auditáveis

---

## Métricas-Chave {#métricas-chave}
| Métrica | Definição | Objetivo Inicial |
|---------|-----------|------------------|
| MTTP Crítico | Tempo médio até patch crítico | ≤ SLA do nível (Política 19 §4.3; 3 dias em L3) |
| % SLA Cumprido | (Vulns patch dentro SLA) / total | ≥90% (escolha do Manual) |
| Cobertura SBOM | % componentes identificados | ≥95% |
| Tempo Médio Resposta Disclosure | Receção → primeira resposta | ≤5 dias úteis sem indício de exploração; triagem ≤4 h com indício de exploração ativa (escolha do Manual) |
| Gate Efetividade | Releases com vulnerabilidade explorável conhecida bloqueadas | 100% (piso `CTX-CRA-P01`) |
| Exceções sobre Exploráveis Conhecidas | Nº exceções ativas sobre vulnerabilidades exploráveis conhecidas em release para o mercado | 0 (piso `CTX-CRA-P02`) |

---

## Artefactos a Manter (Data Room) {#artefactos-a-manter-data-room}
| Artefacto | Tipo | Frequência Atualização |
|-----------|------|------------------------|
| Política Segurança Produto & CRA | Documento | Anual / quando requisito muda |
| Registo de Papéis CRA & Período de Apoio (`CTX-CRA-R01`) | Documento | Por linha de produto / revisão de release |
| SBOM Releases | Ficheiros | Cada release major/minor |
| Dashboard Vulnerabilidades | Painel | Contínuo (live) |
| Relatórios Qualidade Release | Documento | Cada release |
| Guia Segurança Produto | Documento | Cada release major |
| Runbook Exploração Ativa | Documento | Anual / exercícios |
| Registos Disclosure | Tickets / Issues | Contínuo |
| Checklist Supply Chain | Documento | Trimestral |

---

## Exceções (Política Resumida) {#exceções-política-resumida}
**Regra CRA:** uma vulnerabilidade explorável conhecida não é excetuável na colocação no mercado, seja qual for a severidade (piso `CTX-CRA-P02`). O piso não admite justificação nem aprovação de nenhum nível. As categorias abaixo aplicam-se apenas a vulnerabilidades sem exploração conhecida e a produtos já no mercado, no âmbito do tratamento sem demora.

Categorias:
- Inaceitáveis: RCE crítico, bypass autenticação, exposure credenciais em claro
- Aceitáveis (TTL da Política 05 §7: Critical 7 dias com plano de remediação; não aceitável em L3): Crítico sem patch disponível, com compensação robusta e análise documentada de que a vulnerabilidade não é explorável no produto (p. ex. componente não usado ou não alcançável). Uma vulnerabilidade explorável conhecida nunca é aceitável na colocação no mercado (pisos CTX-CRA-P01/P02; o critério da lei é a explorabilidade, não a exploração ativa)
- Aceitáveis (TTL da Política 05 §7: High 90 / 30 / 14 dias em L1 / L2 / L3): High com mitigação parcial e análise documentada de que não é explorável no produto

Registos: ID | Vulnerabilidade | Severidade | Justificação | Aprovador | TTL | Mitigação | Data Revisão

Escalação (só para vulnerabilidades não exploráveis no produto; alçadas da Política 05 §6): Critical → CISO (L2; não aceitável em L3); High → AppSec ou CISO, conforme o nível; Medium/Low → AppSec.

---

## Próximos Passos Depois da Fase 9 {#próximos-passos-depois-da-fase-9}
1. Avaliação formal conformidade (legal + técnico)  
2. Preparar documentação para eventual auditoria/regulador  
3. Integração com outras normas (ex: DORA, NIS2) - evitar duplicação  
4. Refinar métricas (MTTP por componente, densidade vulnerabilidades)  
5. Automatizar geração relatório trimestral CRA

---

## Recursos Práticos de Implementação {#recursos-práticos-de-implementação}

Para suporte concreto na implementação deste playbook, consultar os seguintes exemplos reutilizáveis:

- 🛠️ **[Opções de Toolchain](../exemplo-playbook/exemplo-toolchain-options)** - Comparação de ferramentas SCA, SBOM e vulnerability management
- 📊 **[KPIs e Targets](../exemplo-playbook/exemplo-kpis-targets)** - Métricas de patching e SBOM coverage adaptáveis ao CRA
- 👥 **[RACI e Governance](../exemplo-playbook/exemplo-raci-governance)** - Matrizes de responsabilidades para vulnerability handling
- 📝 **[Relatório de Incidentes](../exemplo-playbook/exemplo-relatorio-incidentes)** - Template adaptável para reporte de exploração ativa (CRA)

Estes recursos demonstram implementações práticas das abstenções deliberadas do SbD-ToE.

---

## Referências {#referências}
- [Análise normativa CRA](intro)
- SbD-ToE Capítulos 01–14
- ENISA: Vulnerability Disclosure Guidelines
- ISO/IEC 29147 & 30111
- CycloneDX, SPDX

**Versão:** 1.1  
**Data:** Setembro 2026 (alinhada com a matriz de cobertura e o contexto `CTX-CRA`)  
**Nota:** Este playbook complementa a análise normativa CRA com abordagem sequencial prática e não substitui a rota formal de conformidade do regulamento.
