---
id: guia-preparacao-sandbox
title: Sandbox Preparation Guide for Contractors
description: Setup and use of an isolated environment for the practical training of contractors before access to real systems
tags: [governanca, contractors, sandbox, formacao, onboarding, pratica]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/13-formacao-onboarding/addon/13-guia-preparacao-sandbox.md
  source_sha256: 952bed0892f15019e4089b3636350760a9f15e49efad2d0e449a4c7c0be7ad28
  source_commit: 50f5914ebc90e4135e6678b2278709d5082dd237
  target_sha256: 6882dc34f2623b0c5a7487a4f90dac2df8ef5e596a3f379596a3b0e5dda9dde0
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [cycle_iteration, lifecycle_phase, practitioner_manual, threat, validation_evaluation]
  glossary_sha256: 6014d7b847404cbf1617297bddbc97ef01b3b72d355846ab682041beda1e42a4
  translated_at: 2026-09-27T07:06:06Z
  stamped_at: 2026-09-27T07:06:06Z
  reviewed_by: null
---

# Sandbox Preparation Guide for Contractors

**Version:** 1.0  
**Last update:** November 2025  
**Responsible:** DevOps + AppSec Engineer + Training Manager  
**Lifecycle:** Creation at T-5 days, active during onboarding (1–2 weeks), destruction after completion

---

## 📖 Objective {#-objetivo}

Provide an **isolated, secure and controlled environment** in which contractors practise:
- Use of corporate tools (Git, CI/CD, SCA, SAST, etc.)
- Security procedures (secrets management, MFA, etc.)
- Secure code workflows before real access to production

**Benefit:** Reduces the risk of error in production, increases the contractor's confidence, validates understanding of the policies.

---

## 🎯 Types of Sandbox (by Profile) {#-tipos-de-sandbox-por-perfil}

### 1️⃣ Sandbox for Developers {#1️⃣-sandbox-para-developers}

**Scope:** Git, CI/CD, secrets management, SAST/SCA, code review workflow

#### 1.1 Private GitHub/GitLab Organisation {#11-githubgitlab-organization-private}

```
Estrutura:
├─ Org: "sandbox-contractors"
├─ Team: "contractors-L1" (se L1)
├─ Repo: "sandbox-app-basic" (demo app segura)
│   ├─ Dockerfile (para container building)
│   ├─ package.json (com dependências)
│   ├─ .github/workflows (CI/CD demo)
│   ├─ README.md (onboarding guide)
│   └─ exercises/ (exercícios práticos)
└─ Repo: "sandbox-app-vulnerable" (app com vulnerabilidades intencionais - OWASP Top 10)
    ├─ SQL injection example
    ├─ XSS example
    ├─ CSRF example
    └─ Authentication bypass example
```

**Access:**
- The contractor receives an invite to the private organisation
- Permissions: **pull-only** initially
  - May clone and practise
  - May comment on issues/PRs
  - May not push directly
- After validation: **branch-write** (create branches, PR)
- Never: access to the main branch until final approval

**Duration:** 1 week

**Practical Exercises:**
1. Clone the repo and set up the local environment
2. Identify 3 vulnerabilities in `sandbox-app-vulnerable`
3. Write a secure test case
4. Create a PR (without merging) with a security improvement

---

#### 1.2 CI/CD Pipeline Demo (GitHub Actions / GitLab CI) {#12-cicd-pipeline-demo-github-actions--gitlab-ci}

```yaml
# .github/workflows/security-checks-demo.yml
name: Security Checks Demo

on: [pull_request]

jobs:
  sast:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run SonarQube SAST (demo)
        run: |
          # Simular execução de SonarQube
          echo "SAST: Checking code for vulnerabilities..."
          # Retorna findings (demo)
  sca:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run Snyk SCA (demo)
        run: |
          # Simular execução de Snyk
          echo "SCA: Checking dependencies for CVEs..."
  secrets:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Secrets scanning (demo)
        run: |
          # Simular secrets detection
          echo "Scanning for hardcoded secrets..."
```

**Objective:** The contractor sees the automatic workflow in action and understands the mandatory checks

---

#### 1.3 Secrets Management Demo (Vault / Azure Key Vault) {#13-secrets-management-demo-vault--azure-key-vault}

```
Setup Sandbox:
├─ Vault (local Docker ou cloud demo)
├─ Path: "/sandbox/contractors/{contractor-name}"
├─ Secrets pré-configurados:
│   ├─ API_KEY_DEMO=sk_demo_xxx (fake)
│   ├─ DB_PASSWORD=demo_password (fake)
│   └─ JWT_SECRET=demo_secret (fake)
└─ Instruções: Como aceder, rotacionar, reportar vazamento
```

**Exercise:** 
- The contractor accesses the Vault and reveals a secret
- Takes a screenshot of the process
- Learns that secrets must never be hardcoded

---

### 2️⃣ Sandbox for DevOps/Infrastructure {#2️⃣-sandbox-para-devopsinfrastructure}

**Scope:** IaC, containers, Kubernetes, secrets, CI/CD pipelines

