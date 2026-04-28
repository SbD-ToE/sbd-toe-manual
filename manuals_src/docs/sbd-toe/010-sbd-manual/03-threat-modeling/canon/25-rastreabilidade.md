# 25. Rastreabilidade — Threat Modeling

## Sumário

Este capítulo trata do **processo formal de modelação de ameaças** —
identificação de ameaças, avaliação de risco, mitigation traceability,
e ligação ameaça↔requisito. As fontes externas seguintes contribuem para
esta área:

- **OWASP SAMM v2.1** — 50 referência(s)
- **NIST SP 800-53 Rev. 5** — 36 referência(s)
- **PCI DSS v4.0.1** — 33 referência(s)
- **NIST SSDF (SP 800-218 v1.1)** — 25 referência(s)
- **OWASP DSOMM** — 21 referência(s)
- **CIS Controls v8.1.2** — 14 referência(s)
- **PCI Secure SLC v1.1** — 9 referência(s)
- **EU Digital Operational Resilience Act (DORA)** — 7 referência(s)
- **HIPAA Security Rule** — 4 referência(s)
- **SAFECode — Practical Security Stories and Tasks for Agile Development (2012)** — 4 referência(s)
- **SAFECode — Fundamental Practices for Secure Software Development (2018)** — 4 referência(s)
- **MITRE CAPEC v3.9** — 2 referência(s)
- **ENISA — Multilayer AI Cybersecurity Practices (2023)** — 2 referência(s)
- **EU Cyber Resilience Act (CRA)** — 1 referência(s)
- **EU NIS2 Directive** — 1 referência(s)
- **EU GDPR (RGPD)** — 1 referência(s)
- **OWASP MCP Top 10 (v0.1, 2025 beta)** — 1 referência(s)
- **OWASP Proactive Controls (2018)** — 1 referência(s)

---

## OWASP SAMM v2.1

