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
> O CRA não impõe um formato único de SBOM nem obriga explicitamente ao uso de normas específicas.  
> No entanto, padrões como **CycloneDX**, **SPDX**, **ISO/IEC 29147 (Vulnerability Disclosure)** e **ISO/IEC 30111 (Vulnerability Handling)** são amplamente reconhecidos e fornecem uma base sólida para cumprir os requisitos técnicos e processuais do regulamento.  
> O SbD-ToE assume estes padrões como **boas práticas recomendadas**, não como requisitos legais em si mesmos.

O SbD-ToE foi desenhado para aplicações e pipelines software; grande parte dos controlos técnicos e processuais **alinha com o núcleo de obrigações CRA**. Este documento identifica cobertura, lacunas intencionais e ações de adaptação, sem fingir que a conformidade de produto fica exausta no manual base.

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

| Domínio CRA | Referência Regulamentar (Resumo) | Cobertura SbD-ToE | Lacuna Intencional | Ação de Adaptação |
|-------------|----------------------------------|-------------------|--------------------|-------------------|
| Gestão do Ciclo de Vida Seguro | Requisitos de segurança aplicável durante todo o ciclo (design → desenvolvimento → distribuição → manutenção) | Cap. 02 (requisitos), Cap. 06 (desenvolvimento), Cap. 07 (CI/CD), Cap. 11 (pré-deploy) | Não distingue bem papéis fabricante/importador/distribuidor nem a determinação formal do support period | Mapear roles SbD-ToE → papéis CRA e registar policy de support period |
| Identificação e Gestão de Vulnerabilidades | Processos para receber, avaliar, priorizar e corrigir vulnerabilidades | Cap. 05 (SBOM/SCA), Cap. 10 (testes), Cap. 12 (monitorização), Addons exceções | Mecanismo formal de receção externa (coordinated disclosure portal) | Implementar canal público + política de divulgação coordenada de vulnerabilidades (Anexo I, Parte II, ponto 5) |
| SBOM / Transparência | Disponibilização de informação de componentes e dependências críticas | Cap. 05 (SBOM contínuo) | Formato exato de disponibilização externa (ex: CycloneDX export público) | Criar rotina de export SBOM sanitizada para stakeholders |
| Correções e Patches Rápidos | Aplicar correções de segurança sem demora injustificada | Cap. 05 (gestão CVE), Cap. 07 (automação CI/CD), Cap. 12 (deteção de exploração) | O CRA não fixa prazos numéricos de correção (exige correção «sem demora») | Definir SLA interno de patch (ex.: Crítico ≤15d, Alto ≤30d, Médio ≤90d) como operacionalização do «sem demora» |
| Reporte de vulnerabilidades ativamente exploradas | Notificar a CSIRT designada como coordenadora e a ENISA, através da plataforma única, das vulnerabilidades ativamente exploradas e dos incidentes graves: alerta precoce ≤24 h, notificação ≤72 h e relatório final (art. 14.º; aplicável desde 11.9.2026) | Cap. 12 (deteção, métricas exploração), Cap. 14 (governança) | Não separa suficientemente reporting obrigatório, comunicação a utilizadores e plataforma/regime oficial | Adicionar runbook técnico + interface formal de notificação e comunicação |
| Medidas para Prevenção de Vulnerabilidades | Controlo de qualidade e testes de segurança antes de release | Cap. 10 (SAST/DAST/fuzzing), Cap. 11 (gate de release) | Critérios formais de rejeição/liberação por criticidade | Adicionar matriz: nível criticidade → bloqueio automático release |
| Documentação de Segurança | Instruções e info de segurança para utilizadores/admins | Cap. 04 (arquitetura), Cap. 11 (deploy seguro) | Manual não gera sozinho a totalidade da surface `Annex II` (support period, contact point, end-of-support wording) | Criar artifact "Guia de Segurança do Produto" + tabela de support period e ponto de contacto |
| Monitorização Pós-Comercialização | Observação contínua de exploração e falhas | Cap. 12 (monitorização, alertas) | Integração com canal de feedback utilizador | Criar backlog específico "Feedback Segurança" + triagem semanal |
| Gestão de Exceções | Justificação de desvios temporários | Cap. 02 addon 08, Cap. 05 addon 09, Cap. 14 governance | Não mapeia limites CRA de aceitabilidade | Introduzir lista de vulnerabilidades "não-exceptuáveis" (ex: RCE crítico) |
| Segurança na Cadeia | Componentes de terceiros seguros, verificação de integridade | Cap. 05 (SCA), Cap. 07 (pipeline), Cap. 09 (runtime containers) | Processo de verificação de firmware/hardware e boundary de operador económico ainda pouco explícitos | Adicionar checklist supply chain físico (hash, secure boot se aplicável) e registo por papel |
| Conformidade e CE Mark | Declaração e marcação de conformidade | (Não coberto) | Avaliação técnica/legal formal | Estabelecer processo paralelo GRC + jurídico |