#### 2.1 Kubernetes Sandbox Cluster {#21-kubernetes-sandbox-cluster}

```
Setup:
├─ Namespace: "sandbox-contractors"
├─ RBAC: Contractor tem role "viewer" + "editor" em namespace
├─ Deployments pré-criados:
│   ├─ demo-app (insegura)
│   ├─ demo-app-hardened (segura)
│   └─ metrics-server (para observability demo)
├─ Resources:
│   ├─ 2 pods, 1 GB RAM max, 500m CPU max
│   ├─ Network policies (demo)
│   └─ Security contexts (demo)
└─ Logs: Prometheus/Grafana acesso read-only
```

**Exercises:**
1. Deploy a simple application (via YAML manifest)
2. Compare security: "insecure vs. hardened" deployment
3. Identify 3 security issues
4. Propose fixes (IaC)

#### 2.2 Terraform/CloudFormation Demo {#22-terraformcloudformation-demo}

```
Scenario:
├─ Estado inicial: VPC insegura (open security groups)
├─ Contractor tarefa: Corrigir 5 issues de IaC
│   ├─ Add security group restrictions
│   ├─ Enable encryption
│   ├─ Add network policies
│   └─ Enable logging
└─ Validação: Terraform plan review (não apply)
```

---

### 3️⃣ Sandbox for QA/Testers {#3️⃣-sandbox-para-qatesters}

**Scope:** Security testing, OWASP, scanning tools

#### 3.1 Web App for Manual Testing (OWASP WebGoat / Juice Shop) {#31-web-app-para-teste-manual-owasp-webgoat--juice-shop}

```
Setup:
├─ Deploy OWASP Juice Shop em sandbox k8s
├─ Acesso: http://sandbox-qa.internal:8080
├─ Tasks pré-definidas:
│   ├─ SQL Injection (ranked by difficulty)
│   ├─ XSS (cross-site scripting)
│   ├─ CSRF (cross-site request forgery)
│   ├─ Broken authentication
│   └─ Sensitive data exposure
└─ Scoring: Contractor completa 70% das tasks
```

#### 3.2 ZAP (OWASP Zap) Demo Scanning {#32-zap-owasp-zap-demo-scanning}

```bash
# Setup ZAP no sandbox
docker run -t owasp/zap2docker-stable zap-baseline.py \
  -t http://sandbox-qa:8080 \
  -r report.html

# Contractor aprende:
# - Como executar DAST
# - Interpretar findings
# - Falsos positivos
# - Remediação
```

---

## 🚀 Creation and Provisioning Process {#-processo-de-criação-e-provisão}

### Timeline {#timeline}

```
T-5 dias: Setup começa
  ├─ DevOps cria infrastructure (repos, k8s ns, IaC)
  ├─ AppSec configura permissões e logging
  └─ Training Manager prepara exercícios

T-3 dias: Sandbox ready
  ├─ Teste de acesso funciona
  ├─ Documentação criada
  └─ Contractor recebe credenciais

T-0 (Onboarding):
  ├─ Contractor recebe email com links + instruções
  ├─ First exercise: "Setup environment locally"
  ├─ Daily check-ins com Tech Lead
  └─ Logging de atividade ativado

T+7 dias: Validação
  ├─ Contractor completou 70%+ de exercícios
  ├─ Quiz de compreensão passed (>80%)
  └─ Sign-off → Acesso real concedido
```

### Provisioning Checklist {#checklist-de-provisão}

```yaml
Pre-Sandbox:
  - [ ] Contractor validado (US-06 passed)
  - [ ] Role/função definida (Dev, DevOps, QA, etc.)
  - [ ] LMS enrollment completado
  - [ ] Email corporativo criado (ou temporário)

Sandbox Creation:
  - [ ] Git org criado (ou branch/namespace)
  - [ ] Demo repos clonados
  - [ ] K8s namespace criado
  - [ ] IaC templates preparados
  - [ ] Permissões RBAC configuradas (read-only initially)
  - [ ] Secrets criados (demo/fake values)
  - [ ] Logging/monitoring ativado

Access Provisioning:
  - [ ] Git credentials (SSH key ou token) entregues seguramente
  - [ ] Kubeconfig criado
  - [ ] VPN access (se necessário)
  - [ ] Email de boas-vindas com links + instruções

Validation:
  - [ ] Contractor conecta com sucesso (first login captured)
  - [ ] Pode clonar repos
  - [ ] Pode visualizar k8s namespace
  - [ ] Exercícios acessíveis
```

---

## 📋 Standard Exercises by Profile {#-exercícios-padrão-por-perfil}

### For Developers {#para-developers}

| # | Exercise | Duration | Objective | Success |
|----|-----------|---------|----------|---------|
| 1 | Clone & Setup | 1h | Get familiar with Git and the local dev env | Git clone OK, README followed |
| 2 | Identify Vulns | 2h | Understand the OWASP Top 10 | ≥3 vulns identified |
| 3 | Secure Coding | 2h | Write secure code | Function with a passing test |
| 4 | Create PR | 1h | PR workflow, code review | PR created correctly |
| **Total** | | **6h** | | ✅ Score ≥70% |

