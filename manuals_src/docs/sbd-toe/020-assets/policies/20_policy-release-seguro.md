---
id: policy-release-seguro
title: Política de Release Seguro
description: Política organizacional que define os requisitos para a aprovação formal de releases de software, incluindo checklist de segurança pré-release, gate automático de conformidade, critérios go/no-go, artefacto imutável de decisão e rastreabilidade ponta-a-ponta commit→pipeline→release, proporcional ao nível de criticidade (L1, L2, L3).
tags: [policy, release, go/no-go, checklist, gate, aprovação, artefacto imutável, rastreabilidade, cap10, cap11, L1, L2, L3, governance]
sidebar_position: 20
---

# Política de Release Seguro

## 1. Objetivo

Esta política define os requisitos para a **aprovação formal de releases de software**, garantindo que nenhuma versão é promovida a produção sem evidência documentada de conformidade com os requisitos de segurança aplicáveis.

Uma release é uma decisão de risco — não apenas uma operação técnica. Sem critérios de go/no-go explícitos, a decisão de promover a produção é tomada implicitamente, por omissão, sem visibilidade sobre o estado real de segurança. Esta política formaliza esse processo: a promoção a produção é um ato deliberado, com evidência agregada, aprovação registada e responsabilidade atribuída.

O objetivo desta política é garantir que:

- Cada release tem uma checklist de segurança verificada e registada
- O gate de segurança pré-release é automático e produz um resultado binário (Aprovado/Rejeitado)
- A decisão de go/no-go é tomada por pessoa com autoridade adequada e registada com identidade e timestamp
- O artefacto promovido a produção é imutável — é o mesmo que passou pelos testes, não uma nova build
- A rastreabilidade commit→pipeline→release é verificável em qualquer momento

---

## 2. Âmbito e obrigatoriedade

| Nível | Obrigatoriedade |
|---|---|
| L1 | Recomendado; checklist simplificada; aprovação do Tech Lead |
| L2 | Obrigatório; checklist completa; gate automático; aprovação formal |
| L3 | Obrigatório; checklist completa; gate automático; dupla aprovação; artefacto de decisão imutável |

---

## 3. Gate de segurança pré-release

O pipeline deve incluir um job `release-security-gate` executado antes de qualquer promoção a produção, que:

- [ ] Agrega os resultados de todos os gates de segurança do ciclo de build (SAST, SCA, DAST, secret detection)
- [ ] Verifica que nenhum finding bloqueante está em aberto sem exceção formal aprovada
- [ ] Verifica que o SBOM está gerado e assinado (L2/L3)
- [ ] Verifica que o artefacto candidato tem assinatura válida (L2/L3)
- [ ] Produz um relatório de resultado binário: **APROVADO** ou **REJEITADO**
- [ ] Arquiva o relatório como artefacto imutável da release (ligado à tag/versão)

O gate não substitui a aprovação humana — bloqueia a promoção se os critérios automáticos não forem cumpridos, e fornece evidência para que a aprovação humana seja informada.

---

## 4. Checklist de segurança pré-release

Antes de cada release, a checklist seguinte deve ser preenchida e arquivada:

### 4.1 Critérios obrigatórios

| Critério | L2 | L3 |
|---|---|---|
| Findings Critical abertos: 0 (ou exceção aprovada) | Obrigatório | Obrigatório |
| Findings High abertos: 0 (ou exceção aprovada) | Obrigatório | Obrigatório |
| Findings Medium abertos sem exceção | Tolerado com registo | Bloqueante |
| Secret detection: nenhum finding aberto | Obrigatório | Obrigatório |
| SBOM gerado e assinado para esta versão | Obrigatório | Obrigatório |
| Artefacto assinado e verificável | Obrigatório | Obrigatório |
| DAST executado em staging para esta release | Obrigatório | Obrigatório |
| Cobertura DAST ≥ threshold definido | Recomendado | Obrigatório |
| Exceções a CVEs: todas dentro de validade | Obrigatório | Obrigatório |
| Testes de regressão passados | Obrigatório | Obrigatório |
| Threat model atualizado (se houve alteração arquitetural) | Obrigatório | Obrigatório |
| PenTest concluído (se obrigatório para este ciclo) | Não aplicável | Obrigatório (anual ou por release major) |
| Documentação de segurança atualizada | Recomendado | Obrigatório |

### 4.2 Aceitação de risco residual

Se a release for aprovada com findings em aberto (com exceção formal), deve existir um registo de aceitação de risco residual que inclua:

- [ ] Identificação dos findings aceites e referência às exceções formais
- [ ] Justificação de negócio para prosseguir com risco residual
- [ ] Responsável pela aceitação e data
- [ ] Plano de resolução com prazo

---

## 5. Decisão go/no-go

### 5.1 Critérios de bloqueio automático (no-go)

A promoção a produção é automaticamente bloqueada se:

- O gate automático pré-release retornar estado REJEITADO
- Existir finding Critical ou High em aberto sem exceção formal válida
- O artefacto candidato não tiver assinatura válida (L2/L3)
- O SBOM não estiver gerado para esta versão (L2/L3)
- O DAST não tiver sido executado em staging para esta release candidata (L2/L3)

