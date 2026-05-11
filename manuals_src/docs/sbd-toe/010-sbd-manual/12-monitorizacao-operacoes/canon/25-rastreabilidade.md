# 25. Rastreabilidade — Monitorização & Operações

## Sumário

Este capítulo trata de **monitorização, logging e operações de segurança** —
logging estruturado, audit trail, centralização, deteção de incidentes,
integração com SIEM/SOAR. As fontes externas seguintes contribuem para
esta área:

- **NIST SP 800-53 Rev. 5** — 100 referência(s)
- **PCI DSS v4.0.1** — 28 referência(s)
- **CIS Controls v8.1.2** — 27 referência(s)
- **OWASP ASVS v5.0.0** — 23 referência(s)
- **OWASP DSOMM** — 17 referência(s)
- **MITRE CAPEC v3.9** — 13 referência(s)
- **MITRE CWE — Software Development View (v4.19.1)** — 8 referência(s)
- **HIPAA Security Rule** — 5 referência(s)
- **OWASP SAMM v2.1** — 5 referência(s)
- **MITRE ATLAS — Adversarial Threat Landscape for AI Systems** — 3 referência(s)
- **OWASP Proactive Controls (2018)** — 3 referência(s)
- **EU Digital Operational Resilience Act (DORA)** — 2 referência(s)
- **SAFECode — Fundamental Practices for Secure Software Development (2018)** — 2 referência(s)
- **NIST SSDF (SP 800-218 v1.1)** — 2 referência(s)
- **EU GDPR (RGPD)** — 1 referência(s)
- **OWASP Machine Learning Top 10** — 1 referência(s)
- **OWASP Top 10 (2021)** — 1 referência(s)
- **PCI Secure SLC v1.1** — 1 referência(s)

---

## NIST SP 800-53 Rev. 5

