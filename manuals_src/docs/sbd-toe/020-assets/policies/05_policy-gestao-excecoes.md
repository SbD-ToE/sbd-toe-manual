---
id: policy-gestao-excecoes
title: Política de Gestão de Exceções de Segurança
description: Política organizacional transversal que define o processo formal de submissão, avaliação, aprovação, registo e reavaliação de exceções a controlos de segurança obrigatórios, com alçadas proporcionais ao nível de risco da aplicação. Aplica-se a todos os capítulos SbD-ToE onde existam controlos com obrigatoriedade formal.
tags: [policy, exceções, gestão de exceções, aprovação, alçadas, TTL, mitigação compensatória, cap01, cap02, cap05, cap06, cap07, cap14, L1, L2, L3, governance, transversal]
sidebar_position: 5
---

# Política de Gestão de Exceções de Segurança

## 1. Objetivo

Esta política define o processo formal e transversal para a gestão de **exceções a controlos de segurança obrigatórios** definidos no modelo SbD-ToE.

Uma exceção ocorre sempre que um controlo obrigatório para o nível de criticidade da aplicação **não pode ser aplicado** dentro do prazo esperado, ou quando existe um desvio deliberado e justificado a uma prática ou requisito de segurança.

A existência de exceções é inevitável em qualquer programa de segurança maduro. O problema não é a exceção em si - é a exceção **informal, não registada, sem prazo e sem mitigação**. Exceções não geridas tornam-se dívida de risco permanente e são frequentemente o vetor de incidentes de segurança.

Esta política é **transversal** - aplica-se a todos os domínios e capítulos do manual SbD-ToE onde existam controlos com obrigatoriedade formal.

---

## 2. Âmbito

Esta política aplica-se a toda a organização e cobre exceções originadas em qualquer um dos seguintes contextos:

| Contexto | Exemplos |
|---|---|
| Controlos de requisitos não aplicados | Requisito obrigatório para o nível não implementado (Cap. 02) |
| Dependências com CVEs ativos | Vulnerabilidade sem fix disponível ou com impacto avaliado como aceitável (Cap. 05) |
| Padrões de código inseguros mantidos | Anti-pattern mantido por constrangimento técnico (Cap. 06) |
| Gates de CI/CD contornados | Override de gate de segurança sem aprovação formal (Cap. 07) |
| Findings de testes não corrigidos | Vulnerabilidade identificada por SAST/DAST/fuzzing sem remediação no SLA (Cap. 10) |
| Exceções arquiteturais | Padrão inseguro mantido por decisão de negócio ou técnica (Cap. 04) |
| Exceções IaC ou de containers | Configuração não conforme com baseline de segurança (Cap. 08, Cap. 09) |
| Controlos de deploy não aplicados | Gate ou validação não executada antes de promoção (Cap. 11) |

---

## 3. Princípios fundamentais

- **Toda a exceção é temporária** - não existe exceção permanente; toda a exceção tem data de expiração
- **Toda a exceção é documentada** - sem registo formal, não existe exceção; existe incumprimento
- **Toda a exceção tem owner** - alguém é explicitamente responsável pelo acompanhamento
- **Toda a exceção tem mitigação** - quando tecnicamente viável, existe um controlo compensatório ativo durante o período de exceção
- **A aprovação é proporcional ao risco** - a alçada de aprovação escala com o nível de criticidade e a severidade do controlo excecionado

---

## 4. Tipos de exceção

| Tipo | Descrição |
|---|---|
| **Exceção técnica** | Controlo técnico não implementável no prazo; dependência com vulnerabilidade ativa |
| **Exceção de processo** | Passo obrigatório do processo de segurança não executado (ex: gate contornado) |
| **Exceção arquitetural** | Decisão de design que não cumpre os padrões de arquitetura segura definidos |
| **Exceção regulatória** | Desvio a um requisito com implicações de conformidade normativa |

---

## 5. Processo formal de exceção

### 5.1 Passos obrigatórios

1. **Identificar o controlo excecionado** - qual o requisito, controlo ou prática que não está a ser cumprido
2. **Justificar tecnicamente** - por que razão o controlo não pode ser aplicado (constrangimento técnico, dependência externa, prazo, custo de implementação)
3. **Avaliar o impacto** - qual o risco adicional introduzido pela exceção no contexto da aplicação
4. **Definir mitigação compensatória** - que controlo alternativo fica ativo durante o período de exceção
5. **Definir prazo de expiração (TTL)** - data até à qual a exceção é válida; não existe renovação automática
6. **Submeter para aprovação** - pela alçada adequada ao nível de risco (ver secção 6)
7. **Registar formalmente** - no repositório de exceções da aplicação ou plataforma GRC
8. **Comunicar** - ao Security Champion e à equipa responsável

### 5.2 Checklist por registo de exceção

- [ ] Identificador único da exceção
- [ ] Controlo excecionado (ID do requisito ou controlo SbD-ToE, quando aplicável)
- [ ] Tipo de exceção (técnica / processo / arquitetural / regulatória)
- [ ] Descrição técnica do desvio e da sua origem
- [ ] Severidade do risco introduzido pela exceção (Critical / High / Medium / Low)
- [ ] Justificação técnica e de negócio
- [ ] Mitigação compensatória definida e verificável
- [ ] Owner da exceção (responsável pelo acompanhamento)
- [ ] Data de início da exceção
- [ ] Data de expiração (TTL)
- [ ] Aprovação formal (nome, role, data)
- [ ] Data de reavaliação agendada

---

## 6. Alçadas de aprovação por nível e severidade

