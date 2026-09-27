---
id: policy-irp
title: Política de Integração com IRP (Incident Response Plan)
description: Política organizacional que define os requisitos de integração entre a monitorização de segurança e o processo de resposta a incidentes (IRP), incluindo critérios de activação, playbooks obrigatórios, fases de resposta, notificação regulatória, post-mortem e testes periódicos, proporcional ao nível de criticidade (L1, L2, L3).
tags: [policy, IRP, incident response, playbook, SOAR, contenção, notificação, post-mortem, cap12, L1, L2, L3, governance, DORA]
grupo: operacoes
sidebar_position: 32
---

# Política de Integração com IRP

## 1. Objetivo {#1-objetivo}

Esta política define os requisitos para a **integração entre os sistemas de monitorização de segurança e o processo formal de resposta a incidentes (IRP)** da organização.

A detecção de um incidente de segurança só tem valor operacional quando conduz a uma resposta estruturada. Alertas sem playbooks associados tornam-se decisões ad-hoc sob pressão - precisamente quando as decisões mais importantes precisam de ser as mais rápidas e correctas. O IRP transforma a detecção em resposta: define quem faz o quê, em que ordem, com que autoridade e com que evidência.

O objetivo desta política é garantir que:

- Cada categoria de alerta de segurança tem um playbook de resposta associado
- A activação do IRP é criteriosa, proporcional e auditável
- As fases de contenção, erradicação e recuperação são executadas de forma ordenada
- A notificação regulatória é feita dentro dos prazos aplicáveis
- O post-mortem é realizado após cada incidente, a partir de L2; sob DORA ou NIS2, também em L1 para os incidentes que atingem o limiar de notificação
- Os playbooks e o próprio IRP são testados periodicamente

---

## 2. Âmbito e obrigatoriedade {#2-âmbito-e-obrigatoriedade}

| Nível | Obrigatoriedade |
|---|---|
| L1 | Recomendado; processo de resposta documentado; contactos de escalonamento definidos; incidentes registados |
| L2 | Obrigatório; playbooks definidos; integração com sistema de gestão de incidentes; post-mortem |
| L3 | Obrigatório; playbooks automatizados (SOAR); testes semestrais; war room |

A notificação regulatória (secção 6) é obrigatória sempre que aplicável, em qualquer nível: depende do incidente e da entidade, não do nível L.

---

## 3. Critérios de activação do IRP {#3-critérios-de-activação-do-irp}

O IRP é activado formalmente quando um alerta ou evento de segurança é confirmado como incidente. Os critérios de activação incluem:

| Categoria | Exemplos | Activação |
|---|---|---|
| Comprometimento de credenciais | Credencial de produção exposta, acesso não autorizado confirmado | Imediata |
| Exfiltração de dados | Download anómalo de dados confirmado, PII exposta | Imediata |
| Ransomware / malware | Ficheiros encriptados, binário suspeito em execução | Imediata |
| Disponibilidade | Indisponibilidade prolongada com suspeita de causa de segurança | Após 15 minutos de impacto |
| Anomalia de segurança de alta severidade | Padrão comportamental suspeito confirmado pelo SIEM | Após triagem positiva |
| Vulnerabilidade crítica em produção | CVE Critical com exploit activo em sistema exposto | Activação preventiva |

Um alerta não confirmado não activa o IRP formalmente - activa a fase de triagem. A activação formal ocorre após confirmação.

---

## 4. Fases de resposta a incidentes {#4-fases-de-resposta-a-incidentes}

### 4.1 Triagem (T0 - ≤ 15 minutos de detecção) {#41-triagem-t0----15-minutos-de-detecção}

- [ ] Alerta classificado: verdadeiro positivo ou falso positivo
- [ ] Severidade atribuída (P1–P4; P1 é o topo da escala)
- [ ] Responsável pelo incidente designado (Incident Commander)
- [ ] Avaliação de notificabilidade: se houver indício de violação de dados pessoais, de incidente significativo (NIS2), de incidente de caráter severo relacionado com as TIC (DORA), de vulnerabilidade ativamente explorada ou incidente grave (CRA) ou de incidente grave (AI Act), o incidente segue o **trilho regulatório**, em qualquer severidade e em qualquer nível, e sobe no mínimo a P2: GRC/Compliance e EPD/DPO informados ≤ 1 h após a confirmação; o momento do conhecimento registado no ticket; decisão de notificabilidade ≤ 4 h (escolha do Manual; ver secção 6), registada com a fundamentação, também quando é negativa
- [ ] Canal de comunicação do incidente aberto (war room se P1)

### 4.2 Contenção (T1 - início imediato após confirmação) {#42-contenção-t1---início-imediato-após-confirmação}

