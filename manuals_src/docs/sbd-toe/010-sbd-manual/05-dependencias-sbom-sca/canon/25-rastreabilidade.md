# 25. Rastreabilidade — Dependências, SBOM & SCA

## Sumário

Este capítulo trata de **integridade da supply chain de software** —
proveniência, dependências verificadas, SBOM, controlo de origem,
assinatura e verification semantics. As fontes externas seguintes
contribuem para esta área:

- **NIST SP 800-53 Rev. 5** — 196 referência(s)
- **CIS Controls v8.1.2** — 23 referência(s)
- **OWASP DSOMM** — 21 referência(s)
- **NIST SSDF (SP 800-218 v1.1)** — 18 referência(s)
- **OWASP SAMM v2.1** — 15 referência(s)
- **SLSA Specification v1.0 — Build Track** — 14 referência(s)
- **PCI DSS v4.0.1** — 13 referência(s)
- **SAFECode — Software Integrity Controls (2010)** — 9 referência(s)
- **OWASP ASVS v5.0.0** — 8 referência(s)
- **SAFECode — Practical Security Stories and Tasks for Agile Development (2012)** — 8 referência(s)
- **EU Digital Operational Resilience Act (DORA)** — 2 referência(s)
- **HIPAA Security Rule** — 2 referência(s)
- **OWASP MCP — Third-Party Servers v1.0** — 2 referência(s)
- **OWASP MCP Top 10 (v0.1, 2025 beta)** — 2 referência(s)
- **PCI Secure SLC v1.1** — 2 referência(s)
- **SAFECode — Fundamental Practices for Secure Software Development (2018)** — 2 referência(s)
- **MITRE CWE — Software Development View (v4.19.1)** — 1 referência(s)
- **EU Cyber Resilience Act (CRA)** — 1 referência(s)

---

## NIST SP 800-53 Rev. 5

