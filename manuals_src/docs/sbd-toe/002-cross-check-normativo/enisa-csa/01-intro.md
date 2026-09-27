---
id: intro
title: Certificação ENISA/CSA (EUCC, EUCS, EU5G) - Nota de Enquadramento
description: Quando usar e como mapear ao SbD-ToE (evidências, decisão e reaproveitamento)
tags: [certificacao, enisa, csa, eucc, eucs, eu5g, procurement]
sidebar_position: 9
---

# Certificação ENISA/CSA: quando usar e como mapear ao SbD‑ToE

> Veja também: [CRA](/sbd-toe/cross-check-normativo/cra/intro), [DORA](/sbd-toe/cross-check-normativo/dora/intro), [NIS2](/sbd-toe/cross-check-normativo/nis2/intro) e a [Nota de Convergência DORA & NIS2](/sbd-toe/cross-check-normativo/dora/convergencia-dora).
>
> Cobertura obrigação a obrigação: [Cobertura CSA/EUCC](/sbd-toe/cross-check-normativo/enisa-csa/cobertura).

## Âmbito {#âmbito}

### 🏛️ ENISA e Cybersecurity Act (CSA) {#️-enisa-e-cybersecurity-act-csa}

O **Cybersecurity Act** é o **Regulamento (UE) 2019/881** (CELEX: [32019R0881](https://eur-lex.europa.eu/legal-content/PT/TXT/?uri=CELEX:32019R0881)), que:

- reforça o mandato da **ENISA** enquanto agência europeia de cibersegurança; e
- estabelece um **quadro europeu de certificação de cibersegurança** para produtos, serviços e processos TIC.

O quadro prevê vários **sistemas europeus de certificação da cibersegurança** («esquemas», na designação corrente), entre eles:

- **EUCC** - para produtos de TIC (substituto evolutivo dos Common Criteria a nível europeu);
- **EUCS** - para serviços de computação em nuvem;
- **EU5G** - para redes e serviços 5G.

> 📅 **Estado em 2026.**  
> O EUCC foi adotado pelo Regulamento de Execução (UE) 2024/482 e está mapeado obrigação a obrigação na matriz de cobertura, com o CSA (arts. 51.º a 56.º). O EUCS e o EU5G não estão mapeados: ficam como referência, sem resposta de cobertura.

Do ponto de vista do SbD-ToE, a certificação ao abrigo do CSA implica, tipicamente:

- um **mapeamento claro entre requisitos de segurança** dos esquemas e controlos concretos (incluindo evidência técnica);
- **documentação robusta** de arquitetura, _threat modeling_, _hardening_, _secure development_ e _testing_;
- processos repetíveis de **gestão de vulnerabilidades**, _patching_, monitorização e resposta a incidentes;
- **governação e _ownership_ claros** sobre ativos, pipelines, ambientes e decisões de risco.

O manual SbD-ToE fornece a "camada de engenharia" que permite:

- desenhar e operar sistemas alinhados com os níveis de garantia definidos em cada sistema (no EUCC: substancial e elevado);
- produzir **artefactos de evidência** (SBOM, relatórios de testes, _runbooks_, matrizes de rastreabilidade) que podem ser usados em processos de avaliação de conformidade sob o CSA.

---

Os esquemas europeus de certificação de cibersegurança, no âmbito do **Cybersecurity Act (CSA)**, visam **reconhecimento UE** de que produtos/serviços cumprem requisitos de segurança. A **ENISA** elabora os projetos de sistema, a pedido da Comissão, que os adota por ato de execução; a certificação é executada por **Organismos de Avaliação da Conformidade (CABs)** acreditados e supervisionada por **autoridades nacionais**.

Esta nota explica "para quem se destina", quando é útil/necessária e como **reaproveitar controlos e evidências do SbD‑ToE**.

## O que este Manual cobre e o que fica de fora {#o-que-este-manual-cobre-e-o-que-fica-de-fora}

O SbD-ToE é centrado na aplicação: requisitos, arquitetura, código, dependências, pipeline, deploy e operação do software. Para cada obrigação do CSA e do EUCC, o Manual responde numa de três categorias, e nenhuma obrigação fica em silêncio:

- **Cobre**, e diz de que forma: requisito do catálogo, política, piso ou requisito acrescentado pelo regime, ou evidência de engenharia para um dever de outro plano.
- **Lacuna declarada**: o que o Manual não cobre por omissão, com o que falta.
- **Fora de âmbito**: o que o Manual não trata, com a razão.

A lista completa, obrigação a obrigação, é gerada da matriz de cobertura e está em [Cobertura](./cobertura#cobertura). Quando esta página e a lista divergirem, prevalece a lista.

A certificação é voluntária, salvo quando o direito da União ou dos Estados-Membros a torna obrigatória (CSA, art. 56.º, n.º 2). Por isso, este regime não tem contexto no overlay regulatório: não eleva nem acrescenta requisitos, e responde só nas três categorias.

O Manual cobre, entre outros, os objetivos de segurança do art. 51.º e do art. 51.º-A (cifragem, controlo de acessos, registo, SBOM, cópias de segurança com restauro testado e recuperação da aplicação), o ponto de contacto do art. 55.º, n.º 1, al. c) (`GOV-015`) e a notificação de incidentes do art. 56.º, n.º 8 ([Política 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória)).

**Lacunas declaradas, em resumo:**
- informações complementares de cibersegurança do art. 55.º (guia de utilização segura, período de apoio, repositórios de vulnerabilidades e avisos) e as obrigações do EUCC que delas dependem. Quando o produto está também sob o CRA, o período de apoio é prescrito pelo `CTX-CRA-R01`;
- divulgação pública de vulnerabilidades corrigidas e inscrição na base de dados europeia de vulnerabilidades (EUCC, art. 39.º); o aviso público sobre vulnerabilidades corrigidas é prescrito só no contexto CRA (`CTX-CRA-R03`);
- cálculo do potencial de ataque segundo os Critérios Comuns e a CEM (EUCC, art. 34.º, n.º 2) e análise das vulnerabilidades referida ao alvo de avaliação e ao certificado (arts. 33.º a 35.º);
- rota de atualização corretiva consciente da certificação (EUCC, anexo IV);
- conservação dos registos por 5 anos após a caducidade do certificado (EUCC, arts. 8.º, n.º 7, e 41.º, n.º 2);
- mecanismo de atualização segura no produto entregue ao utilizador, prescrito só para produtos CRA (`CTX-CRA-R02`), e avaliação das ferramentas de TIC de terceiros usadas na prestação do serviço (art. 51.º, al. j), e art. 51.º-A, al. g)).

