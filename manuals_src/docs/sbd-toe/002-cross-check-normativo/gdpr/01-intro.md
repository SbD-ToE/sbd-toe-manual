---
id: intro
title: GDPR - Cross-Check Normativo
description: Como o SbD-ToE cobre requisitos técnicos do RGPD (UE 2016/679)
tags: [cross-check, gdpr, privacidade, protecao-dados, art32, privacy-by-design]
sidebar_position: 7
---

# GDPR: Cross-Check Normativo

> Para implementação prática, consulte o [Playbook SbD-ToE 4 GDPR](/sbd-toe/cross-check-normativo/gdpr/playbook).
>
> Para padrões aplicacionais universais, ver capítulos base do SbD-ToE (01–14).

## Âmbito {#âmbito}

O **Regulamento Geral sobre a Proteção de Dados (RGPD/GDPR)** - **Regulamento (UE) 2016/679** (CELEX: [32016R0679](https://eur-lex.europa.eu/legal-content/PT/TXT/?uri=CELEX:32016R0679)) - estabelece princípios e obrigações para o tratamento de dados pessoais. Este cross‑check foca a **dimensão técnica** alinhada ao SbD-ToE (segurança e engineering), reconhecendo que várias obrigações são **jurídico‑organizacionais**: bases legais, informação ao titular, resposta formal aos pedidos, metodologia da AIPD, EPD e transferências internacionais. Estas ficam fora do âmbito do Manual. A capacidade técnica de exercer os direitos dos titulares, essa, está prescrita (PRI-003, PRI-006; CTX-RGPD-R01 a R05).

Sugere-se usar o SbD-ToE como núcleo técnico para os artigos que exigem medidas de segurança, privacidade‑by‑design e gestão de incidentes, articulando com jurídico/GRC para o restante.

## O que este Manual cobre e o que fica de fora {#o-que-este-manual-cobre-e-o-que-fica-de-fora}

O SbD-ToE é centrado na aplicação: requisitos, arquitetura, código, dependências, pipeline, deploy e operação do software. Para cada obrigação do RGPD, o Manual responde numa de três categorias, e nenhuma obrigação fica em silêncio:

- **Cobre**, e diz de que forma: requisito do catálogo, política, piso ou requisito acrescentado pelo regime, ou evidência de engenharia para um dever de outro plano.
- **Lacuna declarada**: o que o Manual não cobre por omissão, com o que falta.
- **Fora de âmbito**: o que o Manual não trata, com a razão.

A lista completa, obrigação a obrigação, é gerada da matriz de cobertura e está em [Requisitos aplicáveis — O que este Manual cobre e o que fica de fora](./requisitos-aplicaveis#cobertura). Quando esta página e a lista divergirem, prevalece a lista.

**Fora de âmbito, por decisão do programa:**
- Segurança da entidade como um todo (rede corporativa e canais de administração, EDR, patching de sistemas operativos e equipamentos, inventário e classificação de todos os ativos): o Manual é centrado na aplicação.
- O lado jurídico: bases legais, resposta formal ao titular e prazos, metodologia da AIPD, encarregado da proteção de dados, transferências internacionais. O Manual cobre a parte técnica dos direitos (PRI-001 a PRI-007).

---

## PARTE I: ANÁLISE NORMATIVA (GDPR → SbD-ToE) {#parte-i-análise-normativa-gdpr--sbd-toe}

### Princípios (Art. 5) {#princípios-art-5}
Exigem: licitude, lealdade e transparência; limitação das finalidades; minimização dos dados; exatidão; limitação da conservação; integridade e confidencialidade; responsabilidade.

Cobertura SbD-ToE:
- Cap. 01: Classificação e identificação de dados por criticidade (apoia minimização/retensão)
- Cap. 02: Requisitos de segurança (confidencialidade, integridade, disponibilidade)
- Cap. 04: Arquitetura segura (segregação, encriptação, logging proporcional)
- Cap. 11: Validação antes de produção (confirmações de requisitos)
- Cap. 02 (catálogo PRI): minimização (PRI-001), retenção com apagamento efetivo (PRI-002), exatidão e rectificação (PRI-003), inventário de finalidades e destinatários (PRI-004), PII em registos (PRI-005)

**Fora do âmbito:** licitude e bases legais (art. 5.º, n.º 1, al. a), e art. 6.º). É matéria jurídica, tratada com o Jurídico/DPO.

---

### Consentimento e direitos dos titulares (arts. 7.º, 8.º e 12.º–22.º) {#direitos-dos-titulares-arts-7-22}
Exigem que o titular possa dar e retirar o consentimento e exercer os direitos de acesso, rectificação, apagamento, limitação, portabilidade e oposição, e que as decisões exclusivamente automatizadas tenham salvaguardas.

Cobertura SbD-ToE:
- Cap. 02 (catálogo PRI): acesso, rectificação, apagamento e exportação em formato de leitura automática, por mecanismo testado, com propagação aos destinatários registados (PRI-003, PRI-004; arts. 15.º, n.º 3, 16.º, 17.º, 19.º e 20.º, n.º 1) e verificação da identidade do requerente (PRI-003, AUT-009; art. 12.º, n.º 6)
- Limitação do tratamento (CTX-RGPD-R01; art. 18.º) e apagamento de dados tornados públicos (CTX-RGPD-R02; art. 17.º, n.º 2)
- Consentimento e oposição, incluindo sinais automatizados como o Global Privacy Control (PRI-006; CTX-RGPD-R04; arts. 7.º e 21.º)
- Verificação da idade e consentimento parental, quando aplicável (CTX-RGPD-R03; art. 8.º, n.º 2)
- Decisões exclusivamente automatizadas com intervenção humana, ponto de vista e contestação (CTX-RGPD-R05; art. 22.º)

**Lacunas declaradas:** a transmissão directa dos dados entre responsáveis, quando tecnicamente possível (art. 20.º, n.º 2); o canal de pedidos e o conteúdo informativo da resposta ao titular (arts. 12.º, n.º 2, e 15.º, n.º 1) só estão cobertos na parte técnica.

**Fora do âmbito:** a resposta formal ao titular, com prazos, fundamentação e custos (arts. 11.º, n.º 2, 12.º, n.os 3 a 5, e 18.º, n.º 3), e a informação ao titular, incluindo os avisos de privacidade (arts. 12.º, n.º 1, 13.º, 14.º e 21.º, n.º 4). São matéria jurídico-comunicacional, tratada com o Jurídico/DPO.

---

### Proteção de dados desde a conceção e por defeito (art. 25.º) {#privacy-by-designdefault-art-25}
Exige medidas que apliquem os princípios de proteção de dados desde a conceção e que, por defeito, só sejam tratados os dados pessoais necessários para cada finalidade (quantidade, extensão, conservação, acessibilidade).

Cobertura SbD-ToE:
- Cap. 04: Padrões arquiteturais seguros (pseudonimização, segmentação)
- Cap. 06–07: Pipelines com gates para evitar exposições (secrets, dados excessivos)
- Cap. 11: Checklists pré‑deploy (parâmetros de privacidade por defeito)
- Cap. 03: análise de ameaças de privacidade com LINDDUN em todos os níveis quando há dados pessoais, em forma leve em L1 (THR-003)
- Cap. 02: privacidade por defeito nas definições voltadas ao utilizador (PRI-007) e minimização (PRI-001)

---

### Registos de Atividades (Art. 30) {#registos-de-atividades-art-30}
Exige ROPA (Record of Processing Activities).

**Apoio à evidência:** o inventário de finalidades e destinatários por conjunto de dados (PRI-004, obrigatório em qualquer nível: CTX-RGPD-P04) e o inventário de aplicações (CLA-008) alimentam o registo do art. 30.º. O registo em si, como documento do responsável pelo tratamento, é mantido pelo Jurídico/DPO, com referência aos IDs das aplicações.

---

### Segurança do Tratamento (Art. 32) {#segurança-do-tratamento-art-32}
Exige medidas técnicas e organizativas adequadas ao risco, incluindo, consoante o adequado: pseudonimização e cifragem, confidencialidade/integridade/disponibilidade/resiliência, restabelecimento da disponibilidade e testes regulares da eficácia.

Cobertura SbD-ToE:
- Cap. 02: Requisitos mínimos por nível (inclui cifragem, IAM, hardening)
- Cap. 04: Arquitetura (segregação, gestão de chaves)
- Cap. 05: Gestão de vulnerabilidades e dependências (SBOM/SCA)
- Cap. 10: Testes de segurança e avaliação contínua
- Cap. 12: Monitorização, continuidade e exercícios

A adequação ao risco faz-se pela classificação (CLA-001, CLA-003) e pelo threat model, incluindo o risco para os titulares (THR-001, THR-002). As cópias de segurança com restauro testado incluem os dados pessoais (OPS-016; CTX-RGPD-P03).

---

### Notificação de Violação (Art. 33/34) {#notificação-de-violação-art-3334}
Exige notificar a autoridade de controlo competente sem demora injustificada e, sempre que possível, até 72 h após o conhecimento da violação, salvo se não for suscetível de resultar num risco (art. 33.º); se houver elevado risco, comunicar aos titulares (art. 34.º).

Cobertura SbD-ToE:
- Cap. 12: Deteção, classificação e resposta a incidentes; runbooks
- Cap. 14: RACI para decisões e comunicações

**Cobertura:** prazos, critério e conteúdo mínimo da notificação à autoridade de controlo (Política 32 §6 e §6.1) e registo de todas as violações, notificadas ou não, com a fundamentação da decisão (CTX-RGPD-R06). **Lacuna declarada:** o conteúdo mínimo da comunicação aos titulares (art. 34.º, n.º 2). **Fora do âmbito:** os formulários e a relação com a autoridade de controlo.

---

### DPIA - Avaliação de Impacto (Art. 35) {#dpia---avaliação-de-impacto-art-35}
Exige DPIA quando o tratamento é suscetível de alto risco.

Cobertura SbD-ToE (parcial):
- Cap. 03: Threat Modeling (pode servir de base técnica)
- Cap. 04: Medidas de mitigação técnicas

**Apoio à evidência:** o threat model com LINDDUN (THR-003) e a descrição sistemática do tratamento (THR-002) servem de anexo técnico da AIPD. **Fora do âmbito:** a metodologia da AIPD, a lista de tratamentos sujeitos e a consulta prévia à autoridade (arts. 35.º, n.os 3 e 9, e 36.º), que são matéria jurídica. **Lacuna declarada:** a revisão pelo EPD só existe em L3 e incide sobre a análise LINDDUN, não sobre a AIPD (art. 35.º, n.º 2).

---

### Subcontratantes (Art. 28) e Contratos {#subcontratantes-art-28-e-contratos}
Exige contratos com processadores com cláusulas de proteção de dados.

Cobertura SbD-ToE:
- Cap. 14: Ciclo de vida de fornecedores/contractors e cláusulas de segurança
- Cap. 05: Transparência de componentes (SBOM) e risco de terceiros

**Cobertura:** o contrato do art. 28.º, n.º 3, é obrigatório em qualquer nível sempre que um subcontratante trata dados pessoais (CTX-RGPD-P01; com os que recebem dados pessoais em prompts de IA: Política 18 §10.3, CTX-RGPD-P02), com segurança, apoio aos direitos e apagamento ou devolução no fim do serviço (als. c), e) e g); PRI-002, PRI-003). **Fora do âmbito:** o conteúdo jurídico das cláusulas e os mecanismos de transferência (SCC, BCR, derrogações). **Lacuna declarada:** regra de localização e transferência para os subcontratantes fora do EEE que não sejam fornecedores de IA (arts. 44.º e 46.º).

