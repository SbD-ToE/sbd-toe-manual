# 25. Rastreabilidade — Threat Modeling

## Sumário

Este capítulo trata do **processo formal de modelação de ameaças** —
identificação de ameaças, avaliação de risco, mitigation traceability,
e ligação ameaça↔requisito. As fontes externas seguintes contribuem para
esta área:

- **NIST SP 800-53 Rev. 5** — 108 referência(s)
- **MITRE ATLAS — Adversarial Threat Landscape for AI Systems** — 46 referência(s)
- **MITRE CAPEC v3.9** — 41 referência(s)
- **PCI DSS v4.0.1** — 35 referência(s)
- **OWASP SAMM v2.1** — 32 referência(s)
- **NIST SSDF (SP 800-218 v1.1)** — 16 referência(s)
- **NIST AI RMF 1.0** — 15 referência(s)
- **NIST AI 100-2 e2025 — Adversarial Machine Learning Taxonomy** — 12 referência(s)
- **OWASP DSOMM** — 10 referência(s)
- **PCI Secure SLC v1.1** — 10 referência(s)
- **CIS Controls v8.1.2** — 6 referência(s)
- **MITRE CWE — Software Development View (v4.19.1)** — 5 referência(s)
- **EU Digital Operational Resilience Act (DORA)** — 5 referência(s)
- **EU NIS2 Directive** — 4 referência(s)
- **OWASP Machine Learning Top 10** — 4 referência(s)
- **SAFECode — Fundamental Practices for Secure Software Development (2018)** — 4 referência(s)
- **OWASP ASVS v5.0.0** — 3 referência(s)
- **ENISA — Multilayer AI Cybersecurity Practices (2023)** — 2 referência(s)
- **HIPAA Security Rule** — 2 referência(s)
- **OWASP LLM Top 10 (2025)** — 2 referência(s)
- **OWASP Proactive Controls (2018)** — 2 referência(s)
- **SAFECode — Practical Security Stories and Tasks for Agile Development (2012)** — 2 referência(s)
- **EU Cyber Resilience Act (CRA)** — 1 referência(s)
- **OWASP MCP — Third-Party Servers v1.0** — 1 referência(s)
- **SLSA Specification v1.0 — Build Track** — 1 referência(s)

---

## NIST SP 800-53 Rev. 5