**Fora de âmbito, por decisão do programa:**
- Segurança da entidade como um todo (rede corporativa e canais de administração, EDR, patching de sistemas operativos e equipamentos, inventário e classificação de todos os ativos): o Manual é centrado na aplicação.
- Relação formal com o organismo de certificação, o ITSEF e a autoridade nacional: plano da certificação, que este cross-check remete para o dossiê de certificação.
- Promoção, marca e rótulo do certificado e comunicação da sua suspensão: plano jurídico-comercial da certificação.
- Declaração UE de conformidade e assunção de responsabilidade (CSA, art. 53.º, n.º 2): plano jurídico da conformidade.
- Certificação de perfis de proteção: atividade de quem desenvolve perfis, não do processo de engenharia do produto.
- Disposições sobre a arquitetura do sistema de certificação (autoavaliação, níveis, retirada): não criam dever de engenharia.

## Para quem se destina {#para-quem-se-destina}

- **Fabricantes de produtos TIC** → sistema **EUCC** (Reg. de Execução (UE) 2024/482; base Critérios Comuns). Níveis de garantia: «substancial» (AVA_VAN 1–2) e «elevado» (AVA_VAN 3–5); o EUCC não prevê o nível «básico».
- **Prestadores de serviços Cloud** → esquema **EUCS** (para serviços cloud; não mapeado na matriz).
- **Fornecedores/Operadores 5G** → esquema **EU5G** (para redes e componentes 5G). Níveis: alinhados ao risco.
- **CABs/Laboratórios** → aplicam os critérios dos esquemas.
- **Autoridades nacionais de certificação da cibersegurança** → supervisionam e fazem cumprir as regras dos sistemas (e, no nível «elevado», emitem certificados); a ENISA publica os certificados no seu sítio Web.
- **Compradores (incl. setor público)** → usam certificados como critério de procurement.

