# 25. Rastreabilidade — Dependências, SBOM & SCA

## Sumário

Este capítulo trata de **integridade da supply chain de software** —
proveniência, dependências verificadas, SBOM, controlo de origem,
assinatura e verification semantics. As fontes externas seguintes
contribuem para esta área:

- **NIST SP 800-53 Rev. 5** — 47 referência(s)
- **CIS Controls v8.1.2** — 29 referência(s)
- **OWASP DSOMM** — 27 referência(s)
- **MITRE ATLAS — Adversarial Threat Landscape for AI Systems** — 19 referência(s)
- **MITRE CAPEC v3.9** — 11 referência(s)
- **OWASP SAMM v2.1** — 10 referência(s)
- **NIST SSDF (SP 800-218 v1.1)** — 9 referência(s)
- **PCI DSS v4.0.1** — 8 referência(s)
- **SLSA Specification v1.0 — Build Track** — 7 referência(s)
- **MITRE CWE — Software Development View (v4.19.1)** — 5 referência(s)
- **OWASP ASVS v5.0.0** — 4 referência(s)
- **SAFECode — Software Integrity Controls (2010)** — 4 referência(s)
- **NIST AI RMF 1.0** — 3 referência(s)
- **PCI Secure SLC v1.1** — 3 referência(s)
- **NIST AI 100-2 e2025 — Adversarial Machine Learning Taxonomy** — 2 referência(s)
- **SAFECode — Practical Security Stories and Tasks for Agile Development (2012)** — 2 referência(s)
- **EU Cyber Resilience Act (CRA)** — 1 referência(s)
- **EU Digital Operational Resilience Act (DORA)** — 1 referência(s)
- **OWASP LLM Top 10 (2025)** — 1 referência(s)
- **OWASP MCP — Secure Server Development v1.0** — 1 referência(s)
- **OWASP MCP — Third-Party Servers v1.0** — 1 referência(s)
- **OWASP MCP Top 10 (v0.1, 2025 beta)** — 1 referência(s)
- **SAFECode — Fundamental Practices for Secure Software Development (2018)** — 1 referência(s)

---

## NIST SP 800-53 Rev. 5

