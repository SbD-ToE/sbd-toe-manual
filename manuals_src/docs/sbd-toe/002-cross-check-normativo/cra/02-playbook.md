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

Princípio: Reutilizar > Inventar. Muitas capacidades (SBOM, patching, testes) já existem, mas a conformidade `CRA` exige também contexto de produto, papel de operador económico, support period, reporting formal e rota documental própria.

Este playbook é mais defensável quando aplicado a:

- fabricante de produto com elementos digitais
- fornecedor que precisa de organizar evidência técnica para uma leitura `CRA`
- contextos com produto versionado, contacto de segurança, período de suporte e responsabilidades de operador económico

Fora desse contexto, o SbD-ToE continua útil como base técnica, mas a leitura já não é uma leitura `CRA` completa.

> 📚 **Recursos de Suporte:** Para templates práticos e exemplos de implementação, consultar [Exemplo-Playbook](/sbd-toe/cross-check-normativo/exemplo-playbook/exemplo-toolchain-options) com toolchains, KPIs, RACI e processos de vulnerability handling reutilizáveis.

## Mapa Rápido CRA → SbD-ToE {#mapa-rápido-cra--sbd-toe}

| Área CRA | SbD-ToE | Ação | Evidência |
|----------|---------|------|----------|
| Ciclo de Vida Seguro | [Cap. 02](/sbd-toe/sbd-manual/requisitos-seguranca/intro), [Cap. 06](/sbd-toe/sbd-manual/desenvolvimento-seguro/intro), [Cap. 07](/sbd-toe/sbd-manual/cicd-seguro/intro), [Cap. 11](/sbd-toe/sbd-manual/deploy-seguro/intro) | Política ciclo de vida, support period e gates | Política aprovada; pipeline YAML; registo de support period |
| Vulnerability Handling | [Cap. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro), [Cap. 10](/sbd-toe/sbd-manual/testes-seguranca/intro), [Cap. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro) | Processo triagem + SLA | Registos triagem; métricas SLA |
| SBOM | [Cap. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro) | Geração contínua + export | Ficheiros CycloneDX por release |
| Patching Rápido | [Cap. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro), [Cap. 07](/sbd-toe/sbd-manual/cicd-seguro/intro) | Workflow patch automático | Pull requests patch + tempos |
| Reporte Exploração | [Cap. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro), [Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro) | Runbook técnico + interface de notificação regulatória | Runbook; matriz de comunicação; JSON exemplo |
| Documentação Segurança | [Cap. 04](/sbd-toe/sbd-manual/arquitetura-segura/intro), [Cap. 11](/sbd-toe/sbd-manual/deploy-seguro/intro) | Guia de segurança do produto + contact point + fim de suporte | PDF/Markdown guia publicado; tabela de suporte |
| Exceções | [Cap. 02](/sbd-toe/sbd-manual/requisitos-seguranca/intro) addon 08, [Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro) | Política exceções CRA | Registos exceções + aprovadores |
| Cadeia Fornecimento | [Cap. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro), [Cap. 09](/sbd-toe/sbd-manual/containers-imagens/intro), [Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro) | Checklist supply chain físico | Checklist preenchida |

---

## Fases de Implementação (≈ 6–9 meses) {#fases-de-implementação--69-meses}

### Fase 1 (M0–M1): Fundamentos, Scope Gate & Governance {#fase-1-m0m1-fundamentos-scope-gate--governance}
1. Designar Owner CRA (GRC + AppSec)  
2. Criar Política "Segurança de Produto & CRA" (aprovada por gestão)  
3. Mapear roles SbD-ToE → papéis CRA (fabricante, importador, distribuidor, substantial modification quando aplicável)  
4. Definir matriz criticidade produto (base L1–L3 adaptada)  
5. Registar support period e regra de comunicação de fim de suporte por linha de produto  
**Evidências:** Ata aprovação; matriz criticidade; política versão 1.0; registo de papéis e suporte

### Fase 2 (M1–M2): SBOM & Inventário {#fase-2-m1m2-sbom--inventário}
1. Ativar geração automática SBOM (build pipeline)  
2. Validar cobertura (≥95% componentes listados)  
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
2. Criar gate "no-critical-known" (release bloqueada)  
3. Processo exceção crítica (board-level)  
4. Template relatório qualidade release  
**Evidências:** Logs pipeline; configuração gate; relatório release #1

### Fase 5 (M4–M5): Disclosure & Comunicação Externa {#fase-5-m4m5-disclosure--comunicação-externa}
1. Publicar security.txt + chave PGP  
2. Página "Vulnerability Disclosure Policy"  
3. Runbook triagem reporte externo  
4. Canal email/portal dedicado  
5. Identificar ponto de contacto de segurança para utilizadores e investigadores  
**Evidências:** Página pública; registo primeiro teste reporte; contacto publicado

