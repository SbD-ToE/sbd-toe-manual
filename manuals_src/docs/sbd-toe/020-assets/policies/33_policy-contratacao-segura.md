---
id: policy-contratacao-segura
title: Política de Contratação Segura
description: Política organizacional que define os requisitos de segurança aplicáveis ao ciclo de vida contratual com fornecedores e contractors, incluindo due diligence pré-contratual, cláusulas contratuais mínimas por nível de risco, onboarding técnico, monitorização de conformidade, reavaliação periódica e offboarding seguro, proporcional ao nível de criticidade (L1, L2, L3).
tags: [policy, contratação, fornecedores, contractors, due diligence, cláusulas contratuais, onboarding, offboarding, conformidade, cap14, L1, L2, L3, governance, DORA, NIS2]
grupo: governacao
sidebar_position: 33
---

# Política de Contratação Segura

## 1. Objetivo

Esta política define os **requisitos de segurança aplicáveis ao ciclo de vida contratual com fornecedores, parceiros e contractors** que acedem a sistemas, dados ou infraestrutura da organização.

A externalização de competências técnicas e o recurso a serviços de terceiros são práticas operacionais correntes. No entanto, cada fornecedor ou contractor com acesso técnico representa um vector de risco adicional: pode introduzir vulnerabilidades, ter acesso a dados sensíveis sem enquadramento adequado, ou manter acesso residual após o términus do contrato. A gestão deste risco não pode ser relegada para uma cláusula genérica de confidencialidade - exige um processo estruturado que começa antes da assinatura do contrato e termina apenas com o offboarding verificado.

O objetivo desta política é garantir que:

- A avaliação de segurança de fornecedores é realizada antes de qualquer contrato que envolva acesso a sistemas ou dados
- Os contratos incluem cláusulas de segurança proporcionais ao nível de risco da relação
- O onboarding técnico de contractors é condicionado à conclusão de formação mínima obrigatória
- A conformidade dos fornecedores activos é monitorizada e reavaliada periodicamente
- O offboarding é executado de forma imediata, completa e auditável

---

## 2. Âmbito e obrigatoriedade

Esta política aplica-se a todos os fornecedores, parceiros e contractors que:

- Acedem a sistemas, plataformas ou infraestrutura da organização
- Desenvolvem, mantêm ou operam componentes de software em nome da organização
- Processam, armazenam ou transmitem dados da organização ou dos seus utilizadores
- Têm acesso a ambientes regulados (produção, dados de saúde, dados financeiros, PII)

| Nível | Obrigatoriedade |
|---|---|
| L1 | Recomendado; cláusulas básicas de confidencialidade e boas práticas; contacto de segurança definido |
| L2 | Obrigatório; due diligence pré-contratual; cláusulas SbD-ToE; onboarding documentado; reavaliação anual |
| L3 | Obrigatório; due diligence formal; auditoria técnica; cláusulas completas; SBOM e relatórios de testes obrigatórios; reavaliação semestral; direito formal de auditoria |

---

## 3. Due diligence pré-contratual

Antes de estabelecer qualquer relação contratual com acesso técnico, deve ser realizada uma avaliação de segurança proporcional ao nível de risco:

### 3.1 Critérios de avaliação

| Critério | L2 | L3 |
|---|---|---|
| Política de segurança da informação documentada | Verificação | Obrigatório + evidência |
| Processo de gestão de vulnerabilidades | Verificação | Obrigatório + SLA definido |
| Incidentes de segurança nos últimos 12 meses | Declaração | Declaração + análise |
| Certificações ou conformidade com normas (ISO 27001, SOC 2, etc.) | Recomendado | Obrigatório para acesso a dados regulados |
| Capacidade de entrega de SBOM | Não aplicável | Obrigatório para software desenvolvido |
| Relatórios de testes de segurança recentes | Recomendado | Obrigatório |
| Processo de offboarding documentado | Recomendado | Obrigatório |

### 3.2 Resultado da due diligence

O resultado da due diligence deve ser documentado e aprovado antes da assinatura do contrato:

- **Aprovado sem condições**: relação contratual estabelecida
- **Aprovado com condições**: contrato estabelecido com plano de remediação de lacunas identificadas e prazo definido
- **Rejeitado**: fornecedor não elegível para relação com acesso técnico até resolução das não-conformidades

---

## 4. Cláusulas contratuais mínimas de segurança

