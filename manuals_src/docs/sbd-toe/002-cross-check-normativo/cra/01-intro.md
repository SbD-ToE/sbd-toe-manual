---
id: intro
title: CRA - Cross-Check Normativo
description: Análise de como o SbD-ToE suporta o núcleo técnico do Cyber Resilience Act em contexto de produtos com elementos digitais, com fronteiras explícitas de conformidade
tags: [cross-check, cra, regulamentacao, produtos-digitais, sbom, vulnerabilidades]
sidebar_position: 5
---

# CRA: Cross-Check Normativo

> Para implementação prática, consulte o [Playbook SbD-ToE 4 CRA](/sbd-toe/cross-check-normativo/cra/playbook).
> 
> Para padrões aplicacionais universais, ver capítulos base do SbD-ToE (01–14).
>
> Para a resposta obrigação a obrigação (o que o Manual cobre, as lacunas declaradas e o que fica fora de âmbito) e para os requisitos que se aplicam sob o contexto `CTX-CRA`, consulte [Requisitos aplicáveis](/sbd-toe/cross-check-normativo/cra/requisitos-aplicaveis).

## Âmbito {#âmbito}

### 🧩 CRA - Cyber Resilience Act {#-cra---cyber-resilience-act}

O **Cyber Resilience Act (CRA)** é o **Regulamento (UE) 2024/2847** (CELEX: [32024R2847](https://eur-lex.europa.eu/legal-content/PT/TXT/?uri=CELEX:32024R2847)), que estabelece requisitos horizontais para a conceção, desenvolvimento, produção e suporte de produtos com elementos digitais.

Nesta leitura, o `CRA` deve ser entendido antes de mais como enquadramento de:

- produto com elementos digitais
- fabricante e outros operadores económicos
- obrigações técnicas suportadas por evidência
- e rota formal de conformidade separada

O CRA impõe obrigações aos fabricantes, importadores e distribuidores, incluindo:

- requisitos essenciais de **segurança por conceção e por defeito** durante todo o ciclo de vida;
- processos de **gestão de vulnerabilidades**, incluindo receção, análise, correção e divulgação responsável;
- **tratamento de vulnerabilidades durante o período de apoio** (Anexo I, Parte II) e correção sem demora;
- requisitos de **documentação técnica**, instruções e informação ao utilizador — a documentação técnica e a declaração de conformidade UE ficam à disposição das autoridades de fiscalização do mercado «por, pelo menos, 10 anos após a data de colocação no mercado do produto com elementos digitais ou pelo período de apoio, consoante o que for mais longo» (art. 13.º, n.º 13);
- obrigações de **notificação de vulnerabilidades exploradas ativamente e incidentes graves**.

### Gate de âmbito {#gate-de-âmbito}

Esta leitura local do `CRA` é mais defensável quando aplicada a:

- fabricantes de software ou produtos com elementos digitais
- fornecedores que precisam de evidência técnica para uma superfície de conformidade de produto
- contextos onde exista um produto, uma versão, um período de suporte e uma cadeia de responsabilidades de operador económico

Fora desse contexto, o SbD-ToE continua útil como base técnica, mas a leitura deixa de ser uma leitura `CRA` plena e passa a ser apenas suporte parcial.

No contexto do SbD-ToE, o CRA é operacionalizado através de:

- práticas de engenharia segura (capítulos de requisitos, arquitetura, desenvolvimento, IaC, pipelines, testes);
- gestão de SBOM, proveniência e supply chain (dependências, containers, imagens, CI/CD);
- processos estruturados de _vulnerability handling_ e _incident handling_;
- governação e contratos (incluindo subcontratantes e fornecedores de software/serviços).

> ⚖️ **Nota sobre referências técnicas.**  
> O CRA exige a SBOM «num formato de uso corrente e legível por máquina que abranja, pelo menos, as dependências de nível superior dos produtos» (anexo I, parte II, ponto 1), sem impor um formato concreto; a Comissão pode especificá-lo por atos de execução (art. 13.º, n.º 24).  
> Padrões como **CycloneDX**, **SPDX**, **ISO/IEC 29147 (Vulnerability Disclosure)** e **ISO/IEC 30111 (Vulnerability Handling)** são amplamente reconhecidos e fornecem uma base sólida para cumprir os requisitos técnicos e processuais do regulamento.  
> O SbD-ToE assume estes padrões como **boas práticas recomendadas**, não como requisitos legais em si mesmos.

O SbD-ToE foi desenhado para aplicações e pipelines software; grande parte dos controlos técnicos e processuais **alinha com o núcleo de obrigações CRA**. Este documento responde a cada obrigação numa de três categorias (cobre, lacuna declarada, fora de âmbito) e indica as ações de adaptação, sem fingir que a conformidade de produto fica exausta no manual base.

## O que este Manual cobre e o que fica de fora {#o-que-este-manual-cobre-e-o-que-fica-de-fora}

O SbD-ToE é centrado na aplicação: requisitos, arquitetura, código, dependências, pipeline, deploy e operação do software. Para cada obrigação do CRA, o Manual responde numa de três categorias, e nenhuma obrigação fica em silêncio:

- **Cobre**, e diz de que forma: requisito do catálogo, política, piso ou requisito acrescentado pelo regime, ou evidência de engenharia para um dever de outro plano.
- **Lacuna declarada**: o que o Manual não cobre por omissão, com o que falta.
- **Fora de âmbito**: o que o Manual não trata, com a razão.

A lista completa, obrigação a obrigação, é gerada da matriz de cobertura e está em [Requisitos aplicáveis — O que este Manual cobre e o que fica de fora](./requisitos-aplicaveis#cobertura). Quando esta página e a lista divergirem, prevalece a lista.

Quando a aplicação é ou integra um produto com elementos digitais colocado no mercado, declara-se o contexto `CTX-CRA`. O contexto eleva quatro requisitos a obrigatórios em qualquer nível (pisos `CTX-CRA-P01` a `P04`: bloqueio por vulnerabilidade explorável conhecida, sem exceção na colocação no mercado, diligência devida sobre componentes de terceiros, divulgação coordenada com ponto de contacto único) e acrescenta cinco requisitos próprios do regime (`CTX-CRA-R01` a `R05`: período de apoio, mecanismo de atualizações de segurança, avisos públicos sobre vulnerabilidades corrigidas, comunicação ao mantenedor de componentes, critério de incidente grave).

**Fora de âmbito, por decisão do programa:**
- Segurança da entidade como um todo (rede corporativa e canais de administração, EDR, patching de sistemas operativos e equipamentos, inventário e classificação de todos os ativos): o Manual é centrado na aplicação.
- Avaliação da conformidade, marcação CE e declaração UE de conformidade. A documentação técnica (anexo VII) tem mapa de evidência na [página gerada](./requisitos-aplicaveis#mapa-evidencia).

## Aviso Regulatório {#aviso-regulatório}

O CRA introduz obrigações de: classificação como produto importante (classes I/II, Anexo III) ou crítico (Anexo IV), marcação CE, declaração de conformidade, avaliação de conformidade (inclui módulos com envolvimento de organismos notificados em certas categorias), obrigações pós-comercialização (vulnerability handling), e notificação de vulnerabilidades ativamente exploradas, em simultâneo, à CSIRT designada como coordenadora e à ENISA, através da plataforma única de comunicação de informações (art. 14.º e 16.º): notificação de alerta precoce no prazo de 24 horas após o conhecimento, notificação de vulnerabilidade no prazo de 72 horas e relatório final o mais tardar 14 dias após a disponibilização de uma medida corretiva ou de atenuação; os incidentes graves que afetem a segurança do produto seguem o mesmo circuito (24 horas, 72 horas e relatório final no prazo de um mês). O art. 14.º é aplicável desde 11 de setembro de 2026 (art. 71.º, n.º 2).

Também convém fixar duas datas operacionais do regulamento:

- `Article 14` aplica-se a partir de `11 September 2026`
- a aplicação geral do regulamento arranca a `11 December 2027`

O SbD-ToE cobre o "como" técnico, mas **não substitui**:
- Procedimentos formais de avaliação da conformidade (módulo A; módulos B + C; módulo H; ou sistema europeu de certificação da cibersegurança, art. 32.º)
- Interações com organismos notificados
- Emissão da declaração UE de conformidade / marcação CE
- Processo jurídico de responsabilidade do fabricante/importador/distribuidor

## PARTE I: Obrigações CRA vs. SbD-ToE {#parte-i-obrigações-cra-vs-sbd-toe}

| Domínio CRA | Referência Regulamentar (Resumo) | Cobertura SbD-ToE | Lacuna declarada ou fora de âmbito | Ação de Adaptação |
|-------------|----------------------------------|-------------------|------------------------------------|-------------------|
| Gestão do Ciclo de Vida Seguro | Requisitos de segurança aplicável durante todo o ciclo (design → desenvolvimento → distribuição → manutenção) | Cap. 02 (requisitos), Cap. 06 (desenvolvimento), Cap. 07 (CI/CD), Cap. 11 (pré-deploy); período de apoio: `CTX-CRA-R01` | Lacuna declarada: política de versões suportadas (art. 13.º, n.º 10), canais beta ou de pré-lançamento (art. 4.º, n.º 3), classificação do produto nas categorias dos anexos III e IV (art. 7.º, n.º 1). Fora de âmbito: papel do operador económico, por ser qualificação jurídica | Declarar o contexto `CTX-CRA` por aplicação ou produto e determinar o período de apoio conforme `CTX-CRA-R01` |
| Identificação e Gestão de Vulnerabilidades | Processos para receber, avaliar, priorizar e corrigir vulnerabilidades | Cap. 05 (SBOM/SCA), Cap. 10 (testes), Cap. 12 (monitorização), Addons exceções; `GOV-015` (política de divulgação coordenada e canal de receção de relatos externos; piso `CTX-CRA-P04`) | — | Publicar a política de divulgação coordenada e o ponto de contacto único conforme `GOV-015` e o piso `CTX-CRA-P04` (anexo I, parte II, pontos 5 e 6) |
| SBOM / Transparência | Disponibilização de informação de componentes e dependências críticas | Cap. 05 (SBOM contínuo em CycloneDX ou SPDX, `DEP-001`) | Lacuna declarada: indicar ao utilizador onde aceder à SBOM, quando o fabricante a disponibiliza (anexo II, ponto 9) | Criar rotina de export SBOM sanitizada para stakeholders |
| Correções e Patches Rápidos | Aplicar correções de segurança sem demora injustificada | Cap. 05 (gestão CVE), Cap. 07 (automação CI/CD), Cap. 12 (deteção de exploração); distribuição das atualizações: `CTX-CRA-R02` | — (o CRA pede que as vulnerabilidades sejam resolvidas e corrigidas «sem demora» (anexo I, parte II, ponto 2), sem fixar dias) | Aplicar a escada interna única de remediação do Manual ([Cap. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/aplicacao-lifecycle)) como operacionalização do «sem demora» — escolha do Manual, não prazo do CRA |
| Reporte de vulnerabilidades ativamente exploradas | Notificar a CSIRT designada como coordenadora e a ENISA, através da plataforma única, das vulnerabilidades ativamente exploradas e dos incidentes graves: alerta precoce ≤24 h, notificação ≤72 h e relatório final (art. 14.º; aplicável desde 11.9.2026) | Cap. 12 (deteção, métricas exploração), Cap. 14 (governança); [Política 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória) (prazos, destinatários e informação aos utilizadores afetados); critério de incidente grave: `CTX-CRA-R05` | Lacuna declarada: conteúdo mínimo de cada notificação (art. 14.º, n.os 2 e 4), relatório intercalar a pedido da CSIRT (n.º 6) e regra de determinação da CSIRT coordenadora (n.º 7) | Completar o runbook de notificação com o conteúdo mínimo de cada notificação e o relatório intercalar |
| Medidas para Prevenção de Vulnerabilidades | Controlo de qualidade e testes de segurança antes de release | Cap. 10 (SAST/DAST/fuzzing), Cap. 11 (gate de release); `DEP-002` com o piso `CTX-CRA-P01` | — | Bloquear qualquer vulnerabilidade explorável conhecida, em qualquer nível e além do critério de severidade (piso `CTX-CRA-P01`): o CRA pede a disponibilização «sem nenhuma vulnerabilidade passível de ser explorada conhecida» (anexo I, parte I, ponto 2, al. a)) |
| Documentação de Segurança | Instruções e info de segurança para utilizadores/admins | Cap. 04 (arquitetura), Cap. 11 (deploy seguro); ponto de contacto: `GOV-015` (piso `CTX-CRA-P04`); período e fim do apoio: `CTX-CRA-R01`; instruções de atualização: `CTX-CRA-R02` | Lacuna declarada: guia de colocação em funcionamento e utilização segura, efeito de alterações do produto na segurança dos dados, desativação segura e remoção de dados (anexo II, ponto 8, als. a), b) e d)); conteúdo, língua e conservação das instruções (art. 13.º, n.º 18) | Criar o artefacto "Guia de Segurança do Produto" para as partes em lacuna |
| Monitorização Pós-Comercialização | Observação contínua de exploração e falhas | Cap. 12 (monitorização, alertas) | — | Criar backlog específico "Feedback Segurança" + triagem semanal |
| Gestão de Exceções | Justificação de desvios temporários | Cap. 02 addon 08, Cap. 05 addon 09, Cap. 14 governance; [Política 12 §4](/sbd-toe/assets/policies/policy-excecoes-cve#4-tipos-de-exceção) com o piso `CTX-CRA-P02` | — | Aplicar o piso `CTX-CRA-P02`: as exceções «fix deferred» e «risk accepted» não se aplicam a vulnerabilidades exploráveis conhecidas na colocação no mercado, e o piso não admite justificação |
| Segurança na Cadeia | Componentes de terceiros seguros, verificação de integridade | Cap. 05 (SCA), Cap. 07 (pipeline), Cap. 09 (runtime containers); `DEP-006` com o piso `CTX-CRA-P03`; comunicação ao mantenedor do componente: `CTX-CRA-R04` | Fora de âmbito: firmware, hardware e arranque seguro, porque o Manual é centrado na aplicação | Aplicar `DEP-006` com o piso `CTX-CRA-P03` e o acrescento `CTX-CRA-R04` |
| Conformidade e CE Mark | Declaração e marcação de conformidade | — | Fora de âmbito: plano da conformidade formal e do mercado (declaração UE, marcação CE, organismos notificados), fora do âmbito de um manual de engenharia de segurança de software | Estabelecer processo paralelo GRC + jurídico; o Manual fornece a evidência técnica |

## PARTE II: Cobertura Detalhada {#parte-ii-cobertura-detalhada}

### 1. Ciclo de Vida Seguro {#1-ciclo-de-vida-seguro}
O SbD-ToE define gates de segurança desde a classificação até ao deploy. Isto suporta a obrigação CRA de garantir segurança "by design" e durante a manutenção.

O papel do operador económico (fabricante, importador, distribuidor) é uma qualificação jurídica e fica fora de âmbito. O período de apoio e a comunicação do fim do apoio ao utilizador estão prescritos no contexto `CTX-CRA` (`CTX-CRA-R01`).

**Ação:** Consolidar num documento único: "Matriz de Controle CRA" listando controlos por fase (design, build, test, release, manutenção).

### 2. Vulnerability Handling & Coordinated Disclosure {#2-vulnerability-handling--coordinated-disclosure}
SbD-ToE já prevê triagem interna (SCA, scans, testes). O CRA exige também uma política de divulgação coordenada e um canal externo para investigadores ou utilizadores reportarem falhas (anexo I, parte II, pontos 5 e 6). O Manual prescreve a política de divulgação coordenada e o canal de receção de relatos externos (`GOV-015`), que o contexto `CTX-CRA` torna obrigatórios em qualquer nível, com ponto de contacto único (piso `CTX-CRA-P04`).

**Ação:** Publicar a política e o ponto de contacto conforme `GOV-015` e o piso `CTX-CRA-P04`.

### 3. SBOM e Transparência {#3-sbom-e-transparência}
SBOM contínuo (Cap. 05) é base para fornecer visibilidade. O CRA exige a SBOM num formato de uso corrente e legível por máquina (anexo I, parte II, ponto 1); o Cap. 05 cumpre-o com CycloneDX ou SPDX (`DEP-001`).

**Ação:** Gerar export sanitized (sem caminhos internos sensíveis) e manter versão por release maior.

### 4. Patching Rápido {#4-patching-rápido}
Aplicar a escada interna de remediação do Manual ([Política 19 §4.3](/sbd-toe/assets/policies/policy-estrategia-testes#43-slas-de-triagem-e-resolução); escolha do Manual) como operacionalização do «sem demora» do CRA (anexo I, parte II, ponto 2); com indício de exploração ativa, o prazo antecipa-se. Integrar no pipeline: se CVE crítico → tarefa automática + alerta CISO.

**Ação:** Automação: Workflow CI que abre issue + etiqueta "CRA-Patch".

### 5. Reporte de Vulnerabilidade Explorada {#5-reporte-de-vulnerabilidade-explorada}
Quando exploração confirmada (telemetria, IOC, prova), gerar relatório mínimo: ID vulnerabilidade, componente, versão afetada, impacto, mitigação temporária, prazo patch.

Prazos do art. 14.º (aplicável desde 11.9.2026), à CSIRT designada como coordenadora e à ENISA, pela plataforma única: notificação de alerta precoce ≤ 24 h e notificação de vulnerabilidade ≤ 72 h após o conhecimento; relatório final ≤ 14 dias após a disponibilização da medida corretiva ou de atenuação. Para incidentes graves: 24 h, 72 h e relatório final ≤ 1 mês após a notificação. O fabricante informa também os utilizadores afetados (art. 14.º, n.º 8).

Isto deve ser lido como base técnica para cumprir a obrigação de reporte, não como substituto da surface regulatória completa de `Articles 14-16`, que inclui notificação formal, coordenação institucional e comunicação a utilizadores quando aplicável.

**Ação:** Script de extração (ex: export do SIEM + SBOM) → JSON pronto.

### 6. Qualidade e Testes de Segurança {#6-qualidade-e-testes-de-segurança}
SbD-ToE cobre variedade de testes. Alinhar com a exigência do CRA de disponibilizar o produto no mercado sem vulnerabilidades exploráveis conhecidas (Anexo I, Parte I, 2(a), com base na avaliação dos riscos).

**Ação:** Gate que bloqueia qualquer vulnerabilidade explorável conhecida antes de release, em qualquer nível (`DEP-002`, piso `CTX-CRA-P01`). Estas vulnerabilidades não admitem exceção na colocação no mercado (piso `CTX-CRA-P02`).

### 7. Documentação de Segurança do Produto {#7-documentação-de-segurança-do-produto}
Gerar guia para administradores/utilizadores: configurações seguras, atualização, contacto de segurança, políticas de logging.

Para leitura `CRA`, o ponto de contacto de segurança (`GOV-015`, piso `CTX-CRA-P04`), o período de apoio e a data do seu fim (`CTX-CRA-R01`) e as instruções para instalar as atualizações (`CTX-CRA-R02`) estão prescritos. Ficam como lacuna declarada o guia de colocação em funcionamento e utilização segura, as instruções sobre o efeito de alterações na segurança dos dados e sobre a desativação e remoção de dados, e a indicação de onde aceder à SBOM (anexo II, pontos 8 e 9).

**Ação:** Template derivado de Cap. 04 (arquitetura) + Cap. 11 (deploy seguro).

### 8. Monitorização Pós-Comercialização {#8-monitorização-pós-comercialização}
Cap. 12 já define monitorização; adicionar painéis específicos: "Vulnerabilidades conhecidas vs. status patch".

**Ação:** Dashboard com: total vulns abertas, tempo médio patch, percentagem SLA atendido.

### 9. Exceções {#9-exceções}
No contexto CRA, as exceções «fix deferred» e «risk accepted» não se aplicam a vulnerabilidades exploráveis conhecidas no momento da colocação no mercado, seja qual for o tipo ou a severidade (piso `CTX-CRA-P02`, [Política 12 §4](/sbd-toe/assets/policies/policy-excecoes-cve#4-tipos-de-exceção)). As restantes seguem a política geral de exceções.

**Ação:** Aplicar o piso `CTX-CRA-P02` nas aplicações que declaram o contexto `CTX-CRA`.

### 10. Cadeia de Fornecimento {#10-cadeia-de-fornecimento}
A diligência devida sobre componentes de terceiros é `DEP-006`, obrigatória em qualquer nível no contexto CRA (piso `CTX-CRA-P03`); a comunicação ao mantenedor de uma vulnerabilidade num componente é `CTX-CRA-R04`.

**Fora de âmbito:** firmware, hardware, módulos criptográficos físicos e arranque seguro. O Manual é centrado na aplicação; uma organização com estes elementos no produto precisa de processo próprio.

### 11. Conformidade e Marcação CE {#11-conformidade-e-marcação-ce}
Fora de âmbito: é o plano da conformidade formal e do mercado (declaração UE, marcação CE, organismos notificados), fora do âmbito de um manual de engenharia de segurança de software. Requer processo documental legal.

**Ação:** Criar swimlane separado GRC/Jurídico; manter referência dos controlos técnicos como evidência de segurança.

## Lacunas declaradas e fora de âmbito {#lacunas-intencionais}

O canal de divulgação coordenada (`GOV-015`, piso `CTX-CRA-P04`) e o formato da SBOM (`DEP-001`, CycloneDX ou SPDX) estão cobertos e já não constam desta secção. A lista completa, obrigação a obrigação, está em [Requisitos aplicáveis](./requisitos-aplicaveis#cobertura); as tabelas abaixo agrupam-na.

**Lacunas declaradas** (o Manual não cobre, ou cobre só em parte):

| Grupo | Obrigações | O que falta |
|-------|------------|-------------|
| Produto e ciclo de vida | Art. 4.º, n.º 3; art. 7.º, n.º 1; art. 13.º, n.os 10 e 14 | Regra para canais beta ou de pré-lançamento; classificação do produto nas categorias dos anexos III e IV, que determinam a rota de conformidade; política de versões suportadas; acompanhamento das normas harmonizadas e especificações comuns |
| Avaliação de riscos | Art. 13.º, n.os 3 e 4 | Avaliação de riscos estruturada requisito essencial a requisito essencial e integrada na documentação técnica |
| Requisitos do produto entregue | Anexo I, parte I, ponto 2, als. b), f), g), i), l) e m) | Configuração segura por defeito do produto entregue e reposição do estado original; comunicação de corrupções ao utilizador; minimização de dados não pessoais; não degradar outros dispositivos ou redes; opção de exclusão do registo pelo utilizador; remoção e transferência seguras de todos os dados |
| Informação ao utilizador | Anexo II, pontos 8 (als. a), b), d)) e 9; art. 13.º, n.º 18 | Guia de colocação em funcionamento e utilização segura; efeito de alterações na segurança dos dados; desativação segura e remoção de dados; onde aceder à SBOM; conteúdo, língua e conservação das instruções |
| Conservação da documentação | Art. 13.º, n.º 13 | O Manual aplica os 10 anos à SBOM e ao pacote de evidências, mas não ainda às versões do threat model nem aos registos de aprovação |
| Notificações do art. 14.º | Art. 14.º, n.os 2, 4, 6 e 7 | Conteúdo mínimo de cada notificação; relatório intercalar a pedido da CSIRT; regra de determinação da CSIRT coordenadora |

