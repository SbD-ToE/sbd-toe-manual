---
id: faq
title: FAQ - Perguntas Frequentes
description: Respostas rápidas sobre aplicabilidade, âmbito, compliance e implementação do SbD-ToE
tags: [faq, aplicabilidade, compliance, implementacao]
sidebar_position: 7
---

# FAQ - Perguntas Frequentes

## Âmbito e Aplicabilidade {#âmbito-e-aplicabilidade}

### Para quem é o SbD-ToE? {#para-quem-é-o-sbd-toe}

Organizações que:
- **Desenvolvem** software (produto próprio, ferramentas internas, apps para clientes).
- **Contratem** desenvolvimento (outsourcing, contractors, system integrators).
- **Adquirem** SaaS/PaaS/IaaS crítico e precisam validar segurança do fornecedor.
- **Operam** infraestrutura TIC crítica (on-prem, cloud, hybrid).
- Estão sujeitas a **regulação** (NIS2, DORA, CRA, GDPR) e precisam de evidências técnicas de conformidade.

O SbD-ToE **não** é apenas para empresas de software. É para qualquer organização com **sistemas TIC críticos**.

---

### A minha organização não desenvolve software. O SbD-ToE é relevante? {#a-minha-organização-não-desenvolve-software-o-sbd-toe-é-relevante}

**Sim, muito provavelmente.**

Mesmo sem desenvolvimento interno, a maioria das organizações:
- **Adquire ou contrata** software (ERP, CRM, core systems, SaaS).
- **Opera** infraestrutura (servidores, cloud, rede).
- **Gere dados sensíveis** (clientes, colaboradores, financeiros).

O SbD-ToE ajuda a:
- **Classificar** aplicações por criticidade (Cap. 01).
- **Definir requisitos** de segurança para fornecedores (Cap. 02, 14).
- **Validar segurança** de software adquirido (Cap. 10: pentests, auditorias).
- **Gerir fornecedores** conforme DORA/NIS2 (Cap. 05, 14: SBOM, contratos, SLAs).
- **Operar com resiliência** (Cap. 12: logs, backups, incidentes, monitorização).

**Exemplo:** Banco que usa SAP/Oracle (não desenvolve) ainda precisa de:
- Classificar o ERP como L3 (crítico).
- Exigir SBOM e SLAs de patch ao fornecedor.
- Integrar logs no SIEM corporativo.
- Fazer pentests anuais.
- Documentar tudo para auditoria DORA.

→ **Capítulos aplicáveis:** 01, 02, 05, 10, 12, 14.

---

### Qual a diferença entre SbD-ToE e ISO 27001? {#qual-a-diferença-entre-sbd-toe-e-iso-27001}

| Aspeto | SbD-ToE | ISO 27001 |
|--------|---------|-----------|
| **Foco** | Segurança **aplicacional** e pipeline (desenvolvimento, aquisição, operação de software) | Gestão de segurança da informação (ISMS) **organizacional** |
| **Nível** | Técnico-operacional detalhado | Alto nível, abstrato (controlos genéricos) |
| **Estrutura** | 14 capítulos por domínio técnico (SBOM, CI/CD, IaC, threat modeling, testes) | 93 controlos em 4 temas (anexo A da ISO/IEC 27001:2022) |
| **Certificável?** | Não (é framework interno) | Sim (certificação por CAB acreditado) |
| **Relação** | **Contribui** para controlos do anexo A com detalhe técnico (p. ex. A.8.8, A.8.25–A.8.29); não há cross-check publicado nem mapeamento controlo a controlo | **Exige** controlos; deixa "como" em aberto |

**Em termos práticos:**
- ISO 27001 diz: "Deve gerir vulnerabilidades técnicas" (controlo A.8.8 na edição de 2022).
- SbD-ToE diz: "Cap. 05 - Como fazer SBOM, SCA, patching com SLAs, exceções formais, integração CI/CD".

**Podem coexistir?** Sim, e devem. O SbD-ToE fornece o "como técnico" que pode apoiar a implementação e a auditoria ISO 27001.

---

## Compliance e Regulação {#compliance-e-regulação}

### O SbD-ToE cobre DORA/NIS2/CRA/GDPR? {#o-sbd-toe-cobre-doranis2cragdpr}

**Sim, mas de forma diferente:**

