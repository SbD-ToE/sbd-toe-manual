# 25. Rastreabilidade — Testes de Segurança

## Sumário

Este capítulo trata de **testes de segurança e validação empírica** —
estratégia de testes, execução, gestão de findings, rastreabilidade de
correções. As fontes externas seguintes contribuem para esta área:

- **NIST SP 800-53 Rev. 5** — 50 referência(s)
- **OWASP DSOMM** — 39 referência(s)
- **MITRE ATLAS — Adversarial Threat Landscape for AI Systems** — 16 referência(s)
- **NIST AI 100-2 e2025 — Adversarial Machine Learning Taxonomy** — 15 referência(s)
- **OWASP SAMM v2.1** — 14 referência(s)
- **PCI DSS v4.0.1** — 13 referência(s)
- **MITRE CAPEC v3.9** — 9 referência(s)
- **CIS Controls v8.1.2** — 9 referência(s)
- **SAFECode — Practical Security Stories and Tasks for Agile Development (2012)** — 7 referência(s)
- **NIST SSDF (SP 800-218 v1.1)** — 5 referência(s)
- **NIST AI RMF 1.0** — 4 referência(s)
- **PCI Secure SLC v1.1** — 3 referência(s)
- **SAFECode — Fundamental Practices for Secure Software Development (2018)** — 2 referência(s)
- **MITRE CWE — Software Development View (v4.19.1)** — 1 referência(s)
- **HIPAA Security Rule** — 1 referência(s)
- **OWASP MCP — Secure Server Development v1.0** — 1 referência(s)
- **OWASP Machine Learning Top 10** — 1 referência(s)
- **SAFECode — Software Integrity Controls (2010)** — 1 referência(s)
- **SLSA Specification v1.0 — Build Track** — 1 referência(s)

---

## NIST SP 800-53 Rev. 5

