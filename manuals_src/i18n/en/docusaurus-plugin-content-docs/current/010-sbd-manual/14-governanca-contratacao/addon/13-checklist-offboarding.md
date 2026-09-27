---
id: checklist-offboarding
title: Secure Offboarding Checklist
description: Formalised and executable procedure for the secure termination of contractors and suppliers
tags: [governanca, contractors, offboarding, rescisao, seguranca, auditoria]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/14-governanca-contratacao/addon/13-checklist-offboarding.md
  source_sha256: af3cfe45f4752aa63bf79f4271214deb7cfe0973a054f375e7c63355ae17b1e4
  source_commit: 036d74010f423f247be988e4a417375c74edb9d9
  target_sha256: b6b211abaec6da5d0a90413ad53deb416f62f09d724e3c8de933cfe75704a4b8
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 740bf440657434f2680e8b3e2e5b7f069a9b07bceba4d9fc3fab698ab88c4a2f
  glossary_keys: [cycle_iteration, framework_source_corpus, mirror_osf, practitioner_manual, role_tech_lead, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: 61461bcc9bf3491e7ba4723a058e2f416e19ce1a2ec6d9bee6926491062f1e7e
  translated_at: 2026-09-27T07:54:01Z
  stamped_at: 2026-09-27T07:54:01Z
  reviewed_by: null
---

# Secure Offboarding Checklist

**Version:** 1.0  
**Last update:** November 2025  
**Responsible:** HR (coordination) + DevOps (technical) + AppSec (validation) + Security Champion  
**Cycle:** from T-14 days before until T+1 day after the end

---

## 📖 Objective {#-objetivo}

Formalise and execute a **secure offboarding** process for:
- Contractors whose contract ends
- Critical suppliers that are terminated
- Team members (internal or external) who leave the organisation

**Benefit:** Complete revocation of access, recovery of assets, DORA/NIS2 compliance

---

## 🏃 Offboarding Timeline {#-timeline-de-offboarding}

```
T-14 dias: Notificação de término é conhecida
  └─ HR notifica Security Champion + DevOps + AppSec

T-10 dias: Preparação começa
  └─ Checklist de offboarding enviado a stakeholders

T-5 dias: Avisos iniciais
  └─ Notificação ao contractor/fornecedor (email + verbal)
  └─ Backup de trabalho iniciado

T-1 dia: Avisos finais
  └─ Last day confirmation email
  └─ Equipamentos recolhidos agendados

T+0 (Dia de Término):
  └─ Acesso revogado em T+0 (imediato após fim do expediente), com verificação até T+1
  └─ Assets finais recuperados

T+1 dia: Verificação
  └─ Sign-off de conclusão
  └─ Entrevista de saída (feedback)

T+7 dias: Auditoria
  └─ Revisão de logs (comportamento suspeito?)
  └─ Validação de limpeza
```

---

## 📋 PRE-OFFBOARDING (T-14 to T-1) {#-pré-offboarding-t-14-a-t-1}

### 1. Initial Notification and Planning {#1-notificação-inicial-e-planning}

| Item | Owner | Status | Date | Notes |
|------|-------|--------|------|-------|
| **HR notifies: CISO, Security Champion, Tech Lead, DevOps Lead, Manager** | HR | [ ] | ____ | Email with the end date |
| **Planning meeting 2 weeks before** | Security Champion | [ ] | ____ | Checklist sent, responsibilities assigned |
| **Notice to the contractor (if known in advance)** | Manager | [ ] | ____ | Verbal + written |
| **Document the reason for leaving** | HR | [ ] | ____ | Resignation, end of contract, termination, etc. |

---

### 2. Backup and Recovery of Work {#2-backup-e-recuperação-de-trabalho}

| Item | Owner | Executed | Verified | Notes |
|------|-------|-----------|-----------|-------|
| **Identify all the contractor's repositories/data** | Tech Lead | [ ] | [ ] | List Git repos, Jira boards, OneDrive shares |
| **Last commit identified** | DevOps | [ ] | [ ] | Date, SHA, content |
| **Full backup of private repositories** | DevOps | [ ] | [ ] | E.g.: `git clone --mirror` |
| **Backup of developed source code** | DevOps | [ ] | [ ] | Zip archive, versioned with a timestamp |
| **Backup of created documentation** | Tech Lead | [ ] | [ ] | Wikis, README, specs, design docs |
| **Backup of important communication** | HR | [ ] | [ ] | Critical emails, Slack messages (if compliance requires it) |
| **Archive in secure storage** | DevOps | [ ] | [ ] | Retention: 5 years (Policy 33 §8), restricted access |

**Storage:**
```
Location: /archive/offboarded/{contractor-name}/{date}/
├─ git-repos-backup.tar.gz
├─ code-artifacts/
├─ documentation/
└─ metadata.json (index, sizes, checksums)
```

---

### 3. Pre-Offboarding Notifications {#3-notificações-pré-offboarding}

| Communication | From | To | When | Content |
|-------------|----|----|--------|----------|
| **Offboarding Notice** | Security Champion | Contractor | T-7 days | Exact end date, list of what to hand over |
| **Equipment Return Notice** | HR | Contractor | T-5 days | When/where to return the laptop, mobile phone, badges, etc. |
| **Post-Termination Confidentiality Notice** | Legal | Contractor | T-1 day | Legal confidentiality obligations continue, duration, consequences |
| **Last Access Email** | Security Champion | Contractor + Manager | T-0 | Last day of access - final activities? |

---

## 🔐 OFFBOARDING EXECUTION (T+0 END DATE) {#-offboarding-execution-t0-data-de-término}

### 4. Revocation of Technical Access (on the same day as T+0) {#4-revogação-de-acesso-técnico-24h-após-t0}

**Timeline:** Start revocation between T+0 (end of the working day) and T+1 (morning)

#### 4.1 Git & CI/CD Access {#41-git--cicd-access}

| Item | Owner | Command/Action | Status | Verification |
|------|-------|------------|--------|-------------|
| **Remove the contractor from Github/GitLab orgs** | DevOps | `github:remove-member {org} {user}` | [ ] | Contractor cannot clone private repos |
| **Revoke SSH keys (all)** | DevOps | Delete from `~/.ssh/authorized_keys` and the Git platform | [ ] | SSH clone fails |
| **Revoke Personal Access Tokens (PATs)** | DevOps | Revoke via GitHub/GitLab settings | [ ] | API calls fail with 401 |
| **Revoke CI/CD credentials** | DevOps | Delete service account tokens | [ ] | CI/CD pipeline fails if the contractor tries to trigger it |
| **Remove collaborator permissions** | Tech Lead | Remove from all repositories | [ ] | No "edit" access visible |
| **Archive contractor repos (if personal)** | DevOps | `git archive` and move to `/archive` | [ ] | Repos marked as archived on platform |

**Verification:**
```bash
# Post-revocation check (5 min após revogação)
ssh -i /tmp/test-key git@github.com
# Expected: Permission denied (publickey)

git clone https://github.com/[org]/[private-repo]
# Expected: fatal: repository not found / access denied
```

---

#### 4.2 VPN, Wifi, Physical Access {#42-vpn-wifi-physical-access}

| Item | Owner | Action | Status | Verification |
|------|-------|------|--------|-------------|
| **Deactivate VPN account** | IT | Deactivate in VPN management console | [ ] | VPN login fails |
| **Revoke Wifi credentials** | IT | Remove MAC address / WiFi certificate | [ ] | Device cannot connect |
| **Deactivate badge/card access** | Facilities | Card deactivated in access control system | [ ] | Badge scan denied at doors |
| **Deactivate parking pass** | Facilities | Remove licence plate from parking system | [ ] | Cannot access parking |

---

#### 4.3 Cloud & SaaS Platforms {#43-cloud--saas-platforms}

| Platform | Item | Owner | Action | Status | Verification |
|-----------|------|-------|------|--------|-------------|
| **AWS** | IAM User | DevOps | Deactivate access key + delete user | [ ] | `aws s3 ls` fails (401) |
| **Azure** | Service Principal / User | DevOps | Delete or disable in Entra ID | [ ] | Cannot login to Azure portal |
| **Google Cloud** | Service Account | DevOps | Delete service account | [ ] | GCP API calls fail |
| **Jira** | User Account | Tech Lead | Deactivate user in directory | [ ] | Cannot login, all issues reassigned |
| **Confluence** | User Account | Tech Lead | Deactivate user | [ ] | Cannot access wikis |
| **Slack** | User Account | HR | Deactivate user | [ ] | Cannot login, marked as "inactive" |
| **Email** | Corporate Email | HR | Disable mailbox (may keep 30 days) | [ ] | OWA/IMAP login fails |

---

#### 4.4 Database & Data Store Access {#44-database--data-store-access}

| Item | Owner | Action | Status | Verification |
|------|-------|------|--------|-------------|
| **Revoke PostgreSQL roles** | DBA | `DROP ROLE contractor_name` | [ ] | psql connection rejected |
| **Revoke MySQL users** | DBA | `DROP USER 'contractor'@'%'` | [ ] | MySQL login fails |
| **Revoke MongoDB auth** | DBA | Remove user from database | [ ] | MongoDB auth fails |
| **Revoke S3/Storage access** | DevOps | Remove IAM policy, delete credentials | [ ] | AWS S3 upload/download fails |
| **Revoke Vault access** | DevOps | Remove AppRole, invalidate token | [ ] | Vault `auth` fails |

---

#### 4.5 MFA & Authentication {#45-mfa--authentication}

| Item | Owner | Action | Status | Verification |
|------|-------|------|--------|-------------|
| **Remove MFA device** | IT | Remove from Microsoft Authenticator / Authy | [ ] | Contractor cannot log in with MFA |
| **Revoke biometric access** | Facilities | Remove fingerprint from system | [ ] | Badge reader rejects biometric |
| **Revoke corporate device registration** | IT | Remove from MDM (Mobile Device Management) | [ ] | Device loses corporate mail, VPN |


#### 4.6 Integrations, Automation and Indirect Access {#46-integrações-automação-e-acessos-indiretos}

| Item | Owner | Action | Status | Verification |
|------|-------|------|--------|-------------|
| **Inventory the integrations associated with the user** | DevOps | List apps/integrations connected to Git, CI/CD, ChatOps, ALM | [ ] | List attached to the offboarding |
| **Revoke application and integration tokens** | DevOps | Revoke OAuth tokens, webhooks, installed apps, bots, runners | [ ] | Events/actions stop executing |
| **Revoke credentials in secrets managers and automation** | DevOps | Invalidate tokens/approles, remove bindings to pipelines | [ ] | Access fails / executions fail |
| **Remove synchronisation/export configurations** | IT/DevOps | Disable synchronisations, forwards, connections to external storage | [ ] | No export exists after T+0 |
| **Validate that there are no permissions inherited through groups** | IT/Tech Lead | Review indirect groups/roles in directories and platforms | [ ] | No residual access via a group |

---

### 5. Recovery of Physical Assets {#5-recuperação-de-ativos-físicos}

| Item | Collected By | Responsible | Status | Verification |
|------|---------------|-------------|--------|-------------|
| **Laptop/Desktop computer** | IT | Security Champion | [ ] | Device serial verified, collected in person |
| **Mobile phone (if corporate)** | IT | Security Champion | [ ] | Wiped on site (or scheduled) |
| **Badges/Cards** | Facilities | Security Champion | [ ] | Physically returned |
| **Keys (office, lab, locker)** | Facilities | Security Champion | [ ] | All accounted for |
| **Hardware tokens (security key, fob)** | IT | Security Champion | [ ] | Returned and destroyed |
| **External drives/USB sticks** | Tech Lead | Security Champion | [ ] | Scanned for unauthorised data |
| **Documents/printouts** | HR | Security Champion | [ ] | Collected, shredded or archived |
| **Other equipment** | HR | Security Champion | [ ] | Specify: _________________ |

**Procedure:**
```
1. Schedule collection meeting (T+0 or T+1)
2. Witness: Security Champion + HR + IT
3. Device powered off, inventory checked
4. Wiping scheduled (within 48h) or done on-site
5. Sign-off form completed
6. Evidence photographed/logged
```

---

### 6. Secrets & Credentials Rotation {#6-secrets--credentials-rotation}

| Item | Owner | Action | Status | Verification |
|------|-------|------|--------|-------------|
| **API keys contractor had access to** | AppSec | Revoke in platform, rotate secrets | [ ] | Old key returns 401 |
| **Database passwords** | DBA | Rotate in Vault + all apps updated | [ ] | Old password fails login |
| **JWT signing keys** | DevOps | Rotate if contractor had access | [ ] | Old tokens become invalid |
| **SSH host keys (if compromised risk)** | DevOps | Regenerate (e.g.: GitHub deploy keys) | [ ] | Old SSH key fails |
| **OAuth tokens** | DevOps | Revoke all tokens for contractor's app | [ ] | App reauthenticates |
| **Certificates/SSL keys** | DevOps | Rotate if contractor had access | [ ] | Old cert expires or revoked |

**Time limit:** all rotations on the same day for planned departures, within ≤ 2 h for unplanned departures and immediately for security reasons (the Manual's choice; Policy 33 §7).

---

## 📋 POST-OFFBOARDING (T+1 to T+7) {#-pós-offboarding-t1-a-t7}

### 7. Verification of Completion {#7-verificação-de-conclusão}

**T+1 (Day after the end):**

| Item | Owner | Verified | Observations |
|------|-------|-----------|-------------|
| **Confirmation: All access revoked** | DevOps | [ ] | Cross-check all platforms |
| **Confirmation: All devices recovered** | IT | [ ] | Serial numbers matched, wiping initiated |
| **Confirmation: Contractor cannot log in to any platform** | AppSec | [ ] | Login test (must fail) on 5 random platforms |
| **Data backup verified** | DevOps | [ ] | Archive integrity validated (checksums OK) |
| **Sign-off form signed** | Security Champion | [ ] | All parties have signed |

**Sign-Off Form Template:**

```
OFFBOARDING SIGN-OFF

Contractor: ________________
Data de Término: ________________
Data de Offboarding Completado: ________________

Confirmamos que o seguinte foi completado:
  ✓ Acesso técnico revogado (Git, Cloud, VPN, Email, Jira, Slack)
  ✓ Ativos físicos recuperados (laptop, badge, chaves)
  ✓ Secrets rotacionados (API keys, DB passwords, etc.)
  ✓ Backup de dados arquivado
  ✓ Confidentiality agreement assinado e reforçado
  ✓ Nenhum acesso residual identificado

Assinado por:
  - HR Manager: _________________ Data: _____
  - Security Champion: _________________ Data: _____
  - DevOps Lead: _________________ Data: _____
  - Tech Lead: _________________ Data: _____

Escalonamento (se necessário):
  Incidentes durante offboarding: [_______________]
  CISO Notificado? [ ] Sim [ ] Não
  Data: _____

Contacto para follow-up: _________________
```

---

### 8. Exit Interview (Feedback) {#8-entrevista-de-saída-feedback}

**T+1 or T+2, 1-1 with the contractor (optional but recommended)**

| Topic | Question | Answer | Actions |
|--------|---------|----------|-------|
| **Security** | How were the security policies? Clear? An impediment? | [_____] | [ ] Feedback for training |
| **Incidents** | Any security incident/error during the project? | [_____] | [ ] Incident ticket if so |
| **Access Control** | Was access appropriate? Did you have excessive permissions? | [_____] | [ ] Adjustment for the next one |
| **Tooling** | Were the security tools intuitive? | [_____] | [ ] Tool review if feedback is negative |
| **Training** | Was the onboarding training sufficient? | [_____] | [ ] Track iterated if there are gaps |
| **Recommendations** | Recommendations for improvement? | [_____] | [ ] Backlog item created |

**Result:** Scoring (1–5) aggregated into a "Contractor Security Rating" (see US-20)

---

### 9. Log Audit (T+3 to T+7) {#9-auditoria-de-logs-t3-a-t7}

**AppSec Engineer review:**

| Verification | Query | Expected result | Status |
|-------------|-------|-------------------|--------|
| **Last access to Git** | Git logs for the last 72h | No new commit/push | [ ] |
| **Last access to the VPN** | VPN logs for the last 72h | Access ended at T+0 | [ ] |
| **Last access to email** | Email logs for the last 72h | No login after T+0 | [ ] |
| **Last access to the cloud** | Cloud audit logs for the last 72h | No action after T+0 | [ ] |
| **Suspicious behaviour** | SIEM alerts for the last 7 days | No alert related to the contractor | [ ] |
| **Data exfiltration attempt** | DLP logs for the last 7 days | No upload/download attempt | [ ] |
| **Activity via integrations/bots** | Automation/ChatOps/GitHub Apps/CI logs | No execution associated with the user after T+0 | [ ] |

**If an anomaly is found:**
- [ ] Alert the CISO immediately
- [ ] Start an incident investigation
- [ ] Review residual access logs
- [ ] Escalation to Legal if necessary

---

## 📊 Artefacts & Documentation {#-artefactos--documentação}

**Keep for 5 years (Policy 33 §8):**

```
Archive Location: /compliance/offboarding/{contractor-name}/{date}/
├─ offboarding-checklist.pdf (signed)
├─ backup-manifest.json
│  ├─ repositories: [list]
│  ├─ artifacts: [list]
│  └─ timestamp, checksums
├─ device-inventory.pdf (with photos)
├─ secrets-rotation-log.txt
├─ access-revocation-log.txt
├─ audit-logs-excerpt.pdf (last 72h)
├─ exit-interview.pdf
└─ sign-off-form.pdf
```

---

## ⚠️ Red Flags & Escalation {#️-red-flags--escalation}

If any of the following occurs, **ESCALATE IMMEDIATELY**:

| Red Flag | Action | Owner |
|----------|------|-------|
| **Contractor tries to log in after T+0** | Escalate CISO, investigate login attempt | Security Monitoring |
| **Data missing from the backup** | Investigate theft/deletion, forensics | DevOps + CISO |
| **Secrets were not rotated in time** | Rotate NOW, investigate why | AppSec + DevOps |
| **"Missing" equipment** | Escalate HR + Legal, possibly theft | Facilities + HR |
| **Contractor has not returned equipment** | Legal letter, escalate to management | HR + Legal |
| **Suspicious behaviour in the logs** | Full forensics, preserve evidence | AppSec + CISO |
| **Contractor on a sanctions list (after leaving)** | Legal + CISO, compliance check | Compliance + Legal |

---

## 📎 Checklists by Type of Departure {#-checklists-por-tipo-de-saída}

### A. Immediate Termination (for Cause) {#a-rescisão-imediata-por-causa}

```
Diferença: Sem avisos, revogação no mesmo dia

[ ] Security incident confirmado
[ ] Violação de política de segurança
[ ] Roubo de ativos
[ ] Breach potencial
[ ] Comportamento malicioso confirmado

Ações especiais:
- [ ] Device wiped on-site (não permitir levar laptop)
- [ ] Backup forense realizado ANTES de wipe
- [ ] Legal notificado
- [ ] CISO escalação obrigatória
- [ ] Possível relato a authorities
```

### B. Amicable Termination (End of Contract) {#b-rescisão-amigável-fim-de-contrato}

```
Timeline: Planeado com 2 semanas de aviso

[ ] Backup de trabalho completo
[ ] Knowledge transfer realizado
[ ] Entrevista de saída feita
[ ] Referências para re-hire consideradas
[ ] Thank you email sent
```

### C. End of Contract by Expiry {#c-fim-de-contrato-por-expiração}

```
Automático após data pré-definida

[ ] Notificação automática em HR system
[ ] Offboarding inicia T-14 dias automaticamente
[ ] Extensão? Re-negotiate com Procurement
```

---

## 🏁 Success Criteria {#-success-criteria}

Offboarding is considered **COMPLETE** when:

- ✅ All technical access revoked (0 residual access)
- ✅ All physical assets recovered
- ✅ Secrets rotated
- ✅ Backup archived with confirmed integrity
- ✅ Sign-off form signed by 4+ parties
- ✅ Log audit shows no post-termination activity
- ✅ Confidentiality obligations reinforced
- ✅ Complete archive in compliance storage (5 years)

---

## 📎 References & Links {#-referências--links}

- [Technical Preparation - US-15](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-15---preparação-técnica-e-validação-de-contractors-pré-acesso)
- [Offboarding - US-17](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-17---offboarding-seguro-de-contractors-e-rescisão-de-fornecedores)
- [Post-Project Feedback - US-20](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-20---feedback-pós-projeto-e-rating-de-contractors)
- [Validation Template](./template-validacao-contractors)
- [Post-Termination Confidentiality Policy] (internal link)

---

**Ownership:** HR + DevOps + AppSec  
**Review:** Annual  
**Last update:** November 2025
