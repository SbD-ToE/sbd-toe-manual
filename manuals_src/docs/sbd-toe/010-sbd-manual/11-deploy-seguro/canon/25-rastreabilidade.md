# 25. Rastreabilidade — Deploy Seguro

## Sumário

Este capítulo trata de **release promotion e deploy controlado** —
gates de promoção, rollback, readiness checks, exposição runtime
minimizada. As fontes externas seguintes contribuem para esta área:

- **NIST SP 800-53 Rev. 5** — 124 referência(s)
- **MITRE CAPEC v3.9** — 49 referência(s)
- **PCI DSS v4.0.1** — 47 referência(s)
- **OWASP DSOMM** — 39 referência(s)
- **CIS Controls v8.1.2** — 21 referência(s)
- **OWASP ASVS v5.0.0** — 13 referência(s)
- **NIST SSDF (SP 800-218 v1.1)** — 13 referência(s)
- **SAFECode — Practical Security Stories and Tasks for Agile Development (2012)** — 11 referência(s)
- **OWASP SAMM v2.1** — 9 referência(s)
- **MITRE CWE — Software Development View (v4.19.1)** — 8 referência(s)
- **MITRE ATLAS — Adversarial Threat Landscape for AI Systems** — 4 referência(s)
- **PCI Secure SLC v1.1** — 4 referência(s)
- **SLSA Specification v1.0 — Build Track** — 4 referência(s)
- **HIPAA Security Rule** — 2 referência(s)
- **OWASP Top 10 (2021)** — 2 referência(s)
- **SAFECode — Fundamental Practices for Secure Software Development (2018)** — 2 referência(s)
- **SAFECode — Software Integrity Controls (2010)** — 2 referência(s)
- **ENISA — Multilayer AI Cybersecurity Practices (2023)** — 1 referência(s)
- **EU Digital Operational Resilience Act (DORA)** — 1 referência(s)
- **NIST AI 100-2 e2025 — Adversarial Machine Learning Taxonomy** — 1 referência(s)
- **NIST AI RMF 1.0** — 1 referência(s)

---

## NIST SP 800-53 Rev. 5

