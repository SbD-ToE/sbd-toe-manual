---
id: policy-deploy-seguro
title: Política de Deploy Seguro
description: Política organizacional que define os requisitos de segurança para o processo de deploy de software em produção, incluindo verificação de artefactos assinados, separação de ambientes, estratégias de rollout progressivo, separação entre automação e autorização humana, e rastreabilidade ponta-a-ponta, proporcional ao nível de criticidade (L1, L2, L3).
tags: [policy, deploy, deploy seguro, rollout, canary, blue-green, artefactos assinados, rollback, rastreabilidade, cap11, L1, L2, L3, governance]
grupo: pipeline-entrega
sidebar_position: 25
---

# Política de Deploy Seguro

## 1. Objetivo

Esta política define os requisitos de segurança para o **processo de deploy de software em ambientes de produção**, cobrindo desde a verificação de integridade do artefacto até à monitorização pós-deploy e capacidade de rollback.

O deploy é o momento em que o risco acumulado durante o desenvolvimento chega ao ambiente onde tem impacto real. Um deploy sem verificação de integridade do artefacto, sem aprovação formal, sem estratégia de rollout controlado ou sem capacidade de rollback rápido transforma um incidente potencialmente contido num evento de indisponibilidade ou comprometimento de difícil recuperação.

O objetivo desta política é garantir que:

- Apenas artefactos assinados e verificados são promovidos a produção
- O deploy é um acto deliberado com aprovação registada, não uma promoção automática implícita
- Estratégias de rollout progressivo reduzem o raio de impacto de regressões não detetadas
- O rollback é automatizado ou pode ser executado em tempo mínimo
- A rastreabilidade commit→pipeline→artefacto→deploy é verificável em auditoria

---

## 2. Âmbito e obrigatoriedade

| Nível | Obrigatoriedade |
|---|---|
| L1 | Recomendado; deploy via pipeline; rollback disponível |
| L2 | Obrigatório; artefacto assinado; aprovação formal; rastreabilidade completa |
| L3 | Obrigatório; dupla aprovação; rollout progressivo; monitorização activa pós-deploy |

---

## 3. Verificação do artefacto antes do deploy

Antes de iniciar qualquer deploy em staging ou produção, o pipeline deve verificar:

| Verificação | L1 | L2 | L3 |
|---|---|---|---|
| Artefacto identificado por digest SHA256 (não por tag flutuante) | Recomendado | Obrigatório | Obrigatório |
| Assinatura do artefacto válida (Cosign ou equivalente) | Recomendado | Obrigatório | Obrigatório + bloqueio automático |
| SBOM associado ao artefacto presente e acessível | Recomendado | Obrigatório | Obrigatório |
| Artefacto é o mesmo que passou pelos gates de segurança (sem rebuild) | Recomendado | Obrigatório | Obrigatório |
| Gate de segurança pré-release com resultado APROVADO | Recomendado | Obrigatório | Obrigatório |

:::warning
Um artefacto reconstruído a partir do mesmo código não é equivalente ao artefacto que passou pelos testes - dependências podem ter mudado, variáveis de ambiente de build podem diferir. O deploy deve sempre usar o artefacto original testado, identificado pelo seu digest.
:::

---

## 4. Aprovação formal de deploy

O deploy em produção requer aprovação humana explícita, registada com identidade e timestamp:

| Nível | Aprovador mínimo | Formato de registo |
|---|---|---|
| L1 | Tech Lead | Comentário ou aprovação no PR de deploy |
| L2 | Tech Lead + DevOps/SRE | Aprovação formal no pipeline ou sistema de release |
| L3 | Tech Lead + DevOps/SRE + AppSec Engineer (dupla aprovação) | Registo formal com identidade, timestamp, digest aprovado |

A aprovação deve referenciar:
- [ ] Versão e digest do artefacto aprovado
- [ ] Resultado do gate de segurança pré-release
- [ ] Ambiente destino

### 4.1 Separação entre automação e autorização irreversível

Ferramentas de automação podem executar deploys, mas não podem autorizar acções irreversíveis sem aprovação humana prévia registada:

- O pipeline executa mecanicamente o que foi aprovado - não decide
- A aprovação deve preceder a execução em ambientes de staging e produção
- Deploys automáticos sem aprovação humana são permitidos apenas em ambientes de desenvolvimento

---

## 5. Estratégias de rollout progressivo (L2/L3)

Em L2/L3, o deploy em produção deve usar uma estratégia de rollout progressivo para limitar o raio de impacto de regressões não detetadas em testes:

| Estratégia | Descrição | Aplicação |
|---|---|---|
| **Canary** | Percentagem crescente de tráfego (ex: 1% → 5% → 20% → 100%) com análise de métricas entre etapas | L2/L3 |
| **Blue-Green** | Dois ambientes equivalentes; mudança de routing após validação | L2/L3 |
| **Rolling update** | Substituição gradual de instâncias/pods, com health checks em cada etapa | L1/L2/L3 |

