# 25. Rastreabilidade — Deploy Seguro

## Sumário

Este capítulo trata de **release promotion e deploy controlado** —
gates de promoção, rollback, readiness checks, exposição runtime
minimizada. As fontes externas seguintes contribuem para esta área:

- **MITRE CAPEC v3.9** — 80 referência(s)
- **NIST SP 800-53 Rev. 5** — 70 referência(s)
- **OWASP DSOMM** — 38 referência(s)
- **OWASP ASVS v5.0.0** — 18 referência(s)
- **OWASP SAMM v2.1** — 18 referência(s)
- **CIS Controls v8.1.2** — 17 referência(s)
- **PCI DSS v4.0.1** — 12 referência(s)
- **MITRE CWE — Software Development View (v4.19.1)** — 9 referência(s)
- **PCI Secure SLC v1.1** — 6 referência(s)
- **NIST SSDF (SP 800-218 v1.1)** — 6 referência(s)
- **EU Digital Operational Resilience Act (DORA)** — 2 referência(s)
- **SAFECode — Practical Security Stories and Tasks for Agile Development (2012)** — 2 referência(s)
- **SAFECode — Software Integrity Controls (2010)** — 1 referência(s)

---

## MITRE CAPEC v3.9

**O que esta ES traz para este capítulo:** contribui 80 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `CAPEC-11` | An attack of this type exploits a Web server's decision to take action based on filename or file extension. Because different file types are handled by different server processes, misclassification ma | conceito: Code Review For Input And Error Discipline (mechanism `ACM-IVF-001`) |
| `CAPEC-141` | An attacker exploits the functionality of cache technologies to cause specific data to be cached that aids the attackers' objectives. This describes any attack whereby an attacker places incorrect or | conceito: Trust-Boundary And DFD Modeling (mechanism `ACM-ATB-002`) |
| `CAPEC-142` | A domain name server translates a domain name (such as www.example.com) into an IP address that Internet hosts use to contact Internet resources. An adversary modifies a public DNS cache to cause cert | conceito: Trust-Boundary And DFD Modeling (mechanism `ACM-ATB-002`) |
| `CAPEC-146` | An adversary corrupts or modifies the content of XML schema information passed between a client and server for the purpose of undermining the security of the target. XML Schemas provide the structure | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `CAPEC-161` | An attacker exploits characteristics of the infrastructure of a network entity in order to perpetrate attacks or information gathering on network objects or effect a change in the ordinary information | conceito: Trust-Boundary And DFD Modeling (mechanism `ACM-ATB-002`) |
| `CAPEC-165` | An attacker modifies file contents or attributes (such as extensions or names) of files in a manner to cause incorrect processing by an application. Attackers use this class of attacks to cause applic | conceito: Code Review For Input And Error Discipline (mechanism `ACM-IVF-001`) |
| `CAPEC-166` | An attacker forces the target into a previous state in order to leverage potential weaknesses in the target dependent upon a prior configuration or state-dependent factors. Even in cases where an atta | conceito: Trust-Boundary And DFD Modeling (mechanism `ACM-ATB-002`) |
| `CAPEC-168` | An attacker exploits the functionality of Microsoft NTFS Alternate Data Streams (ADS) to undermine system security. ADS allows multiple "files" to be stored in one directory entry referenced as filena | conceito: Code Review For Input And Error Discipline (mechanism `ACM-IVF-001`) |
| `CAPEC-176` | An attacker manipulates files or settings external to a target application which affect the behavior of that application. For example, many applications use external configuration files and libraries | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `CAPEC-184` | An attacker initiates a series of events designed to cause a user, program, server, or device to perform actions which undermine the integrity of software code, device data structures, or device firmw | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `CAPEC-185` | An attacker uses deceptive methods to cause a user or an automated process to download and install dangerous code that originates from an attacker controlled source. There are several variations to th | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `CAPEC-186` | An adversary uses deceptive methods to cause a user or an automated process to download and install dangerous code believed to be a valid update that originates from an adversary controlled source. Mi | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `CAPEC-187` | An attacker exploits two layers of weaknesses in server or client software for automated update mechanisms to undermine the integrity of the target code-base. The first weakness involves a failure to | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `CAPEC-268` | The attacker injects, manipulates, deletes, or forges malicious log entries into the log file, in an attempt to mislead an audit of the log file or cover tracks of an attack. Due to either insufficien | conceito: Trust-Boundary And DFD Modeling (mechanism `ACM-ATB-002`) |
| `CAPEC-270` | An adversary adds a new entry to the "run keys" in the Windows registry so that an application of their choosing is executed when a user logs in. In this way, the adversary can get their executable to | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `CAPEC-271` | An adversary corrupts or modifies the content of a schema for the purpose of undermining the security of the target. Schemas provide the structure and content definitions for resources used by an appl | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `CAPEC-35` | An attack of this type exploits a system's trust in configuration and resource files. When the executable loads the resource (such as an image file or configuration file) the attacker has modified the | conceito: Code Review For Input And Error Discipline (mechanism `ACM-IVF-001`) |
| `CAPEC-439` | An attacker undermines the integrity of a product, software, or technology at some stage of the distribution channel. The core threat of modification or manipulation during distribution arise from the | conceito: Artifact Signing And Attestation (mechanism `ACM-SCBI-004`) |
| `CAPEC-441` | An adversary installs or adds malicious logic (also known as malware) into a seemingly benign component of a fielded system. This logic is often hidden from the user of the system and works behind the | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `CAPEC-442` | An adversary adds malicious logic, often in the form of a computer virus, to otherwise benign software. This logic is often hidden from the user of the software and works behind the scenes to achieve | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `CAPEC-443` | An adversary uses their privileged position within an authorized development organization to inject malicious logic into a codebase or product. Mitigations: Assess software and hardware during develop | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `CAPEC-444` | An adversary modifies a technology, product, or component during its development to acheive a negative impact once the system is deployed. The goal of the adversary is to modify the system in such a w | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `CAPEC-445` | An adversary exploits a configuration management system so that malicious logic is inserted into a software products build, update or deployed environment. If an adversary can control the elements inc | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `CAPEC-447` | An adversary modifies the design of a technology, product, or component to acheive a negative impact once the system is deployed. In this type of attack, the goal of the adversary is to modify the des | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `CAPEC-448` | An adversary tampers with a DLL and embeds a computer virus into gaps between legitimate machine instructions. These gaps may be the result of compiler optimizations that pad memory blocks for perform | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `CAPEC-452` | An adversary inserts malicious logic into hardware, typically in the form of a computer virus or rootkit. This logic is often hidden from the user of the hardware and works behind the scenes to achiev | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `CAPEC-456` | An adversary inserts malicious logic into memory enabling them to achieve a negative impact. This logic is often hidden from the user of the system and works behind the scenes to achieve negative impa | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `CAPEC-457` | An adversary loads malicious code onto a USB memory stick in order to infect any system which the device is plugged in to. USB drives present a significant security risk for business and government ag | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `CAPEC-458` | An adversary inserts malicious logic into a product or technology via flashing the on-board memory with a code-base that contains malicious logic. Various attacks exist against the integrity of flash | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `CAPEC-481` | Adversaries can provide contradictory destinations when sending messages. Traffic is routed in networks using the domain names in various headers available at different levels of the OSI model. In a C | conceito: Trust-Boundary And DFD Modeling (mechanism `ACM-ATB-002`) |
| `CAPEC-51` | SOA and Web Services often use a registry to perform look up, get schema information, and metadata about services. A poisoned registry can redirect (think phishing for servers) the service requester t | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `CAPEC-511` | An attacker uses common delivery mechanisms such as email attachments or removable media to infiltrate the IDE (Integrated Development Environment) of a victim manufacturer with the intent of implanti | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `CAPEC-516` | An adversary with access to system components during allocated baseline development can substitute a maliciously altered hardware component for a baseline component during the product development and | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `CAPEC-517` | An attacker with access to a manufacturer's documentation, which include descriptions of advanced technology and/or specific components' criticality, alters the documents to circumvent dial-down funct | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `CAPEC-518` | An attacker with access to a manufacturer's documentation alters the descriptions of system capabilities with the intent of causing errors in derived system requirements, impacting the overall effecti | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `CAPEC-519` | An attacker with access to a manufacturer's documentation containing requirements allocation and software design processes maliciously alters the documentation in order to cause errors in system desig | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `CAPEC-520` | An adversary with either direct access to the product assembly process or to the supply of subcomponents used in the product assembly process introduces counterfeit hardware components into product as | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `CAPEC-521` | An attacker with access to a manufacturer's hardware manufacturing process documentation alters the design specifications, which introduces flaws advantageous to the attacker once the system is deploy | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `CAPEC-524` | An attacker alters or establishes rogue processes in an integration facility in order to insert maliciously altered components into the system. The attacker would then supply the malicious components. | conceito: Artifact Signing And Attestation (mechanism `ACM-SCBI-004`) |
| `CAPEC-532` | An attacker with access to download and update system software sends a maliciously altered BIOS to the victim or victim supplier/integrator, which when installed allows for future exploitation. Mitiga | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `CAPEC-533` | An attacker introduces malicious code to the victim's system by altering the payload of a software update, allowing for additional compromise or site disruption at the victim location. These manual, o | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `CAPEC-536` | An attacker with access to data files and processes on a victim's system injects malicious data into critical operational data during configuration or recalibration, causing the victim's system to per | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `CAPEC-537` | An adversary, leveraging the ability to manipulate components of primary support systems and tools within the development and production environments, inserts malicious software within the hardware an | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `CAPEC-538` | Adversaries implant malicious code in open source software (OSS) libraries to have it widely distributed, as OSS is commonly downloaded by developers and other users to incorporate into software devel | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `CAPEC-539` | An attacker with access to the development environment process of an application-specific integrated circuit (ASIC) for a victim system being developed or maintained after initial deployment can inser | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `CAPEC-547` | An adversary conducts a physical attack a device or component, destroying it such that it no longer functions as intended. | conceito: API Gateway With Mutual Authentication (mechanism `ACM-ITS-001`) |
| `CAPEC-548` | An adversary contaminates organizational information systems (including devices and networks) by causing them to handle information of a classification/sensitivity for which they have not been authori | conceito: Code Review For Input And Error Discipline (mechanism `ACM-IVF-001`) |
| `CAPEC-559` | In this attack pattern, the adversary sends disruptive signals at a target satellite using a rogue uplink station to disrupt the intended transmission. Those within the satellite's footprint are preve | conceito: API Gateway With Mutual Authentication (mechanism `ACM-ITS-001`) |
| `CAPEC-571` | An adversary prevents host-generated logs being delivered to a central location in an attempt to hide indicators of compromise. | conceito: Trust-Boundary And DFD Modeling (mechanism `ACM-ATB-002`) |
| `CAPEC-572` | An adversary modifies file contents by adding data to files for several reasons. Many different attacks could “follow” this pattern resulting in numerous outcomes. Adding data to a file could also res | conceito: Code Review For Input And Error Discipline (mechanism `ACM-IVF-001`) |
| `CAPEC-582` | An adversary disables the network route between two targets. The goal is to completely sever the communications channel between two entities. This is often the result of a major error or the use of an | conceito: API Gateway With Mutual Authentication (mechanism `ACM-ITS-001`) |
| `CAPEC-583` | In this attack pattern, an adversary physically disables networking hardware by powering it down or disconnecting critical equipment. Disabling or shutting off critical system resources prevents them | conceito: API Gateway With Mutual Authentication (mechanism `ACM-ITS-001`) |
| `CAPEC-584` | An adversary suppresses the Border Gateway Protocol (BGP) advertisement for a route so as to render the underlying network inaccessible. The BGP protocol helps traffic move throughout the Internet by | conceito: API Gateway With Mutual Authentication (mechanism `ACM-ITS-001`) |
| `CAPEC-585` | In this attack pattern, an adversary influences a target's web-hosting company to disable a target domain. The goal is to prevent access to the targeted service provided by that domain. It usually occ | conceito: API Gateway With Mutual Authentication (mechanism `ACM-ITS-001`) |
| `CAPEC-589` | An adversary intercepts traffic and intentionally drops DNS requests based on content in the request. In this way, the adversary can deny the availability of specific services or content to the user e | conceito: API Gateway With Mutual Authentication (mechanism `ACM-ITS-001`) |
| `CAPEC-590` | An adversary performing this type of attack drops packets destined for a target IP address. The aim is to prevent access to the service hosted at the target IP address. Mitigations: Have a large pool | conceito: API Gateway With Mutual Authentication (mechanism `ACM-ITS-001`) |
| `CAPEC-601` | An adversary uses radio noise or signals in an attempt to disrupt communications. By intentionally overwhelming system resources with illegitimate traffic, service is denied to the legitimate traffic | conceito: API Gateway With Mutual Authentication (mechanism `ACM-ITS-001`) |
| `CAPEC-603` | An adversary blocks the delivery of an important system resource causing the system to fail or stop working. | conceito: API Gateway With Mutual Authentication (mechanism `ACM-ITS-001`) |
| `CAPEC-604` | In this attack scenario, the attacker actively transmits on the Wi-Fi channel to prevent users from transmitting or receiving data from the targeted Wi-Fi network. There are several known techniques t | conceito: API Gateway With Mutual Authentication (mechanism `ACM-ITS-001`) |
| `CAPEC-605` | In this attack scenario, the attacker actively transmits signals to overpower and disrupt the communication between a cellular user device and a cell tower. Several existing techniques are known in th | conceito: API Gateway With Mutual Authentication (mechanism `ACM-ITS-001`) |
| `CAPEC-607` | An attacker obstructs the interactions between system components. By interrupting or disabling these interactions, an adversary can often force the system into a degraded state or cause the system to | conceito: API Gateway With Mutual Authentication (mechanism `ACM-ITS-001`) |
| `CAPEC-614` | SIM cards are the de facto trust anchor of mobile devices worldwide. The cards protect the mobile identity of subscribers, associate devices with phone numbers, and increasingly store payment credenti | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `CAPEC-635` | The extension of a file name is often used in various contexts to determine the application that is used to open and use it. If an attacker can cause an alternative application to be used, it may be a | conceito: Code Review For Input And Error Discipline (mechanism `ACM-IVF-001`) |
| `CAPEC-636` | Files on various operating systems can have a complex format which allows for the storage of other data, in addition to its contents. Often this is metadata about the file, such as a cached thumbnail | conceito: Code Review For Input And Error Discipline (mechanism `ACM-IVF-001`) |
| `CAPEC-638` | An adversary exploits systems features and/or improperly protected firmware of hardware components, such as Hard Disk Drives (HDD), with the goal of executing malicious code from within the component' | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `CAPEC-649` | An adversary adds a space character to the end of a file extension and takes advantage of an application that does not properly neutralize trailing special elements in file names. This extra space, wh | conceito: Code Review For Input And Error Discipline (mechanism `ACM-IVF-001`) |
| `CAPEC-655` | An adversary adds data to a file to increase the file size beyond what security tools are capable of handling in an attempt to mask their actions. In addition to this, adding data to a fil | conceito: Code Review For Input And Error Discipline (mechanism `ACM-IVF-001`) |
| `CAPEC-657` | An attackers uses identify or content spoofing to trick a client into performing an automated software update from a malicious source. A malicious automated software update that leverages spoofing can | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `CAPEC-669` | An adversary with access to an organization’s software update infrastructure inserts malware into the content of an outgoing update to fielded systems where a wide range of malicious effects are possi | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `CAPEC-670` | An adversary with the ability to alter tools used in a development environment causes software to be developed with maliciously modified tools. Such tools include requirements management and database | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `CAPEC-671` | An adversary with access to functional requirements for an application specific integrated circuit (ASIC), a chip designed/customized for a singular particular use, maliciously alters requirements der | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `CAPEC-672` | During the programming step of chip manufacture, an adversary with access and necessary technical skills maliciously alters a chip’s intended program logic to produce an effect intended by the adversa | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `CAPEC-673` | Software produced by a reputable developer is clandestinely infected with malicious code and then digitally signed by the unsuspecting developer, where the software has been altered via a compromised | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `CAPEC-674` | An adversary alters the functionality of a field-programmable gate array (FPGA) by causing an FPGA configuration memory chip reload in order to introduce a malicious function that could result in the | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `CAPEC-678` | During the system build process, the system is deliberately misconfigured by the alteration of the build data. Access to system configuration data files and build processes is susceptible to deliberat | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `CAPEC-700` | An adversary which has gained elevated access to network boundary devices may use these devices to create a channel to bridge trusted and untrusted networks. Boundary devices do not necessarily have t | conceito: Trust-Boundary And DFD Modeling (mechanism `ACM-ATB-002`) |
| `CAPEC-75` | Generally these are manually edited files that are not in the preview of the system administrators, any ability on the attackers' behalf to modify these files, for example in a CVS repository, gives u | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `CAPEC-81` | Web Logs Tampering attacks involve an attacker injecting, deleting or otherwise tampering with the contents of web logs typically for the purposes of masking other malicious behavior. Additionally, wr | conceito: Trust-Boundary And DFD Modeling (mechanism `ACM-ATB-002`) |
| `CAPEC-93` | This attack targets the log files of the target host. The attacker injects, manipulates or forges malicious log entries in the log file, allowing them to mislead a log audit, cover traces of attack, o | conceito: Trust-Boundary And DFD Modeling (mechanism `ACM-ATB-002`) |
| `CAPEC-96` | An application typically makes calls to functions that are a part of libraries external to the application. These libraries may be part of the operating system or they may be third party libraries. It | conceito: API Gateway With Mutual Authentication (mechanism `ACM-ITS-001`) |

