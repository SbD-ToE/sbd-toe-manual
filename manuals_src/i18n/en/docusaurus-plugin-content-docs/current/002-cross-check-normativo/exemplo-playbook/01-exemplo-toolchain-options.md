---
id: exemplo-toolchain-options
title: "Example: Toolchain Options"
description: Examples of how to implement toolchain principles with different tools
tags: [exemplos, toolchain, ferramentas, iac, logs, vulnerabilidades]
translation:
  source_locale: pt
  source_path: 002-cross-check-normativo/exemplo-playbook/01-exemplo-toolchain-options.md
  source_sha256: e5784daff3b113b2e2ec865b47e7cbae25f968d9e3b1a268b1eb17aa58d69400
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: a3de58e092b3f2da945b6fad3939da61cfef7f3a86857e96633c1b51f4d0bdb2
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: da8c4621ee3f200794cd49e34ddc29239ba89f55effb1e5e578d388e50580b8d
  glossary_keys: [audit_trail, chapter_role, como_fazer, maturity, practitioner_manual, sbdtoe_sbd, traceability, verification_taxonomy]
  glossary_sha256: f1b42be461b0db2d669344d17fa3508d62bc00daf66abd60d6d37783e014c61f
  translated_at: 2026-09-26T17:57:32Z
  reviewed_by: null
---

# Example: Toolchain Options

## Context {#enquadramento}

SbD-ToE prescribes ([Ch. 08](/sbd-toe/sbd-manual/iac-infraestrutura/intro), [Ch. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)):
- ✓ Infrastructure as Code (IaC)
- ✓ Centralised log collection
- ✓ Vulnerability analysis (SCA + SAST)
- ✓ Access auditing

SbD-ToE **does NOT prescribe** which tool to use. This document presents **examples of different stacks**.

---

## 1. Infrastructure as Code (IaC) {#1-infraestrutura-como-código-iac}

### Principle ([Ch. 08](/sbd-toe/sbd-manual/iac-infraestrutura/intro)) {#princípio-cap-08}
All infrastructure configuration must be versioned, audited and automated.

<details>
<summary><strong>🔧 Option A: Terraform + AWS</strong></summary>

```hcl
# main.tf
terraform {
  required_version = ">= 1.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

# Audit trail: Git commit logs, terraform state (com encryption em S3)
resource "aws_s3_bucket" "tf_state" {
  bucket = "company-terraform-state"
}

resource "aws_s3_bucket_versioning" "tf_state" {
  bucket = aws_s3_bucket.tf_state.id
  versioning_configuration {
    status = "Enabled"  # Audit trail via versioning
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "tf_state" {
  bucket = aws_s3_bucket.tf_state.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}
```

**Audit Evidence ([Ch. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)):**
- Git logs: `git log terraform/ --oneline --decorate`
- Terraform state history: S3 versioning
- Change approvals: GitHub branch protection + code review

</details>

---

<details>
<summary><strong>☁️ Option B: CloudFormation + AWS</strong></summary>

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: 'CloudFormation template com auditoria'

Parameters:
  Environment:
    Type: String
    Default: prod

Resources:
  VPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 10.0.0.0/16
      EnableDnsHostnames: true
      EnableDnsSupport: true
      Tags:
        - Key: Environment
          Value: !Ref Environment
        - Key: ManagedBy
          Value: CloudFormation

  # CloudTrail para auditoria
  CloudTrailRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Principal:
              Service: cloudtrail.amazonaws.com
            Action: sts:AssumeRole
```

**Audit Evidence:**
- CloudTrail logs: Who deployed, what, when
- Stack events: `aws cloudformation describe-stack-events`
- Change sets: Review before applying

</details>

---

<details>
<summary><strong>⎈ Option C: Helm + Kubernetes</strong></summary>

```yaml
# values.yaml
replicaCount: 3

image:
  repository: company/app
  tag: "1.2.3"
  pullPolicy: IfNotPresent

podSecurityContext:
  runAsNonRoot: true
  runAsUser: 1000
  fsGroup: 2000

securityContext:
  allowPrivilegeEscalation: false
  capabilities:
    drop:
      - ALL
  readOnlyRootFilesystem: true

# Audit logging
apiServer:
  auditLog:
    enabled: true
    maxAge: 30
    maxBackup: 10
    maxSize: 100