Todos os contratos que impliquem acesso técnico devem incluir cláusulas de segurança proporcionais ao nível de risco:

### 4.1 Cláusulas universais (todos os níveis)

| Cláusula | Descrição |
|---|---|
| Confidencialidade | Obrigação de confidencialidade de dados, credenciais e arquitetura |
| Notificação de incidentes | Prazo de notificação de incidentes de segurança à organização (recomendado: ≤ 24 horas de conhecimento) |
| Uso aceitável | Proibição de acesso além do estritamente necessário para o âmbito contratual |
| Subcontratação | Proibição ou condicionamento de subcontratação com acesso a dados ou sistemas |
| Rescisão por incumprimento | Cláusula de rescisão imediata em caso de violação de segurança grave |

### 4.2 Cláusulas adicionais por nível de risco

| Nível | Cláusulas adicionais |
|---|---|
| **L1** | Compromisso genérico com boas práticas; política de notificação de incidentes |
| **L2** | Aplicação do Catálogo SbD-ToE; fornecimento de evidência técnica sob solicitação; SLA para resolução de vulnerabilidades críticas |
| **L3** | Testes de segurança periódicos obrigatórios (com relatório entregue); SBOM entregue por release; SLA para correções críticas (≤ 72 horas); direito formal de auditoria técnica pela organização; requisitos de formação de segurança para pessoal com acesso |

### 4.3 Modelo contratual de referência

A organização deve manter um modelo contratual padrão com cláusulas de segurança validadas juridicamente, actualizado anualmente ou após alterações regulatórias relevantes. O modelo deve ser disponibilizado a Procurement e Jurídico como referência de negociação - as cláusulas de segurança são requisitos mínimos, não pontos de negociação em contratos L2/L3.

---

## 5. Onboarding técnico de contractors

Contractors que acedam a sistemas ou repositórios da organização devem completar um processo de onboarding técnico antes de receberem permissões:

### 5.1 Processo de onboarding

| Etapa | Descrição | Obrigatoriedade |
|---|---|---|
| Trilho formativo mínimo | Formação sobre políticas de segurança, gestão de credenciais, acesso a dados, reporte de incidentes | L2/L3 obrigatório; L1 recomendado |
| Validação de compreensão | Quiz ou teste com nota mínima de 80% | L2/L3 obrigatório |
| Assinatura de termos específicos | Termo de responsabilidade e confidencialidade individual | Todos os níveis |
| Ambiente sandbox | Acesso inicial a ambiente de desenvolvimento isolado antes de produção | L3 obrigatório |
| Atribuição de permissões mínimas | Acesso com princípio do menor privilégio; sem acesso a produção sem aprovação explícita | L2/L3 obrigatório |

### 5.2 Bloqueio de acesso

O acesso a sistemas da organização é **bloqueado até conclusão de todas as etapas de onboarding obrigatórias**. A conclusão deve ser registada (LMS, sistema de RH ou ferramenta equivalente) e associada à identidade do contractor.

---

## 6. Monitorização de conformidade de fornecedores activos

A relação contratual não termina com a assinatura - os fornecedores activos com acesso técnico devem ser monitorizados continuamente:

### 6.1 Indicadores de conformidade a monitorizar

| Indicador | Descrição |
|---|---|
| Cumprimento de SLA de correção de vulnerabilidades | Tempo entre notificação e remediação confirmada |
| Entrega de artefactos contratuais | SBOM, relatórios de testes, relatórios de auditoria (onde aplicável) |
| Notificação de incidentes dentro do prazo | Conformidade com o prazo contratual de notificação |
| Ausência de incidentes de segurança atribuídos ao fornecedor | Registo de ocorrências |

### 6.2 Reavaliação periódica

| Nível | Cadência | Âmbito |
|---|---|---|
| L1 | Anual | Revisão de cláusulas e conformidade básica |
| L2 | Anual | Due diligence actualizada; verificação de SLAs; análise de incidentes |
| L3 | Semestral | Due diligence técnica completa; revisão de artefactos; verificação de certificações; análise de risco residual |

O resultado da reavaliação deve originar uma decisão documentada:
- **Continuidade sem alterações**: conformidade mantida
- **Continuidade com plano de melhoria**: lacunas identificadas com prazo de resolução
- **Penalização contratual**: incumprimento de SLA com impacto financeiro (se previsto)
- **Substituição**: não-conformidade grave ou risco inaceitável

---

