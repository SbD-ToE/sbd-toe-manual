---
id: excecoes-e-aceitacao-risco
title: Excepções e Aceitação de Risco em Vulnerabilidades de Dependências
description: Especificidades da gestão de excepções no contexto de findings SCA/CVE
tags: [dependencias, sbom, sca, exceptions, cve]
---

# Excepções e Aceitação de Risco em Vulnerabilidades de Dependências

> Processo base, alçadas, campos obrigatórios, cadeia de autoridade e lifecycle estão definidos em **Cap. 14 — `addon/12-processo-excecoes.md`**. Este ficheiro define apenas as especificidades deste domínio.

---

## Âmbito

Excepções a findings de análise de composição de software (SCA) — vulnerabilidades em dependências identificadas por scanner, referenciadas por CVE ou equivalente.

---

## Triggers específicos deste domínio

Uma excepção SCA exige que **todos** os seguintes critérios sejam analisados e documentados:

- a vulnerabilidade não tem impacto directo no contexto de execução da aplicação (ex: dependência usada apenas no build, não no runtime);
- não existe versão alternativa viável com o mesmo comportamento esperado;
- existem controlos compensatórios eficazes e verificáveis (ex: sandboxing, WAF, isolamento de build);
- o risco residual é explicitamente documentado e aceite formalmente.

A ausência de patch disponível é condição necessária mas não suficiente para aprovação da excepção.

---

## Campos adicionais obrigatórios (SCA)

| Campo | Obrigatório | Notas |
|---|---|---|
| CVE / ID de vulnerabilidade | Sim | |
| Componente afectado | Sim | Nome e versão exacta (ex: `lib-legacy@1.0.4`) |
| Contexto de uso | Sim | `runtime` / `build-only` / `test-only` |
| Versão corrigida disponível? | Sim | Se sim, justificação para não aplicar |

---

## Template YAML

```yaml
- cve: CVE-YYYY-NNNNN
  componente: nome-do-pacote@versao
  contexto: build-only | runtime | test-only
  motivo: "Justificação técnica objectiva"
  controlo_compensatorio: "Controlo alternativo aplicado"
  aprovado_por: "nome@funcao"
  validade: "YYYY-MM-DD"
  revisao_agendada: true
```

Localização sugerida: `/security/excecoes-sca.yaml` no repositório, ou sistema centralizado com equivalência rastreável.

---

## Referências cruzadas

| Documento | Relação |
|---|---|
| `02-analise-sca.md` | Origem dos findings que podem originar excepção |
| `04-integracao-ci-cd.md` | Verificação de validade das excepções no pipeline |
| `08-rastreabilidade-vulnerabilidades.md` | Registo da decisão de aceitação de risco como estado final |
| Cap. 14 — `addon/12-processo-excecoes.md` | Processo canónico de gestão de excepções |