```

**Audit Evidence:**
- Helm release history: `helm history app-name`
- Git tags: `git tag -l v1.2.3`
- Kubernetes audit logs: Centralised in the SIEM

</details>

---

## 2. Centralised Log Collection {#2-recolha-centralizada-de-logs}

### Principle ([Ch. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)) {#princípio-cap-12}
Logs from all applications, infrastructure and access must be centralised, retained in line with policy, and protected against alteration.

<details>
<summary><strong>🔍 Option A: ELK Stack (Elasticsearch + Logstash + Kibana)</strong></summary>

```yaml
# logstash.conf
input {
  tcp {
    port => 5000
    codec => json
  }
  file {
    path => "/var/log/app/*.log"
    start_position => "beginning"
  }
}

filter {
  if [type] == "application" {
    mutate {
      add_field => { "[@metadata][index_name]" => "logs-app-%{+YYYY.MM.dd}" }
    }
    grok {
      match => { "message" => "%{TIMESTAMP_ISO8601:timestamp} %{LOGLEVEL:level} %{GREEDYDATA:msg}" }
    }
  }
}

output {
  elasticsearch {
    hosts => ["elasticsearch:9200"]
    index => "%{[@metadata][index_name]}"
    user => "${ES_USER}"
    password => "${ES_PASSWORD}"
    ssl => true
  }
}
```

**Audit Compliance ([Ch. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)):**
- Retention: Policy-based (e.g. 3 years critical, 1 year operational)
- Immutability: Elasticsearch read-only index after the period
- Alerts: Elasticsearch Watcher for anomalies

</details>

---

<details>
<summary><strong>📊 Option B: Datadog</strong></summary>

```python
# Python app
import logging
from datadog import initialize, statsd
from datadog_checks.base import AgentCheck

logger = logging.getLogger(__name__)

class SecurityAuditLogger:
    def __init__(self):
        self.dd_config = {
            'api_key': os.getenv('DD_API_KEY'),
            'app_key': os.getenv('DD_APP_KEY'),
        }
        initialize(**self.dd_config)
    
    def log_access(self, user, resource, action, status):
        """Log access event to Datadog"""
        event_data = {
            'title': f'Access: {action}',
            'text': f'User {user} attempted {action} on {resource}',
            'tags': ['audit', 'security', status],
            'priority': 'normal' if status == 'allowed' else 'high',
        }
        statsd.event('security.access', **event_data)
        logger.info(f"Logged: {action} by {user}")
```

**Audit Compliance:**
- Retention: Configurable (15 days to 15 months)
- Retention policy: API-driven
- Alerting: Query-based monitors

</details>

---

<details>
<summary><strong>☁️ Option C: Azure Sentinel</strong></summary>

```kusto
// KQL query para auditoria
SecurityEvent
| where TimeGenerated > ago(24h)
| where EventID in (4625, 4624)  // Falhas e sucessos login
| summarize FailureCount = countif(EventID == 4625), 
            SuccessCount = countif(EventID == 4624) by Account
| where FailureCount > 5
| project Account, FailureCount, SuccessCount
```

**Audit Compliance:**
- Retention: 90 days (free), up to 5 years (extended)
- Immutability: Logs protected via Azure RBAC
- Alerts: Automation rules + Playbooks

</details>

---

### 2.1. Application Integration: How to Push Logs {#21-integração-aplicacional-como-fazer-push-de-logs}

The options above show **where** to centralise logs. This section shows **how** applications send logs to those infrastructures.

<details>
<summary><strong>📘 .NET (ASP.NET Core) → Elasticsearch/Datadog</strong></summary>

**Option 1: Serilog + Elasticsearch**
```csharp
// Program.cs
using Serilog;
using Serilog.Sinks.Elasticsearch;

var builder = WebApplication.CreateBuilder(args);

// Configurar Serilog
Log.Logger = new LoggerConfiguration()
    .MinimumLevel.Information()
    .MinimumLevel.Override("Microsoft", LogEventLevel.Warning)
    .Enrich.FromLogContext()
    .Enrich.WithMachineName()
    .Enrich.WithEnvironmentName()
    .Enrich.WithProperty("Application", "MyApp")
    .WriteTo.Console()
    .WriteTo.Elasticsearch(new ElasticsearchSinkOptions(new Uri("https://elasticsearch:9200"))
    {
        AutoRegisterTemplate = true,
        IndexFormat = "logs-myapp-{0:yyyy.MM.dd}",
        ModifyConnectionSettings = conn => conn
            .BasicAuthentication("user", "password")
            .ServerCertificateValidationCallback((o, cert, chain, errors) => true), // Prod: validar cert!
        EmitEventFailure = EmitEventFailureHandling.WriteToSelfLog,
        FailureCallback = e => Console.WriteLine($"Unable to submit event {e.MessageTemplate}"),
    })
    .CreateLogger();