**Fora de âmbito** (o Manual não trata, com a razão):

| Área | Razão |
|------|-------|
| Declaração UE de conformidade, marcação CE, organismos notificados, relação com autoridades e regime sancionatório | Plano jurídico, da conformidade formal e do mercado, fora do âmbito de um manual de engenharia de segurança de software |
| Deveres de importadores, distribuidores e mandatários; requalificação como fabricante (arts. 21.º e 22.º) | Dever de outro operador económico, ou qualificação jurídica |
| Administrador de software de código aberto (art. 24.º) | O Manual não modela esse papel |
| Identificação do fabricante no produto e contactos na embalagem (art. 13.º, n.º 16; anexo II, ponto 1); indicação comercial da data de fim do apoio no ato de compra | Rotulagem e plano de mercado |
| Notificação voluntária (art. 15.º) | Faculdade, não dever |
| Regime transitório e listas de categorias de produto (anexos III e IV) | Plano jurídico; as listas determinam a rota de conformidade |
| Firmware, hardware e arranque seguro | O Manual é centrado na aplicação |

## Métrica Simples CRA (Autoavaliação) {#métrica-simples-cra-autoavaliação}

Responda SIM ou NÃO aos seguintes pontos:
1. Existe política de segurança do produto cobrindo design→manutenção?
2. Há SBOM completo gerado por release?
3. Existe canal público de vulnerability disclosure (`GOV-015`)?
4. SLA de patch documentado e monitorizado?
5. Gate que bloqueia qualquer vulnerabilidade explorável conhecida (piso `CTX-CRA-P01`)?
6. Dashboard de vulnerabilidades pós-comercialização ativo?
7. Export SBOM externa sanitizada disponível para clientes/reguladores?
8. Política de exceções sem exceção para vulnerabilidades exploráveis conhecidas na colocação no mercado (piso `CTX-CRA-P02`)?
9. Guia de Segurança do Produto publicado?
10. Processo de reporte de exploração ativa documentado?