Notas:
- A certificação é **voluntária**, salvo quando o direito da União ou dos Estados-Membros a torne obrigatória (CSA, art. 56.º, n.º 2); **cadernos de encargos** podem exigi-la por contrato.
- A certificação **não dispensa** as obrigações do **CRA** (declaração UE, marcação CE, obrigações pós-comercialização). Um certificado europeu que abranja requisitos essenciais do anexo I do CRA faz presumir a conformidade com esses requisitos (CRA, art. 27.º, n.º 8); com nível de garantia pelo menos «substancial», num sistema especificado por ato delegado, dispensa a avaliação por terceiros para os requisitos correspondentes (CRA, art. 27.º, n.º 9).

## Esquemas em foco {#esquemas-em-foco}

### EUCC - ICT products (base Common Criteria) {#eucc---ict-products-base-common-criteria}
Objetivo: evidenciar que um produto TIC cumpre requisitos e foi avaliado segundo uma **Target of Evaluation** e **Security Functional/Assurance Requirements**. 
Nível de garantia impacta a **profundidade de testes** e a **independência**.

### EUCS - Cloud services {#eucs---cloud-services}
Objetivo: evidenciar controlos de segurança e governança de serviços Cloud. Abrange **gestão de risco, IAM, cifragem, operação, continuidade**, etc.

### EU5G - Redes 5G {#eu5g---redes-5g}
Objetivo: evidenciar requisitos de segurança para fornecedores/operadores na cadeia 5G (equipamento, software, gestão, supply chain).

## Como se relaciona com DORA/NIS2/CRA {#como-se-relaciona-com-doranis2cra}

- Partilham a mesma “língua técnica” (cifragem, IAM, gestão de vulnerabilidades, testes, monitorização, continuidade).
- **CRA** impõe requisitos e **marcação CE** para produtos com elementos digitais; a certificação CSA pode fazer presumir a conformidade com os requisitos essenciais que abranja (CRA, art. 27.º, n.os 8 e 9), mas não substitui as restantes obrigações do fabricante.
- **NIS2/DORA** exigem maturidade técnica; a certificação pode **acelerar auditorias** e aceitar **certificados como prova** em procurement/regulação.

## Árvores de decisão (simplificadas) {#árvores-de-decisão-simplificadas}

1) O que é o meu objeto principal?
- Produto TIC (software/firmware/hardware com SW) → considerar **EUCC**
- Serviço Cloud (IaaS/PaaS/SaaS) → considerar **EUCS**
- Fornecedor/Operador 5G → considerar **EU5G**
- Outro → certificação CSA pode não ser aplicável

2) Há exigência externa?
- Regulador/lei/setor exige? → prosseguir com certificação
- Cliente/concursos pedem? → avaliar custo/benefício e o nível de garantia previsto no sistema (no EUCC: substancial ou elevado)
- Não há exigência? → manter “readiness” e evidências; decidir estrategicamente

3) Qual o nível?
- Mercado e risco baixo → o nível mais baixo previsto no sistema (no EUCC: substancial)
- Mercados críticos/altamente regulados → substancial ou elevado

## Mapeamento SbD‑ToE → Certificação (evidência típica) {#mapeamento-sbdtoe--certificação-evidência-típica}