## PARTE II: Cobertura Detalhada {#parte-ii-cobertura-detalhada}

### 1. Ciclo de Vida Seguro {#1-ciclo-de-vida-seguro}
O SbD-ToE define gates de segurança desde a classificação até ao deploy. Isto suporta a obrigação CRA de garantir segurança "by design" e durante a manutenção.

O que ainda fica fora desta base técnica é a formalização explícita de:

- papel do operador económico
- support period
- e comunicação do fim de suporte ao utilizador

**Ação:** Consolidar num documento único: "Matriz de Controle CRA" listando controlos por fase (design, build, test, release, manutenção).

### 2. Vulnerability Handling & Coordinated Disclosure {#2-vulnerability-handling--coordinated-disclosure}
SbD-ToE já prevê triagem interna (SCA, scans, testes). CRA exige também canal externo para investigadores ou utilizadores reportarem falhas.

**Ação:** Criar página pública com política de disclosure (Âmbito, chave PGP, tempo de resposta, não iniciar ação legal de boa fé).

### 3. SBOM e Transparência {#3-sbom-e-transparência}
SBOM contínuo (Cap. 05) é base para fornecer visibilidade. CRA poderá exigir formato padronizado (CycloneDX/SPDX).

**Ação:** Gerar export sanitized (sem caminhos internos sensíveis) e manter versão por release maior.

### 4. Patching Rápido {#4-patching-rápido}
Definir SLA CRA diferenciado por severidade e criticidade do produto. Integrar no pipeline: se CVE crítico → tarefa automática + alerta CISO.

**Ação:** Automação: Workflow CI que abre issue + etiqueta "CRA-Patch".

### 5. Reporte de Vulnerabilidade Explorada {#5-reporte-de-vulnerabilidade-explorada}
Quando exploração confirmada (telemetria, IOC, prova), gerar relatório mínimo: ID vulnerabilidade, componente, versão afetada, impacto, mitigação temporária, prazo patch.

Isto deve ser lido como base técnica para cumprir a obrigação de reporte, não como substituto da surface regulatória completa de `Articles 14-16`, que inclui notificação formal, coordenação institucional e comunicação a utilizadores quando aplicável.

**Ação:** Script de extração (ex: export do SIEM + SBOM) → JSON pronto.

### 6. Qualidade e Testes de Segurança {#6-qualidade-e-testes-de-segurança}
SbD-ToE cobre variedade de testes. Alinhar com a exigência do CRA de disponibilizar o produto no mercado sem vulnerabilidades exploráveis conhecidas (Anexo I, Parte I, 2(a), com base na avaliação dos riscos).

**Ação:** Gate "no-critical-known" antes de release; exceções só com aprovação board (criticidade máxima).

### 7. Documentação de Segurança do Produto {#7-documentação-de-segurança-do-produto}
Gerar guia para administradores/utilizadores: configurações seguras, atualização, contacto de segurança, políticas de logging.

Para leitura `CRA`, este guia também deve deixar explícito:

- ponto de contacto de segurança
- tipo e duração do support period
- data de fim de suporte comunicada ao utilizador

**Ação:** Template derivado de Cap. 04 (arquitetura) + Cap. 11 (deploy seguro).

### 8. Monitorização Pós-Comercialização {#8-monitorização-pós-comercialização}
Cap. 12 já define monitorização; adicionar painéis específicos: "Vulnerabilidades conhecidas vs. status patch".

