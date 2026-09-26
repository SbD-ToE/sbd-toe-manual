---
id: formacao-uso-seguro-ia-tooling
title: "Addon-12 - Training in the Secure Use of AI and Pervasive Tooling"
description: Training content to ensure the responsible and secure use of automated tools, code assistants and generative AI
tags: [formacao, ia, tooling, copilot, code-generation, llm, automacao, guardrails]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/13-formacao-onboarding/addon/12-formacao-uso-seguro-ia-tooling.md
  source_sha256: 498ac2af09637140dfba9625186b6094cacc36e371e6a6314ecfadaa1d32a5e2
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: a7510e2b52fb3320c84591c290e3f86952a581a37c611401c973dc91ea42aad3
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: d743dfcba33f930c34618b93d1eaaa34f697328d45aaf3bb657c33b8b3c59c9a
  glossary_keys: [chapter_role, instrument, llm, practitioner_manual, requirement_runtime, sbdtoe_sbd, validation_evaluation]
  glossary_sha256: 274931c697393230a6977112e9386c2d1b55fce0b67b344f4f53eb029547459f
  translated_at: 2026-09-26T11:44:23Z
  reviewed_by: null
---

# Addon-12 - Training in the Secure Use of AI and Pervasive Tooling

## 🎯 Objective {#-objetivo}

With the pervasive adoption of automated tools (SAST, DAST, SCA, GitHub Copilot, code generators, LLMs, SOAR, monitoring), it is critical that **training covers when to trust vs. when to validate**.

This addon defines the essential training content for each technical chapter of SbD-ToE, ensuring that members of staff understand:
- **When automation is deterministic** (it can be trusted)
- **When it is non-deterministic** (always validate)
- **Limits of automation** (guardrails)
- **Common anti-patterns** (insecure practices)

---

## 🧠 Fundamental Principle {#-princípio-fundamental}

**Tools are technical instruments, not autonomous decision-makers.**

- ✅ Automation **assists** humans in repetitive and objective tasks
- ❌ Automation **does not decide** in contexts that require judgement, context or trade-offs
- ⚠️ AI outputs **always require validation** before production

---

## 📖 Training Content by Technical Chapter {#-conteúdos-formativos-por-capítulo-técnico}

### Ch. 01 - Application Classification {#cap-01---classificação-de-aplicações}

**Tools**: Risk classification assistants, automated templates

**What to train**:
- ❌ **Anti-pattern**: Accepting an automatically generated classification without review
- ✅ **Good practice**: Classification is a governance decision, not an automatic one
- ✅ **Validate**: Criticality criteria (data, exposure, impact) against the real context
- ✅ **Escalate**: An L3 classification always requires AppSec + Management

**Practical example**:
```yaml
# ❌ MAU: Aceitar classificação gerada
risk_level: L2  # Gerado por ferramenta

# ✅ BOM: Validar e justificar
risk_level: L3
justification: "Aplicação processa dados GDPR + exposição pública + regulação NIS2"
approved_by: "AppSec Lead + CTO"
validation_date: "2026-01-04"
```

---

### Ch. 02 - Security Requirements {#cap-02---requisitos-de-segurança}

**Tools**: Requirements generators (LLMs, automated templates)

**What to train**:
- ❌ **Anti-pattern**: Copying generated requirements without adapting them to the context
- ✅ **Good practice**: Requirements must be specific, measurable and traceable
- ✅ **Validate**: Completeness (are all the critical domains covered?)
- ✅ **Validate**: Applicability (does the requirement make sense for this application?)

**Practical example**:
```markdown
<!-- Identificadores ilustrativos (EX-…); não correspondem ao Catálogo de Requisitos do Cap. 02. -->
❌ MAU: Requisito genérico gerado
EX-AUTH-001: "A aplicação deve implementar autenticação segura"

✅ BOM: Requisito específico e validado
EX-AUTH-001: "Autenticação via OAuth 2.0 + PKCE com MFA obrigatório para roles admin"
- Aplicável: ✓ (aplicação web com dados GDPR)
- Mensurável: ✓ (teste automatizado valida PKCE + MFA)
- Rastreável: ✓ (ligado a THR-001 threat model)
```

---

### Ch. 03 - Threat Modelling {#cap-03---threat-modeling}

**Tools**: LLMs for threat analysis (ChatGPT, GitHub Copilot for threat lists)