- [ ] Acções de contenção imediata executadas (isolamento de sistema, revogação de credencial, bloqueio de IP)
- [ ] Contenção documentada com timestamp e identidade do executor
- [ ] Sem destruição de evidências durante contenção (preserve first, contain second quando possível)
- [ ] Comunicação interna ao Tech Lead, AppSec Engineer e GRC

### 4.3 Investigação {#43-investigação}

- [ ] Recolha de logs, traces e evidências relevantes
- [ ] Timeline do incidente reconstruída
- [ ] Causa raiz identificada ou hipótese de trabalho documentada
- [ ] Âmbito do impacto determinado (sistemas, dados, utilizadores afectados)
- [ ] Dados de impacto registados: utilizadores ou clientes afectados, duração e período de indisponibilidade, distribuição geográfica, dados afectados (confidencialidade, integridade, disponibilidade), perdas financeiras estimadas, serviços ou funções críticas afectados; são os dados que os critérios de notificabilidade da secção 6.1 pedem

### 4.4 Erradicação {#44-erradicação}

- [ ] Causa raiz eliminada (patch, revogação de acesso, remoção de malware)
- [ ] Sistemas afectados reconstruídos de zero quando há suspeita de persistência
- [ ] Verificação de que o vector de entrada foi fechado

### 4.5 Recuperação {#45-recuperação}

- [ ] Sistemas restaurados com versões limpas e verificadas
- [ ] Monitorização reforçada no período pós-recuperação
- [ ] Confirmação de estado normal de operação

### 4.6 Post-mortem {#46-post-mortem}

- [ ] Realizado no prazo máximo de 5 dias úteis após resolução
- [ ] Participação de todas as funções envolvidas
- [ ] Análise de causa raiz (5 Whys ou equivalente)
- [ ] Plano de acções correctivas com owner e prazo
- [ ] Documento arquivado e lições aprendidas partilhadas internamente
- [ ] Revisão dos artefactos afectados, com disposição registada por artefacto (revisto ou sem alteração, com a razão): análise de risco e classificação, threat model, modelo de acessos, configurações, arquitectura, contratos de fornecedores, KPIs e o próprio IRP

### 4.7 Análise de recorrência {#47-análise-de-recorrência}

Os incidentes analisam-se também em conjunto, para encontrar padrões e recorrências (a mesma causa primária aparente). A análise é trimestral em L2 e mensal em L3, e recomendada em L1 (escolha do Manual). Cada recorrência abre um problema, com causa raiz e acções correctivas com owner e prazo. As regras de agregação para efeitos de notificação são dos regimes (DORA, NIS2) e constam do overlay regulatório.

---

## 5. Playbooks de resposta {#5-playbooks-de-resposta}

Cada categoria de incidente deve ter um playbook que detalha as acções específicas por fase:

| Categoria de incidente | Playbook obrigatório |
|---|---|
| Credencial comprometida | Revogação, rotação, auditoria de acessos no período de exposição |
| Exfiltração de dados / PII | Contenção, análise de âmbito, notificação regulatória |
| Ransomware | Isolamento, forensics, recuperação de backup |
| Vulnerabilidade crítica em produção | Patching de emergência, contenção temporária, comunicação |
| Deploy de código malicioso | Rollback, análise da pipeline, revogação de credenciais de CI |
| Comprometimento de dependência (supply chain) | Identificação do âmbito, remoção, rebuild |

Em L3, os playbooks devem estar integrados com SOAR para automação das acções de contenção imediata (ex: bloqueio de IP, revogação de token, isolamento de pod).

---

## 6. Notificação regulatória {#6-notificação-regulatória}

Alguns incidentes requerem notificação a autoridades regulatórias dentro de prazos definidos:

