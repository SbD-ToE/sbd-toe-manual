---
id: policy-aceitacao-risco
title: Política de Aceitação de Risco Residual
description: Política organizacional que define os critérios, o processo formal, as alçadas de aprovação e os requisitos de rastreabilidade para a aceitação de risco residual em aplicações classificadas L1 a L3, incluindo riscos provenientes de controlos não aplicados, findings não corrigidos e ameaças identificadas no threat modeling.
tags: [policy, risco residual, aceitação de risco, exceções, cap01, cap03, cap10, governance, L1, L2, L3]
grupo: risco
sidebar_position: 3
---

# Política de Aceitação de Risco Residual

## 1. Objetivo

Esta política define o processo formal para a **aceitação de risco residual** em aplicações desenvolvidas ou operadas pela organização.

Risco residual é o risco que permanece após a aplicação dos controlos de segurança definidos para o nível de criticidade da aplicação. A sua aceitação não é, por si só, uma falha - é uma decisão de gestão informada, desde que formalizada, aprovada com a alçada adequada, temporalmente delimitada e rastreável.

A ausência de um processo formal de aceitação de risco leva a que decisões de risco sejam tomadas implicitamente, sem visibilidade, sem responsabilidade atribuída e sem mecanismo de revisão.

---

## 2. Âmbito

Esta política aplica-se a todas as situações em que exista risco residual identificado e aceite, incluindo:

- Controlos obrigatórios para o nível de criticidade que não foram aplicados
- Findings de segurança (SAST, DAST, IAST, SCA, fuzzing, pentest) que não foram corrigidos
- Ameaças identificadas no threat modeling para as quais não existe mitigação implementada
- Exceções arquiteturais com impacto na postura de segurança
- Dependências com vulnerabilidades conhecidas sem correção disponível ou viável

---

## 3. Tipos de risco residual

| Tipo | Origem | Exemplos |
|---|---|---|
| **Controlo não aplicado** | Matriz de controlos SbD-ToE | Requisito obrigatório para o nível não implementado |
| **Finding não corrigido** | SAST, DAST, IAST, SCA, fuzzing, pentest | Vulnerabilidade identificada sem remediação dentro do SLA |
| **Ameaça aceite** | Threat modeling | Ameaça STRIDE documentada sem mitigação técnica |
| **Exceção arquitetural** | Revisão de arquitetura | Padrão inseguro mantido por constrangimento técnico ou de negócio |
| **Dependência vulnerável** | SCA / SBOM | CVE ativo sem fix disponível ou com impacto avaliado como aceitável |

---

## 4. Critérios para aceitação de risco

Um risco residual só pode ser aceite formalmente se cumprir **todos** os seguintes critérios:

- [ ] O risco é **compatível com o nível de criticidade** da aplicação (L1, L2 ou L3)
- [ ] O risco residual está **dentro dos limiares definidos** para aceitação no nível em causa
- [ ] Existem **evidências suficientes dos controlos aplicados** que reduzem o risco ao nível residual
- [ ] Foi identificada e documentada uma **mitigação compensatória**, quando tecnicamente viável
- [ ] A decisão de aceitação é **temporalmente delimitada** - com data de expiração e reavaliação
- [ ] A decisão é **formalmente aprovada** pela alçada adequada ao nível de risco

:::warning
A aceitação de risco não substitui a correção. É uma decisão temporária e documentada, não uma solução permanente. Todo o risco aceite deve ter data de expiração e mecanismo de reavaliação.
:::

---

## 5. Limiares de aceitação por nível

| Nível | Severidade máxima aceitável sem escalada | Prazo máximo de aceitação |
|---|---|---|
| L1 | High (com justificação e compensação) | 90 dias |
| L2 | Medium sem escalada; High requer aprovação AppSec | 60 dias |
| L3 | Medium requer AppSec; High requer CISO; Critical não é aceitável | 30 dias |

:::note
Findings de severidade **Critical** não podem ser aceites como risco residual em nenhum nível sem um plano de remediação ativo com prazo definido. A aceitação de um finding Critical é uma exceção de último recurso, sujeita a aprovação de CISO e registo formal com prazo máximo de 7 dias.
:::

---

## 6. Processo de aceitação

### 6.1 Passos obrigatórios

1. **Identificar o risco residual** - origem, tipo, severidade e contexto técnico
2. **Avaliar o impacto** - consequência real no contexto da aplicação e do negócio
3. **Definir mitigação compensatória** - controlo alternativo ativo durante o período de aceitação
4. **Documentar a justificação técnica** - por que razão o controlo não foi aplicado ou o finding não foi corrigido
5. **Definir prazo de validade** - data de expiração da aceitação e data de reavaliação
6. **Obter aprovação formal** - pela alçada adequada ao nível de risco (ver secção 7)
7. **Registar** - no repositório de exceções da aplicação ou plataforma GRC