**What to train**:
- ❌ **Anti-pattern**: Accepting a generated threat model without AppSec validation
- ✅ **Good practice**: Threat models are contextual and require knowledge of the system
- ✅ **Validate**: Are the threats realistic for this architecture?
- ✅ **Validate**: Are the proposed controls adequate?

**Practical example**:
```markdown
❌ MAU: Ameaça genérica de LLM
THR-001: "SQL Injection"
Controlo: "Use prepared statements"

✅ BOM: Ameaça contextualizada
THR-001: "SQL Injection em endpoint /api/users/search (aceita query param não-validado)"
Arquitetura: Node.js + PostgreSQL
Controlo: "Parametrized queries via node-postgres + input validation com Joi schema"
Validação: "Teste SAST (Semgrep rule sql-injection) + DAST (OWASP ZAP payload)"
Aprovação: "AppSec Lead validou arquitetura e controlo"
```

---

### Ch. 04 - Secure Architecture {#cap-04---arquitetura-segura}

**Tools**: Diagram generators (Mermaid, PlantUML), ADR assistants

**What to train**:
- ❌ **Anti-pattern**: Accepting generated architecture diagrams without validation
- ✅ **Good practice**: Architecture requires trade-offs (security vs. performance, cost, complexity)
- ✅ **Validate**: Does the diagram reflect the real implementation?
- ✅ **Validate**: Do the ADRs have a security analysis and formal approval?

**Practical example**:
```markdown
❌ MAU: ADR gerado sem contexto
ADR-001: "Use microservices"
Razão: "Better scalability"

✅ BOM: ADR com análise de segurança
ADR-001: "Adotar API Gateway (Kong) para autenticação centralizada"
Contexto: "Aplicação L3 com 5 microservices, cada um com autenticação própria (inconsistente)"
Decisão: "Kong API Gateway + OAuth 2.0 + rate limiting"
Trade-offs:
  - ✅ Segurança: Autenticação centralizada, rate limiting, auditoria
  - ❌ Complexidade: Novo componente a manter
  - ❌ Custo: Licença Kong Enterprise
Ameaças mitigadas: THR-001 (credential stuffing), THR-002 (DoS)
Aprovação: "Arch Lead + AppSec + CTO"
```

---

### Ch. 05 - Dependencies, SBOM, SCA {#cap-05---dependências-sbom-sca}

**Tools**: SCA (Snyk, Dependabot, npm audit, safety)

**What to train**:
- ❌ **Anti-pattern**: Accepting every update suggestion without analysis
- ❌ **Anti-pattern**: Ignoring every alert (alert fatigue)
- ✅ **Good practice**: Understanding false positives vs. real risks
- ✅ **Validate**: Is the CVE applicable to the way the library is used here?
- ✅ **Validate**: Does the update break compatibility?

**Practical example**:
```markdown
❌ MAU: Ignorar CVE sem análise
CVE-2024-12345 (lodash): ALTA
Ação: ❌ Ignorado (muitos alertas)

✅ BOM: Analisar e decidir formalmente
CVE-2024-12345 (lodash): ALTA - Prototype pollution
Análise:
  - Aplicável? ✓ (usamos lodash.set com input do utilizador)
  - Exploitável? ✓ (endpoint público /api/config)
  - Mitigação disponível? ✓ (atualizar para 4.17.22)
Decisão: "Atualizar para 4.17.22 + teste de regressão"
Aprovação: "Tech Lead + AppSec"
Evidência: "PR-123 com testes + validação staging"
```

---

### Ch. 06 - Secure Development {#cap-06---desenvolvimento-seguro}

**Tools**: GitHub Copilot, ChatGPT, code generators, Cursor, Tabnine

**What to train**:
- ❌ **Anti-pattern**: Accepting generated code without reading/testing it
- ❌ **Anti-pattern**: Accepting a batch of suggestions (committing everything at once)
- ✅ **Good practice**: **Always read** suggested code line by line
- ✅ **Good practice**: **Always test** with unit tests before committing
- ✅ **Good practice**: **Always validate** against the security requirements