### For DevOps {#para-devops}

| # | Exercise | Duration | Objective | Success |
|----|-----------|---------|----------|---------|
| 1 | Deploy Insecure | 1h | Deploy the app on k8s | Pod running |
| 2 | Identify Issues | 2h | Security audit of IaC | ≥5 issues found |
| 3 | Hardening | 2h | Fix the issues (no apply) | Terraform plan review OK |
| 4 | Network Policies | 1h | Add restrictions | Policy defined |
| **Total** | | **6h** | | ✅ Score ≥70% |

### For QA/Testers {#para-qatesters}

| # | Exercise | Duration | Objective | Success |
|----|-----------|---------|----------|---------|
| 1 | OWASP Top 10 | 2h | Knowledge of common vulns | Quiz 70% |
| 2 | Manual Testing | 2h | Explore Juice Shop | ≥5 vulnerabilities exploited |
| 3 | DAST Scanning | 1h | Use ZAP | Report generated, findings interpreted |
| 4 | False Positives | 1h | Validation of the findings | 3+ false positives identified |
| **Total** | | **6h** | | ✅ Score ≥70% |

---

## 🔐 Sandbox Security {#-segurança-do-sandbox}

### Isolation {#isolamento}

- **Network:** The sandbox connects to the sandbox network, with no direct access to production
- **Storage:** Data in the sandbox is ephemeral (deleted after onboarding)
- **Compute:** Resource limits applied (CPU, memory, disk)
- **Logging:** All actions logged (read, write, delete)

### Monitoring {#monitorização}

```yaml
Logging:
  - Todos os logins capturados (timestamp, IP)
  - Git commits/pushes auditados
  - K8s API calls em audit log
  - Secret access tracked
  - Alertas se comportamento suspeito:
      - Download of /etc/shadow (Linux)
      - Git push com thousands of files
      - Multiple failed login attempts
```

### Post-Onboarding Destruction {#destruição-pós-onboarding}

```bash
# T+14 dias (ou após conclusão)
T-1 dia: Contractor notificado que sandbox será destruído amanhã
T+0: Backup de work realizado (se necessário)
     Contractor removido de org/namespace
     Credentials revogadas
     Resources deletados
     Logs arquivados (conforme a Política 29 §7)
```

---

## 📚 Documentation and Instructions {#-documentação-e-instruções}

Each sandbox includes a **README.md with:**

````markdown
# Sandbox Onboarding Guide

## Bem-vindo!

Este é seu ambiente de prática seguro. Aqui pode aprender sem risco de impactar produção.

### Quick Start

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/[org]/sandbox-app.git
   ```

2. **Setup local environment:**
   ```bash
   cd sandbox-app
   cp .env.example .env
   # Não substitua secrets - use Vault
   ```

3. **Executar testes de segurança:**
   ```bash
   npm install
   npm run test:security
   ```

### Exercícios

Comece com Exercício 1: [Link]

### Pedir Ajuda

- Slack: #sandbox-support
- Email: [security-email]
- Escalação: Tech Lead [name]

### Logs de Atividade

A sua atividade está sendo monitorizada (logs auditados). Isto é normal e esperado.

### Deadline

Exercícios devem ser completados até [data]. Quiz passa em [data + 1].

---
````

---

## 🎓 Integration with Ch. 13 (Training) {#-integration-com-cap-13-formação}

The sandbox is the **practical component of US-16 (Training Track)**:

- Theoretical track: LMS + online courses
- Practical track: sandbox exercises
- Validation: quiz + exercise score

**Completion SLA:** T+7 days = onboarding complete

---

## 🏁 End-of-Engagement Checklist {#-checklist-de-término}

```
[ ] Contractor completou 70% exercícios
[ ] Quiz score ≥80%
[ ] Tech Lead validou compreensão (conversation check-in)
[ ] AppSec Engineer reviewed logs (sem red flags)
[ ] Backup de work realizado
[ ] Sandbox credentials revogadas
[ ] Sign-off de conclusão assinado
[ ] Histórico arquivado (conforme a Política 33 §8)
[ ] Acesso real concedido (US-15 completo)
```

---

## 📎 Templates and Links {#-templates-e-links}

- [Contractor Validation Template](/sbd-toe/sbd-manual/governanca-contratacao/addon/template-validacao-contractors)
- [Technical Preparation - US-15](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-15---preparação-técnica-e-validação-de-contractors-pré-acesso)
- [Training and Onboarding - Ch. 13](/sbd-toe/sbd-manual/formacao-onboarding/aplicacao-lifecycle)
- [Offboarding Checklist](/sbd-toe/sbd-manual/governanca-contratacao/addon/checklist-offboarding)

---

## 🔄 Continuous Improvement {#-melhoria-contínua}

**Feedback Loop:**
1. The contractor completes the sandbox
2. The AppSec Engineer reviews the logs
3. Feedback captured (what worked, what was confusing)
4. Exercises iterated quarterly
5. New threat scenarios included

**Ownership:** DevOps + AppSec Engineer  
**Review:** Quarterly (minimum)