### Fase 6 (M5–M6): Reporte de Exploração Ativa {#fase-6-m5m6-reporte-de-exploração-ativa}
1. Definir critérios de "explorada ativamente" (IOC, telemetria confirmada)  
2. Criar script export JSON incidente + SBOM componente afetado  
3. Runbook de notificação à CSIRT designada como coordenadora e à ENISA, através da plataforma única (alerta precoce ≤24 h, notificação ≤72 h e relatório final (art. 14.º; aplicável desde 11.9.2026)), e matriz de comunicação a utilizadores (art. 14.º, n.º 8)  
4. Simulação exercício interno  
**Evidências:** Script; runbook; relatório exercício; matriz de comunicação

### Fase 7 (M6–M7): Documentação de Segurança do Produto {#fase-7-m6m7-documentação-de-segurança-do-produto}
1. Escrever Guia Segurança (instalação segura, atualização, contacto, support period, fim de suporte)  
2. Validar com AppSec + engenharia  
3. Publicar versão 1.0 (Markdown/PDF)  
4. Processo atualização por release  
**Evidências:** Guia v1; diff v1→v2 (exemplo)

### Fase 8 (M7–M8): Cadeia Fornecimento Expandida {#fase-8-m7m8-cadeia-fornecimento-expandida}
1. Inventariar firmware/hardware (se aplicável)  
2. Checklist integridade (hash, assinatura, origem)  
3. Processo atualização segura (secure channel)  
4. Métrica cobertura supply chain (≥90%)  
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
- [ ] Política exceções CRA publicada
- [ ] Exceções críticas aprovadas board

### Checklist Release Gate {#checklist-release-gate}
- [ ] SAST integrado
- [ ] DAST integrado
- [ ] Fuzzing (se aplicável)
- [ ] Gate bloqueia vulnerabilidade explorável conhecida (anexo I, parte I, ponto 2, al. a)), não só CVE crítico
- [ ] Relatório qualidade release arquivado
- [ ] Processo override exceção formal

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
- [ ] Percurso rápido: triagem ≤ 4 h com indício de exploração ativa (escolha do Manual); alerta precoce ≤ 24 h após o conhecimento
- [ ] Matriz de comunicação a utilizadores
- [ ] Simulação concluída
- [ ] Evidência testes arquivada

### Checklist Documentação Segurança {#checklist-documentação-segurança}
- [ ] Guia instalação segura
- [ ] Guia atualização + rollback
- [ ] Contacto segurança (security@)
- [ ] Support period documentado
- [ ] Data de fim de suporte comunicável
- [ ] Recomendações configuração endurecida
- [ ] Secção gestão de vulnerabilidades
- [ ] Versão e data
- [ ] Documentação técnica (incluindo a SBOM) e declaração de conformidade UE conservadas por pelo menos 10 anos após a colocação no mercado ou pelo período de apoio, consoante o que for mais longo (art. 13.º, n.º 13)

### Checklist Supply Chain Física (se aplicável) {#checklist-supply-chain-física-se-aplicável}
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
| % SLA Cumprido | (Vulns patch dentro SLA) / total | ≥90% |
| Cobertura SBOM | % componentes identificados | ≥95% |
| Tempo Médio Resposta Disclosure | Receção → primeira resposta | ≤5 dias úteis sem indício de exploração; triagem ≤4 h com indício de exploração ativa (escolha do Manual) |
| Gate Efetividade | Releases bloqueadas por CVE crítico | 100% bloqueadas |
| Exceções Críticas Ativas | Nº exceções críticas abertas | Tendência decrescente |

---

## Artefactos a Manter (Data Room) {#artefactos-a-manter-data-room}
| Artefacto | Tipo | Frequência Atualização |
|-----------|------|------------------------|
| Política Segurança Produto & CRA | Documento | Anual / quando requisito muda |
| Registo de Papéis CRA & Support Period | Documento | Por linha de produto / revisão de release |
| SBOM Releases | Ficheiros | Cada release major/minor |
| Dashboard Vulnerabilidades | Painel | Contínuo (live) |
| Relatórios Qualidade Release | Documento | Cada release |
| Guia Segurança Produto | Documento | Cada release major |
| Runbook Exploração Ativa | Documento | Anual / exercícios |
| Registos Disclosure | Tickets / Issues | Contínuo |
| Checklist Supply Chain | Documento | Trimestral |

---

## Exceções (Política Resumida) {#exceções-política-resumida}
Categorias:
- Inaceitáveis: RCE crítico, bypass autenticação, exposure credenciais em claro
- Aceitáveis (TTL da Política 05 §7: Critical 7 dias com plano de remediação; não aceitável em L3): Crítico sem patch disponível + compensação robusta
- Aceitáveis (TTL da Política 05 §7: High 90 / 30 / 14 dias em L1 / L2 / L3): High com mitigação parcial

Registos: ID | Vulnerabilidade | Severidade | Justificação | Aprovador | TTL | Mitigação | Data Revisão

Escalação: Crítico → Board; High → CISO/AppSec; Medium/Low → AppSec.

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

**Versão:** 1.0  
**Data:** Novembro 2025  
**Nota:** Este playbook complementa a análise normativa CRA com abordagem sequencial prática e não substitui a rota formal de conformidade do regulamento.