**O que esta ES traz para este capítulo:** contribui 50 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `SP800-53-CA-2` | Control Assessments. Select the appropriate assessor or assessment team for the type of assessment to be conducted; Develop a control assessment plan that describes the scope of the assessment includi | conceito: Risk-Based Security Test Planning (practice `ACP-TSV-001`) |
| `SP800-53-CA-4` | Security Certification | conceito: Reproducible Test Evidence Management (practice `ACP-TSV-004`) |
| `SP800-53-CA-5` | Plan of Action and Milestones. Develop a plan of action and milestones for the system to document the planned remediation actions of the organization to correct weaknesses or deficiencies noted during | conceito: Findings Triage, SLA And Retest Closure (practice `ACP-TSV-003`) |
| `SP800-53-CA-8` | Penetration Testing. Conduct penetration testing [frequency] on [system(s) or system components]. | conceito: Specialized Empirical Testing (practice `ACP-TSV-006`) |
| `SP800-53-CA-8.2` | Red Team Exercises. Employ the following red-team exercises to simulate attempts by adversaries to compromise organizational systems in accordance with applicable rules of engagement: [red team exerci | conceito: Specialized Empirical Testing (practice `ACP-TSV-006`) |
| `SP800-53-CM-4.1` | Separate Test Environments. Analyze changes to the system in a separate test environment before implementation in an operational environment, looking for security and privacy impacts due to flaws, wea | conceito: Staged Dynamic Testing And Gate Enforcement (practice `ACP-TSV-005`) |
| `SP800-53-CP-1` | Policy and Procedures. Develop, document, and disseminate to [organization-defined personnel or roles]: contingency planning policy that: Addresses purpose, scope, roles, responsibilities, management | conceito: Identidade, autenticação e gestão de sessões (slice `ACO-IAT`) |
| `SP800-53-CP-10.1` | Contingency Plan Testing | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `SP800-53-CP-4` | Contingency Plan Testing. Test the contingency plan for the system [frequency] using the following tests to determine the effectiveness of the plan and the readiness to execute the plan: [organization | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `SP800-53-CP-4.1` | Coordinate with Related Plans. Coordinate contingency plan testing with organizational elements responsible for related plans. | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `SP800-53-CP-4.3` | Automated Testing. Test the contingency plan using [automated mechanisms]. | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `SP800-53-CP-7.5` | Equivalent Information Security Safeguards | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `SP800-53-CP-8.5` | Alternate Telecommunication Service Testing. Test alternate telecommunication services [frequency]. | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `SP800-53-CP-9.1` | Testing for Reliability and Integrity. Test backup information [organization-defined frequency] to verify media reliability and information integrity. | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `SP800-53-IR-1` | Policy and Procedures. Develop, document, and disseminate to [organization-defined personnel or roles]: incident response policy that: Addresses purpose, scope, roles, responsibilities, management com | conceito: Identidade, autenticação e gestão de sessões (slice `ACO-IAT`) |
| `SP800-53-IR-3.2` | Coordination with Related Plans. Coordinate incident response testing with organizational elements responsible for related plans. | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `SP800-53-IR-3.3` | Continuous Improvement. Use qualitative and quantitative data from testing to: Determine the effectiveness of incident response processes; Continuously improve incident response processes; and Provide | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `SP800-53-IR-4.1` | Automated Incident Handling Processes. Support the incident handling process using [automated mechanisms]. | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `SP800-53-IR-5.1` | Track incidents | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `SP800-53-IR-6.1` | Automated Reporting. Report incidents using [automated mechanisms]. | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `SP800-53-IR-8.1` | Breaches. Include the following in the Incident Response Plan for breaches involving personally identifiable information: A process to determine if notice to individuals or other organizations, includ | conceito: Gestão de segredos, configuração protegida e identidades operacionais (slice `ACO-SPC`) |
| `SP800-53-MP-6.2` | Equipment Testing. Test sanitization equipment and procedures [organization-defined frequency] to ensure that the intended sanitization is being achieved. | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `SP800-53-MP-8.2` | Equipment Testing. Test downgrading equipment and procedures [organization-defined frequency] to ensure that downgrading actions are being achieved. | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `SP800-53-PE-13.4` | Inspections. Ensure that the facility undergoes [frequency] fire protection inspections by authorized and qualified inspectors and identified deficiencies are resolved within [time period]. | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `SP800-53-PE-3.6` | Facility Penetration Testing | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `SP800-53-PL-6` | Security-related Activity Planning | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `SP800-53-PM-14` | Testing, Training, and Monitoring. Implement a process for ensuring that organizational plans for conducting security and privacy testing, training, and monitoring activities associated with organizat | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `SP800-53-PM-9` | Risk Management Strategy. Develops a comprehensive strategy to manage: Security risk to organizational operations and assets, individuals, other organizations, and the Nation associated with the opera | conceito: Identidade, autenticação e gestão de sessões (slice `ACO-IAT`) |
| `SP800-53-RA-5.10` | Correlate Scanning Information. Correlate the output from vulnerability scanning tools to determine the presence of multi-vulnerability and multi-hop attack vectors. | conceito: Staged Dynamic Testing And Gate Enforcement (practice `ACP-TSV-005`) |
| `SP800-53-RA-5.3` | Breadth and Depth of Coverage. Define the breadth and depth of vulnerability scanning coverage. | conceito: Staged Dynamic Testing And Gate Enforcement (practice `ACP-TSV-005`) |
| `SP800-53-RA-5.6` | Automated Trend Analyses. Compare the results of multiple vulnerability scans using [automated mechanisms]. | conceito: Staged Dynamic Testing And Gate Enforcement (practice `ACP-TSV-005`) |
| `SP800-53-RA-5.9` | Penetration Testing and Analyses | conceito: Staged Dynamic Testing And Gate Enforcement (practice `ACP-TSV-005`) |
| `SP800-53-SA-10.4` | Trusted Generation. Require the developer of the system, system component, or system service to employ tools for comparing newly generated versions of security-relevant hardware descriptions, source c | conceito: Pipeline Definition As Reviewed Code (practice `ACP-SCBI-004`) |
| `SP800-53-SA-11` | Developer Testing and Evaluation. Require the developer of the system, system component, or system service, at all post-design stages of the system development life cycle, to: Develop and implement a | conceito: Governed Static Analysis Execution (practice `ACP-TSV-002`) |
| `SP800-53-SA-11.1` | Static Code Analysis. Require the developer of the system, system component, or system service to employ static code analysis tools to identify common flaws and document the results of the analysis. | conceito: Governed Static Analysis Execution (practice `ACP-TSV-002`) |
| `SP800-53-SA-11.7` | Verify Scope of Testing and Evaluation. Require the developer of the system, system component, or system service to verify that the scope of testing and evaluation provides complete coverage of the re | conceito: Governed Static Analysis Execution (practice `ACP-TSV-002`) |
| `SP800-53-SA-11.8` | Dynamic Code Analysis. Require the developer of the system, system component, or system service to employ dynamic code analysis tools to identify common flaws and document the results of the analysis. | conceito: Governed Static Analysis Execution (practice `ACP-TSV-002`) |
| `SP800-53-SA-12.7` | Assessments Prior to Selection / Acceptance / Update | conceito: Automated Dependency And Image Risk Gating (practice `ACP-SCBI-002`) |
| `SP800-53-SA-15.10` | Incident Response Plan. Require the developer of the system, system component, or system service to provide, implement, and test an incident response plan. | conceito: Pipeline Definition As Reviewed Code (practice `ACP-SCBI-004`) |
| `SP800-53-SA-15.7` | Automated Vulnerability Analysis. Require the developer of the system, system component, or system service [frequency] to: Perform an automated vulnerability analysis using [tools]; Determine the expl | conceito: Pipeline Definition As Reviewed Code (practice `ACP-SCBI-004`) |
| `SP800-53-SA-17.6` | Structure for Testing. Require the developer of the system, system component, or system service to structure security-relevant hardware, software, and firmware to facilitate testing. | conceito: Architecture Review And Approval Governance (practice `ACP-ATB-005`) |
| `SP800-53-SA-21` | Developer Screening. Require that the developer of [system, systems component, or system service]: Has appropriate access authorizations as determined by assigned [official government duties]; and Sat | conceito: Least-Privilege Authorization Governance (practice `ACP-IAT-002`) |
| `SP800-53-SA-21.1` | Validation of Screening | conceito: Least-Privilege Authorization Governance (practice `ACP-IAT-002`) |
| `SP800-53-SA-9.1` | Risk Assessments and Organizational Approvals. Conduct an organizational assessment of risk prior to the acquisition or outsourcing of information security services; and Verify that the acquisition or | conceito: Trust Boundary And Integration Review (practice `ACP-ITS-001`) |
| `SP800-53-SC-31.1` | Test Covert Channels for Exploitability. Test a subset of the identified covert channels to determine the channels that are exploitable. | conceito: Secret Leak Prevention In Source And Pipeline (practice `ACP-SPC-001`) |
| `SP800-53-SI-4.1` | System-wide Intrusion Detection System. Connect and configure individual intrusion detection tools into a system-wide intrusion detection system. | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `SP800-53-SI-4.9` | Testing of Monitoring Tools and Mechanisms. Test intrusion-monitoring tools and mechanisms [frequency]. | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `SP800-53-SI-6.1` | Notification of Failed Security Tests | conceito: Reproducible Test Evidence Management (practice `ACP-TSV-004`) |
| `SP800-53-SI-6.2` | Automation Support for Distributed Testing. Implement automated mechanisms to support the management of distributed security and privacy function testing. | conceito: Reproducible Test Evidence Management (practice `ACP-TSV-004`) |
| `SP800-53-SR-6.1` | Testing and Analysis. Employ of the following supply chain elements, processes, and actors associated with the system, system component, or system service: [supply chain elements, processes, and actor | conceito: Automated Dependency And Image Risk Gating (practice `ACP-SCBI-002`) |

---

## OWASP DSOMM

**O que esta ES traz para este capítulo:** contribui 39 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `DSOMM-ACTIVITY-0779681137F9467C9FF248F346E77FF3` | Simple Scan. Simple Scan Deficient security tests are performed. Simple vulnerabilities are not detected and missing security configurations (e.g. headers) are not set. Fast feedback is not given. A s | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `DSOMM-ACTIVITY-0C10A7F7F78F49F2943D19FDEF248FED` | Fix based on accessibility. Fix based on accessibility Overwhelming volume of security findings from automated testing tools. This might lead to ignorance of findings. Implement a simple risk-based pr | conceito: Findings Workflow And Exception Governance (mechanism `ACM-TSV-004`) |
| `DSOMM-ACTIVITY-12C90CC63D584D9B82FFD469D2A0C298` | Ad-Hoc Security trainings for software developers. Ad-Hoc Security trainings for software developers Ad-hoc security training provides basic awareness of software security risks and best practices to | conceito: Explicit Threat Disposition Register (mechanism `ACM-TMR-004`) |
| `DSOMM-ACTIVITY-297BE0018D9441EEAB29207020D423C0` | Usage of multiple analyzers. Usage of multiple analyzers Each vulnerability analyzer has different opportunities. By using just one analyzer, some vulnerabilities might not be found. Usage of multiple | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `DSOMM-ACTIVITY-2EBFC4218C76415CA3B0FA518915BD10` | High test intensity. High test intensity A too small intensity or a too high confidence might lead to not visible vulnerabilities. A deep scan with high test intensity and a low confidence threshold i | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `DSOMM-ACTIVITY-31833D5635AF4EF39300F23D27646CE7` | Regular security training for externals. Regular security training for externals Understanding security is hard. Provide security awareness training for all personnel including externals involved in s | conceito: Threat Representation Models (mechanism `ACM-TMR-001`) |
| `DSOMM-ACTIVITY-35446784761040D9AF9ED43F3173BF8C` | Conduction of collaborative team security checks. Conduction of collaborative team security checks Development teams limited insight over security practices. Mutual security testing the security of ot | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `DSOMM-ACTIVITY-46D6A2A8F9DC4C159FC81723CFECBDDC` | Test the cloud configuration. Test the cloud configuration Standard hardening practices for cloud environments are not performed leading to vulnerabilities. With the help of tools, the configuration o | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `DSOMM-ACTIVITY-517B095749814AC0B4C70D8D1934C474` | Local development linting & style checks performed. Local development linting & style checks performed Insecure or unmaintainable code base. Integrate static code analysis tools in IDEs. | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `DSOMM-ACTIVITY-55F4C9163A34474DAD969A9F7A4F6A83` | Simple visualization of defects. Simple visualization of defects The security level of a component is not visible. Therefore, the motivation to enhance the security is not give. Vulnerabilities are si | conceito: Findings Workflow And Exception Governance (mechanism `ACM-TSV-004`) |
| `DSOMM-ACTIVITY-58825D221CE64748AF810EC9956E4129` | Test of virtualized environments. Test of virtualized environments Virtualized environments (e.g. via <i>Container Images</i>) might contains unsecure configurations. Test virtualized environments for | conceito: Trust-Boundary And DFD Modeling (mechanism `ACM-ATB-002`) |
| `DSOMM-ACTIVITY-58C46807FEE9448BB6DD8050C464AB52` | Security-Lessoned-Learned. Security-Lessoned-Learned After an incident, a similar incident might reoccur. Running a 'lessons learned' session after an incident helps drive continuous improvement. Regu | conceito: Threat Model Versioning Controls (mechanism `ACM-TMR-003`) |
| `DSOMM-ACTIVITY-598897A2358E441F984CE12EC4F6110A` | Regular automated tests. Regular automated tests After pushing source code to the version control system, any delay in receiving feedback on defects makes them harder for the developer to remediate. O | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `DSOMM-ACTIVITY-5B5A1EB2113F41FBA3D606AF4FDC9CEA` | Usage of multiple scanners. Usage of multiple scanners Each vulnerability scanner has different opportunities. By using just one scanner, some vulnerabilities might not be found. Usage of multiple spi | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `DSOMM-ACTIVITY-5E0FF85BEC894EF096B15695FA0025DC` | Coverage of more input vectors. Coverage of more input vectors Parts of the service are not covered. For example specially formatted or coded parameters are not getting detected as parameter (e.g. par | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `DSOMM-ACTIVITY-6532C1FE9D2342288722558DDABCA7D4` | Test for unused Resources. Test for unused Resources Unused resources, specially secrets, might be still valid, but are exposing information. As an attacker, I compromise a system, gather credentials | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |
| `DSOMM-ACTIVITY-6C05C8378C9946E2828B7C903E27DBA4` | Static analysis for important server side components. Static analysis for important server side components Important parts in the source code of the middleware have vulnerabilities. Usage of static an | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `DSOMM-ACTIVITY-71699DAFB2A4466BA0B289F7DBB18506` | Metrics are combined with tests. Metrics are combined with tests Changes might cause high load due to programming errors. Metrics during tests helps to identify programming errors. | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `DSOMM-ACTIVITY-79EF8103E1ED40558DF8FD2B2015BEBE` | Creation and application of a testing concept. Creation and application of a testing concept Scans might use a too small or too high test intensity. A testing concept considering the amount of time pe | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `DSOMM-ACTIVITY-7A82020C94D1471CBBD35F7FE7DF4876` | Advanced visualization of defects. Advanced visualization of defects Correlation of the vulnerabilities of different tools to have an overview of the the overall security level per component/project/t | conceito: Findings Workflow And Exception Governance (mechanism `ACM-TSV-004`) |
| `DSOMM-ACTIVITY-7BB7076493924462935DE55B2E148199` | Test of the configuration of cloud environments. Test of the configuration of cloud environments Standard hardening practices for cloud environments are not performed leading to vulnerabilities. With | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `DSOMM-ACTIVITY-85BA562384BE42198892808837BE582D` | Usage of a vulnerability management system. Usage of a vulnerability management system For known vulnerabilities a processes to estimate the exploit ability of a vulnerability is recommended. To imple | conceito: Threat Mitigation Linkage Controls (mechanism `ACM-TMR-005`) |
| `DSOMM-ACTIVITY-87B54313FAFD4860930F5EF132B3E4AD` | Test libyear. Test libyear Vulnerabilities in running artifacts stay for long and might get exploited. Test `libyear`, which provides a good insight how good patch management is. | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |
| `DSOMM-ACTIVITY-8FC3DE677B8D420B8D24F35928CFED6E` | Test the definition of virtualized environments. Test the definition of virtualized environments The definition of virtualized environments (e.g. via <i>Dockerfile</i>) might contain unsecure configur | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `DSOMM-ACTIVITY-9768F154357A4C06AF6FD66570677C9B` | Regular security training for all. Regular security training for all Conduct security awareness training for all roles currently involved in the management, development, testing, or auditing of the so | conceito: Explicit Threat Disposition Register (mechanism `ACM-TMR-004`) |
| `DSOMM-ACTIVITY-AAFFA73F59F64267B0AB732F3D13E90D` | Integration in development process. Integration in development process Validating Findings by Security Engineers Pros: - Ensures accuracy and relevance of findings before they reach product teams - Re | conceito: Findings Workflow And Exception Governance (mechanism `ACM-TSV-004`) |
| `DSOMM-ACTIVITY-AB5725AA4D5347B996DFC14B3FA93BCD` | Load tests. Load tests As it is unknown how many requests the systems and applications can serve, due to an unexpected load the availability is disturbed. Load test against the production system or a | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `DSOMM-ACTIVITY-BFDACB521E3F431DAE72D844A5E86415` | Usage of test and production environments. Usage of test and production environments Security tests are not running regularly because test environments are missing A test and a production like environ | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `DSOMM-ACTIVITY-C1ACC8AF312E4503A817A26220C993A0` | Simple false positive treatment. Simple false positive treatment Security tests may produce false positives (or _"false alarms"_), findings that are incorrectly identified as vulnerabilities. It is im | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `DSOMM-ACTIVITY-C6E3C81256E241B0AE01B7AFC41A004C` | Test for stored secrets in code. Test for stored secrets in code Stored secrets in git history or directly in code shouldn't exists because they might be exposed to unauthorized parties. Test for secr | conceito: Secret Management Systems (mechanism `ACM-SPC-001`) |
| `DSOMM-ACTIVITY-D0D681E7D6DE4829AC64A9EB2546AA0D` | Coverage and control metrics. Coverage and control metrics The effectiveness of configuration, patch and vulnerability management is unknown. Usage of Coverage- and control-metrics to show the effecti | conceito: Threat Mitigation Linkage Controls (mechanism `ACM-TMR-005`) |
| `DSOMM-ACTIVITY-DCCF1949B9A84CE8B9926A4A7F3A623A` | Test for unauthorized installation. Test for unauthorized installation Unapproved components are used. Components must be whitelisted. Regular scans on the docker infrastructure (e.g. cluster) need to | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |
| `DSOMM-ACTIVITY-E237176BBEC5447DA926E37D6DD60E4B` | Static analysis for important client side components. Static analysis for important client side components Important parts in the source code of the frontend have vulnerabilities. Usage of static anal | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `DSOMM-ACTIVITY-EA6F69F754A54922AC15A77FF0C16162` | Dismiss stale PR approvals. Dismiss stale PR approvals Intentional or accidental alterations in critical branches like main (or master) through post-approval code additions. Implement a policy where a | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `DSOMM-ACTIVITY-EE68331F9B1D4F61844BB2EA04753A84` | Static analysis for all self written components. Static analysis for all self written components Parts in the source code of the frontend or middleware have vulnerabilities. Usage of static analysis t | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `DSOMM-ACTIVITY-F0E018143B884BD0A3A9F91DB001D20BADVANCED` | WAF Advanced. WAF Advanced This advanced configuration goes beyond typical WAF implementations by enforcing strict input format checks and parameter validation to prevent any unauthorized or malformed | conceito: Static Rulepacks And Security Linters (mechanism `ACM-IVF-002`) |
| `DSOMM-ACTIVITY-F2F0F274C1A0450192FE7FC4452BC8AD` | Exploit likelihood estimation. Exploit likelihood estimation Severity-based vulnerability triage alone generates a lot false positives, requiring a more refined approach. Use the likelihood of exploit | conceito: Threat Mitigation Linkage Controls (mechanism `ACM-TMR-005`) |
| `DSOMM-ACTIVITY-F4FF841D3B2A45D9853E5EC7ECBCB054` | Static analysis for all components/libraries. Static analysis for all components/libraries Used components like libraries and legacy applications might have vulnerabilities Usage of a static analysis | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `DSOMM-ACTIVITY-F88D1B173D7D4C3D8139AD44FC4942D4` | Regular security training of security champions. Regular security training of security champions Understanding security is hard, even for security champions. Regular security training of security cham | conceito: Threat Representation Models (mechanism `ACM-TMR-001`) |

---

## MITRE ATLAS — Adversarial Threat Landscape for AI Systems

**O que esta ES traz para este capítulo:** contribui 16 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `AML.CS0000` | Evasion of Deep Learning Detector for Malware C&C Traffic. The Palo Alto Networks Security AI research team tested a deep learning model for malware command and control (C&C) traffic detection in HTTP | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `AML.CS0013` | Backdoor Attack on Deep Learning Models in Mobile Apps. Deep learning models are increasingly used in mobile applications as critical components. Researchers from Microsoft Research demonstrated that | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `AML.CS0051` | OpenClaw Command & Control via Prompt Injection. Researchers at HiddenLayer demonstrated how a webpage can embed an indirect prompt injection that causes OpenClaw to silently execute a malicious scrip | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `AML.M0006` | Use Ensemble Methods. Use an ensemble of models for inference to increase robustness to adversarial inputs. Some attacks may effectively evade one model or model family but be ineffective against othe | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `AML.M0016` | Vulnerability Scanning. Vulnerability scanning is used to find potentially exploitable software vulnerabilities to remediate them. File formats such as pickle files that are commonly used to store AI | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `AML.M0018` | User Training. Educate AI model developers to on AI supply chain risks and potentially malicious AI artifacts. Educate users on how to identify deepfakes and phishing attempts. | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `AML.M0025` | Maintain AI Dataset Provenance. Maintain a detailed history of datasets used for AI applications. The history should include information about the dataset's source as well as a complete record of any | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `AML.T0001` | Search Open AI Vulnerability Analysis. Much like the [Search Open Technical Databases](/techniques/AML.T0000), there is often ample research available on the vulnerabilities of common AI models. Once | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `AML.T0006` | Active Scanning. An adversary may probe or scan the victim system to gather information for targeting. This is distinct from other reconnaissance techniques that do not involve direct interaction with | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `AML.T0016.000` | Adversarial AI Attack Implementations. Adversaries may search for existing open source implementations of AI attacks. The research community often publishes their code for reproducibility and to furth | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `AML.T0042` | Verify Attack. Adversaries can verify the efficacy of their attack via an inference API or access to an offline copy of the target model. This gives the adversary confidence that their approach works | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `AML.T0043.001` | Black-Box Optimization. In Black-Box attacks, the adversary has black-box (i.e. [AI Model Inference API Access](/techniques/AML.T0040) via API access) access to the target model. With black-box attack | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `AML.T0043.003` | Manual Modification. Adversaries may manually modify the input data to craft adversarial data. They may use their knowledge of the target model to modify parts of the data they suspect helps the model | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `AML.TA0001` | AI Attack Staging. The adversary is leveraging their knowledge of and access to the target system to tailor the attack. AI Attack Staging consists of techniques adversaries use to prepare their attac | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `AML.TA0005` | Execution. The adversary is trying to run malicious code embedded in AI artifacts or software. Execution consists of techniques that result in adversary-controlled code running on a local or remote s | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `AML.TA0007` | Defense Evasion. The adversary is trying to avoid being detected by AI-enabled security software. Defense Evasion consists of techniques that adversaries use to avoid detection throughout their compr | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |

---

## NIST AI 100-2 e2025 — Adversarial Machine Learning Taxonomy

**O que esta ES traz para este capítulo:** contribui 15 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `NIST-AI-100-2-E2025-2.1.3` | Attacker Capabilities. AML attacks for PredAI systems can be taxonomized with respect to the capabilities that an attacker controls. An adversary might leverage six types of capabilities to achieve th | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `NIST-AI-100-2-E2025-2.1.4` | Attacker Knowledge. Another dimension of attack classification is how much knowledge the attacker has about the ML system. There are three main types of attacks: White-box attacks. These assume that t | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `NIST-AI-100-2-E2025-2.2.1` | White-Box Evasion Attacks. In the white-box threat model, the attacker has full knowledge of the model architecture and parameters, as discussed in Section 2.1.4. The main challenge for creating adver | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `NIST-AI-100-2-E2025-2.2.2` | Black-Box Evasion Attacks. [NISTAML.025] [Back to Index] Black-box evasion attacks are designed under a realistic adversarial model in which the attacker has no prior knowledge of the model architectu | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `NIST-AI-100-2-E2025-2.2.3` | Transferability of Attacks. Another method for generating adversarial attacks under restrictive threat models involves transferring an attack crafted on a different ML model. Typically, an attacker tr | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `NIST-AI-100-2-E2025-2.2.5` | Mitigations. Mitigating evasion attacks is challenging because adversarial examples are widespread in a variety of ML model architectures and application domains. Possible explanations for the existen | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `NIST-AI-100-2-E2025-2.3` | Poisoning Attacks and Mitigations. Poisoning attacks are broadly defined as adversarial attacks during the training stage of the ML algorithm. The first known poisoning attack was developed for worm s | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `NIST-AI-100-2-E2025-2.3.2` | Targeted Poisoning. [NISTAML.024] [Back to Index] In contrast to availability attacks, targeted poisoning attacks induce a change in the ML model’s prediction on a small number of targeted samples. If | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `NIST-AI-100-2-E2025-2.4.3` | Property Inference. [NISTAML.034] [Back to Index] In property inference attacks (also called distribution inference), the attacker tries to learn global information about the training data distributio | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `NIST-AI-100-2-E2025-3.3.1` | Attack Techniques. A range of techniques exist for launching direct prompting attacks, many of which gener- alise across various attacker objectives. With a focus on direct prompting attacks to enable | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `NIST-AI-100-2-E2025-3.3.3` | Mitigations. The following defense strategies can be employed throughout the deployment life cycle of an AI model or system to reduce the risk that the model or system will be vulnerable to direct pro | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `NIST-AI-100-2-E2025-3.5` | Security of Agents. An increasingly common use of GenAI models is constructing an (often LLM-based) AGENT, a software system that iteratively prompts a model, process its outputs – such as to select a | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `NIST-AI-100-2-E2025-3.6` | Benchmarks for AML Vulnerabilities. There are several publicly available benchmarks for evaluating models’ vulnerability to AML attacks. Datasets like JailbreakBench [72], AdvBench [448], HarmBench [2 | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `NIST-AI-100-2-E2025-4.2.2` | Supply Chain Challenges. The literature on AML shows a trend of designing new attacks that are more difficult to detect. Since the poisoning of AI models can persist through safety training and be tri | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `NIST-AI-100-2-E2025-4.2.5` | Risk Management in Light of AML. A key question that this taxonomy deliberately leaves aside is how organizations can make decisions about the development and use of AI systems in light of evidence ab | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |

---

## OWASP SAMM v2.1

**O que esta ES traz para este capítulo:** contribui 14 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `SAMM-ACTIVITY-G_EG_1_B` | Identify security champions. Identify security champions. Implement a program where each software development team has a member considered a "Security Champion" who is the liaison between Information | conceito: Threat Representation Models (mechanism `ACM-TMR-001`) |
| `SAMM-ACTIVITY-I_DM_1_B` | Define basic defect metrics. Define basic defect metrics. Once per defined period of time (typically at least once per year), go over your both resolved and still open recorded security defects in eve | conceito: Findings Workflow And Exception Governance (mechanism `ACM-TSV-004`) |
| `SAMM-ACTIVITY-I_DM_2_A` | track security defects | conceito: Findings Workflow And Exception Governance (mechanism `ACM-TSV-004`) |
| `SAMM-ACTIVITY-I_DM_2_B` | Define advanced defect metrics | conceito: Findings Workflow And Exception Governance (mechanism `ACM-TSV-004`) |
| `SAMM-ACTIVITY-I_DM_3_B` | Use metrics to improve the security strategy. Use metrics to improve the security strategy. Regularly (at least once per year) revisit the defect management metrics you're collecting and compare the e | conceito: Findings Workflow And Exception Governance (mechanism `ACM-TSV-004`) |
| `SAMM-ACTIVITY-I_SB_3_B` | Test application dependencies | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `SAMM-ACTIVITY-O_IM_3_B` | Establish an incident response team | conceito: Reviewer Accountability And Consistency Gates (mechanism `ACM-TMR-006`) |
| `SAMM-ACTIVITY-V_RT_1_B` | Perform fuzz testing. Perform fuzz testing. Perform fuzzing, sending random or malformed data to the test subject in an attempt to make it crash. Fuzz testing or Fuzzing is a Black Box software testin | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `SAMM-ACTIVITY-V_RT_3_A` | Automate security requirements testing. Automate security requirements testing. Write and automate regression tests for all identified (and fixed) bugs to ensure that these become a test harness preve | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `SAMM-ACTIVITY-V_ST_1_B` | Test high risk application components manually | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `SAMM-ACTIVITY-V_ST_2_A` | Develop application-specific security test cases. Develop application-specific security test cases. Increase the effectiveness of automated security testing tools by tuning and customizing them for yo | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `SAMM-ACTIVITY-V_ST_2_B` | Establish a penetration testing process | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `SAMM-ACTIVITY-V_ST_3_A` | review results during development | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `SAMM-ACTIVITY-V_ST_3_B` | Establish continuous, scalable security verification. Establish continuous, scalable security verification. Integrate security testing in parallel to all other development activities, including requir | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |

---

## PCI DSS v4.0.1

**O que esta ES traz para este capítulo:** contribui 13 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `PCI-1.1.1` | All security policies and operational 1.1.1 Examine documentation and interview. All security policies and operational 1.1.1 Examine documentation and interview an | conceito: Versioned Diagrams And ADR Records (mechanism `ACM-ATB-001`) |
| `PCI-1.3.1` | Inbound traffic to the CDE is restricted as 1.3.1.a Examine configuration standards for NSCs. Inbound traffic to the CDE is restricted as 1.3.1.a Examine configuration standards for NSCs | conceito: Versioned Diagrams And ADR Records (mechanism `ACM-ATB-001`) |
| `PCI-1.3.2` | Outbound traffic from the CDE is restricted as 1.3.2.a Examine configuration standards for NSCs. Outbound traffic from the CDE is restricted as 1.3.2.a Examine configuration standards for NSCs | conceito: Boundary Mediation Controls (mechanism `ACM-ATB-003`) |
| `PCI-11.3.1` | Internal vulnerability scans are performed as 11.3.1.a Examine internal scan report results f. Internal vulnerability scans are performed as 11.3.1.a Examine internal scan report results | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `PCI-11.3.2` | External vulnerability scans are performed as 11.3.2.a Examine ASV scan reports from the last. External vulnerability scans are performed as 11.3.2.a Examine ASV scan reports from the last | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `PCI-11.4.1` | A penetration testing methodology is defined, 11.4.1 Examine documentation and interview. A penetration testing methodology is defined, 11.4.1 Examine documentation and interview inter | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `PCI-11.4.4` | Exploitable vulnerabilities and security 11.4.4 Examine penetration testing results to veri. Exploitable vulnerabilities and security 11.4.4 Examine penetration testing results to ve | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `PCI-11.4.5` | If segmentation is used to isolate the CDE 11.4.5.a Examine segmentation controls and. If segmentation is used to isolate the CDE 11.4.5.a Examine segmentation controls and | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `PCI-11.5.1` | Intrusion-detection and/or intrusion- 11.5.1.a Examine system configurations and. Intrusion-detection and/or intrusion- 11.5.1.a Examine system configurations and t | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `PCI-5.1.1` | All security policies and operational 5.1.1 Examine documentation and interview. All security policies and operational 5.1.1 Examine documentation and interview and ma | conceito: Build And Image Inventory Generation (mechanism `ACM-SCBI-005`) |
| `PCI-6.5.2` | Upon completion of a significant change, all 6.5.2 Examine documentation for significant. Upon completion of a significant change, all 6.5.2 Examine documentation for significant helps e | conceito: Schema And Contract Validators (mechanism `ACM-IVF-003`) |
| `PCI-6.5.5` | Live PANs are not used in pre-production 6.5.5.a Examine policies and procedures to verify m. Live PANs are not used in pre-production 6.5.5.a Examine policies and procedures to verify | conceito: Code Review For Input And Error Discipline (mechanism `ACM-IVF-001`) |
| `PCI-9.2.1` | Appropriate facility entry controls are in place 9.2.1 Observe entry controls and interview. Appropriate facility entry controls are in place 9.2.1 Observe entry controls and interview | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |

---

## MITRE CAPEC v3.9

**O que esta ES traz para este capítulo:** contribui 9 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `CAPEC-121` | Exploit Non-Production Interfaces. Exploit Non-Production Interfaces. An adversary exploits a sample, demonstration, test, or debug interface that is unintentionally enabled on a production system, wi | conceito: API Gateway With Mutual Authentication (mechanism `ACM-ITS-001`) |
| `CAPEC-190` | Reverse Engineer an Executable to Expose Assumed Hidden Functionality. Reverse Engineer an Executable to Expose Assumed Hidden Functionality. An attacker analyzes a binary file or executable for the p | conceito: Secret Management Systems (mechanism `ACM-SPC-001`) |
| `CAPEC-261` | Fuzzing for garnering other adjacent user/sensitive data. Fuzzing for garnering other adjacent user/sensitive data. An adversary who is authorized to send queries to a target sends variants of expecte | conceito: Secret Management Systems (mechanism `ACM-SPC-001`) |
| `CAPEC-28` | Fuzzing. Fuzzing. In this attack pattern, the adversary leverages fuzzing to try to identify weaknesses in the system. Fuzzing is a software security and functionality testing method that feeds random | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `CAPEC-300` | Port Scanning. Port Scanning. An adversary uses a combination of techniques to determine the state of the ports on a remote target. Any service or application available for TCP or UDP networking will | conceito: Secret Management Systems (mechanism `ACM-SPC-001`) |
| `CAPEC-305` | TCP ACK Scan. TCP ACK Scan. An adversary uses TCP ACK segments to gather information about firewall or ACL configuration. The purpose of this type of scan is to discover information about filter confi | conceito: Secret Management Systems (mechanism `ACM-SPC-001`) |
| `CAPEC-310` | Scanning for Vulnerable Software. Scanning for Vulnerable Software. An attacker engages in scanning activity to find vulnerable software versions or types, such as operating system versions or network | conceito: Secret Management Systems (mechanism `ACM-SPC-001`) |
| `CAPEC-639` | Probe System Files. Probe System Files. An adversary obtains unauthorized information due to improperly protected files. If an application stores sensitive information in a file that is not protected | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `CAPEC-672` | Malicious Code Implanted During Chip Programming. Malicious Code Implanted During Chip Programming. During the programming step of chip manufacture, an adversary with access and necessary technical sk | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |

---

## CIS Controls v8.1.2

**O que esta ES traz para este capítulo:** contribui 9 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `CIS-14.9` | Conduct Role-Specific Security Awareness and Skills Training. Conduct role-specific security awareness and skills training. Example implementations include secure system administration courses for IT | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `CIS-15.5` | Assess Service Providers. Assess service providers consistent with the enterprise’s service provider management policy. Assessment scope may vary based on classification(s), and may include review of | conceito: API Gateway With Mutual Authentication (mechanism `ACM-ITS-001`) |
| `CIS-16.12` | Implement Code-Level Security Checks. Apply static and dynamic analysis tools within the application life cycle to verify that secure coding practices are being followed. | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `CIS-16.14` | Conduct Threat Modeling. Conduct threat modeling. Threat modeling is the process of identifying and addressing application security design flaws within a design, before code is created. It is conducte | conceito: Structured Threat Analysis Frameworks (mechanism `ACM-TMR-002`) |
| `CIS-17.5` | Assign Key Roles and Responsibilities. Assign key roles and responsibilities for incident response, including staff from legal, IT, information security, facilities, public relations, human resources, | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `CIS-18.1` | Establish and Maintain a Penetration Testing Program. Establish and maintain a penetration testing program appropriate to the size, complexity, industry, and maturity of the enterprise. Penetration te | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `CIS-18.4` | Validate Security Measures. Validate security measures after each penetration test. If deemed necessary, modify rulesets and capabilities to detect the techniques used during testing. | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `CIS-7` | Continuous Vulnerability Management. Develop a plan to continuously assess and track vulnerabilities on all enterprise assets within the enterprise’s infrastructure, in order to remediate, and minimiz | conceito: Threat Mitigation Linkage Controls (mechanism `ACM-TMR-005`) |
| `CIS-7.1` | Establish | conceito: Threat Mitigation Linkage Controls (mechanism `ACM-TMR-005`) |

---

## SAFECode — Practical Security Stories and Tasks for Agile Development (2012)

**O que esta ES traz para este capítulo:** contribui 7 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `SCAGILE-EXP-10` | Prioritization of resolution of issues from code analysis. Prioritization of resolution of issues identified by code analysis tools (static and run-time), especially for existing code | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `SCAGILE-EXP-4` | Conduct penetration tests on software around beta stage. Conduct penetration tests on the software around beta stage | conceito: Static Analysis Profile Management (mechanism `ACM-TSV-005`) |
| `SCAGILE-EXP-5` | Enhance existing test suite to include security test cases. Enhance existing test suite to include security test cases | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `SCAGILE-EXP-7` | Perform network fuzz testing. Perform network fuzz testing | conceito: Static Analysis Profile Management (mechanism `ACM-TSV-005`) |
| `SCAGILE-OPS-15` | Ensure all QA engineers have obtained secure testing training. Ensure all QA engineers have obtained secure testing training | conceito: Threat Traceability Into Requirements And Validation (practice `ACP-TMR-005`) |
| `SCAGILE-OPS-4` | Resolve critical and high severity issues from static analysis. Resolve critical and high severity issues identified by static code analysis tools | conceito: Test Execution Surfaces (mechanism `ACM-TSV-002`) |
| `SCAGILE-OPS-9` | Continuously verify coverage of static code analysis tools. Continuously verify coverage of static code analysis tools for new and existing code | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |

---

## NIST SSDF (SP 800-218 v1.1)

**O que esta ES traz para este capítulo:** contribui 5 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `SSDF-PRACTICE-RV.3` | Analyze Vulnerabilities to Identify Their Root Causes. Help reduce the frequency of vulnerabilities in the future. | conceito: Reviewer Accountability And Consistency Gates (mechanism `ACM-TMR-006`) |
| `SSDF-TASK-PO.4.2` | Implement processes, mechanisms, etc. to gather and safeguard the necessary information in support of the criteria. | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `SSDF-TASK-PW.8.1` | Determine whether executable code testing should be performed to find vulnerabilities not identified by previous reviews, analysis, or testing and, if so, which types of testing should be used. | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `SSDF-TASK-RV.3.1` | Analyze identified vulnerabilities to determine their root causes. | conceito: Reviewer Accountability And Consistency Gates (mechanism `ACM-TMR-006`) |
| `SSDF-TASK-RV.3.3` | Review the software for similar vulnerabilities to eradicate a c lass of vulnerabilities , and proactively fix them rather than waiting for external reports. | conceito: Threat Model Versioning Controls (mechanism `ACM-TMR-003`) |

---

## NIST AI RMF 1.0

**O que esta ES traz para este capítulo:** contribui 4 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `NIST-AI-RMF-MANAGE-4.3` | Incidents and errors are communicated to relevant. monitored regularly. AI actors, including affected communities. Processes for track- ing, responding to, and recovering from incidents and errors are | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `NIST-AI-RMF-MEASURE-2.11` | Fairness and bias – as identified in the MAP. function – are evaluated and results are documented. | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `NIST-AI-RMF-MEASURE-2.7` | AI system security and resilience – as identified. in the MAP function – are evaluated and documented. | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `NIST-AI-RMF-MEASURE-3.3` | Feedback processes for end users and impacted. communities to report problems and appeal system outcomes are established and integrated into AI system evaluation metrics. | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |

---

## PCI Secure SLC v1.1

**O que esta ES traz para este capítulo:** contribui 3 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `PCISSLC-2.3` | Formal software security strategy established and maintained. Strategy based on or aligned with industry-accepted methodologies; covers entire lifecycle; reviewed annually | conceito: Threat Disposition And Accepted Risk Governance (practice `ACP-TMR-004`) |
| `PCISSLC-2.5` | Evidence generated and maintained to demonstrate effectiveness of assurance processes. Evidence generated for each process to illustrate it results in expected security outcomes; frequently collected | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `PCISSLC-4.2` | Newly discovered vulnerabilities fixed; reintroduction of similar vulnerabilities prevented. Process for distributing fixes and preventing reintroduction; criticality criteria defined; decisions to no | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |

---

## SAFECode — Fundamental Practices for Secure Software Development (2018)

**O que esta ES traz para este capítulo:** contribui 2 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `SCFPSSD-MITIGATIONS` | Identify Mitigating Factors or Workarounds. When fixes unavailable, identify mitigations and workarounds for stakeholders | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `SCFPSSD-TESTING` | Testing and Validation (Automated and Manual). Automated testing (SAST, DAST, fuzzing) and manual testing (pen testing, code review) practices | conceito: Test Execution Surfaces (mechanism `ACM-TSV-002`) |

---

## MITRE CWE — Software Development View (v4.19.1)

**O que esta ES traz para este capítulo:** contribui 1 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `CWE-414` | Missing Lock Check. A product does not check to see if a lock is present before performing sensitive operations on a resource. | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |

---

## HIPAA Security Rule

**O que esta ES traz para este capítulo:** contribui 1 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `HIPAA-164-308a8` | Evaluation. Evaluation — Administrative Safeguard. Perform a periodic technical and non-technical evaluation, based initially upon the standards implemented under this rule and subsequently in respons | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |

---

## OWASP MCP — Secure Server Development v1.0

**O que esta ES traz para este capítulo:** contribui 1 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `OWASP-MCP-RISK-LANDSCAPE` | Current Vulnerability Landscape. Current Vulnerability Landscape MCP servers expose a broad and unique attack surface, containing traditional API security vulnerabilities and some unique AI-oriented r | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |

---

## OWASP Machine Learning Top 10

**O que esta ES traz para este capítulo:** contribui 1 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `ML10-2023` | ML10:2023 Model Poisoning. Description. Model poisoning attacks occur when an attacker manipulates the model's parameters to cause it to behave in an undesirable way. How to Prevent. Regularisation: A | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |

---

## SAFECode — Software Integrity Controls (2010)

**O que esta ES traz para este capítulo:** contribui 1 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `SCSIC-DEV-TESTING` | Peer Reviews and Security Testing. SAST, DAST, binary analysis, malware detection, compliance validation, code coverage; peer review for both security and integrity | conceito: Test Execution Surfaces (mechanism `ACM-TSV-002`) |

---

## SLSA Specification v1.0 — Build Track

**O que esta ES traz para este capítulo:** contribui 1 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `SLSA-PRINCIPLE-PREFER-ATTESTATIONS` | Prefer attestations over inferences. Require explicit attestations about an artifact’s provenance; do not infer security properties from a platform’s configurations. Reasoning : Theoretically, access | conceito: Artifact Signing And Attestation (mechanism `ACM-SCBI-004`) |

---