**O que esta ES traz para este capítulo:** contribui 47 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `SP800-53-AC-13` | Supervision and Review — Access Control | conceito: Access Abuse Monitoring And Audit Trail (practice `ACP-IAT-006`) |
| `SP800-53-AT-1` | Policy and Procedures. Develop, document, and disseminate to [organization-defined personnel or roles]: awareness and training policy that: Addresses purpose, scope, roles, responsibilities, managemen | conceito: Identidade, autenticação e gestão de sessões (slice `ACO-IAT`) |
| `SP800-53-AU-10.5` | Digital Signatures | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `SP800-53-CA-3.1` | Unclassified National Security System Connections | conceito: Trust Boundary And Integration Review (practice `ACP-ITS-001`) |
| `SP800-53-CA-3.2` | Classified National Security System Connections | conceito: Trust Boundary And Integration Review (practice `ACP-ITS-001`) |
| `SP800-53-CA-3.3` | Unclassified Non-national Security System Connections | conceito: Trust Boundary And Integration Review (practice `ACP-ITS-001`) |
| `SP800-53-CA-5.1` | Automation Support for Accuracy and Currency. Ensure the accuracy, currency, and availability of the plan of action and milestones for the system using [automated mechanisms]. | conceito: Findings Triage, SLA And Retest Closure (practice `ACP-TSV-003`) |
| `SP800-53-CM-14` | Signed Components. Prevent the installation of [organization-defined software and firmware components] without verification that the component has been digitally signed using a certificate that is rec | conceito: Artifact Signature And Provenance Validation (practice `ACP-SCBI-006`) |
| `SP800-53-CM-8.1` | Updates During Installation and Removal. Update the inventory of system components as part of component installations, removals, and system updates. | conceito: Build-Linked SBOM Generation (practice `ACP-SCBI-001`) |
| `SP800-53-CM-8.3` | Automated Unauthorized Component Detection. Detect the presence of unauthorized hardware, software, and firmware components within the system using [organization-defined automated mechanisms] [frequen | conceito: Build-Linked SBOM Generation (practice `ACP-SCBI-001`) |
| `SP800-53-CM-8.4` | Accountability Information. Include in the system component inventory information, a means for identifying by , individuals responsible and accountable for administering those components. | conceito: Build-Linked SBOM Generation (practice `ACP-SCBI-001`) |
| `SP800-53-IA-9.2` | Transmission of Decisions | conceito: Machine Identity And Mutual Authentication Discipline (practice `ACP-ITS-002`) |
| `SP800-53-MA-3.2` | Inspect Media. Check media containing diagnostic and test programs for malicious code before the media are used in the system. | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `SP800-53-MP-1` | Policy and Procedures. Develop, document, and disseminate to [organization-defined personnel or roles]: media protection policy that: Addresses purpose, scope, roles, responsibilities, management comm | conceito: Identidade, autenticação e gestão de sessões (slice `ACO-IAT`) |
| `SP800-53-MP-6.1` | Review, Approve, Track, Document | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `SP800-53-MP-8` | Media Downgrading. Establish [system media downgrading process] that includes employing downgrading mechanisms with strength and integrity commensurate with the security category or classification of | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `SP800-53-PE-15.1` | Automation Support. Detect the presence of water near the system and alert [personnel or roles] using [automated mechanisms]. | conceito: Logging de eventos de segurança e audit trail (slice `ACO-SLG`) |
| `SP800-53-PE-6.2` | Automated Intrusion Recognition and Responses. Recognize [classes or types of intrusions] and initiate [response actions] using [automated mechanisms]. | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `SP800-53-PL-1` | Policy and Procedures. Develop, document, and disseminate to [organization-defined personnel or roles]: planning policy that: Addresses purpose, scope, roles, responsibilities, management commitment, | conceito: Identidade, autenticação e gestão de sessões (slice `ACO-IAT`) |
| `SP800-53-PM-16.1` | Automated Means for Sharing Threat Intelligence. Employ automated mechanisms to maximize the effectiveness of sharing threat intelligence information. | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `SP800-53-PM-30.1` | Identify, prioritize | conceito: Logging de eventos de segurança e audit trail (slice `ACO-SLG`) |
| `SP800-53-PM-5` | System Inventory. Develop and update [frequency] an inventory of organizational systems. | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `SP800-53-PS-4.2` | Automated Actions. Use [automated mechanisms] to. | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `SP800-53-PS-8` | Personnel Sanctions. Employ a formal sanctions process for individuals failing to comply with established information security and privacy policies and procedures; and Notify [personnel or roles] with | conceito: Gestão de segredos, configuração protegida e identidades operacionais (slice `ACO-SPC`) |
| `SP800-53-RA-5.2` | Update Vulnerabilities to Be Scanned. Update the system vulnerabilities to be scanned. | conceito: Staged Dynamic Testing And Gate Enforcement (practice `ACP-TSV-005`) |
| `SP800-53-SA-1` | Policy and Procedures. Develop, document, and disseminate to [organization-defined personnel or roles]: system and services acquisition policy that: Addresses purpose, scope, roles, responsibilities, | conceito: DFD And Trust-Boundary Grounding (practice `ACP-TMR-002`) |
| `SP800-53-SA-10.1` | Software and Firmware Integrity Verification. Require the developer of the system, system component, or system service to enable integrity verification of software and firmware components. | conceito: Pipeline Definition As Reviewed Code (practice `ACP-SCBI-004`) |
| `SP800-53-SA-10.3` | Hardware Integrity Verification. Require the developer of the system, system component, or system service to enable integrity verification of hardware components. | conceito: Pipeline Definition As Reviewed Code (practice `ACP-SCBI-004`) |
| `SP800-53-SA-11.9` | Interactive Application Security Testing. Require the developer of the system, system component, or system service to employ interactive application security testing tools to identify flaws and docume | conceito: Governed Static Analysis Execution (practice `ACP-TSV-002`) |
| `SP800-53-SA-12` | Supply Chain Protection | conceito: Automated Dependency And Image Risk Gating (practice `ACP-SCBI-002`) |
| `SP800-53-SA-12.3` | Trusted Shipping and Warehousing | conceito: Automated Dependency And Image Risk Gating (practice `ACP-SCBI-002`) |
| `SP800-53-SA-15.2` | Security and Privacy Tracking Tools. Require the developer of the system, system component, or system service to select and employ security and privacy tracking tools for use during the development pr | conceito: Pipeline Definition As Reviewed Code (practice `ACP-SCBI-004`) |
| `SP800-53-SA-18.2` | Inspection of Systems or Components | conceito: Artifact Signature And Provenance Validation (practice `ACP-SCBI-006`) |
| `SP800-53-SA-19` | Component Authenticity | conceito: Artifact Signature And Provenance Validation (practice `ACP-SCBI-006`) |
| `SP800-53-SA-4.4` | Assignment of Components to Systems | conceito: Trust Boundary And Integration Review (practice `ACP-ITS-001`) |
| `SP800-53-SC-20` | Secure Name/Address Resolution Service (Authoritative Source). Provide additional data origin authentication and integrity verification artifacts along with the authoritative name resolution data the | conceito: Message Integrity And Authorized Peer Validation (practice `ACP-ITS-004`) |
| `SP800-53-SI-18.1` | Automation Support. Correct or delete personally identifiable information that is inaccurate or outdated, incorrectly determined regarding impact, or incorrectly de-identified using [automated mechani | conceito: Operational Identity Binding And OIDC Use (practice `ACP-SPC-004`) |
| `SP800-53-SI-4.24` | Indicators of Compromise. Discover, collect, and distribute to [personnel or roles] , indicators of compromise provided by [sources]. | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `SP800-53-SI-4.3` | Automated Tool and Mechanism Integration. Employ automated tools and mechanisms to integrate intrusion detection tools and mechanisms into access control and flow control mechanisms. | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `SP800-53-SI-5.1` | Automated Alerts and Advisories. Broadcast security alert and advisory information throughout the organization using [automated mechanisms]. | conceito: Threat Traceability Into Requirements And Validation (practice `ACP-TMR-005`) |
| `SP800-53-SI-7.4` | Tamper-evident Packaging | conceito: Artifact Signature And Provenance Validation (practice `ACP-SCBI-006`) |
| `SP800-53-SR-11` | implement anti-counterfeit policy | conceito: Artifact Signature And Provenance Validation (practice `ACP-SCBI-006`) |
| `SP800-53-SR-11.3` | Anti-counterfeit Scanning. Scan for counterfeit system components [frequency]. | conceito: Artifact Signature And Provenance Validation (practice `ACP-SCBI-006`) |
| `SP800-53-SR-3.1` | Diverse Supply Base. Employ a diverse set of sources for the following system components and services: [organization-defined system components and services]. | conceito: Approved Source And Registry Governance (practice `ACP-SCBI-003`) |
| `SP800-53-SR-4` | Document, monitor | conceito: Artifact Signature And Provenance Validation (practice `ACP-SCBI-006`) |
| `SP800-53-SR-4.4` | Supply Chain Integrity — Pedigree. Employ [controls] and conduct [analysis method] to ensure the integrity of the system and system components by validating the internal composition and provenance of | conceito: Artifact Signature And Provenance Validation (practice `ACP-SCBI-006`) |
| `SP800-53-SR-9` | Tamper Resistance and Detection. Implement a tamper protection program for the system, system component, or system service. | conceito: Artifact Signature And Provenance Validation (practice `ACP-SCBI-006`) |

---

## CIS Controls v8.1.2

**O que esta ES traz para este capítulo:** contribui 29 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `CIS-1.1` | Establish | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `CIS-10` | Malware Defenses. Prevent or control the installation, spread, and execution of malicious applications, code, or scripts on enterprise assets. | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `CIS-10.1` | Deploy and Maintain Anti-Malware Software. Deploy and maintain anti-malware software on all enterprise assets. | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `CIS-10.2` | Configure Automatic Anti-Malware Signature Updates. Configure automatic updates for anti-malware signature files on all enterprise assets. | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `CIS-10.4` | Configure Automatic Anti-Malware Scanning of Removable Media. Configure anti-malware software to automatically scan removable media. | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |
| `CIS-13.2` | Deploy a Host-Based Intrusion Detection Solution. Deploy a host-based intrusion detection solution on enterprise assets, where appropriate and/or supported. | conceito: Logging de eventos de segurança e audit trail (slice `ACO-SLG`) |
| `CIS-13.3` | Deploy a Network Intrusion Detection Solution. Deploy a network intrusion detection solution on enterprise assets, where appropriate. Example implementations include the use of a Network Intrusion Det | conceito: Logging de eventos de segurança e audit trail (slice `ACO-SLG`) |
| `CIS-13.5` | Manage Access Control for Remote Assets. Manage access control for assets remotely connecting to enterprise resources. Determine amount of access to enterprise resources based on: up-to-date anti-malw | conceito: Access Policy Enforcement (mechanism `ACM-IAT-002`) |
| `CIS-13.7` | Deploy a Host-Based Intrusion Prevention Solution. Deploy a host-based intrusion prevention solution on enterprise assets, where appropriate and/or supported. Example implementations include use of an | conceito: Logging de eventos de segurança e audit trail (slice `ACO-SLG`) |
| `CIS-13.8` | Deploy a Network Intrusion Prevention Solution. Deploy a network intrusion prevention solution, where appropriate. Example implementations include the use of a Network Intrusion Prevention System (NIP | conceito: Logging de eventos de segurança e audit trail (slice `ACO-SLG`) |
| `CIS-14.7` | Train Workforce on How to Identify and Report if Their Enterprise Assets are Missing Security Updates. Train workforce to understand how to verify and report out-of-date software patches or any failur | conceito: Threat Mitigation Linkage Controls (mechanism `ACM-TMR-005`) |
| `CIS-15.1` | Establish | conceito: Integração e segurança service-to-service (slice `ACO-ITS`) |
| `CIS-16.13` | Conduct Application Penetration Testing. Conduct application penetration testing. For critical applications, authenticated penetration testing is better suited to finding business logic vulnerabilitie | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `CIS-16.3` | Perform Root Cause Analysis on Security Vulnerabilities. Perform root cause analysis on security vulnerabilities. When reviewing vulnerabilities, root cause analysis is the task of evaluating underlyi | conceito: Threat Model Versioning Controls (mechanism `ACM-TMR-003`) |
| `CIS-16.4` | Establish | conceito: Build And Image Inventory Generation (mechanism `ACM-SCBI-005`) |
| `CIS-16.5` | Use Up-to-Date and Trusted Third-Party Software Components. Use up-to-date and trusted third-party software components. When possible, choose established and proven frameworks and libraries that provi | conceito: Approved Source And Registry Governance (practice `ACP-SCBI-003`) |
| `CIS-18.2` | Perform Periodic External Penetration Tests. Perform periodic external penetration tests based on program requirements, no less than annually. External penetration testing must include enterprise and | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `CIS-18.5` | Perform Periodic Internal Penetration Tests. Perform periodic internal penetration tests based on program requirements, no less than annually. The testing may be clear box or opaque box. | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `CIS-2` | Inventory and Control of Software Assets. Actively manage (inventory, track, and correct) all software (operating systems and applications) on the network so that only authorized software is installed | conceito: Build And Image Inventory Generation (mechanism `ACM-SCBI-005`) |
| `CIS-2.1` | Establish | conceito: Build And Image Inventory Generation (mechanism `ACM-SCBI-005`) |
| `CIS-2.2` | Ensure Authorized Software is Currently Supported | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |
| `CIS-2.4` | Utilize Automated Software Inventory Tools. Utilize software inventory tools, when possible, throughout the enterprise to automate the discovery and documentation of installed software. | conceito: Build And Image Inventory Generation (mechanism `ACM-SCBI-005`) |
| `CIS-2.5` | Allowlist Authorized Software. Use technical controls, such as application allowlisting, to ensure that only authorized software can execute or be accessed. Reassess bi-annually, or more frequently. | conceito: Approved Source And Registry Governance (practice `ACP-SCBI-003`) |
| `CIS-4.4` | Implement and Manage a Firewall on Servers. Implement and manage a firewall on servers, where supported. Example implementations include a virtual firewall, operating system firewall, or a third-party | conceito: Release promotion, rollout controlado e readiness para rollback (slice `ACO-RPR`) |
| `CIS-7.3` | Perform Automated Operating System Patch Management. Perform operating system updates on enterprise assets through automated patch management on a monthly, or more frequent, basis. | conceito: Threat modeling, gestão de risco e rastreabilidade de mitigações (slice `ACO-TMR`) |
| `CIS-7.4` | Perform Automated Application Patch Management. Perform application updates on enterprise assets through automated patch management on a monthly, or more frequent, basis. | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |
| `CIS-7.5` | Perform Automated Vulnerability Scans of Internal Enterprise Assets. Perform automated vulnerability scans of internal enterprise assets on a quarterly, or more frequent, basis. Conduct both authentic | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `CIS-7.6` | Perform Automated Vulnerability Scans of Externally-Exposed Enterprise Assets. Perform automated vulnerability scans of externally-exposed enterprise assets. Perform scans on a monthly, or more freque | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `CIS-9.7` | Deploy and Maintain Email Server Anti-Malware Protections. Deploy and maintain email server anti-malware protections, such as attachment scanning and/or sandboxing. | conceito: Validação de input, parsing seguro e tratamento controlado de erros (slice `ACO-IVF`) |

---

## OWASP DSOMM

**O que esta ES traz para este capítulo:** contribui 27 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `DSOMM-ACTIVITY-08F27C262C6A47FE94585E88F188085D` | Automated deployment of automated PRs. Automated deployment of automated PRs Even if automated dependencies PRs are merged, they might not be deployed. This results in vulnerabilities in running artif | conceito: Release Promotion Controls (mechanism `ACM-RPR-001`) |
| `DSOMM-ACTIVITY-0DE465A655A74343AF79948BB5FF10BA` | Evaluation of the trust of used components. Evaluation of the trust of used components Application and system components like Open Source libraries or images can have implementation flaws or deploymen | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |
| `DSOMM-ACTIVITY-13367D8FE37F4197A6109FFCA4FDE261` | Test of infrastructure components for known vulnerabilities. Test of infrastructure components for known vulnerabilities Infrastructure components might have vulnerabilities. Test for known vulnerabil | conceito: Threat Mitigation Linkage Controls (mechanism `ACM-TMR-005`) |
| `DSOMM-ACTIVITY-13E9757E58E24277BC0FEADC674891E6` | Inventory of production dependencies. Inventory of production dependencies Delayed identification of components and their vulnerabilities in production. In case a vulnerability is known by the organiz | conceito: Build And Image Inventory Generation (mechanism `ACM-SCBI-005`) |
| `DSOMM-ACTIVITY-16E39C8F5336400188EDA552D2447531` | Reduction of the attack surface. Reduction of the attack surface Distroless images are minimal, stripped-down base images that contain only the essential components required to run your application. T | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |
| `DSOMM-ACTIVITY-26E1C6D556324EC780D2E564B98732AD` | Software Composition Analysis. Software Composition Analysis Subscribing to Github projects and reading release notes might help. Software Composition Analysis for infrastructure might help, but is of | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |
| `DSOMM-ACTIVITY-2858AC12017940D99ACF1B839C030473` | SBOM of components. SBOM of components SBOM (Software Bill of Materials) is a document that lists all components, libraries, and dependencies used in a software application or container image. Creatin | conceito: Build And Image Inventory Generation (mechanism `ACM-SCBI-005`) |
| `DSOMM-ACTIVITY-2A44B708734F4463B0CB86DC46344B2F` | Inventory of production components. Inventory of production components An inventory of production components is a complete, up-to-date list of all applications running in production. This enables effe | conceito: Build And Image Inventory Generation (mechanism `ACM-SCBI-005`) |
| `DSOMM-ACTIVITY-34869EAFF2E14926B0BD28C43402F057` | Nightly build of images (base images). Nightly build of images (base images) A base image is a pre-built image that serves as a starting point for building new images or containers. These base images | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |
| `DSOMM-ACTIVITY-485A33837F2E4DBABB84479377070904` | Usage of a maximum lifetime for images. Usage of a maximum lifetime for images The maximum lifetime for a Docker container refers to the duration a container should be allowed to run before it is cons | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |
| `DSOMM-ACTIVITY-535F301AE8E84EDAAD77A08B035C92DE` | Simple mob hacking. Simple mob hacking ### Guidelines for your simple mob hacking session - All exploits happen via the user interface. - No need for security/hacking tools. - No need for deep technic | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `DSOMM-ACTIVITY-6B96E5A0CE344EA4A88F469D3B84546E` | Usage of a short maximum lifetime for images. Usage of a short maximum lifetime for images The maximum lifetime for a Docker container refers to the duration a container should be allowed to run befor | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |
| `DSOMM-ACTIVITY-6E180ABC7C984265B4E9852CB91B067B` | Local development security checks performed. Local development security checks performed Creating and developing code contains code smells and quality issues. Integration of quality and linting plugin | conceito: Secret Management Systems (mechanism `ACM-SPC-001`) |
| `DSOMM-ACTIVITY-74938A3F126949B99D0FC43A79A1985A` | Defined deployment process. Defined deployment process A *defined deployment process* is a documented and standardized procedure for releasing software into production, ensuring consistency and reduci | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `DSOMM-ACTIVITY-7DE0AE33653845CD8222A1475647BA58` | Correlate known vulnerabilities in infrastructure with new image versions. Correlate known vulnerabilities in infrastructure with new image versions TODO. TODO | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |
| `DSOMM-ACTIVITY-830570280B774D2E813540969768AE88` | Inventory of production artifacts. Inventory of production artifacts In case a vulnerability of severity high or critical exists, it needs to be known where an artifacts (e.g. container image) with th | conceito: Build And Image Inventory Generation (mechanism `ACM-SCBI-005`) |
| `DSOMM-ACTIVITY-837F8F90ADC24E6B9EBB60C2EE29494D` | Test for malware. Test for malware Third party might include malware. Ether due to the maintainer (e.g. typo squatting of an image name and using the wrong image) or by an attacker on behalf of the ma | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |
| `DSOMM-ACTIVITY-8AE0B92C10E04602BA227524D6AED488` | Automated PRs for patches. Automated PRs for patches Automated PRs for patches ensure that updates for outdated or vulnerable dependencies are created and proposed without manual intervention. Tools c | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |
| `DSOMM-ACTIVITY-994151396B50441B89E10AA59ACCD43D` | A patch policy is defined. A patch policy is defined A patch policy defines how and when software components, images, and dependencies are updated. A patch policy ensures that all these artifacts are | conceito: Threat Mitigation Linkage Controls (mechanism `ACM-TMR-005`) |
| `DSOMM-ACTIVITY-9F10792761E9457485AD3F2B4BCA8665` | Signing of code. Signing of code Execution or usage of malicious code or data e.g. via executables, libraries or container images. Digitally signing commits helps to prevent unauthorized manipulation | conceito: Artifact Signing And Attestation (mechanism `ACM-SCBI-004`) |
| `DSOMM-ACTIVITY-A854B48D83BD4F8D8621A0BDD470837F` | Same artifact for environments. Same artifact for environments Building of an artifact for different environments means that an untested artifact might reach the production environment. Building an ar | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `DSOMM-ACTIVITY-A86C1FBC28FD461089A3A7F73ACFE45F` | Containers are running as non-root. Containers are running as non-root There are various reasons to run a container as non-root. Samples are listed: ## Container Escape Vectors - Root privileges signi | conceito: Trust-Boundary And DFD Modeling (mechanism `ACM-ATB-002`) |
| `DSOMM-ACTIVITY-CB6321AA0FBF49969E0805AB26EF4C1E` | Test for new image version. Test for new image version When a new version of an image is available, it might fix security vulnerabilities. Check for new images of containers in production. | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |
| `DSOMM-ACTIVITY-D918CD44A97243E9A974EFF3F4A5DCFE` | Software Composition Analysis (server side). Software Composition Analysis (server side) Use a tool like trivy and concentrate on application related vulnerabilities. At this stage, ignore vulnerabili | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |
| `DSOMM-ACTIVITY-DDFE7C3CB7A44CBA9041B044D4A34E5B` | Test for image lifetime. Test for image lifetime Old container images in production indicate that patch management is not performed and therefore vulnerabilities might exists. Check the image age of c | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |
| `DSOMM-ACTIVITY-F3C4971E9F4D4E598ED0F0BDB6262477` | Pinning of artifacts. Pinning of artifacts Unauthorized manipulation of artifacts might be difficult to spot. For example, this may result in using images with malicious code. Also, intended major cha | conceito: Artifact Signing And Attestation (mechanism `ACM-SCBI-004`) |
| `DSOMM-ACTIVITY-F6F7737F25A943178DE209BF59F29B5B` | Defined build process. Defined build process A *build process* includes more than just compiling your source code. It also covers: - Managing (third party) dependencies - Environment configuration - R | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |

---

## MITRE ATLAS — Adversarial Threat Landscape for AI Systems

**O que esta ES traz para este capítulo:** contribui 19 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `AML.CS0006` | ClearviewAI Misconfiguration. Clearview AI makes a facial recognition tool that searches publicly available photos for matches. This tool has been used for investigative purposes by law enforcement a | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `AML.CS0028` | AI Model Tampering via Supply Chain Attack. Researchers at Trend Micro, Inc. used service indexing portals and web searching tools to identify over 8,000 misconfigured private container registries exp | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `AML.CS0032` | Attempted Evasion of ML Phishing Webpage Detection System. Adversaries create phishing websites that appear visually similar to legitimate sites. These sites are designed to trick users into entering | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `AML.M0014` | Verify AI Artifacts. Verify the cryptographic checksum of all AI artifacts to verify that the file was not modified by an attacker. | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `AML.M0023` | AI Bill of Materials. An AI Bill of Materials (AI BOM) contains a full listing of artifacts and resources that were used in building the AI. The AI BOM can help mitigate supply chain risks and enable | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `AML.M0029` | Human In-the-Loop for AI Agent Actions. Systems should require the user or another human stakeholder to approve AI agent actions before the agent takes them. The human approver may be technical staff | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `AML.T0002` | Acquire Public AI Artifacts. Adversaries may search public sources, including cloud storage, public-facing services, and software or data repositories, to identify AI artifacts. These AI artifacts may | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `AML.T0008` | Acquire Infrastructure. Adversaries may buy, lease, or rent infrastructure for use throughout their operation. A wide variety of infrastructure exists for hosting and orchestrating adversary operation | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `AML.T0010.004` | Container Registry. An adversary may compromise a victim's container registry by pushing a manipulated container image and overwriting an existing container name and/or tag. Users of the container reg | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `AML.T0016.001` | Software Tools. Adversaries may search for and obtain software tools to support their operations. Software designed for legitimate use may be repurposed by an adversary for malicious intent. An advers | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `AML.T0035` | AI Artifact Collection. Adversaries may collect AI artifacts for [Exfiltration](/tactics/AML.TA0010) or for use in [AI Attack Staging](/tactics/AML.TA0001). AI artifacts include models and datasets as | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `AML.T0036` | Data from Information Repositories. Adversaries may leverage information repositories to mine valuable information. Information repositories are tools that allow for storage of information, typically | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `AML.T0060` | Publish Hallucinated Entities. Adversaries may create an entity they control, such as a software package, website, or email address to a source hallucinated by an LLM. The hallucinations may take the | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `AML.T0061` | LLM Prompt Self-Replication. An adversary may use a carefully crafted [LLM Prompt Injection](/techniques/AML.T0051) designed to cause the LLM to replicate the prompt as part of its output. This allows | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `AML.T0088` | Generate Deepfakes. Adversaries may use generative artificial intelligence (GenAI) to create synthetic media (i.e. imagery, video, audio, and text) that appear authentic. These "[deepfakes]( https://e | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `AML.T0089` | Process Discovery. Adversaries may attempt to get information about processes running on a system. Once obtained, this information could be used to gain an understanding of common AI-related software/ | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `AML.T0102` | Generate Malicious Commands. Adversaries may use large language models (LLMs) to dynamically generate malicious commands from natural language. Dynamically generated commands may be harder detect as t | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `AML.T0104` | Publish Poisoned AI Agent Tool. Adversaries may create and publish poisoned AI agent tools. Poisoned tools may contain an [LLM Prompt Injection](/techniques/AML.T0051), which can lead to a variety of | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `AML.TA0009` | Collection. The adversary is trying to gather AI artifacts and other related information relevant to their goal. Collection consists of techniques adversaries may use to gather information and the so | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |

---

## MITRE CAPEC v3.9

**O que esta ES traz para este capítulo:** contribui 11 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `CAPEC-206` | Signing Malicious Code. Signing Malicious Code. The adversary extracts credentials used for code signing from a production environment and then uses these credentials to sign malicious content with th | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `CAPEC-442` | Infected Software. Infected Software. An adversary adds malicious logic, often in the form of a computer virus, to otherwise benign software. This logic is often hidden from the user of the software a | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `CAPEC-459` | Creating a Rogue Certification Authority Certificate. Creating a Rogue Certification Authority Certificate. An adversary exploits a weakness resulting from using a hashing algorithm with weak collisio | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `CAPEC-473` | Signature Spoof. Signature Spoof. An attacker generates a message or datablock that causes the recipient to believe that the message or datablock was generated and cryptographically signed by an autho | conceito: Authentication And Federation Protocols (mechanism `ACM-IAT-001`) |
| `CAPEC-476` | Signature Spoofing by Misrepresentation. Signature Spoofing by Misrepresentation. An attacker exploits a weakness in the parsing or display code of the recipient software to generate a data blob conta | conceito: Authentication And Federation Protocols (mechanism `ACM-IAT-001`) |
| `CAPEC-477` | Signature Spoofing by Mixing Signed and Unsigned Content. Signature Spoofing by Mixing Signed and Unsigned Content. An attacker exploits the underlying complexity of a data structure that allows for b | conceito: Authentication And Federation Protocols (mechanism `ACM-IAT-001`) |
| `CAPEC-529` | Malware-Directed Internal Reconnaissance. Malware-Directed Internal Reconnaissance. Adversary uses malware or a similarly controlled application installed inside an organizational perimeter to gather | conceito: Secret Management Systems (mechanism `ACM-SPC-001`) |
| `CAPEC-549` | Local Execution of Code. Local Execution of Code. An adversary installs and executes malicious code on the target system in an effort to achieve a negative technical impact. Examples include rootkits, | conceito: Code Review For Input And Error Discipline (mechanism `ACM-IVF-001`) |
| `CAPEC-642` | Replace Binaries. Replace Binaries. Adversaries know that certain binaries will be regularly executed as part of normal processing. If these binaries are not protected with the appropriate file system | conceito: Access Policy Enforcement (mechanism `ACM-IAT-002`) |
| `CAPEC-657` | Malicious Automated Software Update via Spoofing. Malicious Automated Software Update via Spoofing. An attackers uses identify or content spoofing to trick a client into performing an automated softwa | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `CAPEC-677` | update. | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |

---

## OWASP SAMM v2.1

**O que esta ES traz para este capítulo:** contribui 10 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `SAMM-ACTIVITY-D_SA_1_B` | Identify tools and technologies. Identify tools and technologies. People often take the path of least resistance in developing, deploying or operating a software solution. New technologies are often i | conceito: Versioned Diagrams And ADR Records (mechanism `ACM-ATB-001`) |
| `SAMM-ACTIVITY-D_SR_3_B` | Align security methodology with suppliers. Align security methodology with suppliers. The best way to minimize the risk of issues in software is to align maximally and integrate closely between the di | conceito: Threat Mitigation Linkage Controls (mechanism `ACM-TMR-005`) |
| `SAMM-ACTIVITY-I_SB_1_A` | Define a consistent build process | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `SAMM-ACTIVITY-I_SB_1_B` | Identify application dependencies. Identify application dependencies. Keep a record of all dependencies used throughout the target production environment. This is sometimes referred to as a Bill of Ma | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `SAMM-ACTIVITY-I_SB_2_A` | Automate the build process. Automate the build process. Automate the build process so that builds can be executed consistently anytime. The build process shouldn't typically require any intervention, | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `SAMM-ACTIVITY-I_SB_3_A` | Enforce a security baseline during build | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `SAMM-ACTIVITY-I_SD_3_A` | Verify the integrity of deployment artifacts. Verify the integrity of deployment artifacts. Take advantage of binaries being signed at the build time and include automatic verification of the integrit | conceito: Release Promotion Controls (mechanism `ACM-RPR-001`) |
| `SAMM-ACTIVITY-O_EM_2_B` | Ensure processes include regular schedules for applying vendor updates, aligned with vendor update calendars (e.g., Microsoft Patch Tuesday) | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |
| `SAMM-ACTIVITY-O_EM_3_B` | Enforce timely patch management | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |
| `SAMM-ACTIVITY-V_ST_1_A` | Perform automated security testing. Perform automated security testing. Use automated static and dynamic security test tools for software, resulting in more efficient security testing and higher quali | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |

---

## NIST SSDF (SP 800-218 v1.1)

**O que esta ES traz para este capítulo:** contribui 9 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `SSDF-PRACTICE-PW.6` | Configure the Compilation, Interpreter, and Build Processes to Improve Executable Security. Decrease the number of security vulnerabilities in the software and reduce costs by eliminating vulnerabilit | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `SSDF-PRACTICE-PW.8` | Test Executable Code to Identify Vulnerabilities and Verify Compliance with Security Requirements. Help identify vulnerabilities so that they can be corrected before the software is released in order | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `SSDF-TASK-PO.1.3` | Communicate requirements to all third parties who will provide commercial software components to the organization for reuse by the organization’s own software. [Formerly PW.3.1] | conceito: Compliance Monitoring And Regulatory Change Feeds (mechanism `ACM-TMR-008`) |
| `SSDF-TASK-PO.5.2` | Secure and harden development endpoints (i.e., endpoints for software designers, developers, testers, builders, etc. ) to perform development -related tasks using a risk-based approach. | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `SSDF-TASK-PS.2.1` | Make software integrity verification information available to software acquirers . | conceito: Artifact Signing And Attestation (mechanism `ACM-SCBI-004`) |
| `SSDF-TASK-PW.2.1` | Have | conceito: Architecture Review Gates (mechanism `ACM-ATB-004`) |
| `SSDF-TASK-PW.4.1` | Acquire and maintain well-secured software components (e.g., software libraries, modules, middleware, frameworks) from commercial, open- source, and other third- party developers for use by the organi | conceito: Approved Source And Registry Governance (practice `ACP-SCBI-003`) |
| `SSDF-TASK-PW.6.1` | Use compiler , interpreter, and build tools that offer features to improve executable security. | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `SSDF-TASK-PW.6.2` | Determine which compiler, interpreter, and build tool features should be used and how each should be configured, then implement and use the approved configurations. | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |

---

## PCI DSS v4.0.1

**O que esta ES traz para este capítulo:** contribui 8 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `PCI-12.5.1` | An inventory of system components that are 12.5.1.a Examine the inventory to verify it includes. An inventory of system components that are 12.5.1.a Examine the inventory to verify it includes c | conceito: Threat Representation Models (mechanism `ACM-TMR-001`) |
| `PCI-3.3.3` | Additional requirement for issuers and 3.3.3.a Additional testing procedure for issu. Additional requirement for issuers and 3.3.3.a Additional testing procedure for is | conceito: Secret Management Systems (mechanism `ACM-SPC-001`) |
| `PCI-5.3.3` | For removable electronic media, the anti- 5.3.3.a Examine anti-malware solution(s). For removable electronic media, the anti- 5.3.3.a Examine anti-malware solution(s) entry met | conceito: Build And Image Inventory Generation (mechanism `ACM-SCBI-005`) |
| `PCI-5.4.1` | Processes and automated mechanisms are in 5.4.1 Observe implemented processes and. Processes and automated mechanisms are in 5.4.1 Observe implemented processes and personnel | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |
| `PCI-7.2.6` | All user access to query repositories of stored 7.2.6.a Examine policies and procedures and. All user access to query repositories of stored 7.2.6.a Examine policies and procedures and | aplicacao_lifecycle (strong): Aplicação de Arquitetura Segura no Ciclo de Vida > User Stories reutilizáveis |
| `PCI-9.4.2` | All media with cardholder data is classified in 9.4.2.a Examine documentation to verify that. All media with cardholder data is classified in 9.4.2.a Examine documentation to verify that | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `PCI-9.4.4` | Management approves all media with 9.4.4.a Examine documentation to verify that. Management approves all media with 9.4.4.a Examine documentation to verify that | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `PCI-9.4.7` | Electronic media with cardholder data is 9.4.7.a Examine the media destruction policy to. Electronic media with cardholder data is 9.4.7.a Examine the media destruction policy to cont | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |

---

## SLSA Specification v1.0 — Build Track

**O que esta ES traz para este capítulo:** contribui 7 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `SLSA-BUILD-L3` | Build L3: Hardened builds. Summary Forging the provenance or evading verification requires exploiting a vulnerability that is beyond the capabilities of most adversaries. In practice, this means that | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `SLSA-BUILD-PLATFORM-ISOLATION` | Isolation strength. The build platform is responsible for isolating between builds, even within the same tenant project. In other words, how strong of a guarantee do we have that the build really exec | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `SLSA-BUILD-PLATFORM-PROVENANCE-GENERATION` | Provenance generation. The build platform is responsible for generating provenance describing how the package was produced. The SLSA Build level describes the overall provenance integrity according to | conceito: Artifact Signing And Attestation (mechanism `ACM-SCBI-004`) |
| `SLSA-PRODUCER-CONSISTENT-BUILD` | Follow a consistent build process. The producer MUST build their artifact in a consistent manner such that verifiers can form expectations about the build process. In some implementations, the produce | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `SLSA-PRODUCER-DISTRIBUTE-PROVENANCE` | Distribute provenance. The producer MUST distribute provenance to artifact consumers. The producer MAY delegate this responsibility to the package ecosystem , provided that the package ecosystem is ca | conceito: Artifact Signing And Attestation (mechanism `ACM-SCBI-004`) |
| `SLSA-VERIFY-BUILD-LEVEL` | Step 1: Check SLSA Build level. First, check the SLSA Build level by comparing the artifact to its provenance and the provenance to a preconfigured root of trust. The goal is to ensure that the proven | conceito: Artifact Signing And Attestation (mechanism `ACM-SCBI-004`) |
| `SLSA-VERIFY-EXPECTATIONS` | Step 2: Check expectations. Next, check that the package’s provenance meets your expectations for that package in order to mitigate threat “C” . In our threat model, the adversary has ability to invok | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |

---

## MITRE CWE — Software Development View (v4.19.1)

**O que esta ES traz para este capítulo:** contribui 5 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `CWE-1103` | Use of Platform-Dependent Third Party Components. The product relies on third-party components that do not provide equivalent functionality across all desirable platforms. | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `CWE-1104` | Use of Unmaintained Third Party Components. The product relies on third-party components that are not actively supported or maintained by the original developer or a trusted proxy for the original dev | conceito: Approved Source And Registry Governance (practice `ACP-SCBI-003`) |
| `CWE-205` | Observable Behavioral Discrepancy. The product's behaviors indicate important differences that may be observed by unauthorized actors in a way that reveals | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `CWE-347` | Improper Verification of Cryptographic Signature. The product does not verify, or incorrectly verifies, the cryptographic signature for data. | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `CWE-841` | Improper Enforcement of Behavioral Workflow. The product supports a session in which more than one behavior must be performed by an actor, but it does not properly ensure that the actor performs the b | conceito: Code Review For Input And Error Discipline (mechanism `ACM-IVF-001`) |

---

## OWASP ASVS v5.0.0

**O que esta ES traz para este capítulo:** contribui 4 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `ASVS-REQ-V1.3.4` | Verify that user-supplied Scalable Vector Graphics (SVG) scriptable content is validated or sanitized to contain only tags and attributes (such as draw graphics) that are safe for the application, e.g | conceito: Code Review For Input And Error Discipline (mechanism `ACM-IVF-001`) |
| `ASVS-REQ-V11.1.2` | Verify that a cryptographic inventory is performed, maintained, regularly updated, and includes all cryptographic keys, algorithms, and certificates used by the application. It must also document wher | conceito: Gestão de segredos, configuração protegida e identidades operacionais (slice `ACO-SPC`) |
| `ASVS-REQ-V15.1.2` | Verify that an inventory catalog, such as software bill of materials (SBOM), is maintained of all third-party libraries in use, including verifying that components come from pre-defined, trusted, and | conceito: Versioned Diagrams And ADR Records (mechanism `ACM-ATB-001`) |
| `ASVS-REQ-V5.4.3` | Verify that files obtained from untrusted sources are scanned by antivirus scanners to prevent serving of known malicious content. | conceito: Code Review For Input And Error Discipline (mechanism `ACM-IVF-001`) |

---

## SAFECode — Software Integrity Controls (2010)

**O que esta ES traz para este capítulo:** contribui 4 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `SCSIC-DELIVERY-SIGNING` | Code Signing and Cryptographic Verification. Products digitally marked with vendor identity; checksums and hashes for component verification; integrity verification during installation and execution | conceito: Build And Image Inventory Generation (mechanism `ACM-SCBI-005`) |
| `SCSIC-DEV-BUILD` | Build Environment Security. Automated builds, minimal human access, build scripts as code assets, service accounts traceable, build traceability to individuals | conceito: Artifact Signing And Attestation (mechanism `ACM-SCBI-004`) |
| `SCSIC-DEV-MANIFEST` | Software Bill of Materials / Manifest. Manifest of all code assets contributing to a product, including in-house and third party components, similar to BOM in manufacturing | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `SCSIC-SOURCING-OSS` | Open Source Software Sourcing Controls. Evaluate reputation and release practices of OSS communities; validate packages and distribution sites; vulnerability monitoring and patching strategy | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |

---

## NIST AI RMF 1.0

**O que esta ES traz para este capítulo:** contribui 3 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `NIST-AI-RMF-GOVERN-1` | GOVERN 1.1: Legal and regulatory requirements involving AI. Policies, processes, are understood, managed, and documented. procedures, and GOVERN 1.2: The characteristics of trustworthy AI are inte- pr | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `NIST-AI-RMF-GOVERN-4` | GOVERN 4.1: Organizational policies and practices are in place. Organizational to foster a critical thinking and safety-first mindset in the design, teams are committed development, deployment, and us | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `NIST-AI-RMF-MAP-2.3` | Scientific integrity and TEVV considerations are iden-. tified and documented, including those related to experimental design, data collection and selection (e.g., availability, repre- sentativeness, | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |

---

## PCI Secure SLC v1.1

**O que esta ES traz para este capítulo:** contribui 3 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `PCISSLC-4.1` | Existing and emerging software vulnerabilities detected in a timely manner. Mature process for security testing; tools appropriate for software architecture; testing throughout lifecycle including thi | conceito: Test Execution Surfaces (mechanism `ACM-TSV-002`) |
| `PCISSLC-6.2` | Software releases and updates delivered securely ensuring integrity. Mechanism to verify integrity of updated code during delivery; processes reasonable and appropriate; results in secure delivery | conceito: Build And Image Inventory Generation (mechanism `ACM-SCBI-005`) |
| `PCISSLC-7.1` | Sensitive production data only collected where legitimate business need. Process to record and authorize collection/retention of sensitive data; inventory maintained; decisions approved and justified | conceito: Secret Scope And Binding Controls (mechanism `ACM-SPC-004`) |

---

## NIST AI 100-2 e2025 — Adversarial Machine Learning Taxonomy

**O que esta ES traz para este capítulo:** contribui 2 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `NIST-AI-100-2-E2025-2.1.5` | Data Modality. Until recently, most attacks and defenses in adversarial machine learning have operated under a single modality, but a new trend in the field is to use multimodal data. The tax- onomy o | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |
| `NIST-AI-100-2-E2025-2.3.3` | Backdoor Poisoning. [NISTAML.021, NISTAML.023] [Back to Index] Backdoor poisoning attacks are poisoning attacks that cause the targeted model to misclas- sify samples containing a particular BACKDOOR | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |

---

## SAFECode — Practical Security Stories and Tasks for Agile Development (2012)

**O que esta ES traz para este capítulo:** contribui 2 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `SCAGILE-OPS-10` | Perform automated vulnerability scanner. Perform and add to testing cycle automated vulnerability scanner (OS and web as appropriate) | conceito: Test Execution Surfaces (mechanism `ACM-TSV-002`) |
| `SCAGILE-OPS-11` | Perform automated malware scanner on released binaries. Perform and add to release cycle automated malware scanner on released binaries | conceito: Artifact Signing And Attestation (mechanism `ACM-SCBI-004`) |

---

## EU Cyber Resilience Act (CRA)

**O que esta ES traz para este capítulo:** contribui 1 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `CRA-ART-19` | CRA Article 19. Article 19 (Obligations of distributors) requires distributors, when making a product with digital elements available on the market, to act with due care in relation to the requirement | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |

---

## EU Digital Operational Resilience Act (DORA)

**O que esta ES traz para este capítulo:** contribui 1 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `DORA-ART-24` | DORA Article 24. Article 24 (General requirements for the performance of digital operational resilience testing) requires financial entities, other than microenterprises, to establish, maintain and re | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |

---

## OWASP LLM Top 10 (2025)

**O que esta ES traz para este capítulo:** contribui 1 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `LLM03-2025` | LLM03:2025 Supply Chain. LLM supply chains are susceptible to various vulnerabilities, which can affect the integrity of training data, models, and deployment platforms. These risks can result in bias | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |

---

## OWASP MCP — Secure Server Development v1.0

**O que esta ES traz para este capítulo:** contribui 1 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `OWASP-MCP-CONTINUOUS-VALIDATION` | Tools & Continuous Validation. 8. Tools & Continuous Validation • Automated Code Scanning: Use static analysis (SAST) tools (with custom MCP rules) and Invariant MCP-Scan in your CI/CD pipeline. Use S | conceito: Integridade da supply chain de software e do build (slice `ACO-SCBI`) |

---

## OWASP MCP — Third-Party Servers v1.0

**O que esta ES traz para este capítulo:** contribui 1 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `OWASP-MCP-3P-GOVERNANCE-REGISTRY` | Trusted registry and governance workflow for third-party MCP servers. Tools & Utilities No tool will provide complete coverage, and the tools listed will vary in maturity and effectiveness. Use these | conceito: Approved Source And Registry Governance (practice `ACP-SCBI-003`) |

---

## OWASP MCP Top 10 (v0.1, 2025 beta)

**O que esta ES traz para este capítulo:** contribui 1 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `MCP04-2025` | Software Supply Chain Attacks & Dependency Tampering. MCP ecosystems depend on open-source packages, connectors, and model-side plug-ins that may contain malicious or vulnerable components. A compromi | conceito: Artifact Signing And Attestation (mechanism `ACM-SCBI-004`) |

---

## SAFECode — Fundamental Practices for Secure Software Development (2018)

**O que esta ES traz para este capítulo:** contribui 1 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `SCFPSSD-FIX-VULN` | Fix the Vulnerability. Process for fixing identified vulnerabilities and providing patches | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |

---