**O que esta ES traz para este capítulo:** contribui 50 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `SAMM-ACTIVITY-D_TA_1_A` | Perform application risk assessments Ability to classify applications according to risk A basic assessment of the application risk is performed to understand likelihood and impact of an attack. Use a | conceito: Structured Threat Analysis Frameworks (mechanism `ACM-TMR-002`) |
| `SAMM-ACTIVITY-D_TA_1_B` | Perform basic threat modeling Identification of architectural design flaws in your applications Perform best-effort, risk-based threat modeling using brainstorming and existing diagrams with simple th | conceito: Structured Threat Analysis Frameworks (mechanism `ACM-TMR-002`) |
| `SAMM-ACTIVITY-D_TA_2_A` | Inventorize risk profiles Solid understanding of the risk level of your application portfolio Understand the risk for all applications in the organization by centralizing the risk profile inventory fo | conceito: Structured Threat Analysis Frameworks (mechanism `ACM-TMR-002`) |
| `SAMM-ACTIVITY-D_TA_2_B` | Standardize and scale threat modeling Clear expectations of the quality of threat modeling activities Standardize threat modeling training, processes, and tools to scale across the organization. Use a | conceito: Structured Threat Analysis Frameworks (mechanism `ACM-TMR-002`) |
| `SAMM-ACTIVITY-D_TA_3_A` | Periodic review of risk profiles Timely update of the application classification in case of changes Periodically review application risk profiles at regular intervals to ensure accuracy and reflect cu | conceito: Structured Threat Analysis Frameworks (mechanism `ACM-TMR-002`) |
| `SAMM-ACTIVITY-D_TA_3_B` | Optimize threat modeling Assurance of continuous improvement of threat modeling activities Continuously optimization and automation of your threat modeling methodology. Threat modeling is integrated i | conceito: Structured Threat Analysis Frameworks (mechanism `ACM-TMR-002`) |
| `SAMM-ACTIVITY-G_EG_1_A` | Train all stakeholders for awareness Basic security awareness for all relevant employees Provide security awareness training for all personnel involved in software development. Conduct security awaren | conceito: Explicit Threat Disposition Register (mechanism `ACM-TMR-004`) |
| `SAMM-ACTIVITY-G_EG_1_B` | Identify security champions Basic embedding of security in the development organization Identify a "Security Champion" within each development team. Implement a program where each software development | conceito: Threat Representation Models (mechanism `ACM-TMR-001`) |
| `SAMM-ACTIVITY-G_EG_2_A` | Customize security training Relevant employee roles trained according to their specific role Offer technology and role-specific guidance, including security nuances of each language and platform. Cond | conceito: Threat Mitigation Linkage Controls (mechanism `ACM-TMR-005`) |
| `SAMM-ACTIVITY-G_EG_2_B` | Implement centers of excellence Specific security best practices tailored to the organization Develop a secure software center of excellence promoting thought leadership among developers and architect | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `SAMM-ACTIVITY-G_EG_3_A` | Standardize security guidance Adequate security knowledge of all employees ensured prior to working on critical tasks Standardized in-house guidance around the organization's secure software developme | conceito: Reviewer Accountability And Consistency Gates (mechanism `ACM-TMR-006`) |
| `SAMM-ACTIVITY-G_EG_3_B` | Establish a security community Collective development of security know-how among all product teams Build a secure software community including all organization people involved in software security. Se | conceito: Reviewer Accountability And Consistency Gates (mechanism `ACM-TMR-006`) |
| `SAMM-ACTIVITY-G_PC_1_A` | Define policies and standards Clear expectation of minimum security level in the organization Determine a security baseline representing organization's policies and standards. Develop a library of pol | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `SAMM-ACTIVITY-G_PC_1_B` | Identify compliance requirements Security policies and standards aligned with external compliance drivers Identify 3rd-party compliance drivers and requirements and map to existing policies and standa | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `SAMM-ACTIVITY-G_PC_2_A` | Develop test procedures Common understanding of how to reach compliance with security policies for product teams Develop security requirements applicable to all applications. To assist with the ongoin | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `SAMM-ACTIVITY-G_PC_2_B` | Standardize policy and compliance requirements Common understanding how to reach compliance with external compliance drivers for product teams Publish compliance-specific application requirements and | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `SAMM-ACTIVITY-G_PC_3_A` | Measure compliance to policies and standards Understanding of your organization's compliance with policies and standards Measure and report on the status of individual application's adherence to polic | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `SAMM-ACTIVITY-G_PC_3_B` | Measure compliance to external requirements Understanding of your organization's compliance with external compliance drivers Measure and report on individual application's compliance with 3rd party re | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `SAMM-ACTIVITY-G_SM_1_A` | Identify the organization's risk appetite Common understanding of your organization's security posture Identify organization drivers as they relate to the organization's risk tolerance. Understand, ba | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `SAMM-ACTIVITY-G_SM_1_B` | Define basic security metrics Basic insights into your AppSec program's effectiveness and efficiency Define metrics with insight into the effectiveness and efficiency of the Application Security Progr | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `SAMM-ACTIVITY-G_SM_2_A` | Define the security strategy Available and agreed upon roadmap of your AppSec program Publish a unified strategy for application security. Based on the magnitude of assets, threats, and risk tolerance | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `SAMM-ACTIVITY-G_SM_2_B` | Set strategic KPIs Transparency on your AppSec program's performance Set targets and KPI's for measuring the program effectiveness. Once the organization has defined its application security metrics, | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `SAMM-ACTIVITY-G_SM_3_A` | Align security and business strategies Continuous AppSec program alignment with the organization's business goals Align the application security program to support the organization's growth. You revie | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `SAMM-ACTIVITY-G_SM_3_B` | Drive the security program through metrics Continuous improvement of your program according to results Influence the strategy based on the metrics and organizational needs. Define guidelines for influ | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `SAMM-ACTIVITY-I_DM_1_A` | Track security defects centrally Transparency of known security defects impacting particular applications Introduce a structured tracking of security defects and make knowledgeable decisions based on | conceito: Findings Workflow And Exception Governance (mechanism `ACM-TSV-004`) |
| `SAMM-ACTIVITY-I_DM_1_B` | Define basic defect metrics Identification of quick wins derived from available defect information Regularly go over previously recorded security defects and derive quick wins from basic metrics. Once | conceito: Findings Workflow And Exception Governance (mechanism `ACM-TSV-004`) |
| `SAMM-ACTIVITY-I_DM_2_A` | Rate and track security defects Consistent classification of security defects with clear expectations of their handling Rate all security defects over the whole organization consistently and define SL | conceito: Findings Workflow And Exception Governance (mechanism `ACM-TSV-004`) |
| `SAMM-ACTIVITY-I_DM_2_B` | Define advanced defect metrics Improved learning from security defects in your organization Collect standardized defect management metrics and use these also for prioritization of centrally driven ini | conceito: Findings Workflow And Exception Governance (mechanism `ACM-TSV-004`) |
| `SAMM-ACTIVITY-I_DM_3_A` | Enforce an SLA for defect management Assurance that security defects are handled within predefined SLAs Enforce the predefined SLAs and integrate your defect management system with other relevant tool | conceito: Findings Workflow And Exception Governance (mechanism `ACM-TSV-004`) |
| `SAMM-ACTIVITY-I_DM_3_B` | Use metrics to improve the security strategy Optimized security strategy based on defect information Continuously improve your security defect management metrics and correlate it with other sources. R | conceito: Findings Workflow And Exception Governance (mechanism `ACM-TSV-004`) |
| `SAMM-ACTIVITY-O_IM_1_A` | Use best-effort incident detection Ability to detect the most obvious security incidents Use available log data to perform best-effort detection of possible security incidents. Analyze available log d | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `SAMM-ACTIVITY-O_IM_1_B` | Create an incident response plan Ability to efficiently solve most common security incidents Identify roles and responsibilities for incident response. The first step is to recognize the incident resp | conceito: Threat Model Versioning Controls (mechanism `ACM-TMR-003`) |
| `SAMM-ACTIVITY-O_IM_2_A` | Define an incident detection process Timely and consistent detection of expected security incidents Follow an established, well-documented process for incident detection, with emphasis on automated lo | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `SAMM-ACTIVITY-O_IM_2_B` | Define an incident response process Understanding and efficient handling of most security incidents Establish a formal incident response process and ensure staff are properly trained in performing the | conceito: Threat Model Versioning Controls (mechanism `ACM-TMR-003`) |
| `SAMM-ACTIVITY-O_IM_3_A` | Improve the incident detection process Ability to timely detect security incidents Use a proactively managed process for detection of incidents. Ensure process documentation includes measures for cont | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `SAMM-ACTIVITY-O_IM_3_B` | Establish an incident response team Efficient incident response independent of time, location, or type of incident Employ a dedicated, well-trained incident response team. Establish a dedicated incide | conceito: Reviewer Accountability And Consistency Gates (mechanism `ACM-TMR-006`) |
| `SAMM-FUNCTION-GOVERNANCE` | Governance Governance focuses on the processes and activities related to how an organization manages overall software development activities. More specifically, this includes concerns that impact cros | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `SAMM-PRACTICE-G_EG` | G-EG Education and Guidance This practice focuses on increasing the knowledge in the organization regarding secure software. The Education and Guidance (EG) practice focuses on arming personnel involv | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `SAMM-PRACTICE-G_PC` | G-PC Policy and Compliance This practice drives the adherence to internal and external standards and regulations. The Policy and Compliance (PC) practice focuses on understanding and meeting external | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `SAMM-PRACTICE-G_SM` | G-SM Strategy and Metrics This practice forms the basis of your secure software activities by building an overall plan. Software assurance entails many different activities and concerns. Without an ov | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `SAMM-PRACTICE-LEVEL-D_SR_1` | D-SR-1 Security Requirements L1 Consider security explicitly during the software requirements process. | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `SAMM-PRACTICE-LEVEL-D_SR_2` | D-SR-2 Security Requirements L2 Increase granularity of security requirements derived from business logic and known risks. | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `SAMM-PRACTICE-LEVEL-D_SR_3` | D-SR-3 Security Requirements L3 Mandate security requirements process for all software projects and third-party dependencies. | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `SAMM-PRACTICE-LEVEL-G_PC_1` | G-PC-1 Policy and Compliance L1 Identify and document governance and compliance drivers relevant to the organization. | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `SAMM-PRACTICE-LEVEL-G_PC_2` | G-PC-2 Policy and Compliance L2 Establish application-specific security and compliance baseline. | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `SAMM-PRACTICE-LEVEL-G_PC_3` | G-PC-3 Policy and Compliance L3 Measure adherence to policies, standards, and 3rd-party requirements. | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `SAMM-PRACTICE-LEVEL-V_RT_2` | V-RT-2 Requirements-driven Testing L2 Perform implementation review to discover application-specific risks against the security requirements. | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `SAMM-STREAM-D_TA_B` | D-TA-B Threat Modeling Threat modeling is intended to help software development teams understand what risks exist in what is being built, what could go wrong, and how the risks can be mitigated or rem | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `SAMM-STREAM-G_PC_A` | G-PC-A Policy and Standards This stream focuses on maintaining policies and standards and providing them to support integration into the SDLC. | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `SAMM-STREAM-G_PC_B` | G-PC-B Compliance Management This stream focuses on identifying and providing compliance requirements to support integration into the SDLC. | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |

---

## NIST SP 800-53 Rev. 5

