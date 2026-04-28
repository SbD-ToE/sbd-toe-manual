# 25. Rastreabilidade — Testes de Segurança

## Sumário

Este capítulo trata de **testes de segurança e validação empírica** —
estratégia de testes, execução, gestão de findings, rastreabilidade de
correções. As fontes externas seguintes contribuem para esta área:

- **OWASP DSOMM** — 74 referência(s)
- **NIST SP 800-53 Rev. 5** — 69 referência(s)
- **CIS Controls v8.1.2** — 24 referência(s)
- **OWASP SAMM v2.1** — 24 referência(s)
- **PCI DSS v4.0.1** — 17 referência(s)
- **SAFECode — Practical Security Stories and Tasks for Agile Development (2012)** — 13 referência(s)
- **PCI Secure SLC v1.1** — 9 referência(s)
- **NIST SSDF (SP 800-218 v1.1)** — 9 referência(s)
- **EU Digital Operational Resilience Act (DORA)** — 5 referência(s)
- **SAFECode — Fundamental Practices for Secure Software Development (2018)** — 5 referência(s)
- **OWASP ASVS v5.0.0** — 1 referência(s)
- **EU Cyber Resilience Act (CRA)** — 1 referência(s)
- **EU NIS2 Directive** — 1 referência(s)
- **EU GDPR (RGPD)** — 1 referência(s)
- **HIPAA Security Rule** — 1 referência(s)
- **SAFECode — Software Integrity Controls (2010)** — 1 referência(s)

---

## OWASP DSOMM