**O que esta ES traz para este capítulo:** contribui 124 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `SP800-53-AC-18.3` | Disable Wireless Networking. Disable, when not intended for use, wireless networking capabilities embedded within system components prior to issuance and deployment. | conceito: Transport And Protocol Hardening (practice `ACP-ITS-003`) |
| `SP800-53-AC-3.9` | Controlled Release. Release information outside of the system only if: The receiving [system or system component] provides [controls]; and [controls] are used to validate the appropriateness of the in | conceito: Least-Privilege Authorization Governance (practice `ACP-IAT-002`) |
| `SP800-53-AC-4.23` | Modify Non-releasable Information. When transferring information between different security domains, modify non-releasable information by implementing [modification action]. | conceito: Trust-Boundary And Flow Review (practice `ACP-ATB-003`) |
| `SP800-53-AC-9.3` | Notification of Account Changes. Notify the user, upon successful logon, of changes to [security-related characteristics or parameters] during [time period]. | conceito: Access Abuse Monitoring And Audit Trail (practice `ACP-IAT-006`) |
| `SP800-53-AT-5` | Contacts with Security Groups and Associations | conceito: Identidade, autenticação e gestão de sessões (slice `ACO-IAT`) |
| `SP800-53-AU-1` | Policy and Procedures. Develop, document, and disseminate to [organization-defined personnel or roles]: audit and accountability policy that: Addresses purpose, scope, roles, responsibilities, managem | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `SP800-53-AU-10` | Non-repudiation. Provide irrefutable evidence that an individual (or process acting on behalf of an individual) has performed [actions]. | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `SP800-53-AU-10.4` | Validate Binding of Information Reviewer Identity. Validate the binding of the information reviewer identity to the information at the transfer or release points prior to release or transfer between [ | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `SP800-53-AU-6` | Audit Record Review, Analysis, and Reporting. Review and analyze system audit records [frequency] for indications of [inappropriate or unusual activity] and the potential impact of the inappropriate o | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `SP800-53-AU-6.10` | Audit Level Adjustment | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `SP800-53-AU-6.9` | Correlation with Information from Nontechnical Sources. Correlate information from nontechnical sources with audit record information to enhance organization-wide situational awareness. | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `SP800-53-CM-10.1` | Open-source Software. Establish the following restrictions on the use of open-source software: [restrictions]. | conceito: Approved Source And Registry Governance (practice `ACP-SCBI-003`) |
| `SP800-53-CM-11.1` | Alerts for Unauthorized Installations | conceito: Approved Source And Registry Governance (practice `ACP-SCBI-003`) |
| `SP800-53-CM-2` | Baseline Configuration. Develop, document, and maintain under configuration control, a current baseline configuration of the system | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `SP800-53-CM-2.1` | Reviews and Updates | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `SP800-53-CM-2.3` | Retention of Previous Configurations. Retain [number] of previous versions of baseline configurations of the system to support rollback. | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `SP800-53-CM-2.4` | Unauthorized Software | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `SP800-53-CM-2.5` | Authorized Software | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `SP800-53-CM-2.6` | Development and Test Environments. Maintain a baseline configuration for system development and test environments that is managed separately from the operational baseline configuration. | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `SP800-53-CM-2.7` | Configure Systems | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `SP800-53-CM-3` | Configuration Change Control. Determine and document the types of changes to the system that are configuration-controlled | conceito: Accountable Release Approval (practice `ACP-RPR-001`) |
| `SP800-53-CM-3.3` | Automated Change Implementation. Implement changes to the current system baseline and deploy the updated baseline across the installed base using [automated mechanisms]. | conceito: Accountable Release Approval (practice `ACP-RPR-001`) |
| `SP800-53-CM-3.4` | Security and Privacy Representatives. Require [organization-defined security and privacy representatives] to be members of the [configuration change control element]. | conceito: Accountable Release Approval (practice `ACP-RPR-001`) |
| `SP800-53-CM-3.5` | Automated Security Response. Implement the following security responses automatically if baseline configurations are changed in an unauthorized manner: [security responses]. | conceito: Accountable Release Approval (practice `ACP-RPR-001`) |
| `SP800-53-CM-3.7` | Review System Changes. Review changes to the system [frequency] or when [circumstances] to determine whether unauthorized changes have occurred. | conceito: Accountable Release Approval (practice `ACP-RPR-001`) |
| `SP800-53-CM-3.8` | Prevent or Restrict Configuration Changes. Prevent or restrict changes to the configuration of the system under the following circumstances: [circumstances]. | conceito: Accountable Release Approval (practice `ACP-RPR-001`) |
| `SP800-53-CM-4` | Impact Analyses. Analyze changes to the system to determine potential security and privacy impacts prior to change implementation. | conceito: Staged Dynamic Testing And Gate Enforcement (practice `ACP-TSV-005`) |
| `SP800-53-CM-4.2` | Verification of Controls. After system changes, verify that the impacted controls are implemented correctly, operating as intended, and producing the desired outcome with regard to meeting the securit | conceito: Staged Dynamic Testing And Gate Enforcement (practice `ACP-TSV-005`) |
| `SP800-53-CM-5` | Define, document, approve | conceito: Least-Privilege Authorization Governance (practice `ACP-IAT-002`) |
| `SP800-53-CM-5.2` | Review System Changes | conceito: Least-Privilege Authorization Governance (practice `ACP-IAT-002`) |
| `SP800-53-CM-5.3` | Signed Components | conceito: Least-Privilege Authorization Governance (practice `ACP-IAT-002`) |
| `SP800-53-CM-5.5` | Privilege Limitation for Production and Operation. Limit privileges to change system components and system-related information within a production or operational environment; and Review and reevaluate | conceito: Least-Privilege Authorization Governance (practice `ACP-IAT-002`) |
| `SP800-53-CM-5.6` | Limit Library Privileges. Limit privileges to change software resident within software libraries. | conceito: Least-Privilege Authorization Governance (practice `ACP-IAT-002`) |
| `SP800-53-CM-5.7` | Automatic Implementation of Security Safeguards | conceito: Least-Privilege Authorization Governance (practice `ACP-IAT-002`) |
| `SP800-53-CM-6` | Configuration Settings. Establish and document configuration settings for components employed within the system that reflect the most restrictive mode consistent with operational requirements using [c | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `SP800-53-CM-6.1` | Manage, apply | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `SP800-53-CM-6.2` | Respond to Unauthorized Changes. Take the following actions in response to unauthorized changes to [configuration settings]: [actions]. | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `SP800-53-CM-6.3` | Unauthorized Change Detection | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `SP800-53-CM-6.4` | Conformance Demonstration | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `SP800-53-CM-7.2` | Prevent Program Execution. Prevent program execution in accordance with. | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `SP800-53-CM-7.4` | Unauthorized Software — Deny-by-exception. Identify [software programs] | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `SP800-53-CM-7.5` | Authorized Software — Allow-by-exception. Identify [software programs] | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `SP800-53-CM-7.6` | Confined Environments with Limited Privileges. Require that the following user-installed software execute in a confined physical or virtual machine environment with limited privileges: [user-installed | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `SP800-53-CM-7.7` | Code Execution in Protected Environments. Allow execution of binary or machine-executable code only in confined physical or virtual machine environments and with the explicit approval of [personnel or | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `SP800-53-CM-7.8` | Binary or Machine Executable Code. Prohibit the use of binary or machine-executable code from sources with limited or no warranty or without the provision of source code; and Allow exceptions only for | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `SP800-53-CM-7.9` | Prohibiting The Use of Unauthorized Hardware. Identify [hardware components] | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `SP800-53-CM-8` | System Component Inventory. Develop and document an inventory of system components that: Accurately reflects the system | conceito: Build-Linked SBOM Generation (practice `ACP-SCBI-001`) |
| `SP800-53-CM-8.5` | No Duplicate Accounting of Components | conceito: Build-Linked SBOM Generation (practice `ACP-SCBI-001`) |
| `SP800-53-CP-10.2` | Transaction Recovery. Implement transaction recovery for systems that are transaction-based. | conceito: Release promotion, rollout controlado e readiness para rollback (slice `ACO-RPR`) |
| `SP800-53-CP-10.3` | Compensating Security Controls. Addressed through tailoring. | conceito: Release promotion, rollout controlado e readiness para rollback (slice `ACO-RPR`) |
| `SP800-53-CP-10.4` | Restore Within Time Period. Provide the capability to restore system components within [restoration time periods] from configuration-controlled and integrity-protected information representing a known | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `SP800-53-CP-10.6` | Component Protection. Protect system components used for recovery and reconstitution. | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `SP800-53-CP-12` | Safe Mode. When [conditions] are detected, enter a safe mode of operation with [restrictions]. | conceito: Release promotion, rollout controlado e readiness para rollback (slice `ACO-RPR`) |
| `SP800-53-CP-13` | Alternative Security Mechanisms. Employ [alternative or supplemental security mechanisms] for satisfying [security functions] when the primary means of implementing the security function is unavailabl | conceito: Release promotion, rollout controlado e readiness para rollback (slice `ACO-RPR`) |
| `SP800-53-CP-2` | Contingency Plan. Develop a contingency plan for the system that: Identifies essential mission and business functions and associated contingency requirements | conceito: Identidade, autenticação e gestão de sessões (slice `ACO-IAT`) |
| `SP800-53-CP-2.5` | Continue Mission and Business Functions. Plan for the continuance of mission and business functions with minimal or no loss of operational continuity and sustains that continuity until full system res | conceito: Gestão de segredos, configuração protegida e identidades operacionais (slice `ACO-SPC`) |
| `SP800-53-CP-2.6` | Alternate Processing and Storage Sites. Plan for the transfer of mission and business functions to alternate processing and/or storage sites with minimal or no loss of operational continuity and susta | conceito: Gestão de segredos, configuração protegida e identidades operacionais (slice `ACO-SPC`) |
| `SP800-53-CP-4.4` | Full Recovery and Reconstitution. Include a full recovery and reconstitution of the system to a known state as part of contingency plan testing. | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `SP800-53-CP-9.2` | Test Restoration Using Sampling. Use a sample of backup information in the restoration of selected system functions as part of contingency plan testing. | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `SP800-53-IA-12.3` | Identity Evidence Validation and Verification. Require that the presented identity evidence be validated and verified through [methods of validation and verification]. | conceito: Strong Authentication And Step-Up Enforcement (practice `ACP-IAT-001`) |
| `SP800-53-IA-3.4` | Device Attestation. Handle device identification and authentication based on attestation by [configuration management process]. | conceito: Strong Authentication And Step-Up Enforcement (practice `ACP-IAT-001`) |
| `SP800-53-IR-4` | Incident Handling. Implement an incident handling capability for incidents that is consistent with the incident response plan and includes preparation, detection and analysis, containment, eradication | conceito: Identidade, autenticação e gestão de sessões (slice `ACO-IAT`) |
| `SP800-53-IR-4.14` | Security Operations Center. Establish and maintain a security operations center. | conceito: Release promotion, rollout controlado e readiness para rollback (slice `ACO-RPR`) |
| `SP800-53-IR-4.2` | Dynamic Reconfiguration. Include the following types of dynamic reconfiguration for [system components] as part of the incident response capability: [types of dynamic reconfiguration]. | conceito: Gestão de segredos, configuração protegida e identidades operacionais (slice `ACO-SPC`) |
| `SP800-53-IR-4.3` | Continuity of Operations. Identify [classes of incidents] and take the following actions in response to those incidents to ensure continuation of organizational mission and business functions: [action | conceito: Release promotion, rollout controlado e readiness para rollback (slice `ACO-RPR`) |
| `SP800-53-IR-4.5` | Automatic Disabling of System. Implement a configurable capability to automatically disable the system if [security violations] are detected. | conceito: Release promotion, rollout controlado e readiness para rollback (slice `ACO-RPR`) |
| `SP800-53-IR-5` | Incident Monitoring. Track and document incidents. | conceito: Release promotion, rollout controlado e readiness para rollback (slice `ACO-RPR`) |
| `SP800-53-IR-9.3` | Post-spill Operations. Implement the following procedures to ensure that organizational personnel impacted by information spills can continue to carry out assigned tasks while contaminated systems are | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `SP800-53-MA-1` | Policy and Procedures. Develop, document, and disseminate to [organization-defined personnel or roles]: maintenance policy that: Addresses purpose, scope, roles, responsibilities, management commitmen | conceito: Identidade, autenticação e gestão de sessões (slice `ACO-IAT`) |
| `SP800-53-MA-2` | Controlled Maintenance. Schedule, document, and review records of maintenance, repair, and replacement on system components in accordance with manufacturer or vendor specifications and/or organization | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `SP800-53-MA-3` | Approve, control | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `SP800-53-MA-3.6` | Software Updates and Patches. Inspect maintenance tools to ensure the latest software updates and patches are installed. | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `SP800-53-MA-4.3` | Comparable Security and Sanitization. Require that nonlocal maintenance and diagnostic services be performed from a system that implements a security capability comparable to the capability implemente | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `SP800-53-MA-5.5` | Non-system Maintenance. Ensure that non-escorted personnel performing maintenance activities not directly associated with the system but in the physical proximity of the system, have required access a | conceito: Identidade, autenticação e gestão de sessões (slice `ACO-IAT`) |
| `SP800-53-MA-7` | Field Maintenance. Restrict or prohibit field maintenance on [systems or system components] to [trusted maintenance facilities]. | conceito: Integração e segurança service-to-service (slice `ACO-ITS`) |
| `SP800-53-MP-3` | Media Marking. Mark system media indicating the distribution limitations, handling caveats, and applicable security markings (if any) of the information; and Exempt [types of media exempted from marki | conceito: Release promotion, rollout controlado e readiness para rollback (slice `ACO-RPR`) |
| `SP800-53-MP-8.3` | Controlled Unclassified Information. Downgrade system media containing controlled unclassified information prior to public release. | conceito: Release promotion, rollout controlado e readiness para rollback (slice `ACO-RPR`) |
| `SP800-53-PE-1` | Policy and Procedures. Develop, document, and disseminate to [organization-defined personnel or roles]: physical and environmental protection policy that: Addresses purpose, scope, roles, responsibili | conceito: Identidade, autenticação e gestão de sessões (slice `ACO-IAT`) |
| `SP800-53-PL-3` | System Security Plan Update | conceito: Release promotion, rollout controlado e readiness para rollback (slice `ACO-RPR`) |
| `SP800-53-PM-1` | Information Security Program Plan. Develop and disseminate an organization-wide information security program plan that: Provides an overview of the requirements for the security program and a descript | conceito: Identidade, autenticação e gestão de sessões (slice `ACO-IAT`) |
| `SP800-53-PM-21` | Accounting of Disclosures. Develop and maintain an accurate accounting of disclosures of personally identifiable information, including: Date, nature, and purpose of each disclosure | conceito: Identidade, autenticação e gestão de sessões (slice `ACO-IAT`) |
| `SP800-53-PM-24` | Data Integrity Board. Establish a Data Integrity Board to: Review proposals to conduct or participate in a matching program; and Conduct an annual review of all matching programs in which the agency h | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `SP800-53-PS-1` | Policy and Procedures. Develop, document, and disseminate to [organization-defined personnel or roles]: personnel security policy that: Addresses purpose, scope, roles, responsibilities, management co | conceito: Identidade, autenticação e gestão de sessões (slice `ACO-IAT`) |
| `SP800-53-PT-2` | Authority to Process Personally Identifiable Information. Determine and document the [authority] that permits the [processing] of personally identifiable information; and Restrict the [processing] of | conceito: Gestão de segredos, configuração protegida e identidades operacionais (slice `ACO-SPC`) |
| `SP800-53-PT-6.1` | Routine Uses. Review all routine uses published in the system of records notice at [frequency] to ensure continued accuracy, and to ensure that routine uses continue to be compatible with the purpose | conceito: Gestão de segredos, configuração protegida e identidades operacionais (slice `ACO-SPC`) |
| `SP800-53-RA-5.8` | Review Historic Audit Logs. Review historic audit logs to determine if a vulnerability identified in a [system] has been previously exploited within an [time period]. | conceito: Staged Dynamic Testing And Gate Enforcement (practice `ACP-TSV-005`) |
| `SP800-53-SA-10` | Developer Configuration Management. Require the developer of the system, system component, or system service to: Perform configuration management during system, component, or service | conceito: Pipeline Definition As Reviewed Code (practice `ACP-SCBI-004`) |
| `SP800-53-SA-10.7` | Security and Privacy Representatives. Require [organization-defined security and privacy representatives] to be included in the [organization-defined configuration change management and control proces | conceito: Pipeline Definition As Reviewed Code (practice `ACP-SCBI-004`) |
| `SP800-53-SA-12.9` | Operations Security | conceito: Automated Dependency And Image Risk Gating (practice `ACP-SCBI-002`) |
| `SP800-53-SA-15.8` | Reuse of Threat and Vulnerability Information. Require the developer of the system, system component, or system service to use threat modeling and vulnerability analyses from similar systems, componen | conceito: Pipeline Definition As Reviewed Code (practice `ACP-SCBI-004`) |
| `SP800-53-SA-19.1` | Anti-counterfeit Training | conceito: Artifact Signature And Provenance Validation (practice `ACP-SCBI-006`) |
| `SP800-53-SA-19.2` | Configuration Control for Component Service and Repair | conceito: Artifact Signature And Provenance Validation (practice `ACP-SCBI-006`) |
| `SP800-53-SA-3.1` | Manage Preproduction Environment. Protect system preproduction environments commensurate with risk throughout the system development life cycle for the system, system component, or system service. | conceito: DFD And Trust-Boundary Grounding (practice `ACP-TMR-002`) |
| `SP800-53-SA-4.5` | System, Component, and Service Configurations. Require the developer of the system, system component, or system service to: Deliver the system, component, or service with [security configurations] imp | conceito: Trust Boundary And Integration Review (practice `ACP-ITS-001`) |
| `SP800-53-SA-8` | Security and Privacy Engineering Principles. Apply the following systems security and privacy engineering principles in the specification, design, development, implementation, and modification of the | conceito: Architectural Decision And Solution Traceability (practice `ACP-ATB-002`) |
| `SP800-53-SA-8.11` | Inverse Modification Threshold. Implement the security design principle of inverse modification threshold in [systems or system components]. | conceito: Architectural Decision And Solution Traceability (practice `ACP-ATB-002`) |
| `SP800-53-SA-8.12` | Hierarchical Protection. Implement the security design principle of hierarchical protection in [systems or system components]. | conceito: Architectural Decision And Solution Traceability (practice `ACP-ATB-002`) |
| `SP800-53-SA-8.13` | Minimized Security Elements. Implement the security design principle of minimized security elements in [systems or system components]. | conceito: Architectural Decision And Solution Traceability (practice `ACP-ATB-002`) |
| `SP800-53-SA-8.19` | Continuous Protection. Implement the security design principle of continuous protection in [systems or system components]. | conceito: Architectural Decision And Solution Traceability (practice `ACP-ATB-002`) |
| `SP800-53-SA-8.24` | Secure Failure and Recovery. Implement the security design principle of secure failure and recovery in [organization-defined systems or system components]. | conceito: Architectural Decision And Solution Traceability (practice `ACP-ATB-002`) |
| `SP800-53-SA-8.26` | Performance Security. Implement the security design principle of performance security in [systems or system components]. | conceito: Architectural Decision And Solution Traceability (practice `ACP-ATB-002`) |
| `SP800-53-SA-8.28` | Acceptable Security. Implement the security design principle of acceptable security in [systems or system components]. | conceito: Architectural Decision And Solution Traceability (practice `ACP-ATB-002`) |
| `SP800-53-SA-8.3` | Modularity and Layering. Implement the security design principles of modularity and layering in [organization-defined systems or system components]. | conceito: Architectural Decision And Solution Traceability (practice `ACP-ATB-002`) |
| `SP800-53-SA-8.30` | Procedural Rigor. Implement the security design principle of procedural rigor in [systems or system components]. | conceito: Architectural Decision And Solution Traceability (practice `ACP-ATB-002`) |
| `SP800-53-SA-8.31` | Secure System Modification. Implement the security design principle of secure system modification in [systems or system components]. | conceito: Architectural Decision And Solution Traceability (practice `ACP-ATB-002`) |
| `SP800-53-SC-16.2` | Anti-spoofing Mechanisms. Implement anti-spoofing mechanisms to prevent adversaries from falsifying the security attributes indicating the successful application of the security process. | conceito: Message Integrity And Authorized Peer Validation (practice `ACP-ITS-004`) |
| `SP800-53-SC-18.5` | Allow Execution Only in Confined Environments. Allow execution of permitted mobile code only in confined virtual machine environments. | conceito: Dangerous Pattern Exclusion (practice `ACP-IVF-003`) |
| `SP800-53-SC-34` | Non-modifiable Executable Programs. For [system components] , load and execute: The operating environment from hardware-enforced, read-only media; and The following applications from hardware-enforced | conceito: Pipeline Definition As Reviewed Code (practice `ACP-SCBI-004`) |
| `SP800-53-SC-51` | Hardware-based Protection. Employ hardware-based, write-protect for [system firmware components]; and Implement specific procedures for [authorized individuals] to manually disable hardware write-prot | conceito: Trust-Boundary And Flow Review (practice `ACP-ATB-003`) |
| `SP800-53-SC-7.16` | Prevent Discovery of System Components. Prevent the discovery of specific system components that represent a managed interface. | conceito: External Exposure And Boundary Mediation Design (practice `ACP-ATB-004`) |
| `SP800-53-SI-18` | Personally Identifiable Information Quality Operations. Check the accuracy, relevance, timeliness, and completeness of personally identifiable information across the information life cycle [organizati | conceito: Operational Identity Binding And OIDC Use (practice `ACP-SPC-004`) |
| `SP800-53-SI-18.5` | Notice of Correction or Deletion. Notify [recipients] and individuals that the personally identifiable information has been corrected or deleted. | conceito: Operational Identity Binding And OIDC Use (practice `ACP-SPC-004`) |
| `SP800-53-SI-19.3` | Release. Remove personally identifiable information elements from a dataset prior to its release if those elements in the dataset do not need to be part of the data release. | conceito: Operational Identity Binding And OIDC Use (practice `ACP-SPC-004`) |
| `SP800-53-SI-2` | Flaw Remediation. Identify, report, and correct system flaws | conceito: Automated Dependency And Image Risk Gating (practice `ACP-SCBI-002`) |
| `SP800-53-SI-2.3` | Time to Remediate Flaws and Benchmarks for Corrective Actions. Measure the time between flaw identification and flaw remediation; and Establish the following benchmarks for taking corrective actions: | conceito: Automated Dependency And Image Risk Gating (practice `ACP-SCBI-002`) |
| `SP800-53-SI-2.5` | Automatic Software and Firmware Updates. Install [security-relevant software and firmware updates] automatically to [system components]. | conceito: Automated Dependency And Image Risk Gating (practice `ACP-SCBI-002`) |
| `SP800-53-SI-3.4` | Updates Only by Privileged Users. Update malicious code protection mechanisms only when directed by a privileged user. | conceito: Automated Dependency And Image Risk Gating (practice `ACP-SCBI-002`) |
| `SP800-53-SI-4.21` | Probationary Periods. Implement the following additional monitoring of individuals during [probationary period]: [additional monitoring]. | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `SP800-53-SI-7.10` | Protection of Boot Firmware. Implement the following mechanisms to protect the integrity of boot firmware in [system components]: [mechanisms]. | conceito: Artifact Signature And Provenance Validation (practice `ACP-SCBI-006`) |
| `SP800-53-SI-7.17` | Runtime Application Self-protection. Implement [controls] for application self-protection at runtime. | conceito: Artifact Signature And Provenance Validation (practice `ACP-SCBI-006`) |
| `SP800-53-SI-7.5` | Automated Response to Integrity Violations. Automatically when integrity violations are discovered. | conceito: Artifact Signature And Provenance Validation (practice `ACP-SCBI-006`) |
| `SP800-53-SR-1` | Policy and Procedures. Develop, document, and disseminate to [organization-defined personnel or roles]: supply chain risk management policy that: Addresses purpose, scope, roles, responsibilities, man | conceito: Approved Source And Registry Governance (practice `ACP-SCBI-003`) |
| `SP800-53-SR-11.2` | Configuration Control for Component Service and Repair. Maintain configuration control over the following system components awaiting service or repair and serviced or repaired components awaiting retu | conceito: Artifact Signature And Provenance Validation (practice `ACP-SCBI-006`) |
| `SP800-53-SR-12` | Component Disposal. Dispose of [data, documentation, tools, or system components] using the following techniques and methods: [techniques and methods]. | conceito: Build-Linked SBOM Generation (practice `ACP-SCBI-001`) |

---

## MITRE CAPEC v3.9

**O que esta ES traz para este capítulo:** contribui 49 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `CAPEC-165` | File Manipulation. File Manipulation. An attacker modifies file contents or attributes (such as extensions or names) of files in a manner to cause incorrect processing by an application. Attackers use | conceito: Code Review For Input And Error Discipline (mechanism `ACM-IVF-001`) |
| `CAPEC-166` | Force the System to Reset Values. Force the System to Reset Values. An attacker forces the target into a previous state in order to leverage potential weaknesses in the target dependent upon a prior c | conceito: Trust-Boundary And DFD Modeling (mechanism `ACM-ATB-002`) |
| `CAPEC-176` | Configuration/Environment Manipulation. Configuration/Environment Manipulation. An attacker manipulates files or settings external to a target application which affect the behavior of that application | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `CAPEC-180` | Exploiting Incorrectly Configured Access Control Security Levels. Exploiting Incorrectly Configured Access Control Security Levels. An attacker exploits a weakness in the configuration of access contr | conceito: Access Policy Enforcement (mechanism `ACM-IAT-002`) |
| `CAPEC-212` | Functionality Misuse. Functionality Misuse. An adversary leverages a legitimate capability of an application in such a way as to achieve a negative technical impact. The system functionality is not al | conceito: Access Policy Enforcement (mechanism `ACM-IAT-002`) |
| `CAPEC-270` | Modification of Registry Run Keys. Modification of Registry Run Keys. An adversary adds a new entry to the "run keys" in the Windows registry so that an application of their choosing is executed when | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `CAPEC-35` | Leverage Executable Code in Non-Executable Files. Leverage Executable Code in Non-Executable Files. An attack of this type exploits a system's trust in configuration and resource files. When the execu | conceito: Code Review For Input And Error Discipline (mechanism `ACM-IVF-001`) |
| `CAPEC-38` | Leveraging/Manipulating Configuration File Search Paths. Leveraging/Manipulating Configuration File Search Paths. This pattern of attack sees an adversary load a malicious resource into a program's st | conceito: Approved Source And Registry Governance (practice `ACP-SCBI-003`) |
| `CAPEC-417` | Influence Perception. Influence Perception. The adversary uses social engineering to exploit the target's perception of the relationship between the adversary and themselves. This goal is to persuade | conceito: Authentication And Federation Protocols (mechanism `ACM-IAT-001`) |
| `CAPEC-421` | Influence Perception of Authority. Influence Perception of Authority. An adversary uses a social engineering technique to convey a sense of authority that motivates the target to reveal specific infor | conceito: Authentication And Federation Protocols (mechanism `ACM-IAT-001`) |
| `CAPEC-438` | Modification During Manufacture. Modification During Manufacture. An attacker modifies a technology, product, or component during a stage in its manufacture for the purpose of carrying out an attack a | conceito: Release promotion, rollout controlado e readiness para rollback (slice `ACO-RPR`) |
| `CAPEC-439` | Manipulation During Distribution. Manipulation During Distribution. An attacker undermines the integrity of a product, software, or technology at some stage of the distribution channel. The core threa | conceito: Artifact Signing And Attestation (mechanism `ACM-SCBI-004`) |
| `CAPEC-441` | Malicious Logic Insertion. Malicious Logic Insertion. An adversary installs or adds malicious logic (also known as malware) into a seemingly benign component of a fielded system. This logic is often h | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `CAPEC-443` | Malicious Logic Inserted Into Product by Authorized Developer. Malicious Logic Inserted Into Product by Authorized Developer. An adversary uses their privileged position within an authorized developme | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `CAPEC-445` | Malicious Logic Insertion into Product Software via Configuration Management Manipulation. Malicious Logic Insertion into Product Software via Configuration Management Manipulation. An adversary explo | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `CAPEC-446` | Malicious Logic Insertion into Product via Inclusion of Third-Party Component. Malicious Logic Insertion into Product via Inclusion of Third-Party Component. An adversary conducts supply chain attacks | conceito: Release promotion, rollout controlado e readiness para rollback (slice `ACO-RPR`) |
| `CAPEC-447` | Design Alteration. Design Alteration. An adversary modifies the design of a technology, product, or component to acheive a negative impact once the system is deployed. In this type of attack, the goal | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `CAPEC-478` | Modification of Windows Service Configuration. Modification of Windows Service Configuration. An adversary exploits a weakness in access control to modify the execution parameters of a Windows service | conceito: Release promotion, rollout controlado e readiness para rollback (slice `ACO-RPR`) |
| `CAPEC-511` | Infiltration of Software Development Environment. Infiltration of Software Development Environment. An attacker uses common delivery mechanisms such as email attachments or removable media to infiltra | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `CAPEC-516` | Hardware Component Substitution During Baselining. Hardware Component Substitution During Baselining. An adversary with access to system components during allocated baseline development can substitute | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `CAPEC-517` | Documentation Alteration to Circumvent Dial-down. Documentation Alteration to Circumvent Dial-down. An attacker with access to a manufacturer's documentation, which include descriptions of advanced te | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `CAPEC-519` | Documentation Alteration to Cause Errors in System Design. Documentation Alteration to Cause Errors in System Design. An attacker with access to a manufacturer's documentation containing requirements | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `CAPEC-521` | Hardware Design Specifications Are Altered. Hardware Design Specifications Are Altered. An attacker with access to a manufacturer's hardware manufacturing process documentation alters the design speci | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `CAPEC-522` | Malicious Hardware Component Replacement. Malicious Hardware Component Replacement. An adversary replaces legitimate hardware in the system with faulty counterfeit or tampered hardware in the supply c | conceito: Release promotion, rollout controlado e readiness para rollback (slice `ACO-RPR`) |
| `CAPEC-533` | Malicious Manual Software Update. Malicious Manual Software Update. An attacker introduces malicious code to the victim's system by altering the payload of a software update, allowing for additional c | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `CAPEC-534` | Malicious Hardware Update. Malicious Hardware Update. An adversary introduces malicious hardware during an update or replacement procedure, allowing for additional compromise or site disruption at the | conceito: Release promotion, rollout controlado e readiness para rollback (slice `ACO-RPR`) |
| `CAPEC-536` | Data Injected During Configuration. Data Injected During Configuration. An attacker with access to data files and processes on a victim's system injects malicious data into critical operational data d | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `CAPEC-537` | Infiltration of Hardware Development Environment. Infiltration of Hardware Development Environment. An adversary, leveraging the ability to manipulate components of primary support systems and tools w | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `CAPEC-539` | ASIC With Malicious Functionality. ASIC With Malicious Functionality. An attacker with access to the development environment process of an application-specific integrated circuit (ASIC) for a victim s | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `CAPEC-551` | Modify Existing Service. Modify Existing Service. When an operating system starts, it also starts programs called services or daemons. Modifying existing services may break existing services or may en | conceito: Code Review For Input And Error Discipline (mechanism `ACM-IVF-001`) |
| `CAPEC-552` | Install Rootkit. Install Rootkit . An adversary exploits a weakness in authentication to install malware that alters the functionality and information provide by targeted operating system API calls. O | conceito: Code Review For Input And Error Discipline (mechanism `ACM-IVF-001`) |
| `CAPEC-558` | Replace Trusted Executable. Replace Trusted Executable. An adversary exploits weaknesses in privilege management or access control to replace a trusted executable with a malicious version and enable t | conceito: Release promotion, rollout controlado e readiness para rollback (slice `ACO-RPR`) |
| `CAPEC-562` | Modify Shared File. Modify Shared File. An adversary manipulates the files in a shared location by adding malicious programs, scripts, or exploit code to valid content. Once a user opens the shared co | conceito: Access Policy Enforcement (mechanism `ACM-IAT-002`) |
| `CAPEC-578` | Disable Security Software. Disable Security Software. An adversary exploits a weakness in access control to disable security tools so that detection does not occur. This can take the form of killing p | conceito: Release promotion, rollout controlado e readiness para rollback (slice `ACO-RPR`) |
| `CAPEC-583` | Disabling Network Hardware. Disabling Network Hardware. In this attack pattern, an adversary physically disables networking hardware by powering it down or disconnecting critical equipment. Disabling | conceito: API Gateway With Mutual Authentication (mechanism `ACM-ITS-001`) |
| `CAPEC-638` | Altered Component Firmware. Altered Component Firmware. An adversary exploits systems features and/or improperly protected firmware of hardware components, such as Hard Disk Drives (HDD), with the goa | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `CAPEC-640` | Inclusion of Code in Existing Process. Inclusion of Code in Existing Process. The adversary takes advantage of a bug in an application failing to verify the integrity of the running process to execute | conceito: Release promotion, rollout controlado e readiness para rollback (slice `ACO-RPR`) |
| `CAPEC-665` | Exploitation of Thunderbolt Protection Flaws. Exploitation of Thunderbolt Protection Flaws. An adversary leverages a firmware weakness within the Thunderbolt protocol, on a computing device to manipul | conceito: Message Integrity And Authorized Peer Policies (mechanism `ACM-ITS-004`) |
| `CAPEC-669` | Alteration of a Software Update. Alteration of a Software Update. An adversary with access to an organization’s software update infrastructure inserts malware into the content of an outgoing update to | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `CAPEC-670` | Software Development Tools Maliciously Altered. Software Development Tools Maliciously Altered. An adversary with the ability to alter tools used in a development environment causes software to be dev | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `CAPEC-673` | Developer Signing Maliciously Altered Software. Developer Signing Maliciously Altered Software. Software produced by a reputable developer is clandestinely infected with malicious code and then digita | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `CAPEC-674` | Design for FPGA Maliciously Altered. Design for FPGA Maliciously Altered. An adversary alters the functionality of a field-programmable gate array (FPGA) by causing an FPGA configuration memory chip r | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `CAPEC-678` | build processes is susceptible to deliberate misconfiguration of the system. | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `CAPEC-679` | Exploitation of Improperly Configured or Implemented Memory Protections. Exploitation of Improperly Configured or Implemented Memory Protections. An adversary takes advantage of missing or incorrectly | conceito: Access Policy Enforcement (mechanism `ACM-IAT-002`) |
| `CAPEC-68` | Subvert Code-signing Facilities. Subvert Code-signing Facilities. Many languages use code signing facilities to vouch for code's identity and to thus tie code to its assigned privileges within an envi | conceito: Access Policy Enforcement (mechanism `ACM-IAT-002`) |
| `CAPEC-681` | Exploitation of Improperly Controlled Hardware Security Identifiers. Exploitation of Improperly Controlled Hardware Security Identifiers. An adversary takes advantage of missing or incorrectly configu | conceito: Access Policy Enforcement (mechanism `ACM-IAT-002`) |
| `CAPEC-702` | Exploiting Incorrect Chaining or Granularity of Hardware Debug Components. Exploiting Incorrect Chaining or Granularity of Hardware Debug Components. An adversary exploits incorrect chaining or granul | conceito: Access Policy Enforcement (mechanism `ACM-IAT-002`) |
| `CAPEC-75` | Manipulating Writeable Configuration Files. Manipulating Writeable Configuration Files. Generally these are manually edited files that are not in the preview of the system administrators, any ability | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `CAPEC-77` | Manipulating User-Controlled Variables. Manipulating User-Controlled Variables. This attack targets user controlled variables (DEBUG=1, PHP Globals, and So Forth). An adversary can override variables | conceito: Short-Lived Token Controls (mechanism `ACM-IAT-004`) |

---

## PCI DSS v4.0.1

**O que esta ES traz para este capítulo:** contribui 47 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `PCI-1.2.1` | Configuration standards for NSC rulesets are: 1.2.1.a Examine the configuration standards for s. Configuration standards for NSC rulesets are: 1.2.1.a Examine the configuration standards for | conceito: Architecture Review Gates (mechanism `ACM-ATB-004`) |
| `PCI-1.2.6` | Security features are defined and 1.2.6.a Examine documentation that identifies all. Security features are defined and 1.2.6.a Examine documentation that identifies all | conceito: Versioned Diagrams And ADR Records (mechanism `ACM-ATB-001`) |
| `PCI-1.2.7` | Configurations of NSCs are reviewed at least 1.2.7.a Examine documentation to verify. Configurations of NSCs are reviewed at least 1.2.7.a Examine documentation to verify opport | conceito: Trust-Boundary And DFD Modeling (mechanism `ACM-ATB-002`) |
| `PCI-1.5.1` | Security controls are implemented on any 1.5.1.a Examine policies and configuration. Security controls are implemented on any 1.5.1.a Examine policies and configuration the Int | conceito: Trust-Boundary And DFD Modeling (mechanism `ACM-ATB-002`) |
| `PCI-10.1.1` | All security policies and operational 10.1.1 Examine documentation and interview a. All security policies and operational 10.1.1 Examine documentation and interview | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `PCI-10.4.3` | Exceptions and anomalies identified during 10.4.3.a Examine security policies and procedures l. Exceptions and anomalies identified during 10.4.3.a Examine security policies and procedures | conceito: Machine-Readable Structured Logging (mechanism `ACM-SLG-001`) |
| `PCI-11.1.1` | All security policies and operational 11.1.1 Examine documentation and interview and. All security policies and operational 11.1.1 Examine documentation and interview a | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `PCI-11.5.2` | A change-detection mechanism (for example, 11.5.2.a Examine system settings, monitored file. A change-detection mechanism (for example, 11.5.2.a Examine system settings, monitored fi | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `PCI-11.6.1` | A change- and tamper-detection mechanism 11.6.1.a Examine system settings, monitored. A change- and tamper-detection mechanism 11.6.1.a Examine system settings, monitored | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `PCI-12.1.2` | The information security policy is: 12.1.2 Examine the information security policy an. The information security policy is: 12.1.2 Examine the information security policy | conceito: Threat Mitigation Linkage Controls (mechanism `ACM-TMR-005`) |
| `PCI-12.1.3` | The security policy clearly defines 12.1.3.a Examine the information security policy. The security policy clearly defines 12.1.3.a Examine the information security policy | conceito: Threat Model Versioning Controls (mechanism `ACM-TMR-003`) |
| `PCI-12.10.2` | At least once every 12 months, the security 12.10.2 Interview personnel and review. At least once every 12 months, the security 12.10.2 Interview personnel and review plan can iden | conceito: Explicit Threat Disposition Register (mechanism `ACM-TMR-004`) |
| `PCI-12.10.4` | Personnel responsible for responding to 12.10.4 Examine training documentation and. Personnel responsible for responding to 12.10.4 Examine training documentation and respo | conceito: Threat Model Versioning Controls (mechanism `ACM-TMR-003`) |
| `PCI-12.10.7` | Incident response procedures are in place, 12.10.7.a Examine documented incident response. Incident response procedures are in place, 12.10.7.a Examine documented incident response | conceito: Threat Model Versioning Controls (mechanism `ACM-TMR-003`) |
| `PCI-12.2.1` | Acceptable use policies for end-user 12.2.1 Examine the acceptable use policies for inv. Acceptable use policies for end-user 12.2.1 Examine the acceptable use policies for i | conceito: Structured Threat Analysis Frameworks (mechanism `ACM-TMR-002`) |
| `PCI-12.8.3` | An established process is implemented for 12.8.3.a Examine policies and procedures to verify in. An established process is implemented for 12.8.3.a Examine policies and procedures to verify | conceito: Explicit Threat Disposition Register (mechanism `ACM-TMR-004`) |
| `PCI-2.1.1` | All security policies and operational 2.1.1 Examine documentation and interview. All security policies and operational 2.1.1 Examine documentation and interview and ma | conceito: Release Promotion Controls (mechanism `ACM-RPR-001`) |
| `PCI-2.2.1` | Configuration standards are developed, 2.2.1.a Examine system configuration standards. Configuration standards are developed, 2.2.1.a Examine system configuration standards opera | conceito: Release Promotion Controls (mechanism `ACM-RPR-001`) |
| `PCI-2.2.2` | Vendor default accounts are managed as 2.2.2.a Examine system configuration standards to. Vendor default accounts are managed as 2.2.2.a Examine system configuration standards | conceito: Release Promotion Controls (mechanism `ACM-RPR-001`) |
| `PCI-2.2.3` | Primary functions requiring different security 2.2.3.a Examine system configuration standards. Primary functions requiring different security 2.2.3.a Examine system configuration standards | conceito: Release Promotion Controls (mechanism `ACM-RPR-001`) |
| `PCI-2.2.4` | Only necessary services, protocols, daemons, 2.2.4.a Examine system configuration standards to. Only necessary services, protocols, daemons, 2.2.4.a Examine system configuration standards to | conceito: Release Promotion Controls (mechanism `ACM-RPR-001`) |
| `PCI-2.2.6` | System security parameters are configured to 2.2.6.a Examine system configuration standards to p. System security parameters are configured to 2.2.6.a Examine system configuration standards to | conceito: Release Promotion Controls (mechanism `ACM-RPR-001`) |
| `PCI-2.2.7` | All non-console administrative access is 2.2.7.a Examine system configuration standards to. All non-console administrative access is 2.2.7.a Examine system configuration standards to | conceito: Rollback And Containment Controls (mechanism `ACM-RPR-004`) |
| `PCI-2.3.1` | For wireless environments connected to the 2.3.1.a Examine policies and procedures and. For wireless environments connected to the 2.3.1.a Examine policies and procedures and | conceito: Release Promotion Controls (mechanism `ACM-RPR-001`) |
| `PCI-5.2.1` | An anti-malware solution | conceito: Build And Image Inventory Generation (mechanism `ACM-SCBI-005`) |
| `PCI-5.2.2` | The deployed anti-malware solution(s): 5.2.2 Examine vendor documentation and. The deployed anti-malware solution(s): 5.2.2 Examine vendor documentation and of malware t | conceito: Build And Image Inventory Generation (mechanism `ACM-SCBI-005`) |
| `PCI-5.2.3` | Any system components that are not at risk for 5.2.3.a Examine documented policies and. Any system components that are not at risk for 5.2.3.a Examine documented policies and curre | conceito: Build And Image Inventory Generation (mechanism `ACM-SCBI-005`) |
| `PCI-5.3.1` | The anti-malware solution | conceito: Build And Image Inventory Generation (mechanism `ACM-SCBI-005`) |
| `PCI-5.3.2` | The anti-malware solution(s): 5.3.2.a Examine anti-malware solution(s). The anti-malware solution(s): 5.3.2.a Examine anti-malware solution(s) but cu | conceito: Build And Image Inventory Generation (mechanism `ACM-SCBI-005`) |
| `PCI-5.3.5` | Anti-malware mechanisms cannot be disabled 5.3.5.a Examine anti-malware configurations, to. Anti-malware mechanisms cannot be disabled 5.3.5.a Examine anti-malware configurations, to a | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `PCI-6.1.1` | All security policies and operational 6.1.1 Examine documentation and interview. All security policies and operational 6.1.1 Examine documentation and interview mainta | conceito: Code Review For Input And Error Discipline (mechanism `ACM-IVF-001`) |
| `PCI-6.1.2` | Roles and responsibilities for performing 6.1.2.a Examine documentation to verify that. Roles and responsibilities for performing 6.1.2.a Examine documentation to verify that | conceito: Schema And Contract Validators (mechanism `ACM-IVF-003`) |
| `PCI-6.3.3` | All system components are protected from 6.3.3.a Examine policies and procedures to verify. All system components are protected from 6.3.3.a Examine policies and procedures to verify | conceito: Code Review For Input And Error Discipline (mechanism `ACM-IVF-001`) |
| `PCI-6.4.1` | For public-facing web applications, new threats 6.4.1 For public-facing web applications, ensure. For public-facing web applications, new threats 6.4.1 For public-facing web applications, ensu | conceito: Code Review For Input And Error Discipline (mechanism `ACM-IVF-001`) |
| `PCI-6.4.2` | For public-facing web applications, an 6.4.2 For public-facing web applications, examine. For public-facing web applications, an 6.4.2 For public-facing web applications, examine | conceito: Code Review For Input And Error Discipline (mechanism `ACM-IVF-001`) |
| `PCI-6.4.3` | All payment page scripts that are loaded and 6.4.3.a Examine policies and procedures to verify. All payment page scripts that are loaded and 6.4.3.a Examine policies and procedures to verify | conceito: Code Review For Input And Error Discipline (mechanism `ACM-IVF-001`) |
| `PCI-6.5.1` | Changes to all system components in the 6.5.1.a Examine documented change control. Changes to all system components in the 6.5.1.a Examine documented change control all cha | conceito: Code Review For Input And Error Discipline (mechanism `ACM-IVF-001`) |
| `PCI-6.5.3` | Pre-production environments are separated 6.5.3.a Examine policies and procedures to verify. Pre-production environments are separated 6.5.3.a Examine policies and procedures to verify | conceito: Code Review For Input And Error Discipline (mechanism `ACM-IVF-001`) |
| `PCI-6.5.4` | Roles and functions are separated between 6.5.4.a Examine policies and procedures to verify. Roles and functions are separated between 6.5.4.a Examine policies and procedures to verify | conceito: Code Review For Input And Error Discipline (mechanism `ACM-IVF-001`) |
| `PCI-7.1.1` | All security policies and operational 7.1.1 Examine documentation and interview. All security policies and operational 7.1.1 Examine documentation and interview and ma | conceito: Periodic Review And Access Audit (mechanism `ACM-IAT-003`) |
| `PCI-8.1.1` | All security policies and operational 8.1.1 Examine documentation and interview. All security policies and operational 8.1.1 Examine documentation and interview and main | conceito: Periodic Review And Access Audit (mechanism `ACM-IAT-003`) |
| `PCI-8.3.6` | If passwords/passphrases are used as 8.3.6 Examine system configuration settings to. If passwords/passphrases are used as 8.3.6 Examine system configuration settings to lin | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura |
| `PCI-8.3.7` | Individuals are not allowed to submit a new 8.3.7 Examine system configuration settings to. Individuals are not allowed to submit a new 8.3.7 Examine system configuration settings to effec | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura |
| `PCI-9.1.1` | All security policies and operational 9.1.1 Examine documentation and interview. All security policies and operational 9.1.1 Examine documentation and interview and ma | conceito: Release promotion, rollout controlado e readiness para rollback (slice `ACO-RPR`) |
| `PCI-REQ-1` | Install and Maintain Network Security Controls. Requirement 1: Install and Maintain Network Security Controls. Goal: Build and Maintain a Secure Network and Systems. | conceito: Trust-Boundary And DFD Modeling (mechanism `ACM-ATB-002`) |
| `PCI-REQ-2` | Apply Secure Configurations to All System Components. Requirement 2: Apply Secure Configurations to All System Components. Goal: Build and Maintain a Secure Network and Systems. | conceito: Release Promotion Controls (mechanism `ACM-RPR-001`) |
| `PCI-REQ-5` | Protect All Systems and Networks from Malicious Software. Requirement 5: Protect All Systems and Networks from Malicious Software. Goal: Maintain a Vulnerability Management Program. | conceito: Build And Image Inventory Generation (mechanism `ACM-SCBI-005`) |

---

## OWASP DSOMM

**O que esta ES traz para este capítulo:** contribui 39 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `DSOMM-ACTIVITY-03643CA203C2472B8E19956BF02FE9B7` | App. Hardening Level 2 (75%). App. Hardening Level 2 (75%) Using an insecure application might lead to a compromised application. This might lead to total data theft or data modification. Following fr | conceito: Code Review For Input And Error Discipline (mechanism `ACM-IVF-001`) |
| `DSOMM-ACTIVITY-066084C6113546359CC59E75C7C5459F` | Version control. Version control Use a _version control system_ like Github, Gitlab, Bitbucket, etc to version your source code. Also known as _source control_, _revision control_, or _source code man | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `DSOMM-ACTIVITY-0CB2626BFB0D4A0F968857F787310D97` | Blue/Green Deployment. Blue/Green Deployment A new artifact's version can have unknown defects. Using a blue/green deployment strategy increases application availability and reduces deployment risk by | conceito: Rollback And Containment Controls (mechanism `ACM-RPR-004`) |
| `DSOMM-ACTIVITY-0CB2C39A3CEC4353B3AB8D70DAF4C9D2` | Test for Patch Deployment Time. Test for Patch Deployment Time Automatic PRs for dependencies are overlooked resulting in known vulnerabilities in production artifacts. Test of the Patch Deployment Ti | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |
| `DSOMM-ACTIVITY-0EC92899A5CB4649984B2FB1D6C784AD` | Number of vulnerabilities/severity/layer. Number of vulnerabilities/severity/layer Communication can be performed in a simple way, e.g. text based during the build process. This activity depends on at | conceito: Findings Workflow And Exception Governance (mechanism `ACM-TSV-004`) |
| `DSOMM-ACTIVITY-11B3848EE9314146A35D35409ADA24EE` | Usage of security by default for components. Usage of security by default for components Components (images, libraries, applications) are not hardened. Hardening of components is important, specially | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `DSOMM-ACTIVITY-13AF12273DD14D4FA9E953DEB793C18F` | Test for Time to Patch. Test for Time to Patch Automatic PRs for dependencies are overlooked resulting in known vulnerabilities in production artifacts. Test of the Time to Patch (e.g. based on Mean T | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |
| `DSOMM-ACTIVITY-1B9281B948E24C019AC69DB9931C4885` | Information security targets are communicated. Information security targets are communicated Employees don't know their organizations security targets. Therefore security is not considered during deve | conceito: Explicit Threat Disposition Register (mechanism `ACM-TMR-004`) |
| `DSOMM-ACTIVITY-29318D6018CE452680EAF5928E49F639` | Secure headers. Secure headers Missing or misconfigured security headers can lead to various security vulnerabilities, e.g.: - Cross-Site Scripting (XSS) due to missing Content Security Policy - Click | conceito: Boundary Mediation Controls (mechanism `ACM-ATB-003`) |
| `DSOMM-ACTIVITY-3A94D55EFD8249969EB320D23FF2A873` | Applications are running in virtualized environments. Applications are running in virtualized environments Through a vulnerability in one service on a server, the attacker gains access to other servic | conceito: Trust-Boundary And DFD Modeling (mechanism `ACM-ATB-002`) |
| `DSOMM-ACTIVITY-3F63BDBCC75F4780A941E6AD42E894E1` | Approval by reviewing any new version. Approval by reviewing any new version An individual might forget to implement security measures to protect source code or infrastructure components. On each new | conceito: Release Promotion Gates (mechanism `ACM-SCBI-003`) |
| `DSOMM-ACTIVITY-44F2C8A94AAA4C72942D63F78B89F385` | Treatment of defects with high or critical severity. Treatment of defects with high or critical severity All security problems that are rated as "high" or "critical" must be fixed before the software | conceito: Findings Workflow And Exception Governance (mechanism `ACM-TSV-004`) |
| `DSOMM-ACTIVITY-4CAE98C2416344EDBB883C67C569533A` | App. Hardening Level 3. App. Hardening Level 3 Using an insecure application might lead to a compromised application. This might lead to total data theft or data modification. Following frameworks lik | conceito: Code Review For Input And Error Discipline (mechanism `ACM-IVF-001`) |
| `DSOMM-ACTIVITY-5786959D0C6F46A68E1CA32FF1A50222` | Signing of artifacts. Signing of artifacts To perform a push to a GitHub repository, you must be authenticated. It's important to note that GitHub does not verify if the authenticated user's email add | conceito: Artifact Signing And Attestation (mechanism `ACM-SCBI-004`) |
| `DSOMM-ACTIVITY-5992C38C8597403589DBD15820D81C3A` | Baseline Hardening of the environment. Baseline Hardening of the environment Using default configurations for a cluster environment leads to potential risks. Harden environments according to best prac | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `DSOMM-ACTIVITY-5C61FD6B81064C68AC28A8A42F1C67DC` | Backup. Backup If errors are experienced during the deployment process you want to deploy an old release. However, due to changes in the database this is often unfeasible. Performing automated periodi | conceito: Rollback And Containment Controls (mechanism `ACM-RPR-004`) |
| `DSOMM-ACTIVITY-621FB6A55C0A4408826A068868BB031B` | Test cluster deployment resources. Test cluster deployment resources The deployment configuration (e.g. kubernetes deployment resources) might contain unsecured configurations. Test the deployment con | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `DSOMM-ACTIVITY-67667C97C33E4306A4E5E7B1D8E10C5A` | High coverage of security related module and integration tests. High coverage of security related module and integration tests Vulnerabilities are rising due to code changes in a complex microservice | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `DSOMM-ACTIVITY-67E1A9AA9FBF4EC5A2DE400F01960C51` | Automated deployment process. Automated deployment process An *automated deployment process* implements the defined deployment steps using automation tools, ensuring consistency, auditability, and min | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `DSOMM-ACTIVITY-77FFC53E9F3D41F492D302F04F9B6B0F` | Patching mean time to resolution via production. Patching mean time to resolution via production Without measuring Mean Time to Resolution (MTTR) related to patching, it is challenging to identify del | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |
| `DSOMM-ACTIVITY-86D490B9D7984A5BA011AB9688014C46` | Patching mean time to resolution via PR. Patching mean time to resolution via PR Without measuring Mean Time to Resolution (MTTR) related to patching, it is challenging to identify delays in the patch | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |
| `DSOMM-ACTIVITY-8B994601575E4EA5B228ACCB18C8E514` | Infrastructure as Code. Infrastructure as Code No tracking of changes in systems might lead to errors in the configuration. In additions, it might lead to unauthorized changes. An examples is jenkins. | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `DSOMM-ACTIVITY-8F2B4D5A3C1E4B7A9D8F2E6C4A1B5D7F` | Artifact-based false positive treatment. Artifact-based false positive treatment Artifact-based false positive treatment enables more granular control over finding suppression by linking decisions to | conceito: Findings Workflow And Exception Governance (mechanism `ACM-TSV-004`) |
| `DSOMM-ACTIVITY-94A96F798BD6490497C0994FF88F176A` | Handover of confidential parameters. Handover of confidential parameters Parameters are often used to set credentials, for example by starting containers or applications; these parameters can often be | conceito: Secret Management Systems (mechanism `ACM-SPC-001`) |
| `DSOMM-ACTIVITY-9E3A7C2F1B4D4E8AA5C67F2B9D1E3A8C` | Global false positive treatment. Global false positive treatment Global false positive treatment allows (security) teams to make organization-wide decisions about specific vulnerabilities or finding p | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `DSOMM-ACTIVITY-A340F46B63604CB8847BA0D3483D09D3` | Building and testing of artifacts in virtual environments. Building and testing of artifacts in virtual environments While building and testing artifacts, third party systems, application frameworks a | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `DSOMM-ACTIVITY-A511799B045E4B9698437D63D8C1E2AD` | Usage of feature toggles. Usage of feature toggles Using environment variables to enable or disable features can lead to a situation where a feature is accidentally enabled in the production environme | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `DSOMM-ACTIVITY-BFDB576EA4164EC696FEA078D58B2FF8` | Conduction of build-it, break-it, fix-it contests. Conduction of build-it, break-it, fix-it contests Understanding security is hard, even for security champions and the conduction of security training | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `DSOMM-ACTIVITY-C72DA77986CC45B1A339190CE5093171` | Definition of simple BCDR practices for critical components. Definition of simple BCDR practices for critical components Business Continuity and Disaster Recovery (BCDR) is a plan and a process that e | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `DSOMM-ACTIVITY-CE970C9BDA9441CFBD788C15357B7E8E` | Integration of vulnerability issues into the development process. Integration of vulnerability issues into the development process To read console output of the build server to search for vulnerabilit | conceito: Threat Mitigation Linkage Controls (mechanism `ACM-TMR-005`) |
| `DSOMM-ACTIVITY-DA4FF665DCB94E939D2048CDEDC50FC2` | Defined decommissioning process. Defined decommissioning process The decommissioning process in the context of Docker and Kubernetes involves retiring Docker containers, images, and Kubernetes resourc | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `DSOMM-ACTIVITY-DCF9601BB4F24E259143E39AF75F7C33` | Hardening of the Environment. Hardening of the Environment Using default configurations for a cluster environment leads to potential risks. Harden environments according to best practices. Level 2 and | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `DSOMM-ACTIVITY-DF428C9DEFA042269F47A15BB53F822B` | Environment depending configuration parameters (secrets). Environment depending configuration parameters (secrets) Unauthorized access to secrets stored in source code or in artifacts (e.g. container | conceito: Secret Management Systems (mechanism `ACM-SPC-001`) |
| `DSOMM-ACTIVITY-F0E018143B884BD0A3A9F91DB001D20B` | WAF baseline. WAF baseline A baseline WAF configuration provides essential defense against common vulnerabilities, acting as a first line of automated threat detection and response. Steps: - Configure | conceito: Schema And Contract Validators (mechanism `ACM-IVF-003`) |
| `DSOMM-ACTIVITY-F0E018143B884BD0A3A9F91DB001D20BMEDIUM` | WAF medium. WAF medium A medium-level WAF configuration builds upon the baseline to offer a more nuanced and responsive defense mechanism against a wider array of threats. Sample steps: - Implement an | conceito: Schema And Contract Validators (mechanism `ACM-IVF-003`) |
| `DSOMM-ACTIVITY-F7B215DC73A44C619E49B3A3AF1C9AC3` | Security Coaching. Security Coaching Training does not change behaviour. Therefore, even if security practices are understood, it's likely that they are not performed. By coaching teams on security to | conceito: Structured Threat Analysis Frameworks (mechanism `ACM-TMR-002`) |
| `DSOMM-ACTIVITY-F8E80F1825034E3EB3BC7F67BB28DEFE` | Usage of a chaos technology. Usage of a chaos technology Due to manual changes on a system, they are not replaceable anymore. In case of a crash it might happen that a planned redundant system is unav | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `DSOMM-ACTIVITY-F994A55D71BB45A4A8870A213D72C504` | Aligning security in teams. Aligning security in teams The concept of Security Champions might suggest that only he/she is responsible for security. However, everyone in the project team should be res | conceito: Reviewer Accountability And Consistency Gates (mechanism `ACM-TMR-006`) |
| `DSOMM-ACTIVITY-FFE86CAF2FEC4630B5142DB83983984D` | App. Hardening Level 2. App. Hardening Level 2 Using an insecure application might lead to a compromised application. This might lead to total data theft or data modification. Following frameworks lik | conceito: Code Review For Input And Error Discipline (mechanism `ACM-IVF-001`) |

---

## CIS Controls v8.1.2

**O que esta ES traz para este capítulo:** contribui 21 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `CIS-10.5` | Enable Anti-Exploitation Features. Enable anti-exploitation features on enterprise assets and software, where possible, such as Microsoft® Data Execution Prevention (DEP), Windows® Defender Exploit Gu | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `CIS-11.2` | Perform Automated Backups. Perform automated backups of in-scope enterprise assets. Run backups weekly, or more frequently, based on the sensitivity of the data. | conceito: Release promotion, rollout controlado e readiness para rollback (slice `ACO-RPR`) |
| `CIS-11.5` | Test Data Recovery. Test backup recovery quarterly, or more frequently, for a sampling of in-scope enterprise assets. | conceito: Release promotion, rollout controlado e readiness para rollback (slice `ACO-RPR`) |
| `CIS-12.1` | Ensure Network Infrastructure is Up-to-Date. Ensure network infrastructure is kept up-to-date. Example implementations include running the latest stable release of software and/or using currently supp | conceito: Arquitetura segura e fronteiras de confiança (slice `ACO-ATB`) |
| `CIS-14` | Security Awareness and Skills Training. Establish and maintain a security awareness program to influence behavior among the workforce to be security conscious and properly skilled to reduce cybersecur | conceito: Explicit Threat Disposition Register (mechanism `ACM-TMR-004`) |
| `CIS-14.1` | Establish | conceito: Reviewer Accountability And Consistency Gates (mechanism `ACM-TMR-006`) |
| `CIS-15.2` | Establish | conceito: Integração e segurança service-to-service (slice `ACO-ITS`) |
| `CIS-16` | Manage the security life cycle of in-house developed, hosted | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `CIS-16.1` | Establish | conceito: Structured Threat Analysis Frameworks (mechanism `ACM-TMR-002`) |
| `CIS-16.2` | Establish | conceito: Findings Workflow And Exception Governance (mechanism `ACM-TSV-004`) |
| `CIS-16.6` | Establish | conceito: Threat Mitigation Linkage Controls (mechanism `ACM-TMR-005`) |
| `CIS-16.7` | Use Standard Hardening Configuration Templates for Application Infrastructure. Use standard, industry-recommended hardening configuration templates for application infrastructure components. This incl | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `CIS-17` | Establish a program to develop | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `CIS-17.2` | Establish | conceito: Structured Threat Analysis Frameworks (mechanism `ACM-TMR-002`) |
| `CIS-17.4` | Establish | conceito: Reviewer Accountability And Consistency Gates (mechanism `ACM-TMR-006`) |
| `CIS-17.7` | Conduct Routine Incident Response Exercises. Plan and conduct routine incident response exercises and scenarios for key personnel involved in the incident response process to prepare for responding to | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `CIS-18.3` | Remediate Penetration Test Findings. Remediate penetration test findings based on the enterprise’s documented vulnerability remediation process. This should include determining a timeline and level of | conceito: Findings Workflow And Exception Governance (mechanism `ACM-TSV-004`) |
| `CIS-4.1` | Establish | conceito: Authentication And Federation Protocols (mechanism `ACM-IAT-001`) |
| `CIS-4.2` | Establish | conceito: Release promotion, rollout controlado e readiness para rollback (slice `ACO-RPR`) |
| `CIS-4.8` | Uninstall or Disable Unnecessary Services on Enterprise Assets and Software. Uninstall or disable unnecessary services on enterprise assets and software, such as an unused file sharing service, web ap | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `CIS-7.2` | Establish and Maintain a Remediation Process. Establish and maintain a risk-based remediation strategy documented in a remediation process, with monthly, or more frequent, reviews. | conceito: Threat Mitigation Linkage Controls (mechanism `ACM-TMR-005`) |

---

## OWASP ASVS v5.0.0

**O que esta ES traz para este capítulo:** contribui 13 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `ASVS-REQ-V11.1.3` | Verify that cryptographic discovery mechanisms are employed to identify all instances of cryptography in the system, including encryption, hashing, and signing operations. | conceito: Gestão de segredos, configuração protegida e identidades operacionais (slice `ACO-SPC`) |
| `ASVS-REQ-V13.1.4` | Verify that the application's documentation defines the secrets that are critical for the security of the application and a schedule for rotating them, based on the organization's threat model and bus | conceito: Configuration Baseline Enforcement Controls (mechanism `ACM-RPR-008`) |
| `ASVS-REQ-V13.4.2` | Verify that debug modes are disabled for all components in production environments to prevent exposure of debugging features and information leakage. | conceito: Configuration Baseline Enforcement Controls (mechanism `ACM-RPR-008`) |
| `ASVS-REQ-V13.4.4` | Verify that using the HTTP TRACE method is not supported in production environments, to avoid potential information leakage. | conceito: Configuration Baseline Enforcement Controls (mechanism `ACM-RPR-008`) |
| `ASVS-REQ-V13.4.5` | Verify that documentation (such as for internal APIs) and monitoring endpoints are not exposed unless explicitly intended. | conceito: Configuration Baseline Enforcement Controls (mechanism `ACM-RPR-008`) |
| `ASVS-REQ-V13.4.6` | Verify that the application does not expose detailed version information of backend components. | conceito: Configuration Baseline Enforcement Controls (mechanism `ACM-RPR-008`) |
| `ASVS-REQ-V15.1.1` | Verify that application documentation defines risk based remediation time frames for 3rd party component versions with vulnerabilities and for updating libraries in general, to minimize the risk from | conceito: Versioned Diagrams And ADR Records (mechanism `ACM-ATB-001`) |
| `ASVS-REQ-V15.2.1` | Verify that the application only contains components which have not breached the documented update and remediation time frames. | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |
| `ASVS-REQ-V15.2.3` | Verify that the production environment only includes functionality that is required for the application to function, and does not expose extraneous functionality such as test code, sample snippets, an | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |
| `ASVS-REQ-V15.2.5` | Verify that the application implements additional protections around parts of the application which are documented as containing "dangerous functionality" or using third-party libraries considered to | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |
| `ASVS-REQ-V2.3.4` | Verify that business logic level locking mechanisms are used to ensure that limited quantity resources (such as theater seats or delivery slots) cannot be double-booked by manipulating the application | conceito: Code Review For Input And Error Discipline (mechanism `ACM-IVF-001`) |
| `ASVS-REQ-V2.4.1` | Verify that anti-automation controls are in place to protect against excessive calls to application functions that could lead to data exfiltration, garbage-data creation, quota exhaustion, rate-limit | conceito: API Gateway With Mutual Authentication (mechanism `ACM-ITS-001`) |
| `ASVS-REQ-V8.3.2` | Verify that changes to values on which authorization decisions are made are applied immediately. Where changes cannot be applied immediately, (such as when relying on data in self-contained tokens), t | conceito: Access Policy Enforcement (mechanism `ACM-IAT-002`) |

---

## NIST SSDF (SP 800-218 v1.1)

**O que esta ES traz para este capítulo:** contribui 13 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `SSDF-PRACTICE-PO.5` | Implement | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `SSDF-PRACTICE-PS.2` | Provide a Mechanism for Verifying Software Release Integrity. Help software acquirers ensure that the software they acquire is legitimate and has not been tampered with. | conceito: Artifact Signing And Attestation (mechanism `ACM-SCBI-004`) |
| `SSDF-PRACTICE-PS.3` | Archive and Protect Each Software Release. Preserve software releases in order to help identify, analyze, and eliminate vulnerabilities discovered in the software after release. | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `SSDF-PRACTICE-PW.4` | Reuse Existing, Well-Secured Software When Feasible Instead of Duplicating Functionality. Lower the costs of software development, expedite software development, and decrease the likelihood of introdu | conceito: Approved Source And Registry Governance (practice `ACP-SCBI-003`) |
| `SSDF-PRACTICE-PW.9` | Configure Software to Have Secure Settings by Default. Help improve the security of the softwar e at the time of installation to reduce the likelihood of the software being deployed with weak security | conceito: Configuration Baseline Enforcement Controls (mechanism `ACM-RPR-008`) |
| `SSDF-TASK-PO.3.2` | Follow recommended security practices to deploy , operate, and maintain tools and toolchains. | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `SSDF-TASK-PO.5.1` | Separate and protect each environment involved in software development. | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `SSDF-TASK-PS.3.2` | Collect, safeguard, maintain, and share provenance data for all components of each software release (e.g., in a software bill of materials [SBOM]). | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `SSDF-TASK-PW.4.4` | Verify that acquired commercial, open-source, and all other third-party software components comply with the requirements , as defined by the organization, throughout their life cycle s. | conceito: Approved Source And Registry Governance (practice `ACP-SCBI-003`) |
| `SSDF-TASK-PW.9.1` | Define a secure baseline by determining how to configure each setting that has an effect on security or a security -related setting so that the default settings are secure and do not weaken the securi | conceito: Configuration Baseline Enforcement Controls (mechanism `ACM-RPR-008`) |
| `SSDF-TASK-PW.9.2` | Implement the default settings (or groups of default settings, if applicable), and document each setting for software administrators. | conceito: Configuration Baseline Enforcement Controls (mechanism `ACM-RPR-008`) |
| `SSDF-TASK-RV.1.3` | Have a policy that addresses vulnerability disclosure and remediation, and implement the roles, responsibilities, and processes needed to support that policy. | conceito: Findings Workflow And Exception Governance (mechanism `ACM-TSV-004`) |
| `SSDF-TASK-RV.3.2` | Analyze the root causes over time to identify patterns, such as a particular secure coding practice not being followed consistently. | conceito: Threat Model Versioning Controls (mechanism `ACM-TMR-003`) |

---

## SAFECode — Practical Security Stories and Tasks for Agile Development (2012)

**O que esta ES traz para este capítulo:** contribui 11 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `SCAGILE-EXP-11` | Environment hardening (development, building, deployment). Environment hardening covering development systems, building environment, deployment infrastructure | conceito: Rollback And Containment Controls (mechanism `ACM-RPR-004`) |
| `SCAGILE-EXP-12` | Securing configuration. Securing configuration e.g. web server hardening, ACLs on folders holding sensitive data, configuration file hardening | conceito: Rollback And Containment Controls (mechanism `ACM-RPR-004`) |
| `SCAGILE-EXP-2` | Security fix/patch validation (completeness and strength). Security fix/patch validation checking completeness and strength of fixes | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `SCAGILE-EXP-9` | Security tool recommendations and effective use. Security tool recommendations and effective use including customization | conceito: Artifact Signing And Attestation (mechanism `ACM-SCBI-004`) |
| `SCAGILE-OPS-12` | Use secure versions of communication protocols. Use secure versions of communication protocols for new code and existing code | conceito: Trust Boundary Models (mechanism `ACM-ITS-002`) |
| `SCAGILE-OPS-13` | Ensure inclusion of security patches from previous releases. Ensure inclusion of security patches/fixes applied in previous release(s) | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |
| `SCAGILE-OPS-14` | Ensure all developers have obtained secure coding training. Ensure all developers have obtained secure coding training | conceito: Threat Traceability Into Requirements And Validation (practice `ACP-TMR-005`) |
| `SCAGILE-OPS-16` | Ensure security fixes verified by security experts before committing. Ensure security fixes are verified by security experts before committing them | conceito: Test Execution Surfaces (mechanism `ACM-TSV-002`) |
| `SCAGILE-OPS-2` | Verify security POCs and plan for fixes. Verify security POCs and plan for fixes as recommendation for software development team | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `SCAGILE-OPS-6` | Keep track of patches/fixes to OS components. Keep track of patches/fixes to OS components for new and existing code | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |
| `SCAGILE-OPS-8` | Use appropriate security-related flags for compiler. Use appropriate security-related flags for compiler for new and existing code | conceito: Artifact Signing And Attestation (mechanism `ACM-SCBI-004`) |

---

## OWASP SAMM v2.1

**O que esta ES traz para este capítulo:** contribui 9 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `SAMM-ACTIVITY-D_SA_1_A` | Adhere to basic security principles. Adhere to basic security principles. During design, technical staff on the product team use a short checklist of security principles. Typically, security principle | conceito: Versioned Diagrams And ADR Records (mechanism `ACM-ATB-001`) |
| `SAMM-ACTIVITY-D_TA_3_A` | Periodic review of risk profiles. Periodic review of risk profiles. The application portfolio of an organization changes, as well as the conditions and constraints in which an application lives (e.g., | conceito: Structured Threat Analysis Frameworks (mechanism `ACM-TMR-002`) |
| `SAMM-ACTIVITY-G_SM_1_B` | Define basic security metrics. Define basic security metrics. Define and document metrics to evaluate the effectiveness and efficiency of the application security program. This way improvements are me | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `SAMM-ACTIVITY-I_SB_2_B` | Review application dependencies for security | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `SAMM-ACTIVITY-I_SD_1_A` | Define the deployment process over all stages, breaking it down into a set of clear instructions to either be followed by a person | conceito: Release Promotion Controls (mechanism `ACM-RPR-001`) |
| `SAMM-ACTIVITY-I_SD_2_A` | Ensure | conceito: Release Promotion Controls (mechanism `ACM-RPR-001`) |
| `SAMM-ACTIVITY-O_EM_2_A` | Establish hardening baselines. Establish hardening baselines. Establish configuration hardening baselines for all components in each technology stack used. To assist with consistent application of the | conceito: Configuration Baseline Enforcement Controls (mechanism `ACM-RPR-008`) |
| `SAMM-ACTIVITY-O_OM_2_B` | Formalize decommissioning process. Formalize decommissioning process. As part of decommissioning a system, application, or service, follow an established process for removing all relevant accounts, fi | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |
| `SAMM-ACTIVITY-O_OM_3_B` | Review application lifecycle state regularly | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |

---

## MITRE CWE — Software Development View (v4.19.1)

**O que esta ES traz para este capítulo:** contribui 8 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `CWE-1037` | Processor Optimization Removal or Modification of Security-critical Code. The developer builds a security-critical protection mechanism into the software, but the processor optimizes the execution of | conceito: Release promotion, rollout controlado e readiness para rollback (slice `ACO-RPR`) |
| `CWE-1188` | Initialization of a Resource with an Insecure Default. The product initializes or sets a resource with a default that is intended to be changed by the product's installer, administrator, or maintainer | conceito: Configuration Baseline Enforcement Controls (mechanism `ACM-RPR-008`) |
| `CWE-1341` | Multiple Releases of Same Resource or Handle. The product attempts to close or release a resource or handle more than once, without any successful open between the close operations. | conceito: API Gateway With Mutual Authentication (mechanism `ACM-ITS-001`) |
| `CWE-15` | External Control of System or Configuration Setting. One or more system settings or configuration elements can be externally controlled by a user. | conceito: Configuration Baseline Enforcement Controls (mechanism `ACM-RPR-008`) |
| `CWE-283` | Unverified Ownership. The product does not properly verify that a critical resource is owned by the proper entity. | conceito: Release promotion, rollout controlado e readiness para rollback (slice `ACO-RPR`) |
| `CWE-487` | Reliance on Package-level Scope. Java packages are not inherently closed; therefore, relying on them for code security is not a good practice. | conceito: Release promotion, rollout controlado e readiness para rollback (slice `ACO-RPR`) |
| `CWE-547` | Use of Hard-coded, Security-relevant Constants. The product uses hard-coded constants instead of symbolic names for security-critical values, which increases the likelihood of mistakes during code mai | conceito: Configuration Baseline Enforcement Controls (mechanism `ACM-RPR-008`) |
| `CWE-733` | Compiler Optimization Removal or Modification of Security-critical Code. The developer builds a security-critical protection mechanism into the software, but the compiler optimizes the program such th | conceito: Release promotion, rollout controlado e readiness para rollback (slice `ACO-RPR`) |

---

## MITRE ATLAS — Adversarial Threat Landscape for AI Systems

**O que esta ES traz para este capítulo:** contribui 4 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `AML.CS0008` | ProofPoint Evasion. Proof Pudding (CVE-2019-20634) is a code repository that describes how ML researchers evaded ProofPoint's email protection system by first building a copy-cat email protection ML m | conceito: Release promotion, rollout controlado e readiness para rollback (slice `ACO-RPR`) |
| `AML.CS0052` | LLMSmith: RCE Vulnerabilities in LLM-Integrated Applications. Researchers identified 20 remote code execution (RCE) vulnerabilities across 11 different LLM frameworks. They discovered applications dep | conceito: Release promotion, rollout controlado e readiness para rollback (slice `ACO-RPR`) |
| `AML.T0002.002` | AI Agent Configuration. Adversaries may acquire publicly accessible AI agent configuration files to understand agent capabilities, gain unauthorized access to tools and data sources, or identify crede | conceito: Release promotion, rollout controlado e readiness para rollback (slice `ACO-RPR`) |
| `AML.T0081` | Modify AI Agent Configuration. Adversaries may modify the configuration files for AI agents on a system. This allows malicious changes to persist beyond the life of a single agent and affects any agen | conceito: Release promotion, rollout controlado e readiness para rollback (slice `ACO-RPR`) |

---

## PCI Secure SLC v1.1

**O que esta ES traz para este capítulo:** contribui 4 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `PCISSLC-3.3` | Software security controls implemented to mitigate threats and design weaknesses. Process for defining security requirements and implementing controls to mitigate threats; mitigation decisions recorde | conceito: Threat Model Versioning Controls (mechanism `ACM-TMR-003`) |
| `PCISSLC-5.1` | All changes to software identified, assessed, and approved. Process to identify, assess, and approve all changes | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `PCISSLC-8.1` | Software vendor provides secure implementation guidance to stakeholders. Guidance on secure implementation, configuration, and operation; documentation of all security-related configurable options | conceito: Rollback And Containment Controls (mechanism `ACM-RPR-004`) |
| `PCISSLC-8.2` | Secure implementation guidance includes detailed install/configure instructions. Detailed instructions on how to securely install, initialize, configure, and maintain software | conceito: Rollback And Containment Controls (mechanism `ACM-RPR-004`) |

---

## SLSA Specification v1.0 — Build Track

**O que esta ES traz para este capítulo:** contribui 4 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `SLSA-BUILD-L1` | Build L1: Provenance exists. Summary Package has provenance showing how it was built. Can be used to prevent mistakes but is trivial to bypass or forge. Intended for Projects and organizations wanting | conceito: Artifact Signing And Attestation (mechanism `ACM-SCBI-004`) |
| `SLSA-BUILD-L2` | Build L2: Hosted build platform. Summary Forging the provenance or evading verification requires an explicit “attack”, though this may be easy to perform. Deters unsophisticated adversaries or those w | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `SLSA-PRINCIPLE-TRUST-PLATFORMS` | Trust platforms, verify artifacts. Establish trust in a small number of platforms and systems—such as change management, build, and packaging platforms—and then automatically verify the many artifacts | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `SLSA-PRODUCER-CHOOSE-BUILD-PLATFORM` | Choose an appropriate build platform. The producer MUST select a build platform that is capable of reaching their desired SLSA Build Level. For example, if a producer wishes to produce a Build Level 3 | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |

---

## HIPAA Security Rule

**O que esta ES traz para este capítulo:** contribui 2 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `HIPAA-164-308a5` | Security Awareness and Training. Security Awareness and Training — Administrative Safeguard. Implement a security awareness and training programme for all members of the workforce (including managemen | conceito: Release promotion, rollout controlado e readiness para rollback (slice `ACO-RPR`) |
| `HIPAA-164-316a` | Policies and Procedures. Policies and Procedures — Standard. Implement reasonable and appropriate policies and procedures to comply with the standards, implementation specifications, or other requirem | conceito: Threat Model Versioning Controls (mechanism `ACM-TMR-003`) |

---

## OWASP Top 10 (2021)

**O que esta ES traz para este capítulo:** contribui 2 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `TOP10-A05-2021` | Security Misconfiguration. The application might be vulnerable if the application is missing appropriate security hardening across any part of the application stack or improperly configured permission | conceito: Release promotion, rollout controlado e readiness para rollback (slice `ACO-RPR`) |
| `TOP10-A06-2021` | Vulnerable and Outdated Components. You are likely vulnerable if you do not know the versions of all components you use. If the software is vulnerable, unsupported, or out of date, including the OS, w | conceito: Release promotion, rollout controlado e readiness para rollback (slice `ACO-RPR`) |

---

## SAFECode — Fundamental Practices for Secure Software Development (2018)

**O que esta ES traz para este capítulo:** contribui 2 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `SCFPSSD-COMPILER` | Use Current Compiler and Toolchain Versions and Secure Compiler Options. Current compiler/toolchain versions with security-enhancing compiler options enabled | conceito: Artifact Signing And Attestation (mechanism `ACM-SCBI-004`) |
| `SCFPSSD-THIRD-PARTY` | Manage Security Risk Inherent in the Use of Third-party Components. Risk management for third-party and open source components including monitoring vulnerabilities | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |

---

## SAFECode — Software Integrity Controls (2010)

**O que esta ES traz para este capítulo:** contribui 2 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `SCSIC-DEVELOPMENT` | Vendor Software Development Integrity Controls. Controls for development phase: people security, physical security, network security, code repository security, build environment, peer review, security | conceito: Artifact Signing And Attestation (mechanism `ACM-SCBI-004`) |
| `SCSIC-SOURCING` | Vendor Sourcing Integrity Controls. Controls for vendor sourcing process: contractual integrity, defined expectations, ownership, vulnerability response, security training, OSS management | conceito: Approved Source And Registry Governance (practice `ACP-SCBI-003`) |

---

## ENISA — Multilayer AI Cybersecurity Practices (2023)

**O que esta ES traz para este capítulo:** contribui 1 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `ENISA-AI-FAICP-CONCLUSIONS` | Conclusions and way forward for AI cybersecurity practices. A multilayer framework for good cybersecurity practices for AI June 2023 36 4. CONCLUSIONS AND THE WAY FORWARD The report provide s a framew | conceito: Explicit Threat Disposition Register (mechanism `ACM-TMR-004`) |

---

## EU Digital Operational Resilience Act (DORA)

**O que esta ES traz para este capítulo:** contribui 1 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `DORA-ART-12` | DORA Article 12. Article 12 (Backup policies and procedures, restoration and recovery procedures and methods) requires financial entities to establish backup policies and procedures specifying the sco | conceito: Release Promotion Controls (mechanism `ACM-RPR-001`) |

---

## NIST AI 100-2 e2025 — Adversarial Machine Learning Taxonomy

**O que esta ES traz para este capítulo:** contribui 1 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `NIST-AI-100-2-E2025-3.1` | Attack Classification. While many attack types in the PredAI taxonomy apply to GenAI (e.g., data poisoning, model poisoning, and model extraction), recent work has also introduced novel AML at- tacks | conceito: Release promotion, rollout controlado e readiness para rollback (slice `ACO-RPR`) |

---

## NIST AI RMF 1.0

**O que esta ES traz para este capítulo:** contribui 1 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `NIST-AI-RMF-MAP-3.5` | Processes for human oversight are defined, assessed,. and documented in accordance with organizational policies from the GOVERN function. | conceito: Release promotion, rollout controlado e readiness para rollback (slice `ACO-RPR`) |

---