| Regulação | Tipo de incidente | Prazo |
|---|---|---|
| RGPD - Art. 33, n.º 1 | Violação de dados pessoais (salvo se não for suscetível de resultar num risco para os direitos e liberdades das pessoas singulares) | À autoridade de controlo (em Portugal, a CNPD): sem demora injustificada e, sempre que possível, até 72 horas após ter tido conhecimento; depois das 72 h, acompanhada dos motivos do atraso; pode ser faseada (n.º 4) |
| RGPD - Art. 33, n.º 2 | Violação conhecida pelo subcontratante | Ao responsável pelo tratamento, sem demora injustificada (o contrato pode fixar um prazo em horas) |
| RGPD - Art. 34 | Violação suscetível de implicar um elevado risco para os direitos e liberdades das pessoas singulares | Aos titulares dos dados, sem demora injustificada (exceções no n.º 3) |
| DORA - Art. 19 + Reg. Delegado (UE) 2025/301, art. 5.º | Incidente de caráter severo relacionado com as TIC (entidade financeira) | Notificação inicial ≤ 4 h após a classificação como severo e ≤ 24 h após o conhecimento; relatório intercalar ≤ 72 h após a notificação inicial; relatório final ≤ 1 mês após o último relatório intercalar |
| DORA - Art. 19, n.º 3 | Incidente de caráter severo com impacto nos interesses financeiros dos clientes | Aos clientes, sem demora indevida e logo que a entidade tenha tomado conhecimento |
| NIS2 - Art. 23, n.º 4 (conforme a transposição nacional) | Incidente significativo em entidade essencial/importante | À CSIRT ou, se aplicável, à autoridade competente: alerta rápido ≤ 24 h; notificação de incidente ≤ 72 h (prestadores de serviços de confiança: ≤ 24 h); relatório intercalar a pedido; relatório final ≤ 1 mês após a notificação de incidente (se o incidente estiver em curso: relatório intercalar nessa altura e final ≤ 1 mês após a resolução) |
| CRA - Art. 14 (aplicável desde 11.9.2026) | Vulnerabilidade ativamente explorada ou incidente grave num produto com elementos digitais colocado no mercado pela organização | À CSIRT designada como coordenadora e à ENISA, pela plataforma única: alerta precoce ≤ 24 h; notificação ≤ 72 h; relatório final ≤ 14 dias após a medida corretiva (vulnerabilidade) ou ≤ 1 mês após a notificação (incidente grave) |
| CRA - Art. 14, n.º 8 | Vulnerabilidade ativamente explorada ou incidente grave | Aos utilizadores afetados (e, se for caso disso, a todos), com as medidas de atenuação e corretivas que possam tomar |
| AI Act - Art. 73 | Incidente grave com sistema de IA de risco elevado | À autoridade de fiscalização do mercado do Estado-Membro onde ocorreu: imediatamente após determinar a relação causal (ou a sua probabilidade razoável) e, o mais tardar, 15 dias após o conhecimento pelo prestador ou pelo responsável pela implantação; 10 dias em caso de morte; 2 dias em caso de infração generalizada ou de incidente grave do art. 3.º, ponto 49, alínea b); admite relatório inicial incompleto (n.º 5) |
| AI Act - Art. 75, n.º 1-A | Incidente grave com sistema de IA de risco elevado sujeito à competência do Serviço para a IA (sistema baseado num modelo de finalidade geral do mesmo prestador) | Ao Serviço para a IA, em vez da autoridade de fiscalização do mercado, com os prazos do art. 73 |
| AI Act - Art. 55, n.º 1, al. c) | Incidente grave com modelo de IA de finalidade geral com risco sistémico (prestador do modelo) | Ao Serviço para a IA e, se for caso disso, às autoridades nacionais competentes, sem demora injustificada, com as eventuais medidas corretivas |
| CSA - Art. 56, n.º 8 | Vulnerabilidade ou irregularidade detetada depois da certificação que possa afetar a conformidade de um produto com certificado europeu de cibersegurança | Ao organismo emissor do certificado (ou à autoridade que o emitiu) |

:::warning
A determinação de se um incidente é notificável deve ser feita pelo GRC/Compliance com o apoio do Encarregado de Proteção de Dados (EPD/DPO) quando aplicável. Os prazos contam-se a partir do conhecimento do incidente ou da violação - não da identificação da causa raiz -, salvo nas etapas que a lei ancora noutro momento: o relatório final NIS2 conta da notificação de incidente; o relatório final CRA de uma vulnerabilidade conta da disponibilização da medida corretiva ou de atenuação. No DORA, o prazo de 4 h conta da classificação do incidente como de caráter severo (com o limite de 24 h a contar do conhecimento) e o de 72 h conta da notificação inicial (Reg. Delegado (UE) 2025/301, art. 5.º).
:::

