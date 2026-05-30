---
id: catalogo-requisitos
title: Definir o catálogo de Requisitos Aplicacionais
description: Lista essencial de requisitos de segurança organizados por categoria e nível de risco
tags: [tipo:catalogo, tema:requisitos, rastreabilidade, criticidade, ASVS]
---

<!--template: sbdtoe-addon -->

# Catálogo de Requisitos Aplicacionais

O **catálogo de requisitos de segurança** é um dos pilares do modelo SbD-ToE, funcionando como referência estruturada para garantir que cada aplicação, projeto ou sistema adota controlos adequados ao seu nível de risco, tipologia e contexto operacional.
O catálogo SbD-ToE fornece os **identificadores canónicos de referência** (`AUT-001`, `LOG-003`, etc.) - estáveis, independentes de projecto e alinhados com frameworks externos. Cada organização deve criar o seu próprio catálogo a partir desta base, e cada projecto instancia os requisitos aplicáveis sob a forma de **tags operacionais rastreáveis** (`SEC-L2-AUT-MFA`). A distinção entre os dois sistemas e o modelo de instanciação estão descritos em [Taxonomia e Rastreabilidade](./taxonomia-rastreabilidade).

A existência de um catálogo formal permite:
- Garantir **proporcionalidade** das exigências (L1, L2, L3), evitando sobrecarga ou lacunas;
- Assegurar **rastreabilidade** entre risco, requisito, controlo e evidência;
- Integrar os requisitos de segurança nos processos de desenvolvimento, auditoria e manutenção;
- Servir de base comum para curadoria, evolução e adaptação organizacional.

Neste capitulo inclui-se um catálogo que foi consolidado a partir de múltiplas fontes reconhecidas (ASVS, MSTG, NIST SSDF, IEC 62443, entre outras) e destina-se a ser **adaptado e curado por cada organização ou projeto**, de modo a garantir alinhamento com o contexto e o estado da arte. Não é imutável, é um documento vivo e deverá ser mantido regularmete e atualizado. 

---

## 📌 Como aplicar este catálogo no SbD-ToE

1. **Seleção proporcional**:  
   Cada requisito tem a indicação do(s) nível(is) de risco em que é obrigatório ou recomendado (L1, L2, L3).

2. **Curadoria contínua**:  
   Recomenda-se a revisão e adaptação periódica destes requisitos, acrescentando ou ajustando conforme o tipo de aplicação, ameaças emergentes e contexto do negócio.

3. **Integração operacional**:  
   O catálogo deve ser incorporado nos processos de backlog, definição de critérios de aceitação, testes e validação, bem como na documentação técnica e auditorias.

4. **Evolução e cobertura**:  
   Novos requisitos podem (e devem) ser acrescentados com base em lições aprendidas, incidentes, novos standards ou alterações de contexto.

---

## 📚 Consulta rápida dos requisitos base

Consulte a aplicação proporcional dos requisitos por domínio técnico no  
[Catálogo Base de Requisitos (anexo deste capítulo)](/sbd-toe/sbd-manual/requisitos-seguranca/addon/lista-requisitos-base):

- [AUT - Autenticação e Identidade](lista-requisitos-base#aut) 
- [ACC - Controlo de Acesso](lista-requisitos-base#acc) 
- [LOG - Registo e Monitorização](lista-requisitos-base#log)
- [SES - Sessões e Estado](lista-requisitos-base#ses) 
- [VAL - Validação de Dados](lista-requisitos-base#val)
- [ERR - Gestão de Erros](lista-requisitos-base#err)
- [CFG - Configuração Segura](lista-requisitos-base#cfg)
- [ENC - Dados Sensíveis e Criptografia](lista-requisitos-base#enc)
- [API - Segurança de APIs](lista-requisitos-base#api)
- [INT - Mensagens e Integrações](lista-requisitos-base#int)
- [REQ - Definição de Requisitos](lista-requisitos-base#req)
- [DST - Distribuição de Artefactos](lista-requisitos-base#dst)
- [IDE - Ferramentas de Desenvolvimento](lista-requisitos-base#ide)

Para consulta rápida da aplicação proporcional dos requisitos por nível de risco, ver o anexo “Catálogo Base de Requisitos” no final deste capítulo.
---

## 📌 Nota Final

O catálogo deve ser entendido como **referência viva e adaptável** - ponto de partida para a definição dos requisitos concretos de cada organização ou projeto, e para a integração efetiva da segurança em todo o ciclo de vida do software.

> Para validação, critérios de aceitação e evidências, consultar a secção de [validação de requisitos](./validacao-requisitos).