**Practical example**:
```python
# Identificadores ilustrativos (EX-…); não correspondem ao Catálogo de Requisitos do Cap. 02.
# ❌ MAU: Código gerado por Copilot aceito sem revisão
def authenticate_user(username, password):
    # Copilot gerou isto:
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    # ❌ SQL Injection! Mas dev não leu, só aceitou

# ✅ BOM: Código revisado e corrigido
def authenticate_user(username, password):
    # Dev leu sugestão, identificou problema, corrigiu:
    query = "SELECT * FROM users WHERE username=%s AND password=%s"
    cursor.execute(query, (username, hash_password(password)))
    # ✅ Parametrized query + password hashing
    # ✅ Teste unitário criado: test_sql_injection_blocked()
    # ✅ Validado contra EX-AUTH-001
```

**Secure prompt engineering practices**:
```markdown
❌ MAU: Prompt vago
"Generate authentication code"

✅ BOM: Prompt com requisitos de segurança
"Generate authentication code using bcrypt for password hashing, 
parametrized SQL queries to prevent injection, and session tokens 
with 15-minute expiry. Include unit tests for SQL injection and 
password strength validation."
```

---

### Ch. 07 - Secure CI/CD {#cap-07---cicd-seguro}

**Tools**: Pipeline automation (GitHub Actions, GitLab CI, Jenkins)

**What to train**:
- ❌ **Anti-pattern**: Blindly trusting automatic gates without understanding the criteria
- ✅ **Good practice**: Understanding when gates are deterministic vs. non-deterministic
- ✅ **Validate**: Why did the gate block? Is it a false positive?
- ✅ **Escalate**: When to request a formal exception?

**Practical example**:
```yaml
# Gate automático bloqueou deploy
❌ MAU: Dev ignora gate (cria PR para remover gate)

✅ BOM: Dev analisa e decide
Gate bloqueado: "SAST encontrou SQL injection em user_controller.py linha 45"
Análise:
  - É verdadeiro? ✓ (query concatena string de user input)
  - É crítico? ✓ (endpoint público, dados sensíveis)
Ação: "Corrigir código (parametrized query) + teste unitário"
Resultado: "Gate passa após correção"

# Caso de falso positivo
Gate bloqueado: "SAST: Uso de MD5 (inseguro)"
Análise:
  - Contexto: Usado para checksum de ficheiro, não criptografia
  - É falso positivo? ✓
Ação: "Solicitar exceção formal com justificação"
Aprovação: "AppSec valida contexto, aprova exceção com validade 6 meses"
```

---

### Ch. 08 - IaC and Infrastructure {#cap-08---iac-e-infraestrutura}

**Tools**: Terraform/CloudFormation generators, IaC assistants

**What to train**:
- ❌ **Anti-pattern**: Copying templates without validating the security configurations
- ✅ **Good practice**: IaC is code and requires the same validation as the application
- ✅ **Validate**: Are the IAM/RBAC permissions least privilege?
- ✅ **Validate**: Do critical resources have encryption at rest/in transit?

**Practical example**:
```hcl
# Identificadores ilustrativos (EX-…); não correspondem ao Catálogo de Requisitos do Cap. 02.
# ❌ MAU: Template gerado com permissões excessivas
resource "aws_iam_role" "app_role" {
  # Copilot gerou isto:
  policy = "*"  # ❌ Wildcard! Permite tudo
}

# ✅ BOM: Revisado e corrigido para mínimo privilégio
resource "aws_iam_role" "app_role" {
  policy = jsonencode({
    Statement = [{
      Effect = "Allow"
      Action = [
        "s3:GetObject",
        "s3:PutObject"
      ]
      Resource = "arn:aws:s3:::my-app-bucket/*"  # ✅ Scope específico
    }]
  })
  # ✅ Validado contra EX-IAM-001 (mínimo privilégio)
  # ✅ Teste: terraform plan + checkov scan
}
```

---

### Ch. 09 - Containers and Images {#cap-09---containers-e-imagens}

**Tools**: Dockerfile generators, Kubernetes manifest assistants

**What to train**:
- ❌ **Anti-pattern**: Using base images without validating their origin/vulnerabilities
- ✅ **Good practice**: Base images must be official, up to date and scanned
- ✅ **Validate**: Does the Dockerfile have no embedded secrets?
- ✅ **Validate**: Does the container run as non-root?