**O que esta ES traz para este capítulo:** contribui 36 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `SP800-53-CP-8.2` | Obtain alternate telecommunications services to reduce the likelihood of sharing a single point of failure with primary telecommunications services. | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `SP800-53-IR-9.3` | Implement the following procedures to ensure that organizational personnel impacted by information spills can continue to carry out assigned tasks while contaminated systems are undergoing corrective | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `SP800-53-MA-5.2` | Verify that personnel performing maintenance and diagnostic activities on a system processing, storing, or transmitting classified information possess security clearances and formal access approvals f | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `SP800-53-PE-22` | Mark {{ insert: param, pe-22_odp }} indicating the impact level or classification level of the information permitted to be processed, stored, or transmitted by the hardware component. | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `SP800-53-PE-23` | Plan the location or site of the facility where the system resides considering physical and environmental hazards; and For existing facilities, consider the physical and environmental hazards in the o | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `SP800-53-PE-8.3` | Limit personally identifiable information contained in visitor access records to the following elements identified in the privacy risk assessment: {{ insert: param, pe-08.03_odp }}. | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `SP800-53-PL-5` | Privacy Impact Assessment | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `SP800-53-PM-23` | Establish a Data Governance Body consisting of {{ insert: param, pm-23_odp.01 }} with {{ insert: param, pm-23_odp.02 }}. | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `SP800-53-PM-28` | Identify and document: Assumptions affecting risk assessments, risk responses, and risk monitoring; Constraints affecting risk assessments, risk responses, and risk monitoring; Priorities and trade-of | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `SP800-53-PS-3.1` | Verify that individuals accessing a system processing, storing, or transmitting classified information are cleared and indoctrinated to the highest classification level of the information to which the | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `SP800-53-RA-1` | Develop, document, and disseminate to {{ insert: param, ra-1_prm_1 }}: {{ insert: param, ra-01_odp.03 }} risk assessment policy that: Procedures to facilitate the implementation of the risk assessment | conceito: DFD And Trust-Boundary Grounding (practice `ACP-TMR-002`) |
| `SP800-53-RA-10` | Establish and maintain a cyber threat hunting capability to: Search for indicators of compromise in organizational systems; and Detect, track, and disrupt threats that evade existing controls; and Emp | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `SP800-53-RA-2` | Categorize the system and information it processes, stores, and transmits; Document the security categorization results, including supporting rationale, in the security plan for the system; and Verify | conceito: Threat Disposition And Accepted Risk Governance (practice `ACP-TMR-004`) |
| `SP800-53-RA-2.1` | Conduct an impact-level prioritization of organizational systems to obtain additional granularity on system impact levels. | conceito: Threat Disposition And Accepted Risk Governance (practice `ACP-TMR-004`) |
| `SP800-53-RA-3` | Conduct a risk assessment, including: Identifying threats to and vulnerabilities in the system; Determining the likelihood and magnitude of harm from unauthorized access, use, disclosure, disruption, | conceito: Structured Threat Analysis Method Selection (practice `ACP-TMR-003`) |
| `SP800-53-RA-3.1` | Assess supply chain risks associated with {{ insert: param, ra-03.01_odp.01 }} ; and Update the supply chain risk assessment {{ insert: param, ra-03.01_odp.02 }} , when there are significant changes t | conceito: Structured Threat Analysis Method Selection (practice `ACP-TMR-003`) |
| `SP800-53-RA-3.2` | Use all-source intelligence to assist in the analysis of risk. | conceito: Structured Threat Analysis Method Selection (practice `ACP-TMR-003`) |
| `SP800-53-RA-3.3` | Determine the current cyber threat environment on an ongoing basis using {{ insert: param, ra-03.03_odp }}. | conceito: Structured Threat Analysis Method Selection (practice `ACP-TMR-003`) |
| `SP800-53-RA-3.4` | Employ the following advanced automation and analytics capabilities to predict and identify risks to {{ insert: param, ra-03.04_odp.02 }}: {{ insert: param, ra-3.4_prm_2 }}. | conceito: Structured Threat Analysis Method Selection (practice `ACP-TMR-003`) |
| `SP800-53-RA-4` | Risk Assessment Update | conceito: Threat Model Creation And Triggered Refresh (practice `ACP-TMR-001`) |
| `SP800-53-RA-5` | Monitor and scan for vulnerabilities in the system and hosted applications {{ insert: param, ra-5_prm_1 }} and when new vulnerabilities potentially affecting the system are identified and reported; Em | conceito: Staged Dynamic Testing And Gate Enforcement (practice `ACP-TSV-005`) |
| `SP800-53-RA-5.1` | Update Tool Capability | conceito: Staged Dynamic Testing And Gate Enforcement (practice `ACP-TSV-005`) |
| `SP800-53-RA-5.10` | Correlate the output from vulnerability scanning tools to determine the presence of multi-vulnerability and multi-hop attack vectors. | conceito: Staged Dynamic Testing And Gate Enforcement (practice `ACP-TSV-005`) |
| `SP800-53-RA-5.11` | Establish a public reporting channel for receiving reports of vulnerabilities in organizational systems and system components. | conceito: Staged Dynamic Testing And Gate Enforcement (practice `ACP-TSV-005`) |
| `SP800-53-RA-5.2` | Update the system vulnerabilities to be scanned {{ insert: param, ra-05.02_odp.01 }}. | conceito: Staged Dynamic Testing And Gate Enforcement (practice `ACP-TSV-005`) |
| `SP800-53-RA-5.3` | Define the breadth and depth of vulnerability scanning coverage. | conceito: Staged Dynamic Testing And Gate Enforcement (practice `ACP-TSV-005`) |
| `SP800-53-RA-5.4` | Determine information about the system that is discoverable and take {{ insert: param, ra-05.04_odp }}. | conceito: Staged Dynamic Testing And Gate Enforcement (practice `ACP-TSV-005`) |
| `SP800-53-RA-5.5` | Implement privileged access authorization to {{ insert: param, ra-05.05_odp.01 }} for {{ insert: param, ra-05.05_odp.02 }}. | conceito: Staged Dynamic Testing And Gate Enforcement (practice `ACP-TSV-005`) |
| `SP800-53-RA-5.6` | Compare the results of multiple vulnerability scans using {{ insert: param, ra-05.06_odp }}. | conceito: Staged Dynamic Testing And Gate Enforcement (practice `ACP-TSV-005`) |
| `SP800-53-RA-5.7` | Automated Detection and Notification of Unauthorized Components | conceito: Staged Dynamic Testing And Gate Enforcement (practice `ACP-TSV-005`) |
| `SP800-53-RA-5.8` | Review historic audit logs to determine if a vulnerability identified in a {{ insert: param, ra-05.08_odp.01 }} has been previously exploited within an {{ insert: param, ra-05.08_odp.02 }}. | conceito: Staged Dynamic Testing And Gate Enforcement (practice `ACP-TSV-005`) |
| `SP800-53-RA-5.9` | Penetration Testing and Analyses | conceito: Staged Dynamic Testing And Gate Enforcement (practice `ACP-TSV-005`) |
| `SP800-53-RA-6` | Employ a technical surveillance countermeasures survey at {{ insert: param, ra-06_odp.01 }} {{ insert: param, ra-06_odp.02 }}. | conceito: Secret Leak Prevention In Source And Pipeline (practice `ACP-SPC-001`) |
| `SP800-53-RA-7` | Respond to findings from security and privacy assessments, monitoring, and audits in accordance with organizational risk tolerance. | conceito: Threat Disposition And Accepted Risk Governance (practice `ACP-TMR-004`) |
| `SP800-53-RA-8` | Conduct privacy impact assessments for systems, programs, or other activities before: Developing or procuring information technology that processes personally identifiable information; and Initiating | conceito: Threat Disposition And Accepted Risk Governance (practice `ACP-TMR-004`) |
| `SP800-53-RA-9` | Identify critical system components and functions by performing a criticality analysis for {{ insert: param, ra-09_odp.01 }} at {{ insert: param, ra-09_odp.02 }}. | conceito: Threat Model Creation And Triggered Refresh (practice `ACP-TMR-001`) |

