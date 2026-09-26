---
id: guia-preparacao-sandbox
title: Sandbox Preparation Guide for Contractors
description: Setup and use of an isolated environment for the practical training of contractors before access to real systems
tags: [governanca, contractors, sandbox, formacao, onboarding, pratica]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/13-formacao-onboarding/addon/13-guia-preparacao-sandbox.md
  source_sha256: f5df336e9ded0859420177ac0535c83eb50c1dfffe105f67d12534a7c8f9f75b
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: f762776c7d738b787b951f3720ba14bf469eff2b2b8718c6091933ae53777f7f
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: d743dfcba33f930c34618b93d1eaaa34f697328d45aaf3bb657c33b8b3c59c9a
  glossary_keys: [cycle_iteration, lifecycle_phase, practitioner_manual, validation_evaluation]
  glossary_sha256: a69a2bb101cfd4e4e549bbca9ce816783635ce9bc40a6973f89207a71071f655
  translated_at: 2026-09-26T11:44:24Z
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
     Logs arquivados (7 anos)
```

---

## 📚 Documentation and Instructions {#-documentação-e-instruções}

Each sandbox includes a **README.md with:**

```markdown
# Sandbox Onboarding Guide

## Bem-vindo!

Este é seu ambiente de prática seguro. Aqui pode aprender sem risco de impactar produção.

### Quick Start

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/[org]/sandbox-app.git
   ```

2. **Set up the local environment:**
   ```bash
   cd sandbox-app
   cp .env.example .env
   # Não substitua secrets - use Vault
   ```

3. **Run the security tests:**
   ```bash
   npm install
   npm run test:security
   ```

### Exercises {#exercícios}

Start with Exercise 1: [Link]

### Asking for Help {#pedir-ajuda}

- Slack: #sandbox-support
- Email: [security-email]
- Escalation: Tech Lead [name]

### Activity Logs {#logs-de-atividade}

Your activity is being monitored (audited logs). This is normal and expected.

### Deadline {#deadline}

Exercises must be completed by [date]. The quiz takes place on [date + 1].

---
```

---

## 🎓 Integration com Cap. 13 (Formação)

Sandbox é **componente prático de US-16 (Trilho de Formação)**:

- Trilho teórico: LMS + cursos online
- Trilho prático: Sandbox exercises
- Validação: Quiz + Exercise score

**SLA de Conclusão:** T+7 dias = onboarding completo

---

## 🏁 Checklist de Término

```
[ ] Contractor completed 70% of the exercises
[ ] Quiz score ≥80%
[ ] Tech Lead validated understanding (conversation check-in)
[ ] AppSec Engineer reviewed the logs (no red flags)
[ ] Backup of work carried out
[ ] Sandbox credentials revoked
[ ] Completion sign-off signed
[ ] History archived (7 years)
[ ] Real access granted (US-15 complete)
```

---

## 📎 Templates e Links

- [Contractor Validation Template](/sbd-toe/sbd-manual/governanca-contratacao/addon/template-validacao-contractors)
- [Preparação Técnica - US-15](../aplicacao-lifecycle#us-15)
- [Formação e Onboarding - Cap. 13](/sbd-toe/sbd-manual/formacao-onboarding/aplicacao-lifecycle)
- [Offboarding Checklist](/sbd-toe/sbd-manual/governanca-contratacao/addon/checklist-offboarding)

---

## 🔄 Melhoria Contínua

**Feedback Loop:**
1. Contractor completa sandbox
2. AppSec Engineer revê logs
3. Feedback capturado (what worked, what was confusing)
4. Exercises iteradas trimestralmente
5. Novos cenários de ameaça incluídos

**Propriedade:** DevOps + AppSec Engineer  
**Revisão:** Quarterly (mínimo)