---

## PARTE II: Convergências/Interações {#parte-ii-convergênciasinterações}

- Incidentes com dados pessoais podem requerer dupla notificação: RGPD (72h) + regimes setoriais (p.ex., NIS2/DORA). Sugere-se runbook único com bifurcação de reporte.
- Medidas Art. 32 complementam controlos NIS2/DORA (mesma base técnica; evidência reaproveitável).

---

## Resumo: fora do âmbito e lacunas declaradas {#lacunas-intencionais-resumo}

O que o Manual cobre está nas secções acima; esta tabela reúne o que fica fora do âmbito, com a razão, e as lacunas declaradas.

| Área | Categoria | Razão / o que falta |
|---|---|---|
| Bases legais, informação ao titular (arts. 6.º, 13.º, 14.º) | Fora do âmbito | Matéria jurídica: Jurídico/DPO |
| Resposta formal aos pedidos dos titulares (prazos, fundamentação) | Fora do âmbito | «Direitos formais»; a capacidade técnica está em PRI-003 e PRI-006 |
| Metodologia da AIPD, consulta prévia | Fora do âmbito | Metodologia jurídico-organizacional; anexos técnicos em THR-002 e THR-003 |
| Estatuto e designação do EPD | Fora do âmbito | Organização jurídica |
| Responsáveis conjuntos e representante na UE (arts. 26.º, 27.º) | Fora do âmbito | Relação jurídica |
| Regime das transferências (SCC, BCR, derrogações) | Fora do âmbito | Jurídico/DPO |
| Localização e transferência de subcontratantes não-IA fora do EEE | Lacuna declarada | Só a fatia de fornecedores de IA tem regra (arts. 44.º e 46.º) |
| Política de proteção de dados | Lacuna declarada | Não há política dedicada entre as 39 (art. 24.º, n.º 2) |
| Conteúdo da comunicação aos titulares | Lacuna declarada | Art. 34.º, n.º 2 |
| Envolvimento do EPD em design, AIPD e subcontratantes | Lacuna declarada | Art. 38.º, n.º 1 |
| Transmissão directa entre responsáveis | Lacuna declarada | Art. 20.º, n.º 2 |