---

## PCI DSS v4.0.1

**O que esta ES traz para este capítulo:** contribui 33 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `PCI-12.1.1` | An overall information security policy is: 12.1.1 Examine the information security policy and policy ties to and governs all other policies and | conceito: Threat Model Versioning Controls (mechanism `ACM-TMR-003`) |
| `PCI-12.1.2` | The information security policy is: 12.1.2 Examine the information security policy and methods evolve rapidly. Without updating the | conceito: Threat Mitigation Linkage Controls (mechanism `ACM-TMR-005`) |
| `PCI-12.1.3` | The security policy clearly defines 12.1.3.a Examine the information security policy to responsibilities assigned, there could be misuse | conceito: Threat Model Versioning Controls (mechanism `ACM-TMR-003`) |
| `PCI-12.1.4` | Responsibility for information security is 12.1.4 Examine the information security policy to responsibility is actively managing and | conceito: Threat Model Versioning Controls (mechanism `ACM-TMR-003`) |
| `PCI-12.10.1` | An incident response plan exists and is 12.10.1.a Examine the incident response plan to that is properly disseminated, read, and | conceito: Threat Model Versioning Controls (mechanism `ACM-TMR-003`) |
| `PCI-12.10.2` | At least once every 12 months, the security 12.10.2 Interview personnel and review plan can identify broken business processes and | conceito: Explicit Threat Disposition Register (mechanism `ACM-TMR-004`) |
| `PCI-12.10.3` | Specific personnel are designated to be 12.10.3 Examine documentation and interview person who is trained in incident response and | conceito: Threat Model Versioning Controls (mechanism `ACM-TMR-003`) |
| `PCI-12.10.4` | Personnel responsible for responding to 12.10.4 Examine training documentation and response team, extended damage to the network | conceito: Threat Model Versioning Controls (mechanism `ACM-TMR-003`) |
| `PCI-12.10.5` | The security incident response plan 12.10.5 Examine documentation and observe monitoring systems that are explicitly designed to | conceito: Threat Representation Models (mechanism `ACM-TMR-001`) |
| `PCI-12.10.6` | The security incident response plan is 12.10.6.a Examine policies and procedures to response plan after an incident occurs and in-step | conceito: Threat Model Versioning Controls (mechanism `ACM-TMR-003`) |
| `PCI-12.10.7` | Incident response procedures are in place, 12.10.7.a Examine documented incident response procedures that are followed in the event that | conceito: Threat Model Versioning Controls (mechanism `ACM-TMR-003`) |
| `PCI-12.2.1` | Acceptable use policies for end-user 12.2.1 Examine the acceptable use policies for investment and may pose significant risk to an | conceito: Structured Threat Analysis Frameworks (mechanism `ACM-TMR-002`) |
| `PCI-12.3.1` | specified at Requirement 12.3.1. | conceito: Threat Model Versioning Controls (mechanism `ACM-TMR-003`) |
| `PCI-12.3.2` | A targeted risk analysis is performed for each 12.3.2 Examine the documented targeted risk- methodology enables an entity to meet the | conceito: Structured Threat Analysis Frameworks (mechanism `ACM-TMR-002`) |
| `PCI-12.3.3` | Cryptographic cipher suites and protocols in 12.3.3 Examine documentation for cryptographic change or be deprecated due to identification of | conceito: Threat Model Versioning Controls (mechanism `ACM-TMR-003`) |
| `PCI-12.3.4` | Hardware and software technologies in use 12.3.4 Examine documentation for the review of constantly evolving, and organizations need to be | conceito: Structured Threat Analysis Frameworks (mechanism `ACM-TMR-002`) |
| `PCI-12.4.1` | Additional requirement for service 12.4.1 Additional testing procedure for service compliance responsibilities ensures executive- | conceito: Threat Model Versioning Controls (mechanism `ACM-TMR-003`) |
| `PCI-12.4.2` | Additional requirement for service 12.4.2.a Additional testing procedure for procedures are being followed provides | conceito: Threat Model Versioning Controls (mechanism `ACM-TMR-003`) |
| `PCI-12.5.1` | An inventory of system components that are 12.5.1.a Examine the inventory to verify it includes components will enable an organization to define | conceito: Threat Representation Models (mechanism `ACM-TMR-001`) |
| `PCI-12.5.2` | PCI DSS scope is documented and 12.5.2.a Examine documented results of scope ensure PCI DSS scope remains up to date and | conceito: Threat Representation Models (mechanism `ACM-TMR-001`) |
| `PCI-12.5.3` | Additional requirement for service 12.5.3.a Additional testing procedure for define the requirements and protocol for effective | conceito: Threat Mitigation Linkage Controls (mechanism `ACM-TMR-005`) |
| `PCI-12.6.1` | A formal security awareness program is 12.6.1 Examine the security awareness program to company’s information security policies and | conceito: Explicit Threat Disposition Register (mechanism `ACM-TMR-004`) |
| `PCI-12.6.2` | The security awareness program is: 12.6.2 Examine security awareness program are not static. As such, the security awareness | conceito: Threat Model Versioning Controls (mechanism `ACM-TMR-003`) |
| `PCI-12.6.3` | Personnel receive security awareness 12.6.3.a Examine security awareness program information about the importance of information | conceito: Threat Model Versioning Controls (mechanism `ACM-TMR-003`) |
| `PCI-12.7.1` | Potential personnel who will have access to 12.7.1 Interview responsible Human Resource potential personnel who are expected to be given | conceito: Threat Model Versioning Controls (mechanism `ACM-TMR-003`) |
| `PCI-12.8.1` | A list of all third-party service providers 12.8.1.a Examine policies and procedures to verify potential risk extends outside the organization | conceito: Threat Model Versioning Controls (mechanism `ACM-TMR-003`) |
| `PCI-12.8.2` | Written agreements with TPSPs are 12.8.2.a Examine policies and procedures to verify demonstrates its commitment to maintaining | conceito: Threat Model Versioning Controls (mechanism `ACM-TMR-003`) |
| `PCI-12.8.3` | An established process is implemented for 12.8.3.a Examine policies and procedures to verify including details for selection and vetting prior to | conceito: Explicit Threat Disposition Register (mechanism `ACM-TMR-004`) |
| `PCI-12.8.4` | A program is implemented to monitor TPSPs’ 12.8.4.a Examine policies and procedures to verify engaged TPSPs provides assurance and awareness | conceito: Threat Mitigation Linkage Controls (mechanism `ACM-TMR-005`) |
| `PCI-12.8.5` | Information is maintained about which PCI 12.8.5.a Examine policies and procedures to verify PCI DSS requirements and sub-requirements its | conceito: Threat Mitigation Linkage Controls (mechanism `ACM-TMR-005`) |
| `PCI-12.9.1` | Additional requirement for service 12.9.1 Additional testing procedure for service requirement is intended to promote a consistent | conceito: Threat Model Versioning Controls (mechanism `ACM-TMR-003`) |
| `PCI-12.9.2` | Additional requirement for service 12.9.2 Additional testing procedure for service information to enable its customers to meet their | conceito: Threat Model Versioning Controls (mechanism `ACM-TMR-003`) |
| `PCI-REQ-12` | Requirement 12: Support Information Security with Organizational Policies and Programs. Goal: Maintain an Information Security Policy. | conceito: Threat Model Versioning Controls (mechanism `ACM-TMR-003`) |