**Practical example**:
```dockerfile
# ❌ MAU: Dockerfile gerado com práticas inseguras
FROM ubuntu:latest  # ❌ Tag "latest" não é reproduzível
RUN apt-get install -y curl git  # ❌ Pacotes desnecessários
ENV API_KEY="sk-abc123..."  # ❌ Secret embebido!
USER root  # ❌ Roda como root

# ✅ BOM: Revisado e corrigido
FROM ubuntu:22.04  # ✅ Tag específica, reproduzível
RUN apt-get update && apt-get install -y curl \
    && rm -rf /var/lib/apt/lists/*  # ✅ Apenas o necessário + cleanup
# ✅ Secret via environment variable (injetado em runtime)
USER nonroot:nonroot  # ✅ Non-root user
# ✅ Validado: docker scan, trivy scan
# ✅ Teste: container inicia com user nonroot
```

---

### Ch. 10 - Security Testing {#cap-10---testes-de-segurança}

**Tools**: Test generators (Copilot for tests, ChatGPT, test automation)

**What to train**:
- ❌ **Critical anti-pattern**: Generated tests that merely "prove" the implemented code (tautology)
- ✅ **Good practice**: Tests must validate **requirements**, not the implementation
- ✅ **Validate**: Do the tests cover negative cases (failures, invalid inputs)?
- ✅ **Validate**: Are the tests independent of the implementation?

**Practical example - THE TAUTOLOGY PROBLEM**:

```python
# Identificadores ilustrativos (EX-…); não correspondem ao Catálogo de Requisitos do Cap. 02.
# ❌ MAU: Teste gerado por IA que apenas "prova" o código implementado
# Código implementado (com bug!)
def calculate_discount(price, user_role):
    if user_role == "admin":
        return price * 0.5  # ❌ BUG: Admin não deveria ter 50% desconto!
    elif user_role == "premium":
        return price * 0.8
    else:
        return price

# Teste gerado por Copilot (aceitou o bug!)
def test_calculate_discount():
    # ❌ Teste apenas "prova" que código funciona como implementado
    assert calculate_discount(100, "admin") == 50  # ✓ passa, mas valida BUG!
    assert calculate_discount(100, "premium") == 80
    assert calculate_discount(100, "guest") == 100

# ✅ BOM: Teste baseado em REQUISITOS, não implementação
# EX-DISC-001: "Descontos: premium=20%, guest=0%. Admin não tem desconto especial"

def test_calculate_discount_against_requirements():
    # ✅ Testa contra requisito EX-DISC-001
    assert calculate_discount(100, "admin") == 100  # ❌ FALHA! Bug detectado
    assert calculate_discount(100, "premium") == 80  # ✓
    assert calculate_discount(100, "guest") == 100   # ✓
    
    # ✅ Testa casos negativos (não gerados por IA!)
    assert calculate_discount(100, None) raises ValueError
    assert calculate_discount(-10, "premium") raises ValueError
    assert calculate_discount(100, "unknown_role") == 100  # default behavior
```

**Validation checklist for generated tests**:
- [ ] Does the test validate the **requirement**, not the implementation?
- [ ] Does the test cover **negative cases** (invalid inputs, failures)?
- [ ] Is the test **independent** of implementation details?
- [ ] **Would the test fail** if the implementation violated the requirement?
- [ ] Does the test have **clear assertions** (not merely "no crash")?

**Another example - Security tests**:
```python
# Identificadores ilustrativos (EX-…); não correspondem ao Catálogo de Requisitos do Cap. 02.
# ❌ MAU: Teste gerado que não testa segurança real
def test_authentication():
    # Copilot gerou:
    response = login("user", "password")
    assert response.status_code == 200  # ❌ Só testa se funciona, não se é seguro!

# ✅ BOM: Teste valida requisito de segurança EX-AUTH-001
def test_authentication_security():
    # ✅ Testa SQL injection
    response = login("admin' OR '1'='1", "anything")
    assert response.status_code == 401  # Deve bloquear
    
    # ✅ Testa brute force protection
    for i in range(10):
        login("user", "wrong_password")
    response = login("user", "correct_password")
    assert response.status_code == 429  # Rate limited
    
    # ✅ Testa password strength
    response = register("user", "123")  # Weak password
    assert response.status_code == 400
    assert "password too weak" in response.json()["error"]
```

---

### Ch. 11 - Secure Deployment {#cap-11---deploy-seguro}

**Tools**: Deploy automation (Terraform, Helm, Spinnaker, Argo)

**What to train**:
- ❌ **Anti-pattern**: Blindly trusting automatic rollback
- ✅ **Good practice**: Understanding when automatic rollback is safe vs. when it requires a human decision
- ✅ **Validate**: Can a DB rollback cause data loss?
- ✅ **Escalate**: When to trigger a manual vs. automatic rollback?