**O que esta ES traz para este capítulo:** contribui 108 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `SP800-53-AT-2.2` | Insider Threat. Provide literacy training on recognizing and reporting potential indicators of insider threat. | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `SP800-53-AT-2.6` | Cyber Threat Environment. Provide literacy training on the cyber threat environment; and Reflect current cyber threat information in system operations. | conceito: Gestão de segredos, configuração protegida e identidades operacionais (slice `ACO-SPC`) |
| `SP800-53-AU-10.3` | Chain of Custody. Maintain reviewer or releaser credentials within the established chain of custody for information reviewed or released. | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `SP800-53-AU-2.3` | Reviews and Updates | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `SP800-53-CA-7` | Continuous Monitoring. Develop a system-level continuous monitoring strategy and implement continuous monitoring in accordance with the organization-level continuous monitoring strategy that includes: | conceito: Risk-Based Security Test Planning (practice `ACP-TSV-001`) |
| `SP800-53-CA-7.3` | Trend Analyses. Employ trend analyses to determine if control implementations, the frequency of continuous monitoring activities, and the types of activities used in the continuous monitoring process | conceito: Risk-Based Security Test Planning (practice `ACP-TSV-001`) |
| `SP800-53-CA-7.4` | Risk Monitoring. Ensure risk monitoring is an integral part of the continuous monitoring strategy that includes the following: Effectiveness monitoring | conceito: Risk-Based Security Test Planning (practice `ACP-TSV-001`) |
| `SP800-53-CA-7.6` | Automation Support for Monitoring. Ensure the accuracy, currency, and availability of monitoring results for the system using [automated mechanisms]. | conceito: Risk-Based Security Test Planning (practice `ACP-TSV-001`) |
| `SP800-53-CM-11` | User-installed Software. Establish [policies] governing the installation of software by users | conceito: Approved Source And Registry Governance (practice `ACP-SCBI-003`) |
| `SP800-53-CM-11.3` | Automated Enforcement and Monitoring. Enforce and monitor compliance with software installation policies using [organization-defined automated mechanisms]. | conceito: Approved Source And Registry Governance (practice `ACP-SCBI-003`) |
| `SP800-53-CM-3.1` | Automated Documentation, Notification, and Prohibition of Changes. Use [automated mechanisms] to: Document proposed changes to the system; Notify [approval authorities] of proposed changes to the syst | conceito: Accountable Release Approval (practice `ACP-RPR-001`) |
| `SP800-53-CM-7.3` | Registration Compliance. Ensure compliance with [registration requirements]. | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `SP800-53-CM-8.6` | Assessed Configurations and Approved Deviations. Include assessed component configurations and any approved deviations to current deployed configurations in the system component inventory. | conceito: Build-Linked SBOM Generation (practice `ACP-SCBI-001`) |
| `SP800-53-CP-6.1` | Separation from Primary Site. Identify an alternate storage site that is sufficiently separated from the primary storage site to reduce susceptibility to the same threats. | conceito: Gestão de segredos, configuração protegida e identidades operacionais (slice `ACO-SPC`) |
| `SP800-53-CP-7.1` | Separation from Primary Site. Identify an alternate processing site that is sufficiently separated from the primary processing site to reduce susceptibility to the same threats. | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `SP800-53-CP-9.4` | Protection from Unauthorized Modification | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `SP800-53-IR-4.12` | Malicious Code and Forensic Analysis. Analyze malicious code and/or other residual artifacts remaining in the system after the incident. | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `SP800-53-IR-4.13` | Behavior Analysis. Analyze anomalous or suspected adversarial behavior in or related to [environments or resources]. | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `SP800-53-IR-4.6` | Insider Threats. Implement an incident handling capability for incidents involving insider threats. | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `SP800-53-IR-4.7` | Insider Threats — Intra-organization Coordination. Coordinate an incident handling capability for insider threats that includes the following organizational entities [entities]. | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `SP800-53-IR-6.2` | Vulnerabilities Related to Incidents. Report system vulnerabilities associated with reported incidents to [personnel or roles]. | conceito: Identidade, autenticação e gestão de sessões (slice `ACO-IAT`) |
| `SP800-53-MA-5.1` | Individuals Without Appropriate Access. Implement procedures for the use of maintenance personnel that lack appropriate security clearances or are not U.S. citizens, that include the following require | conceito: Identidade, autenticação e gestão de sessões (slice `ACO-IAT`) |
| `SP800-53-MA-5.2` | Security Clearances for Classified Systems. Verify that personnel performing maintenance and diagnostic activities on a system processing, storing, or transmitting classified information possess secur | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `SP800-53-MA-5.3` | Citizenship Requirements for Classified Systems. Verify that personnel performing maintenance and diagnostic activities on a system processing, storing, or transmitting classified information are U.S. | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `SP800-53-MA-5.4` | Foreign Nationals. Ensure that: Foreign nationals with appropriate security clearances are used to conduct maintenance and diagnostic activities on classified systems only when the systems are jointly | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `SP800-53-PE-14.2` | Monitoring with Alarms and Notifications. Employ environmental control monitoring that provides an alarm or notification of changes potentially harmful to personnel or equipment to [personnel or roles | conceito: Gestão de segredos, configuração protegida e identidades operacionais (slice `ACO-SPC`) |
| `SP800-53-PE-23` | Facility Location. Plan the location or site of the facility where the system resides considering physical and environmental hazards; and For existing facilities, consider the physical and environment | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `SP800-53-PL-2` | System Security and Privacy Plans. Develop security and privacy plans for the system that: Are consistent with the organization’s enterprise architecture | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `SP800-53-PL-8.1` | Defense in Depth. Design the security and privacy architectures for the system using a defense-in-depth approach that: Allocates [controls] to [locations and architectural layers]; and Ensures that th | conceito: Arquitetura segura e fronteiras de confiança (slice `ACO-ATB`) |
| `SP800-53-PM-12` | Insider Threat Program. Implement an insider threat program that includes a cross-discipline insider threat incident handling team. | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `SP800-53-PM-25` | Minimization of Personally Identifiable Information Used in Testing, Training, and Research. Develop, document, and implement policies and procedures that address the use of personally identifiable in | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `SP800-53-PM-28` | Risk Framing. Identify and document: Assumptions affecting risk assessments, risk responses, and risk monitoring | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `SP800-53-PM-29` | analyze risk from an organization-wide perspective | conceito: Identidade, autenticação e gestão de sessões (slice `ACO-IAT`) |
| `SP800-53-PM-3` | Information Security and Privacy Resources. Include the resources needed to implement the information security and privacy programs in capital planning and investment requests and document all excepti | conceito: Gestão de segredos, configuração protegida e identidades operacionais (slice `ACO-SPC`) |
| `SP800-53-PM-30` | Supply Chain Risk Management Strategy. Develop an organization-wide strategy for managing supply chain risks associated with the development, acquisition, maintenance, and disposal of systems, system | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `SP800-53-PM-31` | Continuous Monitoring Strategy. Develop an organization-wide continuous monitoring strategy and implement continuous monitoring programs that include: Establishing the following organization-wide metr | conceito: Logging de eventos de segurança e audit trail (slice `ACO-SLG`) |
| `SP800-53-PM-4` | Plan of Action and Milestones Process. Implement a process to ensure that plans of action and milestones for the information security, privacy, and supply chain risk management programs and associated | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `SP800-53-PS-2` | Position Risk Designation. Assign a risk designation to all organizational positions | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `SP800-53-PS-3.4` | Citizenship Requirements. Verify that individuals accessing a system processing, storing, or transmitting [information types] meet [citizenship requirements]. | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `SP800-53-PS-4.1` | Post-employment Requirements. Notify terminated individuals of applicable, legally binding post-employment requirements for the protection of organizational information; and Require terminated individ | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `SP800-53-PS-6.3` | Post-employment Requirements. Notify individuals of applicable, legally binding post-employment requirements for protection of organizational information; and Require individuals to sign an acknowledg | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `SP800-53-PS-7` | External Personnel Security. Establish personnel security requirements, including security roles and responsibilities for external providers | conceito: Identidade, autenticação e gestão de sessões (slice `ACO-IAT`) |
| `SP800-53-PT-3` | Personally Identifiable Information Processing Purposes. Identify and document the [purpose(s)] for processing personally identifiable information | conceito: Gestão de segredos, configuração protegida e identidades operacionais (slice `ACO-SPC`) |
| `SP800-53-PT-3.2` | Automation. Track processing purposes of personally identifiable information using [automated mechanisms]. | conceito: Gestão de segredos, configuração protegida e identidades operacionais (slice `ACO-SPC`) |
| `SP800-53-RA-1` | Policy and Procedures. Develop, document, and disseminate to [organization-defined personnel or roles]: risk assessment policy that: Addresses purpose, scope, roles, responsibilities, management commi | conceito: DFD And Trust-Boundary Grounding (practice `ACP-TMR-002`) |
| `SP800-53-RA-10` | Threat Hunting. Establish and maintain a cyber threat hunting capability to: Search for indicators of compromise in organizational systems | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `SP800-53-RA-2` | Security Categorization. Categorize the system and information it processes, stores, and transmits; Document the security categorization results, including supporting rationale, in the security plan f | conceito: Threat Disposition And Accepted Risk Governance (practice `ACP-TMR-004`) |
| `SP800-53-RA-2.1` | Impact-level Prioritization. Conduct an impact-level prioritization of organizational systems to obtain additional granularity on system impact levels. | conceito: Threat Disposition And Accepted Risk Governance (practice `ACP-TMR-004`) |
| `SP800-53-RA-3` | Risk Assessment. Conduct a risk assessment, including: Identifying threats to and vulnerabilities in the system | conceito: Structured Threat Analysis Method Selection (practice `ACP-TMR-003`) |
| `SP800-53-RA-3.1` | Supply Chain Risk Assessment. Assess supply chain risks associated with [systems, system components, and system services]; and Update the supply chain risk assessment [frequency] , when there are sign | conceito: Structured Threat Analysis Method Selection (practice `ACP-TMR-003`) |
| `SP800-53-RA-3.2` | Use of All-source Intelligence. Use all-source intelligence to assist in the analysis of risk. | conceito: Structured Threat Analysis Method Selection (practice `ACP-TMR-003`) |
| `SP800-53-RA-3.3` | Dynamic Threat Awareness. Determine the current cyber threat environment on an ongoing basis using [means]. | conceito: Structured Threat Analysis Method Selection (practice `ACP-TMR-003`) |
| `SP800-53-RA-3.4` | Predictive Cyber Analytics. Employ the following advanced automation and analytics capabilities to predict and identify risks to [systems or system components]: [organization-defined advanced automati | conceito: Structured Threat Analysis Method Selection (practice `ACP-TMR-003`) |
| `SP800-53-RA-4` | Risk Assessment Update | conceito: Threat Model Creation And Triggered Refresh (practice `ACP-TMR-001`) |
| `SP800-53-RA-5` | Vulnerability Monitoring and Scanning. Monitor and scan for vulnerabilities in the system and hosted applications [organization-defined frequency and/or randomly in accordance with organization-define | conceito: Staged Dynamic Testing And Gate Enforcement (practice `ACP-TSV-005`) |
| `SP800-53-RA-5.1` | Update Tool Capability | conceito: Staged Dynamic Testing And Gate Enforcement (practice `ACP-TSV-005`) |
| `SP800-53-RA-5.11` | Public Disclosure Program. Establish a public reporting channel for receiving reports of vulnerabilities in organizational systems and system components. | conceito: Staged Dynamic Testing And Gate Enforcement (practice `ACP-TSV-005`) |
| `SP800-53-RA-5.4` | Discoverable Information. Determine information about the system that is discoverable and take [corrective actions]. | conceito: Staged Dynamic Testing And Gate Enforcement (practice `ACP-TSV-005`) |
| `SP800-53-RA-5.7` | Automated Detection and Notification of Unauthorized Components | conceito: Staged Dynamic Testing And Gate Enforcement (practice `ACP-TSV-005`) |
| `SP800-53-RA-6` | Technical Surveillance Countermeasures Survey. Employ a technical surveillance countermeasures survey at [locations]. | conceito: Secret Leak Prevention In Source And Pipeline (practice `ACP-SPC-001`) |
| `SP800-53-RA-7` | Risk Response. Respond to findings from security and privacy assessments, monitoring, and audits in accordance with organizational risk tolerance. | conceito: Threat Disposition And Accepted Risk Governance (practice `ACP-TMR-004`) |
| `SP800-53-RA-9` | Criticality Analysis. Identify critical system components and functions by performing a criticality analysis for [systems, system components, or system services] at [decision points in the system deve | conceito: Threat Model Creation And Triggered Refresh (practice `ACP-TMR-001`) |
| `SP800-53-SA-11.2` | Threat Modeling and Vulnerability Analyses. Require the developer of the system, system component, or system service to perform threat modeling and vulnerability analyses during development and the su | conceito: Governed Static Analysis Execution (practice `ACP-TSV-002`) |
| `SP800-53-SA-11.3` | Independent Verification of Assessment Plans and Evidence. Require an independent agent satisfying [independence criteria] to verify the correct implementation of the developer security and privacy as | conceito: Governed Static Analysis Execution (practice `ACP-TSV-002`) |
| `SP800-53-SA-12.14` | Identity and Traceability | conceito: Automated Dependency And Image Risk Gating (practice `ACP-SCBI-002`) |
| `SP800-53-SA-15` | Development Process, Standards, and Tools. Require the developer of the system, system component, or system service to follow a documented development process that: Explicitly addresses security and p | conceito: Pipeline Definition As Reviewed Code (practice `ACP-SCBI-004`) |
| `SP800-53-SA-15.1` | Quality Metrics. Require the developer of the system, system component, or system service to: Define quality metrics at the beginning of the development process; and Provide evidence of meeting the qu | conceito: Pipeline Definition As Reviewed Code (practice `ACP-SCBI-004`) |
| `SP800-53-SA-15.3` | Criticality Analysis. Require the developer of the system, system component, or system service to perform a criticality analysis: At the following decision points in the system development life cycle: | conceito: Pipeline Definition As Reviewed Code (practice `ACP-SCBI-004`) |
| `SP800-53-SA-15.4` | Threat Modeling and Vulnerability Analysis | conceito: Pipeline Definition As Reviewed Code (practice `ACP-SCBI-004`) |
| `SP800-53-SA-17.2` | Security-relevant Components. Require the developer of the system, system component, or system service to: Define security-relevant hardware, software, and firmware; and Provide a rationale that the d | conceito: Architecture Review And Approval Governance (practice `ACP-ATB-005`) |
| `SP800-53-SA-17.3` | Formal Correspondence. Require the developer of the system, system component, or system service to: Produce, as an integral part of the development process, a formal top-level specification that speci | conceito: Architecture Review And Approval Governance (practice `ACP-ATB-005`) |
| `SP800-53-SA-17.4` | Informal Correspondence. Require the developer of the system, system component, or system service to: Produce, as an integral part of the development process, an informal descriptive top-level specifi | conceito: Architecture Review And Approval Governance (practice `ACP-ATB-005`) |
| `SP800-53-SA-17.5` | Conceptually Simple Design. Require the developer of the system, system component, or system service to: Design and structure the security-relevant hardware, software, and firmware to use a complete, | conceito: Architecture Review And Approval Governance (practice `ACP-ATB-005`) |
| `SP800-53-SA-2` | Allocation of Resources. Determine the high-level information security and privacy requirements for the system or system service in mission and business process planning; Determine, document, and allo | conceito: Threat Traceability Into Requirements And Validation (practice `ACP-TMR-005`) |
| `SP800-53-SA-3` | System Development Life Cycle. Acquire, develop, and manage the system using [system-development life cycle] that incorporates information security and privacy considerations | conceito: DFD And Trust-Boundary Grounding (practice `ACP-TMR-002`) |
| `SP800-53-SA-3.3` | Technology Refresh. Plan for and implement a technology refresh schedule for the system throughout the system development life cycle. | conceito: DFD And Trust-Boundary Grounding (practice `ACP-TMR-002`) |
| `SP800-53-SA-4` | Acquisition Process. Include the following requirements, descriptions, and criteria, explicitly or by reference, using in the acquisition contract for the system, system component, or system service: | conceito: Trust Boundary And Integration Review (practice `ACP-ITS-001`) |
| `SP800-53-SA-4.3` | Development Methods, Techniques, and Practices. Require the developer of the system, system component, or system service to demonstrate the use of a system development life cycle process that includes | conceito: Trust Boundary And Integration Review (practice `ACP-ITS-001`) |
| `SP800-53-SA-4.7` | NIAP-approved Protection Profiles. Limit the use of commercially provided information assurance and information assurance-enabled information technology products to those products that have been succe | conceito: Trust Boundary And Integration Review (practice `ACP-ITS-001`) |
| `SP800-53-SA-4.8` | Continuous Monitoring Plan for Controls. Require the developer of the system, system component, or system service to produce a plan for continuous monitoring of control effectiveness that is consisten | conceito: Trust Boundary And Integration Review (practice `ACP-ITS-001`) |
| `SP800-53-SA-8.21` | Self-analysis. Implement the security design principle of self-analysis in [systems or system components]. | conceito: Architectural Decision And Solution Traceability (practice `ACP-ATB-002`) |
| `SP800-53-SA-8.25` | Economic Security. Implement the security design principle of economic security in [systems or system components]. | conceito: Architectural Decision And Solution Traceability (practice `ACP-ATB-002`) |
| `SP800-53-SA-8.27` | Human Factored Security. Implement the security design principle of human factored security in [systems or system components]. | conceito: Architectural Decision And Solution Traceability (practice `ACP-ATB-002`) |
| `SP800-53-SA-8.32` | Sufficient Documentation. Implement the security design principle of sufficient documentation in [systems or system components]. | conceito: Architectural Decision And Solution Traceability (practice `ACP-ATB-002`) |
| `SP800-53-SA-8.4` | Partially Ordered Dependencies. Implement the security design principle of partially ordered dependencies in [systems or system components]. | conceito: Architectural Decision And Solution Traceability (practice `ACP-ATB-002`) |
| `SP800-53-SA-8.7` | Reduced Complexity. Implement the security design principle of reduced complexity in [systems or system components]. | conceito: Architectural Decision And Solution Traceability (practice `ACP-ATB-002`) |
| `SP800-53-SA-9.2` | Identification of Functions, Ports, Protocols, and Services. Require providers of the following external system services to identify the functions, ports, protocols, and other services required for th | conceito: Trust Boundary And Integration Review (practice `ACP-ITS-001`) |
| `SP800-53-SC-11.1` | Irrefutable Communications Path. Provide a trusted communications path that is irrefutably distinguishable from other communications paths; and Initiate the trusted communications path for communicati | conceito: Transport And Protocol Hardening (practice `ACP-ITS-003`) |
| `SP800-53-SC-35` | External Malicious Code Identification. Include system components that proactively seek to identify network-based malicious code or malicious websites. | conceito: Automated Dependency And Image Risk Gating (practice `ACP-SCBI-002`) |
| `SP800-53-SC-40` | Wireless Link Protection. Protect external and internal [organization-defined wireless links] from the following signal parameter attacks: [organization-defined types of signal parameter attacks or re | conceito: Transport And Protocol Hardening (practice `ACP-ITS-003`) |
| `SP800-53-SI-15` | Information Output Filtering. Validate information output from the following software programs and/or applications to ensure that the information is consistent with the expected content: [software pro | conceito: Pre-Use Data Validation Discipline (practice `ACP-IVF-004`) |
| `SP800-53-SI-19` | De-identification. Remove the following elements of personally identifiable information from datasets: [elements]; and Evaluate [frequency] for effectiveness of de-identification. | conceito: Operational Identity Binding And OIDC Use (practice `ACP-SPC-004`) |
| `SP800-53-SI-2.2` | Automated Flaw Remediation Status. Determine if system components have applicable security-relevant software and firmware updates installed using [automated mechanisms] [frequency]. | conceito: Automated Dependency And Image Risk Gating (practice `ACP-SCBI-002`) |
| `SP800-53-SI-22` | Information Diversity. Identify the following alternative sources of information for [essential functions and services]: [alternative information sources]; and Use an alternative information source fo | conceito: Trust-Boundary And Flow Review (practice `ACP-ATB-003`) |
| `SP800-53-SI-3.10` | Malicious Code Analysis. Employ the following tools and techniques to analyze the characteristics and behavior of malicious code: [tools and techniques]; and Incorporate the results from malicious cod | conceito: Automated Dependency And Image Risk Gating (practice `ACP-SCBI-002`) |
| `SP800-53-SI-4.17` | Integrated Situational Awareness. Correlate information from monitoring physical, cyber, and supply chain activities to achieve integrated, organization-wide situational awareness. | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `SP800-53-SI-4.19` | Risk for Individuals. Implement [additional monitoring] of individuals who have been identified by [sources] as posing an increased level of risk. | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `SP800-53-SI-4.5` | System-generated Alerts. Alert [personnel or roles] when the following system-generated indications of compromise or potential compromise occur: [compromise indicators]. | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `SP800-53-SI-5` | Security Alerts, Advisories, and Directives. Receive system security alerts, advisories, and directives from [external organizations] on an ongoing basis; Generate internal security alerts, advisories | conceito: Threat Traceability Into Requirements And Validation (practice `ACP-TMR-005`) |
| `SP800-53-SI-7.2` | Automated Notifications of Integrity Violations. Employ automated tools that provide notification to [personnel or roles] upon discovering discrepancies during integrity verification. | conceito: Artifact Signature And Provenance Validation (practice `ACP-SCBI-006`) |
| `SP800-53-SI-7.7` | Integration of Detection and Response. Incorporate the detection of the following unauthorized changes into the organizational incident response capability: [changes]. | conceito: Artifact Signature And Provenance Validation (practice `ACP-SCBI-006`) |
| `SP800-53-SI-8.2` | Automatic Updates. Automatically update spam protection mechanisms [frequency]. | conceito: Boundary Input Validation (practice `ACP-IVF-001`) |
| `SP800-53-SR-10` | Inspection of Systems or Components. Inspect the following systems or system components to detect tampering: [systems or system components]. | conceito: Staged Dynamic Testing And Gate Enforcement (practice `ACP-TSV-005`) |
| `SP800-53-SR-2` | Supply Chain Risk Management Plan. Develop a plan for managing supply chain risks associated with the research and development, design, manufacturing, acquisition, delivery, integration, operations an | conceito: Automated Dependency And Image Risk Gating (practice `ACP-SCBI-002`) |
| `SP800-53-SR-3.2` | Limitation of Harm. Employ the following controls to limit harm from potential adversaries identifying and targeting the organizational supply chain: [controls]. | conceito: Approved Source And Registry Governance (practice `ACP-SCBI-003`) |
| `SP800-53-SR-5` | Acquisition Strategies, Tools, and Methods. Employ the following acquisition strategies, contract tools, and procurement methods to protect against, identify, and mitigate supply chain risks: [strateg | conceito: Automated Dependency And Image Risk Gating (practice `ACP-SCBI-002`) |
| `SP800-53-SR-8` | Notification Agreements. Establish agreements and procedures with entities involved in the supply chain for the system, system component, or system service for the. | conceito: Threat Traceability Into Requirements And Validation (practice `ACP-TMR-005`) |
| `SP800-53-SR-9.1` | Multiple Stages of System Development Life Cycle. Employ anti-tamper technologies, tools, and techniques throughout the system development life cycle. | conceito: Artifact Signature And Provenance Validation (practice `ACP-SCBI-006`) |

---

## MITRE ATLAS — Adversarial Threat Landscape for AI Systems

**O que esta ES traz para este capítulo:** contribui 46 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `AML.CS0021` | ChatGPT Conversation Exfiltration. [Embrace the Red](https://embracethered.com/blog/) demonstrated that ChatGPT users' conversations can be exfiltrated via an indirect prompt injection. To execute the | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `AML.CS0025` | Web-Scale Data Poisoning: Split-View Attack. Many recent large-scale datasets are distributed as a list of URLs pointing to individual datapoints. The researchers show that many of these datasets are | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `AML.CS0042` | SesameOp: Novel backdoor uses OpenAI Assistants API for command and control. The Microsoft Incident Response - Detection and Response Team (DART) investigated a compromised system where a threat actor | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `AML.CS0045` | Data Exfiltration via an MCP Server used by Cursor. The Backslash Security Research Team demonstrated that a Model Context Protocol (MCP) tool can be used as a vector for an indirect prompt injection | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `AML.CS0054` | Data Exfiltration via Remote Poisoned MCP Tool. Researchers at Invariant Labs demonstrated that AI agents configured with remote Model Context Protocol (MCP) Tools can be vulnerable to model poisoning | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `AML.M0000` | Limit Public Release of Information. Limit the public release of technical information about the AI stack used in an organization's products or services. Technical knowledge of how AI is used can be l | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `AML.M0001` | Limit Model Artifact Release. Limit public release of technical project details including data, algorithms, model architectures, and model checkpoints that are used in production, or that are represen | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `AML.M0017` | AI Model Distribution Methods. Deploying AI models to edge devices can increase the attack surface of the system. Consider serving models in the cloud to reduce the level of access the adversary has t | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `AML.M0030` | Restrict AI Agent Tool Invocation on Untrusted Data. Untrusted data can contain prompt injections that invoke an AI agent's tools, potentially causing confidentiality, integrity or availability violat | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `AML.T0003` | Search Victim-Owned Websites. Adversaries may search websites owned by the victim for information that can be used during targeting. Victim-owned websites may contain technical details about their AI- | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `AML.T0008.002` | Domains. Adversaries may acquire domains that can be used during targeting. Domain names are the human readable names used to represent one or more IP addresses. They can be purchased or, in some case | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `AML.T0008.003` | Physical Countermeasures. Adversaries may acquire or manufacture physical countermeasures to aid or support their attack. These components may be used to disrupt or degrade the model, such as adversa | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `AML.T0010.003` | Model. AI-enabled systems often rely on open sourced models in various ways. Most commonly, the victim organization may be using these models for fine tuning. These models will be downloaded from an e | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `AML.T0010.005` | AI Agent Tool. Adversaries may target AI agent tools as a means to compromise a victim's AI supply chain. Tools add capabilities to AI agents, allowing them to interact with other services, connect to | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `AML.T0011.003` | Malicious Link. An adversary may rely upon a user clicking a malicious link in order to gain execution. Users may be subjected to social engineering to get them to click on a link that will lead to co | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `AML.T0015` | Evade AI Model. Adversaries can [Craft Adversarial Data](/techniques/AML.T0043) that prevents an AI model from correctly identifying the contents of the data or [Generate Deepfakes](/techniques/AML.T0 | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `AML.T0018` | Manipulate AI Model. Adversaries may directly manipulate an AI model to change its behavior or introduce malicious code. Manipulating a model gives the adversary a persistent change in the system. Thi | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `AML.T0018.000` | Poison AI Model. Adversaries may manipulate an AI model's weights to change it's behavior or performance, resulting in a poisoned model. Adversaries may poison a model by directly manipulating its wei | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `AML.T0018.001` | Modify AI Model Architecture. Adversaries may directly modify an AI model's architecture to re-define it's behavior. This can include adding or removing layers as well as adding pre or post-processing | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `AML.T0019` | Publish Poisoned Datasets. Adversaries may [Poison Training Data](/techniques/AML.T0020) and publish it to a public location. The poisoned dataset may be a novel dataset or a poisoned variant of an ex | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `AML.T0020` | Poison Training Data. Adversaries may attempt to poison datasets used by an AI model by modifying the underlying data or its labels. This allows the adversary to embed vulnerabilities in AI models tra | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `AML.T0024.000` | Infer Training Data Membership. Adversaries may infer the membership of a data sample or global characteristics of the data in its training set, which raises privacy concerns. Some strategies make use | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `AML.T0029` | Denial of AI Service. Adversaries may target AI-enabled systems with a flood of requests for the purpose of degrading or shutting down the service. Since many AI systems require significant amounts of | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `AML.T0031` | Erode AI Model Integrity. Adversaries may degrade the target model's performance with adversarial data inputs to erode confidence in the system over time. This can lead to the victim organization wast | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `AML.T0046` | Spamming AI System with Chaff Data. Adversaries may spam the AI system with chaff data that causes increase in the number of detections. This can cause analysts at the victim organization to waste tim | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `AML.T0058` | Publish Poisoned Models. Adversaries may publish a poisoned model to a public location such as a model registry or code repository. The poisoned model may be a novel model or a poisoned variant of an | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `AML.T0059` | Erode Dataset Integrity. Adversaries may poison or manipulate portions of a dataset to reduce its usefulness, reduce trust, and cause users to waste resources correcting errors. | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `AML.T0064` | Gather RAG-Indexed Targets. Adversaries may identify data sources used in retrieval augmented generation (RAG) systems for targeting purposes. By pinpointing these sources, attackers can focus on pois | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `AML.T0067` | LLM Trusted Output Components Manipulation. Adversaries may utilize prompts to a large language model (LLM) which manipulate various components of its response in order to make it appear trustworthy t | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `AML.T0067.000` | Citations. Adversaries may manipulate the citations provided in an AI system's response, in order to make it appear trustworthy. Variants include citing a providing the wrong citation, making up a new | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `AML.T0069.002` | System Prompt. Adversaries may discover a large language model's system instructions provided by the AI system builder to learn about the system's capabilities and circumvent its guardrails. | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `AML.T0079` | Stage Capabilities. Adversaries may upload, install, or otherwise set up capabilities that can be used during targeting. To support their operations, an adversary may need to take capabilities they de | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `AML.T0084.003` | Call Chains. Adversaries may extract call chains from AI agent configurations, which can reveal potentially targets for remote code execution (RCE) or other vulnerabilities. Vulnerable call chains oft | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `AML.T0086` | Exfiltration via AI Agent Tool Invocation. AI agent tools capable of performing write operations may be invoked to exfiltrate data to an adversary. Sensitive information can be encoded into the tool's | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `AML.T0093` | Prompt Infiltration via Public-Facing Application. An adversary may introduce malicious prompts into the victim's system via a public-facing application with the intention of it being ingested by an A | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `AML.T0097` | Virtualization/Sandbox Evasion. Adversaries may employ various means to detect and avoid virtualization and analysis environments. This may include changing behaviors based on the results of checks fo | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `AML.T0099` | AI Agent Tool Data Poisoning. Adversaries may place malicious content on a victim's system where it can be retrieved by an AI Agent Tool. This may be accomplished by placing documents in a location th | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `AML.T0101` | Data Destruction via AI Agent Tool Invocation. Adversaries may invoke an AI agent's tool capable of performing mutative operations to perform Data Destruction. Adversaries may destroy data and files o | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `AML.T0109` | AI Supply Chain Rug Pull. Adversaries may publish legitimate AI components or software, gain user adoption, then push an update with a malicious variant, leading to [AI Supply Chain Compromise](/techn | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `AML.T0110` | AI Agent Tool Poisoning. Adversaries may achieve persistence by poisoning tools used by AI agents including built-in tools or tools available to the agent via Model Context Protocol (MCP) connections. | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `AML.T0111` | AI Supply Chain Reputation Inflation. AI Supply Chain Reputation Inflation is the process of building or leveraging genuinely credible-looking trust signals to increase the perceived legitimacy of AI | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `AML.T0112.001` | AI Artifacts. Adversaries may achieve full system compromise by introducing malicious AI artifacts, such as models or data, that contain embedded malware or other malicious commands. AI artifacts are | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `AML.TA0002` | Reconnaissance. The adversary is trying to gather information about the AI system they can use to plan future operations. Reconnaissance consists of techniques that involve adversaries actively or pa | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `AML.TA0006` | Persistence. The adversary is trying to maintain their foothold via AI artifacts or software. Persistence consists of techniques that adversaries use to keep access to systems across restarts, change | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `AML.TA0008` | Discovery. The adversary is trying to figure out your AI environment. Discovery consists of techniques an adversary may use to gain knowledge about the system and internal network. These techniques h | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `AML.TA0011` | Impact. The adversary is trying to manipulate, interrupt, erode confidence in, or destroy your AI systems and data. Impact consists of techniques that adversaries use to disrupt availability or compr | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |

---

## MITRE CAPEC v3.9

**O que esta ES traz para este capítulo:** contribui 41 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `CAPEC-132` | Symlink Attack. Symlink Attack. An adversary positions a symbolic link in such a manner that the targeted user or application accesses the link's endpoint, assuming that it is accessing a file with th | conceito: Approved Source And Registry Governance (practice `ACP-SCBI-003`) |
| `CAPEC-143` | Detect Unpublicized Web Pages. Detect Unpublicized Web Pages. An adversary searches a targeted web site for web pages that have not been publicized. In doing this, the adversary may be able to gain ac | conceito: Secret Management Systems (mechanism `ACM-SPC-001`) |
| `CAPEC-144` | Detect Unpublicized Web Services. Detect Unpublicized Web Services. An adversary searches a targeted web site for web services that have not been publicized. This attack can be especially dangerous si | conceito: Secret Management Systems (mechanism `ACM-SPC-001`) |
| `CAPEC-154` | Resource Location Spoofing. Resource Location Spoofing. An adversary deceives an application or user and convinces them to request a resource from an unintended location. By spoofing the location, the | conceito: Approved Source And Registry Governance (practice `ACP-SCBI-003`) |
| `CAPEC-169` | Footprinting. Footprinting. An adversary engages in probing and exploration activities to identify constituents and properties of the target.. Prerequisites: An application must publicize identifiable | conceito: Secret Management Systems (mechanism `ACM-SPC-001`) |
| `CAPEC-170` | Web Application Fingerprinting. Web Application Fingerprinting. An attacker sends a series of probes to a web application in order to elicit version-dependent and type-dependent behavior that assists | conceito: Secret Management Systems (mechanism `ACM-SPC-001`) |
| `CAPEC-178` | Cross-Site Flashing. Cross-Site Flashing. An attacker is able to trick the victim into executing a Flash document that passes commands or calls to a Flash player browser plugin, allowing the attacker | conceito: Schema And Contract Validators (mechanism `ACM-IVF-003`) |
| `CAPEC-186` | Malicious Software Update. Malicious Software Update. An adversary uses deceptive methods to cause a user or an automated process to download and install dangerous code believed to be a valid update t | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `CAPEC-188` | Reverse Engineering. Reverse Engineering. An adversary discovers the structure, function, and composition of an object, resource, or system by using a variety of analysis techniques to effectively det | conceito: Secret Management Systems (mechanism `ACM-SPC-001`) |
| `CAPEC-201` | Serialized Data External Linking. Serialized Data External Linking. An adversary creates a serialized data file (e.g. XML, YAML, etc...) that contains an external data reference. Because serialized da | conceito: Message Integrity And Authorized Peer Policies (mechanism `ACM-ITS-004`) |
| `CAPEC-219` | XML Routing Detour Attacks. XML Routing Detour Attacks. An attacker subverts an intermediate system used to process XML content and forces the intermediate to modify and/or re-route the processing of | conceito: API Gateway With Mutual Authentication (mechanism `ACM-ITS-001`) |
| `CAPEC-221` | Data Serialization External Entities Blowup. Data Serialization External Entities Blowup. This attack takes advantage of the entity replacement property of certain data serialization languages (e.g., | conceito: Message Integrity And Authorized Peer Policies (mechanism `ACM-ITS-004`) |
| `CAPEC-224` | Fingerprinting. Fingerprinting. An adversary compares output from a target system to known indicators that uniquely identify specific details about the target. Most commonly, fingerprinting is done to | conceito: Secret Management Systems (mechanism `ACM-SPC-001`) |
| `CAPEC-293` | Traceroute Route Enumeration. Traceroute Route Enumeration. An adversary uses a traceroute utility to map out the route which data flows through the network in route to a target destination. Tracerout | conceito: Secret Management Systems (mechanism `ACM-SPC-001`) |
| `CAPEC-387` | Navigation Remapping To Propagate Malicious Content. Navigation Remapping To Propagate Malicious Content. An adversary manipulates either egress or ingress data from a client within an application fra | conceito: API Gateway With Mutual Authentication (mechanism `ACM-ITS-001`) |
| `CAPEC-414` | Pretexting via Delivery Person. Pretexting via Delivery Person. An adversary engages in pretexting behavior, assuming the role of a delivery person, to solicit information from target persons, or mani | conceito: Secret Management Systems (mechanism `ACM-SPC-001`) |
| `CAPEC-418` | Influence Perception of Reciprocation. Influence Perception of Reciprocation. An adversary uses a social engineering techniques to produce a sense of obligation in the target to perform a certain acti | conceito: Authentication And Federation Protocols (mechanism `ACM-IAT-001`) |
| `CAPEC-420` | Influence Perception of Scarcity. Influence Perception of Scarcity. The adversary leverages a perception of scarcity to persuade the target to perform an action or divulge information that is advantag | conceito: Authentication And Federation Protocols (mechanism `ACM-IAT-001`) |
| `CAPEC-423` | Influence Perception of Liking. Influence Perception of Liking. The adversary influences the target's actions by building a relationship where the target has a liking to the adversary. People are more | conceito: Authentication And Federation Protocols (mechanism `ACM-IAT-001`) |
| `CAPEC-425` | Target Influence via Framing. Target Influence via Framing. An adversary uses framing techniques to contextualize a conversation so that the target is more likely to be influenced by the adversary's p | conceito: Authentication And Federation Protocols (mechanism `ACM-IAT-001`) |
| `CAPEC-427` | Influence via Psychological Principles. Influence via Psychological Principles. The adversary shapes the target's actions or behavior by focusing on the ways human interact and learn, leveraging such | conceito: Authentication And Federation Protocols (mechanism `ACM-IAT-001`) |
| `CAPEC-444` | Development Alteration. Development Alteration. An adversary modifies a technology, product, or component during its development to acheive a negative impact once the system is deployed. The goal of t | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `CAPEC-448` | Embed Virus into DLL. Embed Virus into DLL. An adversary tampers with a DLL and embeds a computer virus into gaps between legitimate machine instructions. These gaps may be the result of compiler opti | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `CAPEC-51` | Poison Web Service Registry. Poison Web Service Registry. SOA and Web Services often use a registry to perform look up, get schema information, and metadata about services. A poisoned registry can red | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `CAPEC-520` | Counterfeit Hardware Component Inserted During Product Assembly. Counterfeit Hardware Component Inserted During Product Assembly. An adversary with either direct access to the product assembly process | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `CAPEC-530` | Provide Counterfeit Component. Provide Counterfeit Component. An attacker provides a counterfeit component during the procurement process of a lower-tier component supplier to a sub-system developer o | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `CAPEC-548` | Contaminate Resource. Contaminate Resource. An adversary contaminates organizational information systems (including devices and networks) by causing them to handle information of a classification/sens | conceito: Code Review For Input And Error Discipline (mechanism `ACM-IVF-001`) |
| `CAPEC-573` | Process Footprinting. Process Footprinting. An adversary exploits functionality meant to identify information about the currently running processes on the target system to an authorized user. By knowi | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `CAPEC-575` | Account Footprinting. Account Footprinting. An adversary exploits functionality meant to identify information about the domain accounts and their permissions on the target system to an authorized user | conceito: Secret Management Systems (mechanism `ACM-SPC-001`) |
| `CAPEC-580` | System Footprinting. System Footprinting. An adversary engages in active probing and exploration activities to determine security information about a remote target system. Often times adversaries will | conceito: Secret Management Systems (mechanism `ACM-SPC-001`) |
| `CAPEC-581` | Security Software Footprinting. Security Software Footprinting. Adversaries may attempt to get a listing of security tools that are installed on the system and their configurations. This may include s | conceito: Secret Management Systems (mechanism `ACM-SPC-001`) |
| `CAPEC-623` | Compromising Emanations Attack. Compromising Emanations Attack. Compromising Emanations (CE) are defined as unintentional signals which an attacker may intercept and analyze to disclose the informatio | conceito: Secret Management Systems (mechanism `ACM-SPC-001`) |
| `CAPEC-643` | Identify Shared Files/Directories on System. Identify Shared Files/Directories on System. An adversary discovers connections between systems by exploiting the target system's standard practice of reve | conceito: Secret Management Systems (mechanism `ACM-SPC-001`) |
| `CAPEC-646` | Peripheral Footprinting. Peripheral Footprinting. Adversaries may attempt to obtain information about attached peripheral devices and components connected to a computer system. Examples may include di | conceito: Secret Management Systems (mechanism `ACM-SPC-001`) |
| `CAPEC-647` | Collect Data from Registries. Collect Data from Registries. An adversary exploits a weakness in authorization to gather system-specific data and sensitive information within a registry (e.g., Windows | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `CAPEC-655` | Avoid Security Tool Identification by Adding Data. Avoid Security Tool Identification by Adding Data. An adversary adds data to a file to increase the file size beyond what security tools are capable | conceito: Code Review For Input And Error Discipline (mechanism `ACM-IVF-001`) |
| `CAPEC-662` | Adversary in the Browser (AiTB). Adversary in the Browser (AiTB). An adversary exploits security vulnerabilities or inherent functionalities of a web browser, in order to manipulate traffic between tw | conceito: API Gateway With Mutual Authentication (mechanism `ACM-ITS-001`) |
| `CAPEC-671` | Requirements for ASIC Functionality Maliciously Altered. Requirements for ASIC Functionality Maliciously Altered. An adversary with access to functional requirements for an application specific integr | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `CAPEC-690` | Metadata Spoofing. Metadata Spoofing. An adversary alters the metadata of a resource (e.g., file, directory, repository, etc.) to present a malicious resource as legitimate/credible.. Prerequisites: I | conceito: Artifact Signing And Attestation (mechanism `ACM-SCBI-004`) |
| `CAPEC-691` | Spoof Open-Source Software Metadata. Spoof Open-Source Software Metadata. An adversary spoofs open-source software metadata in an attempt to masquerade malicious software as popular, maintained, and t | conceito: Artifact Signing And Attestation (mechanism `ACM-SCBI-004`) |
| `CAPEC-692` | Spoof Version Control System Commit Metadata. Spoof Version Control System Commit Metadata. An adversary spoofs metadata pertaining to a Version Control System (VCS) (e.g., Git) repository's commits t | conceito: Artifact Signing And Attestation (mechanism `ACM-SCBI-004`) |

---

## PCI DSS v4.0.1

**O que esta ES traz para este capítulo:** contribui 35 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `PCI-1.1.2` | Roles and responsibilities for performing 1.1.2.a Examine documentation to verify that. Roles and responsibilities for performing 1.1.2.a Examine documentation to verify that | conceito: Versioned Diagrams And ADR Records (mechanism `ACM-ATB-001`) |
| `PCI-1.4.3` | Anti-spoofing measures are implemented to 1.4.3 Examine vendor documentation and. Anti-spoofing measures are implemented to 1.4.3 Examine vendor documentation and helps to, amo | conceito: Versioned Diagrams And ADR Records (mechanism `ACM-ATB-001`) |
| `PCI-10.3.4` | File integrity monitoring or change-detection 10.3.4 Examine system settings, monitored files,. File integrity monitoring or change-detection 10.3.4 Examine system settings, monitored files, | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `PCI-10.7.1` | Additional requirement for service 10.7.1.a Additional testing procedure for. Additional requirement for service 10.7.1.a Additional testing procedure for | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `PCI-11.1.2` | Roles and responsibilities for performing 11.1.2.a Examine documentation to verify that. Roles and responsibilities for performing 11.1.2.a Examine documentation to verify that assign | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `PCI-11.4.6` | Additional requirement for service 11.4.6.a Additional testing procedure for. Additional requirement for service 11.4.6.a Additional testing procedure for | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `PCI-12.1.1` | An overall information security policy is: 12.1.1 Examine the information security policy and. An overall information security policy is: 12.1.1 Examine the information security policy and p | conceito: Threat Model Versioning Controls (mechanism `ACM-TMR-003`) |
| `PCI-12.1.4` | Responsibility for information security is 12.1.4 Examine the information security policy to. Responsibility for information security is 12.1.4 Examine the information security policy to | conceito: Threat Model Versioning Controls (mechanism `ACM-TMR-003`) |
| `PCI-12.10.3` | Specific personnel are designated to be 12.10.3 Examine documentation and interview. Specific personnel are designated to be 12.10.3 Examine documentation and interview person | conceito: Threat Model Versioning Controls (mechanism `ACM-TMR-003`) |
| `PCI-12.10.6` | The security incident response plan is 12.10.6.a Examine policies and procedures to res. The security incident response plan is 12.10.6.a Examine policies and procedures to r | conceito: Threat Model Versioning Controls (mechanism `ACM-TMR-003`) |
| `PCI-12.3.1` | specified at Requirement 12.3.1.. specified at Requirement 12.3.1. | conceito: Threat Model Versioning Controls (mechanism `ACM-TMR-003`) |
| `PCI-12.3.2` | A targeted risk analysis is performed for each 12.3.2 Examine the documented targeted risk-. A targeted risk analysis is performed for each 12.3.2 Examine the documented targeted risk- me | conceito: Structured Threat Analysis Frameworks (mechanism `ACM-TMR-002`) |
| `PCI-12.3.4` | Hardware and software technologies in use 12.3.4 Examine documentation for the review of. Hardware and software technologies in use 12.3.4 Examine documentation for the review of co | conceito: Structured Threat Analysis Frameworks (mechanism `ACM-TMR-002`) |
| `PCI-12.4.1` | Additional requirement for service 12.4.1 Additional testing procedure for service c. Additional requirement for service 12.4.1 Additional testing procedure for service | conceito: Threat Model Versioning Controls (mechanism `ACM-TMR-003`) |
| `PCI-12.4.2` | Additional requirement for service 12.4.2.a Additional testing procedure for. Additional requirement for service 12.4.2.a Additional testing procedure for proc | conceito: Threat Model Versioning Controls (mechanism `ACM-TMR-003`) |
| `PCI-12.5.2` | PCI DSS scope is documented and 12.5.2.a Examine documented results of scope. PCI DSS scope is documented and 12.5.2.a Examine documented results of scope e | conceito: Threat Representation Models (mechanism `ACM-TMR-001`) |
| `PCI-12.5.3` | Additional requirement for service 12.5.3.a Additional testing procedure for. Additional requirement for service 12.5.3.a Additional testing procedure for define t | conceito: Threat Mitigation Linkage Controls (mechanism `ACM-TMR-005`) |
| `PCI-12.6.1` | A formal security awareness program is 12.6.1 Examine the security awareness program to. A formal security awareness program is 12.6.1 Examine the security awareness program to | conceito: Explicit Threat Disposition Register (mechanism `ACM-TMR-004`) |
| `PCI-12.6.2` | The security awareness program is: 12.6.2 Examine security awareness program ar. The security awareness program is: 12.6.2 Examine security awareness program | conceito: Threat Model Versioning Controls (mechanism `ACM-TMR-003`) |
| `PCI-12.6.3` | Personnel receive security awareness 12.6.3.a Examine security awareness program. Personnel receive security awareness 12.6.3.a Examine security awareness program informa | conceito: Threat Model Versioning Controls (mechanism `ACM-TMR-003`) |
| `PCI-12.7.1` | Potential personnel who will have access to 12.7.1 Interview responsible Human Resource po. Potential personnel who will have access to 12.7.1 Interview responsible Human Resource | conceito: Threat Model Versioning Controls (mechanism `ACM-TMR-003`) |
| `PCI-12.8.1` | A list of all third-party service providers 12.8.1.a Examine policies and procedures to verify. A list of all third-party service providers 12.8.1.a Examine policies and procedures to verify p | conceito: Threat Model Versioning Controls (mechanism `ACM-TMR-003`) |
| `PCI-12.8.4` | A program is implemented to monitor TPSPs’ 12.8.4.a Examine policies and procedures to verify. A program is implemented to monitor TPSPs’ 12.8.4.a Examine policies and procedures to verify e | conceito: Threat Mitigation Linkage Controls (mechanism `ACM-TMR-005`) |
| `PCI-12.8.5` | Information is maintained about which PCI 12.8.5.a Examine policies and procedures to verify. Information is maintained about which PCI 12.8.5.a Examine policies and procedures to verify PCI | conceito: Threat Mitigation Linkage Controls (mechanism `ACM-TMR-005`) |
| `PCI-12.9.1` | Additional requirement for service 12.9.1 Additional testing procedure for service r. Additional requirement for service 12.9.1 Additional testing procedure for service | conceito: Threat Model Versioning Controls (mechanism `ACM-TMR-003`) |
| `PCI-12.9.2` | Additional requirement for service 12.9.2 Additional testing procedure for service. Additional requirement for service 12.9.2 Additional testing procedure for service | conceito: Threat Model Versioning Controls (mechanism `ACM-TMR-003`) |
| `PCI-2.1.2` | Roles and responsibilities for performing 2.1.2.a Examine documentation to verify that. Roles and responsibilities for performing 2.1.2.a Examine documentation to verify that | conceito: Release Promotion Controls (mechanism `ACM-RPR-001`) |
| `PCI-3.7.9` | Additional requirement for service 3.7.9 Additional testing procedure for service. Additional requirement for service 3.7.9 Additional testing procedure for service tran | conceito: Secret Management Systems (mechanism `ACM-SPC-001`) |
| `PCI-6.2.1` | Bespoke and custom software are developed 6.2.1 Examine documented software development r. Bespoke and custom software are developed 6.2.1 Examine documented software development | conceito: Code Review For Input And Error Discipline (mechanism `ACM-IVF-001`) |
| `PCI-6.2.4` | Software engineering techniques or other 6.2.4 Examine documented procedures and. Software engineering techniques or other 6.2.4 Examine documented procedures and vulner | conceito: Schema And Contract Validators (mechanism `ACM-IVF-003`) |
| `PCI-6.3.1` | Security vulnerabilities are identified and 6.3.1.a Examine policies and procedures for. Security vulnerabilities are identified and 6.3.1.a Examine policies and procedures for | conceito: Schema And Contract Validators (mechanism `ACM-IVF-003`) |
| `PCI-6.3.2` | An inventory of bespoke and custom software, 6.3.2.a Examine documentation and interview. An inventory of bespoke and custom software, 6.3.2.a Examine documentation and interview custom | conceito: Schema And Contract Validators (mechanism `ACM-IVF-003`) |
| `PCI-8.2.3` | Additional requirement for service 8.2.3 Additional testing procedure for service. Additional requirement for service 8.2.3 Additional testing procedure for service pre | maturity (weak): Maturidade - Arquitetura Segura > OWASP DSOMM - Architecture, Requirements, Risk |
| `PCI-REQ-12` | Support Information Security with Organizational Policies and Programs. Requirement 12: Support Information Security with Organizational Policies and Programs. Goal: Maintain an Information Security P | conceito: Threat Model Versioning Controls (mechanism `ACM-TMR-003`) |
| `PCI-REQ-6` | Develop and Maintain Secure Systems and Software. Requirement 6: Develop and Maintain Secure Systems and Software. Goal: Maintain a Vulnerability Management Program. | conceito: Schema And Contract Validators (mechanism `ACM-IVF-003`) |

---

## OWASP SAMM v2.1

**O que esta ES traz para este capítulo:** contribui 32 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `SAMM-ACTIVITY-D_SR_1_A` | Identify security requirements | conceito: Requirements Registry And Derivation Traceability (mechanism `ACM-TMR-007`) |
| `SAMM-ACTIVITY-D_SR_1_B` | Perform vendor assessments | conceito: Requirements Registry And Derivation Traceability (mechanism `ACM-TMR-007`) |
| `SAMM-ACTIVITY-D_SR_2_A` | Standardize and integrate security requirements. Standardize and integrate security requirements. Security requirements can originate from other sources including policies and legislation, known probl | conceito: Compliance Monitoring And Regulatory Change Feeds (mechanism `ACM-TMR-008`) |
| `SAMM-ACTIVITY-D_SR_2_B` | Discuss security responsibilities with suppliers. Discuss security responsibilities with suppliers. Increase your confidence in the capability of your suppliers for software security. Discuss concrete | conceito: Threat Mitigation Linkage Controls (mechanism `ACM-TMR-005`) |
| `SAMM-ACTIVITY-D_SR_3_A` | Develop a security requirements framework. Develop a security requirements framework. Setup a security requirements framework to help projects elicit an appropriate and complete requirements set for t | conceito: Compliance Monitoring And Regulatory Change Feeds (mechanism `ACM-TMR-008`) |
| `SAMM-ACTIVITY-D_TA_1_A` | Perform application risk assessments. Perform application risk assessments. Use a simple method to evaluate the application risk per application, estimating the potential business impact that it poses | conceito: Structured Threat Analysis Frameworks (mechanism `ACM-TMR-002`) |
| `SAMM-ACTIVITY-D_TA_1_B` | Perform basic threat modeling. Perform basic threat modeling. Threat modeling is a structured activity for identifying, evaluating, and managing system threats, architectural design flaws, and recomme | conceito: Structured Threat Analysis Frameworks (mechanism `ACM-TMR-002`) |
| `SAMM-ACTIVITY-D_TA_2_A` | Create an extensive | conceito: Structured Threat Analysis Frameworks (mechanism `ACM-TMR-002`) |
| `SAMM-ACTIVITY-D_TA_2_B` | Standardize and scale threat modeling. Standardize and scale threat modeling. Use a standardized threat modeling methodology for your organization and align this on your application risk levels. Think | conceito: Structured Threat Analysis Frameworks (mechanism `ACM-TMR-002`) |
| `SAMM-ACTIVITY-D_TA_3_B` | Optimize threat modeling. Optimize threat modeling. Threat modeling is integrated into your SDLC and has become part of the developer security culture. Reusable risk patterns, comprising related threa | conceito: Structured Threat Analysis Frameworks (mechanism `ACM-TMR-002`) |
| `SAMM-ACTIVITY-G_EG_1_A` | Train all stakeholders for awareness. Train all stakeholders for awareness. Conduct security awareness training for all roles currently involved in the management, development, testing, or auditing of | conceito: Explicit Threat Disposition Register (mechanism `ACM-TMR-004`) |
| `SAMM-ACTIVITY-G_EG_2_B` | Implement centers of excellence. Implement centers of excellence. The organization implements a formal secure coding center of excellence, with architects and senior developers representing the differ | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `SAMM-ACTIVITY-G_EG_3_A` | Implement a formal training program requiring anyone involved with the software development lifecycle to complete appropriate role and technology-specific training as part of the onboarding process | conceito: Reviewer Accountability And Consistency Gates (mechanism `ACM-TMR-006`) |
| `SAMM-ACTIVITY-G_EG_3_B` | Establish a security community. Establish a security community. Security is the responsibility of all employees, not just the Information Security team. Deploy communication and knowledge sharing plat | conceito: Reviewer Accountability And Consistency Gates (mechanism `ACM-TMR-006`) |
| `SAMM-ACTIVITY-G_PC_1_A` | Define policies | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `SAMM-ACTIVITY-G_PC_1_B` | Identify compliance requirements | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `SAMM-ACTIVITY-G_PC_2_A` | Develop test procedures. Develop test procedures. To assist with the ongoing implementation and verification of compliance with policies and standards, develop application security and appropriate tes | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `SAMM-ACTIVITY-G_PC_2_B` | test scripts to establish | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `SAMM-ACTIVITY-G_PC_3_A` | Measure compliance to policies and standards. Measure compliance to policies and standards. Develop a program to measure each application's compliance with existing policies and standards. Mandatory r | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `SAMM-ACTIVITY-G_PC_3_B` | test scripts help determine the status of compliance | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `SAMM-ACTIVITY-G_SM_1_A` | Identify the organization's risk appetite | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `SAMM-ACTIVITY-G_SM_2_A` | Define the security strategy. Define the security strategy. Based on the magnitude of assets, threats, and risk tolerance, develop a security strategic plan and budget to address business priorities a | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `SAMM-ACTIVITY-G_SM_2_B` | Set strategic KPIs. Set strategic KPIs. Once the organization has defined its application security metrics, collect enough information to establish realistic goals. Test identified metrics to ensure y | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `SAMM-ACTIVITY-G_SM_3_A` | Align security and business strategies. Align security and business strategies. You review the application security plan periodically for ongoing applicability and support of the organization's evolvi | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `SAMM-ACTIVITY-G_SM_3_B` | Drive the security program through metrics. Drive the security program through metrics. Define guidelines for influencing the Application Security program based on the KPIs and other application secur | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `SAMM-ACTIVITY-O_EM_1_B` | Identify applications and third-party components which need to be updated | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |
| `SAMM-ACTIVITY-V_AA_1_B` | Evaluate architecture for typical threats | conceito: Architecture Review Gates (mechanism `ACM-ATB-004`) |
| `SAMM-ACTIVITY-V_AA_2_B` | Structurally verify the architecture for identified threats. Structurally verify the architecture for identified threats. Systematically review each threat identified during the Threat Assessment acti | conceito: Architecture Review Gates (mechanism `ACM-ATB-004`) |
| `SAMM-ACTIVITY-V_RT_1_A` | Test the effectiveness of security controls | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `SAMM-ACTIVITY-V_RT_2_A` | Define | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `SAMM-ACTIVITY-V_RT_2_B` | Define | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `SAMM-ACTIVITY-V_RT_3_B` | Perform security stress testing | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |

---

## NIST SSDF (SP 800-218 v1.1)

**O que esta ES traz para este capítulo:** contribui 16 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `SSDF-PRACTICE-PO.1` | Define Security Requirements for Software Development. Ensure that security requirements for software development are known at all times so that they can be taken into account throughout the SDLC and | conceito: Requirements Registry And Derivation Traceability (mechanism `ACM-TMR-007`) |
| `SSDF-PRACTICE-PO.2` | Implement Roles and Responsibilities. Ensure that everyone inside and outside of the organization involved in the SDLC is prepared to perform their SDLC -related roles and responsibilities throughout | conceito: Explicit Threat Disposition Register (mechanism `ACM-TMR-004`) |
| `SSDF-PRACTICE-PO.3` | Implement Supporting Toolchains. Use automation to reduce human effort and improve the accuracy, reproducibility, usability, and comprehensiveness of security practices throughout the SDLC, as well as | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `SSDF-PRACTICE-PO.4` | Define and Use Criteria for Software Security Checks. Help ensure that the software resulting from the SDLC meets the organization’s expectations by defining and using criteria for checking the softwa | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `SSDF-PRACTICE-PW.1` | Design Software to Meet Security Requirements and Mitigate Security Risks. Identify and evaluate the security requirements for the software | conceito: Threat Representation Models (mechanism `ACM-TMR-001`) |
| `SSDF-PRACTICE-PW.2` | Review the Software Design to Verify Compliance with Security Requirements and Risk Information. Help ensure that the software will meet the security requirements and satisfactorily address the identi | conceito: Architecture Review Gates (mechanism `ACM-ATB-004`) |
| `SSDF-PRACTICE-RV.1` | Identify and Confirm Vulnerabilities on an Ongoing Basis. Help ensure that vulnerabilities are identified more quickly so that they can be remediated more quickly in accordance with risk , reducing th | conceito: Findings Workflow And Exception Governance (mechanism `ACM-TSV-004`) |
| `SSDF-PRACTICE-RV.2` | Assess, Prioritize | conceito: Findings Workflow And Exception Governance (mechanism `ACM-TSV-004`) |
| `SSDF-TASK-PO.1.1` | Identify | conceito: Requirements Registry And Derivation Traceability (mechanism `ACM-TMR-007`) |
| `SSDF-TASK-PO.1.2` | Identify | conceito: Requirements Registry And Derivation Traceability (mechanism `ACM-TMR-007`) |
| `SSDF-TASK-PO.4.1` | Define criteria for software security checks and track throughout t he SDLC. | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `SSDF-TASK-PW.1.1` | Use forms of risk modeling – such as threat modeling, attack modeling, or attack surface mapping – to help assess the security risk for the software. | conceito: Structured Threat Analysis Frameworks (mechanism `ACM-TMR-002`) |
| `SSDF-TASK-PW.1.2` | Track and maintain the software’s security requirements, risks, and design decisions. | conceito: Compliance Monitoring And Regulatory Change Feeds (mechanism `ACM-TMR-008`) |
| `SSDF-TASK-PW.4.2` | Create and maintain well -secured software components in -house following SDLC processes to meet common internal software development needs that cannot be better met by third-party software components | conceito: Approved Source And Registry Governance (practice `ACP-SCBI-003`) |
| `SSDF-TASK-RV.2.1` | Analyze each vulnerability to gather sufficient information about risk to plan its remediation or other risk response . | conceito: Findings Workflow And Exception Governance (mechanism `ACM-TSV-004`) |
| `SSDF-TASK-RV.2.2` | Plan and implement risk responses for vulnerabilities . | conceito: Explicit Threat Disposition Register (mechanism `ACM-TMR-004`) |

---

## NIST AI RMF 1.0

**O que esta ES traz para este capítulo:** contribui 15 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `NIST-AI-RMF-GOVERN-1.3` | Processes, procedures, and practices are in place. measuring, and to determine the needed level of risk management activities based managing of AI on the organization’s risk tolerance. risks are in pl | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `NIST-AI-RMF-GOVERN-1.5` | Ongoing monitoring and periodic review of the. risk management process and its outcomes are planned and or- ganizational roles and responsibilities clearly defined, including determining the frequency | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `NIST-AI-RMF-GOVERN-2` | GOVERN 2.1: Roles and responsibilities and lines of communi-. Accountability cation related to mapping, measuring, and managing AI risks are structures are in documented and are clear to individuals a | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `NIST-AI-RMF-GOVERN-3.2` | Policies and procedures are in place to define and. prioritized in the mapping, differentiate roles and responsibilities for human-AI configura- measuring, and tions and oversight of AI systems. manag | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `NIST-AI-RMF-MANAGE-1` | AI MANAGE 1.1: A determination is made as to whether the AI. risks based on system achieves its intended purposes and stated objectives and assessments and whether its development or dep | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `NIST-AI-RMF-MANAGE-1.3` | Responses to the AI risks deemed high priority, as. functions are identified by the MAP function, are developed, planned, and doc- prioritized, umented. Risk response options can include mitigating, t | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `NIST-AI-RMF-MANAGE-2.3` | Procedures are followed to respond to and recover. implemented, from a previously unknown risk when it is identified. documented, and informed by input MANAGE 2.4: Mechanisms are in place and applied, | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `NIST-AI-RMF-MANAGE-3` | AI MANAGE 3.1: AI risks and benefits from third-party resources. risks and benefits are regularly monitored, and risk controls are applied and from third-party documented. entities are MANAG | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `NIST-AI-RMF-MANAGE-4` | Risk MANAGE 4.1: Post-deployment AI system monitoring plans. treatments, are implemented, including mechanisms for capturing and eval- including response uating input from users and other rel | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `NIST-AI-RMF-MAP-1.6` | System requirements (e.g., “the system shall respect. the privacy of its users”) are elicited from and understood by rel- evant AI actors. Design decisions take socio-technical implica- tions into acc | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `NIST-AI-RMF-MAP-4` | Risks and MAP 4.1: Approaches for mapping AI technology and legal risks. benefits are mapped of its components – including the use of third-party data or soft- for all components ware – are in | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `NIST-AI-RMF-MAP-5.2` | monitor AI risk | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `NIST-AI-RMF-MEASURE-2.3` | AI system performance or assurance criteria. are measured qualitatively or quantitatively and demonstrated for conditions similar to deployment setting(s). Measures are documented. | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `NIST-AI-RMF-MEASURE-2.6` | The AI system is evaluated regularly for safety. risks – as identified in the MAP function. The AI system to be de- ployed is demonstrated to be safe, its residual negative risk does not exceed the ri | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `NIST-AI-RMF-MEASURE-4.3` | Measurable performance improvements or de-. clines based on consultations with relevant AI actors, in- cluding affected communities, and field data about context- relevant risks and trustworthiness ch | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |

---

## NIST AI 100-2 e2025 — Adversarial Machine Learning Taxonomy

**O que esta ES traz para este capítulo:** contribui 12 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `NIST-AI-100-2-E2025-2.1` | Attack Classification. Figure 1 introduces a taxonomy of attacks in AML on PredAI systems, based on attacker goals and objectives, capabilities, and knowledge. Model Poisoning Model Control Query Acce | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `NIST-AI-100-2-E2025-2.3.1` | Availability Poisoning. [NISTAML.013] [Back to Index] The first poisoning attacks discovered in cybersecurity applications were availability attacks against worm signature generation and spam classifi | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `NIST-AI-100-2-E2025-2.3.4` | Model Poisoning. [NISTAML.011, NISTAML.026] [Back to Index] Model poisoning attacks attempt to directly modify the trained ML model to inject mali- cious functionality into it. In centralized learning | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `NIST-AI-100-2-E2025-3.1.2` | Attacker Goals and Objectives. As with PredAI, attacker objectives can be classified broadly along the dimensions of avail- ability, integrity, and privacy, along with a new, GenAI-specific category o | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `NIST-AI-100-2-E2025-3.2` | Supply Chain Attacks and Mitigations. [NISTAML.05] [Back to Index] Since AI is software, it inherits many of the vulnerabilities of the traditional software sup- ply chain, such as reliance on third-p | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `NIST-AI-100-2-E2025-3.2.2` | Model Poisoning Attacks. [NISTAML.051] [Back to Index] In GenAI, it is common for developers to use foundation models developed by third parties. Attackers can take advantage of this fact by offering | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `NIST-AI-100-2-E2025-3.2.3` | Mitigations. GenAI poisoning mitigations largely overlap with PredAI poisoning mitigations (see Sec. 2.3). For preventing data poisoning with web-scale data dependencies, this includes ver- March 2025 | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `NIST-AI-100-2-E2025-3.4.2` | Integrity Attacks. [NISTAML.027] [Back to Index] Through indirect prompt injection, attackers can use malicious resources to prompt GenAI systems to become untrustworthy and generate content that devi | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `NIST-AI-100-2-E2025-3.4.3` | Privacy Compromise. Attackers can use indirect prompt injection attacks to compromise the privacy of a GenAI system or its primary users. For example, attackers could use indirect prompt injection att | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `NIST-AI-100-2-E2025-4.1.2` | Theoretical Limitations on Adversarial Robustness. Given the multitude of powerful attacks, appropriate mitigations must be designed before AI systems are deployed in critical domains. This challenge | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `NIST-AI-100-2-E2025-4.1.3` | Evaluation. Another general problem of AML mitigations for both evasion and poisoning attacks is the lack of reliable benchmarks, which causes results from AML papers to be routinely incom- parable, a | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `NIST-AI-100-2-E2025-4.2.1` | The Scale Challenge. Data is fundamentally important for training models. Recent trends in GenAI have been towards significant investment in larger models and larger datasets for training them. Few de | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |

---

## OWASP DSOMM

**O que esta ES traz para este capítulo:** contribui 10 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `DSOMM-ACTIVITY-0B28367B75A04BAEA9263725C1BF9BB0` | Security consulting on request. Security consulting on request Security consulting on request allows teams to seek expert advice on security-related questions or challenges as they arise. This support | conceito: Explicit Threat Disposition Register (mechanism `ACM-TMR-004`) |
| `DSOMM-ACTIVITY-10E23A8C22FF4487A70687CCC9D0798E` | Monitoring of costs. Monitoring of costs Not monitoring costs might lead to unexpected high resource consumption and a high invoice. Implement cost budgets. Setting of an alert threshold and sending o | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `DSOMM-ACTIVITY-2B7CC923BDAF43E38FB4A995B7783969` | Treatment of defects per protection requirement. Treatment of defects per protection requirement The protection requirements for an application should consider: - Data criticality - Application access | conceito: Findings Workflow And Exception Governance (mechanism `ACM-TSV-004`) |
| `DSOMM-ACTIVITY-47419324E263415B815DE7161B6B905E` | Conduction of simple threat modeling on technical level. Conduction of simple threat modeling on technical level # OWASP SAMM Description Threat modeling is a structured activity for identifying, eval | conceito: Structured Threat Analysis Frameworks (mechanism `ACM-TMR-002`) |
| `DSOMM-ACTIVITY-48F97F31931C46EB9B3EE2FEC0CD0426` | Conduction of simple threat modeling on business level. Conduction of simple threat modeling on business level Business related threats are discovered too late in the development and deployment proces | conceito: Structured Threat Analysis Frameworks (mechanism `ACM-TMR-002`) |
| `DSOMM-ACTIVITY-6217FE115ED74CF49DE4555BCFA6FE87` | Each team has a security champion. Each team has a security champion Implement a program where each software development team has a member considered a "Security Champion" who is the liaison between I | conceito: Reviewer Accountability And Consistency Gates (mechanism `ACM-TMR-006`) |
| `DSOMM-ACTIVITY-72737130472C498480F89AB2F1C2ED5D` | Determining the protection requirement. Determining the protection requirement Not defining the protection requirement of applications can lead to wrong prioritization, delayed remediation of critical | conceito: Requirements Registry And Derivation Traceability (mechanism `ACM-TMR-007`) |
| `DSOMM-ACTIVITY-AC8730A2CCC0465C9550D91EDAE9D5EE` | Require status checks to pass. Require status checks to pass Organizations risk introducing broken builds, quality issues, and security vulnerabilities into their codebase. Mandate passing of security | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `DSOMM-ACTIVITY-B597928E54D648A5A8068003DCD56AAB` | App. Hardening Level 1 (50%). App. Hardening Level 1 (50%) To tackle the security of code developed in-house, OWASP offers an extensive collection of [Cheatsheets](https://cheatsheetseries.owasp.org/) | conceito: Code Review For Input And Error Discipline (mechanism `ACM-IVF-001`) |
| `DSOMM-ACTIVITY-CF81922530CB47028E3260225EEDC33D` | App. Hardening Level 1. App. Hardening Level 1 To tackle the security of code developed in-house, OWASP offers an extensive collection of [Cheatsheets](https://cheatsheetseries.owasp.org/) demonstrati | conceito: Code Review For Input And Error Discipline (mechanism `ACM-IVF-001`) |

---

## PCI Secure SLC v1.1

**O que esta ES traz para este capítulo:** contribui 10 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `PCISSLC-1.2` | Software security responsibilities are assigned. Software security responsibilities clearly defined and assigned to appropriate individuals or teams including development personnel | conceito: Threat Disposition And Accepted Risk Governance (practice `ACP-TMR-004`) |
| `PCISSLC-1.3` | Software development personnel maintain skills in software security. Mature process for managing and maintaining software security skills; skills required for each role clearly defined; annual review | conceito: Threat Disposition And Accepted Risk Governance (practice `ACP-TMR-004`) |
| `PCISSLC-10.1` | Change summary provided to stakeholders for all software updates. Mature process to communicate all software changes; clear summary of functionality impacted; change details accessible to stakeholders | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `PCISSLC-2.1` | Regulatory and industry security and compliance requirements identified and monitored. Mature process to identify and monitor external regulatory and industry security and compliance requirements; rev | conceito: Compliance Monitoring And Regulatory Change Feeds (mechanism `ACM-TMR-008`) |
| `PCISSLC-2.2` | Software security policy defined and establishes rules and goals. Software security policy communicated to all vendor personnel; covers all control objectives; approved by senior leadership | conceito: Threat Disposition And Accepted Risk Governance (practice `ACP-TMR-004`) |
| `PCISSLC-2.4` | Software security assurance processes implemented throughout entire lifecycle. Security assurance processes defined, implemented and maintained; checkpoints throughout SDLC | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `PCISSLC-3.1` | Critical assets are identified and classified. Mature process to identify and classify critical assets; CIA requirements for each defined; inventory maintained | conceito: Threat Representation Models (mechanism `ACM-TMR-001`) |
| `PCISSLC-9.1` | Communication channels defined for reporting and receiving security information. Bidirectional communication channels for security issues; stakeholders can report issues and receive timely updates; re | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `PCISSLC-9.2` | Stakeholders notified about security updates in a timely manner. Mature process exists to notify stakeholders about security updates in a timely manner | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `PCISSLC-9.3` | Mitigation instructions provided when security updates not readily available. Instructions for mitigating threat or reducing impact when timely patch not available; risk mitigation provided to stakeho | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |

---

## CIS Controls v8.1.2

**O que esta ES traz para este capítulo:** contribui 6 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `CIS-15.4` | Ensure Service Provider Contracts Include Security Requirements. Ensure service provider contracts include security requirements. Example requirements may include minimum security program requirements | conceito: Trust Boundary Models (mechanism `ACM-ITS-002`) |
| `CIS-15.6` | Monitor Service Providers. Monitor service providers consistent with the enterprise’s service provider management policy. Monitoring may include periodic reassessment of service provider compliance, m | conceito: API Gateway With Mutual Authentication (mechanism `ACM-ITS-001`) |
| `CIS-17.8` | Conduct Post-Incident Reviews. Conduct post-incident reviews. Post-incident reviews help prevent incident recurrence through identifying lessons learned and follow-up action. | conceito: Threat Model Versioning Controls (mechanism `ACM-TMR-003`) |
| `CIS-17.9` | Establish | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `CIS-7.7` | Remediate Detected Vulnerabilities. Remediate detected vulnerabilities in software through processes and tooling on a monthly, or more frequent, basis, based on the remediation process. | conceito: Findings Workflow And Exception Governance (mechanism `ACM-TSV-004`) |
| `CIS-9.3` | Maintain | conceito: Validação de input, parsing seguro e tratamento controlado de erros (slice `ACO-IVF`) |

---

## MITRE CWE — Software Development View (v4.19.1)

**O que esta ES traz para este capítulo:** contribui 5 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `CWE-179` | Incorrect Behavior Order: Early Validation. The product validates input before applying protection mechanisms that modify the input, which could allow an attacker to bypass the validation via dangerou | conceito: Static Rulepacks And Security Linters (mechanism `ACM-IVF-002`) |
| `CWE-212` | Improper Removal of Sensitive Information Before Storage or Transfer. The product stores, transfers, or shares a resource that contains sensitive information, but it does not properly remove that info | conceito: Code Review For Input And Error Discipline (mechanism `ACM-IVF-001`) |
| `CWE-222` | Truncation of Security-relevant Information. The product truncates the display, recording, or processing of security-relevant information in a way that can obscure the source or nature of an attack. | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `CWE-223` | Omission of Security-relevant Information. The product does not record or display information that would be important for identifying the source or nature of an attack, or determining if an action is | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `CWE-538` | Insertion of Sensitive Information into Externally-Accessible File or Directory. The product places sensitive information into files or directories that are accessible to actors who are allowed to hav | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |

---

## EU Digital Operational Resilience Act (DORA)

**O que esta ES traz para este capítulo:** contribui 5 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `DORA-ART-13` | DORA Article 13. Article 13 (Learning and evolving) requires financial entities to gather information on vulnerabilities and cyber threats, ICT-related incidents (in particular cyber-attacks) and anal | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `DORA-ART-15` | DORA Article 15. Article 15 (Further harmonisation of ICT risk-management tools, methods, processes and policies) provides the legal basis for the European Supervisory Authorities to develop, in consu | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `DORA-ART-18` | DORA Article 18. Article 18 (Classification of ICT-related incidents and cyber threats) requires financial entities to classify ICT-related incidents and determine their impact based on criteria inclu | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `DORA-ART-27` | DORA Article 27. Article 27 (Requirements for testers for the carrying out of TLPT) sets requirements for testers used in TLPT. Internal testers and external providers shall meet the highest professio | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `DORA-ART-6` | DORA Article 6. Article 6 (ICT risk-management framework) requires financial entities to have a sound, comprehensive and well-documented ICT risk-management framework as part of their overall risk-man | conceito: Threat Representation Models (mechanism `ACM-TMR-001`) |

---

## EU NIS2 Directive

**O que esta ES traz para este capítulo:** contribui 4 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `NIS2-ART-20` | NIS2 Article 20. Article 20 (Governance) requires that management bodies of essential and important entities approve the cybersecurity risk-management measures taken to comply with Article 21, oversee | conceito: Threat Representation Models (mechanism `ACM-TMR-001`) |
| `NIS2-ART-21` | NIS2 Article 21. Article 21 (Cybersecurity risk-management measures) obliges essential and important entities to take appropriate and proportionate technical, operational and organisational measures t | conceito: Automated Topology Validation Jobs (mechanism `ACM-ATB-005`) |
| `NIS2-ART-22` | NIS2 Article 22. Article 22 (Union-level coordinated security risk assessments of critical supply chains) provides for the Cooperation Group, in cooperation with the Commission and ENISA, to carry out | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `NIS2-ART-23` | NIS2 Article 23. Article 23 (Reporting obligations) requires essential and important entities to notify, without undue delay, their CSIRT or competent authority of any incident having a significant im | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |

---

## OWASP Machine Learning Top 10

**O que esta ES traz para este capítulo:** contribui 4 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `ML01-2023` | ML01:2023 Input Manipulation Attack. Description. Input Manipulation Attacks is an umbrella term, which include Adversarial Attacks, a type of attack in which an attacker deliberately alters input dat | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `ML02-2023` | ML02:2023 Data Poisoning Attack. Description. Data poisoning attacks occur when an attacker manipulates the training data to cause the model to behave in an undesirable way. How to Prevent. Data valid | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `ML03-2023` | ML03:2023 Model Inversion Attack. Description. Model inversion attacks occur when an attacker reverse-engineers the model to extract information from it. How to Prevent. Access control: Limiting acces | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `ML09-2023` | ML09:2023 Output Integrity Attack. Description. In an Output Integrity Attack scenario, an attacker aims to modify or manipulate the output of a machine learning model in order to change its behavior | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |

---

## SAFECode — Fundamental Practices for Secure Software Development (2018)

**O que esta ES traz para este capítulo:** contribui 4 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `SCFPSSD-LIFECYCLE-FEEDBACK` | Secure Development Lifecycle Feedback. Root cause analysis feedback loop into SDLC improvement | conceito: Explicit Threat Disposition Register (mechanism `ACM-TMR-004`) |
| `SCFPSSD-PLANNING` | Planning the Implementation and Deployment of Secure Development Practices. Organizational culture, expertise, deployment scope, stakeholder management, compliance measurement, SDL process health | conceito: Threat Disposition And Accepted Risk Governance (practice `ACP-TMR-004`) |
| `SCFPSSD-SECURITY-CONTROLS` | Actively Manage Application Security Controls. Application security control definition and active management throughout lifecycle | conceito: Requirements Registry And Derivation Traceability (mechanism `ACM-TMR-007`) |
| `SCFPSSD-THREAT-MODELING` | Threat Modeling. Systematic identification and assessment of threats to software design | conceito: Structured Threat Analysis Frameworks (mechanism `ACM-TMR-002`) |

---

## OWASP ASVS v5.0.0

**O que esta ES traz para este capítulo:** contribui 3 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `ASVS-REQ-V15.1.4` | Verify that application documentation highlights third-party libraries which are considered to be "risky components". | conceito: Versioned Diagrams And ADR Records (mechanism `ACM-ATB-001`) |
| `ASVS-REQ-V15.1.5` | Verify that application documentation highlights parts of the application where "dangerous functionality" is being used. | conceito: Versioned Diagrams And ADR Records (mechanism `ACM-ATB-001`) |
| `ASVS-REQ-V3.1.1` | Verify that application documentation states the expected security features that browsers using the application must support (such as HTTPS, HTTP Strict Transport Security (HSTS), Content Security Pol | conceito: Boundary Mediation Controls (mechanism `ACM-ATB-003`) |

---

## ENISA — Multilayer AI Cybersecurity Practices (2023)

**O que esta ES traz para este capítulo:** contribui 2 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `ENISA-AI-FAICP-LAYER-III` | Layer III - Sector-specific cybersecurity good practices for AI. A multilayer framework for good cybersecurity practices for AI June 2023 23 and trustworthy AI. • ALLAI73 is an independent Dutch organ | conceito: Reviewer Accountability And Consistency Gates (mechanism `ACM-TMR-006`) |
| `ENISA-AI-FAICP-SURVEY` | Survey analysis of monitoring, enforcement and national preparedness. A multilayer framework for good cybersecurity practices for AI June 2023 27 3. SURVEY ANALYSIS The proposal for the A I Act95 regu | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |

---

## HIPAA Security Rule

**O que esta ES traz para este capítulo:** contribui 2 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `HIPAA-164-308a1` | Security Management Process. Security Management Process — Administrative Safeguard. The covered entity must implement policies and procedures to prevent, detect, contain and correct security violatio | conceito: Threat Model Versioning Controls (mechanism `ACM-TMR-003`) |
| `HIPAA-164-308a2` | Assigned Security Responsibility. Assigned Security Responsibility — Administrative Safeguard. Identify the security official who is responsible for the development and implementation of the policies | conceito: Threat Model Versioning Controls (mechanism `ACM-TMR-003`) |

---

## OWASP LLM Top 10 (2025)

**O que esta ES traz para este capítulo:** contribui 2 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `LLM04-2025` | detect, in effect creating the opportunity for a model to become a sleeper agent | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `LLM08-2025` | LLM08:2025 Vector and Embedding Weaknesses. Vectors and embeddings vulnerabilities present significant security risks in systems utilizing Retrieval Augmented Generation (RAG) with Large Language Mode | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |

---

## OWASP Proactive Controls (2018)

**O que esta ES traz para este capítulo:** contribui 2 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `OPC-C1` | Define Security Requirements. A security requirement is a statement of needed security functionality that ensures one of many different security properties of software is being satisfied. Security req | conceito: Requirements Registry And Derivation Traceability (mechanism `ACM-TMR-007`) |
| `OPC-C2` | Leverage Security Frameworks and Libraries. Secure coding libraries and software frameworks with embedded security help software developers guard against security-related design and implementation fla | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |

---

## SAFECode — Practical Security Stories and Tasks for Agile Development (2012)

**O que esta ES traz para este capítulo:** contribui 2 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `SCAGILE-EXP-3` | Performing threat modeling for new/enhanced features. Performing threat modeling for new or enhanced features | conceito: Threat Model Versioning Controls (mechanism `ACM-TMR-003`) |
| `SCAGILE-OPS-1` | Configure bug tracking to track security vulnerabilities. Configure bug tracking to track security vulnerabilities as a requirement for software development team | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |

---

## EU Cyber Resilience Act (CRA)

**O que esta ES traz para este capítulo:** contribui 1 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `CRA-ART-14` | CRA Article 14. Article 14 (Reporting obligations of manufacturers) requires manufacturers to notify ENISA of any actively exploited vulnerability contained in their product within 24 hours of becomin | conceito: Threat Model Versioning Controls (mechanism `ACM-TMR-003`) |

---

## OWASP MCP — Third-Party Servers v1.0

**O que esta ES traz para este capítulo:** contribui 1 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `OWASP-MCP-3P-TOOL-INTERFERENCE` | Tool interference across multiple MCP servers. Current Vulnerability Landscape Common attack patterns have begun to emerge around MCP, many focused on malicious inputs designed to influence an LLM, or | conceito: Trust-Boundary And DFD Modeling (mechanism `ACM-ATB-002`) |

---

## SLSA Specification v1.0 — Build Track

**O que esta ES traz para este capítulo:** contribui 1 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `SLSA-PRINCIPLE-TRUST-CODE` | Trust code, not individuals. Securely trace all software back to source code rather than trust individuals who have write access to package registries. Reasoning : Code is static and analyzable. Peopl | conceito: Artifact Signing And Attestation (mechanism `ACM-SCBI-004`) |

---