## 7. Offboarding seguro

O offboarding de um contractor ou a rescisão de um contrato com fornecedor devem ser executados de forma imediata e verificável:

### 7.1 Checklist de offboarding

- [ ] Revogação de todos os acessos (sistemas, repositórios, ferramentas, VPN, credenciais de serviço)
- [ ] Remoção de chaves SSH, tokens, API keys e certificados emitidos em nome do contractor/fornecedor
- [ ] Recuperação de equipamentos ou activos da organização fornecidos ao contractor
- [ ] Confirmação de eliminação ou devolução de dados da organização em posse do fornecedor (quando aplicável)
- [ ] Desactivação de contas nos sistemas de identidade (IdP, Active Directory, etc.)
- [ ] Registo documentado da conclusão do offboarding (timestamp, responsável, estado de cada item)

### 7.2 Prazos de offboarding

| Tipo de saída | Prazo máximo para revogação de acessos |
|---|---|
| Saída planeada (fim de contrato) | No próprio dia de terminus |
| Saída não planeada (rescisão imediata) | ≤ 2 horas após decisão |
| Rescisão por causa de segurança | Imediato - revogação prioritária antes de qualquer outro procedimento |

:::warning
A manutenção de acessos activos após o términus do contrato é uma das causas mais comuns de acessos residuais não autorizados. O processo de offboarding deve ser automatizado ao máximo para evitar dependência de acção manual sob pressão ou com lacunas de informação.
:::

---

## 8. Registo e rastreabilidade

Para cada fornecedor e contractor, a organização deve manter um registo actualizado que inclua:

| Artefacto | Conteúdo | Retenção |
|---|---|---|
| Resultado de due diligence | Avaliação pré-contratual, decisão, condições | Duração do contrato + 3 anos |
| Contrato com cláusulas de segurança | Versão assinada com cláusulas aplicáveis | Duração do contrato + 5 anos |
| Registo de onboarding | Trilho formativo, quiz, permissões iniciais | Duração do contrato + 1 ano |
| Registos de reavaliação | Resultados de cada ciclo de avaliação periódica | Duração do contrato + 3 anos |
| Registo de offboarding | Checklist concluído, timestamp, responsável | 5 anos |

---

## 9. Responsabilidades

| Role | Responsabilidade |
|---|---|
| Procurement / Jurídico | Garantir que contratos incluem cláusulas de segurança mínimas; conduzir negociação com modelo de referência |
| GRC / Compliance | Manter modelo contratual actualizado; conduzir due diligence; auditar conformidade; reavaliações periódicas |
| AppSec Engineer | Definir requisitos técnicos de segurança a incluir nos contratos; avaliar artefactos técnicos (SBOM, relatórios); apoiar due diligence técnica |
| Security Champion | Executar onboarding técnico de contractors; verificar conclusão de formação antes de atribuição de acessos |
| DevOps / SRE | Executar revogação técnica de acessos no offboarding; gerir identidades e permissões |
| RH | Coordenar processo de onboarding/offboarding com Security Champion; registar conclusão nos sistemas de RH |

---

## 10. Revisão e auditoria desta política

Esta política deve ser **revista anualmente** ou após qualquer um dos seguintes eventos:

- Incidente de segurança envolvendo um fornecedor ou contractor
- Alteração regulatória que modifique obrigações de due diligence ou notificação (ex: DORA, NIS2, RGPD)
- Resultado de auditoria que identifique lacunas no processo de contratação ou offboarding

---

## 11. Referências normativas e técnicas

| Referência | Relevância |
|---|---|
| SbD-ToE Cap. 14 - Governança & Contratação | US-02: cláusulas contratuais; US-14: reavaliação de fornecedores; US-15: onboarding de contractors; US-17: offboarding |
| Política de Rastreabilidade Organizacional (`34_policy-rastreabilidade-organizacional.md`) | Registo e evidência de conformidade |
| Política de Gestão de Segredos (`18_policy-gestao-segredos.md`) | Credenciais de contractors e revogação |
| ISO/IEC 27001 - A.15 | Supplier relationships |
| ISO/IEC 27036 | Information security for supplier relationships |
| NIST SP 800-161 | Cybersecurity Supply Chain Risk Management |
| RGPD - Art. 28 | Subprocessadores de dados pessoais |
| DORA - Art. 28-30 | ICT third-party risk management |
| NIS2 - Art. 21 | Supply chain security measures |