**Practical example**:
```yaml
# Deploy automation com guardrails
❌ MAU: Rollback automático sem validação
on_error: rollback  # ❌ Pode causar perda de dados se BD mudou!

✅ BOM: Rollback com validação de contexto
on_error:
  if: deployment_type == "binary"
    then: rollback_automatic  # ✅ Seguro: apenas binário
  elif: deployment_type == "database"
    then: rollback_manual_approval  # ⚠️ Exige decisão humana (perda de dados?)
    notify: ["DevOps", "DBA", "AppSec"]
  elif: deployment_type == "config"
    then: rollback_automatic  # ✅ Seguro: apenas config
```

---

### Ch. 12 - Monitoring and Operations {#cap-12---monitorização-e-operações}

**Tools**: SOAR, automatic alerts, behavioural correlation

**What to train**:
- ❌ **Anti-pattern**: Blindly trusting automatic alerts without validation
- ❌ **Anti-pattern**: Letting SOAR execute critical actions without human validation
- ✅ **Good practice**: Understanding when alerts are deterministic vs. heuristic
- ✅ **Validate**: Can a behavioural correlation alert be a false positive?
- ✅ **Escalate**: When to trigger an automatic vs. manual response?

**Practical example**:
```yaml
# Alerta determinístico (pode confiar)
alert: "CPU >90% por 5 minutos"
action: auto_scale  # ✅ Determinístico, ação segura

# Alerta não-determinístico (validar sempre)
alert: "Padrão de comportamento suspeito: User X downloads 10GB em 1h"
❌ MAU: SOAR bloqueia user automaticamente
✅ BOM: SOAR notifica IR para validação humana
  - IR valida: Processo legítimo de backup? Exfiltração?
  - Decisão humana: Bloquear ou exceção formal
  - Rastreabilidade: Decisão registada com justificação
```

---

## 🚨 Limits of Automation (Guardrails) - Synthesis {#-limites-de-automação-guardrails---síntese}

**What tools CANNOT do on their own**:

| Action | Automation Allowed? | Reason |
|------|---------------------|-------|
| Classify an application as L1/L2/L3 | ❌ NO | Governance decision, organisational context |
| Generate security requirements | ⚠️ Assist | A human validates completeness and applicability |
| Create threat models | ⚠️ Assist | AppSec validates that the threats are realistic for the architecture |
| Accept CVEs without analysis | ❌ NO | May be a false positive or not applicable |
| Generate code without review | ❌ NO | May contain vulnerabilities or logic bugs |
| Generate tests that "prove" the code | ❌ NO | Tests must validate requirements, not the implementation |
| Approve exceptions to findings | ❌ NO | Requires formal justification + human approval |
| Purge logs automatically | ❌ NO | Evidence is irreversible |
| Roll back a DB automatically | ❌ NO | May cause data loss |
| Block users by correlation | ❌ NO | Behavioural correlation is heuristic (false positive) |

---

## ✅ Validation Practices for AI Outputs {#-práticas-de-validação-de-outputs-de-ia}

### Universal Checklist (All Chapters) {#checklist-universal-todos-os-capítulos}

When using generation/assistance tools:

- [ ] **Read the code/output** line by line (do not accept in batch)
- [ ] **Test against requirements** (not merely "it works")
- [ ] **Validate the context** (does the output make sense for this application?)
- [ ] **Cover negative cases** (failures, invalid inputs)
- [ ] **Document the origin** (AI-generated code? mark it clearly)
- [ ] **Track decisions** (why accept/reject a suggestion?)
- [ ] **Escalate doubts** (do not assume correctness without understanding)

### Secure Prompt Engineering {#prompt-engineering-seguro}

```markdown
<!-- Identificadores ilustrativos (EX-…); não correspondem ao Catálogo de Requisitos do Cap. 02. -->
❌ MAU: Prompt vago
"Generate code for user authentication"

✅ BOM: Prompt com requisitos de segurança explícitos
"Generate user authentication code that:
- Uses bcrypt for password hashing (work factor 12)
- Implements rate limiting (5 attempts per 15 min)
- Validates input with Joi schema (email format, password min 12 chars)
- Uses parametrized SQL queries (prevent injection)
- Returns generic error messages (no user enumeration)
- Logs failed attempts with IP and timestamp
- Includes unit tests for SQL injection and brute force
- References EX-AUTH-001 and EX-AUTH-002"
```

