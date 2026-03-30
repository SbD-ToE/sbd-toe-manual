---
id: excecoes
sidebar_position: 3
title: Excepções a Requisitos de Arquitectura Segura
description: Especificidades da gestão de excepções no contexto dos requisitos de arquitectura segura (ARC-001..013)
tags: [exceções, arquitectura, risco, rastreabilidade, adr]
---

# Excepções a Requisitos de Arquitectura Segura

> Processo base, alçadas, campos obrigatórios, cadeia de autoridade e lifecycle estão definidos em **Cap. 14 - `addon/12-processo-excecoes.md`**. Este ficheiro define apenas as especificidades deste domínio.

---

## Âmbito

Excepções a requisitos do catálogo de arquitectura: `ARC-001` a `ARC-013`.

---

## Triggers específicos deste domínio

- migração faseada entre ambientes ou arquitecturas com janela de não-conformidade delimitada e plano de conclusão;
- integração de componente herdado ou de terceiro sem possibilidade de modificação arquitectural no âmbito do projecto;
- custo de refactoring arquitectural desproporcionado face ao nível de risco efectivo do contexto (L1);
- decisão de arquitectura documentada em ADR com aceitação de risco explícita e aprovada.

---

## Identificação do requisito afectado

- ID canónico do catálogo (ex: `ARC-003`, `ARC-008`);
- tag operacional (ex: `SEC-L2-ARC-003`);
- referência ao ADR associado, se existir.

---

## Integração com rastreabilidade arquitectural

Excepções a requisitos ARC devem ser reflectidas na matriz de rastreabilidade (`06-rastreabilidade.md`), com:

- identificação da ameaça não mitigada pelo controlo em falta;
- referência ao ADR que documenta a decisão e as condições de reversão;
- data de expiração alinhada com o plano de arquitectura.

Excepções não registadas na matriz de rastreabilidade são tratadas como lacuna de cobertura.

---

## Alinhamento normativo

- ISO/IEC 27001 A.18.1.4 - aceitação formal de riscos residuais
- SSDF GV.3 - aprovação de excepções e desvios de processos de segurança
- OWASP SAMM Governance - registo e lifecycle de decisões excepcionais

---

## Referências cruzadas

| Documento | Relação |
|---|---|
| `01-catalogo-requisitos.md` | Catálogo ARC-001..013 - requisitos que podem ter excepções |
| `06-rastreabilidade.md` | Matriz de rastreabilidade onde a excepção é registada |
| Cap. 14 - `addon/12-processo-excecoes.md` | Processo canónico de gestão de excepções |