**O que esta ES traz para este capítulo:** contribui 196 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `SP800-53-CP-10.4` | Provide the capability to restore system components within {{ insert: param, cp-10.04_odp }} from configuration-controlled and integrity-protected information representing a known, operational state f | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `SP800-53-CP-10.6` | Protect system components used for recovery and reconstitution. | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `SP800-53-CP-4.5` | Employ {{ insert: param, cp-04.05_odp.01 }} to {{ insert: param, cp-04.05_odp.02 }} to disrupt and adversely affect the system or system component. | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `SP800-53-CP-9` | Conduct backups of user-level information contained in {{ insert: param, cp-09_odp.01 }} {{ insert: param, cp-09_odp.02 }}; Conduct backups of system-level information contained in the system {{ inser | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `SP800-53-CP-9.1` | Test backup information {{ insert: param, cp-9.1_prm_1 }} to verify media reliability and information integrity. | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `SP800-53-IR-4.10` | Coordinate incident handling activities involving supply chain events with other organizations involved in the supply chain. | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `SP800-53-IR-6.3` | Provide incident information to the provider of the product or service and other organizations involved in the supply chain or supply chain governance for systems or system components related to the i | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `SP800-53-IR-9` | Respond to information spills by: Assigning {{ insert: param, ir-09_odp.01 }} with responsibility for responding to information spills; Identifying the specific information involved in the system cont | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `SP800-53-MA-2` | Schedule, document, and review records of maintenance, repair, and replacement on system components in accordance with manufacturer or vendor specifications and/or organizational requirements; Approve | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `SP800-53-MA-4.3` | Require that nonlocal maintenance and diagnostic services be performed from a system that implements a security capability comparable to the capability implemented on the system being serviced; or Rem | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `SP800-53-MA-4.6` | Implement the following cryptographic mechanisms to protect the integrity and confidentiality of nonlocal maintenance and diagnostic communications: {{ insert: param, ma-04.06_odp }}. | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `SP800-53-MP-6` | Sanitize {{ insert: param, mp-6_prm_1 }} prior to disposal, release out of organizational control, or release for reuse using {{ insert: param, mp-6_prm_2 }} ; and Employ sanitization mechanisms with | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `SP800-53-MP-8` | Establish {{ insert: param, mp-08_odp.01 }} that includes employing downgrading mechanisms with strength and integrity commensurate with the security category or classification of the information; Ver | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `SP800-53-PE-16` | Authorize and control {{ insert: param, pe-16_prm_1 }} entering and exiting the facility; and Maintain records of the system components. | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `SP800-53-PE-18` | Position system components within the facility to minimize potential damage from {{ insert: param, pe-18_odp }} and to minimize the opportunity for unauthorized access. | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `SP800-53-PE-19.1` | Protect system components, associated data communications, and networks in accordance with national Emissions Security policies and procedures based on the security category or classification of the i | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `SP800-53-PE-3.2` | Perform security checks {{ insert: param, pe-03.02_odp }} at the physical perimeter of the facility or system for exfiltration of information or removal of system components. | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `SP800-53-PL-2` | Develop security and privacy plans for the system that: Are consistent with the organization’s enterprise architecture; Explicitly define the constituent system components; Describe the operational co | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `SP800-53-PL-8` | Develop security and privacy architectures for the system that: Describe the requirements and approach to be taken for protecting the confidentiality, integrity, and availability of organizational inf | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `SP800-53-PM-24` | Establish a Data Integrity Board to: Review proposals to conduct or participate in a matching program; and Conduct an annual review of all matching programs in which the agency has participated. | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `SP800-53-PM-30` | Develop an organization-wide strategy for managing supply chain risks associated with the development, acquisition, maintenance, and disposal of systems, system components, and system services; Implem | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `SP800-53-PM-4` | Implement a process to ensure that plans of action and milestones for the information security, privacy, and supply chain risk management programs and associated organizational systems: Are developed | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `SP800-53-PM-7.1` | Offload {{ insert: param, pm-07.01_odp }} to other systems, system components, or an external provider. | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `SP800-53-SA-1` | Develop, document, and disseminate to {{ insert: param, sa-1_prm_1 }}: {{ insert: param, sa-01_odp.03 }} system and services acquisition policy that: Procedures to facilitate the implementation of the | conceito: DFD And Trust-Boundary Grounding (practice `ACP-TMR-002`) |
| `SP800-53-SA-10` | Require the developer of the system, system component, or system service to: Perform configuration management during system, component, or service {{ insert: param, sa-10_odp.01 }}; Document, manage, | conceito: Pipeline Definition As Reviewed Code (practice `ACP-SCBI-004`) |
| `SP800-53-SA-10.1` | Require the developer of the system, system component, or system service to enable integrity verification of software and firmware components. | conceito: Pipeline Definition As Reviewed Code (practice `ACP-SCBI-004`) |
| `SP800-53-SA-10.2` | Provide an alternate configuration management process using organizational personnel in the absence of a dedicated developer configuration management team. | conceito: Pipeline Definition As Reviewed Code (practice `ACP-SCBI-004`) |
| `SP800-53-SA-10.3` | Require the developer of the system, system component, or system service to enable integrity verification of hardware components. | conceito: Pipeline Definition As Reviewed Code (practice `ACP-SCBI-004`) |
| `SP800-53-SA-10.4` | Require the developer of the system, system component, or system service to employ tools for comparing newly generated versions of security-relevant hardware descriptions, source code, and object code | conceito: Pipeline Definition As Reviewed Code (practice `ACP-SCBI-004`) |
| `SP800-53-SA-10.5` | Require the developer of the system, system component, or system service to maintain the integrity of the mapping between the master build data describing the current version of security-relevant hard | conceito: Pipeline Definition As Reviewed Code (practice `ACP-SCBI-004`) |
| `SP800-53-SA-10.6` | Require the developer of the system, system component, or system service to execute procedures for ensuring that security-relevant hardware, software, and firmware updates distributed to the organizat | conceito: Pipeline Definition As Reviewed Code (practice `ACP-SCBI-004`) |
| `SP800-53-SA-10.7` | Require {{ insert: param, sa-10.7_prm_1 }} to be included in the {{ insert: param, sa-10.7_prm_2 }}. | conceito: Pipeline Definition As Reviewed Code (practice `ACP-SCBI-004`) |
| `SP800-53-SA-11` | Require the developer of the system, system component, or system service, at all post-design stages of the system development life cycle, to: Develop and implement a plan for ongoing security and priv | conceito: Governed Static Analysis Execution (practice `ACP-TSV-002`) |
| `SP800-53-SA-11.1` | Require the developer of the system, system component, or system service to employ static code analysis tools to identify common flaws and document the results of the analysis. | conceito: Governed Static Analysis Execution (practice `ACP-TSV-002`) |
| `SP800-53-SA-11.2` | Require the developer of the system, system component, or system service to perform threat modeling and vulnerability analyses during development and the subsequent testing and evaluation of the syste | conceito: Governed Static Analysis Execution (practice `ACP-TSV-002`) |
| `SP800-53-SA-11.3` | Require an independent agent satisfying {{ insert: param, sa-11.03_odp }} to verify the correct implementation of the developer security and privacy assessment plans and the evidence produced during t | conceito: Governed Static Analysis Execution (practice `ACP-TSV-002`) |
| `SP800-53-SA-11.4` | Require the developer of the system, system component, or system service to perform a manual code review of {{ insert: param, sa-11.04_odp.01 }} using the following processes, procedures, and/or techn | conceito: Governed Static Analysis Execution (practice `ACP-TSV-002`) |
| `SP800-53-SA-11.5` | Require the developer of the system, system component, or system service to perform penetration testing: At the following level of rigor: {{ insert: param, sa-11.5_prm_1 }} ; and Under the following c | conceito: Governed Static Analysis Execution (practice `ACP-TSV-002`) |
| `SP800-53-SA-11.6` | Require the developer of the system, system component, or system service to perform attack surface reviews. | conceito: Governed Static Analysis Execution (practice `ACP-TSV-002`) |
| `SP800-53-SA-11.7` | Require the developer of the system, system component, or system service to verify that the scope of testing and evaluation provides complete coverage of the required controls at the following level o | conceito: Governed Static Analysis Execution (practice `ACP-TSV-002`) |
| `SP800-53-SA-11.8` | Require the developer of the system, system component, or system service to employ dynamic code analysis tools to identify common flaws and document the results of the analysis. | conceito: Governed Static Analysis Execution (practice `ACP-TSV-002`) |
| `SP800-53-SA-11.9` | Require the developer of the system, system component, or system service to employ interactive application security testing tools to identify flaws and document the results. | conceito: Governed Static Analysis Execution (practice `ACP-TSV-002`) |
| `SP800-53-SA-12` | Supply Chain Protection | conceito: Automated Dependency And Image Risk Gating (practice `ACP-SCBI-002`) |
| `SP800-53-SA-12.1` | Acquisition Strategies / Tools / Methods | conceito: Automated Dependency And Image Risk Gating (practice `ACP-SCBI-002`) |
| `SP800-53-SA-12.10` | Validate as Genuine and Not Altered | conceito: Automated Dependency And Image Risk Gating (practice `ACP-SCBI-002`) |
| `SP800-53-SA-12.11` | Penetration Testing / Analysis of Elements, Processes, and Actors | conceito: Automated Dependency And Image Risk Gating (practice `ACP-SCBI-002`) |
| `SP800-53-SA-12.12` | Inter-organizational Agreements | conceito: Automated Dependency And Image Risk Gating (practice `ACP-SCBI-002`) |
| `SP800-53-SA-12.13` | Critical Information System Components | conceito: Automated Dependency And Image Risk Gating (practice `ACP-SCBI-002`) |
| `SP800-53-SA-12.14` | Identity and Traceability | conceito: Automated Dependency And Image Risk Gating (practice `ACP-SCBI-002`) |
| `SP800-53-SA-12.15` | Processes to Address Weaknesses or Deficiencies | conceito: Automated Dependency And Image Risk Gating (practice `ACP-SCBI-002`) |
| `SP800-53-SA-12.2` | Supplier Reviews | conceito: Automated Dependency And Image Risk Gating (practice `ACP-SCBI-002`) |
| `SP800-53-SA-12.3` | Trusted Shipping and Warehousing | conceito: Automated Dependency And Image Risk Gating (practice `ACP-SCBI-002`) |
| `SP800-53-SA-12.4` | Diversity of Suppliers | conceito: Automated Dependency And Image Risk Gating (practice `ACP-SCBI-002`) |
| `SP800-53-SA-12.5` | Limitation of Harm | conceito: Automated Dependency And Image Risk Gating (practice `ACP-SCBI-002`) |
| `SP800-53-SA-12.6` | Minimizing Procurement Time | conceito: Automated Dependency And Image Risk Gating (practice `ACP-SCBI-002`) |
| `SP800-53-SA-12.7` | Assessments Prior to Selection / Acceptance / Update | conceito: Automated Dependency And Image Risk Gating (practice `ACP-SCBI-002`) |
| `SP800-53-SA-12.8` | Use of All-source Intelligence | conceito: Automated Dependency And Image Risk Gating (practice `ACP-SCBI-002`) |
| `SP800-53-SA-12.9` | Operations Security | conceito: Automated Dependency And Image Risk Gating (practice `ACP-SCBI-002`) |
| `SP800-53-SA-13` | Trustworthiness | conceito: Pipeline Definition As Reviewed Code (practice `ACP-SCBI-004`) |
| `SP800-53-SA-14` | Criticality Analysis | conceito: Threat Model Creation And Triggered Refresh (practice `ACP-TMR-001`) |
| `SP800-53-SA-14.1` | Critical Components with No Viable Alternative Sourcing | conceito: Threat Model Creation And Triggered Refresh (practice `ACP-TMR-001`) |
| `SP800-53-SA-15` | Require the developer of the system, system component, or system service to follow a documented development process that: Explicitly addresses security and privacy requirements; Identifies the standar | conceito: Pipeline Definition As Reviewed Code (practice `ACP-SCBI-004`) |
| `SP800-53-SA-15.1` | Require the developer of the system, system component, or system service to: Define quality metrics at the beginning of the development process; and Provide evidence of meeting the quality metrics {{ | conceito: Pipeline Definition As Reviewed Code (practice `ACP-SCBI-004`) |
| `SP800-53-SA-15.10` | Require the developer of the system, system component, or system service to provide, implement, and test an incident response plan. | conceito: Pipeline Definition As Reviewed Code (practice `ACP-SCBI-004`) |
| `SP800-53-SA-15.11` | Require the developer of the system or system component to archive the system or component to be released or delivered together with the corresponding evidence supporting the final security and privac | conceito: Pipeline Definition As Reviewed Code (practice `ACP-SCBI-004`) |
| `SP800-53-SA-15.12` | Require the developer of the system or system component to minimize the use of personally identifiable information in development and test environments. | conceito: Pipeline Definition As Reviewed Code (practice `ACP-SCBI-004`) |
| `SP800-53-SA-15.13` | Require the developer of the system or system component to minimize the use of personally identifiable information in development and test environments. | conceito: Pipeline Definition As Reviewed Code (practice `ACP-SCBI-004`) |
| `SP800-53-SA-15.2` | Require the developer of the system, system component, or system service to select and employ security and privacy tracking tools for use during the development process. | conceito: Pipeline Definition As Reviewed Code (practice `ACP-SCBI-004`) |
| `SP800-53-SA-15.3` | Require the developer of the system, system component, or system service to perform a criticality analysis: At the following decision points in the system development life cycle: {{ insert: param, sa- | conceito: Pipeline Definition As Reviewed Code (practice `ACP-SCBI-004`) |
| `SP800-53-SA-15.4` | Threat Modeling and Vulnerability Analysis | conceito: Pipeline Definition As Reviewed Code (practice `ACP-SCBI-004`) |
| `SP800-53-SA-15.5` | Require the developer of the system, system component, or system service to reduce attack surfaces to {{ insert: param, sa-15.05_odp }}. | conceito: Pipeline Definition As Reviewed Code (practice `ACP-SCBI-004`) |
| `SP800-53-SA-15.6` | Require the developer of the system, system component, or system service to implement an explicit process to continuously improve the development process. | conceito: Pipeline Definition As Reviewed Code (practice `ACP-SCBI-004`) |
| `SP800-53-SA-15.7` | Require the developer of the system, system component, or system service {{ insert: param, sa-15.07_odp.01 }} to: Perform an automated vulnerability analysis using {{ insert: param, sa-15.07_odp.02 }} | conceito: Pipeline Definition As Reviewed Code (practice `ACP-SCBI-004`) |
| `SP800-53-SA-15.8` | Require the developer of the system, system component, or system service to use threat modeling and vulnerability analyses from similar systems, components, or services to inform the current developme | conceito: Pipeline Definition As Reviewed Code (practice `ACP-SCBI-004`) |
| `SP800-53-SA-15.9` | Use of Live Data | conceito: Pipeline Definition As Reviewed Code (practice `ACP-SCBI-004`) |
| `SP800-53-SA-16` | Require the developer of the system, system component, or system service to provide the following training on the correct use and operation of the implemented security and privacy functions, controls, | conceito: DFD And Trust-Boundary Grounding (practice `ACP-TMR-002`) |
| `SP800-53-SA-17` | Require the developer of the system, system component, or system service to produce a design specification and security and privacy architecture that: Is consistent with the organization’s security an | conceito: Architecture Review And Approval Governance (practice `ACP-ATB-005`) |
| `SP800-53-SA-17.1` | Require the developer of the system, system component, or system service to: Produce, as an integral part of the development process, a formal policy model describing the {{ insert: param, sa-17.1_prm | conceito: Architecture Review And Approval Governance (practice `ACP-ATB-005`) |
| `SP800-53-SA-17.2` | Require the developer of the system, system component, or system service to: Define security-relevant hardware, software, and firmware; and Provide a rationale that the definition for security-relevan | conceito: Architecture Review And Approval Governance (practice `ACP-ATB-005`) |
| `SP800-53-SA-17.3` | Require the developer of the system, system component, or system service to: Produce, as an integral part of the development process, a formal top-level specification that specifies the interfaces to | conceito: Architecture Review And Approval Governance (practice `ACP-ATB-005`) |
| `SP800-53-SA-17.4` | Require the developer of the system, system component, or system service to: Produce, as an integral part of the development process, an informal descriptive top-level specification that specifies the | conceito: Architecture Review And Approval Governance (practice `ACP-ATB-005`) |
| `SP800-53-SA-17.5` | Require the developer of the system, system component, or system service to: Design and structure the security-relevant hardware, software, and firmware to use a complete, conceptually simple protecti | conceito: Architecture Review And Approval Governance (practice `ACP-ATB-005`) |
| `SP800-53-SA-17.6` | Require the developer of the system, system component, or system service to structure security-relevant hardware, software, and firmware to facilitate testing. | conceito: Architecture Review And Approval Governance (practice `ACP-ATB-005`) |
| `SP800-53-SA-17.7` | Require the developer of the system, system component, or system service to structure security-relevant hardware, software, and firmware to facilitate controlling access with least privilege. | conceito: Architecture Review And Approval Governance (practice `ACP-ATB-005`) |
| `SP800-53-SA-17.8` | Design {{ insert: param, sa-17.08_odp.01 }} with coordinated behavior to implement the following capabilities: {{ insert: param, sa-17.08_odp.02 }}. | conceito: Architecture Review And Approval Governance (practice `ACP-ATB-005`) |
| `SP800-53-SA-17.9` | Use different designs for {{ insert: param, sa-17.09_odp }} to satisfy a common set of requirements or to provide equivalent functionality. | conceito: Architecture Review And Approval Governance (practice `ACP-ATB-005`) |
| `SP800-53-SA-18` | Tamper Resistance and Detection | conceito: Artifact Signature And Provenance Validation (practice `ACP-SCBI-006`) |
| `SP800-53-SA-18.1` | Multiple Phases of System Development Life Cycle | conceito: Artifact Signature And Provenance Validation (practice `ACP-SCBI-006`) |
| `SP800-53-SA-18.2` | Inspection of Systems or Components | conceito: Artifact Signature And Provenance Validation (practice `ACP-SCBI-006`) |
| `SP800-53-SA-19` | Component Authenticity | conceito: Artifact Signature And Provenance Validation (practice `ACP-SCBI-006`) |
| `SP800-53-SA-19.1` | Anti-counterfeit Training | conceito: Artifact Signature And Provenance Validation (practice `ACP-SCBI-006`) |
| `SP800-53-SA-19.2` | Configuration Control for Component Service and Repair | conceito: Artifact Signature And Provenance Validation (practice `ACP-SCBI-006`) |
| `SP800-53-SA-19.3` | Component Disposal | conceito: Artifact Signature And Provenance Validation (practice `ACP-SCBI-006`) |
| `SP800-53-SA-19.4` | Anti-counterfeit Scanning | conceito: Artifact Signature And Provenance Validation (practice `ACP-SCBI-006`) |
| `SP800-53-SA-2` | Determine the high-level information security and privacy requirements for the system or system service in mission and business process planning; Determine, document, and allocate the resources requir | conceito: Threat Traceability Into Requirements And Validation (practice `ACP-TMR-005`) |
| `SP800-53-SA-21` | Require that the developer of {{ insert: param, sa-21_odp.01 }}: Has appropriate access authorizations as determined by assigned {{ insert: param, sa-21_odp.02 }} ; and Satisfies the following additio | conceito: Least-Privilege Authorization Governance (practice `ACP-IAT-002`) |
| `SP800-53-SA-21.1` | Validation of Screening | conceito: Least-Privilege Authorization Governance (practice `ACP-IAT-002`) |
| `SP800-53-SA-22` | Replace system components when support for the components is no longer available from the developer, vendor, or manufacturer; or Provide the following options for alternative sources for continued sup | conceito: Automated Dependency And Image Risk Gating (practice `ACP-SCBI-002`) |
| `SP800-53-SA-22.1` | Alternative Sources for Continued Support | conceito: Automated Dependency And Image Risk Gating (practice `ACP-SCBI-002`) |
| `SP800-53-SA-23` | Employ {{ insert: param, sa-23_odp.01 }} on {{ insert: param, sa-23_odp.02 }} supporting mission essential services or functions to increase the trustworthiness in those systems or components. | conceito: Trust-Boundary And Flow Review (practice `ACP-ATB-003`) |
| `SP800-53-SA-24` | Design organizational systems, system components, or system services to achieve cyber resiliency by: Defining the following cyber resiliency goals: {{ insert: param, sa-24_odp.01 }}. Defining the foll | conceito: Architectural Decision And Solution Traceability (practice `ACP-ATB-002`) |
| `SP800-53-SA-3` | Acquire, develop, and manage the system using {{ insert: param, sa-03_odp }} that incorporates information security and privacy considerations; Define and document information security and privacy rol | conceito: DFD And Trust-Boundary Grounding (practice `ACP-TMR-002`) |
| `SP800-53-SA-3.1` | Protect system preproduction environments commensurate with risk throughout the system development life cycle for the system, system component, or system service. | conceito: DFD And Trust-Boundary Grounding (practice `ACP-TMR-002`) |
| `SP800-53-SA-3.2` | Approve, document, and control the use of live data in preproduction environments for the system, system component, or system service; and Protect preproduction environments for the system, system com | conceito: DFD And Trust-Boundary Grounding (practice `ACP-TMR-002`) |
| `SP800-53-SA-3.3` | Plan for and implement a technology refresh schedule for the system throughout the system development life cycle. | conceito: DFD And Trust-Boundary Grounding (practice `ACP-TMR-002`) |
| `SP800-53-SA-4` | Include the following requirements, descriptions, and criteria, explicitly or by reference, using {{ insert: param, sa-04_odp.01 }} in the acquisition contract for the system, system component, or sys | conceito: Trust Boundary And Integration Review (practice `ACP-ITS-001`) |
| `SP800-53-SA-4.1` | Require the developer of the system, system component, or system service to provide a description of the functional properties of the controls to be implemented. | conceito: Trust Boundary And Integration Review (practice `ACP-ITS-001`) |
| `SP800-53-SA-4.10` | Employ only information technology products on the FIPS 201-approved products list for Personal Identity Verification (PIV) capability implemented within organizational systems. | conceito: Trust Boundary And Integration Review (practice `ACP-ITS-001`) |
| `SP800-53-SA-4.11` | Include {{ insert: param, sa-04.11_odp }} in the acquisition contract for the operation of a system of records on behalf of an organization to accomplish an organizational mission or function. | conceito: Trust Boundary And Integration Review (practice `ACP-ITS-001`) |
| `SP800-53-SA-4.12` | Include organizational data ownership requirements in the acquisition contract; and Require all data to be removed from the contractor’s system and returned to the organization within {{ insert: param | conceito: Trust Boundary And Integration Review (practice `ACP-ITS-001`) |
| `SP800-53-SA-4.2` | Require the developer of the system, system component, or system service to provide design and implementation information for the controls that includes: {{ insert: param, sa-04.02_odp.01 }} at {{ ins | conceito: Trust Boundary And Integration Review (practice `ACP-ITS-001`) |
| `SP800-53-SA-4.3` | Require the developer of the system, system component, or system service to demonstrate the use of a system development life cycle process that includes: {{ insert: param, sa-04.03_odp.01 }}; {{ inser | conceito: Trust Boundary And Integration Review (practice `ACP-ITS-001`) |
| `SP800-53-SA-4.4` | Assignment of Components to Systems | conceito: Trust Boundary And Integration Review (practice `ACP-ITS-001`) |
| `SP800-53-SA-4.5` | Require the developer of the system, system component, or system service to: Deliver the system, component, or service with {{ insert: param, sa-04.05_odp }} implemented; and Use the configurations as | conceito: Trust Boundary And Integration Review (practice `ACP-ITS-001`) |
| `SP800-53-SA-4.6` | Employ only government off-the-shelf or commercial off-the-shelf information assurance and information assurance-enabled information technology products that compose an NSA-approved solution to protec | conceito: Trust Boundary And Integration Review (practice `ACP-ITS-001`) |
| `SP800-53-SA-4.7` | Limit the use of commercially provided information assurance and information assurance-enabled information technology products to those products that have been successfully evaluated against a Nationa | conceito: Trust Boundary And Integration Review (practice `ACP-ITS-001`) |
| `SP800-53-SA-4.8` | Require the developer of the system, system component, or system service to produce a plan for continuous monitoring of control effectiveness that is consistent with the continuous monitoring program | conceito: Trust Boundary And Integration Review (practice `ACP-ITS-001`) |
| `SP800-53-SA-4.9` | Require the developer of the system, system component, or system service to identify the functions, ports, protocols, and services intended for organizational use. | conceito: Trust Boundary And Integration Review (practice `ACP-ITS-001`) |
| `SP800-53-SA-5.1` | Functional Properties of Security Controls | conceito: Architecture Baseline Definition (practice `ACP-ATB-001`) |
| `SP800-53-SA-5.2` | Security-relevant External System Interfaces | conceito: Architecture Baseline Definition (practice `ACP-ATB-001`) |
| `SP800-53-SA-5.3` | High-level Design | conceito: Architecture Baseline Definition (practice `ACP-ATB-001`) |
| `SP800-53-SA-5.4` | Low-level Design | conceito: Architecture Baseline Definition (practice `ACP-ATB-001`) |
| `SP800-53-SA-5.5` | Source Code | conceito: Architecture Baseline Definition (practice `ACP-ATB-001`) |
| `SP800-53-SA-6` | Software Usage Restrictions | conceito: Approved Source And Registry Governance (practice `ACP-SCBI-003`) |
| `SP800-53-SA-7` | User-installed Software | conceito: Approved Source And Registry Governance (practice `ACP-SCBI-003`) |
| `SP800-53-SA-8` | Apply the following systems security and privacy engineering principles in the specification, design, development, implementation, and modification of the system and system components: {{ insert: para | conceito: Architectural Decision And Solution Traceability (practice `ACP-ATB-002`) |
| `SP800-53-SA-8.1` | Implement the security design principle of clear abstractions. | conceito: Architectural Decision And Solution Traceability (practice `ACP-ATB-002`) |
| `SP800-53-SA-8.10` | Implement the security design principle of hierarchical trust in {{ insert: param, sa-08.10_odp }}. | conceito: Architectural Decision And Solution Traceability (practice `ACP-ATB-002`) |
| `SP800-53-SA-8.11` | Implement the security design principle of inverse modification threshold in {{ insert: param, sa-08.11_odp }}. | conceito: Architectural Decision And Solution Traceability (practice `ACP-ATB-002`) |
| `SP800-53-SA-8.12` | Implement the security design principle of hierarchical protection in {{ insert: param, sa-08.12_odp }}. | conceito: Architectural Decision And Solution Traceability (practice `ACP-ATB-002`) |
| `SP800-53-SA-8.13` | Implement the security design principle of minimized security elements in {{ insert: param, sa-08.13_odp }}. | conceito: Architectural Decision And Solution Traceability (practice `ACP-ATB-002`) |
| `SP800-53-SA-8.14` | Implement the security design principle of least privilege in {{ insert: param, sa-08.14_odp }}. | conceito: Architectural Decision And Solution Traceability (practice `ACP-ATB-002`) |
| `SP800-53-SA-8.15` | Implement the security design principle of predicate permission in {{ insert: param, sa-08.15_odp }}. | conceito: Architectural Decision And Solution Traceability (practice `ACP-ATB-002`) |
| `SP800-53-SA-8.16` | Implement the security design principle of self-reliant trustworthiness in {{ insert: param, sa-08.16_odp }}. | conceito: Architectural Decision And Solution Traceability (practice `ACP-ATB-002`) |
| `SP800-53-SA-8.17` | Implement the security design principle of secure distributed composition in {{ insert: param, sa-08.17_odp }}. | conceito: Architectural Decision And Solution Traceability (practice `ACP-ATB-002`) |
| `SP800-53-SA-8.18` | Implement the security design principle of trusted communications channels in {{ insert: param, sa-08.18_odp }}. | conceito: Architectural Decision And Solution Traceability (practice `ACP-ATB-002`) |
| `SP800-53-SA-8.19` | Implement the security design principle of continuous protection in {{ insert: param, sa-08.19_odp }}. | conceito: Architectural Decision And Solution Traceability (practice `ACP-ATB-002`) |
| `SP800-53-SA-8.2` | Implement the security design principle of least common mechanism in {{ insert: param, sa-08.02_odp }}. | conceito: Architectural Decision And Solution Traceability (practice `ACP-ATB-002`) |
| `SP800-53-SA-8.20` | Implement the security design principle of secure metadata management in {{ insert: param, sa-08.20_odp }}. | conceito: Architectural Decision And Solution Traceability (practice `ACP-ATB-002`) |
| `SP800-53-SA-8.21` | Implement the security design principle of self-analysis in {{ insert: param, sa-08.21_odp }}. | conceito: Architectural Decision And Solution Traceability (practice `ACP-ATB-002`) |
| `SP800-53-SA-8.22` | Implement the security design principle of accountability and traceability in {{ insert: param, sa-8.22_prm_1 }}. | conceito: Architectural Decision And Solution Traceability (practice `ACP-ATB-002`) |
| `SP800-53-SA-8.23` | Implement the security design principle of secure defaults in {{ insert: param, sa-08.23_odp }}. | conceito: Architectural Decision And Solution Traceability (practice `ACP-ATB-002`) |
| `SP800-53-SA-8.24` | Implement the security design principle of secure failure and recovery in {{ insert: param, sa-8.24_prm_1 }}. | conceito: Architectural Decision And Solution Traceability (practice `ACP-ATB-002`) |
| `SP800-53-SA-8.25` | Implement the security design principle of economic security in {{ insert: param, sa-08.25_odp }}. | conceito: Architectural Decision And Solution Traceability (practice `ACP-ATB-002`) |
| `SP800-53-SA-8.26` | Implement the security design principle of performance security in {{ insert: param, sa-08.26_odp }}. | conceito: Architectural Decision And Solution Traceability (practice `ACP-ATB-002`) |
| `SP800-53-SA-8.27` | Implement the security design principle of human factored security in {{ insert: param, sa-08.27_odp }}. | conceito: Architectural Decision And Solution Traceability (practice `ACP-ATB-002`) |
| `SP800-53-SA-8.28` | Implement the security design principle of acceptable security in {{ insert: param, sa-08.28_odp }}. | conceito: Architectural Decision And Solution Traceability (practice `ACP-ATB-002`) |
| `SP800-53-SA-8.29` | Implement the security design principle of repeatable and documented procedures in {{ insert: param, sa-08.29_odp }}. | conceito: Architectural Decision And Solution Traceability (practice `ACP-ATB-002`) |
| `SP800-53-SA-8.3` | Implement the security design principles of modularity and layering in {{ insert: param, sa-8.3_prm_1 }}. | conceito: Architectural Decision And Solution Traceability (practice `ACP-ATB-002`) |
| `SP800-53-SA-8.30` | Implement the security design principle of procedural rigor in {{ insert: param, sa-08.30_odp }}. | conceito: Architectural Decision And Solution Traceability (practice `ACP-ATB-002`) |
| `SP800-53-SA-8.31` | Implement the security design principle of secure system modification in {{ insert: param, sa-08.31_odp }}. | conceito: Architectural Decision And Solution Traceability (practice `ACP-ATB-002`) |
| `SP800-53-SA-8.32` | Implement the security design principle of sufficient documentation in {{ insert: param, sa-08.32_odp }}. | conceito: Architectural Decision And Solution Traceability (practice `ACP-ATB-002`) |
| `SP800-53-SA-8.33` | Implement the privacy principle of minimization using {{ insert: param, sa-08.33_odp }}. | conceito: Architectural Decision And Solution Traceability (practice `ACP-ATB-002`) |
| `SP800-53-SA-8.4` | Implement the security design principle of partially ordered dependencies in {{ insert: param, sa-08.04_odp }}. | conceito: Architectural Decision And Solution Traceability (practice `ACP-ATB-002`) |
| `SP800-53-SA-8.5` | Implement the security design principle of efficiently mediated access in {{ insert: param, sa-08.05_odp }}. | conceito: Architectural Decision And Solution Traceability (practice `ACP-ATB-002`) |
| `SP800-53-SA-8.6` | Implement the security design principle of minimized sharing in {{ insert: param, sa-08.06_odp }}. | conceito: Architectural Decision And Solution Traceability (practice `ACP-ATB-002`) |
| `SP800-53-SA-8.7` | Implement the security design principle of reduced complexity in {{ insert: param, sa-08.07_odp }}. | conceito: Architectural Decision And Solution Traceability (practice `ACP-ATB-002`) |
| `SP800-53-SA-8.8` | Implement the security design principle of secure evolvability in {{ insert: param, sa-08.08_odp }}. | conceito: Architectural Decision And Solution Traceability (practice `ACP-ATB-002`) |
| `SP800-53-SA-8.9` | Implement the security design principle of trusted components in {{ insert: param, sa-08.09_odp }}. | conceito: Architectural Decision And Solution Traceability (practice `ACP-ATB-002`) |
| `SP800-53-SA-9` | Require that providers of external system services comply with organizational security and privacy requirements and employ the following controls: {{ insert: param, sa-09_odp.01 }}; Define and documen | conceito: Trust Boundary And Integration Review (practice `ACP-ITS-001`) |
| `SP800-53-SA-9.1` | Conduct an organizational assessment of risk prior to the acquisition or outsourcing of information security services; and Verify that the acquisition or outsourcing of dedicated information security | conceito: Trust Boundary And Integration Review (practice `ACP-ITS-001`) |
| `SP800-53-SA-9.2` | Require providers of the following external system services to identify the functions, ports, protocols, and other services required for the use of such services: {{ insert: param, sa-09.02_odp }}. | conceito: Trust Boundary And Integration Review (practice `ACP-ITS-001`) |
| `SP800-53-SA-9.3` | Establish, document, and maintain trust relationships with external service providers based on the following requirements, properties, factors, or conditions: {{ insert: param, sa-9.3_prm_1 }}. | conceito: Trust Boundary And Integration Review (practice `ACP-ITS-001`) |
| `SP800-53-SA-9.4` | Take the following actions to verify that the interests of {{ insert: param, sa-09.04_odp.01 }} are consistent with and reflect organizational interests: {{ insert: param, sa-09.04_odp.02 }}. | conceito: Trust Boundary And Integration Review (practice `ACP-ITS-001`) |
| `SP800-53-SA-9.5` | Restrict the location of {{ insert: param, sa-09.05_odp.01 }} to {{ insert: param, sa-09.05_odp.02 }} based on {{ insert: param, sa-09.05_odp.03 }}. | conceito: Trust Boundary And Integration Review (practice `ACP-ITS-001`) |
| `SP800-53-SA-9.6` | Maintain exclusive control of cryptographic keys for encrypted material stored or transmitted through an external system. | conceito: Trust Boundary And Integration Review (practice `ACP-ITS-001`) |
| `SP800-53-SA-9.7` | Provide the capability to check the integrity of information while it resides in the external system. | conceito: Trust Boundary And Integration Review (practice `ACP-ITS-001`) |
| `SP800-53-SA-9.8` | Restrict the geographic location of information processing and data storage to facilities located within in the legal jurisdictional boundary of the United States. | conceito: Trust Boundary And Integration Review (practice `ACP-ITS-001`) |
| `SP800-53-SC-13.4` | Digital Signatures | conceito: Artifact Signature And Provenance Validation (practice `ACP-SCBI-006`) |
| `SP800-53-SR-1` | Develop, document, and disseminate to {{ insert: param, sr-1_prm_1 }}: {{ insert: param, sr-01_odp.03 }} supply chain risk management policy that: Procedures to facilitate the implementation of the su | conceito: Approved Source And Registry Governance (practice `ACP-SCBI-003`) |
| `SP800-53-SR-10` | Inspect the following systems or system components {{ insert: param, sr-10_odp.02 }} to detect tampering: {{ insert: param, sr-10_odp.01 }}. | conceito: Staged Dynamic Testing And Gate Enforcement (practice `ACP-TSV-005`) |
| `SP800-53-SR-11` | Develop and implement anti-counterfeit policy and procedures that include the means to detect and prevent counterfeit components from entering the system; and Report counterfeit system components to { | conceito: Artifact Signature And Provenance Validation (practice `ACP-SCBI-006`) |
| `SP800-53-SR-11.1` | Train {{ insert: param, sr-11.01_odp }} to detect counterfeit system components (including hardware, software, and firmware). | conceito: Artifact Signature And Provenance Validation (practice `ACP-SCBI-006`) |
| `SP800-53-SR-11.2` | Maintain configuration control over the following system components awaiting service or repair and serviced or repaired components awaiting return to service: {{ insert: param, sr-11.02_odp }}. | conceito: Artifact Signature And Provenance Validation (practice `ACP-SCBI-006`) |
| `SP800-53-SR-11.3` | Scan for counterfeit system components {{ insert: param, sr-11.03_odp }}. | conceito: Artifact Signature And Provenance Validation (practice `ACP-SCBI-006`) |
| `SP800-53-SR-12` | Dispose of {{ insert: param, sr-12_odp.01 }} using the following techniques and methods: {{ insert: param, sr-12_odp.02 }}. | conceito: Build-Linked SBOM Generation (practice `ACP-SCBI-001`) |
| `SP800-53-SR-2` | Develop a plan for managing supply chain risks associated with the research and development, design, manufacturing, acquisition, delivery, integration, operations and maintenance, and disposal of the | conceito: Automated Dependency And Image Risk Gating (practice `ACP-SCBI-002`) |
| `SP800-53-SR-2.1` | Establish a supply chain risk management team consisting of {{ insert: param, sr-02.01_odp.01 }} to lead and support the following SCRM activities: {{ insert: param, sr-02.01_odp.02 }}. | conceito: Automated Dependency And Image Risk Gating (practice `ACP-SCBI-002`) |
| `SP800-53-SR-3` | Establish a process or processes to identify and address weaknesses or deficiencies in the supply chain elements and processes of {{ insert: param, sr-03_odp.01 }} in coordination with {{ insert: para | conceito: Approved Source And Registry Governance (practice `ACP-SCBI-003`) |
| `SP800-53-SR-3.1` | Employ a diverse set of sources for the following system components and services: {{ insert: param, sr-3.1_prm_1 }}. | conceito: Approved Source And Registry Governance (practice `ACP-SCBI-003`) |
| `SP800-53-SR-3.2` | Employ the following controls to limit harm from potential adversaries identifying and targeting the organizational supply chain: {{ insert: param, sr-03.02_odp }}. | conceito: Approved Source And Registry Governance (practice `ACP-SCBI-003`) |
| `SP800-53-SR-3.3` | Ensure that the controls included in the contracts of prime contractors are also included in the contracts of subcontractors. | conceito: Approved Source And Registry Governance (practice `ACP-SCBI-003`) |
| `SP800-53-SR-4` | Document, monitor, and maintain valid provenance of the following systems, system components, and associated data: {{ insert: param, sr-04_odp }}. | conceito: Artifact Signature And Provenance Validation (practice `ACP-SCBI-006`) |
| `SP800-53-SR-4.1` | Establish and maintain unique identification of the following supply chain elements, processes, and personnel associated with the identified system and critical system components: {{ insert: param, sr | conceito: Artifact Signature And Provenance Validation (practice `ACP-SCBI-006`) |
| `SP800-53-SR-4.2` | Establish and maintain unique identification of the following systems and critical system components for tracking through the supply chain: {{ insert: param, sr-04.02_odp }}. | conceito: Artifact Signature And Provenance Validation (practice `ACP-SCBI-006`) |
| `SP800-53-SR-4.3` | Employ the following controls to validate that the system or system component received is genuine and has not been altered: {{ insert: param, sr-4.3_prm_1 }}. | conceito: Artifact Signature And Provenance Validation (practice `ACP-SCBI-006`) |
| `SP800-53-SR-4.4` | Employ {{ insert: param, sr-04.04_odp.01 }} and conduct {{ insert: param, sr-04.04_odp.02 }} to ensure the integrity of the system and system components by validating the internal composition and prov | conceito: Artifact Signature And Provenance Validation (practice `ACP-SCBI-006`) |
| `SP800-53-SR-5` | Employ the following acquisition strategies, contract tools, and procurement methods to protect against, identify, and mitigate supply chain risks: {{ insert: param, sr-05_odp }}. | conceito: Automated Dependency And Image Risk Gating (practice `ACP-SCBI-002`) |
| `SP800-53-SR-5.1` | Employ the following controls to ensure an adequate supply of {{ insert: param, sr-05.01_odp.02 }}: {{ insert: param, sr-05.01_odp.01 }}. | conceito: Automated Dependency And Image Risk Gating (practice `ACP-SCBI-002`) |
| `SP800-53-SR-5.2` | Assess the system, system component, or system service prior to selection, acceptance, modification, or update. | conceito: Automated Dependency And Image Risk Gating (practice `ACP-SCBI-002`) |
| `SP800-53-SR-6` | Assess and review the supply chain-related risks associated with suppliers or contractors and the system, system component, or system service they provide {{ insert: param, sr-06_odp }}. | conceito: Automated Dependency And Image Risk Gating (practice `ACP-SCBI-002`) |
| `SP800-53-SR-6.1` | Employ {{ insert: param, sr-06.01_odp.01 }} of the following supply chain elements, processes, and actors associated with the system, system component, or system service: {{ insert: param, sr-06.01_od | conceito: Automated Dependency And Image Risk Gating (practice `ACP-SCBI-002`) |
| `SP800-53-SR-7` | Employ the following Operations Security (OPSEC) controls to protect supply chain-related information for the system, system component, or system service: {{ insert: param, sr-07_odp }}. | conceito: Approved Source And Registry Governance (practice `ACP-SCBI-003`) |
| `SP800-53-SR-8` | Establish agreements and procedures with entities involved in the supply chain for the system, system component, or system service for the {{ insert: param, sr-08_odp.01 }}. | conceito: Threat Traceability Into Requirements And Validation (practice `ACP-TMR-005`) |
| `SP800-53-SR-9` | Implement a tamper protection program for the system, system component, or system service. | conceito: Artifact Signature And Provenance Validation (practice `ACP-SCBI-006`) |
| `SP800-53-SR-9.1` | Employ anti-tamper technologies, tools, and techniques throughout the system development life cycle. | conceito: Artifact Signature And Provenance Validation (practice `ACP-SCBI-006`) |

---

## CIS Controls v8.1.2

**O que esta ES traz para este capítulo:** contribui 23 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `CIS-1` | Actively manage (inventory, track, and correct) all enterprise assets (end-user devices, including portable and mobile; network devices; non-computing/Internet of Things (IoT) devices; and servers) co | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `CIS-1.1` | Establish and maintain an accurate, detailed, and up-to-date inventory of all enterprise assets with the potential to store or process data, to include: end-user devices (including portable and mobile | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `CIS-1.2` | Ensure that a process exists to address unauthorized assets on a weekly basis. The enterprise may choose to remove the asset from the network, deny the asset from connecting remotely to the network, o | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `CIS-1.3` | Utilize an active discovery tool to identify assets connected to the enterprise’s network. Configure the active discovery tool to execute daily, or more frequently. | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `CIS-1.4` | Use DHCP logging on all DHCP servers or Internet Protocol (IP) address management tools to update the enterprise’s asset inventory. Review and use logs to update the enterprise’s asset inventory weekl | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `CIS-1.5` | Use a passive discovery tool to identify assets connected to the enterprise’s network. Review and use scans to update the enterprise’s asset inventory at least weekly, or more frequently. | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `CIS-10` | Prevent or control the installation, spread, and execution of malicious applications, code, or scripts on enterprise assets. | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `CIS-10.1` | Deploy and maintain anti-malware software on all enterprise assets. | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `CIS-10.2` | Configure automatic updates for anti-malware signature files on all enterprise assets. | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `CIS-10.3` | Disable autorun and autoplay auto-execute functionality for removable media. | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `CIS-10.4` | Configure anti-malware software to automatically scan removable media. | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |
| `CIS-10.5` | Enable anti-exploitation features on enterprise assets and software, where possible, such as Microsoft® Data Execution Prevention (DEP), Windows® Defender Exploit Guard (WDEG), or Apple® System Integr | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `CIS-10.6` | Centrally manage anti-malware software. | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `CIS-10.7` | Use behavior-based anti-malware software. | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `CIS-17.1` | Designate one key person, and at least one backup, who will manage the enterprise’s incident handling process. Management personnel are responsible for the coordination and documentation of incident r | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `CIS-2` | Actively manage (inventory, track, and correct) all software (operating systems and applications) on the network so that only authorized software is installed and can execute, and that unauthorized an | conceito: Build And Image Inventory Generation (mechanism `ACM-SCBI-005`) |
| `CIS-2.1` | Establish and maintain a detailed inventory of all licensed software installed on enterprise assets. The software inventory must document the title, publisher, initial install/use date, and business p | conceito: Build And Image Inventory Generation (mechanism `ACM-SCBI-005`) |
| `CIS-2.2` | Ensure that only currently supported software is designated as authorized in the software inventory for enterprise assets. If software is unsupported, yet necessary for the fulfillment of the enterpri | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |
| `CIS-2.3` | Ensure that unauthorized software is either removed from use on enterprise assets or receives a documented exception. Review monthly, or more frequently. | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |
| `CIS-2.4` | Utilize software inventory tools, when possible, throughout the enterprise to automate the discovery and documentation of installed software. | conceito: Build And Image Inventory Generation (mechanism `ACM-SCBI-005`) |
| `CIS-2.5` | Use technical controls, such as application allowlisting, to ensure that only authorized software can execute or be accessed. Reassess bi-annually, or more frequently. | conceito: Approved Source And Registry Governance (practice `ACP-SCBI-003`) |
| `CIS-2.6` | Use technical controls to ensure that only authorized software libraries, such as specific .dll, .ocx, and .so files, are allowed to load into a system process. Block unauthorized libraries from loadi | conceito: Approved Source And Registry Governance (practice `ACP-SCBI-003`) |
| `CIS-2.7` | Use technical controls, such as digital signatures and version control, to ensure that only authorized scripts, such as specific .ps1 and .py files, are allowed to execute. Block unauthorized scripts | conceito: Approved Source And Registry Governance (practice `ACP-SCBI-003`) |

---

## OWASP DSOMM

**O que esta ES traz para este capítulo:** contribui 21 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `DSOMM-ACTIVITY-066084C6113546359CC59E75C7C5459F` | Version control Use a _version control system_ like Github, Gitlab, Bitbucket, etc to version your source code. Also known as _source control_, _revision control_, or _source code management_. Without | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `DSOMM-ACTIVITY-08F27C262C6A47FE94585E88F188085D` | Automated deployment of automated PRs Even if automated dependencies PRs are merged, they might not be deployed. This results in vulnerabilities in running artifacts stay for too long and might get ex | conceito: Release Promotion Controls (mechanism `ACM-RPR-001`) |
| `DSOMM-ACTIVITY-16E39C8F5336400188EDA552D2447531` | Reduction of the attack surface Distroless images are minimal, stripped-down base images that contain only the essential components required to run your application. They do not include package manage | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |
| `DSOMM-ACTIVITY-2858AC12017940D99ACF1B839C030473` | SBOM of components SBOM (Software Bill of Materials) is a document that lists all components, libraries, and dependencies used in a software application or container image. Creating an SBOM during the | conceito: Build And Image Inventory Generation (mechanism `ACM-SCBI-005`) |
| `DSOMM-ACTIVITY-34869EAFF2E14926B0BD28C43402F057` | Nightly build of images (base images) A base image is a pre-built image that serves as a starting point for building new images or containers. These base images usually include an operating system, ne | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |
| `DSOMM-ACTIVITY-363A3EEABAF9401088CABB8186A2989D` | .gitignore Unintended leakage of secrets, debug, or workstation specific data .gitignore files help prevent accidental commits of secrets, debug, or workstation specific data | conceito: Secret Management Systems (mechanism `ACM-SPC-001`) |
| `DSOMM-ACTIVITY-485A33837F2E4DBABB84479377070904` | Usage of a maximum lifetime for images The maximum lifetime for a Docker container refers to the duration a container should be allowed to run before it is considered outdated, stale, or insecure. The | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |
| `DSOMM-ACTIVITY-517B095749814AC0B4C70D8D1934C474` | Local development linting & style checks performed Insecure or unmaintainable code base. Integrate static code analysis tools in IDEs. | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `DSOMM-ACTIVITY-5786959D0C6F46A68E1CA32FF1A50222` | Signing of artifacts To perform a push to a GitHub repository, you must be authenticated. It's important to note that GitHub does not verify if the authenticated user's email address matches the one i | conceito: Artifact Signing And Attestation (mechanism `ACM-SCBI-004`) |
| `DSOMM-ACTIVITY-6B96E5A0CE344EA4A88F469D3B84546E` | Usage of a short maximum lifetime for images The maximum lifetime for a Docker container refers to the duration a container should be allowed to run before it is considered outdated, stale, or insecur | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |
| `DSOMM-ACTIVITY-8AE0B92C10E04602BA227524D6AED488` | Automated PRs for patches Automated PRs for patches ensure that updates for outdated or vulnerable dependencies are created and proposed without manual intervention. Tools continuously monitor for new | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |
| `DSOMM-ACTIVITY-994151396B50441B89E10AA59ACCD43D` | A patch policy is defined A patch policy defines how and when software components, images, and dependencies are updated. A patch policy ensures that all these artifacts are regularly reviewed and upda | conceito: Threat Mitigation Linkage Controls (mechanism `ACM-TMR-005`) |
| `DSOMM-ACTIVITY-9F10792761E9457485AD3F2B4BCA8665` | Signing of code Execution or usage of malicious code or data e.g. via executables, libraries or container images. Digitally signing commits helps to prevent unauthorized manipulation of source code. | conceito: Artifact Signing And Attestation (mechanism `ACM-SCBI-004`) |
| `DSOMM-ACTIVITY-A340F46B63604CB8847BA0D3483D09D3` | Building and testing of artifacts in virtual environments While building and testing artifacts, third party systems, application frameworks and 3rd party libraries are used. These might be malicious a | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `DSOMM-ACTIVITY-AC8730A2CCC0465C9550D91EDAE9D5EE` | Require status checks to pass Organizations risk introducing broken builds, quality issues, and security vulnerabilities into their codebase. Mandate passing of security related specified status check | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `DSOMM-ACTIVITY-C7D99B18C3E14D22B2E39AA9146C0B17` | Block force pushes Misuse of force push can lead to loss of work. It may overwrite remote branches without warning, potentially erasing valuable contributions from team members. This can disrupt colla | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `DSOMM-ACTIVITY-E7598AC4B0824E56B7DFE2C6B426A5E2` | Require a PR before merging Intentional or accidental alterations in critical branches like main (or master). Define source code management system policies (e.g. branch protection rules, mandatory cod | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `DSOMM-ACTIVITY-EA6F69F754A54922AC15A77FF0C16162` | Dismiss stale PR approvals Intentional or accidental alterations in critical branches like main (or master) through post-approval code additions. Implement a policy where any commits made after a pull | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `DSOMM-ACTIVITY-F2594F8F1CD645F9AF29EAF3315698EB` | Automated merge of automated PRs Automated merges of automated created PRs for outdated dependencies. Vulnerabilities in running artifacts stay for too long and might get exploited. A good practice is | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |
| `DSOMM-ACTIVITY-F3C4971E9F4D4E598ED0F0BDB6262477` | Pinning of artifacts Unauthorized manipulation of artifacts might be difficult to spot. For example, this may result in using images with malicious code. Also, intended major changes, which are automa | conceito: Artifact Signing And Attestation (mechanism `ACM-SCBI-004`) |
| `DSOMM-ACTIVITY-F6F7737F25A943178DE209BF59F29B5B` | Defined build process A *build process* includes more than just compiling your source code. It also covers: - Managing (third party) dependencies - Environment configuration - Running unit and integra | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |

---

## NIST SSDF (SP 800-218 v1.1)

**O que esta ES traz para este capítulo:** contribui 18 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `SSDF-PRACTICE-PO.3` | Use automation to reduce human effort and improve the accuracy, reproduc ibility, usability, and comprehensiveness of security practices throughout the SDLC, as well as provide a way to document and d | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `SSDF-PRACTICE-PO.5` | Ensure that all components of the environments for software development are strongly protected from internal and external threats to prevent compromises of the environments or the software being devel | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `SSDF-PRACTICE-PS.1` | Help prevent unauthorized changes to code, both inadvertent and intentional, which could circumvent or negate the intended security characteristics of the software. For code that is not intended to be | addon (medium): Modelos de Arquitetura Segura Reutilizáveis > Modelo 1 - Monólito Web com Backend Interno (Risco L1) > Ameaças mitigadas |
| `SSDF-PRACTICE-PS.2` | Help software acquirers ensure that the software they acquire is legitimate and has not been tampered with. | conceito: Artifact Signing And Attestation (mechanism `ACM-SCBI-004`) |
| `SSDF-PRACTICE-PW.3` | Moved to PW.4 | conceito: Approved Source And Registry Governance (practice `ACP-SCBI-003`) |
| `SSDF-PRACTICE-PW.4` | Lower the costs of software development, expedite software development, and decrease the likelihood of introducing additional security vulnerabilities into the softw are by reusing software modules an | conceito: Approved Source And Registry Governance (practice `ACP-SCBI-003`) |
| `SSDF-TASK-PO.3.1` | Specify which tools or tool types must or should be included in each toolchain to mitigate identified risks, as well as how the toolchain components are t o be integrated with each other. | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `SSDF-TASK-PO.3.2` | Follow recommended security practices to deploy , operate, and maintain tools and toolchains. | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `SSDF-TASK-PO.3.3` | Configure tools to generate artifacts6 of their support of secure software development practices as defined by the organization. | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `SSDF-TASK-PO.5.1` | Separate and protect each environment involved in software development. | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `SSDF-TASK-PO.5.2` | Secure and harden development endpoints (i.e., endpoints for software designers, developers, testers, builders, etc. ) to perform development -related tasks using a risk-based approach. | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `SSDF-TASK-PS.1.1` | Store all forms of code – including source code, executable code, and configuration- as-code – based on the principle of least privilege so that only authorized personnel, tools, services, etc. have a | conceito: Access Policy Enforcement (mechanism `ACM-IAT-002`) |
| `SSDF-TASK-PS.2.1` | Make software integrity verification information available to software acquirers . | conceito: Artifact Signing And Attestation (mechanism `ACM-SCBI-004`) |
| `SSDF-TASK-PW.4.1` | Acquire and maintain well-secured software components (e.g., software libraries, modules, middleware, frameworks) from commercial, open- source, and other third- party developers for use by the organi | conceito: Approved Source And Registry Governance (practice `ACP-SCBI-003`) |
| `SSDF-TASK-PW.4.2` | Create and maintain well -secured software components in -house following SDLC processes to meet common internal software development needs that cannot be better met by third-party software components | conceito: Approved Source And Registry Governance (practice `ACP-SCBI-003`) |
| `SSDF-TASK-PW.4.3` | Moved to PW.1.3 --- PAGE 22 --- NIST SP 800-218 SSDF VERSION 1.1 13 Practices Tasks Notional Implementation Examples | conceito: Threat Representation Models (mechanism `ACM-TMR-001`) |
| `SSDF-TASK-PW.4.4` | Verify that acquired commercial, open-source, and all other third-party software components comply with the requirements , as defined by the organization, throughout their life cycle s. | conceito: Approved Source And Registry Governance (practice `ACP-SCBI-003`) |
| `SSDF-TASK-PW.4.5` | Moved to PW.4.1 and PW.4.4 Create Source Code by Adhering to Secure Coding Practices (PW.5): Decrease the number of security vulnerabilities in the software, and reduce costs by minimiz ing vulnerabil | conceito: Approved Source And Registry Governance (practice `ACP-SCBI-003`) |

---

## OWASP SAMM v2.1

**O que esta ES traz para este capítulo:** contribui 15 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `SAMM-ACTIVITY-I_SB_1_A` | Define a consistent build process Limited risk of human error during build process minimizing security issues Create a formal definition of the build process so that it becomes consistent and repeatab | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `SAMM-ACTIVITY-I_SB_1_B` | Identify application dependencies Available information on known security issues in dependencies Create records with Bill of Materials of your applications and opportunistically analyze these. Keep a | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `SAMM-ACTIVITY-I_SB_2_A` | Automate the build process Efficient build process with integrated security tools Automate your build pipeline and secure the used tooling. Add security checks in the build pipeline. Automate the buil | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `SAMM-ACTIVITY-I_SB_2_B` | Review application dependencies for security Full transparency of known security issues in dependencies Evaluate used dependencies and ensure timely reaction to situations posing risk to your applicat | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `SAMM-ACTIVITY-I_SB_3_A` | Enforce a security baseline during build Assurance that you build software complying with a security baseline Define mandatory security checks in the build process and ensure that building non-complia | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `SAMM-ACTIVITY-I_SB_3_B` | Test application dependencies Handling of security issues in dependencies comparable to those in your own code Analyze used dependencies for security issues in a comparable way to your own code. Maint | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `SAMM-FUNCTION-OPERATIONS` | Operations The Operations Business Function encompasses those activities necessary to ensure confidentiality, integrity, and availability are maintained throughout the operational lifetime of an appli | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `SAMM-PRACTICE-I_DM` | I-DM Defect Management This practice focuses on managing security defects in software and their associated metrics. The Defect Management (DM) practice focuses on collecting, recording, and analyzing | conceito: Findings Workflow And Exception Governance (mechanism `ACM-TSV-004`) |
| `SAMM-PRACTICE-I_SB` | I-SB Secure Build This practice focuses on creating a consistently repeatable build process and accounting for the security of application dependencies. The Secure Build (SB) practice emphasises the i | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `SAMM-PRACTICE-I_SD` | I-SD Secure Deployment This practice focuses on increasing the security of software deployments to the production environment and the supporting secrets. One of the final stages in delivering secure s | conceito: Release Promotion Controls (mechanism `ACM-RPR-001`) |
| `SAMM-PRACTICE-LEVEL-I_SB_1` | I-SB-1 Secure Build L1 Build process is repeatable and consistent. | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `SAMM-PRACTICE-LEVEL-I_SB_2` | I-SB-2 Secure Build L2 Build process is optimized and fully integrated into the workflow. | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `SAMM-PRACTICE-LEVEL-I_SB_3` | I-SB-3 Secure Build L3 Build process helps prevent known defects from entering the production environment. | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `SAMM-STREAM-D_SR_B` | D-SR-B Supplier Security Supplier security deals with requirements that are relative to supplier organizations within the development context of the application, in particular for outsourced developme | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `SAMM-STREAM-I_SB_A` | I-SB-A Build Process A consistent build process ensures the software you are deploying is predictable and directly linked to the source code. Furthermore, you can take advantage of the software build | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |

---

## SLSA Specification v1.0 — Build Track

**O que esta ES traz para este capítulo:** contribui 14 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `SLSA-BUILD-L1` | L1 requires provenance exists for the artifact — directly maps to artifact attestation and provenance integrity. | conceito: Artifact Signing And Attestation (mechanism `ACM-SCBI-004`) |
| `SLSA-BUILD-L2` | L2 requires hosted build platform with signed provenance — maps to build execution integrity with provenance as secondary. | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `SLSA-BUILD-L3` | L3 requires hardened build platform with tamper protection — maps to build execution integrity with provenance and promotion integrity. | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `SLSA-BUILD-PLATFORM-ISOLATION` | Build platform isolates between builds to prevent external influence. Maps to build execution integrity and deterministic pipelines. | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `SLSA-BUILD-PLATFORM-PROVENANCE-GENERATION` | Build platform generates provenance with completeness and authenticity. Core provenance integrity requirement. | conceito: Artifact Signing And Attestation (mechanism `ACM-SCBI-004`) |
| `SLSA-PRINCIPLE-PREFER-ATTESTATIONS` | Prefer explicit attestations over inferences. Directly maps to artifact attestation. | conceito: Artifact Signing And Attestation (mechanism `ACM-SCBI-004`) |
| `SLSA-PRINCIPLE-TRUST-CODE` | Trust code not individuals: trace software to source code with provenance. Maps to provenance integrity + controlled sources. | conceito: Artifact Signing And Attestation (mechanism `ACM-SCBI-004`) |
| `SLSA-PRINCIPLE-TRUST-PLATFORMS` | Trust platforms principle: establish trust in build/packaging platforms, verify artifacts automatically. Directly maps to build integrity + attestation. | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `SLSA-PRODUCER-CHOOSE-BUILD-PLATFORM` | Select build platform capable of desired SLSA level. Maps to build execution integrity. | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `SLSA-PRODUCER-CONSISTENT-BUILD` | Build in consistent manner so verifiers can form expectations. Maps to deterministic build definition. | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `SLSA-PRODUCER-DISTRIBUTE-PROVENANCE` | Distribute provenance to consumers. Directly maps to provenance distribution. | conceito: Artifact Signing And Attestation (mechanism `ACM-SCBI-004`) |
| `SLSA-VERIFY-BUILD-LEVEL` | Verify SLSA Build level by comparing artifact to provenance against root of trust. Maps to provenance validation + dependency risk evaluation. | conceito: Artifact Signing And Attestation (mechanism `ACM-SCBI-004`) |
| `SLSA-VERIFY-DEPENDENCIES` | Recursively check resolvedDependencies. Maps to dependency inventory and SBOM traceability + risk evaluation. | conceito: Build And Image Inventory Generation (mechanism `ACM-SCBI-005`) |
| `SLSA-VERIFY-EXPECTATIONS` | Check provenance meets expectations for the package — policy gating against provenance evidence. | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |

---

## PCI DSS v4.0.1

**O que esta ES traz para este capítulo:** contribui 13 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `PCI-5.1.1` | All security policies and operational 5.1.1 Examine documentation and interview and maintaining the various policies and procedures | conceito: Build And Image Inventory Generation (mechanism `ACM-SCBI-005`) |
| `PCI-5.1.2` | Roles and responsibilities for performing 5.1.2.a Examine documentation to verify that assigned, networks and systems may not be | conceito: Build And Image Inventory Generation (mechanism `ACM-SCBI-005`) |
| `PCI-5.2.1` | An anti-malware solution(s) is deployed on all 5.2.1.a Examine system components to verify that newly discovered vulnerabilities in systems | conceito: Build And Image Inventory Generation (mechanism `ACM-SCBI-005`) |
| `PCI-5.2.2` | The deployed anti-malware solution(s): 5.2.2 Examine vendor documentation and of malware to prevent unauthorized access. | conceito: Build And Image Inventory Generation (mechanism `ACM-SCBI-005`) |
| `PCI-5.2.3` | Any system components that are not at risk for 5.2.3.a Examine documented policies and currently be commonly targeted or affected by | conceito: Build And Image Inventory Generation (mechanism `ACM-SCBI-005`) |
| `PCI-5.3.1` | The anti-malware solution(s) is kept current 5.3.1.a Examine anti-malware solution(s) needs to have the latest security updates, | conceito: Build And Image Inventory Generation (mechanism `ACM-SCBI-005`) |
| `PCI-5.3.2` | The anti-malware solution(s): 5.3.2.a Examine anti-malware solution(s) but currently inactive, within the environment. Some | conceito: Build And Image Inventory Generation (mechanism `ACM-SCBI-005`) |
| `PCI-5.3.3` | For removable electronic media, the anti- 5.3.3.a Examine anti-malware solution(s) entry method for malware. Attackers will often pre- | conceito: Build And Image Inventory Generation (mechanism `ACM-SCBI-005`) |
| `PCI-5.3.4` | Audit logs for the anti-malware solution(s) are 5.3.4 Examine anti-malware solution(s) malware mechanisms—for example, by confirming | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `PCI-5.3.5` | Anti-malware mechanisms cannot be disabled 5.3.5.a Examine anti-malware configurations, to always running so that malware is detected in real | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `PCI-5.4.1` | Processes and automated mechanisms are in 5.4.1 Observe implemented processes and personnel have to evaluate the veracity of a | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |
| `PCI-9.2.3` | Physical access to wireless access points, 9.2.3 Interview responsible personnel and observe to wireless components and devices, and | conceito: Build And Image Inventory Generation (mechanism `ACM-SCBI-005`) |
| `PCI-REQ-5` | Requirement 5: Protect All Systems and Networks from Malicious Software. Goal: Maintain a Vulnerability Management Program. | conceito: Build And Image Inventory Generation (mechanism `ACM-SCBI-005`) |

---

## SAFECode — Software Integrity Controls (2010)

**O que esta ES traz para este capítulo:** contribui 9 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `SCSIC-DELIVERY` | Controls for delivery phase: publishing and dissemination, malware scanning, code signing, secure delivery, transfer authenticity, hash verification | conceito: Build And Image Inventory Generation (mechanism `ACM-SCBI-005`) |
| `SCSIC-DELIVERY-SIGNING` | Products digitally marked with vendor identity; checksums and hashes for component verification; integrity verification during installation and execution | conceito: Build And Image Inventory Generation (mechanism `ACM-SCBI-005`) |
| `SCSIC-DEV-BUILD` | Automated builds, minimal human access, build scripts as code assets, service accounts traceable, build traceability to individuals | conceito: Artifact Signing And Attestation (mechanism `ACM-SCBI-004`) |
| `SCSIC-DEV-MANIFEST` | Manifest of all code assets contributing to a product, including in-house and third party components, similar to BOM in manufacturing | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `SCSIC-DEV-REPO` | All code assets in source code repositories with access control; separation of duties; change logs; SCAP compliance; branch access by least privilege | conceito: Artifact Signing And Attestation (mechanism `ACM-SCBI-004`) |
| `SCSIC-DEVELOPMENT` | Controls for development phase: people security, physical security, network security, code repository security, build environment, peer review, security testing | conceito: Artifact Signing And Attestation (mechanism `ACM-SCBI-004`) |
| `SCSIC-SOURCING` | Controls for vendor sourcing process: contractual integrity, defined expectations, ownership, vulnerability response, security training, OSS management | conceito: Approved Source And Registry Governance (practice `ACP-SCBI-003`) |
| `SCSIC-SOURCING-OSS` | Evaluate reputation and release practices of OSS communities; validate packages and distribution sites; vulnerability monitoring and patching strategy | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |
| `SCSIC-SOURCING-TRANSFER` | Authenticated endpoints, encrypted sessions, digitally signed packages with verifiable checksums/hashes | conceito: Build And Image Inventory Generation (mechanism `ACM-SCBI-005`) |

---

## OWASP ASVS v5.0.0

**O que esta ES traz para este capítulo:** contribui 8 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `ASVS-REQ-V15.2.1` | Verify that the application only contains components which have not breached the documented update and remediation time frames. | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |
| `ASVS-REQ-V15.2.2` | Verify that the application has implemented defenses against loss of availability due to functionality which is time-consuming or resource-demanding, based on the documented security decisions and str | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |
| `ASVS-REQ-V15.2.3` | Verify that the production environment only includes functionality that is required for the application to function, and does not expose extraneous functionality such as test code, sample snippets, an | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |
| `ASVS-REQ-V15.2.4` | Verify that third-party components and all of their transitive dependencies are included from the expected repository, whether internally owned or an external source, and that there is no risk of a de | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |
| `ASVS-REQ-V15.2.5` | Verify that the application implements additional protections around parts of the application which are documented as containing "dangerous functionality" or using third-party libraries considered to | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |
| `ASVS-REQ-V3.6.1` | Verify that client-side assets, such as JavaScript libraries, CSS, or web fonts, are only hosted externally (e.g., on a Content Delivery Network) if the resource is static and versioned and Subresourc | conceito: Boundary Mediation Controls (mechanism `ACM-ATB-003`) |
| `ASVS-SECTION-V3.6` | V3.6 External Resource Integrity | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `ASVS-SECTION-V9.1` | V9.1 Token source and integrity | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |

---

## SAFECode — Practical Security Stories and Tasks for Agile Development (2012)

**O que esta ES traz para este capítulo:** contribui 8 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `SCAGILE-EXP-8` | Third-party security assurance for modules and libraries | conceito: Approved Source And Registry Governance (practice `ACP-SCBI-003`) |
| `SCAGILE-EXP-9` | Security tool recommendations and effective use including customization | conceito: Artifact Signing And Attestation (mechanism `ACM-SCBI-004`) |
| `SCAGILE-OPS-11` | Perform and add to release cycle automated malware scanner on released binaries | conceito: Artifact Signing And Attestation (mechanism `ACM-SCBI-004`) |
| `SCAGILE-OPS-13` | Ensure inclusion of security patches/fixes applied in previous release(s) | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |
| `SCAGILE-OPS-3` | Use latest compiler versions as recommendation for new code | conceito: Artifact Signing And Attestation (mechanism `ACM-SCBI-004`) |
| `SCAGILE-OPS-5` | Keep track of patches/fixes to third party dependencies for new and existing code | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |
| `SCAGILE-OPS-6` | Keep track of patches/fixes to OS components for new and existing code | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |
| `SCAGILE-OPS-8` | Use appropriate security-related flags for compiler for new and existing code | conceito: Artifact Signing And Attestation (mechanism `ACM-SCBI-004`) |

---

## EU Digital Operational Resilience Act (DORA)

**O que esta ES traz para este capítulo:** contribui 2 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `DORA-ART-28` | Article 28 of Digital Operational Resilience Act (Regulation (EU) 2022/2554). See validation passes in knowledge-graph working notes for detailed analysis. | conceito: Build And Image Inventory Generation (mechanism `ACM-SCBI-005`) |
| `DORA-ART-30` | Article 30 of Digital Operational Resilience Act | conceito: Build And Image Inventory Generation (mechanism `ACM-SCBI-005`) |

---

## HIPAA Security Rule

**O que esta ES traz para este capítulo:** contribui 2 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `HIPAA-164-308b1` | Business Associate Contracts and Other Arrangements — Administrative Safeguard under HIPAA Security Rule §164.308(b)(1). | conceito: Artifact Signing And Attestation (mechanism `ACM-SCBI-004`) |
| `HIPAA-164-314a1` | Business Associate Contracts or Other Arrangements — Organizational Safeguard under HIPAA Security Rule §164.314(a)(1). | conceito: Artifact Signing And Attestation (mechanism `ACM-SCBI-004`) |

---

## OWASP MCP — Third-Party Servers v1.0

**O que esta ES traz para este capítulo:** contribui 2 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `OWASP-MCP-3P-GOVERNANCE-REGISTRY` | Trusted registry governance → controlled dependency sources | conceito: Approved Source And Registry Governance (practice `ACP-SCBI-003`) |
| `OWASP-MCP-3P-TOOL-POISONING` | Tool poisoning → dependency risk evaluation | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |

---

## OWASP MCP Top 10 (v0.1, 2025 beta)

**O que esta ES traz para este capítulo:** contribui 2 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `MCP03-2025` | Tool poisoning → dependency risk evaluation | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |
| `MCP04-2025` | Dependency tampering, signed components and provenance tracking land directly in supply-chain integrity and promotion verification semantics. | conceito: Artifact Signing And Attestation (mechanism `ACM-SCBI-004`) |

---

## PCI Secure SLC v1.1

**O que esta ES traz para este capítulo:** contribui 2 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `PCISSLC-6.1` | Process, mechanism and/or tools to protect integrity of software code including third-party components; unauthorized access detected and investigated | conceito: Artifact Signing And Attestation (mechanism `ACM-SCBI-004`) |
| `PCISSLC-6.2` | Mechanism to verify integrity of updated code during delivery; processes reasonable and appropriate; results in secure delivery | conceito: Build And Image Inventory Generation (mechanism `ACM-SCBI-005`) |

---

## SAFECode — Fundamental Practices for Secure Software Development (2018)

**O que esta ES traz para este capítulo:** contribui 2 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `SCFPSSD-COMPILER` | Current compiler/toolchain versions with security-enhancing compiler options enabled | conceito: Artifact Signing And Attestation (mechanism `ACM-SCBI-004`) |
| `SCFPSSD-THIRD-PARTY` | Risk management for third-party and open source components including monitoring vulnerabilities | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |

---

## MITRE CWE — Software Development View (v4.19.1)

**O que esta ES traz para este capítulo:** contribui 1 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `CWE-1104` | The product relies on third-party components that are not actively supported or maintained by the original developer or a trusted proxy for the original developer. | conceito: Approved Source And Registry Governance (practice `ACP-SCBI-003`) |

---

## EU Cyber Resilience Act (CRA)

**O que esta ES traz para este capítulo:** contribui 1 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `CRA-ART-13` | Article 13 of Cyber Resilience Act (Regulation (EU) 2024/2847). See validation passes in knowledge-graph working notes for detailed analysis. | conceito: Build And Image Inventory Generation (mechanism `ACM-SCBI-005`) |

---


<!-- WAVE-NOTE: **Nota Wave 4 ACO-SCBI:** esta leitura funciona como **âncora bounded** de `ACO-SCBI` para os rows autorizados de dependency verification, update-channel trust e traceability fits já retidos em `05`. A leitura permanece **dual-anchor** com o Cap. `04`, mantém o Cap. `07` e `11` apenas como diversificação operacional já evidenciada, mantém o Cap. `14` apenas como suporte governativo `SR-*`, mantém o Cap. `02` apenas como scaffold de rastreabilidade, não reabre Cap. `08` ou `09`, não promove `SP800-53-SA-20`, mantém `slsa_spec_v1_0_build_track` como família de confirmação mais limpa e não fabrica rows `pci_dss_v4_0_1` fora da evidência congelada. -->