**Ação:** Dashboard com: total vulns abertas, tempo médio patch, percentagem SLA atendido.

### 9. Exceções {#9-exceções}
Política de exceções adaptada: vulnerabilidades RCE críticas nunca podem ser exceção; outras só com compensação robusta e TTL curto.

**Ação:** Adicionar tabela "Exceções Inaceitáveis CRA" ao policy central.

### 10. Cadeia de Fornecimento {#10-cadeia-de-fornecimento}
Expandir além de software: firmware, módulos criptográficos, dispositivos integrados.

**Ação:** Checklist físico: origem componente, hash firmware, canal de atualização seguro.

### 11. Conformidade e Marcação CE {#11-conformidade-e-marcação-ce}
Fora do âmbito técnico do SbD-ToE. Requer processo documental legal.

**Ação:** Criar swimlane separado GRC/Jurídico; manter referência dos controlos técnicos como evidência de segurança.

## Lacunas Intencionais {#lacunas-intencionais}

| Área | Motivo da Lacuna | Risco se Ignorado | Mitigação Proposta |
|------|------------------|-------------------|--------------------|
| Declaração UE Conformidade | Requer abordagem jurídica | Falha de mercado / penalizações | Integrar equipa legal cedo |
| Organismo Notificado | Processo regulado fora do manual | Atraso certificação | Definir critério de quando envolver |
| Formato Oficial SBOM Externo | Evolução de padrões | Incompatibilidade com requisitos comprador | Implementar export plugin CycloneDX |
| Canal Disclosure Externo | Universalidade do manual | Perda de reporte responsável | Publicar política em site /SECURITY.md |
| Firmware/Hardware Secure Boot | Foco software aplicacional | Vetor físico ignorado | Adicionar checklist supply chain físico |

## Métrica Simples CRA (Autoavaliação) {#métrica-simples-cra-autoavaliação}

Responda SIM aos seguintes pontos:
1. Existe política de segurança do produto cobrindo design→manutenção? ✓
2. Há SBOM completo gerado por release? ✓
3. Existe canal público de vulnerability disclosure? ✓
4. SLA de patch documentado e monitorizado? ✓
5. Gate que bloqueia release com CVE crítico conhecido? ✓
6. Dashboard de vulnerabilidades pós-comercialização ativo? ✓
7. Export SBOM externa sanitizada disponível para clientes/reguladores? ✓
8. Política de exceções define vulnerabilidades inaceitáveis? ✓
9. Guia de Segurança do Produto publicado? ✓
10. Processo de reporte de exploração ativa documentado? ✓

≥8/10 → Boa base técnica CRA. `<`6 → Priorizar SBOM, patching, disclosure, gating crítico.

## Ações Prioritárias (Roadmap Inicial) {#ações-prioritárias-roadmap-inicial}

1. Formalizar política ciclo de vida seguro (integrar CRA requisitos e support period) 
2. Implementar canal disclosure externo (security.txt + página) 
3. Ajustar pipeline com gate "no critical known" 
4. Definir SLA patch CRA e métricas de acompanhamento 
5. Gerar SBOM e export CycloneDX por release 
6. Criar guia de segurança do produto + contact point + fim de suporte 
7. Criar runbook de reporte exploração ativa 
8. Adicionar dashboard pós-comercialização 
9. Checklist supply chain físico (se aplicável) 
10. Swimlane CE Conformidade (jurídico + GRC)

## Referências {#referências}

- **Cyber Resilience Act**: Regulamento (UE) 2024/2847 (CELEX: [32024R2847](https://eur-lex.europa.eu/legal-content/PT/TXT/?uri=CELEX:32024R2847))
- SbD-ToE Manual Capítulos 01–14 
- ENISA Guidance on Product Security & Vulnerability Disclosure 
- ISO/IEC 29147 (Vulnerability Disclosure), ISO/IEC 30111 (Vulnerability Handling)
- CycloneDX / SPDX especificações

**Versão:** 1.0  
**Data:** Novembro 2025  
**Próxima revisão:** Maio 2026