≥8/10 → Boa base técnica CRA. `<`6 → Priorizar SBOM, patching, disclosure, gating por explorabilidade. Os limiares são escolha do Manual, não critério do CRA.

## Ações Prioritárias (Roadmap Inicial) {#ações-prioritárias-roadmap-inicial}

1. Declarar o contexto `CTX-CRA` nas aplicações abrangidas e aplicar os seus pisos (`CTX-CRA-P01` a `P04`) e acrescentos (`CTX-CRA-R01` a `R05`), incluindo o período de apoio 
2. Publicar a política de divulgação coordenada e o ponto de contacto único (`GOV-015`, piso `CTX-CRA-P04`) 
3. Ajustar o pipeline com o gate por vulnerabilidade explorável conhecida (`DEP-002`, piso `CTX-CRA-P01`) 
4. Definir SLA patch CRA e métricas de acompanhamento 
5. Gerar SBOM e export CycloneDX por release 
6. Fechar as lacunas declaradas da informação ao utilizador (guia de utilização segura, efeito de alterações, desativação e remoção de dados, acesso à SBOM) 
7. Completar o runbook de reporte do art. 14.º com o conteúdo mínimo de cada notificação e o relatório intercalar 
8. Adicionar dashboard pós-comercialização 
9. Definir a política de versões suportadas 
10. Swimlane CE Conformidade (jurídico + GRC), fora do âmbito do Manual

## Referências {#referências}

- **Cyber Resilience Act**: Regulamento (UE) 2024/2847 (CELEX: [32024R2847](https://eur-lex.europa.eu/legal-content/PT/TXT/?uri=CELEX:32024R2847))
- SbD-ToE Manual Capítulos 01–14 
- ENISA Guidance on Product Security & Vulnerability Disclosure 
- ISO/IEC 29147 (Vulnerability Disclosure), ISO/IEC 30111 (Vulnerability Handling)
- CycloneDX / SPDX especificações

**Versão:** 1.1  
**Data:** Setembro 2026 (alinhada com a matriz de cobertura e o contexto `CTX-CRA`)