---

## NIST SP 800-53 Rev. 5

**O que esta ES traz para este capítulo:** contribui 70 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `SP800-53-CM-1` | Develop, document, and disseminate to {{ insert: param, cm-1_prm_1 }}: {{ insert: param, cm-01_odp.03 }} configuration management policy that: Procedures to facilitate the implementation of the config | conceito: Accountable Release Approval (practice `ACP-RPR-001`) |
| `SP800-53-CM-10` | Use software and associated documentation in accordance with contract agreements and copyright laws; Track the use of software and associated documentation protected by quantity licenses to control co | conceito: Approved Source And Registry Governance (practice `ACP-SCBI-003`) |
| `SP800-53-CM-10.1` | Establish the following restrictions on the use of open-source software: {{ insert: param, cm-10.01_odp }}. | conceito: Approved Source And Registry Governance (practice `ACP-SCBI-003`) |
| `SP800-53-CM-11` | Establish {{ insert: param, cm-11_odp.01 }} governing the installation of software by users; Enforce software installation policies through the following methods: {{ insert: param, cm-11_odp.02 }} ; a | conceito: Approved Source And Registry Governance (practice `ACP-SCBI-003`) |
| `SP800-53-CM-11.1` | Alerts for Unauthorized Installations | conceito: Approved Source And Registry Governance (practice `ACP-SCBI-003`) |
| `SP800-53-CM-11.2` | Allow user installation of software only with explicit privileged status. | conceito: Approved Source And Registry Governance (practice `ACP-SCBI-003`) |
| `SP800-53-CM-11.3` | Enforce and monitor compliance with software installation policies using {{ insert: param, cm-11.3_prm_1 }}. | conceito: Approved Source And Registry Governance (practice `ACP-SCBI-003`) |
| `SP800-53-CM-12` | Identify and document the location of {{ insert: param, cm-12_odp }} and the specific system components on which the information is processed and stored; Identify and document the users who have acces | conceito: Operational Identity Binding And OIDC Use (practice `ACP-SPC-004`) |
| `SP800-53-CM-12.1` | Use automated tools to identify {{ insert: param, cm-12.01_odp.01 }} on {{ insert: param, cm-12.01_odp.02 }} to ensure controls are in place to protect organizational information and individual privac | conceito: Operational Identity Binding And OIDC Use (practice `ACP-SPC-004`) |
| `SP800-53-CM-13` | Develop and document a map of system data actions. | conceito: Trust-Boundary And Flow Review (practice `ACP-ATB-003`) |
| `SP800-53-CM-14` | Prevent the installation of {{ insert: param, cm-14_prm_1 }} without verification that the component has been digitally signed using a certificate that is recognized and approved by the organization. | conceito: Artifact Signature And Provenance Validation (practice `ACP-SCBI-006`) |
| `SP800-53-CM-2` | Develop, document, and maintain under configuration control, a current baseline configuration of the system; and Review and update the baseline configuration of the system: {{ insert: param, cm-02_odp | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `SP800-53-CM-2.1` | Reviews and Updates | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `SP800-53-CM-2.2` | Maintain the currency, completeness, accuracy, and availability of the baseline configuration of the system using {{ insert: param, cm-02.02_odp }}. | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `SP800-53-CM-2.3` | Retain {{ insert: param, cm-02.03_odp }} of previous versions of baseline configurations of the system to support rollback. | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `SP800-53-CM-2.4` | Unauthorized Software | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `SP800-53-CM-2.5` | Authorized Software | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `SP800-53-CM-2.6` | Maintain a baseline configuration for system development and test environments that is managed separately from the operational baseline configuration. | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `SP800-53-CM-2.7` | Issue {{ insert: param, cm-02.07_odp.01 }} with {{ insert: param, cm-02.07_odp.02 }} to individuals traveling to locations that the organization deems to be of significant risk; and Apply the followin | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `SP800-53-CM-3` | Determine and document the types of changes to the system that are configuration-controlled; Review proposed configuration-controlled changes to the system and approve or disapprove such changes with | conceito: Accountable Release Approval (practice `ACP-RPR-001`) |
| `SP800-53-CM-3.1` | Use {{ insert: param, cm-03.01_odp.01 }} to: Document proposed changes to the system; Notify {{ insert: param, cm-03.01_odp.02 }} of proposed changes to the system and request change approval; Highlig | conceito: Accountable Release Approval (practice `ACP-RPR-001`) |
| `SP800-53-CM-3.2` | Test, validate, and document changes to the system before finalizing the implementation of the changes. | conceito: Accountable Release Approval (practice `ACP-RPR-001`) |
| `SP800-53-CM-3.3` | Implement changes to the current system baseline and deploy the updated baseline across the installed base using {{ insert: param, cm-03.03_odp }}. | conceito: Accountable Release Approval (practice `ACP-RPR-001`) |
| `SP800-53-CM-3.4` | Require {{ insert: param, cm-3.4_prm_1 }} to be members of the {{ insert: param, cm-03.04_odp.03 }}. | conceito: Accountable Release Approval (practice `ACP-RPR-001`) |
| `SP800-53-CM-3.5` | Implement the following security responses automatically if baseline configurations are changed in an unauthorized manner: {{ insert: param, cm-03.05_odp }}. | conceito: Accountable Release Approval (practice `ACP-RPR-001`) |
| `SP800-53-CM-3.6` | Ensure that cryptographic mechanisms used to provide the following controls are under configuration management: {{ insert: param, cm-03.06_odp }}. | conceito: Accountable Release Approval (practice `ACP-RPR-001`) |
| `SP800-53-CM-3.7` | Review changes to the system {{ insert: param, cm-03.07_odp.01 }} or when {{ insert: param, cm-03.07_odp.02 }} to determine whether unauthorized changes have occurred. | conceito: Accountable Release Approval (practice `ACP-RPR-001`) |
| `SP800-53-CM-3.8` | Prevent or restrict changes to the configuration of the system under the following circumstances: {{ insert: param, cm-03.08_odp }}. | conceito: Accountable Release Approval (practice `ACP-RPR-001`) |
| `SP800-53-CM-4` | Analyze changes to the system to determine potential security and privacy impacts prior to change implementation. | conceito: Staged Dynamic Testing And Gate Enforcement (practice `ACP-TSV-005`) |
| `SP800-53-CM-4.1` | Analyze changes to the system in a separate test environment before implementation in an operational environment, looking for security and privacy impacts due to flaws, weaknesses, incompatibility, or | conceito: Staged Dynamic Testing And Gate Enforcement (practice `ACP-TSV-005`) |
| `SP800-53-CM-4.2` | After system changes, verify that the impacted controls are implemented correctly, operating as intended, and producing the desired outcome with regard to meeting the security and privacy requirements | conceito: Staged Dynamic Testing And Gate Enforcement (practice `ACP-TSV-005`) |
| `SP800-53-CM-5` | Define, document, approve, and enforce physical and logical access restrictions associated with changes to the system. | conceito: Least-Privilege Authorization Governance (practice `ACP-IAT-002`) |
| `SP800-53-CM-5.1` | Enforce access restrictions using {{ insert: param, cm-05.01_odp }} ; and Automatically generate audit records of the enforcement actions. | conceito: Least-Privilege Authorization Governance (practice `ACP-IAT-002`) |
| `SP800-53-CM-5.2` | Review System Changes | conceito: Least-Privilege Authorization Governance (practice `ACP-IAT-002`) |
| `SP800-53-CM-5.3` | Signed Components | conceito: Least-Privilege Authorization Governance (practice `ACP-IAT-002`) |
| `SP800-53-CM-5.4` | Enforce dual authorization for implementing changes to {{ insert: param, cm-5.4_prm_1 }}. | conceito: Least-Privilege Authorization Governance (practice `ACP-IAT-002`) |
| `SP800-53-CM-5.5` | Limit privileges to change system components and system-related information within a production or operational environment; and Review and reevaluate privileges {{ insert: param, cm-5.5_prm_1 }}. | conceito: Least-Privilege Authorization Governance (practice `ACP-IAT-002`) |
| `SP800-53-CM-5.6` | Limit privileges to change software resident within software libraries. | conceito: Least-Privilege Authorization Governance (practice `ACP-IAT-002`) |
| `SP800-53-CM-5.7` | Automatic Implementation of Security Safeguards | conceito: Least-Privilege Authorization Governance (practice `ACP-IAT-002`) |
| `SP800-53-CM-6` | Establish and document configuration settings for components employed within the system that reflect the most restrictive mode consistent with operational requirements using {{ insert: param, cm-06_od | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `SP800-53-CM-6.1` | Manage, apply, and verify configuration settings for {{ insert: param, cm-06.01_odp.01 }} using {{ insert: param, cm-6.1_prm_2 }}. | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `SP800-53-CM-6.2` | Take the following actions in response to unauthorized changes to {{ insert: param, cm-06.02_odp.02 }}: {{ insert: param, cm-06.02_odp.01 }}. | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `SP800-53-CM-6.3` | Unauthorized Change Detection | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `SP800-53-CM-6.4` | Conformance Demonstration | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `SP800-53-CM-7` | Configure the system to provide only {{ insert: param, cm-07_odp.01 }} ; and Prohibit or restrict the use of the following functions, ports, protocols, software, and/or services: {{ insert: param, cm- | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `SP800-53-CM-7.1` | Review the system {{ insert: param, cm-07.01_odp.01 }} to identify unnecessary and/or nonsecure functions, ports, protocols, software, and services; and Disable or remove {{ insert: param, cm-7.1_prm_ | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `SP800-53-CM-7.2` | Prevent program execution in accordance with {{ insert: param, cm-07.02_odp.01 }}. | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `SP800-53-CM-7.3` | Ensure compliance with {{ insert: param, cm-07.03_odp }}. | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `SP800-53-CM-7.4` | Identify {{ insert: param, cm-07.04_odp.01 }}; Employ an allow-all, deny-by-exception policy to prohibit the execution of unauthorized software programs on the system; and Review and update the list o | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `SP800-53-CM-7.5` | Identify {{ insert: param, cm-07.05_odp.01 }}; Employ a deny-all, permit-by-exception policy to allow the execution of authorized software programs on the system; and Review and update the list of aut | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `SP800-53-CM-7.6` | Require that the following user-installed software execute in a confined physical or virtual machine environment with limited privileges: {{ insert: param, cm-07.06_odp }}. | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `SP800-53-CM-7.7` | Allow execution of binary or machine-executable code only in confined physical or virtual machine environments and with the explicit approval of {{ insert: param, cm-07.07_odp }} when such code is: Ob | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `SP800-53-CM-7.8` | Prohibit the use of binary or machine-executable code from sources with limited or no warranty or without the provision of source code; and Allow exceptions only for compelling mission or operational | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `SP800-53-CM-7.9` | Identify {{ insert: param, cm-07.09_odp.01 }}; Prohibit the use or connection of unauthorized hardware components; Review and update the list of authorized hardware components {{ insert: param, cm-07. | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `SP800-53-CM-8` | Develop and document an inventory of system components that: Accurately reflects the system; Includes all components within the system; Does not include duplicate accounting of components or component | conceito: Build-Linked SBOM Generation (practice `ACP-SCBI-001`) |
| `SP800-53-CM-8.1` | Update the inventory of system components as part of component installations, removals, and system updates. | conceito: Build-Linked SBOM Generation (practice `ACP-SCBI-001`) |
| `SP800-53-CM-8.2` | Maintain the currency, completeness, accuracy, and availability of the inventory of system components using {{ insert: param, cm-8.2_prm_1 }}. | conceito: Build-Linked SBOM Generation (practice `ACP-SCBI-001`) |
| `SP800-53-CM-8.3` | Detect the presence of unauthorized hardware, software, and firmware components within the system using {{ insert: param, cm-8.3_prm_1 }} {{ insert: param, cm-08.03_odp.04 }} ; and Take the following | conceito: Build-Linked SBOM Generation (practice `ACP-SCBI-001`) |
| `SP800-53-CM-8.4` | Include in the system component inventory information, a means for identifying by {{ insert: param, cm-08.04_odp }} , individuals responsible and accountable for administering those components. | conceito: Build-Linked SBOM Generation (practice `ACP-SCBI-001`) |
| `SP800-53-CM-8.5` | No Duplicate Accounting of Components | conceito: Build-Linked SBOM Generation (practice `ACP-SCBI-001`) |
| `SP800-53-CM-8.6` | Include assessed component configurations and any approved deviations to current deployed configurations in the system component inventory. | conceito: Build-Linked SBOM Generation (practice `ACP-SCBI-001`) |
| `SP800-53-CM-8.7` | Provide a centralized repository for the inventory of system components. | conceito: Build-Linked SBOM Generation (practice `ACP-SCBI-001`) |
| `SP800-53-CM-8.8` | Support the tracking of system components by geographic location using {{ insert: param, cm-08.08_odp }}. | conceito: Build-Linked SBOM Generation (practice `ACP-SCBI-001`) |
| `SP800-53-CM-8.9` | Assign system components to a system; and Receive an acknowledgement from {{ insert: param, cm-08.09_odp }} of this assignment. | conceito: Build-Linked SBOM Generation (practice `ACP-SCBI-001`) |
| `SP800-53-CM-9` | Develop, document, and implement a configuration management plan for the system that: Addresses roles, responsibilities, and configuration management processes and procedures; Establishes a process fo | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `SP800-53-CM-9.1` | Assign responsibility for developing the configuration management process to organizational personnel that are not directly involved in system development. | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `SP800-53-MP-8.3` | Downgrade system media containing controlled unclassified information prior to public release. | conceito: Release promotion, rollout controlado e readiness para rollback (slice `ACO-RPR`) |
| `SP800-53-PL-10` | Select a control baseline for the system. | conceito: Release promotion, rollout controlado e readiness para rollback (slice `ACO-RPR`) |
| `SP800-53-PL-11` | Tailor the selected control baseline by applying specified tailoring actions. | conceito: Release promotion, rollout controlado e readiness para rollback (slice `ACO-RPR`) |
| `SP800-53-SA-5` | Obtain or develop administrator documentation for the system, system component, or system service that describes: Secure configuration, installation, and operation of the system, component, or service | conceito: Secure Configuration Baseline Management (practice `ACP-RPR-008`) |

---

## OWASP DSOMM

**O que esta ES traz para este capítulo:** contribui 38 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `DSOMM-ACTIVITY-070BB14BE04A4F3D896AA08EBA7A35F9` | Role based authentication and authorization Everyone is able to get unauthorized access to information on systems or to modify information unauthorized on systems. The usage of a (role based) access c | conceito: Access Policy Enforcement (mechanism `ACM-IAT-002`) |
| `DSOMM-ACTIVITY-0CB2626BFB0D4A0F968857F787310D97` | Blue/Green Deployment A new artifact's version can have unknown defects. Using a blue/green deployment strategy increases application availability and reduces deployment risk by simplifying the rollba | conceito: Rollback And Containment Controls (mechanism `ACM-RPR-004`) |
| `DSOMM-ACTIVITY-0DE465A655A74343AF79948BB5FF10BA` | Evaluation of the trust of used components Application and system components like Open Source libraries or images can have implementation flaws or deployment flaws. Developers or operations might star | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |
| `DSOMM-ACTIVITY-0FF45FB87EEF46ED9B3A84C955CD7060` | Usage of encryption at rest Evil actors might be able to access data and read information, e.g. from physical hard disks. By using encryption at rest, it is impossible or at least harder to to read in | conceito: Secret Management Systems (mechanism `ACM-SPC-001`) |
| `DSOMM-ACTIVITY-11B3848EE9314146A35D35409ADA24EE` | Usage of security by default for components Components (images, libraries, applications) are not hardened. Hardening of components is important, specially for image on which other teams base on. Harde | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `DSOMM-ACTIVITY-13E9757E58E24277BC0FEADC674891E6` | Inventory of production dependencies Delayed identification of components and their vulnerabilities in production. In case a vulnerability is known by the organization, it needs to be known where an a | conceito: Build And Image Inventory Generation (mechanism `ACM-SCBI-005`) |
| `DSOMM-ACTIVITY-2A44B708734F4463B0CB86DC46344B2F` | Inventory of production components An inventory of production components is a complete, up-to-date list of all applications running in production. This enables effective vulnerability management, inci | conceito: Build And Image Inventory Generation (mechanism `ACM-SCBI-005`) |
| `DSOMM-ACTIVITY-3A94D55EFD8249969EB320D23FF2A873` | Applications are running in virtualized environments Through a vulnerability in one service on a server, the attacker gains access to other services running on the same server. Applications are runnin | conceito: Trust-Boundary And DFD Modeling (mechanism `ACM-ATB-002`) |
| `DSOMM-ACTIVITY-48E92BB1FDBA40E8B6C235DE0D431833` | Immutable infrastructure The availability of IT systems might be disturbed due to components failures Redundancies in the IT systems | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `DSOMM-ACTIVITY-4CE24ABD8BA6494C828D4D193E28E4A1` | Isolated networks for virtual environments Virtual environments in default settings are able to access other virtual environments on the network stack. By using virtual machines, it is often possible | conceito: Trust-Boundary And DFD Modeling (mechanism `ACM-ATB-002`) |
| `DSOMM-ACTIVITY-598E9F131AC84A01B85E8FAB93EE81DE` | MFA One factor authentication is more vulnerable to brute force attacks and is considered less secure. Two ore more factor authentication for all accounts on all (important) systems and applications | conceito: Authentication And Federation Protocols (mechanism `ACM-IAT-001`) |
| `DSOMM-ACTIVITY-5992C38C8597403589DBD15820D81C3A` | Baseline Hardening of the environment Using default configurations for a cluster environment leads to potential risks. Harden environments according to best practices. Level 1 and partially level 2 fr | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `DSOMM-ACTIVITY-5C61FD6B81064C68AC28A8A42F1C67DC` | Backup If errors are experienced during the deployment process you want to deploy an old release. However, due to changes in the database this is often unfeasible. Performing automated periodical back | conceito: Rollback And Containment Controls (mechanism `ACM-RPR-004`) |
| `DSOMM-ACTIVITY-67E1A9AA9FBF4EC5A2DE400F01960C51` | Automated deployment process An *automated deployment process* implements the defined deployment steps using automation tools, ensuring consistency, auditability, and minimizing the risk of human erro | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `DSOMM-ACTIVITY-6DF508EF86FC4C22BD9F646C3127CE7D` | Filter outgoing traffic A compromised infrastructure component might try to send out stolen data. Having a whitelist and explicitly allowing egress traffic provides the ability to stop unauthorized da | conceito: Boundary Mediation Controls (mechanism `ACM-ATB-003`) |
| `DSOMM-ACTIVITY-746025A6DBFB4087A000E46ACAB64EE1` | Usage of an security account Having security auditing in the same account as infrastructure and applications at the cloud provide might cause evil administrators (or threat actors taking over an accou | conceito: Log Integrity And Access Controls (mechanism `ACM-SLG-003`) |
| `DSOMM-ACTIVITY-74938A3F126949B99D0FC43A79A1985A` | Defined deployment process A *defined deployment process* is a documented and standardized procedure for releasing software into production, ensuring consistency and reducing the risk of errors. Deplo | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `DSOMM-ACTIVITY-760F1056B0EE4F22A35BF65446F944CA` | Virtual environments are limited Denial of service (internally by an attacker or unintentionally by a bug) on one service effects other services All virtual environments are using resource limits on h | conceito: Trust-Boundary And DFD Modeling (mechanism `ACM-ATB-002`) |
| `DSOMM-ACTIVITY-8098E416E1ED4AE4A56183EFBE76BF57` | MFA for admins One factor authentication is more vulnerable to brute force attacks and is considered less secure. Two ore more factor authentication for all privileged accounts on systems and applicat | conceito: Authentication And Federation Protocols (mechanism `ACM-IAT-001`) |
| `DSOMM-ACTIVITY-82E499D1F4634A4BBE9068812A874AF6` | Simple access control for systems Basic access control for internal systems is implemented. Attackers a gaining access to other internal systems and application interfaces is one breach occurs. All in | conceito: Access Policy Enforcement (mechanism `ACM-IAT-002`) |
| `DSOMM-ACTIVITY-830570280B774D2E813540969768AE88` | Inventory of production artifacts In case a vulnerability of severity high or critical exists, it needs to be known where an artifacts (e.g. container image) with that vulnerability is deployed. A doc | conceito: Build And Image Inventory Generation (mechanism `ACM-SCBI-005`) |
| `DSOMM-ACTIVITY-85D52588F5424225A33820DC22A5508D` | Rolling update on deployment While a deployment is performed, the application can not be reached. A deployment without downtime is performed*. | conceito: Rollback And Containment Controls (mechanism `ACM-RPR-004`) |
| `DSOMM-ACTIVITY-8B994601575E4EA5B228ACCB18C8E514` | Infrastructure as Code No tracking of changes in systems might lead to errors in the configuration. In additions, it might lead to unauthorized changes. An examples is jenkins. Systems are setup by co | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `DSOMM-ACTIVITY-94A96F798BD6490497C0994FF88F176A` | Handover of confidential parameters Parameters are often used to set credentials, for example by starting containers or applications; these parameters can often be seen by any one listing running proc | conceito: Secret Management Systems (mechanism `ACM-SPC-001`) |
| `DSOMM-ACTIVITY-A511799B045E4B9698437D63D8C1E2AD` | Usage of feature toggles Using environment variables to enable or disable features can lead to a situation where a feature is accidentally enabled in the production environment. Usage of environment i | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `DSOMM-ACTIVITY-A854B48D83BD4F8D8621A0BDD470837F` | Same artifact for environments Building of an artifact for different environments means that an untested artifact might reach the production environment. Building an artifact once and deploying it to | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `DSOMM-ACTIVITY-AD23BE9C56614F1F81A35A5DC7061629` | Usage of edge encryption at transit Evil actors might be able to perform a man in the middle attack and sniff confidential information (e.g. authentication factors like passwords). By using encryption | conceito: API Gateway With Mutual Authentication (mechanism `ACM-ITS-001`) |
| `DSOMM-ACTIVITY-BFDACB521E3F431DAE72D844A5E86415` | Usage of test and production environments Security tests are not running regularly because test environments are missing A test and a production like environment is used | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `DSOMM-ACTIVITY-DA4FF665DCB94E939D2048CDEDC50FC2` | Defined decommissioning process The decommissioning process in the context of Docker and Kubernetes involves retiring Docker containers, images, and Kubernetes resources that are no longer needed or h | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `DSOMM-ACTIVITY-DCF9601BB4F24E259143E39AF75F7C33` | Hardening of the Environment Using default configurations for a cluster environment leads to potential risks. Harden environments according to best practices. Level 2 and partially level 3 from harden | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `DSOMM-ACTIVITY-DF428C9DEFA042269F47A15BB53F822B` | Environment depending configuration parameters (secrets) Unauthorized access to secrets stored in source code or in artifacts (e.g. container images) through process listing (e.g. ps -ef). Set configu | conceito: Secret Management Systems (mechanism `ACM-SPC-001`) |
| `DSOMM-ACTIVITY-E14DE74194B3447C8B07EEA947D82E61` | Production near environments are used by developers In case an errors occurs in production, the developer need to be able to create a production near environment on a local development environment. Us | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `DSOMM-ACTIVITY-E5386ABF91544752A1A8C3A8900F732D` | Limitation of system events System events (system calls) can lead to privilege escalation. System calls are limited. | conceito: Access Policy Enforcement (mechanism `ACM-IAT-002`) |
| `DSOMM-ACTIVITY-ECB0184C6BC945DABBBBA983797FFC93` | Usage of internal encryption at transit Evil actors within the organization of traffic in transit might be able to perform a man in the middle attack and sniff confidential information (e.g. authentic | conceito: API Gateway With Mutual Authentication (mechanism `ACM-ITS-001`) |
| `DSOMM-ACTIVITY-F0E018143B884BD0A3A9F91DB001D20B` | WAF baseline A baseline WAF configuration provides essential defense against common vulnerabilities, acting as a first line of automated threat detection and response. Steps: - Configure WAF in alert | conceito: Schema And Contract Validators (mechanism `ACM-IVF-003`) |
| `DSOMM-ACTIVITY-F0E018143B884BD0A3A9F91DB001D20BADVANCED` | WAF Advanced This advanced configuration goes beyond typical WAF implementations by enforcing strict input format checks and parameter validation to prevent any unauthorized or malformed data from com | conceito: Static Rulepacks And Security Linters (mechanism `ACM-IVF-002`) |
| `DSOMM-ACTIVITY-F0E018143B884BD0A3A9F91DB001D20BMEDIUM` | WAF medium A medium-level WAF configuration builds upon the baseline to offer a more nuanced and responsive defense mechanism against a wider array of threats. Sample steps: - Implement an enhanced se | conceito: Schema And Contract Validators (mechanism `ACM-IVF-003`) |
| `DSOMM-ACTIVITY-F8E80F1825034E3EB3BC7F67BB28DEFE` | Usage of a chaos technology Due to manual changes on a system, they are not replaceable anymore. In case of a crash it might happen that a planned redundant system is unavailable. In addition, it is h | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |

---

## OWASP ASVS v5.0.0

**O que esta ES traz para este capítulo:** contribui 18 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `ASVS-REQ-V1.4.3` | Verify that dynamically allocated memory and resources are released, and that references or pointers to freed memory are removed or set to null to prevent dangling pointers and use-after-free vulnerab | conceito: Release promotion, rollout controlado e readiness para rollback (slice `ACO-RPR`) |
| `ASVS-REQ-V13.1.1` | Verify that all communication needs for the application are documented. This must include external services which the application relies upon and cases where an end user might be able to provide an ex | conceito: Configuration Baseline Enforcement Controls (mechanism `ACM-RPR-008`) |
| `ASVS-REQ-V13.1.2` | Verify that for each service the application uses, the documentation defines the maximum number of concurrent connections (e.g., connection pool limits) and how the application behaves when that limit | conceito: Configuration Baseline Enforcement Controls (mechanism `ACM-RPR-008`) |
| `ASVS-REQ-V13.1.3` | Verify that the application documentation defines resource‑management strategies for every external system or service it uses (e.g., databases, file handles, threads, HTTP connections). This should in | conceito: Configuration Baseline Enforcement Controls (mechanism `ACM-RPR-008`) |
| `ASVS-REQ-V13.1.4` | Verify that the application's documentation defines the secrets that are critical for the security of the application and a schedule for rotating them, based on the organization's threat model and bus | conceito: Configuration Baseline Enforcement Controls (mechanism `ACM-RPR-008`) |
| `ASVS-REQ-V13.2.1` | Verify that communications between backend application components that don't support the application's standard user session mechanism, including APIs, middleware, and data layers, are authenticated. | conceito: API Gateway With Mutual Authentication (mechanism `ACM-ITS-001`) |
| `ASVS-REQ-V13.2.2` | Verify that communications between backend application components, including local or operating system services, APIs, middleware, and data layers, are performed with accounts assigned the least neces | conceito: Access Policy Enforcement (mechanism `ACM-IAT-002`) |
| `ASVS-REQ-V13.2.3` | Verify that if a credential has to be used for service authentication, the credential being used by the consumer is not a default credential (e.g., root/root or admin/admin). | conceito: Configuration Baseline Enforcement Controls (mechanism `ACM-RPR-008`) |
| `ASVS-REQ-V13.2.4` | Verify that an allowlist is used to define the external resources or systems with which the application is permitted to communicate (e.g., for outbound requests, data loads, or file access). This allo | conceito: API Gateway With Mutual Authentication (mechanism `ACM-ITS-001`) |
| `ASVS-REQ-V13.2.5` | Verify that the web or application server is configured with an allowlist of resources or systems to which the server can send requests or load data or files from. | conceito: API Gateway With Mutual Authentication (mechanism `ACM-ITS-001`) |
| `ASVS-REQ-V13.2.6` | Verify that where the application connects to separate services, it follows the documented configuration for each connection, such as maximum parallel connections, behavior when maximum allowed connec | conceito: API Gateway With Mutual Authentication (mechanism `ACM-ITS-001`) |
| `ASVS-REQ-V13.4.1` | Verify that the application is deployed either without any source control metadata, including the .git or .svn folders, or in a way that these folders are inaccessible both externally and to the appli | conceito: Configuration Baseline Enforcement Controls (mechanism `ACM-RPR-008`) |
| `ASVS-REQ-V13.4.2` | Verify that debug modes are disabled for all components in production environments to prevent exposure of debugging features and information leakage. | conceito: Configuration Baseline Enforcement Controls (mechanism `ACM-RPR-008`) |
| `ASVS-REQ-V13.4.3` | Verify that web servers do not expose directory listings to clients unless explicitly intended. | conceito: Configuration Baseline Enforcement Controls (mechanism `ACM-RPR-008`) |
| `ASVS-REQ-V13.4.4` | Verify that using the HTTP TRACE method is not supported in production environments, to avoid potential information leakage. | conceito: Configuration Baseline Enforcement Controls (mechanism `ACM-RPR-008`) |
| `ASVS-REQ-V13.4.5` | Verify that documentation (such as for internal APIs) and monitoring endpoints are not exposed unless explicitly intended. | conceito: Configuration Baseline Enforcement Controls (mechanism `ACM-RPR-008`) |
| `ASVS-REQ-V13.4.6` | Verify that the application does not expose detailed version information of backend components. | conceito: Configuration Baseline Enforcement Controls (mechanism `ACM-RPR-008`) |
| `ASVS-REQ-V13.4.7` | Verify that the web tier is configured to only serve files with specific file extensions to prevent unintentional information, configuration, and source code leakage. | conceito: Configuration Baseline Enforcement Controls (mechanism `ACM-RPR-008`) |

---

## OWASP SAMM v2.1

**O que esta ES traz para este capítulo:** contribui 18 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `SAMM-ACTIVITY-I_SD_1_A` | Use a repeatable deployment process Limited risk of human error during deployment process minimizing security issues Formalize the deployment process and secure the used tooling and processes. Define | conceito: Release Promotion Controls (mechanism `ACM-RPR-001`) |
| `SAMM-ACTIVITY-I_SD_2_A` | Automate deployment and integrate security checks Efficient deployment process with integrated security tools Automate the deployment process over all stages and introduce sensible security verificati | conceito: Release Promotion Controls (mechanism `ACM-RPR-001`) |
| `SAMM-ACTIVITY-I_SD_3_A` | Verify the integrity of deployment artifacts Assured integrity of artifacts being deployed to production Automatically verify integrity of all deployed software, independently on whether it's internal | conceito: Release Promotion Controls (mechanism `ACM-RPR-001`) |
| `SAMM-ACTIVITY-I_SD_3_B` | Enforce lifecycle management of application secrets Minimized possibility and timely detection of production secret abuse Improve the lifecycle of application secrets by regularly generating them and | conceito: Release Promotion Controls (mechanism `ACM-RPR-001`) |
| `SAMM-ACTIVITY-O_EM_1_A` | Use best-effort hardening Hardened basic configuration settings of your components Perform best-effort hardening of configurations, based on readily available information. Understanding the importance | conceito: Configuration Baseline Enforcement Controls (mechanism `ACM-RPR-008`) |
| `SAMM-ACTIVITY-O_EM_1_B` | Practice best-effort patching Mitigation of well-known issues in third-party components Perform best-effort patching of system and application components. Identify applications and third-party compone | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |
| `SAMM-ACTIVITY-O_EM_2_A` | Establish hardening baselines Consistent hardening of technology stack components in your organization Perform consistent hardening of configurations, following established baselines and guidance. Est | conceito: Configuration Baseline Enforcement Controls (mechanism `ACM-RPR-008`) |
| `SAMM-ACTIVITY-O_EM_2_B` | Formalize patch management Consistent and proactive patching of technology stack components Perform regular patching of system and application components, across the full stack. Ensure timely delivery | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |
| `SAMM-ACTIVITY-O_EM_3_A` | Perform continuous configuration monitoring Clear view on component configurations to avoid non-conformities Actively monitor configurations for non-conformance to baselines, and handle detected occur | conceito: Gate Or Policy Check For Prohibited Or Unsafe Overrides (mechanism `ACM-RPR-009`) |
| `SAMM-ACTIVITY-O_EM_3_B` | Enforce timely patch management Clear view on component patch state to avoid non-conformities Actively monitor update status and manage missing patches as security defects. Proactively obtain vulnerab | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |
| `SAMM-PRACTICE-LEVEL-G_EG_1` | G-EG-1 Education and Guidance L1 Offer staff access to resources around the topics of secure development and deployment. | conceito: Release promotion, rollout controlado e readiness para rollback (slice `ACO-RPR`) |
| `SAMM-PRACTICE-LEVEL-I_DM_2` | I-DM-2 Defect Management L2 Defect tracking used to influence the deployment process. | conceito: Release promotion, rollout controlado e readiness para rollback (slice `ACO-RPR`) |
| `SAMM-PRACTICE-LEVEL-I_SD_1` | I-SD-1 Secure Deployment L1 Deployment processes are fully documented. | conceito: Release promotion, rollout controlado e readiness para rollback (slice `ACO-RPR`) |
| `SAMM-PRACTICE-LEVEL-I_SD_3` | I-SD-3 Secure Deployment L3 Deployment process is fully automated and incorporates automated verification of all critical milestones. | conceito: Release promotion, rollout controlado e readiness para rollback (slice `ACO-RPR`) |
| `SAMM-PRACTICE-O_EM` | O-EM Environment Management This practice describes proactive activities carried out to improve and maintain the security of the environments in which the organization's applications operate. The orga | conceito: Configuration Baseline Enforcement Controls (mechanism `ACM-RPR-008`) |
| `SAMM-PRACTICE-O_IM` | O-IM Incident Management This practice addresses activities carried out to improve the organization's detection of, and response to, security incidents. Once your organization has applications in oper | conceito: Release promotion, rollout controlado e readiness para rollback (slice `ACO-RPR`) |
| `SAMM-PRACTICE-O_OM` | O-OM Operational Management This practice focuses on operational support activities required to maintain security throughout the product lifecycle. The Operational Management (OM) practice focuses on | conceito: OIDC-Based Operational Identity (mechanism `ACM-SPC-002`) |
| `SAMM-STREAM-I_SD_A` | I-SD-A Deployment Process A repeatable and consistent deployment process ensures you only deploy correct software artifacts to production. It also paves the way for representative test environments pr | conceito: Release promotion, rollout controlado e readiness para rollback (slice `ACO-RPR`) |

---

## CIS Controls v8.1.2

**O que esta ES traz para este capítulo:** contribui 17 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `CIS-11` | Establish and maintain data recovery practices sufficient to restore in-scope enterprise assets to a pre-incident and trusted state. | conceito: Release promotion, rollout controlado e readiness para rollback (slice `ACO-RPR`) |
| `CIS-11.1` | Establish and maintain a documented data recovery process that includes detailed backup procedures. In the process, address the scope of data recovery activities, recovery prioritization, and the secu | conceito: Release promotion, rollout controlado e readiness para rollback (slice `ACO-RPR`) |
| `CIS-11.2` | Perform automated backups of in-scope enterprise assets. Run backups weekly, or more frequently, based on the sensitivity of the data. | conceito: Release promotion, rollout controlado e readiness para rollback (slice `ACO-RPR`) |
| `CIS-11.3` | Protect recovery data with equivalent controls to the original data. Reference encryption or data separation, based on requirements. | conceito: Release promotion, rollout controlado e readiness para rollback (slice `ACO-RPR`) |
| `CIS-11.4` | Establish and maintain an isolated instance of recovery data. Example implementations include, version controlling backup destinations through offline, cloud, or off-site systems or services. | conceito: Release promotion, rollout controlado e readiness para rollback (slice `ACO-RPR`) |
| `CIS-11.5` | Test backup recovery quarterly, or more frequently, for a sampling of in-scope enterprise assets. | conceito: Release promotion, rollout controlado e readiness para rollback (slice `ACO-RPR`) |
| `CIS-4` | Establish and maintain the secure configuration of enterprise assets (end-user devices, including portable and mobile; network devices; non-computing/IoT devices; and servers) and software (operating | conceito: Configuration Baseline Enforcement Controls (mechanism `ACM-RPR-008`) |
| `CIS-4.11` | Remotely wipe enterprise data from enterprise-owned portable end-user devices when deemed appropriate such as lost or stolen devices, or when an individual no longer supports the enterprise. | conceito: Release promotion, rollout controlado e readiness para rollback (slice `ACO-RPR`) |
| `CIS-4.12` | Ensure separate enterprise workspaces are used on mobile end-user devices, where supported. Example implementations include using an Apple® Configuration Profile or Android™ Work Profile to separate e | conceito: Release promotion, rollout controlado e readiness para rollback (slice `ACO-RPR`) |
| `CIS-4.2` | Establish and maintain a documented secure configuration process for network devices. Review and update documentation annually, or when significant enterprise changes occur that could impact this Safe | conceito: Release promotion, rollout controlado e readiness para rollback (slice `ACO-RPR`) |
| `CIS-4.3` | Configure automatic session locking on enterprise assets after a defined period of inactivity. For general purpose operating systems, the period must not exceed 15 minutes. For mobile end-user devices | conceito: Short-Lived Token Controls (mechanism `ACM-IAT-004`) |
| `CIS-4.4` | Implement and manage a firewall on servers, where supported. Example implementations include a virtual firewall, operating system firewall, or a third-party firewall agent. | conceito: Release promotion, rollout controlado e readiness para rollback (slice `ACO-RPR`) |
| `CIS-4.5` | Implement and manage a host-based firewall or port-filtering tool on end-user devices, with a default-deny rule that drops all traffic except those services and ports that are explicitly allowed. | conceito: Release promotion, rollout controlado e readiness para rollback (slice `ACO-RPR`) |
| `CIS-4.6` | Securely manage enterprise assets and software. Example implementations include managing configuration through version-controlled Infrastructure-as-Code (IaC) and accessing administrative interfaces o | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `CIS-4.7` | Manage default accounts on enterprise assets and software, such as root, administrator, and other pre-configured vendor accounts. Example implementations can include: disabling default accounts or mak | conceito: Periodic Review And Access Audit (mechanism `ACM-IAT-003`) |
| `CIS-4.8` | Uninstall or disable unnecessary services on enterprise assets and software, such as an unused file sharing service, web application module, or service function. | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `CIS-4.9` | Configure trusted DNS servers on network infrastructure. Example implementations include configuring network devices to use enterprise-controlled DNS servers and/or reputable externally accessible DNS | conceito: Release promotion, rollout controlado e readiness para rollback (slice `ACO-RPR`) |

---

## PCI DSS v4.0.1

**O que esta ES traz para este capítulo:** contribui 12 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `PCI-2.1.1` | All security policies and operational 2.1.1 Examine documentation and interview and maintaining the various policies and | conceito: Release Promotion Controls (mechanism `ACM-RPR-001`) |
| `PCI-2.1.2` | Roles and responsibilities for performing 2.1.2.a Examine documentation to verify that assigned, personnel may not be aware of their | conceito: Release Promotion Controls (mechanism `ACM-RPR-001`) |
| `PCI-2.2.1` | Configuration standards are developed, 2.2.1.a Examine system configuration standards operating systems, databases, network devices, | conceito: Release Promotion Controls (mechanism `ACM-RPR-001`) |
| `PCI-2.2.2` | Vendor default accounts are managed as 2.2.2.a Examine system configuration standards to account names and passwords to compromise | conceito: Release Promotion Controls (mechanism `ACM-RPR-001`) |
| `PCI-2.2.3` | Primary functions requiring different security 2.2.3.a Examine system configuration standards to protocols, and daemons for their primary function | conceito: Release Promotion Controls (mechanism `ACM-RPR-001`) |
| `PCI-2.2.4` | Only necessary services, protocols, daemons, 2.2.4.a Examine system configuration standards to additional opportunities for malicious individuals | conceito: Release Promotion Controls (mechanism `ACM-RPR-001`) |
| `PCI-2.2.5` | If any insecure services, protocols, or 2.2.5.a If any insecure services, protocols, or daemons are adequately secured with | conceito: Release Promotion Controls (mechanism `ACM-RPR-001`) |
| `PCI-2.2.6` | System security parameters are configured to 2.2.6.a Examine system configuration standards to provided in system components takes advantage | conceito: Release Promotion Controls (mechanism `ACM-RPR-001`) |
| `PCI-2.2.7` | All non-console administrative access is 2.2.7.a Examine system configuration standards to does not use encrypted communications, | conceito: Rollback And Containment Controls (mechanism `ACM-RPR-004`) |
| `PCI-2.3.1` | For wireless environments connected to the 2.3.1.a Examine policies and procedures and sufficient security configurations (including | conceito: Release Promotion Controls (mechanism `ACM-RPR-001`) |
| `PCI-2.3.2` | For wireless environments connected to the 2.3.2 Interview responsible personnel and examine someone with knowledge of the key leaves the | conceito: Release Promotion Controls (mechanism `ACM-RPR-001`) |
| `PCI-REQ-2` | Requirement 2: Apply Secure Configurations to All System Components. Goal: Build and Maintain a Secure Network and Systems. | conceito: Release Promotion Controls (mechanism `ACM-RPR-001`) |

---

## MITRE CWE — Software Development View (v4.19.1)

**O que esta ES traz para este capítulo:** contribui 9 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `CWE-1051` | The product initializes data using hard-coded values that act as network resource identifiers. | conceito: Configuration Baseline Enforcement Controls (mechanism `ACM-RPR-008`) |
| `CWE-1188` | The product initializes or sets a resource with a default that is intended to be changed by the product's installer, administrator, or maintainer, but the default is not secure. | conceito: Configuration Baseline Enforcement Controls (mechanism `ACM-RPR-008`) |
| `CWE-15` | One or more system settings or configuration elements can be externally controlled by a user. | conceito: Configuration Baseline Enforcement Controls (mechanism `ACM-RPR-008`) |
| `CWE-276` | During installation, installed file permissions are set to allow anyone to modify those files. | conceito: Configuration Baseline Enforcement Controls (mechanism `ACM-RPR-008`) |
| `CWE-426` | The product searches for critical resources using an externally-supplied search path that can point to resources that are not under the product's direct control. | conceito: Configuration Baseline Enforcement Controls (mechanism `ACM-RPR-008`) |
| `CWE-427` | The product uses a fixed or controlled search path to find resources, but one or more locations in that path can be under the control of unintended actors. | conceito: Configuration Baseline Enforcement Controls (mechanism `ACM-RPR-008`) |
| `CWE-428` | The product uses a search path that contains an unquoted element, in which the element contains whitespace or other separators. This can cause the product to access resources in a parent path. | conceito: Configuration Baseline Enforcement Controls (mechanism `ACM-RPR-008`) |
| `CWE-494` | The product downloads source code or an executable from a remote location and executes the code without sufficiently verifying the origin and integrity of the code. | conceito: Release Promotion Controls (mechanism `ACM-RPR-001`) |
| `CWE-547` | The product uses hard-coded constants instead of symbolic names for security-critical values, which increases the likelihood of mistakes during code maintenance or security policy change. | conceito: Configuration Baseline Enforcement Controls (mechanism `ACM-RPR-008`) |

---

## PCI Secure SLC v1.1

**O que esta ES traz para este capítulo:** contribui 6 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `PCISSLC-10.1` | Mature process to communicate all software changes; clear summary of functionality impacted; change details accessible to stakeholders | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `PCISSLC-5.1` | Process to identify, assess, and approve all changes; security impact analysis; all decisions recorded; changes authorized by responsible personnel | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `PCISSLC-5.2` | Formal versioning system; unique identifiers in sequential manner; all changes associated with unique version | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `PCISSLC-8.1` | Guidance on secure implementation, configuration, and operation; documentation of all security-related configurable options | conceito: Rollback And Containment Controls (mechanism `ACM-RPR-004`) |
| `PCISSLC-8.2` | Detailed instructions on how to securely install, initialize, configure, and maintain software; sufficiently detailed; evidence of resulting secure configuration | conceito: Rollback And Containment Controls (mechanism `ACM-RPR-004`) |
| `PCISSLC-8.3` | Guidance updated when new software updates released or security-related options modified; reviewed at least annually | conceito: Rollback And Containment Controls (mechanism `ACM-RPR-004`) |

---

## NIST SSDF (SP 800-218 v1.1)

**O que esta ES traz para este capítulo:** contribui 6 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `SSDF-PRACTICE-PW.6` | Decrease the number of security vulnerabilities in the software and reduce costs by eliminating vulnerabilities before testing occurs. | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `SSDF-PRACTICE-PW.9` | Help improve the security of the softwar e at the time of installation to reduce the likelihood of the software being deployed with weak security settings , putting it at greater risk of compromise. | conceito: Configuration Baseline Enforcement Controls (mechanism `ACM-RPR-008`) |
| `SSDF-TASK-PW.6.1` | Use compiler , interpreter, and build tools that offer features to improve executable security. | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `SSDF-TASK-PW.6.2` | Determine which compiler, interpreter, and build tool features should be used and how each should be configured, then implement and use the approved configurations. | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `SSDF-TASK-PW.9.1` | Define a secure baseline by determining how to configure each setting that has an effect on security or a security -related setting so that the default settings are secure and do not weaken the securi | conceito: Configuration Baseline Enforcement Controls (mechanism `ACM-RPR-008`) |
| `SSDF-TASK-PW.9.2` | Implement the default settings (or groups of default settings, if applicable), and document each setting for software administrators. | conceito: Configuration Baseline Enforcement Controls (mechanism `ACM-RPR-008`) |

---

## EU Digital Operational Resilience Act (DORA)

**O que esta ES traz para este capítulo:** contribui 2 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `DORA-ART-11` | Article 11 of Digital Operational Resilience Act | conceito: Release Promotion Controls (mechanism `ACM-RPR-001`) |
| `DORA-ART-12` | Article 12 of Digital Operational Resilience Act | conceito: Release Promotion Controls (mechanism `ACM-RPR-001`) |

---

## SAFECode — Practical Security Stories and Tasks for Agile Development (2012)

**O que esta ES traz para este capítulo:** contribui 2 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `SCAGILE-EXP-11` | Environment hardening covering development systems, building environment, deployment infrastructure | conceito: Rollback And Containment Controls (mechanism `ACM-RPR-004`) |
| `SCAGILE-EXP-12` | Securing configuration e.g. web server hardening, ACLs on folders holding sensitive data, configuration file hardening | conceito: Rollback And Containment Controls (mechanism `ACM-RPR-004`) |

---

## SAFECode — Software Integrity Controls (2010)

**O que esta ES traz para este capítulo:** contribui 1 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `SCSIC-DEV-DEFAULTS` | Out of the box defaults must be examined and configured to be secure by default; least necessary privileges; disabled unnecessary services | conceito: Rollback And Containment Controls (mechanism `ACM-RPR-004`) |

---


<!-- WAVE-NOTE: **Nota Wave 3 ACO-RPR:** esta leitura funciona como âncora bounded para os rows autorizados de release promotion, rollback/readiness, hardening de configuração e defaults em produção, minimização de superfície runtime e clusters NIST de failover / non-persistence que o freeze de Wave 3 reteve em `ACO-RPR`. A leitura permanece **bounded**, mantém o Cap. `04` apenas para a diversificação arquitetural autorizada, mantém o Cap. `02` apenas como scaffold de requisitos e rastreabilidade, não reabre a visibilidade legada do Cap. `06`, e não converte `ASVS v4`, `CIS`, `NIST`, `DSOMM` ou `SAMM` em autoridade family-blind de deploy. -->
<!-- WAVE-NOTE: **Nota Wave 3 ACO-ATB:** esta superfície é limitada aos rows autorizados de deployment isolation, network change/review, dual-homed devices, heterogeneity / concealment, distributed processing e information diversity quando a evidência já aponta para suporte de deploy/runtime em `ACO-ATB`. A leitura permanece **bounded** a diversificação operacional; a âncora primária de `ACO-ATB` continua em Cap. `04`, a diversificação infra-like mais restrita continua em Cap. `08`, o scaffold de requisitos continua em Cap. `02`, o Cap. `06` não entra como superfície implícita, e este capítulo não ganha autoridade autónoma de arquitetura ou release. -->
<!-- WAVE-NOTE: **Nota Wave 4 ACO-SCBI:** esta superfície é limitada aos rows autorizados `asvs_v4_0_2::ASVS4-REQ-V14.1.5`, `asvs_v4_0_2::ASVS4-REQ-V14.3.3` e `asvs_v4_0_2::ASVS4-REQ-V14.4.7`, mais o suporte already-evidenced de `slsa_spec_v1_0_build_track::SLSA-BUILD-PLATFORM-ISOLATION` e `ssdf_sp800_218_v1_1::SSDF-PRACTICE-PO.5`. A leitura permanece **bounded** a diversificação de deploy / execution-control; as âncoras de `ACO-SCBI` continuam em Cap. `04` e `05`, o suporte governativo continua em Cap. `14`, o scaffold de rastreabilidade continua em Cap. `02`, não se reabrem Cap. `08` ou `09`, e este capítulo não ganha autoridade autónoma de `ACO-SCBI`. -->