---

## Métrica Simples (Autoavaliação) {#métrica-simples-autoavaliação}

Cada «sim» conta um ponto:
1. As apps que tratam dados pessoais estão classificadas e têm requisitos de Art. 32 implementados?
2. Privacy by default configurada (PRI-007; logs mínimos, retenção limitada, cifragem por defeito)?
3. Existe processo de DPIA com anexos técnicos (TM com LINDDUN, controlos) quando aplicável?
4. Runbook de incidente com cronómetro 72h ativo e o conteúdo mínimo da Política 32 §6.1?
5. Processors: contrato do art. 28.º, n.º 3, com cláusulas técnicas e segurança verificada?

≥4/5 → Boa cobertura técnica. `<`3 → Priorizar Art. 32, PbD e incidentes 72h.

---

## Referências {#referências}

- **RGPD/GDPR**: Regulamento (UE) 2016/679 (CELEX: [32016R0679](https://eur-lex.europa.eu/legal-content/PT/TXT/?uri=CELEX:32016R0679))
- ENISA - Guidelines on Security of Personal Data Processing
- EDPB - Guidelines (DPIA, Breach Notification)
- SbD-ToE Capítulos 01–14

**Versão:** 1.1  
**Data:** Setembro 2026  
**Próxima revisão:** Março 2027