| Regulamento | Cobertura SbD-ToE | Lacunas intencionais | Cross-check |
|-------------|-------------------|---------------------|-------------|
| **DORA** | 80–90% dos requisitos técnicos (Art. 5/18/19–20/26–28) | Templates ITS, aprovação board formal, concentração de fornecedores | [02-dora.md](/sbd-toe/cross-check-normativo/dora/intro) |
| **NIS2** | 80–90% dos requisitos técnicos (Art. 20/21/23) | Registo autoridade nacional, templates de reporte | [NIS2.md](/sbd-toe/cross-check-normativo/nis2/intro) |
| **CRA** | 70–80% (SBOM, patching, disclosure, testes) | Marcação CE, declaração de conformidade, organismos notificados | [05-cra.md](/sbd-toe/cross-check-normativo/cra/intro) |
| **GDPR** | 60–70% (Art. 25/32: PbD, segurança do tratamento) | ROPA, base legal, DPIA completa, transferências internacionais | [07-gdpr.md](/sbd-toe/cross-check-normativo/gdpr/intro) |

**Princípio:** O SbD-ToE fornece o **núcleo técnico** reutilizável. As partes jurídico-administrativas (contratos, bases legais, declarações formais) são tratadas por Jurídico/GRC.

---

### Posso usar o SbD-ToE como evidência de compliance? {#posso-usar-o-sbd-toe-como-evidência-de-compliance}

**Como evidência de apoio, sim.** Cada capítulo gera artefactos reutilizáveis:

- **Matriz de classificação L1–L3** → apoia DORA art. 8.º, NIS2 art. 21.º e RGPD arts. 25.º e 32.º.
- **SBOM por release** → evidência para o CRA (anexo I, parte II, ponto 1; documentação técnica do anexo VII); apoia o DORA art. 28.º, sem substituir o registo de informações.
- **Relatórios SAST/DAST/pentest** → apoiam DORA arts. 24.º e 25.º, NIS2 art. 21.º e CRA anexo VII, ponto 6.
- **Runbook de incidentes** → apoia DORA arts. 17.º a 19.º, NIS2 art. 23.º e RGPD arts. 33.º e 34.º (prazos na Política 32 §6).
- **Contratos com fornecedores** → apoiam DORA arts. 28.º a 30.º, NIS2 art. 21.º, n.º 2, al. d), e RGPD art. 28.º.

**Um mesmo conjunto de evidências pode apoiar vários regimes e auditorias;** a conformidade continua a ser juízo da organização. O que cada regime pede, obrigação a obrigação, está no [cross-check normativo](/sbd-toe/cross-check-normativo/intro).

---

### E certificação? Há certificação SbD-ToE? {#e-certificação-há-certificação-sbd-toe}

**Não.** O SbD-ToE não é um esquema de certificação. É um **framework operacional interno**.

**Mas:** as evidências SbD-ToE podem ser reutilizadas para **acelerar e simplificar** certificações externas:
- **ISO 27001** (ISMS) - controlos técnicos do anexo A (sem mapeamento controlo a controlo)
- **EUCC** (esquema europeu adotado; o EUCS e o EU5G ainda não estão adotados) - evidências de segurança de produto/serviço
- **SOC 2 Type II** (para cloud/SaaS) - demonstração de Trust Service Criteria

**Importante:** Reutilizar evidências reduz o esforço (80–90%), mas não substitui a auditoria/avaliação independente necessária para a certificação formal.

Ver: [Certificação ENISA/CSA](/sbd-toe/cross-check-normativo/enisa-csa/intro)

---

## Implementação {#implementação}

### Quanto tempo demora implementar o SbD-ToE? {#quanto-tempo-demora-implementar-o-sbd-toe}

Depende da maturidade inicial:

| Cenário | Duração estimada | Fases prioritárias |
|---------|------------------|-------------------|
| **Greenfield** (nova organização/produto) | 3–6 meses | Cap. 01–02 (classificação/requisitos) → 06–07 (SDLC/CI-CD) → 12 (ops) |
| **Brownfield com maturidade baixa** | 6–12 meses | Cap. 01 (inventário) → 05 (SBOM/SCA) → 10 (testes) → 12 (incidentes) → 14 (governação) |
| **Brownfield com maturidade média** (já tem CI/CD, logs, etc.) | 4–8 meses | Gap analysis → Cap. 03 (TM) → 05 (SBOM) → 10 (testes avançados) → 14 (fornecedores) |
| **Compliance-driven** (DORA/NIS2 deadline) | 6–18 meses | Usar playbooks específicos ([DORA](/sbd-toe/cross-check-normativo/dora/playbook), [NIS2](/sbd-toe/cross-check-normativo/nis2/playbook)) |