builder.Host.UseSerilog();

var app = builder.Build();

// Exemplo de logging estruturado
app.MapGet("/api/users/{id}", (int id, ILogger<Program> logger) =>
{
    logger.LogInformation("User access: {UserId} at {Timestamp}", id, DateTime.UtcNow);
    return Results.Ok(new { id, name = "User" });
});

app.Run();
```

**Option 2: Serilog + Datadog**
```csharp
// Program.cs
using Serilog;
using Serilog.Sinks.Datadog.Logs;

Log.Logger = new LoggerConfiguration()
    .WriteTo.DatadogLogs(
        apiKey: Environment.GetEnvironmentVariable("DD_API_KEY"),
        source: "csharp",
        service: "myapp",
        host: Environment.MachineName,
        tags: new[] { "env:prod", "version:1.0" }
    )
    .CreateLogger();
```

**NuGet Packages:**
```xml
<ItemGroup>
  <PackageReference Include="Serilog.AspNetCore" Version="8.0.0" />
  <PackageReference Include="Serilog.Sinks.Elasticsearch" Version="10.0.0" />
  <PackageReference Include="Serilog.Sinks.Datadog.Logs" Version="0.5.2" />
  <PackageReference Include="Serilog.Enrichers.Environment" Version="3.0.0" />
</ItemGroup>
```

</details>

---

<details>
<summary><strong>📗 Node.js (Express) → Elasticsearch/Datadog</strong></summary>

**Option 1: Winston + Elasticsearch**
```javascript
// logger.js
const winston = require('winston');
const { ElasticsearchTransport } = require('winston-elasticsearch');

const esTransportOpts = {
  level: 'info',
  clientOpts: {
    node: 'https://elasticsearch:9200',
    auth: {
      username: process.env.ES_USER,
      password: process.env.ES_PASSWORD,
    },
    tls: {
      rejectUnauthorized: true, // Prod: validar certificado
    },
  },
  index: 'logs-nodeapp',
  dataStream: true, // Usar data streams do ES 8+
};

const logger = winston.createLogger({
  level: 'info',
  format: winston.format.combine(
    winston.format.timestamp(),
    winston.format.errors({ stack: true }),
    winston.format.json()
  ),
  defaultMeta: { service: 'node-api', environment: process.env.NODE_ENV },
  transports: [
    new winston.transports.Console(),
    new ElasticsearchTransport(esTransportOpts),
  ],
});

module.exports = logger;

// app.js
const express = require('express');
const logger = require('./logger');

const app = express();

app.get('/api/users/:id', (req, res) => {
  logger.info('User access', { 
    userId: req.params.id, 
    ip: req.ip,
    userAgent: req.get('user-agent'),
  });
  res.json({ id: req.params.id, name: 'User' });
});

app.listen(3000, () => logger.info('Server started on port 3000'));
```

**Option 2: Winston + Datadog**
```javascript
const winston = require('winston');
const { createLogger } = require('datadog-winston');

const logger = createLogger({
  apiKey: process.env.DD_API_KEY,
  hostname: 'myapp-prod',
  service: 'node-api',
  ddsource: 'nodejs',
  ddtags: 'env:prod,version:1.0',
});

logger.info('Application started', { pid: process.pid });
```

**NPM Packages:**
```json
{
  "dependencies": {
    "winston": "^3.11.0",
    "winston-elasticsearch": "^0.17.4",
    "datadog-winston": "^2.0.0"
  }
}
```

</details>

---

<details>
<summary><strong>🐍 Python (FastAPI/Django) → Elasticsearch/Datadog</strong></summary>

**Option 1: Python logging + Elasticsearch**
```python
# logging_config.py
import logging
from cmreslogging.handlers import CMRESHandler

def setup_elasticsearch_logging():
    """Configura logging para Elasticsearch"""
    
    handler = CMRESHandler(
        hosts=[{'host': 'elasticsearch', 'port': 9200}],
        auth_type=CMRESHandler.AuthType.BASIC_AUTH,
        auth_details=('user', 'password'),
        es_index_name='logs-python-app',
        use_ssl=True,
        verify_ssl=True,
        es_additional_fields={
            'app': 'python-api',
            'environment': 'production'
        }
    )
    
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)
    
    # Também log para console
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    ))
    logger.addHandler(console_handler)
    
    return logger