**Retenção dos registos de incidentes.** A timeline, o post-mortem e as notificações enviadas conservam-se por 1 ano em L1 e L2 e por 3 anos em L3 (escolha do Manual; ver a [Política 06 §10](/sbd-toe/assets/policies/policy-rastreabilidade#10-prazos-de-retenção-mínimos)). No DORA, o período é definido pela entidade (Reg. Delegado (UE) 2024/1774, art. 22.º, al. d)).

### 6.1 Critério e conteúdo mínimo por regime {#61-critério-e-conteúdo-mínimo-por-regime}

O registo do incidente (secção 4.3) recolhe os dados de impacto; o critério de notificabilidade e os limiares são os de cada regime, que o overlay regulatório detalha. O conteúdo mínimo é o que a lei pede; não substitui os formulários das autoridades.

| Regime | Critério | Conteúdo mínimo |
|---|---|---|
| RGPD - Art. 33 | Risco para os direitos e liberdades das pessoas singulares | Natureza da violação, com as categorias e o número aproximado de titulares e de registos; contacto do EPD; consequências prováveis; medidas adotadas ou propostas. Todas as violações ficam documentadas, notificadas ou não |
| DORA - Art. 19 | Incidente de caráter severo segundo o art. 18 e o Reg. Delegado (UE) 2024/1772, incluindo a agregação de incidentes recorrentes | Modelos do Reg. de Execução (UE) 2025/302 para a notificação inicial, o relatório intercalar e o relatório final |
| NIS2 - Art. 23 | Incidente significativo (art. 23, n.º 3); nas entidades pertinentes, os limiares dos arts. 3 e 4 do Reg. de Execução (UE) 2024/2690 | Alerta rápido: suspeita de ato ilícito ou malicioso e impacto transfronteiriço. Notificação: avaliação inicial, gravidade, impacto e indicadores de exposição. Relatório final: descrição pormenorizada, gravidade e impacto, tipo de ameaça ou causa primária, medidas de atenuação, impacto transfronteiriço |
| CRA - Art. 14 | Incidente grave (art. 14, n.º 5): afeta a disponibilidade, autenticidade, integridade ou confidencialidade de dados ou funções, ou introduz código mal-intencionado | Relatório final: descrição pormenorizada, gravidade e impacto, tipo de ameaça ou causa primária, medidas de atenuação aplicadas e em curso |
| AI Act - Art. 73 | Incidente grave (art. 3, ponto 49) | O previsto no art. 73 |

---

## 7. Comunicação durante o incidente {#7-comunicação-durante-o-incidente}

- [ ] Canal dedicado ao incidente (sem ruído de outros canais)
- [ ] Incident Commander responsável pela comunicação interna e externa
- [ ] Actualizações regulares ao management em incidentes P1 (ex: a cada 30 minutos)
- [ ] Comunicação a utilizadores afectados quando aplicável - honesta e sem comprometer a investigação
- [ ] Sem comunicação pública não autorizada por membros da equipa técnica

---

## 8. Testes periódicos do IRP {#8-testes-periódicos-do-irp}

| Nível | Cadência | Tipo de teste |
|---|---|---|
| L1 | Anual | Revisão tabletop (discussão de cenário) |
| L2 | Semestral | Tabletop + simulação de playbook |
| L3 | Semestral | War room com simulação activa; validação de escalonamento e notificação |

Os resultados dos testes devem ser documentados e as lacunas identificadas devem resultar em acções correctivas com prazo definido.

---

## 9. Responsabilidades {#9-responsabilidades}

| Role | Responsabilidade |
|---|---|
| AppSec Engineer | Manter playbooks; coordenar resposta técnica; garantir preservação de evidências |
| Incident Commander (on-call sénior) | Coordenar o incidente; gerir comunicação; tomar decisões de contenção |
| DevOps / SRE | Executar acções técnicas de contenção e recuperação |
| GRC / Compliance | Determinar obrigações de notificação; contactar autoridades regulatórias; gerir post-mortem |
| Management / CISO | Ser notificado em P1; autorizar comunicações externas; aprovar declarações públicas |

---

## 10. Revisão e auditoria desta política {#10-revisão-e-auditoria-desta-política}

Esta política deve ser **revista anualmente** ou após qualquer um dos seguintes eventos:

- Incidente real que revelou lacunas no IRP
- Alteração regulatória que modifique os prazos ou requisitos de notificação
- Resultado de teste que identifique falhas no processo de resposta

---

## 11. Referências normativas e técnicas {#11-referências-normativas-e-técnicas}

| Referência | Relevância |
|---|---|
| SbD-ToE Cap. 12 - Monitorização & Operações | US-04: integração com IRP; playbooks; automação |
| Política de Monitorização de Segurança (`30_policy-monitorizacao-seguranca.md`) | Detecção de incidentes |
| Política de Gestão de Alertas (`31_policy-gestao-alertas.md`) | Activação de IRP por alerta |
| NIST SP 800-61 rev.2 | Computer Security Incident Handling Guide |
| ISO/IEC 27035 | Information Security Incident Management |
| RGPD - Art. 33-34 | Notificação de violação de dados pessoais |
| DORA - Art. 17-20 | ICT incident management e reporting |
| NIS2 - Art. 23 | Incident notification obligations |
| MITRE ATT&CK | Táticas e técnicas para investigação de incidentes |