### 5.2 Aprovação humana

Mesmo quando o gate automático retorna APROVADO, a promoção a produção requer aprovação humana explícita:

| Nível | Aprovador mínimo | Formato |
|---|---|---|
| L1 | Tech Lead | Comentário ou PR de release aprovado |
| L2 | Tech Lead + AppSec Engineer | Registo formal no sistema de release ou PR de deploy aprovado |
| L3 | Tech Lead + AppSec Engineer (dupla aprovação) | Registo formal com identidade, timestamp e referência ao gate report |

A aprovação deve ser registada com:

- [ ] Identidade do aprovador (não delegável a conta partilhada)
- [ ] Timestamp
- [ ] Referência ao relatório do gate automático
- [ ] Referência ao artefacto aprovado (tag, digest ou hash)
- [ ] Estado da checklist de segurança

---

## 6. Imutabilidade do artefacto

O artefacto promovido a produção deve ser exatamente o mesmo que passou por todos os testes — não uma nova build do mesmo código:

- [ ] A promoção consiste em mover o artefacto já construído e testado para produção, não em reconstruir
- [ ] O artefacto é identificado por digest ou hash imutável, não apenas por tag
- [ ] A assinatura do artefacto é verificada no início do processo de deploy
- [ ] Qualquer rebuild implica reiniciar o ciclo completo de testes

:::warning
"Rebuild from source" como substituto de promoção de artefacto testado é proibido em L2/L3. Um build novo, mesmo a partir do mesmo commit, pode produzir artefactos diferentes (dependências resolvidas em momento diferente, variáveis de ambiente distintas, etc.) e não tem equivalência de segurança ao artefacto previamente testado.
:::

---

## 7. Rastreabilidade ponta-a-ponta

Para qualquer release em produção deve ser possível, em qualquer momento futuro, reconstruir a cadeia:

```
commit SHA → pipeline run → artefacto (digest) → SBOM → testes executados → aprovação de release
```

Para garantir esta rastreabilidade:

- [ ] Cada artefacto de produção é associado ao commit SHA que o originou
- [ ] O pipeline run que produziu o artefacto é referenciado
- [ ] O SBOM e os relatórios de teste são associados ao artefacto
- [ ] O registo de aprovação referencia o digest do artefacto aprovado

---

## 8. Registo histórico de releases

Para cada release, deve ser mantido um registo em `releases.md` (ou sistema equivalente) com:

| Campo | Descrição |
|---|---|
| Versão | Identificador da release (tag semântica) |
| Data de aprovação | Timestamp da decisão go/no-go |
| Aprovador(es) | Identidade(s) que aprovaram |
| Estado gate | APROVADO / REJEITADO (antes de override humano) |
| Findings em aberto | Número e referência a exceções |
| Artefacto | Digest ou hash do artefacto promovido |
| SBOM | Referência ao SBOM associado |
| Notas | Aceitação de risco residual, se aplicável |

---

## 9. Responsabilidades

| Role | Responsabilidade |
|---|---|
| Developer | Garantir que todos os findings bloqueantes estão resolvidos antes de solicitar release |
| Tech Lead | Coordenar o processo de release; verificar checklist; aprovar em L1/L2 |
| AppSec Engineer | Verificar relatórios de segurança; aprovar em L2/L3; validar exceções ativas |
| DevOps / SRE | Configurar gate automático; garantir imutabilidade do artefacto; executar deploy com artefacto aprovado |
| Product Manager | Decidir aceitação de risco residual quando existe conflito entre prazo e segurança |
| GRC / Compliance | Auditar registos de release; verificar rastreabilidade; validar retenção de evidências |

---

## 10. Revisão e auditoria desta política

Esta política deve ser **revista anualmente** ou após qualquer um dos seguintes eventos:

- Incidente originado em release aprovada com findings conhecidos não documentados
- Alteração do processo de deploy que afete a imutabilidade do artefacto
- Alteração regulatória que imponha requisitos adicionais de aprovação

---

## 11. Referências normativas e técnicas

| Referência | Relevância |
|---|---|
| SbD-ToE Cap. 10 — Testes de Segurança | Gate de segurança pré-release, checklist, aceitação de risco |
| SbD-ToE Cap. 11 — Deploy Seguro | Aprovação de deploy, imutabilidade de artefacto |
| SbD-ToE Cap. 07 — CI/CD Seguro | Rastreabilidade commit→pipeline→release |
| Política de Estratégia de Testes (`19_policy-estrategia-testes.md`) | Gates e thresholds de SAST/DAST/SCA |
| Política de SBOM (`11_policy-sbom.md`) | SBOM como evidência de release |
| Política de Aprovação de Release (`26_policy-aprovacao-release.md`) | Processo detalhado de aprovação em L3 |
| SLSA Framework | Integridade de build e promoção de artefactos |
| NIST SP 800-218 (SSDF) PW.8 | Archive and protect each software release |
| ISO/IEC 27001 — A.12.1 | Operational procedures and responsibilities |