# main.py (FastAPI)
from fastapi import FastAPI
from logging_config import setup_elasticsearch_logging

logger = setup_elasticsearch_logging()
app = FastAPI()

@app.get("/api/users/{user_id}")
async def get_user(user_id: int):
    logger.info(
        "User access",
        extra={
            'user_id': user_id,
            'endpoint': '/api/users',
            'action': 'read'
        }
    )
    return {"id": user_id, "name": "User"}
```

**Option 2: Python + Datadog**
```python
from ddtrace import tracer
from ddtrace.contrib.logging import patch as ddtrace_patch_logging
import logging

# Patch logging para adicionar trace context
ddtrace_patch_logging()

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s [dd.service=%(dd.service)s dd.trace_id=%(dd.trace_id)s] %(message)s'
)

logger = logging.getLogger(__name__)

# FastAPI com Datadog APM
from fastapi import FastAPI
from ddtrace.contrib.asgi import TraceMiddleware

app = FastAPI()
app.add_middleware(TraceMiddleware, service="python-api")

@app.get("/api/users/{user_id}")
async def get_user(user_id: int):
    logger.info(f"User access: {user_id}")
    return {"id": user_id}
```

**PIP Requirements:**
```txt
CMRESHandler==1.0.0
python-elasticsearch==8.11.0
ddtrace==2.3.0
```

</details>

---

<details>
<summary><strong>☕ Java (Spring Boot) → Elasticsearch/Datadog</strong></summary>

**Option 1: Logback + Elasticsearch (via Logstash)**
```xml
<!-- logback-spring.xml -->
<configuration>
    <appender name="LOGSTASH" class="net.logstash.logback.appender.LogstashTcpSocketAppender">
        <destination>logstash:5000</destination>
        
        <encoder class="net.logstash.logback.encoder.LogstashEncoder">
            <customFields>{"app":"spring-api","env":"prod"}</customFields>
        </encoder>
        
        <keepAliveDuration>5 minutes</keepAliveDuration>
        <reconnectionDelay>10 seconds</reconnectionDelay>
    </appender>
    
    <appender name="CONSOLE" class="ch.qos.logback.core.ConsoleAppender">
        <encoder>
            <pattern>%d{HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n</pattern>
        </encoder>
    </appender>
    
    <root level="INFO">
        <appender-ref ref="LOGSTASH" />
        <appender-ref ref="CONSOLE" />
    </root>
</configuration>
```

```java
// UserController.java
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/users")
public class UserController {
    private static final Logger logger = LoggerFactory.getLogger(UserController.class);
    
    @GetMapping("/{id}")
    public User getUser(@PathVariable Long id) {
        logger.info("User access: userId={}, action=read", id);
        return new User(id, "User Name");
    }
}
```

**Option 2: Spring Boot + Datadog**
```yaml
# application.yml
management:
  metrics:
    export:
      datadog:
        enabled: true
        api-key: ${DD_API_KEY}
        application-key: ${DD_APP_KEY}
        step: 1m
        
logging:
  pattern:
    console: "%d{yyyy-MM-dd HH:mm:ss} - %msg%n"
  level:
    root: INFO
    com.example: DEBUG
```

**Maven Dependencies:**
```xml
<dependencies>
    <dependency>
        <groupId>net.logstash.logback</groupId>
        <artifactId>logstash-logback-encoder</artifactId>
        <version>7.4</version>
    </dependency>
    <dependency>
        <groupId>io.micrometer</groupId>
        <artifactId>micrometer-registry-datadog</artifactId>
    </dependency>
</dependencies>
```

</details>

---

### SbD-ToE Compliance ([Ch. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)) {#conformidade-sbd-toe-cap-12}

All the examples above ensure:

✅ **Structured logging** (JSON) - makes queries and alerts easier  
✅ **Enriched context** - app, environment, trace IDs, user IDs  
✅ **Automatic push** - logs sent in real time (async)  
✅ **Resilience** - local buffering if the infrastructure is unavailable  
✅ **Security** - TLS, authentication, no sensitive data in logs  

**Audit Evidence:**
- Logs with UTC timestamp, user/session IDs, action performed
- Correlation with traces (Datadog APM, Elasticsearch APM)
- Retention policy configured (3+ years for L3)

---

## 3. Vulnerability Analysis (SCA + SAST) {#3-análise-de-vulnerabilidades-sca--sast}

### Principle ([Ch. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro), [Ch. 07](/sbd-toe/sbd-manual/cicd-seguro/intro)) {#princípio-cap-05-cap-07}
Dependencies and code must be analysed for known vulnerabilities, integrated into CI/CD.

<details>
<summary><strong>🛡️ Option A: SCA + SAST with Snyk + SonarQube</strong></summary>

```yaml
# .github/workflows/security.yml
name: Security Analysis

on: [push, pull_request]

jobs:
  sca:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Run Snyk SCA
        run: |
          npm install -g snyk
          snyk auth ${{ secrets.SNYK_TOKEN }}
          snyk test --severity-threshold=high
        continue-on-error: false  # Falha se HIGH ou CRITICAL
      
      - name: Run SonarQube SAST
        run: |
          docker run --rm \
            -e SONAR_HOST_URL=${{ secrets.SONAR_URL }} \
            -e SONAR_LOGIN=${{ secrets.SONAR_TOKEN }} \
            -v "$PWD:/src" \
            sonarsource/sonar-scanner-cli
```

**[Ch. 07](/sbd-toe/sbd-manual/cicd-seguro/intro) Compliance:**
- Security gate: Blocks the merge if HIGH+
- Reporting: SBOM generated (`snyk sbom --format=cyclonedx`)
- Trail: Logs preserved in CI/CD

---

### Option B: WhiteSource + Custom SAST {#opção-b-whitesource--custom-sast}
```python
# scan.py (SAST custom)
import ast
import re

class SecurityScan:
    def __init__(self, filepath):
        self.filepath = filepath
        self.vulnerabilities = []
    
    def scan_hardcoded_secrets(self):
        """Procura por secrets hardcoded"""
        with open(self.filepath, 'r') as f:
            content = f.read()
        
        patterns = [
            r'password\s*=\s*["\']([a-zA-Z0-9]+)["\']',
            r'api_key\s*=\s*["\']sk_[a-zA-Z0-9]{20,}["\']',
            r'AWS_SECRET_ACCESS_KEY\s*=\s*["\'].*["\']',
        ]
        
        for pattern in patterns:
            matches = re.finditer(pattern, content)
            for match in matches:
                self.vulnerabilities.append({
                    'type': 'Hardcoded Secret',
                    'line': content[:match.start()].count('\n') + 1,
                    'severity': 'CRITICAL',
                })
    
    def report(self):
        return {
            'file': self.filepath,
            'vulnerabilities': self.vulnerabilities,
            'status': 'PASS' if len(self.vulnerabilities) == 0 else 'FAIL'
        }
```

**[Ch. 07](/sbd-toe/sbd-manual/cicd-seguro/intro) Compliance:**
- Gate: Rejects if CRITICAL secrets are found
- Trail: Report saved as a CI/CD artefact

</details>

---

<details>
<summary><strong>🔒 Option B: Dependency Check (Open Source)</strong></summary>

```bash
#!/bin/bash
# scan-dependencies.sh

# Análise de dependências
java -jar dependency-check/bin/dependency-check.jar \
  --scan . \
  --format JSON \
  --out ./odc-reports \
  --project "MyApp" \
  --failOnCVSS 7.0  # Falha se score >= 7.0

# Integração CI/CD
if [ $? -ne 0 ]; then
  echo "Vulnerabilities found with CVSS >= 7.0"
  exit 1
fi
```

**[Ch. 07](/sbd-toe/sbd-manual/cicd-seguro/intro) Compliance:**
- Free and open source
- Integrated security gate
- Report in multiple formats

</details>

---

## 4. CI/CD with Security Gates {#4-cicd-com-gates-de-segurança}

### Principle ([Ch. 07](/sbd-toe/sbd-manual/cicd-seguro/intro)) {#princípio-cap-07}
The pipeline must include security validations, formal approvals and a complete audit trail.

<details>
<summary><strong>🔄 Option A: GitHub Actions</strong></summary>

```yaml
name: Deploy with Security Gates

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  security-gates:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: SAST Analysis
        run: npm run lint:security
        
      - name: SCA Analysis
        run: npm run audit --production
      
      - name: Secrets Scan
        uses: trufflesecurity/trufflehog@main
        with:
          path: ./
          base: ${{ github.event.repository.default_branch }}
          head: HEAD
      
      - name: Build Artifact
        run: npm run build
      
      - name: Sign Artifact
        run: cosign sign-blob --key cosign.key ./dist/app.tar.gz > app.tar.gz.sig
      
      - name: Upload to Registry
        run: |
          echo "${{ secrets.REGISTRY_PASSWORD }}" | docker login -u "${{ secrets.REGISTRY_USER }}" --password-stdin
          docker push myregistry/app:${{ github.sha }}
```

**Audit Trail ([Ch. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)):**
```
Workflow logs (7 anos retention)
├── SAST: SonarQube scan results
├── SCA: Dependency check report
├── Secrets: Trufflehog findings
├── Build: Artifact fingerprint
├── Sign: Signature verification
└── Push: Registry audit logs
```

</details>

---

<details>
<summary><strong>⚙️ Option B: GitLab CI</strong></summary>

```yaml
stages:
  - security
  - build
  - deploy

sast:
  stage: security
  image: sast-scanner:latest
  script:
    - sast-scan . --format json --output sast-report.json
  artifacts:
    reports:
      sast: sast-report.json
  allow_failure: false

sca:
  stage: security
  script:
    - sca-scan . --fail-on-high
  allow_failure: false

secrets:
  stage: security
  script:
    - detect-secrets scan . --baseline .secrets.baseline
  allow_failure: false

build:
  stage: build
  script:
    - docker build -t $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA .
    - docker push $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA
  dependencies:
    - sast
    - sca
    - secrets

approval:
  stage: deploy
  script:
    - echo "Manual approval required for production"
  when: manual
  only:
    - main

deploy:
  stage: deploy
  script:
    - helm upgrade --install app ./chart
  environment:
    name: production
  when: on_success
  only:
    - main
```

**Segregation of Duties ([Ch. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro)):**
- SAST/SCA: Automatic
- Secrets: Automatic
- Approval: Manual (via UI)
- Deploy: Via RBAC

</details>

---

## 5. Integrated Platforms (All-in-One ASPM) {#5-plataformas-integradas-all-in-one-aspm}

### Principle (Multi-chapter) {#princípio-multi-capítulo}
A unified platform can cover multiple security areas with data correlation and centralised dashboards.

### When to Consider Integrated Platforms? {#quando-considerar-plataformas-integradas}

**✅ Advantages:**
- Single dashboard for multiple security areas
- Automatic correlation between vulnerabilities (SCA + SAST + IaC)
- Lower integration effort
- Unified policy management
- Single source of truth for compliance

**⚠️ Challenges:**
- Vendor lock-in
- Typically higher cost
- Less specialisation per area vs. best-of-breed tools
- Dependence on the vendor's roadmap

---

<details>
<summary><strong>🔐 Option A: Xygeni (ASPM - Application Security Posture Management)</strong></summary>

**SbD-ToE Coverage:**

| Xygeni Capability | SbD-ToE Chapter | Description |
|-------------------|------------------|-----------|
| **SCA** | [Ch. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro) | Dependency analysis, automatic SBOM, malware detection in packages |
| **SAST** | [Ch. 06](/sbd-toe/sbd-manual/desenvolvimento-seguro/intro) | Code security analysis, detection of vulnerabilities in code |
| **Secrets Security** | [Ch. 06](/sbd-toe/sbd-manual/desenvolvimento-seguro/intro) + [Ch. 07](/sbd-toe/sbd-manual/cicd-seguro/intro) | Detection of hardcoded secrets, exposed tokens |
| **CI/CD Security** | [Ch. 07](/sbd-toe/sbd-manual/cicd-seguro/intro) | Pipeline security analysis, detection of insecure configurations |
| **IaC Security** | [Ch. 08](/sbd-toe/sbd-manual/iac-infraestrutura/intro) | Scanning of Terraform/CloudFormation/Helm for misconfigurations |
| **Build Security** | [Ch. 07](/sbd-toe/sbd-manual/cicd-seguro/intro) | Build integrity verification, supply chain attacks |
| **Anomaly Detection** | [Ch. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro) | Detection of anomalous behaviour at runtime |
| **ASPM Dashboard** | [Ch. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro) | Unified view of security posture, consolidated KPIs |

**Configuration Example:**

```yaml
# xygeni.yml
project:
  name: "my-secure-app"
  owner: "security-team"

scans:
  sca:
    enabled: true
    fail_on: critical
    sbom:
      format: cyclonedx
      output: sbom.json
  
  sast:
    enabled: true
    languages: [java, python, javascript]
    exclude_paths: [test/*, vendor/*]
  
  secrets:
    enabled: true
    max_depth: 50  # commits
    exclude_patterns:
      - "*.test.js"
      - "mock-data/*"
  
  iac:
    enabled: true
    providers: [aws, azure, kubernetes]
    severity_threshold: medium
  
  cicd:
    enabled: true
    platforms: [github-actions, gitlab-ci]

policies:
  block_critical: true
  require_review_high: true
  auto_create_tickets: true

integrations:
  jira:
    project_key: SEC
    auto_assign: true
  
  slack:
    channel: "#security-alerts"
    notify_on: [critical, high]
```

**Audit Evidence:**
- Central dashboard: Complete scan history
- Consolidated reports: PDF/JSON exportable for compliance
- Traceability: Commit → Scan → Issue → Resolution
- Compliance mappings: NIS2, DORA, CRA, GDPR built in


</details>

---

<details>
<summary><strong>🐍 Option B: Snyk Enterprise (Platform Approach)</strong></summary>

**SbD-ToE Coverage:**

```yaml
# .snyk policy file
version: v1.25.0

# SCA - Cap. 05
ignore:
  - "SNYK-JS-LODASH-590103":
      reason: "False positive - não usamos merge profundo"
      expires: "2025-12-31"

# SAST - Cap. 06
code:
  severity-threshold: high
  
# IaC - Cap. 08
infrastructure-as-code:
  providers: [terraform, kubernetes]
  severity-threshold: medium

# Container - Cap. 09
container:
  base-image-severity: critical
  
patch:
  auto-apply: true
  exclude:
    - "**/test/**"
```

**CI/CD Integration ([Ch. 07](/sbd-toe/sbd-manual/cicd-seguro/intro)):**

```yaml
# .github/workflows/snyk-security.yml
name: Snyk Security Platform

on: [push, pull_request]

jobs:
  snyk-all-in-one:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Run Snyk to check for vulnerabilities
        uses: snyk/actions@master
        env:
          SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}
        with:
          command: test
          args: >
            --all-projects
            --severity-threshold=high
            --sarif-file-output=snyk.sarif
      
      - name: Snyk IaC
        uses: snyk/actions/iac@master
        env:
          SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}
      
      - name: Snyk Container
        uses: snyk/actions/docker@master
        env:
          SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}
        with:
          image: myapp:${{ github.sha }}
      
      - name: Snyk Code (SAST)
        uses: snyk/actions/code@master
        env:
          SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}
      
      - name: Upload to GitHub Security
        uses: github/codeql-action/upload-sarif@v2
        with:
          sarif_file: snyk.sarif
```

</details>

---

<details>
<summary><strong>✅ Option C: Checkmarx One (Unified Platform)</strong></summary>

**Multi-Chapter Coverage:**

```xml
<!-- checkmarx-config.xml -->
<CheckmarxOne>
  <!-- SAST - Cap. 06 -->
  <SAST>
    <PresetName>High Security</PresetName>
    <ExcludeFolders>test,vendor</ExcludeFolders>
    <FailOnSeverity>High</FailOnSeverity>
  </SAST>
  
  <!-- SCA - Cap. 05 -->
  <SCA>
    <RiskThreshold>7.0</RiskThreshold>
    <GenerateSBOM>true</GenerateSBOM>
    <SBOMFormat>CycloneDX</SBOMFormat>
  </SCA>
  
  <!-- IaC - Cap. 08 -->
  <KICS>
    <Platforms>Terraform,Kubernetes,Helm</Platforms>
    <Severity>MEDIUM</Severity>
  </KICS>
  
  <!-- Supply Chain - Cap. 05 + 07 -->
  <SupplyChain>
    <ScanDependencies>true</ScanDependencies>
    <MalwareDetection>true</MalwareDetection>
  </SupplyChain>
  
  <!-- API Security - Cap. 04 -->
  <APITesting>
    <Enabled>true</Enabled>
    <SwaggerPath>./docs/api.yaml</SwaggerPath>
  </APITesting>
</CheckmarxOne>
```

---

### Comparison: Integrated Platform vs. Best-of-Breed {#comparação-plataforma-integrada-vs-best-of-breed}

| Criterion | Integrated Platform<br/>(Xygeni, Snyk, Checkmarx) | Best-of-Breed<br/>(Specialised tools) |
|----------|--------------------------------------|----------------------------------------|
| **Integration** | ✅ Plug-and-play, single dashboard | ⚠️ Requires manual integration |
| **Correlation** | ✅ Automatic between vulnerabilities | ⚠️ Manual or via SIEM/SOAR |
| **Specialisation** | ⚠️ Good but not the leader in every area | ✅ Leader in a specific area |
| **Cost** | ⚠️ Typically higher | ✅ Pay-per-tool, more flexible |
| **Vendor Lock-in** | ⚠️ High | ✅ Low |
| **Compliance** | ✅ Built-in mappings (NIS2, DORA) | ⚠️ Requires manual work |
| **Time-to-Value** | ✅ Fast (weeks) | ⚠️ Medium (months) |
| **Customisation** | ⚠️ Limited to the platform's features | ✅ Full control |
| **In-house Expertise** | ✅ Less required | ⚠️ More required |

---

### Recommendations by Context {#recomendações-por-contexto}

**Use an Integrated Platform when:**
- ✅ Small/medium team without deep expertise in each area
- ✅ Need for rapid compliance (NIS2, DORA, CRA)
- ✅ Budget allows a higher initial investment
- ✅ Preference for operational simplicity
- ✅ Need for a unified executive dashboard

**Use Best-of-Breed when:**
- ✅ Large team with specialists per area
- ✅ Very specific requirements (e.g. analysis of a rare language)
- ✅ Limited budget or pay-as-you-grow
- ✅ Complex/heterogeneous technology stack
- ✅ Priority on avoiding vendor lock-in

**Hybrid Approach (Recommended in many cases):**
```
Plataforma Integrada (core) + Best-of-Breed (especializado)

Exemplo:
- Xygeni/Snyk: SCA, SAST, IaC (cobertura base)
+ Semgrep: SAST avançado com regras custom
+ Trivy: Container scanning especializado
+ Wiz: Cloud security posture
```

</details>

---

## Summary {#síntese}

| Dimension | Principle (SbD-ToE) | Option A | Option B | Option C | Option D (Integrated) |
|----------|---|---|---|---|---|
| **IaC** | [Ch. 08](/sbd-toe/sbd-manual/iac-infraestrutura/intro) | Terraform | CloudFormation | Helm | Xygeni IaC / Snyk IaC |
| **Logs** | [Ch. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro) | ELK | Datadog | Azure Sentinel | Xygeni Anomaly Detection |
| **SCA** | [Ch. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro) | Snyk | WhiteSource | Dep-Check | Xygeni SCA / Snyk SCA |
| **SAST** | [Ch. 06](/sbd-toe/sbd-manual/desenvolvimento-seguro/intro) | SonarQube | Custom | TruffleHog | Xygeni SAST / Checkmarx |
| **Secrets** | [Ch. 06](/sbd-toe/sbd-manual/desenvolvimento-seguro/intro) | TruffleHog | detect-secrets | GitGuardian | Xygeni Secrets / Snyk |
| **CI/CD Security** | [Ch. 07](/sbd-toe/sbd-manual/cicd-seguro/intro) | GitHub Actions | GitLab CI | Jenkins | Xygeni CI/CD Security |
| **Container** | [Ch. 09](/sbd-toe/sbd-manual/containers-imagens/intro) | Trivy | Clair | Grype | Snyk Container / Xygeni |
| **ASPM/Dashboard** | [Ch. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro) | Custom | - | - | Xygeni / Checkmarx One |

**No combination is "correct"** - each organisation chooses according to:
- Existing architecture and technology stack
- Expertise available in the team
- Budget and licensing model
- Local compliance (NIS2, DORA, CRA, GDPR)
- Preference for simplicity vs. specialisation

---

## Next Steps {#próximas-etapas}

1. **Assess the organisational context:**
   - Which technology stack already exists?
   - What is the maturity of the security team?
   - Integrated platform or best-of-breed?

2. **Define the strategy:**
   - **All-in-One:** Xygeni, Snyk Enterprise, Checkmarx One
   - **Best-of-Breed:** Specialised tools per area
   - **Hybrid:** Base platform + specialised tools

3. **Pilot:** 
   - Implement one option in a pilot project
   - Compare time-to-value vs. depth of analysis

4. **Validate:** 
   - Test the security gates
   - Validate the audit trail
   - Measure scalability and false-positive rate

5. **Iterate:** 
   - Adjust according to lessons learned
   - Assess ROI (Return on Investment)
   - Consider a hybrid approach if necessary

6. **Document:** 
   - Update internal policies with the chosen stack
   - Train teams on the selected tools
   - Establish remediation SLAs

---

**Version:** 1.0  
**Date:** November 2025  
**Feedback:** Adapt in line with technological evolution