| Domínio SbD‑ToE | O que demonstra | Relevância CSA |
|-----------------|-----------------|----------------|
| Cap. 02 - Requisitos | Políticas e controlos mínimos por nível | Critérios de segurança documentados |
| Cap. 04 - Arquitetura | Design seguro, IAM, cifragem, gestão de chaves | Controlos funcionais e de desenho |
| Cap. 05 - SBOM/SCA | Inventário de componentes, gestão de CVEs | Vulnerability management e supply chain |
| Cap. 06–07 - SDLC/CI‑CD | Gates, revisão, rastreabilidade, SoD | Secure lifecycle e integridade da build |
| Cap. 08–09 - IaC/Containers | Configurações seguras e runtime | Endurecimento e consistência |
| Cap. 10–11 - Testes/Release | SAST/DAST/fuzzing; gate sem vulnerabilidades conhecidas à saída (`DEP-002`); o mecanismo de atualização segura no utilizador só está prescrito para produtos CRA | Eficácia de controlos antes do release |
| Cap. 12 - Operações | Monitorização, resposta, recuperação da aplicação e cópias de segurança com restauro testado (`OPS-016`, `OPS-017`) | Resiliência operacional (continuidade de negócio da entidade: fora de âmbito) |
| Cap. 13 - Formação | Competências e awareness | Capacidade organizacional |
| Cap. 14 - Governação | RACI, fornecedores, auditoria | Gestão e rastreabilidade |

Sugere-se criar um **dossiê de certificação** com referências cruzadas (control matrix) entre requisitos do esquema (EUCC/EUCS/EU5G) e artefactos SbD‑ToE.

## Checklist de evidências (mínimo viável) {#checklist-de-evidências-mínimo-viável}

- [ ] Política de segurança (versão, aprovação, âmbito)
- [ ] Arquitetura e modelo de dados (inclui IAM/crypto/segregação)
- [ ] SBOM por release + registos SCA + SLAs de patch
- [ ] Pipelines com gates; logs de build/assinar, SoD (segregation of duties)
- [ ] Registos de testes (SAST/DAST/fuzzing/pen)
- [ ] Relatórios de qualidade de release e do gate sem vulnerabilidades conhecidas à saída (`DEP-002`)
- [ ] Monitorização, runbooks, exercícios de incidente e testes de restauro (`OPS-016`)
- [ ] Formação e registos (técnica/gestão)
- [ ] Gestão de fornecedores (contratos, cláusulas, avaliações)
- [ ] Trilho auditado (quem aprovou, quando, porquê)

## Métricas úteis {#métricas-úteis}

- % versões com SBOM publicado
- MTTP (tempo médio até patch) por severidade
- % releases bloqueadas por gate de segurança (e depois corrigidas)
- Cobertura de testes (SAST/DAST/fuzzing) por aplicação
- % controlos mapeados ao esquema escolhido

## Próximos passos {#próximos-passos}

1. Confirmar objeto (produto/serviço) e exigência externa (lei/cliente).  
2. Selecionar esquema e nível alvo (no EUCC: substancial ou elevado).  
3. Construir matriz de mapeamento requisito→evidência (SbD‑ToE).  
4. Preencher as lacunas declaradas na [cobertura](/sbd-toe/cross-check-normativo/enisa-csa/cobertura) (informações complementares do art. 55.º, divulgação pública de vulnerabilidades corrigidas, potencial de ataque CC/CEM, rota de correção consciente da certificação, retenção).  
5. Pré‑auditoria interna; depois selecionar CAB e calendarizar avaliação.  

## Referências {#referências}

- **Cybersecurity Act**: Regulamento (UE) 2019/881 (CELEX: [32019R0881](https://eur-lex.europa.eu/legal-content/PT/TXT/?uri=CELEX:32019R0881))
- ENISA - Páginas dos esquemas de certificação (EUCC, EUCS, EU5G)
- SbD‑ToE Capítulos 01–14; CRA/NIS2/DORA cross‑checks

**Versão:** 1.1  
**Data:** Setembro 2026 (alinhada com a matriz de cobertura do CSA e do EUCC)
