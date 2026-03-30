---
id: intro
title: Assets Organizacionais
description: Políticas, templates e guias para implementação do framework SbD-ToE
---

# 🏛️ Assets Organizacionais

Bem-vindo ao repositório centralizado de **políticas organizacionais** e **templates de implementação** do framework **Security by Design – Theory of Everything (SbD-ToE)**.

## 📌 O que encontra aqui

### **Políticas Organizacionais**

Estas são **políticas formais** que legitimam, operacionalizam e auditam as práticas de segurança descritas nos 14 capítulos do manual SbD-ToE.

**Por que políticas importam?**
- ✅ Tornam as práticas **vinculativas** em toda a organização
- ✅ Servem como base para **auditorias internas e externas**
- ✅ Permitem **rastreabilidade** de decisões de segurança
- ✅ Asseguram **consistência** nos processos

**Exemplos de políticas disponíveis:**
- 🎯 Classificação e Aceitação de Risco
- 📋 Requisitos de Segurança
- 🏗️ Arquitetura Segura
- 🔄 CI/CD Seguro
- 📦 Gestão de Dependências
- 🐳 Containers Seguros
- 📊 Monitorização e Operações
- 🎓 Formação e Onboarding

Cada política é **reutilizável**, **adaptável** à vossa organização e **alinhada** com normas como ISO/IEC 27005, NIST SSDF, OWASP SAMM e CIS Controls.

---

## 🔗 Referência Cruzada

As políticas estão **mapeadas aos capítulos do manual**:

| Capítulo | Políticas Recomendadas |
|----------|------------------------|
| 1. Classificação de Aplicações | Classificação de Risco, Revisão Periódica, Rastreabilidade |
| 2. Requisitos de Segurança | Requisitos de Segurança, Integração em Backlog |
| 3. Threat Modeling | Threat Modeling, Validação de Modelos |
| 4. Arquitetura Segura | Arquitetura Segura, Aprovação Técnica de Design |
| 5. Dependências (SBOM/SCA) | Dependências, SBOM, Exceções CVE, Atualizações Automáticas |
| 6. Desenvolvimento Seguro | Guidelines de Desenvolvimento, Revisão de Código, GenAI |
| 7. CI/CD Seguro | CI/CD Seguro, Gestão de Segredos |
| 8. IaC & Infraestrutura | IaC Seguro, Aprovação de Plans |
| 9. Containers e Imagens | Containers Seguros, Golden Base Images |
| 10. Testes de Segurança | Estratégia de Testes, PenTesting |
| 11. Deploy Seguro | Deploy Seguro, Aprovação de Release, Rollback |
| 12. Monitorização e Operações | Monitoring, Logging, Alertas, Incident Response |
| 13. Formação e Onboarding | Formação de Segurança, KPIs de Formação |
| 14. Governança e Contratação | Contratação Segura, Governança, Traceability Organizacional |

---

## 📂 Estrutura

```
020-assets/
├── intro.md (este ficheiro)
└── policies/
    ├── 01_policy-dast-fuzzing.md
    ├── 02_policy-classificacao-risco.md
    ├── 03_policy-aceitacao-risco.md
    └── ... (mais 34 políticas)
```

---

## 🚀 Como Usar

1. **Identifique o seu capítulo**: Selecione qual capítulo do manual SbD-ToE é relevante para a vossa iniciativa
2. **Consulte a política correspondente**: Cada capítulo aponta às políticas recomendadas
3. **Adapte à vossa organização**: Use as políticas como base, personalizando conforme o contexto
4. **Implemente e audite**: Garanta conformidade através de auditorias periódicas

---

## 💡 Normas & Frameworks Alinhados

As políticas aqui documentadas estão alinhadas com:

- 🔒 **ISO/IEC 27005** – Gestão de Risco de Informação
- 🛡️ **NIST SSDF** – Secure Software Development Framework
- 📋 **OWASP SAMM** – Software Assurance Maturity Model
- 🎯 **CIS Controls v8** – Controles de Segurança Críticos
- 🌐 **ENISA Risk Management** – Recomendações Europeias

---

## 📞 Suporte

Para dúvidas, contribuições ou feedback sobre estas políticas, consulte:
- **Documentação do Manual**: [Security by Design – Manual Completo](/sbd-toe/sbd-manual/)
- **Repositório**: https://github.com/Shiftleftpt/SbD-ToE-Manual

**Última atualização**: 30 de Março de 2026