---

## NIST SSDF (SP 800-218 v1.1)

**O que esta ES traz para este capítulo:** contribui 25 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `SSDF-PRACTICE-PO.1` | Ensure that security requirements for software development are known at all times so that they can be taken into account throughout the SDLC and duplication of effort can be minimized because the requ | conceito: Requirements Registry And Derivation Traceability (mechanism `ACM-TMR-007`) |
| `SSDF-PRACTICE-PO.2` | Ensure that everyone inside and outside of the organization involved in the SDLC is prepared to perform their SDLC -related roles and responsibilities throughout the SDLC. | conceito: Explicit Threat Disposition Register (mechanism `ACM-TMR-004`) |
| `SSDF-PRACTICE-PW.1` | Identify and evaluate the security requirements for the software; determine what security risks the software is likely to face during operation and how the software’s design and architecture should mi | conceito: Threat Representation Models (mechanism `ACM-TMR-001`) |
| `SSDF-PRACTICE-RV.1` | Help ensure that vulnerabilities are identified more quickly so that they can be remediated more quickly in accordance with risk , reducing the window of opportunity for attackers. | conceito: Findings Workflow And Exception Governance (mechanism `ACM-TSV-004`) |
| `SSDF-PRACTICE-RV.2` | Help ensure that vulnerabilities are remediated in accordance with risk to reduc e the window of opportunity for attackers. | conceito: Findings Workflow And Exception Governance (mechanism `ACM-TSV-004`) |
| `SSDF-PRACTICE-RV.3` | Help reduce the frequency of vulnerabilities in the future. | conceito: Reviewer Accountability And Consistency Gates (mechanism `ACM-TMR-006`) |
| `SSDF-TASK-PO.1.1` | Identify and document all security requirements for the organization’s software development infrastructures and processes, and maintain the requirements over time. | conceito: Requirements Registry And Derivation Traceability (mechanism `ACM-TMR-007`) |
| `SSDF-TASK-PO.1.2` | Identify and document all security requirements for organization -developed software to meet, and maintain the requirements over time. | conceito: Requirements Registry And Derivation Traceability (mechanism `ACM-TMR-007`) |
| `SSDF-TASK-PO.1.3` | Communicate requirements to all third parties who will provide commercial software components to the organization for reuse by the organization’s own software. [Formerly PW.3.1] | conceito: Compliance Monitoring And Regulatory Change Feeds (mechanism `ACM-TMR-008`) |
| `SSDF-TASK-PO.2.1` | Create new roles and alter responsibilities for existing roles as needed to encompass all parts of the SDLC . Periodical ly review and maintain the defined roles and responsibilities, updating them as | conceito: Explicit Threat Disposition Register (mechanism `ACM-TMR-004`) |
| `SSDF-TASK-PO.2.2` | Provide role- based training for all personnel with responsibilities that contribute to secure development. Periodically review personnel proficiency and role-based training, and update the training a | conceito: Explicit Threat Disposition Register (mechanism `ACM-TMR-004`) |
| `SSDF-TASK-PO.2.3` | Obtain upper management or authorizing official commitment to secure development, and convey that commitment to all with development - related roles and responsibilities. | conceito: Explicit Threat Disposition Register (mechanism `ACM-TMR-004`) |
| `SSDF-TASK-PW.1.1` | Use forms of risk modeling – such as threat modeling, attack modeling, or attack surface mapping – to help assess the security risk for the software. | conceito: Structured Threat Analysis Frameworks (mechanism `ACM-TMR-002`) |
| `SSDF-TASK-PW.1.2` | Track and maintain the software’s security requirements, risks, and design decisions. | conceito: Compliance Monitoring And Regulatory Change Feeds (mechanism `ACM-TMR-008`) |
| `SSDF-TASK-PW.1.3` | Where appropriate, build in support for using standardized security features and services (e.g., enabling software to integrate with existing log management, identity management, access control, and v | conceito: Threat Representation Models (mechanism `ACM-TMR-001`) |
| `SSDF-TASK-PW.3.2` | Moved to PW.4.4 Reuse Existing, Well-Secured Software When Feasible Instead of Duplicating Functionality (PW.4): Lower the costs of software development, expedite software development, and decrease th | conceito: Approved Source And Registry Governance (practice `ACP-SCBI-003`) |
| `SSDF-TASK-RV.1.1` | Gather information from software acquirers , users , and public sources on potential vulnerabilities in the software and third- party components that the software uses, and investigate all credible re | conceito: Findings Workflow And Exception Governance (mechanism `ACM-TSV-004`) |
| `SSDF-TASK-RV.1.2` | Review, analyze, and/or test the software’s code to identify or confirm the presence of previously undetected vulnerabilities. | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `SSDF-TASK-RV.1.3` | Have a policy that addresses vulnerability disclosure and remediation, and implement the roles, responsibilities, and processes needed to support that policy. | conceito: Findings Workflow And Exception Governance (mechanism `ACM-TSV-004`) |
| `SSDF-TASK-RV.2.1` | Analyze each vulnerability to gather sufficient information about risk to plan its remediation or other risk response . | conceito: Findings Workflow And Exception Governance (mechanism `ACM-TSV-004`) |
| `SSDF-TASK-RV.2.2` | Plan and implement risk responses for vulnerabilities . | conceito: Explicit Threat Disposition Register (mechanism `ACM-TMR-004`) |
| `SSDF-TASK-RV.3.1` | Analyze identified vulnerabilities to determine their root causes. | conceito: Reviewer Accountability And Consistency Gates (mechanism `ACM-TMR-006`) |
| `SSDF-TASK-RV.3.2` | Analyze the root causes over time to identify patterns, such as a particular secure coding practice not being followed consistently. | conceito: Threat Model Versioning Controls (mechanism `ACM-TMR-003`) |
| `SSDF-TASK-RV.3.3` | Review the software for similar vulnerabilities to eradicate a c lass of vulnerabilities , and proactively fix them rather than waiting for external reports. | conceito: Threat Model Versioning Controls (mechanism `ACM-TMR-003`) |
| `SSDF-TASK-RV.3.4` | Review the SDLC process, and update it if appropriate to prevent (or reduce the likelihood of) the root cause recurring in updates to the software or in new software that is created. | conceito: Reviewer Accountability And Consistency Gates (mechanism `ACM-TMR-006`) |

---

## OWASP DSOMM

**O que esta ES traz para este capítulo:** contribui 21 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `DSOMM-ACTIVITY-0B28367B75A04BAEA9263725C1BF9BB0` | Security consulting on request Security consulting on request allows teams to seek expert advice on security-related questions or challenges as they arise. This support can be provided by internal or | conceito: Explicit Threat Disposition Register (mechanism `ACM-TMR-004`) |
| `DSOMM-ACTIVITY-12C90CC63D584D9B82FFD469D2A0C298` | Ad-Hoc Security trainings for software developers Ad-hoc security training provides basic awareness of software security risks and best practices to developers and other personnel involved in software | conceito: Explicit Threat Disposition Register (mechanism `ACM-TMR-004`) |
| `DSOMM-ACTIVITY-185D5A7419DC4422BE0744EA35226783` | Office Hours Developers and Operations are not in contact with the security team and therefore do not ask prior implementation of (known or unknown) threats- As a security team, be open for questions | conceito: Explicit Threat Disposition Register (mechanism `ACM-TMR-004`) |
| `DSOMM-ACTIVITY-31833D5635AF4EF39300F23D27646CE7` | Regular security training for externals Understanding security is hard. Provide security awareness training for all personnel including externals involved in software development on a regular basis. | conceito: Threat Representation Models (mechanism `ACM-TMR-001`) |
| `DSOMM-ACTIVITY-35446784761040D9AF9ED43F3173BF8C` | Conduction of collaborative team security checks Development teams limited insight over security practices. Mutual security testing the security of other teams project enhances security awareness and | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `DSOMM-ACTIVITY-3F63BDBCC75F4780A941E6AD42E894E1` | Approval by reviewing any new version An individual might forget to implement security measures to protect source code or infrastructure components. On each new version (e.g. Pull Request) of source c | conceito: Release Promotion Gates (mechanism `ACM-SCBI-003`) |
| `DSOMM-ACTIVITY-534F60BF09954314BB9CF0F2BF204694` | Conduction of war games Understanding incident response plans during an incident is hard and ineffective. War Games like activities help train for incidents. Security SMEs create attack scenarios in a | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `DSOMM-ACTIVITY-535F301AE8E84EDAAD77A08B035C92DE` | Simple mob hacking ### Guidelines for your simple mob hacking session - All exploits happen via the user interface. - No need for security/hacking tools. - No need for deep technical or security knowl | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `DSOMM-ACTIVITY-58C46807FEE9448BB6DD8050C464AB52` | Security-Lessoned-Learned After an incident, a similar incident might reoccur. Running a 'lessons learned' session after an incident helps drive continuous improvement. Regular meetings with security | conceito: Threat Model Versioning Controls (mechanism `ACM-TMR-003`) |
| `DSOMM-ACTIVITY-6217FE115ED74CF49DE4555BCFA6FE87` | Each team has a security champion Implement a program where each software development team has a member considered a "Security Champion" who is the liaison between Information Security and developers. | conceito: Reviewer Accountability And Consistency Gates (mechanism `ACM-TMR-006`) |
| `DSOMM-ACTIVITY-7121B0C76ACE4D6B95D094535DBCCB57` | Security code review ### Benefits - New vulnerabilities may be found before reaching production. - Old vulnerabilities are found and fixed. Understanding security is hard. The following areas of code | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `DSOMM-ACTIVITY-72737130472C498480F89AB2F1C2ED5D` | Determining the protection requirement Not defining the protection requirement of applications can lead to wrong prioritization, delayed remediation of critical security issues, increasing the risk of | conceito: Requirements Registry And Derivation Traceability (mechanism `ACM-TMR-007`) |
| `DSOMM-ACTIVITY-91B6F75B9F4A4D7795A2AF7AD3222C7C` | Reward of good communication Employees are not getting excited about security. Good communication and transparency encourages cross-organizational support. Gamification of security is also known to he | conceito: Threat Representation Models (mechanism `ACM-TMR-001`) |
| `DSOMM-ACTIVITY-95CAEF9636ED458CA0875C35D4F9DEC2` | Conduction of collaborative security checks with developers and system administrators Security checks by external companies do not increase the understanding of an application/system for internal empl | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `DSOMM-ACTIVITY-9768F154357A4C06AF6FD66570677C9B` | Regular security training for all Conduct security awareness training for all roles currently involved in the management, development, testing, or auditing of the software. The goal is to increase the | conceito: Explicit Threat Disposition Register (mechanism `ACM-TMR-004`) |
| `DSOMM-ACTIVITY-B4193D32394847E2A3263748C48019A1` | Definition of a change management process The impact of a change is not controlled because these are not recorded or documented. Each change of a system is automatically recorded and adequately logged | conceito: Release Promotion Controls (mechanism `ACM-RPR-001`) |
| `DSOMM-ACTIVITY-BFDB576EA4164EC696FEA078D58B2FF8` | Conduction of build-it, break-it, fix-it contests Understanding security is hard, even for security champions and the conduction of security training often focuses on breaking a component instead of b | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `DSOMM-ACTIVITY-C72DA77986CC45B1A339190CE5093171` | Definition of simple BCDR practices for critical components Business Continuity and Disaster Recovery (BCDR) is a plan and a process that enable an organization to quickly restore normal operations af | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `DSOMM-ACTIVITY-F7B215DC73A44C619E49B3A3AF1C9AC3` | Security Coaching Training does not change behaviour. Therefore, even if security practices are understood, it's likely that they are not performed. By coaching teams on security topics using for exam | conceito: Structured Threat Analysis Frameworks (mechanism `ACM-TMR-002`) |
| `DSOMM-ACTIVITY-F88D1B173D7D4C3D8139AD44FC4942D4` | Regular security training of security champions Understanding security is hard, even for security champions. Regular security training of security champions. - Process Documentation: TODO - Training C | conceito: Threat Representation Models (mechanism `ACM-TMR-001`) |
| `DSOMM-ACTIVITY-F994A55D71BB45A4A8870A213D72C504` | Aligning security in teams The concept of Security Champions might suggest that only he/she is responsible for security. However, everyone in the project team should be responsible for security. By al | conceito: Reviewer Accountability And Consistency Gates (mechanism `ACM-TMR-006`) |

---

## CIS Controls v8.1.2

**O que esta ES traz para este capítulo:** contribui 14 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `CIS-14` | Establish and maintain a security awareness program to influence behavior among the workforce to be security conscious and properly skilled to reduce cybersecurity risks to the enterprise. | conceito: Explicit Threat Disposition Register (mechanism `ACM-TMR-004`) |
| `CIS-14.7` | Train workforce to understand how to verify and report out-of-date software patches or any failures in automated processes and tools. Part of this training should include notifying IT personnel of any | conceito: Threat Mitigation Linkage Controls (mechanism `ACM-TMR-005`) |
| `CIS-17.2` | Establish and maintain contact information for parties that need to be informed of security incidents. Contacts may include internal staff, service providers, law enforcement, cyber insurance provider | conceito: Structured Threat Analysis Frameworks (mechanism `ACM-TMR-002`) |
| `CIS-17.3` | Establish and maintain a documented enterprise process for the workforce to report security incidents. The process includes reporting timeframe, personnel to report to, mechanism for reporting, and th | conceito: Threat Traceability Into Requirements And Validation (practice `ACP-TMR-005`) |
| `CIS-17.4` | Establish and maintain a documented incident response process that addresses roles and responsibilities, compliance requirements, and a communication plan. Review annually, or when significant enterpr | conceito: Reviewer Accountability And Consistency Gates (mechanism `ACM-TMR-006`) |
| `CIS-17.6` | Determine which primary and secondary mechanisms will be used to communicate and report during a security incident. Mechanisms can include phone calls, emails, secure chat, or notification letters. Ke | conceito: Threat Traceability Into Requirements And Validation (practice `ACP-TMR-005`) |
| `CIS-7` | Develop a plan to continuously assess and track vulnerabilities on all enterprise assets within the enterprise’s infrastructure, in order to remediate, and minimize, the window of opportunity for atta | conceito: Threat Mitigation Linkage Controls (mechanism `ACM-TMR-005`) |
| `CIS-7.1` | Establish and maintain a documented vulnerability management process for enterprise assets. Review and update documentation annually, or when significant enterprise changes occur that could impact thi | conceito: Threat Mitigation Linkage Controls (mechanism `ACM-TMR-005`) |
| `CIS-7.2` | Establish and maintain a risk-based remediation strategy documented in a remediation process, with monthly, or more frequent, reviews. | conceito: Threat Mitigation Linkage Controls (mechanism `ACM-TMR-005`) |
| `CIS-7.3` | Perform operating system updates on enterprise assets through automated patch management on a monthly, or more frequent, basis. | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `CIS-7.4` | Perform application updates on enterprise assets through automated patch management on a monthly, or more frequent, basis. | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |
| `CIS-7.5` | Perform automated vulnerability scans of internal enterprise assets on a quarterly, or more frequent, basis. Conduct both authenticated and unauthenticated scans. | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `CIS-7.6` | Perform automated vulnerability scans of externally-exposed enterprise assets. Perform scans on a monthly, or more frequent, basis. | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `CIS-7.7` | Remediate detected vulnerabilities in software through processes and tooling on a monthly, or more frequent, basis, based on the remediation process. | conceito: Findings Workflow And Exception Governance (mechanism `ACM-TSV-004`) |

---

## PCI Secure SLC v1.1

**O que esta ES traz para este capítulo:** contribui 9 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `PCISSLC-1.1` | Senior leadership team establishes formal responsibility and authority for security of vendor's products and services | conceito: Threat Disposition And Accepted Risk Governance (practice `ACP-TMR-004`) |
| `PCISSLC-1.2` | Software security responsibilities clearly defined and assigned to appropriate individuals or teams including development personnel | conceito: Threat Disposition And Accepted Risk Governance (practice `ACP-TMR-004`) |
| `PCISSLC-1.3` | Mature process for managing and maintaining software security skills; skills required for each role clearly defined; annual review | conceito: Threat Disposition And Accepted Risk Governance (practice `ACP-TMR-004`) |
| `PCISSLC-2.1` | Mature process to identify and monitor external regulatory and industry security and compliance requirements; reviewed annually | conceito: Compliance Monitoring And Regulatory Change Feeds (mechanism `ACM-TMR-008`) |
| `PCISSLC-2.2` | Software security policy communicated to all vendor personnel; covers all control objectives; approved by senior leadership | conceito: Threat Disposition And Accepted Risk Governance (practice `ACP-TMR-004`) |
| `PCISSLC-2.3` | Strategy based on or aligned with industry-accepted methodologies; covers entire lifecycle; reviewed annually | conceito: Threat Disposition And Accepted Risk Governance (practice `ACP-TMR-004`) |
| `PCISSLC-3.1` | Mature process to identify and classify critical assets; CIA requirements for each defined; inventory maintained | conceito: Threat Representation Models (mechanism `ACM-TMR-001`) |
| `PCISSLC-3.2` | Process to identify, assess, and monitor software threats and design weaknesses; accounts for all inputs/outputs, data flows, trust boundaries; includes open-source components | conceito: Structured Threat Analysis Frameworks (mechanism `ACM-TMR-002`) |
| `PCISSLC-3.3` | Process for defining security requirements and implementing controls to mitigate threats; mitigation decisions recorded and approved | conceito: Threat Model Versioning Controls (mechanism `ACM-TMR-003`) |

---

## EU Digital Operational Resilience Act (DORA)

**O que esta ES traz para este capítulo:** contribui 7 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `DORA-ART-17` | Article 17 of Digital Operational Resilience Act (Regulation (EU) 2022/2554). See validation passes in knowledge-graph working notes for detailed analysis. | conceito: Threat Representation Models (mechanism `ACM-TMR-001`) |
| `DORA-ART-20` | Article 20 of Digital Operational Resilience Act | conceito: Threat Model Versioning Controls (mechanism `ACM-TMR-003`) |
| `DORA-ART-21` | Article 21 of Digital Operational Resilience Act | conceito: Threat Model Versioning Controls (mechanism `ACM-TMR-003`) |
| `DORA-ART-22` | Article 22 of Digital Operational Resilience Act | conceito: Threat Model Versioning Controls (mechanism `ACM-TMR-003`) |
| `DORA-ART-23` | Article 23 of Digital Operational Resilience Act | conceito: Threat Model Versioning Controls (mechanism `ACM-TMR-003`) |
| `DORA-ART-5` | Article 5 of Digital Operational Resilience Act (Regulation (EU) 2022/2554). See validation passes in knowledge-graph working notes for detailed analysis. | conceito: Threat Representation Models (mechanism `ACM-TMR-001`) |
| `DORA-ART-6` | Article 6 of Digital Operational Resilience Act (Regulation (EU) 2022/2554). See validation passes in knowledge-graph working notes for detailed analysis. | conceito: Threat Representation Models (mechanism `ACM-TMR-001`) |

---

## HIPAA Security Rule

**O que esta ES traz para este capítulo:** contribui 4 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `HIPAA-164-308a1` | Security Management Process — Administrative Safeguard under HIPAA Security Rule §164.308(a)(1). | conceito: Threat Model Versioning Controls (mechanism `ACM-TMR-003`) |
| `HIPAA-164-308a2` | Assigned Security Responsibility — Administrative Safeguard under HIPAA Security Rule §164.308(a)(2). | conceito: Threat Model Versioning Controls (mechanism `ACM-TMR-003`) |
| `HIPAA-164-316a` | Policies and Procedures — Policies Safeguard under HIPAA Security Rule §164.316(a). | conceito: Threat Model Versioning Controls (mechanism `ACM-TMR-003`) |
| `HIPAA-164-316b1` | Documentation — Policies Safeguard under HIPAA Security Rule §164.316(b)(1). | conceito: Threat Model Versioning Controls (mechanism `ACM-TMR-003`) |

---

## SAFECode — Practical Security Stories and Tasks for Agile Development (2012)

**O que esta ES traz para este capítulo:** contribui 4 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `SCAGILE-EXP-1` | Software security training covering secure coding and secure testing techniques | conceito: Threat Traceability Into Requirements And Validation (practice `ACP-TMR-005`) |
| `SCAGILE-EXP-3` | Performing threat modeling for new or enhanced features | conceito: Threat Model Versioning Controls (mechanism `ACM-TMR-003`) |
| `SCAGILE-OPS-14` | Ensure all developers have obtained secure coding training | conceito: Threat Traceability Into Requirements And Validation (practice `ACP-TMR-005`) |
| `SCAGILE-OPS-15` | Ensure all QA engineers have obtained secure testing training | conceito: Threat Traceability Into Requirements And Validation (practice `ACP-TMR-005`) |

---

## SAFECode — Fundamental Practices for Secure Software Development (2018)

**O que esta ES traz para este capítulo:** contribui 4 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `SCFPSSD-LIFECYCLE-FEEDBACK` | Root cause analysis feedback loop into SDLC improvement | conceito: Explicit Threat Disposition Register (mechanism `ACM-TMR-004`) |
| `SCFPSSD-PLANNING` | Organizational culture, expertise, deployment scope, stakeholder management, compliance measurement, SDL process health | conceito: Threat Disposition And Accepted Risk Governance (practice `ACP-TMR-004`) |
| `SCFPSSD-SECURITY-CONTROLS` | Application security control definition and active management throughout lifecycle | conceito: Requirements Registry And Derivation Traceability (mechanism `ACM-TMR-007`) |
| `SCFPSSD-THREAT-MODELING` | Systematic identification and assessment of threats to software design | conceito: Structured Threat Analysis Frameworks (mechanism `ACM-TMR-002`) |

---

## MITRE CAPEC v3.9

**O que esta ES traz para este capítulo:** contribui 2 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `CAPEC-25` | The adversary triggers and exploits a deadlock condition in the target software to cause a denial of service. A deadlock can occur when two or more competing actions are waiting for each other to fini | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `CAPEC-696` | An adversary exploits a hardware design flaw in a CPU implementation of transient instruction execution in which a faulting or assisted load instruction transiently forwards adversary-controlled data | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |

---

## ENISA — Multilayer AI Cybersecurity Practices (2023)

**O que esta ES traz para este capítulo:** contribui 2 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `ENISA-AI-FAICP-CONCLUSIONS` | Framework conclusions → threat modeling and risk governance integrity. Broad governance synthesis. Was: The conclusions synthesise the framework into a br | conceito: Explicit Threat Disposition Register (mechanism `ACM-TMR-004`) |
| `ENISA-AI-FAICP-LAYER-III` | Layer III sector-specific → threat modeling governance (regulatory) | conceito: Reviewer Accountability And Consistency Gates (mechanism `ACM-TMR-006`) |

---

## EU Cyber Resilience Act (CRA)

**O que esta ES traz para este capítulo:** contribui 1 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `CRA-ART-14` | Article 14 of Cyber Resilience Act | conceito: Threat Model Versioning Controls (mechanism `ACM-TMR-003`) |

---

## EU NIS2 Directive

**O que esta ES traz para este capítulo:** contribui 1 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `NIS2-ART-20` | Article 20 of Network and Information Security Directive (Directive (EU) 2022/2555). See validation passes in knowledge-graph working notes for detailed analysis. | conceito: Threat Representation Models (mechanism `ACM-TMR-001`) |

---

## EU GDPR (RGPD)

**O que esta ES traz para este capítulo:** contribui 1 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `GDPR-ART-35` | Article 35 of General Data Protection Regulation (Regulation (EU) 2016/679). See validation passes in knowledge-graph working notes for detailed analysis. | conceito: Threat Representation Models (mechanism `ACM-TMR-001`) |

---

## OWASP MCP Top 10 (v0.1, 2025 beta)

**O que esta ES traz para este capítulo:** contribui 1 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `MCP09-2025` | Shadow MCP servers → threat modeling governance (unauthorized deployment) | conceito: Reviewer Accountability And Consistency Gates (mechanism `ACM-TMR-006`) |

---

## OWASP Proactive Controls (2018)

**O que esta ES traz para este capítulo:** contribui 1 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `OPC-C1` | A security requirement is a statement of needed security functionality that ensures one of many different security properties of software is being satisfied. Security requirements are derived from ind | conceito: Requirements Registry And Derivation Traceability (mechanism `ACM-TMR-007`) |

---


<!-- WAVE-NOTE: **Nota Wave 1 ACO-SPC (traceability-only):** rows caveated de `asvs_v4_0_2` (`V8.3.2`, `V8.3.3`) e `nist_sp800_53_rev5` (`RA-6`, `SI-12*`, `SI-18*`, `SI-19*`, `SI-21`) mantêm-se aqui apenas como rastreabilidade non-core de privacidade, surveillance e revisão de risco. Não transformam o Cap. 03 em superfície positiva de `ACO-SPC`. -->