### 5.1 Critérios de promoção entre etapas

A promoção de uma etapa de rollout para a seguinte deve ser condicionada a:

- [ ] Taxa de erros HTTP abaixo do threshold definido (ex: < 0.1% de 5xx)
- [ ] Latência de resposta dentro dos limites normais (ex: P99 < 500ms)
- [ ] Ausência de alertas de segurança activos
- [ ] Ausência de crash loops ou restarts inesperados

### 5.2 Rollback automático por falha de critério

Se um critério de promoção falhar durante o rollout:

- [ ] O rollback é iniciado automaticamente para a versão anterior
- [ ] O rollout é pausado e o alerta é gerado
- [ ] A decisão de tentar nova promoção ou abortar é humana

---

## 6. Separação de ambientes e dados

O ambiente de produção deve estar estritamente separado dos ambientes de teste e staging:

- [ ] Credenciais de produção distintas das de staging - sem partilha de service accounts
- [ ] Dados de produção nunca copiados para staging sem anonimização
- [ ] Testes funcionais em staging com dados sintéticos ou anonimizados
- [ ] Sem acesso de escrita ao ambiente de produção a partir de jobs de teste

---

## 7. Gestão de segredos no deploy

Os segredos necessários em runtime são injectados exclusivamente no momento do deploy, não embebidos no artefacto:

- [ ] Segredos obtidos do cofre centralizado via workload identity (OIDC) ou via Kubernetes Secrets
- [ ] Nenhum segredo presente no artefacto de deploy (imagem, JAR, wheel)
- [ ] Secret scanning executado antes do deploy como gate adicional (L2/L3)

---

## 8. Rastreabilidade do deploy

Cada operação de deploy deve produzir um registo rastreável que permita reconstruir a cadeia completa:

```
commit SHA → pipeline run → artefacto (digest) → gate pré-release → aprovação → deploy → ambiente
```

Artefactos de evidência:

| Artefacto | Descrição | Retenção |
|---|---|---|
| Log de execução do deploy | Output completo do pipeline de deploy | 90 dias (L2), 1 ano (L3) |
| Registo de aprovação | Identidade, timestamp, digest aprovado | 1 ano (L2), 2 anos (L3) |
| Configuração de rollout | Estratégia e critérios de promoção | Versão activa |
| CHANGELOG e tags Git | Versionamento e metadata da release | Histórico |
| Rastreabilidade end-to-end | Referência cruzada commit→artefacto→deploy | Conforme Política de Rastreabilidade |

---

## 9. Feature flags e dark launches

Em L2/L3, funcionalidades de risco podem ser activadas de forma controlada via feature flags:

- [ ] Feature flags versionadas em configuração (YAML/JSON) e não hardcoded
- [ ] Activação e desactivação de feature flags auditadas (quem, quando, que flag)
- [ ] Feature flags de segurança (ex: nova lógica de autenticação) testadas com tráfego limitado antes de activação global
- [ ] Sem feature flags dependentes de segredos não geridos

---

## 10. Responsabilidades

| Role | Responsabilidade |
|---|---|
| Developer | Garantir que o artefacto é o mesmo que passou pelos testes; não fazer deploy manual fora do pipeline |
| DevOps / SRE | Configurar pipeline de deploy; implementar estratégia de rollout; configurar monitorização pós-deploy |
| AppSec Engineer | Verificar gates de segurança antes de aprovação; definir thresholds de rollout; rever configurações de deploy |
| Tech Lead | Aprovar deploy em L2/L3; coordenar rollback se necessário |
| GRC / Compliance | Auditar registos de aprovação; verificar rastreabilidade; validar retenção de logs |

---

## 11. Revisão e auditoria desta política

Esta política deve ser **revista anualmente** ou após qualquer um dos seguintes eventos:

- Incidente causado por deploy de artefacto não verificado ou sem aprovação formal
- Alteração da plataforma de orchestração ou da estratégia de rollout
- Incidente de exposição de segredos durante o processo de deploy

---

## 12. Referências normativas e técnicas

| Referência | Relevância |
|---|---|
| SbD-ToE Cap. 11 - Deploy Seguro | Artefactos assinados, gates, rollout, rollback, rastreabilidade |
| Política de Release Seguro (`20_policy-release-seguro.md`) | Gate pré-release e checklist de segurança |
| Política de Aprovação de Release (`26_policy-aprovacao-release.md`) | Processo de aprovação formal |
| Política de Rollback (`27_policy-rollback.md`) | Critérios e processo de rollback |
| Política de Gestão de Segredos (`18_policy-gestao-segredos.md`) | Injecção de segredos em runtime |
| SLSA Framework | Integridade de artefactos e proveniência |
| NIST SP 800-218 (SSDF) | PW.8, RV.1: deploy e monitorização |
| CIS Software Supply Chain Security | Controlos de deploy seguro |