**Nota:** A implementação é **iterativa** (não "big bang"). Começa-se por apps críticas (L3) e expande-se progressivamente.

---

### Preciso implementar todos os capítulos? {#preciso-implementar-todos-os-capítulos}

**Não necessariamente.** Depende do contexto:

**Obrigatórios para todos:**
- Cap. 01 (Classificação)
- Cap. 02 (Requisitos mínimos)
- Cap. 12 (Monitorização e operações)
- Cap. 14 (Governação)

**Condicionais:**
- **Desenvolves software?** → Cap. 06–07 (SDLC/CI-CD), Cap. 10 (testes).
- **Usas containers?** → Cap. 09.
- **Usas IaC?** → Cap. 08.
- **Apps L3 (críticas)?** → Cap. 03 (Threat Modeling), Cap. 04 (Arquitetura).
- **DORA/CRA?** → Cap. 05 (SBOM obrigatório).

**Princípio:** Implementa o que é **relevante e proporcional** ao risco.

---

### Quanto custa implementar o SbD-ToE? {#quanto-custa-implementar-o-sbd-toe}

Não há custo de licença (é framework aberto). Os custos são **internos** (tempo de equipa) e **ferramentas**:

| Item | Estimativa |
|------|-----------|
| Tempo de equipa (análise, políticas, setup) | 200–500 horas (1–3 FTEs × 3–6 meses) |
| Ferramentas (SAST/DAST/SCA) | 5k–50k€/ano (depende de escala; há opções open-source) |
| SIEM/logging | 10k–100k€/ano (ou cloud-native incluído) |
| Formação (equipa técnica + gestão) | 5k–20k€ |
| Auditoria/validação externa (opcional) | 10k–50k€ |

**ROI:** Redução de incidentes, aceleração de compliance, reutilização de evidências, menor custo de auditoria.

---

## Exceções e Desvios {#exceções-e-desvios}

### O que são "exceções" no SbD-ToE? {#o-que-são-exceções-no-sbd-toe}

**Exceção** = desvio formal de um requisito de segurança, com:
- Justificação técnica ou de negócio.
- Aprovação por autoridade designada (AppSec/CISO/Board, conforme criticidade).
- Período de validade (TTL).
- Plano de remediação ou compensação.
- Trilho auditado.

**Exemplo:** "Deploy de app L3 com CVE High conhecido, mas com WAF compensatório, aprovado por CISO, TTL 30 dias, patch agendado."

Ver: Cap. 02 addon 08, Cap. 05 addon 09, Cap. 14.

---

### Todas as exceções são permitidas? {#todas-as-exceções-são-permitidas}

**Não.** Há categorias de **exceções inaceitáveis**:

- Vulnerabilidades RCE críticas sem compensação.
- Ausência de MFA em apps L3.
- Dados sensíveis não cifrados.
- Violações de conformidade regulatória (ex: DORA/NIS2/GDPR).

**Regra:** Se o regulador ou a criticidade não o permite, não é exceção - é **não-conformidade**.

