---
id: playbook
title: "SbD-ToE 4 GDPR: Playbook de Implementação"
description: Roadmap prático para alinhar o SbD-ToE aos requisitos técnicos do RGPD
tags: [playbook, gdpr, implementacao, privacy-by-design, art32]
sidebar_position: 8
---

# SbD-ToE 4 GDPR: Playbook de Implementação

## Visão Geral {#visão-geral}

Objetivo: operacionalizar os arts. 15.º–22.º, 25.º, 30.º, 32.º, 33.º–34.º e 35.º do RGPD com base nas capacidades técnicas do SbD-ToE e integrar com jurídico/DPO.

Estrutura: Requisitos → Ação → Evidência. Reutilizar controlos NIS2/DORA sempre que possível.

O que o Manual cobre, as lacunas que declara e o que fica fora de âmbito, obrigação a obrigação, estão em [Requisitos aplicáveis — O que este Manual cobre e o que fica de fora](./requisitos-aplicaveis#cobertura).

> 📚 **Recursos de Suporte:** Para templates práticos e exemplos de implementação, consultar [Exemplo-Playbook](/sbd-toe/cross-check-normativo/exemplo-playbook/exemplo-toolchain-options) com toolchains de cifragem, KPIs de privacy e processos de incident response reutilizáveis.

---

## Mapa Rápido: GDPR Art. → SbD-ToE {#mapa-rápido-gdpr-art--sbd-toe}

| Artigo GDPR | Requisito | Capítulo SbD-ToE | Ação Principal |
|-------------|-----------|------------------|----------------|
| 5 | Princípios | [Cap. 01](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro), [Cap. 02](/sbd-toe/sbd-manual/requisitos-seguranca/intro), [Cap. 04](/sbd-toe/sbd-manual/arquitetura-segura/intro), [Cap. 11](/sbd-toe/sbd-manual/deploy-seguro/intro) | Minimização, retenção, segurança |
| 15–22 | Direitos dos titulares | [Cap. 02](/sbd-toe/sbd-manual/requisitos-seguranca/intro) | Mecanismo técnico testado (PRI-003, PRI-006); resposta formal com Jurídico/DPO |
| 25 | Privacy by design/default | [Cap. 04](/sbd-toe/sbd-manual/arquitetura-segura/intro), [Cap. 06](/sbd-toe/sbd-manual/desenvolvimento-seguro/intro)–[Cap. 07](/sbd-toe/sbd-manual/cicd-seguro/intro), [Cap. 11](/sbd-toe/sbd-manual/deploy-seguro/intro) | Configurações seguras por defeito |
| 30 | ROPA | [Cap. 01](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro), [Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro) | Inventário apps/dados + registo GRC |
| 32 | Segurança do tratamento | [Cap. 02](/sbd-toe/sbd-manual/requisitos-seguranca/intro), [Cap. 04](/sbd-toe/sbd-manual/arquitetura-segura/intro), [Cap. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro), [Cap. 10](/sbd-toe/sbd-manual/testes-seguranca/intro), [Cap. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro) | Cifragem, IAM, testes, resiliência |
| 33/34 | Violação de dados | [Cap. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro), [Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro) | Runbook: autoridade de controlo ≤ 72h (art. 33.º); titulares sem demora injustificada se houver elevado risco (art. 34.º) |
| 35 | DPIA | [Cap. 03](/sbd-toe/sbd-manual/threat-modeling/intro), [Cap. 04](/sbd-toe/sbd-manual/arquitetura-segura/intro) | TM + anexos técnicos na DPIA |

---

## Fases de Implementação (≈ 4–6 meses) {#fases-de-implementação--46-meses}

### Fase 1 (M0–M1): Governação e Enquadramento {#fase-1-m0m1-governação-e-enquadramento}
1. Nomear o EPD, se aplicável (matéria jurídica, fora do âmbito do Manual; o Manual assume o papel onde há dados pessoais) e alinhar o RACI ([Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro))  
2. Política de proteção de dados aprovada pela organização (o Manual não a inclui entre as suas políticas: lacuna declarada face ao art. 24.º, n.º 2)  
3. Definir classificação de dados pessoais por aplicação  
**Evidências:** Ata aprovação; RACI; matriz dados/aplicações

### Fase 2 (M1–M2): Inventário & ROPA {#fase-2-m1m2-inventário--ropa}
1. Manter o inventário de finalidades e destinatários por conjunto de dados pessoais (PRI-004, obrigatório em qualquer nível)  
2. Registar o ROPA em ferramenta GRC (campos Art. 30), alimentado por esse inventário  
3. Ligar IDs de apps SbD-ToE ao ROPA  
**Evidências:** ROPA export; mapeamento IDs

### Fase 3 (M2–M3): Privacy by Design/Default (Art. 25) {#fase-3-m2m3-privacy-by-designdefault-art-25}
1. Requisitos PRI do Cap. 02 aplicados: minimização (PRI-001), retenção com apagamento efetivo (PRI-002), PII em registos (PRI-005) e privacidade por defeito (PRI-007)  
2. Configs por defeito: coleta mínima, encryption at rest/in transit  
3. Gate de pipeline: bloqueio se coleta excessiva (linting de schemas, por ex.)  
**Evidências:** Catálogo PbD; pipelines; exemplos de bloqueio

### Fase 3-A (M2–M3): Direitos dos titulares (arts. 15.º–22.º) {#fase-3-a-m2m3-direitos-dos-titulares-arts-1522}
1. Mecanismo testado de acesso, rectificação, apagamento e exportação, que chega aos destinatários registados (PRI-003, PRI-004)  
2. Limitação do tratamento (CTX-RGPD-R01) e apagamento de dados tornados públicos (CTX-RGPD-R02)  
3. Consentimento e oposição, incluindo sinais automatizados como o GPC (PRI-006; CTX-RGPD-R04)  
4. Decisões exclusivamente automatizadas com intervenção humana e contestação (CTX-RGPD-R05)  
5. Verificação da idade e consentimento parental quando aplicável (CTX-RGPD-R03)  
**Fora do âmbito:** a resposta formal ao titular (prazos, fundamentação), com o Jurídico/DPO.  
**Evidências:** testes do mecanismo; registo das execuções

### Fase 4 (M2–M3): Segurança do Tratamento (Art. 32) {#fase-4-m2m3-segurança-do-tratamento-art-32}
1. Cifragem: TLS 1.2+; at rest com gestão de chaves  
2. IAM: MFA, least privilege, revisão periódica de acessos  
3. Testes: SAST/DAST/fuzzing; validação de eficácia  
4. Resiliência: backups, DR testado, monitorização  
**Evidências:** Registos de chaves, relatórios de testes, logs DR

### Fase 5 (M3–M4): DPIA (Art. 35) {#fase-5-m3m4-dpia-art-35}
1. Critérios de gatilho DPIA definidos  
2. Reutilizar Threat Modeling ([Cap. 03](/sbd-toe/sbd-manual/threat-modeling/intro)) como anexo técnico  
3. Anexar a análise LINDDUN, obrigatória em todos os níveis quando há dados pessoais (THR-003)  
4. Parecer do EPD e decisão do responsável pelo tratamento, registados (fora do Manual; o Manual só prevê a revisão do EPD sobre a análise LINDDUN em L3)  
**Evidências:** DPIA #1; anexos TM; aprovação DPO

### Fase 6 (M3–M4): Processors (Art. 28) {#fase-6-m3m4-processors-art-28}
1. Checklist de segurança para processadores  
2. Contrato do art. 28.º, n.º 3, com cada subcontratante que trate dados pessoais, em qualquer nível (CTX-RGPD-P01), com cláusulas técnicas de segurança; o conteúdo jurídico é do Jurídico/DPO  
3. O mesmo contrato com os subcontratantes que recebem dados pessoais em prompts de IA, em qualquer nível (Política 18 §10.3; CTX-RGPD-P02)  
4. Monitorização e revisão anual  
**Evidências:** Checklist; contratos; relatórios de revisão

### Fase 7 (M4–M5): Incidentes e Notificação 72h (Art. 33/34) {#fase-7-m4m5-incidentes-e-notificação-72h-art-3334}
1. Runbook com cronómetro de 72 h (art. 33.º) e o conteúdo mínimo da Política 32 §6.1: natureza da violação, categorias e número aproximado de titulares e de registos, contacto do EPD, consequências prováveis e medidas. Todas as violações ficam registadas, notificadas ou não, com a fundamentação (CTX-RGPD-R06); decisão, sem demora injustificada, sobre a comunicação aos titulares quando houver elevado risco (art. 34.º)  
2. Critério de elevado risco para a comunicação aos titulares; o conteúdo dessa comunicação (art. 34.º, n.º 2) é lacuna declarada do Manual, a preparar com o EPD  
3. Exercício anual de simulação  
**Evidências:** Runbook; registos exercício; relatório pós‑ação

### Fase 8 (M5–M6): Retenção & Eliminação Segura {#fase-8-m5m6-retenção--eliminação-segura}
1. Prazos de retenção por conjunto de dados pessoais, com apagamento efetivo que chega às réplicas, caches e cópias (PRI-002); o fundamento jurídico dos prazos é do Jurídico  
2. Jobs de eliminação ou anonimização agendados  
3. Nos registos e cópias imutáveis (WORM), pseudónimos e chave por titular, e apagamento por destruição da chave (Política 29 §8.1; PRI-005; CTX-RGPD-P05)  
4. Provas de execução (logs, relatórios)  
**Evidências:** Tabela retenções; logs eliminação; auditorias

---

## Checklists {#checklists}

### PbD/PbDf {#pbdpbdf}
- [ ] Requisitos PRI-001 a PRI-007 aplicados e verificados
- [ ] Defaults seguros aplicados (coleta mínima, cifragem)
- [ ] Gate de pipeline para schemas/dados
- [ ] Revisão periódica de configurações

### Art. 32 {#art-32}
- [ ] TLS 1.2+/1.3 e at rest encryption
- [ ] Gestão de chaves com rotação
- [ ] MFA e revisão de privilégios
- [ ] SAST/DAST/fuzzing integrados
- [ ] Backups testados; DR exercitado

### DPIA {#dpia}
- [ ] Critérios de gatilho definidos
- [ ] Threat Modeling anexado
- [ ] Análise LINDDUN anexada (THR-003)
- [ ] Aprovação DPO

### Incidentes 72h {#incidentes-72h}
- [ ] Runbook com o conteúdo mínimo da Política 32 §6.1 e registo de todas as violações (CTX-RGPD-R06)
- [ ] Cronómetro 72h visível (art. 33.º, a contar do conhecimento)
- [ ] Critério de elevado risco e comunicação aos titulares sem demora injustificada (art. 34.º)
- [ ] Exercício anual concluído
- [ ] Conteúdo da comunicação aos titulares preparado com o EPD (lacuna declarada do Manual, art. 34.º, n.º 2)

### Processors {#processors}
- [ ] Checklist de segurança aplicada
- [ ] Contrato do art. 28.º, n.º 3, em vigor com cada subcontratante
- [ ] Revisão anual e registos

### Retenção {#retenção}
- [ ] Tabela aprovada
- [ ] Jobs automáticos configurados
- [ ] Evidência de execução

---

## Métricas-Chave {#métricas-chave}
| Métrica | Definição | Objetivo |
|---------|-----------|---------|
| % apps com Art. 32 completo | Apps com cifragem+IAM+testes | ≥95% |
| Notificações dentro do prazo legal | Conhecimento → submissão à autoridade | 100% ≤ 72h (prazo legal, art. 33.º); um alvo interno mais curto, se existir, é da organização |
| % DPIA no prazo | DPIAs concluídas dentro do SLA | ≥90% |
| Conformidade retenção | Execução jobs vs. plano | ≥95% |

---

## Artefactos a Manter {#artefactos-a-manter}
- Política de proteção de dados (da organização; lacuna declarada do Manual, art. 24.º, n.º 2)
- ROPA export (GRC)
- Relatórios de testes e gates
- DPIAs com anexos técnicos
- Runbook 72h + registos exercício
- Tabelas de retenção + logs de eliminação
- Checklists/processors e contratos

---

## Notas {#notas}
- Incidentes podem acionar também NIS2/DORA. Recomenda-se runbook único com canais de reporte diferenciados.
- O LINDDUN faz parte do threat modeling em todos os níveis quando há dados pessoais, em forma leve em L1 (THR-003, [Cap. 03](/sbd-toe/sbd-manual/threat-modeling/intro)).

---

## Recursos Práticos de Implementação {#recursos-práticos-de-implementação}

Para suporte concreto na implementação deste playbook, consultar os seguintes exemplos reutilizáveis:

- 🛠️ **[Opções de Toolchain](../exemplo-playbook/exemplo-toolchain-options)** - Ferramentas de cifragem, anonimização e data minimization
- 📊 **[KPIs e Targets](../exemplo-playbook/exemplo-kpis-targets)** - Métricas de privacy e retenção de dados adaptáveis ao GDPR
- 👥 **[RACI e Governance](../exemplo-playbook/exemplo-raci-governance)** - Interface técnico/DPO e responsabilidades Art. 32
- 📝 **[Relatório de Incidentes](../exemplo-playbook/exemplo-relatorio-incidentes)** - Template adaptável para violação de dados (72h) Art. 33-34

Estes recursos demonstram implementações práticas alinhadas com GDPR.

---

## Referências {#referências}
- [Análise normativa GDPR](intro)
- EDPB - Guidelines DPIA, Breach Notification
- ENISA - Security of Personal Data Processing
- SbD-ToE [Cap. 01](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro)–[Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro)

**Versão:** 1.1  
**Data:** Setembro 2026  
**Nota:** Este playbook complementa a análise normativa GDPR com ações práticas