| Severidade do risco introduzido | L1 | L2 | L3 |
|---|---|---|---|
| Low | Tech Lead | AppSec Engineer | AppSec Engineer |
| Medium | AppSec Engineer | AppSec Engineer | AppSec Engineer + GRC |
| High | AppSec Engineer | AppSec Engineer + Gestão de Produto | CISO |
| Critical | Não recomendado | CISO | Não aceitável como exceção |

:::warning
Exceções a controlos com impacto de risco **Critical** não são aceitáveis em L3. Em L2, requerem aprovação de CISO e plano de remediação ativo com prazo máximo de 7 dias. A aceitação de risco Critical é sempre uma medida de último recurso.
:::

---

## 7. Prazos máximos de validade (TTL)

| Nível | Severidade | TTL máximo |
|---|---|---|
| L1 | Qualquer | 90 dias |
| L2 | Low / Medium | 60 dias |
| L2 | High | 30 dias |
| L3 | Low / Medium | 30 dias |
| L3 | High | 14 dias |
| Qualquer | Critical | 7 dias (com plano de remediação obrigatório) |

A renovação de uma exceção exige **nova aprovação explícita** com reavaliação documentada. A renovação por omissão ou por timeout não é válida.

---

## 8. Reavaliação e encerramento

Cada exceção deve ser reavaliada na data de expiração. A equipa responsável deve:

1. **Reavaliar o risco** - o contexto mudou? A mitigação compensatória continua eficaz?
2. **Verificar se o controlo pode agora ser aplicado**
3. **Decidir**: encerrar (controlo aplicado) / renovar (nova aprovação) / escalar

Exceções expiradas sem reavaliação são tratadas como **incumprimento ativo** e devem ser escaladas para AppSec Engineer.

O ciclo de reavaliação segue a cadência mínima:

| Nível | Cadência de reavaliação |
|---|---|
| L1 | Na data de expiração |
| L2 | Semestral ou na data de expiração, o que ocorrer primeiro |
| L3 | Trimestral ou na data de expiração, o que ocorrer primeiro |

---

## 9. Integração com o ciclo de desenvolvimento

| Momento | Ação esperada |
|---|---|
| Release / go-live | Verificar todas as exceções ativas; confirmar que estão dentro do TTL e com mitigação ativa |
| Sprint review (L3) | Rever o estado das exceções associadas à aplicação |
| Revisão de classificação de risco | Verificar se exceções ativas continuam compatíveis com o nível |
| Incidente de segurança | Verificar se alguma exceção ativa contribuiu para o incidente; forçar reavaliação imediata |
| Auditoria | Disponibilizar registo completo de exceções ativas e históricas |

---

## 10. Bypass de controlos sem registo formal

O contorno de um controlo de segurança obrigatório **sem registo formal de exceção** é tratado como:

- Não-conformidade com esta política
- Escalada obrigatória para AppSec Engineer
- Registo no sistema GRC como desvio não autorizado
- Em contextos regulados (L3), potencial não-conformidade com obrigações normativas

O pipeline CI/CD e os processos de release devem, sempre que possível, impedir tecnicamente o contorno de gates sem registo formal.

---

## 11. Artefactos

| Artefacto | Localização sugerida | Retenção |
|---|---|---|
| Registo de exceção | `docs/security/exceptions/` ou plataforma GRC | 2 anos após encerramento |
| Evidência de mitigação compensatória | Associada ao registo | Enquanto a exceção estiver ativa |
| Aprovações formais | Associadas ao registo | 2 anos após encerramento |
| Relatório de exceções ativas | GRC / dashboard de conformidade | Atualizado continuamente |

---

## 12. Responsabilidades

| Role | Responsabilidade |
|---|---|
| Developer / Tech Lead | Identificar e reportar necessidade de exceção; iniciar o processo |
| Security Champion | Primeiro ponto de contacto para exceções na equipa; verificar completude do registo |
| AppSec Engineer | Avaliar, aprovar e monitorizar exceções; garantir mitigação eficaz |
| GRC / Compliance | Manter o registo centralizado; emitir relatórios periódicos; alertar sobre TTLs próximos |
| CISO | Aprovar exceções de alto risco; supervisionar o programa de gestão de exceções |
| Gestão de Produto | Participar nas decisões com impacto no negócio; assinar exceções que impliquem trade-offs de entrega |

---

## 13. Revisão e auditoria desta política

Esta política deve ser **revista anualmente** ou após qualquer um dos seguintes eventos:

- Incidente de segurança originado numa exceção mal gerida ou não registada
- Alteração dos limiares de tolerância ao risco da organização
- Alteração regulatória com impacto nos requisitos de gestão de exceções

O registo de exceções deve ser disponibilizado integralmente em auditorias internas e externas.

---

## 14. Referências normativas e técnicas

| Referência | Relevância |
|---|---|
| SbD-ToE Cap. 01 - Classificação de Aplicações | Proporcionalidade de exceções por nível |
| SbD-ToE Cap. 02 - Requisitos de Segurança | Exceções a requisitos com TTL curto em L3 |
| SbD-ToE Cap. 05 - Dependências, SBOM e SCA | Política de exceções a CVEs |
| SbD-ToE Cap. 06 - Desenvolvimento Seguro | Gestão de exceções técnicas |
| SbD-ToE Cap. 07 - CI/CD Seguro | Exceções e bypass controlado de gates |
| SbD-ToE Cap. 14 - Governança e Contratação | Processo formal de exceções com alçadas por nível |
| ISO/IEC 27001 - Cláusula 6.1.3 | Tratamento do risco - opção de aceitação |
| NIST SP 800-53 - CA-7 | Monitorização contínua e gestão de desvios |
| SSDF PW.4 | Revisão de software para gestão de risco |