Ver: [DORA cross-check - Exceções](/sbd-toe/cross-check-normativo/dora/intro#gestão-de-exceções-e-desvios-artigos-5-1723-2427-2830-dora)

---

## Relação com Outros Frameworks {#relação-com-outros-frameworks}

### SbD-ToE vs. OWASP SAMM/BSIMM/SSDF? {#sbd-toe-vs-owasp-sammbsimmssdf}

| Framework | Tipo | Relação com SbD-ToE |
|-----------|------|---------------------|
| **OWASP SAMM** | Modelo de maturidade (self-assessment) | SbD-ToE **implementa** práticas SAMM com detalhe operacional |
| **BSIMM** | Observação descritiva (o que outros fazem) | SbD-ToE usa insights BSIMM como inspiração; vai além com prescrição |
| **NIST SSDF** | Práticas de desenvolvimento seguro (alto nível) | SbD-ToE mapeia e **detalha** cada prática SSDF |

**Convergência:** Todos falam de threat modeling, SAST/DAST, SBOM, testes. SbD-ToE **operacionaliza** com addons, templates, checklists.

---

### Posso usar SbD-ToE com DevSecOps? {#posso-usar-sbd-toe-com-devsecops}

**Sim, é o core do SbD-ToE.**

- Cap. 06–07: Integração de segurança em pipelines (shift-left).
- Cap. 10: Testes contínuos (SAST/DAST/fuzzing).
- Cap. 08–09: IaC e containers (infrastructure-as-code segura).
- Cap. 12: Observabilidade e resposta rápida.

**Princípio:** Segurança automatizada, não manual.

---

## Regulação Multi-Jurisdicional {#regulação-multi-jurisdicional}

### Estou sujeito a DORA + NIS2 + GDPR. Há duplicação? {#estou-sujeito-a-dora--nis2--gdpr-há-duplicação}

**Muito pouca.** A maioria dos controlos técnicos convergem:

- **Gestão de vulnerabilidades** → DORA Art. 5, NIS2 Art. 21, CRA (SBOM/patching).
- **Incidentes** → DORA Art. 18 (24h), NIS2 Art. 23 (24h/72h/1M), GDPR Art. 33 (72h).
- **Fornecedores** → DORA Art. 26–28, NIS2 Art. 21, GDPR Art. 28.
- **Testes** → DORA Art. 19–20, NIS2 Art. 21.

**Estratégia:**
1. Implementa SbD-ToE Cap. 01–14 (núcleo técnico comum).
2. Usa playbooks específicos para ajustes (campos de reporte, templates).
3. Runbook de incidentes único com bifurcação de canais (DORA → EBA, NIS2 → CSIRT, GDPR → DPO).

Ver: [Convergência DORA & NIS2](/sbd-toe/cross-check-normativo/dora/convergencia-dora)

---

## Métricas e Melhoria Contínua {#métricas-e-melhoria-contínua}

### Como medir se estou "SbD-ToE compliant"? {#como-medir-se-estou-sbd-toe-compliant}

Métricas-chave por capítulo:

| Capítulo | Métrica |
|----------|---------|
| **Cap. 01** | % apps classificadas (L1–L3) |
| **Cap. 02** | % apps com requisitos mínimos implementados |
| **Cap. 05** | % releases com SBOM; MTTP (tempo médio até patch) |
| **Cap. 07** | % commits com gates de segurança passados |
| **Cap. 10** | Cobertura SAST/DAST; % releases bloqueadas por CVE crítico |
| **Cap. 12** | MTTD/MTTR (tempo até deteção/resposta); % backups testados |
| **Cap. 14** | % fornecedores com contratos auditados; % exceções no prazo |

**Dashboard único** com KPIs agregados: "SbD-ToE Compliance Score".

---

### O SbD-ToE é "one-time" ou contínuo? {#o-sbd-toe-é-one-time-ou-contínuo}

**Contínuo.**

- Novas apps → classificar (Cap. 01).
- Novos CVEs → patch/excepção (Cap. 05).
- Mudanças arquiteturais → re-TM (Cap. 03).
- Novos fornecedores → onboarding (Cap. 14).
- Exercícios trimestrais → incidentes/DR (Cap. 12).

**Revisão formal:** Anual (políticas, exceções, gaps).

---

## Próximos Passos {#próximos-passos}

### Por onde começo? {#por-onde-começo}

1. **Ler:** [Como usar este manual](/sbd-toe/sbd-manual/fundamentos/como-usar)
2. **Inventariar:** Cap. 01 - Listar e classificar apps críticas.
3. **Gap analysis:** Comparar estado atual vs. requisitos Cap. 02.
4. **Quick wins:** Cap. 05 (SBOM), Cap. 12 (logs centralizados), Cap. 14 (RACI).
5. **Roadmap:** Escolher playbook relevante ([DORA](/sbd-toe/cross-check-normativo/dora/playbook), [NIS2](/sbd-toe/cross-check-normativo/nis2/playbook), [CRA](/sbd-toe/cross-check-normativo/cra/playbook), [GDPR](/sbd-toe/cross-check-normativo/gdpr/playbook)).

---

### Onde obter suporte? {#onde-obter-suporte}

- **Documentação completa:** SbD-ToE Capítulos 01–14
- **Cross-checks normativos:** Secção 002
- **Playbooks práticos:** Ver cada regulamento
- **Comunidade:** (a definir - fórum, GitHub Discussions, etc.)

---

**Versão:** 1.0  
**Data:** Novembro 2025  
**Próxima revisão:** Maio 2026