### 6.2 Checklist por registo de risco aceite

- [ ] Identificador único do registo
- [ ] Tipo de risco (controlo não aplicado / finding / ameaça / exceção arquitetural / dependência)
- [ ] Descrição técnica do risco e da sua origem
- [ ] Severidade avaliada (Critical / High / Medium / Low)
- [ ] Evidência dos controlos existentes que reduzem o risco
- [ ] Mitigação compensatória definida e ativa
- [ ] Justificação técnica e de negócio para a aceitação
- [ ] Data de início da aceitação
- [ ] Data de expiração (sunset)
- [ ] Owner do risco (responsável pelo acompanhamento)
- [ ] Aprovação formal (nome, role, data)
- [ ] Data de reavaliação agendada

---

## 7. Alçadas de aprovação

| Severidade | L1 | L2 | L3 |
|---|---|---|---|
| Low | Tech Lead | AppSec Engineer | AppSec Engineer |
| Medium | AppSec Engineer | AppSec Engineer | AppSec Engineer + GRC |
| High | AppSec Engineer | AppSec Engineer + Gestão | CISO |
| Critical | Não recomendado - plano de remediação obrigatório | Não aceitável sem CISO | Não aceitável |

---

## 8. Reavaliação e expiração

Todo o registo de risco aceite tem **data de expiração**. Na data de expiração, a equipa deve:

1. **Reavaliar o risco** - o contexto mudou? A mitigação compensatória continua eficaz?
2. **Decidir**: corrigir / renovar a aceitação / escalar
3. **Renovar com nova aprovação** se a aceitação for mantida - sem renovação automática
4. **Registar a decisão** com nova data de expiração e aprovação atualizada

Registos expirados sem reavaliação documentada são tratados como **risco não gerido** e devem ser escalados para AppSec.

---

## 9. Integração com o ciclo de desenvolvimento

| Momento | Ação esperada |
|---|---|
| Release / go-live | Verificar todos os riscos aceites ativos; confirmar que estão dentro do prazo e aprovados |
| Sprint review | Rever o estado dos riscos aceites com findings associados |
| Revisão de classificação de risco | Rever se os riscos aceites continuam compatíveis com o nível |
| Incidente de segurança | Verificar se algum risco aceite contribuiu para o incidente; forçar reavaliação imediata |

---

## 10. Artefactos

| Artefacto | Localização sugerida | Retenção |
|---|---|---|
| Registo de risco aceite | `docs/security/risk-acceptance/` ou plataforma GRC | 2 anos após expiração |
| Evidência de mitigação compensatória | Associada ao registo | Enquanto o risco estiver ativo |
| Aprovações formais | Associadas ao registo (PR, issue, documento assinado) | 2 anos após expiração |

---

## 11. Responsabilidades

| Role | Responsabilidade |
|---|---|
| Developer / Tech Lead | Identificar e reportar riscos residuais; iniciar o processo de aceitação |
| AppSec Engineer | Avaliar, validar e aprovar aceitações; monitorizar registos ativos |
| GRC / Compliance | Garantir rastreabilidade e conformidade do registo; emitir relatórios periódicos |
| CISO | Aprovar aceitações de alto risco; supervisionar o programa de gestão de risco residual |
| Gestão de Produto | Participar nas decisões de aceitação com impacto no negócio |

---

## 12. Revisão e auditoria desta política

Esta política deve ser **revista anualmente** ou após qualquer um dos seguintes eventos:

- Incidente de segurança originado num risco previamente aceite
- Alteração dos limiares de tolerância ao risco da organização
- Alteração regulatória com impacto nos critérios de aceitação

O registo de riscos aceites deve ser disponibilizado integralmente em auditorias de segurança internas e externas.

---

## 13. Referências normativas e técnicas

| Referência | Relevância |
|---|---|
| SbD-ToE Cap. 01 - Classificação de Aplicações | Critérios de aceitação de risco por nível |
| SbD-ToE Cap. 03 - Threat Modeling | Justificação formal de risco aceite em ameaças |
| SbD-ToE Cap. 10 - Testes de Segurança | Aceitação de risk em findings de testes |
| SbD-ToE Cap. 14 - Governança e Contratação | Processo formal de exceções com alçadas |
| ISO/IEC 27001 - Cláusula 6.1.3 | Tratamento do risco de segurança da informação |
| NIST SP 800-30 | Guide for Conducting Risk Assessments |
| SSDF PW.4 | Revisão de software para gestão de risco |