**O que esta ES traz para este capítulo:** contribui 100 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `SP800-53-AC-16.9` | Attribute Reassignment — Regrading Mechanisms. Change security and privacy attributes associated with information only via regrading mechanisms validated using [organization-defined techniques or proc | conceito: Least-Privilege Authorization Governance (practice `ACP-IAT-002`) |
| `SP800-53-AC-17.2` | Protection of Confidentiality and Integrity Using Encryption. Implement cryptographic mechanisms to protect the confidentiality and integrity of remote access sessions. | conceito: Transport And Protocol Hardening (practice `ACP-ITS-003`) |
| `SP800-53-AC-17.6` | Protection of Mechanism Information. Protect information about remote access mechanisms from unauthorized use and disclosure. | conceito: Transport And Protocol Hardening (practice `ACP-ITS-003`) |
| `SP800-53-AC-2.13` | Disable Accounts for High-risk Individuals. Disable accounts of individuals within [time period] of discovery of [significant risks]. | conceito: Access Review And Timely Revocation (practice `ACP-IAT-003`) |
| `SP800-53-AC-23` | Data Mining Protection. Employ [techniques] for [data storage objects] to detect and protect against unauthorized data mining. | conceito: Secret Leak Prevention In Source And Pipeline (practice `ACP-SPC-001`) |
| `SP800-53-AC-25` | Reference Monitor. Implement a reference monitor for [access control policies] that is tamperproof, always invoked, and small enough to be subject to analysis and testing, the completeness of which ca | conceito: Least-Privilege Authorization Governance (practice `ACP-IAT-002`) |
| `SP800-53-AC-3.10` | Audited Override of Access Control Mechanisms. Employ an audited override of automated access control mechanisms under [conditions] by [roles]. | conceito: Least-Privilege Authorization Governance (practice `ACP-IAT-002`) |
| `SP800-53-AC-3.5` | Security-relevant Information. Prevent access to [security-relevant information] except during secure, non-operable system states. | conceito: Least-Privilege Authorization Governance (practice `ACP-IAT-002`) |
| `SP800-53-AC-4.15` | Detection of Unsanctioned Information. When transferring information between different security domains, examine the information for the presence of [unsanctioned information] and prohibit the transfe | conceito: Trust-Boundary And Flow Review (practice `ACP-ATB-003`) |
| `SP800-53-AC-4.25` | Data Sanitization. When transferring information between different security domains, sanitize data to minimize in accordance with [policy]. | conceito: Trust-Boundary And Flow Review (practice `ACP-ATB-003`) |
| `SP800-53-AC-4.26` | Audit Filtering Actions. When transferring information between different security domains, record and audit content filtering actions and results for the information being filtered. | conceito: Trust-Boundary And Flow Review (practice `ACP-ATB-003`) |
| `SP800-53-AC-6.9` | Log Use of Privileged Functions. Log the execution of privileged functions. | conceito: Least-Privilege Authorization Governance (practice `ACP-IAT-002`) |
| `SP800-53-AT-4` | Training Records. Document and monitor information security and privacy training activities, including security and privacy awareness training and specific role-based security and privacy training; an | conceito: Identidade, autenticação e gestão de sessões (slice `ACO-IAT`) |
| `SP800-53-AU-11` | Audit Record Retention. Retain audit records for [time period] to provide support for after-the-fact investigations of incidents and to meet regulatory and organizational information retention require | conceito: Log Retention And Lifecycle Governance (practice `ACP-SLG-004`) |
| `SP800-53-AU-11.1` | Long-term Retrieval Capability. Employ [measures] to ensure that long-term audit records generated by the system can be retrieved. | conceito: Log Retention And Lifecycle Governance (practice `ACP-SLG-004`) |
| `SP800-53-AU-12` | Audit Record Generation. Provide audit record generation capability for the event types the system is capable of auditing as defined in [AU-2a](#au-2_smt.a) on [system components]; Allow [personnel or | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `SP800-53-AU-12.1` | System-wide and Time-correlated Audit Trail. Compile audit records from [system components] into a system-wide (logical or physical) audit trail that is time-correlated to within [level of tolerance]. | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `SP800-53-AU-12.3` | Changes by Authorized Individuals. Provide and implement the capability for [individuals or roles] to change the logging to be performed on [system components] based on [selectable event criteria] wit | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `SP800-53-AU-15` | Alternate Audit Logging Capability | conceito: Structured And Centralized Security Logging (practice `ACP-SLG-002`) |
| `SP800-53-AU-2` | Event Logging. Identify the types of events that the system is capable of logging in support of the audit function: [event types] | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `SP800-53-AU-2.2` | Selection of Audit Events by Component | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `SP800-53-AU-3` | Content of Audit Records. Ensure that audit records contain information that establishes the following: What type of event occurred | conceito: Structured And Centralized Security Logging (practice `ACP-SLG-002`) |
| `SP800-53-AU-3.3` | Limit Personally Identifiable Information Elements. Limit personally identifiable information contained in audit records to the following elements identified in the privacy risk assessment: [elements] | conceito: Structured And Centralized Security Logging (practice `ACP-SLG-002`) |
| `SP800-53-AU-4` | Audit Log Storage Capacity. Allocate audit log storage capacity to accommodate [audit log retention requirements]. | conceito: Log Retention And Lifecycle Governance (practice `ACP-SLG-004`) |
| `SP800-53-AU-5` | Response to Audit Logging Process Failures. Alert [personnel or roles] within [time period] in the event of an audit logging process failure; and Take the following additional actions: [additional act | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `SP800-53-AU-5.1` | Storage Capacity Warning. Provide a warning to [personnel, roles, and/or locations] within [time period] when allocated audit log storage volume reaches [percentage] of repository maximum audit log st | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `SP800-53-AU-5.2` | Real-time Alerts. Provide an alert within [real-time period] to [personnel, roles, and/or locations] when the following audit failure events occur: [audit logging failure events requiring real-time al | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `SP800-53-AU-5.3` | Configurable Traffic Volume Thresholds. Enforce configurable network communications traffic volume thresholds reflecting limits on audit log storage capacity and network traffic above those thresholds | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `SP800-53-AU-5.4` | Shutdown on Failure. Invoke a in the event of [audit logging failures] , unless an alternate audit logging capability exists. | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `SP800-53-AU-5.5` | Alternate Audit Logging Capability. Provide an alternate audit logging capability in the event of a failure in primary audit logging capability that implements [alternate audit logging functionality]. | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `SP800-53-AU-6.2` | Automated Security Alerts | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `SP800-53-AU-6.3` | Correlate Audit Record Repositories. Analyze and correlate audit records across different repositories to gain organization-wide situational awareness. | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `SP800-53-AU-6.8` | Full Text Analysis of Privileged Commands. Perform a full text analysis of logged privileged commands in a physically distinct component or subsystem of the system, or other system that is dedicated t | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `SP800-53-AU-8` | Time Stamps. Use internal system clocks to generate time stamps for audit records; and Record time stamps for audit records that meet [granularity of time measurement] and that use Coordinated Univers | conceito: Structured And Centralized Security Logging (practice `ACP-SLG-002`) |
| `SP800-53-AU-9` | Protection of Audit Information. Protect audit information and audit logging tools from unauthorized access, modification, and deletion; and Alert [personnel or roles] upon detection of unauthorized a | conceito: Log Integrity And Protected Access (practice `ACP-SLG-003`) |
| `SP800-53-AU-9.1` | Hardware Write-once Media. Write audit trails to hardware-enforced, write-once media. | conceito: Log Integrity And Protected Access (practice `ACP-SLG-003`) |
| `SP800-53-AU-9.2` | Store on Separate Physical Systems or Components. Store audit records [frequency] in a repository that is part of a physically different system or system component than the system or component being a | conceito: Log Integrity And Protected Access (practice `ACP-SLG-003`) |
| `SP800-53-AU-9.3` | Cryptographic Protection. Implement cryptographic mechanisms to protect the integrity of audit information and audit tools. | conceito: Log Integrity And Protected Access (practice `ACP-SLG-003`) |
| `SP800-53-AU-9.4` | Access by Subset of Privileged Users. Authorize access to management of audit logging functionality to only [subset of privileged users or roles]. | conceito: Log Integrity And Protected Access (practice `ACP-SLG-003`) |
| `SP800-53-IA-2.9` | Network Access to Non-privileged Accounts — Replay Resistant | conceito: Strong Authentication And Step-Up Enforcement (practice `ACP-IAT-001`) |
| `SP800-53-IR-10` | Integrated Information Security Analysis Team | conceito: Logging de eventos de segurança e audit trail (slice `ACO-SLG`) |
| `SP800-53-MA-4.1` | Logging and Review. Log [organization-defined audit events] for nonlocal maintenance and diagnostic sessions; and Review the audit records of the maintenance and diagnostic sessions to detect anomalou | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `SP800-53-MP-6.8` | Remote Purging or Wiping of Information. Provide the capability to purge or wipe information from [systems or system components]. | conceito: Logging de eventos de segurança e audit trail (slice `ACO-SLG`) |
| `SP800-53-PE-3.4` | Lockable Casings. Use lockable physical casings to protect [system components] from unauthorized physical access. | conceito: Logging de eventos de segurança e audit trail (slice `ACO-SLG`) |
| `SP800-53-PE-3.5` | Tamper Protection. Employ [anti-tamper technologies] to physical tampering or alteration of [hardware components] within the system. | conceito: Logging de eventos de segurança e audit trail (slice `ACO-SLG`) |
| `SP800-53-PE-8.2` | Physical Access Records | conceito: Logging de eventos de segurança e audit trail (slice `ACO-SLG`) |
| `SP800-53-PE-8.3` | Limit Personally Identifiable Information Elements. Limit personally identifiable information contained in visitor access records to the following elements identified in the privacy risk assessment: [ | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `SP800-53-PS-3.3` | Information Requiring Special Protective Measures. Verify that individuals accessing a system processing, storing, or transmitting information requiring special protection: Have valid access authoriza | conceito: Identidade, autenticação e gestão de sessões (slice `ACO-IAT`) |
| `SP800-53-PS-6.1` | Information Requiring Special Protection | conceito: Logging de eventos de segurança e audit trail (slice `ACO-SLG`) |
| `SP800-53-PT-2.1` | Data Tagging. Attach data tags containing [authorized processing] to [elements of personally identifiable information]. | conceito: Gestão de segredos, configuração protegida e identidades operacionais (slice `ACO-SPC`) |
| `SP800-53-PT-2.2` | Automation. Manage enforcement of the authorized processing of personally identifiable information using [automated mechanisms]. | conceito: Gestão de segredos, configuração protegida e identidades operacionais (slice `ACO-SPC`) |
| `SP800-53-PT-6.2` | Exemption Rules. Review all Privacy Act exemptions claimed for the system of records at [frequency] to ensure they remain appropriate and necessary in accordance with law, that they have been promulga | conceito: Gestão de segredos, configuração protegida e identidades operacionais (slice `ACO-SPC`) |
| `SP800-53-SA-14` | Criticality Analysis | conceito: Threat Model Creation And Triggered Refresh (practice `ACP-TMR-001`) |
| `SP800-53-SA-15.13` | Logging Syntax. Require the developer of the system or system component to minimize the use of personally identifiable information in development and test environments. | conceito: Pipeline Definition As Reviewed Code (practice `ACP-SCBI-004`) |
| `SP800-53-SA-18` | Tamper Resistance and Detection | conceito: Artifact Signature And Provenance Validation (practice `ACP-SCBI-006`) |
| `SP800-53-SA-19.3` | Component Disposal | conceito: Artifact Signature And Provenance Validation (practice `ACP-SCBI-006`) |
| `SP800-53-SA-4.11` | System of Records. Include [Privacy Act requirements] in the acquisition contract for the operation of a system of records on behalf of an organization to accomplish an organizational mission or funct | conceito: Trust Boundary And Integration Review (practice `ACP-ITS-001`) |
| `SP800-53-SA-4.6` | Use of Information Assurance Products. Employ only government off-the-shelf or commercial off-the-shelf information assurance and information assurance-enabled information technology products that com | conceito: Trust Boundary And Integration Review (practice `ACP-ITS-001`) |
| `SP800-53-SA-9.7` | Organization-controlled Integrity Checking. Provide the capability to check the integrity of information while it resides in the external system. | conceito: Trust Boundary And Integration Review (practice `ACP-ITS-001`) |
| `SP800-53-SC-14` | Public Access Protections | conceito: External Exposure And Boundary Mediation Design (practice `ACP-ATB-004`) |
| `SP800-53-SC-16` | Transmission of Security and Privacy Attributes. Associate [organization-defined security and privacy attributes] with information exchanged between systems and between system components. | conceito: Message Integrity And Authorized Peer Validation (practice `ACP-ITS-004`) |
| `SP800-53-SC-20.2` | Data Origin and Integrity. Provide data origin and integrity protection artifacts for internal name/address resolution queries. | conceito: Message Integrity And Authorized Peer Validation (practice `ACP-ITS-004`) |
| `SP800-53-SC-21.1` | Data Origin and Integrity | conceito: Message Integrity And Authorized Peer Validation (practice `ACP-ITS-004`) |
| `SP800-53-SC-28` | Protection of Information at Rest. Protect the of the following information at rest: [information at rest]. | conceito: Vault-Backed Secret Storage (practice `ACP-SPC-002`) |
| `SP800-53-SC-34.2` | Integrity Protection on Read-only Media. Protect the integrity of information prior to storage on read-only media and control the media after such information has been recorded onto the media. | conceito: Pipeline Definition As Reviewed Code (practice `ACP-SCBI-004`) |
| `SP800-53-SC-34.3` | Hardware-based Protection | conceito: Pipeline Definition As Reviewed Code (practice `ACP-SCBI-004`) |
| `SP800-53-SC-36` | Distributed Processing and Storage. Distribute the following processing and storage components across multiple : [organization-defined processing and storage components]. | conceito: Trust-Boundary And Flow Review (practice `ACP-ATB-003`) |
| `SP800-53-SC-4.2` | Multilevel or Periods Processing. Prevent unauthorized information transfer via shared resources in accordance with [procedures] when system processing explicitly switches between different informatio | conceito: Operational Identity Binding And OIDC Use (practice `ACP-SPC-004`) |
| `SP800-53-SC-8` | Transmission Confidentiality and Integrity. Protect the of transmitted information. | conceito: Transport And Protocol Hardening (practice `ACP-ITS-003`) |
| `SP800-53-SI-1` | Policy and Procedures. Develop, document, and disseminate to [organization-defined personnel or roles]: system and information integrity policy that: Addresses purpose, scope, roles, responsibilities, | conceito: Boundary Input Validation (practice `ACP-IVF-001`) |
| `SP800-53-SI-10.6` | Injection Prevention. Prevent untrusted data injections. | conceito: Boundary Input Validation (practice `ACP-IVF-001`) |
| `SP800-53-SI-12` | Information Management and Retention. Manage and retain information within the system and information output from the system in accordance with applicable laws, executive orders, directives, regulatio | conceito: Operational Identity Binding And OIDC Use (practice `ACP-SPC-004`) |
| `SP800-53-SI-12.1` | Limit Personally Identifiable Information Elements. Limit personally identifiable information being processed in the information life cycle to the following elements of personally identifiable informa | conceito: Operational Identity Binding And OIDC Use (practice `ACP-SPC-004`) |
| `SP800-53-SI-12.3` | Information Disposal. Use the following techniques to dispose of, destroy, or erase information following the retention period: [organization-defined techniques]. | conceito: Operational Identity Binding And OIDC Use (practice `ACP-SPC-004`) |
| `SP800-53-SI-13.5` | Failover Capability. Provide [failover capability] for the system. | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `SP800-53-SI-14.1` | Refresh from Trusted Sources. Obtain software and data employed during system component and service refreshes from the following trusted sources: [trusted sources]. | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `SP800-53-SI-14.2` | Non-persistent Information. ; and Delete information when no longer needed. | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `SP800-53-SI-18.3` | Collection. Collect personally identifiable information directly from the individual. | conceito: Operational Identity Binding And OIDC Use (practice `ACP-SPC-004`) |
| `SP800-53-SI-19.1` | Collection. De-identify the dataset upon collection by not collecting personally identifiable information. | conceito: Operational Identity Binding And OIDC Use (practice `ACP-SPC-004`) |
| `SP800-53-SI-19.5` | Statistical Disclosure Control. Manipulate numerical data, contingency tables, and statistical findings so that no individual or organization is identifiable in the results of the analysis. | conceito: Operational Identity Binding And OIDC Use (practice `ACP-SPC-004`) |
| `SP800-53-SI-19.6` | Differential Privacy. Prevent disclosure of personally identifiable information by adding non-deterministic noise to the results of mathematical operations before the results are reported. | conceito: Operational Identity Binding And OIDC Use (practice `ACP-SPC-004`) |
| `SP800-53-SI-20` | Tainting. Embed data or capabilities in the following systems or system components to determine if organizational data has been exfiltrated or improperly removed from the organization: [systems or sys | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `SP800-53-SI-3.2` | Automatic Updates | conceito: Automated Dependency And Image Risk Gating (practice `ACP-SCBI-002`) |
| `SP800-53-SI-3.7` | Nonsignature-based Detection | conceito: Automated Dependency And Image Risk Gating (practice `ACP-SCBI-002`) |
| `SP800-53-SI-4` | System Monitoring. Monitor the system to detect: Attacks and indicators of potential attacks in accordance with the following monitoring objectives: [monitoring objectives] | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `SP800-53-SI-4.10` | Visibility of Encrypted Communications. Make provisions so that [encrypted communications traffic] is visible to [system monitoring tools and mechanisms]. | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `SP800-53-SI-4.12` | Automated Organization-generated Alerts. Alert [personnel or roles] using [automated mechanisms] when the following indications of inappropriate or unusual activities with security or privacy implicat | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `SP800-53-SI-4.13` | Analyze Traffic and Event Patterns. Analyze communications traffic and event patterns for the system; Develop profiles representing common traffic and event patterns; and Use the traffic and event pro | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `SP800-53-SI-4.16` | Correlate Monitoring Information. Correlate information from monitoring tools and mechanisms employed throughout the system. | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `SP800-53-SI-4.7` | Automated Response to Suspicious Events. Notify [incident response personnel] of detected suspicious events; and Take the following actions upon detection: [least-disruptive actions]. | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `SP800-53-SI-4.8` | Protection of Monitoring Information | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `SP800-53-SI-7` | Software, Firmware, and Information Integrity. Employ integrity verification tools to detect unauthorized changes to the following software, firmware, and information: [organization-defined software, | conceito: Artifact Signature And Provenance Validation (practice `ACP-SCBI-006`) |
| `SP800-53-SI-7.1` | Integrity Checks. Perform an integrity check of [organization-defined software, firmware, and information]. | conceito: Artifact Signature And Provenance Validation (practice `ACP-SCBI-006`) |
| `SP800-53-SI-7.13` | Code Execution in Protected Environments | conceito: Artifact Signature And Provenance Validation (practice `ACP-SCBI-006`) |
| `SP800-53-SI-7.14` | Binary or Machine Executable Code | conceito: Artifact Signature And Provenance Validation (practice `ACP-SCBI-006`) |
| `SP800-53-SI-7.15` | Code Authentication. Implement cryptographic mechanisms to authenticate the following software or firmware components prior to installation: [software or firmware components]. | conceito: Artifact Signature And Provenance Validation (practice `ACP-SCBI-006`) |
| `SP800-53-SI-7.3` | Centrally Managed Integrity Tools. Employ centrally managed integrity verification tools. | conceito: Artifact Signature And Provenance Validation (practice `ACP-SCBI-006`) |
| `SP800-53-SI-7.6` | Cryptographic Protection. Implement cryptographic mechanisms to detect unauthorized changes to software, firmware, and information. | conceito: Artifact Signature And Provenance Validation (practice `ACP-SCBI-006`) |
| `SP800-53-SI-7.9` | Verify Boot Process. Verify the integrity of the boot process of the following system components: [system components]. | conceito: Artifact Signature And Provenance Validation (practice `ACP-SCBI-006`) |
| `SP800-53-SI-9` | Information Input Restrictions | requirements_catalog (strong): Catálogo de Requisitos de Desenvolvimento Seguro |

---

## PCI DSS v4.0.1

**O que esta ES traz para este capítulo:** contribui 28 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `PCI-10.3.1` | Read access to audit logs files is limited to 10.3.1 Interview system administrators and. Read access to audit logs files is limited to 10.3.1 Interview system administrators and read | conceito: Log Integrity And Access Controls (mechanism `ACM-SLG-003`) |
| `PCI-10.3.2` | Audit log files are protected to prevent 10.3.2 Examine system configurations and. Audit log files are protected to prevent 10.3.2 Examine system configurations and | conceito: Log Integrity And Access Controls (mechanism `ACM-SLG-003`) |
| `PCI-10.4.1` | The following audit logs are reviewed at least 10.4.1.a Examine security policies and procedures. The following audit logs are reviewed at least 10.4.1.a Examine security policies and procedures | conceito: Machine-Readable Structured Logging (mechanism `ACM-SLG-001`) |
| `PCI-10.5.1` | Retain audit log history for at least 12 10.5.1.a Examine documentation to verify that the. Retain audit log history for at least 12 10.5.1.a Examine documentation to verify that the m | conceito: Machine-Readable Structured Logging (mechanism `ACM-SLG-001`) |
| `PCI-10.7.2` | Failures of critical security control systems 10.7.2.a Examine documentation to verify that. Failures of critical security control systems 10.7.2.a Examine documentation to verify that | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `PCI-10.7.3` | Failures of any critical security control 10.7.3.a Examine documentation and interview. Failures of any critical security control 10.7.3.a Examine documentation and interview | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `PCI-12.10.5` | The security incident response plan 12.10.5 Examine documentation and observe. The security incident response plan 12.10.5 Examine documentation and observe | conceito: Threat Representation Models (mechanism `ACM-TMR-001`) |
| `PCI-3.2.1` | Account data storage is kept to a minimum through 3.2.1.a Examine the data retention and disp. Account data storage is kept to a minimum through 3.2.1.a Examine the data retention and di | conceito: Secret Management Systems (mechanism `ACM-SPC-001`) |
| `PCI-3.3.2` | SAD that is stored electronically prior to completion 3.3.2 Examine data stores, system configurat. SAD that is stored electronically prior to completion 3.3.2 Examine data stores, system configur | conceito: Secret Management Systems (mechanism `ACM-SPC-001`) |
| `PCI-3.4.2` | When using remote-access technologies, technical 3.4.2.a Examine documented policies and. When using remote-access technologies, technical 3.4.2.a Examine documented policies and | conceito: Secret Management Systems (mechanism `ACM-SPC-001`) |
| `PCI-3.6.1` | Procedures are defined and implemented to 3.6.1 Examine documented key-management. Procedures are defined and implemented to 3.6.1 Examine documented key-management those who | conceito: Secret Management Systems (mechanism `ACM-SPC-001`) |
| `PCI-3.7.5` | Key management policies procedures are 3.7.5.a Examine the documented key-management. Key management policies procedures are 3.7.5.a Examine the documented key-management | conceito: Secret Management Systems (mechanism `ACM-SPC-001`) |
| `PCI-3.7.7` | Key management policies and procedures are 3.7.7.a Examine the documented key-management. Key management policies and procedures are 3.7.7.a Examine the documented key-management key the | conceito: Secret Management Systems (mechanism `ACM-SPC-001`) |
| `PCI-4.1.2` | Roles and responsibilities for performing 4.1.2.a Examine documentation to verify that. Roles and responsibilities for performing 4.1.2.a Examine documentation to verify that | conceito: Secret Management Systems (mechanism `ACM-SPC-001`) |
| `PCI-5.3.4` | Audit logs for the anti-malware solution | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `PCI-7.2.5` | All application and system accounts and 7.2.5.a Examine policies and procedures to verify. All application and system accounts and 7.2.5.a Examine policies and procedures to veri | intro (strong): Arquitetura Segura > Políticas Organizacionais Relevantes |
| `PCI-8.2.1` | All users are assigned a unique ID before 8.2.1.a Interview responsible personnel to verify c. All users are assigned a unique ID before 8.2.1.a Interview responsible personnel to verify | aplicacao_lifecycle (strong): Aplicação de Arquitetura Segura no Ciclo de Vida > User Stories reutilizáveis > US-01 - Definição de princípios e baseline de arquitetura segura |
| `PCI-8.2.5` | Access for terminated users is immediately 8.2.5.a Examine information sources for terminated. Access for terminated users is immediately 8.2.5.a Examine information sources for terminated | aplicacao_lifecycle (strong): Aplicação de Arquitetura Segura no Ciclo de Vida > User Stories reutilizáveis > US-01 - Definição de princípios e baseline de arquitetura segura |
| `PCI-8.6.1` | If accounts used by systems or applications 8.6.1 Examine application and system accounts. If accounts used by systems or applications 8.6.1 Examine application and system accounts | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura |
| `PCI-9.1.2` | Roles and responsibilities for performing 9.1.2.a Examine documentation to verify that. Roles and responsibilities for performing 9.1.2.a Examine documentation to verify that | conceito: Periodic Review And Access Audit (mechanism `ACM-IAT-003`) |
| `PCI-9.3.4` | Visitor logs are used to maintain a physical 9.3.4.a Examine the visitor logs and interview. Visitor logs are used to maintain a physical 9.3.4.a Examine the visitor logs and interview | conceito: Machine-Readable Structured Logging (mechanism `ACM-SLG-001`) |
| `PCI-9.4.3` | Media with cardholder data sent outside the 9.4.3.a Examine documentation to verify that. Media with cardholder data sent outside the 9.4.3.a Examine documentation to verify that | conceito: Logging de eventos de segurança e audit trail (slice `ACO-SLG`) |
| `PCI-9.4.5` | Inventory logs of all electronic media with 9.4.5.a Examine documentation to verify that. Inventory logs of all electronic media with 9.4.5.a Examine documentation to verify that | conceito: Log Integrity And Access Controls (mechanism `ACM-SLG-003`) |
| `PCI-9.4.6` | Hard-copy materials with cardholder data are 9.4.6.a Examine the media destruction policy to. Hard-copy materials with cardholder data are 9.4.6.a Examine the media destruction policy to | conceito: Logging de eventos de segurança e audit trail (slice `ACO-SLG`) |
| `PCI-REQ-10` | Log | conceito: Machine-Readable Structured Logging (mechanism `ACM-SLG-001`) |
| `PCI-REQ-11` | Test Security of Systems and Networks Regularly. Requirement 11: Test Security of Systems and Networks Regularly. Goal: Regularly Monitor and Test Networks. | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `PCI-REQ-3` | Protect Stored Account Data. Requirement 3: Protect Stored Account Data. Goal: Protect Account Data. | conceito: Secret Management Systems (mechanism `ACM-SPC-001`) |
| `PCI-REQ-7` | Restrict Access to System Components and Cardholder Data by Business Need to Know. Requirement 7: Restrict Access to System Components and Cardholder Data by Business Need to Know. Goal: Implement Str | aplicacao_lifecycle (strong): Aplicação de Arquitetura Segura no Ciclo de Vida > User Stories reutilizáveis > US-03 - Revisão formal do design arquitetural |

---

## CIS Controls v8.1.2

**O que esta ES traz para este capítulo:** contribui 27 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `CIS-1` | Inventory and Control of Enterprise Assets. Actively manage (inventory, track, and correct) all enterprise assets (end-user devices, including portable and mobile | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `CIS-1.4` | Use Dynamic Host Configuration Protocol (DHCP) Logging to Update Enterprise Asset Inventory. Use DHCP logging on all DHCP servers or Internet Protocol (IP) address management tools to update the enter | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `CIS-11.4` | Establish and Maintain an Isolated Instance of Recovery Data. Establish and maintain an isolated instance of recovery data. Example implementations include, version controlling backup destinations thr | conceito: Release promotion, rollout controlado e readiness para rollback (slice `ACO-RPR`) |
| `CIS-12` | Network Infrastructure Management. Establish, implement, and actively manage (track, report, correct) network devices, in order to prevent attackers from exploiting vulnerable network services and acc | conceito: Arquitetura segura e fronteiras de confiança (slice `ACO-ATB`) |
| `CIS-12.5` | Centralize Network Authentication, Authorization, and Auditing (AAA). Centralize network AAA. | conceito: Access Policy Enforcement (mechanism `ACM-IAT-002`) |
| `CIS-13.1` | Centralize Security Event Alerting. Centralize security event alerting across enterprise assets for log correlation and analysis. Best practice implementation requires the use of a SIEM, which include | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `CIS-13.11` | Tune Security Event Alerting Thresholds. Tune security event alerting thresholds monthly, or more frequently. | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `CIS-13.6` | Collect Network Traffic Flow Logs. Collect network traffic flow logs and/or network traffic to review and alert upon from network devices. | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `CIS-16.11` | Leverage Vetted Modules or Services for Application Security Components. Leverage vetted modules or services for application security components, such as identity management, encryption, auditing, and | conceito: Approved Source And Registry Governance (practice `ACP-SCBI-003`) |
| `CIS-16.9` | Secure Coding | conceito: Schema And Contract Validators (mechanism `ACM-IVF-003`) |
| `CIS-17.3` | Establish | conceito: Threat Traceability Into Requirements And Validation (practice `ACP-TMR-005`) |
| `CIS-17.6` | Define Mechanisms for Communicating During Incident Response | conceito: Threat Traceability Into Requirements And Validation (practice `ACP-TMR-005`) |
| `CIS-3` | Data Protection. Develop processes and technical controls to identify, classify, securely handle, retain, and dispose of data. | conceito: Gestão de segredos, configuração protegida e identidades operacionais (slice `ACO-SPC`) |
| `CIS-3.14` | Log Sensitive Data Access. Log sensitive data access, including modification and disposal. | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `CIS-3.5` | Securely Dispose of Data. Securely dispose of data as outlined in the enterprise’s documented data management process. Ensure the disposal process and method are commensurate with the data sensitivity | conceito: Gestão de segredos, configuração protegida e identidades operacionais (slice `ACO-SPC`) |
| `CIS-3.7` | Establish | conceito: Gestão de segredos, configuração protegida e identidades operacionais (slice `ACO-SPC`) |
| `CIS-4.11` | Enforce Remote Wipe Capability on Portable End-User Devices. Remotely wipe enterprise data from enterprise-owned portable end-user devices when deemed appropriate such as lost or stolen devices, or wh | conceito: Release promotion, rollout controlado e readiness para rollback (slice `ACO-RPR`) |
| `CIS-5.3` | Disable Dormant Accounts. Delete or disable any dormant accounts after a period of 45 days of inactivity, where supported. | conceito: Periodic Review And Access Audit (mechanism `ACM-IAT-003`) |
| `CIS-8` | Audit Log Management | conceito: Machine-Readable Structured Logging (mechanism `ACM-SLG-001`) |
| `CIS-8.1` | Establish | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `CIS-8.11` | Conduct Audit Log Reviews. Conduct reviews of audit logs to detect anomalies or abnormal events that could indicate a potential threat. Conduct reviews on a weekly, or more frequent, basis. | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `CIS-8.12` | Collect Service Provider Logs. Collect service provider logs, where supported. Example implementations include collecting authentication and authorization events, data creation and disposal events, an | conceito: Machine-Readable Structured Logging (mechanism `ACM-SLG-001`) |
| `CIS-8.3` | Ensure Adequate Audit Log Storage. Ensure that logging destinations maintain adequate storage to comply with the enterprise’s audit log management process. | conceito: Log Retention And Lifecycle Governance (practice `ACP-SLG-004`) |
| `CIS-8.4` | Standardize Time Synchronization. Standardize time synchronization. Configure at least two synchronized time sources across enterprise assets, where supported. | conceito: Machine-Readable Structured Logging (mechanism `ACM-SLG-001`) |
| `CIS-8.5` | Collect Detailed Audit Logs. Configure detailed audit logging for enterprise assets containing sensitive data. Include event source, date, username, timestamp, source addresses, destination addresses, | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `CIS-8.6` | Collect DNS Query Audit Logs. Collect DNS query audit logs on enterprise assets, where appropriate and supported. | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `CIS-8.9` | Centralize Audit Logs. Centralize, to the extent possible, audit log collection and retention across enterprise assets in accordance with the documented audit log management process. Example implement | conceito: Machine-Readable Structured Logging (mechanism `ACM-SLG-001`) |

---

## OWASP ASVS v5.0.0

**O que esta ES traz para este capítulo:** contribui 23 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `ASVS-REQ-V11.2.1` | Verify that industry-validated implementations (including libraries and hardware-accelerated implementations) are used for cryptographic operations. | conceito: Gestão de segredos, configuração protegida e identidades operacionais (slice `ACO-SPC`) |
| `ASVS-REQ-V11.2.3` | Verify that all cryptographic primitives utilize a minimum of 128-bits of security based on the algorithm, key size, and configuration. For example, a 256-bit ECC key provides roughly 128 bits of secu | conceito: Gestão de segredos, configuração protegida e identidades operacionais (slice `ACO-SPC`) |
| `ASVS-REQ-V11.3.3` | Verify that encrypted data is protected against unauthorized modification preferably by using an approved authenticated encryption method or by combining an approved encryption method with an approved | conceito: Gestão de segredos, configuração protegida e identidades operacionais (slice `ACO-SPC`) |
| `ASVS-REQ-V11.4.3` | Verify that hash functions used in digital signatures, as part of data authentication or data integrity are collision resistant and have appropriate bit-lengths. If collision resistance is required, t | conceito: Gestão de segredos, configuração protegida e identidades operacionais (slice `ACO-SPC`) |
| `ASVS-REQ-V14.1.2` | Verify that all sensitive data protection levels have a documented set of protection requirements. This must include (but not be limited to) requirements related to general encryption, integrity verif | conceito: Gestão de segredos, configuração protegida e identidades operacionais (slice `ACO-SPC`) |
| `ASVS-REQ-V14.2.2` | Verify that the application prevents sensitive data from being cached in server components, such as load balancers and application caches, or ensures that the data is securely purged after use. | conceito: Gestão de segredos, configuração protegida e identidades operacionais (slice `ACO-SPC`) |
| `ASVS-REQ-V14.2.4` | Verify that controls around sensitive data related to encryption, integrity verification, retention, how the data is to be logged, access controls around sensitive data in logs, privacy and privacy-en | conceito: Gestão de segredos, configuração protegida e identidades operacionais (slice `ACO-SPC`) |
| `ASVS-REQ-V14.2.8` | Verify that sensitive information is removed from the metadata of user-submitted files unless storage is consented to by the user. | conceito: Gestão de segredos, configuração protegida e identidades operacionais (slice `ACO-SPC`) |
| `ASVS-REQ-V15.4.1` | Verify that shared objects in multi-threaded code (such as caches, files, or in-memory objects accessed by multiple threads) are accessed safely by using thread-safe types and synchronization mechanis | conceito: Gestão de segredos, configuração protegida e identidades operacionais (slice `ACO-SPC`) |
| `ASVS-REQ-V15.4.2` | Verify that checks on a resource's state, such as its existence or permissions, and the actions that depend on them are performed as a single atomic operation to prevent time-of-check to time-of-use ( | conceito: Identidade, autenticação e gestão de sessões (slice `ACO-IAT`) |
| `ASVS-REQ-V15.4.3` | Verify that locks are used consistently to avoid threads getting stuck, whether by waiting on each other or retrying endlessly, and that locking logic stays within the code responsible for managing th | conceito: Gestão de segredos, configuração protegida e identidades operacionais (slice `ACO-SPC`) |
| `ASVS-REQ-V16.1.1` | Verify that an inventory exists documenting the logging performed at each layer of the application's technology stack, what events are being logged, log formats, where that logging is stored, how it i | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `ASVS-REQ-V16.2.1` | Verify that each log entry includes necessary metadata (such as when, where, who, what) that would allow for a detailed investigation of the timeline when an event happens. | conceito: Machine-Readable Structured Logging (mechanism `ACM-SLG-001`) |
| `ASVS-REQ-V16.2.2` | Verify that time sources for all logging components are synchronized, and that timestamps in security event metadata use UTC or include an explicit time zone offset. UTC is recommended to ensure consi | conceito: Machine-Readable Structured Logging (mechanism `ACM-SLG-001`) |
| `ASVS-REQ-V16.2.3` | Verify that the application only stores or broadcasts logs to the files and services that are documented in the log inventory. | conceito: Machine-Readable Structured Logging (mechanism `ACM-SLG-001`) |
| `ASVS-REQ-V16.2.5` | Verify that when logging sensitive data, the application enforces logging based on the data's protection level. For example, it may not be allowed to log certain data, such as credentials or payment d | conceito: Machine-Readable Structured Logging (mechanism `ACM-SLG-001`) |
| `ASVS-REQ-V16.3.1` | Verify that all authentication operations are logged, including successful and unsuccessful attempts. Additional metadata, such as the type of authentication or factors used, should also be collected. | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `ASVS-REQ-V16.3.3` | Verify that the application logs the security events that are defined in the documentation and also logs attempts to bypass the security controls, such as input validation, business logic, and anti-au | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `ASVS-REQ-V16.3.4` | Verify that the application logs unexpected errors and security control failures such as backend TLS failures. | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `ASVS-REQ-V16.4.1` | Verify that all logging components appropriately encode data to prevent log injection. | conceito: Log Integrity And Access Controls (mechanism `ACM-SLG-003`) |
| `ASVS-REQ-V16.4.2` | Verify that logs are protected from unauthorized access and cannot be modified. | conceito: Log Integrity And Access Controls (mechanism `ACM-SLG-003`) |
| `ASVS-REQ-V16.4.3` | Verify that logs are securely transmitted to a logically separate system for analysis, detection, alerting, and escalation. The aim is to ensure that if the application is breached, the logs are not c | conceito: Log Integrity And Access Controls (mechanism `ACM-SLG-003`) |
| `ASVS-REQ-V16.5.4` | Verify that a "last resort" error handler is defined which will catch all unhandled exceptions. This is both to avoid losing error details that must go to log files and to ensure that an error does no | conceito: Code Review For Input And Error Discipline (mechanism `ACM-IVF-001`) |

---

## OWASP DSOMM

**O que esta ES traz para este capítulo:** contribui 17 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `DSOMM-ACTIVITY-0A929C3EAB9A42068761ADF84B74622E` | Creation of advanced abuse stories. Creation of advanced abuse stories Simple user stories are not going deep enough. Relevant security considerations are performed. Security flaws are discovered too | conceito: Structured Threat Analysis Frameworks (mechanism `ACM-TMR-002`) |
| `DSOMM-ACTIVITY-1CD5E4B8BE364726ADC7D8F843F47AC8` | Audit of system events. Audit of system events System events (system calls) trends and attacks are not detected. Gathering of system calls. | conceito: Log Integrity And Access Controls (mechanism `ACM-SLG-003`) |
| `DSOMM-ACTIVITY-4ECED38A79044C45ADB050B663065540` | Centralized system logging. Centralized system logging Centralized system logging involves collecting and storing system logs from multiple sources in a secure, central location. This approach improve | conceito: Machine-Readable Structured Logging (mechanism `ACM-SLG-001`) |
| `DSOMM-ACTIVITY-51F3FCE5B5C846838C41E785FE4F3B5F` | SLA per criticality. SLA per criticality Not communicating how many applications are adhering to SLAs based on the criticality of vulnerabilities can lead to delayed remediation of critical security i | conceito: Threat Mitigation Linkage Controls (mechanism `ACM-TMR-005`) |
| `DSOMM-ACTIVITY-613A73DC4F6049DBA6CE4FB7BF8519F9` | PII logging concept. PII logging concept Personal identifiable information (PII) is logged and the privacy law (e.g. General Data Protection Regulation) is not followed. A concept how to log PII is do | conceito: Log Integrity And Access Controls (mechanism `ACM-SLG-003`) |
| `DSOMM-ACTIVITY-746025A6DBFB4087A000E46ACAB64EE1` | Usage of an security account. Usage of an security account Having security auditing in the same account as infrastructure and applications at the cloud provide might cause evil administrators (or thre | conceito: Log Integrity And Access Controls (mechanism `ACM-SLG-003`) |
| `DSOMM-ACTIVITY-7C7350896A83419F8B27C1E676CEDEA1` | Visualized logging. Visualized logging System and application protocols are not visualized properly which leads to no or very limited logging assessment. Specially developers might have difficulty to | conceito: Machine-Readable Structured Logging (mechanism `ACM-SLG-001`) |
| `DSOMM-ACTIVITY-7F36B9BABC054FD69A2A73344C249722` | Deactivation of unused metrics. Deactivation of unused metrics High resources are used while gathering unused metrics. Deactivation of unused metrics helps to free resources. | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `DSOMM-ACTIVITY-845F06EC148C4C6797557041911DCCA5` | Coverage of sequential operations. Coverage of sequential operations Sequential operations like workflows (e.g. login -> put products in the basket Sequential operations are defined and checked by the | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `DSOMM-ACTIVITY-8A442D8E0EB14793A513571AEF982EDD` | Alerting. Alerting Incidents are discovered after they happened. Thresholds for metrics are set. In case the thresholds are reached, alarms are send out. Which should get attention due to the critical | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `DSOMM-ACTIVITY-95CAEF9636ED458CA0875C35D4F9DEC2` | Conduction of collaborative security checks with developers and system administrators. Conduction of collaborative security checks with developers and system administrators Security checks by external | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `DSOMM-ACTIVITY-BC548CBACB824F76BD4B325D9D256279` | Number of vulnerabilities/severity. Number of vulnerabilities/severity Communication can be performed in a simple way, e.g. text based during the build process. This activity depends on at least one s | conceito: Findings Workflow And Exception Governance (mechanism `ACM-TSV-004`) |
| `DSOMM-ACTIVITY-CCF4561D253F4762ADCBBC4622FD6FC5` | Correlation of security events. Correlation of security events Detection of security related events with hints on different systems/tools/metrics is not possible. Events are correlated on one system. | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `DSOMM-ACTIVITY-CCFDD0A8991E4269AD77C0A54CA655CB` | Logging of security events. Logging of security events Implement logging of security relevant events. The following events tend to be security relevant: - successful/failed login/logout - creation, ch | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `DSOMM-ACTIVITY-D03BC41074A74E9282CBD01A020CB6BF` | Advanced app. metrics. Advanced app. metrics People are not looking into tests results. Vulnerabilities not recolonized, even they are detected by tools. All defects from the dimension Test- and Verif | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `DSOMM-ACTIVITY-EB2C7F9DD0BD4253A2BACFF2ACE4A075` | Security unit tests for important components. Security unit tests for important components Vulnerabilities are rising due to code changes. Usage of unit tests to test important security related featur | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `DSOMM-ACTIVITY-FE875E17AE4A45F8A359244AA4FCBC04` | Centralized application logging. Centralized application logging Local stored logs can be unauthorized manipulated by attackers with system access or might be corrupt after an incident. In addition, i | conceito: Machine-Readable Structured Logging (mechanism `ACM-SLG-001`) |

---

## MITRE CAPEC v3.9

**O que esta ES traz para este capítulo:** contribui 13 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `CAPEC-150` | Collect Data from Common Resource Locations. Collect Data from Common Resource Locations. An adversary exploits well-known locations for resources for the purposes of undermining the security of the t | conceito: Secret Management Systems (mechanism `ACM-SPC-001`) |
| `CAPEC-184` | Software Integrity Attack. Software Integrity Attack. An attacker initiates a series of events designed to cause a user, program, server, or device to perform actions which undermine the integrity of | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `CAPEC-268` | Audit Log Manipulation. Audit Log Manipulation. The attacker injects, manipulates, deletes, or forges malicious log entries into the log file, in an attempt to mislead an audit of the log file or cove | conceito: Trust-Boundary And DFD Modeling (mechanism `ACM-ATB-002`) |
| `CAPEC-54` | Query System for Information. Query System for Information. An adversary, aware of an application's location (and possibly authorized to use the application), probes an application's structure and eva | conceito: Secret Management Systems (mechanism `ACM-SPC-001`) |
| `CAPEC-546` | Incomplete Data Deletion in a Multi-Tenant Environment. Incomplete Data Deletion in a Multi-Tenant Environment. An adversary obtains unauthorized information due to insecure or incomplete data deletio | conceito: Secret Management Systems (mechanism `ACM-SPC-001`) |
| `CAPEC-568` | Capture Credentials via Keylogger. Capture Credentials via Keylogger. An adversary deploys a keylogger in an effort to obtain credentials directly from a system's user. After capturing all the keystro | conceito: Secret Management Systems (mechanism `ACM-SPC-001`) |
| `CAPEC-571` | Block Logging to Central Repository. Block Logging to Central Repository. An adversary prevents host-generated logs being delivered to a central location in an attempt to hide indicators of compromise | conceito: Trust-Boundary And DFD Modeling (mechanism `ACM-ATB-002`) |
| `CAPEC-577` | Owner Footprinting. Owner Footprinting. An adversary exploits functionality meant to identify information about the primary users on the target system to an authorized user. They may do this, for exam | conceito: Secret Management Systems (mechanism `ACM-SPC-001`) |
| `CAPEC-637` | Collect Data from Clipboard | conceito: Secret Management Systems (mechanism `ACM-SPC-001`) |
| `CAPEC-675` | Retrieve Data from Decommissioned Devices. Retrieve Data from Decommissioned Devices. An adversary obtains decommissioned, recycled, or discarded systems and devices that can include an organization’s | conceito: Secret Management Systems (mechanism `ACM-SPC-001`) |
| `CAPEC-69` | Validate all untrusted data | conceito: Access Policy Enforcement (mechanism `ACM-IAT-002`) |
| `CAPEC-81` | Web Server Logs Tampering. Web Server Logs Tampering. Web Logs Tampering attacks involve an attacker injecting, deleting or otherwise tampering with the contents of web logs typically for the purposes | conceito: Trust-Boundary And DFD Modeling (mechanism `ACM-ATB-002`) |
| `CAPEC-93` | Log Injection-Tampering-Forging. Log Injection-Tampering-Forging. This attack targets the log files of the target host. The attacker injects, manipulates or forges malicious log entries in the log fil | conceito: Trust-Boundary And DFD Modeling (mechanism `ACM-ATB-002`) |

---

## MITRE CWE — Software Development View (v4.19.1)

**O que esta ES traz para este capítulo:** contribui 8 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `CWE-117` | Improper Output Neutralization for Logs. The product constructs a log message from external input, but it does not neutralize or incorrectly neutralizes special elements when the message is written to | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `CWE-1230` | Exposure of Sensitive Information Through Metadata. The product prevents direct access to a resource containing sensitive information, but it does not sufficiently limit access to metadata that is der | conceito: Logging de eventos de segurança e audit trail (slice `ACO-SLG`) |
| `CWE-224` | Obscured Security-relevant Information by Alternate Name. The product records security-relevant information according to an alternate name of the affected entity, instead of the canonical name. | conceito: Logging de eventos de segurança e audit trail (slice `ACO-SLG`) |
| `CWE-360` | Trust of System Event Data. Security based on event locations are insecure and can be spoofed. | conceito: Authentication And Federation Protocols (mechanism `ACM-IAT-001`) |
| `CWE-649` | Reliance on Obfuscation or Encryption of Security-Relevant Inputs without Integrity Checking. The product uses obfuscation or encryption of inputs that should not be mutable by an external actor, but | conceito: Logging de eventos de segurança e audit trail (slice `ACO-SLG`) |
| `CWE-766` | Critical Data Element Declared Public. The product declares a critical variable, field, or member to be public when intended security policy requires it to be private. | conceito: Access Policy Enforcement (mechanism `ACM-IAT-002`) |
| `CWE-778` | Insufficient Logging. When a security-critical event occurs, the product either does not record the event or omits important details about the event when logging it. | conceito: Authentication And Federation Protocols (mechanism `ACM-IAT-001`) |
| `CWE-779` | Logging of Excessive Data. The product logs too much information, making log files hard to process and possibly hindering recovery efforts or forensic analysis after an attack. | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |

---

## HIPAA Security Rule

**O que esta ES traz para este capítulo:** contribui 5 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `HIPAA-164-308a6` | Security Incident Procedures. Security Incident Procedures — Administrative Safeguard. Implement policies and procedures to address security incidents. Required implementation specification: Response | conceito: Log Retention And Lifecycle Governance (practice `ACP-SLG-004`) |
| `HIPAA-164-310b` | Workstation Use. Workstation Use — Physical Safeguard. Implement policies and procedures that specify the proper functions to be performed, the manner in which those functions are to be performed, and | conceito: Logging de eventos de segurança e audit trail (slice `ACO-SLG`) |
| `HIPAA-164-310c` | Workstation Security. Workstation Security — Physical Safeguard. Implement physical safeguards for all workstations that access ePHI, to restrict access to authorised users. Workstation security inclu | conceito: Logging de eventos de segurança e audit trail (slice `ACO-SLG`) |
| `HIPAA-164-312b` | Audit Controls. Audit Controls — Technical Safeguard. Implement hardware, software, and/or procedural mechanisms that record and examine activity in information systems that contain or use ePHI. Audit | conceito: Log Integrity And Access Controls (mechanism `ACM-SLG-003`) |
| `HIPAA-164-312c1` | Integrity. Integrity — Technical Safeguard. Implement policies and procedures to protect ePHI from improper alteration or destruction. Addressable implementation specification: Mechanism to Authentica | conceito: Schema And Contract Validators (mechanism `ACM-IVF-003`) |

---

## OWASP SAMM v2.1

**O que esta ES traz para este capítulo:** contribui 5 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `SAMM-ACTIVITY-I_DM_3_A` | Enforce an SLA for defect management | conceito: Findings Workflow And Exception Governance (mechanism `ACM-TSV-004`) |
| `SAMM-ACTIVITY-O_IM_1_A` | Analyze available log data (e.g., access logs, application logs, infrastructure logs), to detect possible security incidents in accordance with known log data retention periods | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `SAMM-ACTIVITY-O_IM_2_A` | Define an incident detection process | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `SAMM-ACTIVITY-O_IM_2_B` | Define an incident response process. Define an incident response process. Establish and document the formal security incident response process. Ensure documentation includes information like&#58 | conceito: Threat Model Versioning Controls (mechanism `ACM-TMR-003`) |
| `SAMM-ACTIVITY-O_IM_3_A` | Ensure process documentation includes measures for continuous process improvement | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |

---

## MITRE ATLAS — Adversarial Threat Landscape for AI Systems

**O que esta ES traz para este capítulo:** contribui 3 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `AML.M0024` | AI Telemetry Logging. Implement logging of inputs and outputs of deployed AI models. When deploying AI agents, implement logging of the intermediate steps of agentic actions and decisions, data access | conceito: Logging de eventos de segurança e audit trail (slice `ACO-SLG`) |
| `AML.T0010` | AI Supply Chain Compromise. Adversaries may gain initial access to a system by compromising the unique portions of the AI supply chain. This could include [Hardware](/techniques/AML.T0010.000), [Data] | conceito: Logging de eventos de segurança e audit trail (slice `ACO-SLG`) |
| `AML.T0075` | Cloud Service Discovery. Adversaries may attempt to enumerate the cloud services running on a system after gaining access. These methods can differ from platform-as-a-service (PaaS), to infrastructure | conceito: Logging de eventos de segurança e audit trail (slice `ACO-SLG`) |

---

## OWASP Proactive Controls (2018)

**O que esta ES traz para este capítulo:** contribui 3 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `OPC-C3` | Secure Database Access. This section describes secure access to all data stores, including both relational databases and NoSQL databases. It covers query parameterization, secure configuration of data | conceito: Logging de eventos de segurança e audit trail (slice `ACO-SLG`) |
| `OPC-C8` | Protect Data Everywhere. Sensitive data such as passwords, credit card numbers, health records, personal information and business secrets require extra protection, particularly if that data falls unde | conceito: Logging de eventos de segurança e audit trail (slice `ACO-SLG`) |
| `OPC-C9` | Implement Security Logging and Monitoring. Logging is a concept that most developers already use for debugging and diagnostics. Security logging is an equally basic concept: to log security informatio | conceito: Logging de eventos de segurança e audit trail (slice `ACO-SLG`) |

---

## EU Digital Operational Resilience Act (DORA)

**O que esta ES traz para este capítulo:** contribui 2 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `DORA-ART-10` | DORA Article 10. Article 10 (Detection) requires mechanisms to promptly detect anomalous activities — including network performance issues and ICT-related incidents — and to identify potential single | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `DORA-ART-19` | DORA Article 19. Article 19 (Reporting of major ICT-related incidents and voluntary notification of significant cyber threats) requires financial entities to report major ICT-related incidents to the | conceito: Logging Failure Visibility Controls (mechanism `ACM-SLG-004`) |

---

## SAFECode — Fundamental Practices for Secure Software Development (2018)

**O que esta ES traz para este capítulo:** contribui 2 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `SCFPSSD-FINDINGS` | Manage Security Findings. Security finding severity definition and risk acceptance process | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `SCFPSSD-LOGGING` | Establish Log Requirements and Audit Practices. Security logging requirements and audit trail practices for software | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |

---

## NIST SSDF (SP 800-218 v1.1)

**O que esta ES traz para este capítulo:** contribui 2 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `SSDF-TASK-PS.3.1` | Securely archive the necessary files and supporting data (e.g., integrity verification information, provenance da ta) to be retained for each software release. | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `SSDF-TASK-PW.1.3` | Where appropriate, build in support for using standardized security features and services (e.g., enabling software to integrate with existing log management, identity management, access control, and v | conceito: Threat Representation Models (mechanism `ACM-TMR-001`) |

---

## EU GDPR (RGPD)

**O que esta ES traz para este capítulo:** contribui 1 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `GDPR-ART-5` | GDPR Article 5. Article 5 (Principles relating to processing of personal data) requires that personal data shall be: | conceito: Secret Management Systems (mechanism `ACM-SPC-001`) |

---

## OWASP Machine Learning Top 10

**O que esta ES traz para este capítulo:** contribui 1 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `ML05-2023` | ML05:2023 Model Theft. Description. Model theft attacks occur when an attacker gains access to the model’s parameters. How to Prevent. Encryption: Encrypting the model’s code, training data, and other | conceito: Logging de eventos de segurança e audit trail (slice `ACO-SLG`) |

---

## OWASP Top 10 (2021)

**O que esta ES traz para este capítulo:** contribui 1 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `TOP10-A09-2021` | Security Logging and Monitoring Failures. This category is to help detect, escalate, and respond to active breaches. Without logging and monitoring, breaches cannot be detected. Insufficient logging, | conceito: Logging de eventos de segurança e audit trail (slice `ACO-SLG`) |

---

## PCI Secure SLC v1.1

**O que esta ES traz para este capítulo:** contribui 1 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `PCISSLC-6.1` | Integrity of all software code maintained throughout lifecycle. Process, mechanism and/or tools to protect integrity of software code including third-party components; unauthorized access detected and | conceito: Artifact Signing And Attestation (mechanism `ACM-SCBI-004`) |

---