**O que esta ES traz para este capítulo:** contribui 74 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `DSOMM-ACTIVITY-017D9E2642B549A4B9459F59B308FB99` | API design validation Creation of insecure or non-compliant API. Design contract-first APIs using an interface description language such as OpenAPI, AsyncAPI or SOAP and validate the specification usi | conceito: Trust Boundary Models (mechanism `ACM-ITS-002`) |
| `DSOMM-ACTIVITY-0779681137F9467C9FF248F346E77FF3` | Simple Scan Deficient security tests are performed. Simple vulnerabilities are not detected and missing security configurations (e.g. headers) are not set. Fast feedback is not given. A simple scan is | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `DSOMM-ACTIVITY-07FE8C4FAE334409B1B2CF64CFCCEA86` | Software Composition Analysis (client side) Client side components might have vulnerabilities. Tests for known vulnerabilities in components via Software Composition Analysis of the frontend are perfo | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |
| `DSOMM-ACTIVITY-0C10A7F7F78F49F2943D19FDEF248FED` | Fix based on accessibility Overwhelming volume of security findings from automated testing tools. This might lead to ignorance of findings. Implement a simple risk-based prioritization framework for v | conceito: Findings Workflow And Exception Governance (mechanism `ACM-TSV-004`) |
| `DSOMM-ACTIVITY-0CB2C39A3CEC4353B3AB8D70DAF4C9D2` | Test for Patch Deployment Time Automatic PRs for dependencies are overlooked resulting in known vulnerabilities in production artifacts. Test of the Patch Deployment Time. This activity is not repeate | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |
| `DSOMM-ACTIVITY-0EC92899A5CB4649984B2FB1D6C784AD` | Number of vulnerabilities/severity/layer Communication can be performed in a simple way, e.g. text based during the build process. This activity depends on at least one security testing implementation | conceito: Findings Workflow And Exception Governance (mechanism `ACM-TSV-004`) |
| `DSOMM-ACTIVITY-13367D8FE37F4197A6109FFCA4FDE261` | Test of infrastructure components for known vulnerabilities Infrastructure components might have vulnerabilities. Test for known vulnerabilities in infrastructure components. Often, the only way to re | conceito: Threat Mitigation Linkage Controls (mechanism `ACM-TMR-005`) |
| `DSOMM-ACTIVITY-13AF12273DD14D4FA9E953DEB793C18F` | Test for Time to Patch Automatic PRs for dependencies are overlooked resulting in known vulnerabilities in production artifacts. Test of the Time to Patch (e.g. based on Mean Time to Close automatic P | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |
| `DSOMM-ACTIVITY-1BD78CDDEF114BB59B585AF2E25FE1C5` | Deactivating of unneeded tests As tools cover a wide range of different vulnerability tests, they might not match the used components. Therefore, they need more time and resources as they need and the | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `DSOMM-ACTIVITY-22AAB0EF76CE4B8C979C3699784330DB` | Coverage of service to service communication Service to service communication is not covered. Service to service communication is dumped and checked. | conceito: API Gateway With Mutual Authentication (mechanism `ACM-ITS-001`) |
| `DSOMM-ACTIVITY-26E1C6D556324EC780D2E564B98732AD` | Software Composition Analysis Subscribing to Github projects and reading release notes might help. Software Composition Analysis for infrastructure might help, but is often too fine-granular. Known vu | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |
| `DSOMM-ACTIVITY-27337442E4B14E878DC9CE86FBB79A39` | Reproducible defect tickets Vulnerability descriptions are hard to understand by staff from operations and development. Vulnerabilities include the test procedure to give the staff from operations and | conceito: Findings Workflow And Exception Governance (mechanism `ACM-TSV-004`) |
| `DSOMM-ACTIVITY-297BE0018D9441EEAB29207020D423C0` | Usage of multiple analyzers Each vulnerability analyzer has different opportunities. By using just one analyzer, some vulnerabilities might not be found. Usage of multiple static tools to find more vu | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `DSOMM-ACTIVITY-2B7CC923BDAF43E38FB4A995B7783969` | Treatment of defects per protection requirement The protection requirements for an application should consider: - Data criticality - Application accessibility (internal vs. external) - Regulatory comp | conceito: Findings Workflow And Exception Governance (mechanism `ACM-TSV-004`) |
| `DSOMM-ACTIVITY-2EBFC4218C76415CA3B0FA518915BD10` | High test intensity A too small intensity or a too high confidence might lead to not visible vulnerabilities. A deep scan with high test intensity and a low confidence threshold is performed. | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `DSOMM-ACTIVITY-44F2C8A94AAA4C72942D63F78B89F385` | Treatment of defects with high or critical severity All security problems that are rated as "high" or "critical" must be fixed before the software can be released or used in production. This means tha | conceito: Findings Workflow And Exception Governance (mechanism `ACM-TSV-004`) |
| `DSOMM-ACTIVITY-46D6A2A8F9DC4C159FC81723CFECBDDC` | Test the cloud configuration Standard hardening practices for cloud environments are not performed leading to vulnerabilities. With the help of tools, the configuration of virtual environments are tes | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `DSOMM-ACTIVITY-51F3FCE5B5C846838C41E785FE4F3B5F` | SLA per criticality Not communicating how many applications are adhering to SLAs based on the criticality of vulnerabilities can lead to delayed remediation of critical security issues, increasing the | conceito: Threat Mitigation Linkage Controls (mechanism `ACM-TMR-005`) |
| `DSOMM-ACTIVITY-55F4C9163A34474DAD969A9F7A4F6A83` | Simple visualization of defects The security level of a component is not visible. Therefore, the motivation to enhance the security is not give. Vulnerabilities are simple visualized. | conceito: Findings Workflow And Exception Governance (mechanism `ACM-TSV-004`) |
| `DSOMM-ACTIVITY-58825D221CE64748AF810EC9956E4129` | Test of virtualized environments Virtualized environments (e.g. via <i>Container Images</i>) might contains unsecure configurations. Test virtualized environments for unsecured configurations. | conceito: Trust-Boundary And DFD Modeling (mechanism `ACM-ATB-002`) |
| `DSOMM-ACTIVITY-598897A2358E441F984CE12EC4F6110A` | Regular automated tests After pushing source code to the version control system, any delay in receiving feedback on defects makes them harder for the developer to remediate. On each push and/or at giv | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `DSOMM-ACTIVITY-5B5A1EB2113F41FBA3D606AF4FDC9CEA` | Usage of multiple scanners Each vulnerability scanner has different opportunities. By using just one scanner, some vulnerabilities might not be found. Usage of multiple spiders and scanner enhance the | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `DSOMM-ACTIVITY-5E0FF85BEC894EF096B15695FA0025DC` | Coverage of more input vectors Parts of the service are not covered. For example specially formatted or coded parameters are not getting detected as parameter (e.g. parameters in REST-like URLs, param | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `DSOMM-ACTIVITY-61E10F9CE1264FFAAF12FDBE0D0A831F` | Weak password test Weak passwords in components like applications or systems, specially for privileged accounts, lead to take over of that account. Automatic brute force attacks are performed. Special | conceito: Authentication And Federation Protocols (mechanism `ACM-IAT-001`) |
| `DSOMM-ACTIVITY-621FB6A55C0A4408826A068868BB031B` | Test cluster deployment resources The deployment configuration (e.g. kubernetes deployment resources) might contain unsecured configurations. Test the deployment configuration for virtualized environm | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `DSOMM-ACTIVITY-6532C1FE9D2342288722558DDABCA7D4` | Test for unused Resources Unused resources, specially secrets, might be still valid, but are exposing information. As an attacker, I compromise a system, gather credentials and try to use them. Test f | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |
| `DSOMM-ACTIVITY-65A2D7D9544146BFA4E3F76919857750` | Usage of different roles Parts of the service are not covered during the scan, because a login is not performed. Integration of authentication with all roles used in the service. For REST APIs, multip | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `DSOMM-ACTIVITY-67667C97C33E4306A4E5E7B1D8E10C5A` | High coverage of security related module and integration tests Vulnerabilities are rising due to code changes in a complex microservice environment in not important components. Implementation of secur | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `DSOMM-ACTIVITY-6A9CB3030F9848A8BDCD56D41C0012B8` | Coverage of hidden endpoints Hidden endpoints of the service are not getting tracked. Hidden endpoints are getting detected and included in the vulnerability scan. | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `DSOMM-ACTIVITY-6C05C8378C9946E2828B7C903E27DBA4` | Static analysis for important server side components Important parts in the source code of the middleware have vulnerabilities. Usage of static analysis tools for important parts of the middleware are | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `DSOMM-ACTIVITY-6D2C3AC68AFC4AF6A5E96188341ACA01` | Test network segmentation Wrong or no network segmentation of pods makes it easier for an attacker to access a database and extract or modify data. Cluster internal test needs to be performed. Integra | conceito: Trust-Boundary And DFD Modeling (mechanism `ACM-ATB-002`) |
| `DSOMM-ACTIVITY-6E180ABC7C984265B4E9852CB91B067B` | Local development security checks performed Creating and developing code contains code smells and quality issues. Integration of quality and linting plugins with interactive development environment (I | conceito: Secret Management Systems (mechanism `ACM-SPC-001`) |
| `DSOMM-ACTIVITY-73AAAE0B5D6849539FA4FD25BF665F2A` | Smoke Test During a deployment an error might happen which leads to non-availability of the system, a part of the system or a feature. Integration tests are performed against the production environmen | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `DSOMM-ACTIVITY-77FFC53E9F3D41F492D302F04F9B6B0F` | Patching mean time to resolution via production Without measuring Mean Time to Resolution (MTTR) related to patching, it is challenging to identify delays in the patching process. Unaddressed vulnerab | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |
| `DSOMM-ACTIVITY-79EF8103E1ED40558DF8FD2B2015BEBE` | Creation and application of a testing concept Scans might use a too small or too high test intensity. A testing concept considering the amount of time per scan/intensity is created and applied. A dyna | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `DSOMM-ACTIVITY-7A82020C94D1471CBBD35F7FE7DF4876` | Advanced visualization of defects Correlation of the vulnerabilities of different tools to have an overview of the the overall security level per component/project/team is not given. Findings are visu | conceito: Findings Workflow And Exception Governance (mechanism `ACM-TSV-004`) |
| `DSOMM-ACTIVITY-7BB7076493924462935DE55B2E148199` | Test of the configuration of cloud environments Standard hardening practices for cloud environments are not performed leading to vulnerabilities. With the help of tools the configuration of virtual en | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `DSOMM-ACTIVITY-7DE0AE33653845CD8222A1475647BA58` | Correlate known vulnerabilities in infrastructure with new image versions TODO. TODO | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |
| `DSOMM-ACTIVITY-837F8F90ADC24E6B9EBB60C2EE29494D` | Test for malware Third party might include malware. Ether due to the maintainer (e.g. typo squatting of an image name and using the wrong image) or by an attacker on behalf of the maintainer with stol | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |
| `DSOMM-ACTIVITY-845F06EC148C4C6797557041911DCCA5` | Coverage of sequential operations Sequential operations like workflows (e.g. login -> put products in the basket Sequential operations are defined and checked by the vulnerability scanner in the defin | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `DSOMM-ACTIVITY-85BA562384BE42198892808837BE582D` | Usage of a vulnerability management system For known vulnerabilities a processes to estimate the exploit ability of a vulnerability is recommended. To implement a security culture including training, | conceito: Threat Mitigation Linkage Controls (mechanism `ACM-TMR-005`) |
| `DSOMM-ACTIVITY-86D490B9D7984A5BA011AB9688014C46` | Patching mean time to resolution via PR Without measuring Mean Time to Resolution (MTTR) related to patching, it is challenging to identify delays in the patching process. Unaddressed vulnerabilities | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |
| `DSOMM-ACTIVITY-87B54313FAFD4860930F5EF132B3E4AD` | Test libyear Vulnerabilities in running artifacts stay for long and might get exploited. Test `libyear`, which provides a good insight how good patch management is. | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |
| `DSOMM-ACTIVITY-8F2B4D5A3C1E4B7A9D8F2E6C4A1B5D7F` | Artifact-based false positive treatment Artifact-based false positive treatment enables more granular control over finding suppression by linking decisions to specific code artifacts, container images | conceito: Findings Workflow And Exception Governance (mechanism `ACM-TSV-004`) |
| `DSOMM-ACTIVITY-8FC3DE677B8D420B8D24F35928CFED6E` | Test the definition of virtualized environments The definition of virtualized environments (e.g. via <i>Dockerfile</i>) might contain unsecure configurations. Test the definition of virtualized enviro | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `DSOMM-ACTIVITY-9711F871F79D45738D4FD2C98FD0D18E` | Coverage of client side dynamic components Parts of the service are not covered during the scan, because JavaScript is not getting executed. Therefore, the coverage of client-side dynamic components i | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `DSOMM-ACTIVITY-9CAC3341FE834079BEF2BFC4279EB594` | Treatment of defects with medium severity Vulnerabilities with severity middle are not visible. Vulnerabilities with severity middle are added to the quality gate. | conceito: Findings Workflow And Exception Governance (mechanism `ACM-TSV-004`) |
| `DSOMM-ACTIVITY-9E3A7C2F1B4D4E8AA5C67F2B9D1E3A8C` | Global false positive treatment Global false positive treatment allows (security) teams to make organization-wide decisions about specific vulnerabilities or finding patterns. When a finding is marked | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `DSOMM-ACTIVITY-A6C4CEFBA0B747878CC7A0F96B4B00D8` | Test for exposed services Standard network segmentation and firewalling has not been performed, leading to world open cluster management ports. With the help of tools the network configuration of unin | conceito: Boundary Mediation Controls (mechanism `ACM-ATB-003`) |
| `DSOMM-ACTIVITY-A8D7D1F1FC2449AB8FB6F3A03DA9C61D` | Dead code elimination Dead code increases the attack surface (use of hard coded credentials and variables, sensitive information) Collection of unused code and then manual removal of unused code. | conceito: Versioned Pipelines (mechanism `ACM-SCBI-001`) |
| `DSOMM-ACTIVITY-AAFFA73F59F64267B0AB732F3D13E90D` | Integration in development process Validating Findings by Security Engineers Pros: - Ensures accuracy and relevance of findings before they reach product teams - Reduces false positives, saving develo | conceito: Findings Workflow And Exception Governance (mechanism `ACM-TSV-004`) |
| `DSOMM-ACTIVITY-AB0A4B513B1843F1A6FCA98E4B28453D` | Default settings for intensity Time pressure and ignorance might lead to false predictions for the test intensity. The intensity of the used tools are not modified to save time. | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `DSOMM-ACTIVITY-AB5725AA4D5347B996DFC14B3FA93BCD` | Load tests As it is unknown how many requests the systems and applications can serve, due to an unexpected load the availability is disturbed. Load test against the production system or a production n | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `DSOMM-ACTIVITY-B2F776063E6C41E9B72D7C0B1D3D581D` | Treatment of all defects Vulnerabilities with severity low are not visible. All vulnerabilities are added to the quality gate. | conceito: Findings Workflow And Exception Governance (mechanism `ACM-TSV-004`) |
| `DSOMM-ACTIVITY-BC548CBACB824F76BD4B325D9D256279` | Number of vulnerabilities/severity Communication can be performed in a simple way, e.g. text based during the build process. This activity depends on at least one security testing implementation. Fail | conceito: Findings Workflow And Exception Governance (mechanism `ACM-TSV-004`) |
| `DSOMM-ACTIVITY-C1ACC8AF312E4503A817A26220C993A0` | Simple false positive treatment Security tests may produce false positives (or _"false alarms"_), findings that are incorrectly identified as vulnerabilities. It is important distinguish these from tr | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `DSOMM-ACTIVITY-C6E3C81256E241B0AE01B7AFC41A004C` | Test for stored secrets in code Stored secrets in git history or directly in code shouldn't exists because they might be exposed to unauthorized parties. Test for secrets in code and git history | conceito: Secret Management Systems (mechanism `ACM-SPC-001`) |
| `DSOMM-ACTIVITY-C922981B65ED40F3A94796FEE9A0125F` | Generation of response statistics No or delayed reaction to findings leads to potential exploitation of findings. Creation and response statistics (e.g. Mean Time to Resolution) of findings. This is a | conceito: Threat Mitigation Linkage Controls (mechanism `ACM-TMR-005`) |
| `DSOMM-ACTIVITY-CB6321AA0FBF49969E0805AB26EF4C1E` | Test for new image version When a new version of an image is available, it might fix security vulnerabilities. Check for new images of containers in production. | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |
| `DSOMM-ACTIVITY-CE970C9BDA9441CFBD788C15357B7E8E` | Integration of vulnerability issues into the development process To read console output of the build server to search for vulnerabilities might be difficult. Also, to check a vulnerability management | conceito: Threat Mitigation Linkage Controls (mechanism `ACM-TMR-005`) |
| `DSOMM-ACTIVITY-CF0D600E114D48879059D81C53805F0D` | Fix rate per repo/product Not communicating how many applications are adhering to SLAs based on the criticality of vulnerabilities can lead to delayed remediation of critical security issues, increasi | conceito: Findings Workflow And Exception Governance (mechanism `ACM-TSV-004`) |
| `DSOMM-ACTIVITY-D0BA0BE5C573405FB905B7A8F87A9CC7` | Coverage analysis Parts of the service are not still covered by tests. Check that there are no missing paths in the application with coverage-tools. | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `DSOMM-ACTIVITY-D17DBFF01F10492AB4C717BB59A0A711` | Exclusion of source code duplicates Duplicates in source code might influence the stability of the application. Automatic Detection and manual removal of duplicates in source code. | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `DSOMM-ACTIVITY-D5E6303CD5C64D59B258A3B9DE38A07F` | Test for stored secrets in build artifacts Stored secrets in container images or other build artifacts shouldn't exists because they might be exposed to unauthorized parties. Test for secrets in conta | conceito: Secret Management Systems (mechanism `ACM-SPC-001`) |
| `DSOMM-ACTIVITY-D918CD44A97243E9A974EFF3F4A5DCFE` | Software Composition Analysis (server side) Use a tool like trivy and concentrate on application related vulnerabilities. At this stage, ignore vulnerabilities in container base images used in the ser | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |
| `DSOMM-ACTIVITY-DCCF1949B9A84CE8B9926A4A7F3A623A` | Test for unauthorized installation Unapproved components are used. Components must be whitelisted. Regular scans on the docker infrastructure (e.g. cluster) need to be performed, to verify that only s | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |
| `DSOMM-ACTIVITY-DDFE7C3CB7A44CBA9041B044D4A34E5B` | Test for image lifetime Old container images in production indicate that patch management is not performed and therefore vulnerabilities might exists. Check the image age of containers in production. | conceito: Automated Security Scanners (mechanism `ACM-SCBI-002`) |
| `DSOMM-ACTIVITY-E237176BBEC5447DA926E37D6DD60E4B` | Static analysis for important client side components Important parts in the source code of the frontend have vulnerabilities. Usage of static analysis tools for important parts of the frontend are use | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `DSOMM-ACTIVITY-EB2C7F9DD0BD4253A2BACFF2ACE4A075` | Security unit tests for important components Vulnerabilities are rising due to code changes. Usage of unit tests to test important security related features like authentication and authorization. | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `DSOMM-ACTIVITY-EE68331F9B1D4F61844BB2EA04753A84` | Static analysis for all self written components Parts in the source code of the frontend or middleware have vulnerabilities. Usage of static analysis tools for all parts of the middleware and frontend | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `DSOMM-ACTIVITY-EFA52CC86C5C4BA2A3D27164B0402F34` | Stylistic analysis Unclear or obfuscated code might have unexpected behavior. Analysis of compliance to style guides of the source code ensures that source code formatting rules are met (e.g. indentat | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `DSOMM-ACTIVITY-F2F0F274C1A0450192FE7FC4452BC8AD` | Exploit likelihood estimation Severity-based vulnerability triage alone generates a lot false positives, requiring a more refined approach. Use the likelihood of exploitation by using *known exploited | conceito: Threat Mitigation Linkage Controls (mechanism `ACM-TMR-005`) |
| `DSOMM-ACTIVITY-F4FF841D3B2A45D9853E5EC7ECBCB054` | Static analysis for all components/libraries Used components like libraries and legacy applications might have vulnerabilities Usage of a static analysis for all used components. | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `DSOMM-ACTIVITY-F57D55F2DC054B349D1FF8CE5BFB0715` | Security integration tests for important components Vulnerabilities are rising due to code changes in a complex microservice environment. Implementation of essential security related integration tests | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |

---

## NIST SP 800-53 Rev. 5

**O que esta ES traz para este capítulo:** contribui 69 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `SP800-53-CA-1` | Develop, document, and disseminate to {{ insert: param, ca-1_prm_1 }}: {{ insert: param, ca-01_odp.03 }} assessment, authorization, and monitoring policy that: Procedures to facilitate the implementat | conceito: Governed Static Analysis Execution (practice `ACP-TSV-002`) |
| `SP800-53-CA-2` | Select the appropriate assessor or assessment team for the type of assessment to be conducted; Develop a control assessment plan that describes the scope of the assessment including: Controls and cont | conceito: Risk-Based Security Test Planning (practice `ACP-TSV-001`) |
| `SP800-53-CA-2.1` | Employ independent assessors or assessment teams to conduct control assessments. | conceito: Risk-Based Security Test Planning (practice `ACP-TSV-001`) |
| `SP800-53-CA-2.2` | Include as part of control assessments, {{ insert: param, ca-02.02_odp.01 }}, {{ insert: param, ca-02.02_odp.02 }}, {{ insert: param, ca-02.02_odp.03 }}. | conceito: Risk-Based Security Test Planning (practice `ACP-TSV-001`) |
| `SP800-53-CA-2.3` | Leverage the results of control assessments performed by {{ insert: param, ca-02.03_odp.01 }} on {{ insert: param, ca-02.03_odp.02 }} when the assessment meets {{ insert: param, ca-02.03_odp.03 }}. | conceito: Risk-Based Security Test Planning (practice `ACP-TSV-001`) |
| `SP800-53-CA-3` | Approve and manage the exchange of information between the system and other systems using {{ insert: param, ca-03_odp.01 }}; Document, as part of each exchange agreement, the interface characteristics | conceito: Trust Boundary And Integration Review (practice `ACP-ITS-001`) |
| `SP800-53-CA-3.1` | Unclassified National Security System Connections | conceito: Trust Boundary And Integration Review (practice `ACP-ITS-001`) |
| `SP800-53-CA-3.2` | Classified National Security System Connections | conceito: Trust Boundary And Integration Review (practice `ACP-ITS-001`) |
| `SP800-53-CA-3.3` | Unclassified Non-national Security System Connections | conceito: Trust Boundary And Integration Review (practice `ACP-ITS-001`) |
| `SP800-53-CA-3.4` | Connections to Public Networks | conceito: Trust Boundary And Integration Review (practice `ACP-ITS-001`) |
| `SP800-53-CA-3.5` | Restrictions on External System Connections | conceito: Trust Boundary And Integration Review (practice `ACP-ITS-001`) |
| `SP800-53-CA-3.6` | Verify that individuals or systems transferring data between interconnecting systems have the requisite authorizations (i.e., write permissions or privileges) prior to accepting such data. | conceito: Trust Boundary And Integration Review (practice `ACP-ITS-001`) |
| `SP800-53-CA-3.7` | Identify transitive (downstream) information exchanges with other systems through the systems identified in [CA-3a](#ca-3_smt.a) ; and Take measures to ensure that transitive (downstream) information | conceito: Trust Boundary And Integration Review (practice `ACP-ITS-001`) |
| `SP800-53-CA-4` | Security Certification | conceito: Reproducible Test Evidence Management (practice `ACP-TSV-004`) |
| `SP800-53-CA-5` | Develop a plan of action and milestones for the system to document the planned remediation actions of the organization to correct weaknesses or deficiencies noted during the assessment of the controls | conceito: Findings Triage, SLA And Retest Closure (practice `ACP-TSV-003`) |
| `SP800-53-CA-5.1` | Ensure the accuracy, currency, and availability of the plan of action and milestones for the system using {{ insert: param, ca-05.01_odp }}. | conceito: Findings Triage, SLA And Retest Closure (practice `ACP-TSV-003`) |
| `SP800-53-CA-6` | Assign a senior official as the authorizing official for the system; Assign a senior official as the authorizing official for common controls available for inheritance by organizational systems; Ensur | conceito: DFD And Trust-Boundary Grounding (practice `ACP-TMR-002`) |
| `SP800-53-CA-6.1` | Employ a joint authorization process for the system that includes multiple authorizing officials from the same organization conducting the authorization. | conceito: DFD And Trust-Boundary Grounding (practice `ACP-TMR-002`) |
| `SP800-53-CA-6.2` | Employ a joint authorization process for the system that includes multiple authorizing officials with at least one authorizing official from an organization external to the organization conducting the | conceito: DFD And Trust-Boundary Grounding (practice `ACP-TMR-002`) |
| `SP800-53-CA-7` | Develop a system-level continuous monitoring strategy and implement continuous monitoring in accordance with the organization-level continuous monitoring strategy that includes: Establishing the follo | conceito: Risk-Based Security Test Planning (practice `ACP-TSV-001`) |
| `SP800-53-CA-7.1` | Employ independent assessors or assessment teams to monitor the controls in the system on an ongoing basis. | conceito: Risk-Based Security Test Planning (practice `ACP-TSV-001`) |
| `SP800-53-CA-7.2` | Types of Assessments | conceito: Risk-Based Security Test Planning (practice `ACP-TSV-001`) |
| `SP800-53-CA-7.3` | Employ trend analyses to determine if control implementations, the frequency of continuous monitoring activities, and the types of activities used in the continuous monitoring process need to be modif | conceito: Risk-Based Security Test Planning (practice `ACP-TSV-001`) |
| `SP800-53-CA-7.4` | Ensure risk monitoring is an integral part of the continuous monitoring strategy that includes the following: Effectiveness monitoring; Compliance monitoring; and Change monitoring. | conceito: Risk-Based Security Test Planning (practice `ACP-TSV-001`) |
| `SP800-53-CA-7.5` | Employ the following actions to validate that policies are established and implemented controls are operating in a consistent manner: {{ insert: param, ca-7.5_prm_1 }}. | conceito: Risk-Based Security Test Planning (practice `ACP-TSV-001`) |
| `SP800-53-CA-7.6` | Ensure the accuracy, currency, and availability of monitoring results for the system using {{ insert: param, ca-07.06_odp }}. | conceito: Risk-Based Security Test Planning (practice `ACP-TSV-001`) |
| `SP800-53-CA-8` | Conduct penetration testing {{ insert: param, ca-08_odp.01 }} on {{ insert: param, ca-08_odp.02 }}. | conceito: Specialized Empirical Testing (practice `ACP-TSV-006`) |
| `SP800-53-CA-8.1` | Employ an independent penetration testing agent or team to perform penetration testing on the system or system components. | conceito: Specialized Empirical Testing (practice `ACP-TSV-006`) |
| `SP800-53-CA-8.2` | Employ the following red-team exercises to simulate attempts by adversaries to compromise organizational systems in accordance with applicable rules of engagement: {{ insert: param, ca-08.02_odp }}. | conceito: Specialized Empirical Testing (practice `ACP-TSV-006`) |
| `SP800-53-CA-8.3` | Employ a penetration testing process that includes {{ insert: param, ca-08.03_odp.01 }} {{ insert: param, ca-08.03_odp.02 }} attempts to bypass or circumvent controls associated with physical access p | conceito: Specialized Empirical Testing (practice `ACP-TSV-006`) |
| `SP800-53-CA-9` | Authorize internal connections of {{ insert: param, ca-09_odp.01 }} to the system; Document, for each internal connection, the interface characteristics, security and privacy requirements, and the nat | conceito: Trust Boundary And Integration Review (practice `ACP-ITS-001`) |
| `SP800-53-CA-9.1` | Perform security and privacy compliance checks on constituent system components prior to the establishment of the internal connection. | conceito: Trust Boundary And Integration Review (practice `ACP-ITS-001`) |
| `SP800-53-CP-10.1` | Contingency Plan Testing | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `SP800-53-CP-4` | Test the contingency plan for the system {{ insert: param, cp-04_odp.01 }} using the following tests to determine the effectiveness of the plan and the readiness to execute the plan: {{ insert: param, | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `SP800-53-CP-4.1` | Coordinate contingency plan testing with organizational elements responsible for related plans. | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `SP800-53-CP-4.2` | Test the contingency plan at the alternate processing site: To familiarize contingency personnel with the facility and available resources; and To evaluate the capabilities of the alternate processing | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `SP800-53-CP-4.3` | Test the contingency plan using {{ insert: param, cp-04.03_odp }}. | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `SP800-53-CP-4.4` | Include a full recovery and reconstitution of the system to a known state as part of contingency plan testing. | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `SP800-53-CP-6.3` | Identify potential accessibility problems to the alternate storage site in the event of an area-wide disruption or disaster and outline explicit mitigation actions. | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `SP800-53-CP-7.2` | Identify potential accessibility problems to alternate processing sites in the event of an area-wide disruption or disaster and outlines explicit mitigation actions. | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `SP800-53-CP-8.4` | Require primary and alternate telecommunications service providers to have contingency plans; Review provider contingency plans to ensure that the plans meet organizational contingency requirements; a | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `SP800-53-CP-8.5` | Test alternate telecommunication services {{ insert: param, cp-08.05_odp }}. | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `SP800-53-CP-9.2` | Use a sample of backup information in the restoration of selected system functions as part of contingency plan testing. | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `SP800-53-IR-3` | Test the effectiveness of the incident response capability for the system {{ insert: param, ir-03_odp.01 }} using the following tests: {{ insert: param, ir-03_odp.02 }}. | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `SP800-53-IR-3.1` | Test the incident response capability using {{ insert: param, ir-03.01_odp }}. | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `SP800-53-IR-3.2` | Coordinate incident response testing with organizational elements responsible for related plans. | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `SP800-53-IR-3.3` | Use qualitative and quantitative data from testing to: Determine the effectiveness of incident response processes; Continuously improve incident response processes; and Provide incident response measu | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `SP800-53-MA-3` | Approve, control, and monitor the use of system maintenance tools; and Review previously approved system maintenance tools {{ insert: param, ma-03_odp }}. | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `SP800-53-MA-3.2` | Check media containing diagnostic and test programs for malicious code before the media are used in the system. | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `SP800-53-MA-3.6` | Inspect maintenance tools to ensure the latest software updates and patches are installed. | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `SP800-53-MA-4.1` | Log {{ insert: param, ma-4.1_prm_1 }} for nonlocal maintenance and diagnostic sessions; and Review the audit records of the maintenance and diagnostic sessions to detect anomalous behavior. | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `SP800-53-MP-6.1` | Review, approve, track, document, and verify media sanitization and disposal actions. | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `SP800-53-MP-6.2` | Test sanitization equipment and procedures {{ insert: param, mp-6.2_prm_1 }} to ensure that the intended sanitization is being achieved. | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `SP800-53-MP-8.2` | Test downgrading equipment and procedures {{ insert: param, mp-8.2_prm_1 }} to ensure that downgrading actions are being achieved. | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `SP800-53-PE-3.6` | Facility Penetration Testing | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `SP800-53-PE-6` | Monitor physical access to the facility where the system resides to detect and respond to physical security incidents; Review physical access logs {{ insert: param, pe-06_odp.01 }} and upon occurrence | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `SP800-53-PE-6.3` | Employ video surveillance of {{ insert: param, pe-06.03_odp.01 }}; Review video recordings {{ insert: param, pe-06.03_odp.02 }} ; and Retain video recordings for {{ insert: param, pe-06.03_odp.03 }}. | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `SP800-53-PE-8` | Maintain visitor access records to the facility where the system resides for {{ insert: param, pe-08_odp.01 }}; Review visitor access records {{ insert: param, pe-08_odp.02 }} ; and Report anomalies i | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `SP800-53-PE-8.1` | Maintain and review visitor access records using {{ insert: param, pe-8.1_prm_1 }}. | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `SP800-53-PL-4` | Establish and provide to individuals requiring access to the system, the rules that describe their responsibilities and expected behavior for information and system usage, security, and privacy; Recei | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `SP800-53-PL-7` | Develop a Concept of Operations (CONOPS) for the system describing how the organization intends to operate the system from the perspective of information security and privacy; and Review and update th | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `SP800-53-PM-11` | Define organizational mission and business processes with consideration for information security and privacy and the resulting risk to organizational operations, organizational assets, individuals, ot | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `SP800-53-PM-14` | Implement a process for ensuring that organizational plans for conducting security and privacy testing, training, and monitoring activities associated with organizational systems: Are developed and ma | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `SP800-53-PM-17` | Establish policy and procedures to ensure that requirements for the protection of controlled unclassified information that is processed, stored or transmitted on external systems, are implemented in a | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `SP800-53-PM-22` | Develop and document organization-wide policies and procedures for: Reviewing for the accuracy, relevance, timeliness, and completeness of personally identifiable information across the information li | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `SP800-53-PM-25` | Develop, document, and implement policies and procedures that address the use of personally identifiable information for internal testing, training, and research; Limit or minimize the amount of perso | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `SP800-53-PM-26` | Implement a process for receiving and responding to complaints, concerns, or questions from individuals about the organizational security and privacy practices that includes: Mechanisms that are easy | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `SP800-53-PS-2` | Assign a risk designation to all organizational positions; Establish screening criteria for individuals filling those positions; and Review and update position risk designations {{ insert: param, ps-0 | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `SP800-53-PS-6` | Develop and document access agreements for organizational systems; Review and update the access agreements {{ insert: param, ps-06_odp.01 }} ; and Verify that individuals requiring access to organizat | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |

---

## CIS Controls v8.1.2

**O que esta ES traz para este capítulo:** contribui 24 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `CIS-14.1` | Establish and maintain a security awareness program. The purpose of a security awareness program is to educate the enterprise’s workforce on how to interact with enterprise assets and data in a secure | conceito: Reviewer Accountability And Consistency Gates (mechanism `ACM-TMR-006`) |
| `CIS-16` | Manage the security life cycle of in-house developed, hosted, or acquired software to prevent, detect, and remediate security weaknesses before they can impact the enterprise. | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `CIS-16.1` | Apply secure design principles in application architectures. Secure design principles include the concept of least privilege and enforcing mediation to validate every operation that the user makes, pr | conceito: Structured Threat Analysis Frameworks (mechanism `ACM-TMR-002`) |
| `CIS-16.1` | Apply secure design principles in application architectures. Secure design principles include the concept of least privilege and enforcing mediation to validate every operation that the user makes, pr | conceito: Structured Threat Analysis Frameworks (mechanism `ACM-TMR-002`) |
| `CIS-16.11` | Leverage vetted modules or services for application security components, such as identity management, encryption, auditing, and logging. Using platform features in critical security functions will red | conceito: Approved Source And Registry Governance (practice `ACP-SCBI-003`) |
| `CIS-16.12` | Apply static and dynamic analysis tools within the application life cycle to verify that secure coding practices are being followed. | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `CIS-16.13` | Conduct application penetration testing. For critical applications, authenticated penetration testing is better suited to finding business logic vulnerabilities than code scanning and automated securi | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `CIS-16.14` | Conduct threat modeling. Threat modeling is the process of identifying and addressing application security design flaws within a design, before code is created. It is conducted through specially train | conceito: Structured Threat Analysis Frameworks (mechanism `ACM-TMR-002`) |
| `CIS-16.2` | Establish and maintain a process to accept and address reports of software vulnerabilities, including providing a means for external entities to report. The process is to include such items as: a vuln | conceito: Findings Workflow And Exception Governance (mechanism `ACM-TSV-004`) |
| `CIS-16.3` | Perform root cause analysis on security vulnerabilities. When reviewing vulnerabilities, root cause analysis is the task of evaluating underlying issues that create vulnerabilities in code, and allows | conceito: Threat Model Versioning Controls (mechanism `ACM-TMR-003`) |
| `CIS-16.4` | Establish and manage an updated inventory of third-party components used in development, often referred to as a “bill of materials,” as well as components slated for future use. This inventory is to i | conceito: Build And Image Inventory Generation (mechanism `ACM-SCBI-005`) |
| `CIS-16.5` | Use up-to-date and trusted third-party software components. When possible, choose established and proven frameworks and libraries that provide adequate security. Acquire these components from trusted | conceito: Approved Source And Registry Governance (practice `ACP-SCBI-003`) |
| `CIS-16.6` | Establish and maintain a severity rating system and process for application vulnerabilities that facilitates prioritizing the order in which discovered vulnerabilities are fixed. This process includes | conceito: Threat Mitigation Linkage Controls (mechanism `ACM-TMR-005`) |
| `CIS-16.7` | Use standard, industry-recommended hardening configuration templates for application infrastructure components. This includes underlying servers, databases, and web servers, and applies to cloud conta | conceito: End-to-End Deploy Traceability (practice `ACP-RPR-004`) |
| `CIS-16.8` | Maintain separate environments for production and non-production systems. | conceito: Trust-Boundary And DFD Modeling (mechanism `ACM-ATB-002`) |
| `CIS-16.9` | Ensure that all software development personnel receive training in writing secure code for their specific development environment and responsibilities. Training can include general security principles | conceito: Schema And Contract Validators (mechanism `ACM-IVF-003`) |
| `CIS-17.7` | Plan and conduct routine incident response exercises and scenarios for key personnel involved in the incident response process to prepare for responding to real-world incidents. Exercises need to test | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `CIS-17.9` | Establish and maintain security incident thresholds, including, at a minimum, differentiating between an incident and an event. Examples can include: abnormal activity, security vulnerability, securit | conceito: Critical Event Catalog Governance (practice `ACP-SLG-001`) |
| `CIS-18` | Test the effectiveness and resiliency of enterprise assets through identifying and exploiting weaknesses in controls (people, processes, and technology), and simulating the objectives and actions of a | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `CIS-18.1` | Establish and maintain a penetration testing program appropriate to the size, complexity, industry, and maturity of the enterprise. Penetration testing program characteristics include scope, such as n | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `CIS-18.2` | Perform periodic external penetration tests based on program requirements, no less than annually. External penetration testing must include enterprise and environmental reconnaissance to detect exploi | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `CIS-18.3` | Remediate penetration test findings based on the enterprise’s documented vulnerability remediation process. This should include determining a timeline and level of effort based on the impact and prior | conceito: Findings Workflow And Exception Governance (mechanism `ACM-TSV-004`) |
| `CIS-18.4` | Validate security measures after each penetration test. If deemed necessary, modify rulesets and capabilities to detect the techniques used during testing. | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `CIS-18.5` | Perform periodic internal penetration tests based on program requirements, no less than annually. The testing may be clear box or opaque box. | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |

---

## OWASP SAMM v2.1

**O que esta ES traz para este capítulo:** contribui 24 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `SAMM-ACTIVITY-V_RT_1_A` | Test the effectiveness of security controls Verified effectiveness of your standard security controls Test for software security controls. Conduct security tests to verify that the standard software s | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `SAMM-ACTIVITY-V_RT_1_B` | Perform fuzz testing Insight into behaviour of your applications when dealing with unexpected input Perform security fuzzing testing. Perform fuzzing, sending random or malformed data to the test subj | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `SAMM-ACTIVITY-V_RT_2_A` | Define and run security test cases from requirements Integration of security requirements into test scenarios Derive test cases from known security requirements. From the security requirements, identi | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `SAMM-ACTIVITY-V_RT_2_B` | Define and run security abuse cases from requirements Detection of application business logic flaws Create and test abuse cases and business logic flaw test. Misuse and abuse cases describe unintended | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `SAMM-ACTIVITY-V_RT_3_A` | Automate security requirements testing Timely and reliable detection of violations to security requirements Perform regression testing (with security unit tests). Write and automate regression tests f | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `SAMM-ACTIVITY-V_RT_3_B` | Perform security stress testing Transparency of resilience against denial of service attacks Denial of service and security stress testing. Applications are particularly susceptible to denial of servi | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `SAMM-ACTIVITY-V_ST_1_A` | Perform automated security testing Detection of common easy-to-find vulnerabilities Utilize automated security testing tools. Use automated static and dynamic security test tools for software, resulti | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `SAMM-ACTIVITY-V_ST_1_B` | Test high risk application components manually Detection of manually identifiable vulnerabilities in critical components Perform manual security testing of high-risk components. Perform selective manu | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `SAMM-ACTIVITY-V_ST_2_A` | Develop application-specific security test cases Detection of organization-specific easy-to-find vulnerabilities Employ application-specific security testing automation. Increase the effectiveness of | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `SAMM-ACTIVITY-V_ST_2_B` | Establish a penetration testing process Understanding of application resilience from black-box perspective Conduct manual penetration testing. Using the set of security test cases identified for each | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `SAMM-ACTIVITY-V_ST_3_A` | Integrate security testing tools in the delivery pipeline Identification of automatically identifiable vulnerabilities in earliest possible stages Integrate automated security testing into the build a | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `SAMM-ACTIVITY-V_ST_3_B` | Establish continuous, scalable security verification Identification of manually identifiable security issues in earliest possible stages Integrate security testing into development process. Integrate | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `SAMM-FUNCTION-VERIFICATION` | Verification Verification focuses on the processes and activities related to how an organization checks and tests artifacts produced throughout software development. This typically includes quality as | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `SAMM-PRACTICE-LEVEL-V_RT_1` | V-RT-1 Requirements-driven Testing L1 Opportunistically find basic vulnerabilities and other security issues. | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `SAMM-PRACTICE-LEVEL-V_RT_3` | V-RT-3 Requirements-driven Testing L3 Maintain the application security level after bug fixes, changes or during maintenance. | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `SAMM-PRACTICE-LEVEL-V_ST_1` | V-ST-1 Security Testing L1 Perform security testing (both manual and tool based) to discover security defects. | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `SAMM-PRACTICE-LEVEL-V_ST_2` | V-ST-2 Security Testing L2 Make security testing during development more complete and efficient through automation complemented with regular manual security penetration tests. | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `SAMM-PRACTICE-LEVEL-V_ST_3` | V-ST-3 Security Testing L3 Embed security testing as part of the development and deployment processes. | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `SAMM-PRACTICE-V_AA` | V-AA Architecture Assessment This practice focuses on validating the security and compliance of the software and supporting infrastructure architecture. The Architecture Assessment (AA) practice ensur | conceito: Architecture Review Gates (mechanism `ACM-ATB-004`) |
| `SAMM-PRACTICE-V_RT` | V-RT Requirements-driven Testing This practice focuses on using both positive (control verification) and negative (misuse/abuse testing) security tests based on requirements (user stories). The goal o | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `SAMM-PRACTICE-V_ST` | V-ST Security Testing This practice focuses on the detection and resolution of basic security issues through automation, allowing manual testing to focus on more complex attack vectors. The Security T | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `SAMM-STREAM-V_RT_A` | V-RT-A Control Verification Control Verification validates that security controls and requirements are met through testing derived from requirements, and prevents the introduction of bugs into later r | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `SAMM-STREAM-V_RT_B` | V-RT-B Misuse/Abuse Testing Misuse/Abuse Testing leverages fuzzing, misuse/abuse cases, and the identification of any functionality or resources in the software that can be abused in order to identify | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |
| `SAMM-STREAM-V_ST_B` | V-ST-B Deep Understanding Deep understanding focuses on performing manual security testing of high-risk components, using complex attack vectors with the goal of making advanced security testing an in | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |

---

## PCI DSS v4.0.1

**O que esta ES traz para este capítulo:** contribui 17 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `PCI-11.1.1` | All security policies and operational 11.1.1 Examine documentation and interview and maintaining the various policies and | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `PCI-11.1.2` | Roles and responsibilities for performing 11.1.2.a Examine documentation to verify that assigned, personnel may not be aware of their | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `PCI-11.2.1` | Authorized and unauthorized wireless access 11.2.1.a Examine policies and procedures to verify technology within a network are common paths | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `PCI-11.2.2` | An inventory of authorized wireless access 11.2.2 Examine documentation to verify that an can help administrators quickly respond when | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `PCI-11.3.1` | Internal vulnerability scans are performed as 11.3.1.a Examine internal scan report results from reduces the likelihood of a vulnerability being | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `PCI-11.3.2` | External vulnerability scans are performed as 11.3.2.a Examine ASV scan reports from the last vulnerable externally facing servers, which can be | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `PCI-11.4.1` | A penetration testing methodology is defined, 11.4.1 Examine documentation and interview internal vulnerabilities to leverage to obtain | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `PCI-11.4.2` | Internal penetration testing is performed: 11.4.2.a Examine the scope of work and results Firstly, just like an external penetration test, it | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `PCI-11.4.3` | External penetration testing is performed: 11.4.3.a Examine the scope of work and results penetration test that found nothing is typically | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `PCI-11.4.4` | Exploitable vulnerabilities and security 11.4.4 Examine penetration testing results to verify prioritized list of vulnerabilities discovered by the | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `PCI-11.4.5` | If segmentation is used to isolate the CDE 11.4.5.a Examine segmentation controls and isolate the CDE from internal untrusted networks, | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `PCI-11.4.6` | Additional requirement for service 11.4.6.a Additional testing procedure for volumes of cardholder data or can provide an | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `PCI-11.4.7` | Additional requirement for multi-tenant 11.4.7 Additional testing procedure for multi- accordance with PCI DSS to simulate attacker | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `PCI-11.5.1` | Intrusion-detection and/or intrusion- 11.5.1.a Examine system configurations and techniques (such as IDS/IPS) compare the traffic | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `PCI-11.5.2` | A change-detection mechanism (for example, 11.5.2.a Examine system settings, monitored files, content files can be an indicator an attacker has | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `PCI-11.6.1` | A change- and tamper-detection mechanism 11.6.1.a Examine system settings, monitored including active content (primarily JavaScript), | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `PCI-REQ-11` | Requirement 11: Test Security of Systems and Networks Regularly. Goal: Regularly Monitor and Test Networks. | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |

---

## SAFECode — Practical Security Stories and Tasks for Agile Development (2012)

**O que esta ES traz para este capítulo:** contribui 13 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `SCAGILE-EXP-10` | Prioritization of resolution of issues identified by code analysis tools (static and run-time), especially for existing code | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `SCAGILE-EXP-2` | Security fix/patch validation checking completeness and strength of fixes | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `SCAGILE-EXP-4` | Conduct penetration tests on the software around beta stage | conceito: Static Analysis Profile Management (mechanism `ACM-TSV-005`) |
| `SCAGILE-EXP-5` | Enhance existing test suite to include security test cases | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `SCAGILE-EXP-6` | Perform file fuzz testing | conceito: Static Analysis Profile Management (mechanism `ACM-TSV-005`) |
| `SCAGILE-EXP-7` | Perform network fuzz testing | conceito: Static Analysis Profile Management (mechanism `ACM-TSV-005`) |
| `SCAGILE-OPS-1` | Configure bug tracking to track security vulnerabilities as a requirement for software development team | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `SCAGILE-OPS-10` | Perform and add to testing cycle automated vulnerability scanner (OS and web as appropriate) | conceito: Test Execution Surfaces (mechanism `ACM-TSV-002`) |
| `SCAGILE-OPS-16` | Ensure security fixes are verified by security experts before committing them | conceito: Test Execution Surfaces (mechanism `ACM-TSV-002`) |
| `SCAGILE-OPS-2` | Verify security POCs and plan for fixes as recommendation for software development team | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `SCAGILE-OPS-4` | Resolve critical and high severity issues identified by static code analysis tools | conceito: Test Execution Surfaces (mechanism `ACM-TSV-002`) |
| `SCAGILE-OPS-7` | Perform stricter code review of risky code categories (network listeners, privileged code, input validation, etc.) | conceito: Test Execution Surfaces (mechanism `ACM-TSV-002`) |
| `SCAGILE-OPS-9` | Continuously verify coverage of static code analysis tools for new and existing code | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |

---

## PCI Secure SLC v1.1

**O que esta ES traz para este capítulo:** contribui 9 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `PCISSLC-2.4` | Security assurance processes defined, implemented and maintained; checkpoints throughout SDLC | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `PCISSLC-2.5` | Evidence generated for each process to illustrate it results in expected security outcomes; frequently collected and kept up to date | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `PCISSLC-2.6` | Mature process to detect weak or ineffective assurance processes; criteria for determining weakness defined; processes updated when weak | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `PCISSLC-3.4` | Mature process to identify weak or ineffective controls; criteria defined; monitoring throughout lifecycle; controls updated timely | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `PCISSLC-4.1` | Mature process for security testing; tools appropriate for software architecture; testing throughout lifecycle including third-party; results inventoried | conceito: Test Execution Surfaces (mechanism `ACM-TSV-002`) |
| `PCISSLC-4.2` | Process for distributing fixes and preventing reintroduction; criticality criteria defined; decisions to not fix approved and justified | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `PCISSLC-9.1` | Bidirectional communication channels for security issues; stakeholders can report issues and receive timely updates; resources to respond | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `PCISSLC-9.2` | Mature process exists to notify stakeholders about security updates in a timely manner | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `PCISSLC-9.3` | Instructions for mitigating threat or reducing impact when timely patch not available; risk mitigation provided to stakeholders | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |

---

## NIST SSDF (SP 800-218 v1.1)

**O que esta ES traz para este capítulo:** contribui 9 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `SSDF-PRACTICE-PO.4` | Help ensure that the software resulting from the SDLC meets the organization’s expectations by defining and using criteria for checking the software’s security during development. | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `SSDF-PRACTICE-PW.7` | Help identify vulnerabilities so that they can be corrected before the software is released to prevent exploitation. Using automated methods lowers the effort and resources needed to detect vulnerabil | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `SSDF-PRACTICE-PW.8` | Help identify vulnerabilities so that they can be corrected before the software is released in order to prevent exploitation. Using automated methods lowers the effort and resources needed to detect v | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `SSDF-TASK-PO.4.1` | Define criteria for software security checks and track throughout t he SDLC. | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `SSDF-TASK-PO.4.2` | Implement processes, mechanisms, etc. to gather and safeguard the necessary information in support of the criteria. | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `SSDF-TASK-PW.7.1` | Determine whether code review (a person looks directly at the code to find issues) and/or code analysis (tools are used to find issues in code, either in a fully automated way or in conjunction with a | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `SSDF-TASK-PW.7.2` | Perform the code review and/or code analysis based on the organization’s secure coding standards, and record and triage all discovered issues and recommended remediations in the development team’s wor | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `SSDF-TASK-PW.8.1` | Determine whether executable code testing should be performed to find vulnerabilities not identified by previous reviews, analysis, or testing and, if so, which types of testing should be used. | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `SSDF-TASK-PW.8.2` | Scope the testing, d esign the tests, perform the testing, and document the results, including record ing and triaging all discovered issues and recommended remediations in the development team’s work | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |

---

## EU Digital Operational Resilience Act (DORA)

**O que esta ES traz para este capítulo:** contribui 5 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `DORA-ART-15` | Article 15 of Digital Operational Resilience Act | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `DORA-ART-24` | Article 24 of Digital Operational Resilience Act (Regulation (EU) 2022/2554). See validation passes in knowledge-graph working notes for detailed analysis. | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `DORA-ART-26` | Article 26 of Digital Operational Resilience Act (Regulation (EU) 2022/2554). See validation passes in knowledge-graph working notes for detailed analysis. | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |
| `DORA-ART-27` | Article 27 of Digital Operational Resilience Act | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `DORA-ART-29` | Article 29 of Digital Operational Resilience Act (Regulation (EU) 2022/2554). See validation passes in knowledge-graph working notes for detailed analysis. | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |

---

## SAFECode — Fundamental Practices for Secure Software Development (2018)

**O que esta ES traz para este capítulo:** contribui 5 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `SCFPSSD-FINDINGS` | Security finding severity definition and risk acceptance process | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `SCFPSSD-FIX-VULN` | Process for fixing identified vulnerabilities and providing patches | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `SCFPSSD-MITIGATIONS` | When fixes unavailable, identify mitigations and workarounds for stakeholders | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |
| `SCFPSSD-TESTING` | Automated testing (SAST, DAST, fuzzing) and manual testing (pen testing, code review) practices | conceito: Test Execution Surfaces (mechanism `ACM-TSV-002`) |
| `SCFPSSD-VULN-RESPONSE` | Internal/external policies, roles, reporter management, fix process, disclosure, lifecycle feedback | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |

---

## OWASP ASVS v5.0.0

**O que esta ES traz para este capítulo:** contribui 1 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `ASVS-REQ-V1.4.2` | Verify that sign, range, and input validation techniques are used to prevent integer overflows. | conceito: Testes de segurança e validação empírica (slice `ACO-TSV`) |

---

## EU Cyber Resilience Act (CRA)

**O que esta ES traz para este capítulo:** contribui 1 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `CRA-ART-18` | Article 18 of Cyber Resilience Act | conceito: CI/CD Gate And Release Promotion (mechanism `ACM-TSV-003`) |

---

## EU NIS2 Directive

**O que esta ES traz para este capítulo:** contribui 1 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `NIS2-ART-22` | Article 22 of Network and Information Security Directive (Directive (EU) 2022/2555). See validation passes in knowledge-graph working notes for detailed analysis. | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |

---

## EU GDPR (RGPD)

**O que esta ES traz para este capítulo:** contribui 1 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `GDPR-ART-28` | Article 28 of General Data Protection Regulation (Regulation (EU) 2016/679). See validation passes in knowledge-graph working notes for detailed analysis. | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |

---

## HIPAA Security Rule

**O que esta ES traz para este capítulo:** contribui 1 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `HIPAA-164-308a8` | Evaluation — Administrative Safeguard under HIPAA Security Rule §164.308(a)(8). | conceito: Integrated Security Scanners (mechanism `ACM-TSV-001`) |

---

## SAFECode — Software Integrity Controls (2010)

**O que esta ES traz para este capítulo:** contribui 1 referência(s) que apoiam o domínio coberto neste capítulo. Cada linha da tabela abaixo identifica a referência externa, descreve-a sucintamente e aponta para o doc ou conceito do manual onde o tema é tratado.

| Referência externa | Descrição | Doc/conceito do manual |
|---|---|---|
| `SCSIC-DEV-TESTING` | SAST, DAST, binary analysis, malware detection, compliance validation, code coverage; peer review for both security and integrity | conceito: Test Execution Surfaces (mechanism `ACM-TSV-002`) |

---


<!-- WAVE-NOTE: **Nota Wave 3 ACO-TSV:** esta leitura funciona como âncora bounded para os rows autorizados de vulnerability scanning, penetration testing, retesting, methodology wrappers, lifecycle / strategy testing e requirement-header packaging que o freeze de Wave 3 reteve em `ACO-TSV`. A leitura permanece **bounded**, mantém o Cap. `04` apenas para os edges de empirical assurance architecture-heavy e wireless / segmentation support, mantém o Cap. `02` apenas como scaffold de requisitos e rastreabilidade para TLS / configuration verification e requirement support, mantém o Cap. `14` apenas como suporte de governação / periodic evaluation wrappers, não força qualquer uso de Cap. `06` ou `13`, e não converte `ASVS v4`, `CIS`, `HIPAA`, `NIST`, `DSOMM` ou `PCI` em autoridade family-blind de testing. -->