---

## 📊 Training Effectiveness Metrics {#-métricas-de-eficácia-da-formação}

Training in the secure use of AI is effective when:

| Metric | Target | Measurement |
|---------|------|---------|
| PRs with untested generated code | 0 | Code review blocks |
| Generated tests that merely "prove" the code | 0 | QA validates against requirements |
| Exceptions to CVEs without justification | 0 | CI/CD gates block |
| Incidents caused by blind trust in alerts | 0 | Incident response audit |
| L3 classifications without AppSec approval | 0 | Governance audit |
| DB rollbacks without human validation | 0 | Deployment logs |
| Critical SOAR actions without IR validation | 0 | SOAR logs |

---

## 🎓 Integration into Training by Profile {#-integração-na-formação-por-perfil}

### Developer {#developer}

**Mandatory modules**:
- ✅ Secure use of GitHub Copilot and code assistants
- ✅ Secure prompt engineering (explicit requirements)
- ✅ Validation of generated code (read + test + requirements)
- ✅ Tests against requirements (no tautology!)
- ✅ When to escalate (security doubts)

**Practical labs**:
- Lab 1: Identify vulnerabilities in AI-generated code
- Lab 2: Create tests based on requirements (not on the implementation)
- Lab 3: Prompt engineering to generate secure code

---

### QA/Testing {#qatestes}

**Mandatory modules**:
- ✅ Limitations of test generators
- ✅ Validation of generated tests (do they cover the requirements?)
- ✅ Negative cases (failures, invalid inputs)
- ✅ Independence from the implementation

**Practical labs**:
- Lab 1: Identify "tautological" tests (they prove the code, not the requirements)
- Lab 2: Extend generated tests with negative cases
- Lab 3: Coverage validation (requirements vs. lines of code)

---

### DevOps/SRE {#devopssre}

**Mandatory modules**:
- ✅ When to trust deploy/rollback automation
- ✅ Rollback guardrails (DB, binary, config)
- ✅ When to escalate to manual validation
- ✅ Monitoring of automatic actions (audit)

**Practical labs**:
- Lab 1: Simulate a DB rollback with data loss
- Lab 2: Configure guardrails in a deploy pipeline
- Lab 3: Audit of automatic actions (SOAR logs)

---

### AppSec {#appsec}

**Mandatory modules**:
- ✅ False positives/negatives of SAST/DAST
- ✅ Validation of generated threat models
- ✅ Management of exceptions to findings
- ✅ Limits of automation (guardrails)

**Practical labs**:
- Lab 1: False positive analysis (context determines risk)
- Lab 2: Validation of a threat model generated by an LLM
- Lab 3: Creation of a formal exception template

---

### IR/Ops {#irops}

**Mandatory modules**:
- ✅ Limitations of SOAR
- ✅ When alerts require human validation
- ✅ Behavioural correlation (false positives)
- ✅ When to trigger an automatic vs. manual response

**Practical labs**:
- Lab 1: Identify a false positive in behavioural correlation
- Lab 2: Configure guardrails in SOAR
- Lab 3: Incident simulation with a mandatory human decision

---

### Management {#gestão}

**Mandatory modules**:
- ✅ When to accept automation risk
- ✅ When to require explicit governance
- ✅ Trade-offs (speed vs. security)
- ✅ Accountability for automated decisions

**Case studies**:
- Case 1: An automatic deploy caused data loss (lack of guardrails)
- Case 2: SOAR blocked a legitimate user (unvalidated false positive)
- Case 3: Generated code introduced a vulnerability (lack of review)

---

## 🏁 Conclusion {#-conclusão}

**Training in the secure use of AI is not optional**: it is critical to prevent:
- ❌ Vulnerabilities introduced by unreviewed generated code
- ❌ Tests that "prove" bugs instead of validating requirements
- ❌ Automated decisions without governance in critical contexts
- ❌ Blind trust in heuristic alerts/correlations

**Fundamental principle**: Tools **assist**, humans **decide**. Automation is an instrument, not a substitute for human judgement in non-deterministic contexts.

---

**Version**: 1.0  
**Last update**: Jan 2026  
**Maintained by**: AppSec + HR Team  
**Review**: Annual or triggered by a new risk
