---
id: gestao-excecoes
title: Excepções a Requisitos de Segurança Aplicacionais
description: Especificidades da gestão de excepções no contexto dos requisitos aplicacionais do Cap. 02
tags: [exceções, requisitos, risco, validação, aplicacional]
---

# Excepções a Requisitos de Segurança Aplicacionais

> Processo base, alçadas, campos obrigatórios, cadeia de autoridade e lifecycle estão definidos em **Cap. 14 — `addon/12-processo-excecoes.md`**. Este ficheiro define apenas as especificidades deste domínio.

---

## Âmbito

Excepções a requisitos do catálogo aplicacional: `AUT`, `ACC`, `LOG`, `SES`, `VAL`, `ERR`, `CFG`, `ENC`, `API`, `INT`.

---

## Triggers específicos deste domínio

- framework ou biblioteca sem suporte nativo ao controlo (ex: ausência de MFA, limitação de validação de input);
- componente de terceiro integrado sem possibilidade de modificação no âmbito do projecto;
- contexto de MVP ou prova de conceito com escopo de risco L1 explicitamente delimitado;
- conflito com requisito funcional ou contratual com evidência documentada;
- migração progressiva de sistema legado com janela de não-conformidade conhecida e temporalmente delimitada.

---

## Identificação do requisito afectado

O campo "Requisito afectado" deve identificar:

- ID canónico do catálogo aplicacional (ex: `AUT-003`, `VAL-002`, `ENC-005`);
- tag operacional do projecto (ex: `SEC-L2-AUT-003`).

---

## Referências cruzadas

| Documento | Relação |
|---|---|
| `01-catalogo-requisitos.md` | Catálogo aplicacional — requisitos que podem ter excepções |
| `04-rastreabilidade-controlo.md` | Matriz de rastreabilidade onde a excepção é registada |
| Cap. 14 — `addon/12-processo-excecoes.md` | Processo canónico de gestão de excepções |
