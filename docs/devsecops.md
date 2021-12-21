# Security and DevSecOps. Container Security
- [Introduction](#introduction)
- [Kubernetes Security Compliance Frameworks](#kubernetes-security-compliance-frameworks)
- [Zero Trust Security](#zero-trust-security)
- [Authentication and Authorization](#authentication-and-authorization)
- [Quality Gates](#quality-gates)
- [16 Gates](#16-gates)
- [Kubernetes Threat Modelling](#kubernetes-threat-modelling)
- [Kubernetes Config Security Threats](#kubernetes-config-security-threats)
- [Security Linting on Kubernetes](#security-linting-on-kubernetes)
- [IaC and Security](#iac-and-security)
- [Multi-Level Security (MLS) vs Multi-Category Security (MCS). Make Secure Pipelines with Podman and Containers](#multi-level-security-mls-vs-multi-category-security-mcs-make-secure-pipelines-with-podman-and-containers)
- [Project Calico](#project-calico)
- [The Falco Project](#the-falco-project)
- [Security Patterns for Microservice Architectures](#security-patterns-for-microservice-architectures)
- [Anchore Container Security Solutions for DevSecOps](#anchore-container-security-solutions-for-devsecops)
- [Twistlock and Threat Stack Container Security](#twistlock-and-threat-stack-container-security)
- [OWASP](#owasp)
- [Source Code Audit](#source-code-audit)
- [StackRox](#stackrox)
- [Secure Container Based CI/CD Workflows. Vulnerability Scanner for Container Images](#secure-container-based-cicd-workflows-vulnerability-scanner-for-container-images)
	- [Securing Kubernetes With Anchore](#securing-kubernetes-with-anchore)
	- [Secure Containers with Notary or Cosign](#secure-containers-with-notary-or-cosign)
- [GitHub security](#github-security)
- [Databases in DMZ and Intranet](#databases-in-dmz-and-intranet)
- [Removing Credentials From Git Repo](#removing-credentials-from-git-repo)
- [Pentesting](#pentesting)
- [SQL Injection](#sql-injection)
- [Credential Managers](#credential-managers)
	- [keycloak](#keycloak)
	- [Git Credential Manager Core](#git-credential-manager-core)
- [Secrets Management](#secrets-management)
	- [AWS Secret Manager](#aws-secret-manager)
	- [Password Hashing](#password-hashing)
	- [Store private data in git repo](#store-private-data-in-git-repo)
	- [HashiCorp Vault](#hashicorp-vault)
		- [HashiCorp Vault Agent](#hashicorp-vault-agent)
	- [Azure Key Vault](#azure-key-vault)
	- [CyberArk and Ansible](#cyberark-and-ansible)
	- [CyberArk Conjur](#cyberark-conjur)
	- [SOPS for Kubernetes](#sops-for-kubernetes)
	- [Alternatives with Kubernetes External Secrets](#alternatives-with-kubernetes-external-secrets)
- [Serverless Security Best Practices](#serverless-security-best-practices)
- [Docker Images & Container Security](#docker-images--container-security)
	- [Sigstore](#sigstore)
	- [Container security best practices](#container-security-best-practices)
- [Pod Security Policies](#pod-security-policies)
- [Kubernetes Network Policies](#kubernetes-network-policies)
- [Static Analysis SAST](#static-analysis-sast)
- [Kubernetes Security Tools](#kubernetes-security-tools)
- [Helm Charts Security. Helm Secrets](#helm-charts-security-helm-secrets)
- [Password Recovery](#password-recovery)
- [Attacks on Kubernetes via Misconfigured Argo Workflows](#attacks-on-kubernetes-via-misconfigured-argo-workflows)
- [Books](#books)
- [CVEs](#cves)
	- [Log4j Log4Shell](#log4j-log4shell)
- [Powershell](#powershell)
- [Let's Encrypt SSL certificates](#lets-encrypt-ssl-certificates)
- [More Security Tools](#more-security-tools)

## Introduction
- [fiercesw.com: DevOps vs DevSecOps](https://fiercesw.com/devsecops-starter)
- [devopszone.info: DevSecOps Explained](https://www.devopszone.info/post/devsecops-explained)
- [linkedin: Dear Google, my data has left your building!](https://www.linkedin.com/pulse/dear-google-my-data-has-left-your-building-zakir-khan/)
- [snyk.io: The State of Open Source Security 2020](https://snyk.io/open-source-security-report/)
- [managedsentinel.com: Executive View — Current and Future Cybersecurity Architecture On One Page](https://www.managedsentinel.com/2019/05/23/cybersecurity-roadmap/)
- [Exploring the (lack of) security in a typical Docker and Kubernetes installation](https://www.neowin.net/news/exploring-the-lack-of-security-in-a-typical-docker-and-kubernets-installation/)
- [kalilinuxtutorials.com: Deploying & Securing Kubernetes Clusters](https://kalilinuxtutorials.com/deploying-securing-kubernetes-clusters/)
- [loves.cloud: Creating a fully automated DevSecOps CI/CD Pipeline](https://loves.cloud/creation-of-a-fully-automated-devsecops-cicd-pipeline/)
- [redhat.com: Balancing Linux security with usability](https://www.redhat.com/sysadmin/linux-security-usability) Your system should be secure, but open enough to serve its function. Here are some tips on how to strike that balance.
- [thenewstack.io: Culture, Vulnerabilities and Budget: Why Devs and AppSec Disagree](https://thenewstack.io/culture-vulnerabilities-and-budget-why-devs-and-appsec-disagree/)
- [computing.co.uk: CloudBees gets busy with security, visibility and control as DevOps evolves](https://www.computing.co.uk/news/4020521/cloudbees-busy-security-visibility-control-devops-evolves) CEO Sacha Labourey: 'DevOps is a pretty good proxy for what needs to happen in any organisation'
- [paloaltonetworks.com: Is Your Organization Protected Against IAM Misconfiguration Risks?](https://blog.paloaltonetworks.com/2020/10/cloud-iam-misconfiguration-risks/)
- [devops.com: How to Successfully Integrate Security and DevOps](https://devops.com/how-to-successfully-integrate-security-and-devops/)
- [helpnetsecurity.com: How to make DevSecOps stick with developers](https://www.helpnetsecurity.com/2020/12/14/how-devsecops-developers/)
- [blog.christophetd.fr: Shifting Cloud Security Left — Scanning Infrastructure as Code for Security Issues](https://blog.christophetd.fr/shifting-cloud-security-left-scanning-infrastructure-as-code-for-security-issues/)
- [devclass.com: Docker: It’s not dead yet, but there’s a tendency to walk away, security report finds](https://devclass.com/2021/01/13/sysdig-container-security-and-usage-report-2021/)
- [roxsrossve.medium.com: El camino hacia DevSecOps](https://roxsrossve.medium.com/el-camino-hacia-devsecops-bbd55e075043)
- [securityboulevard.com: DevOps vs. DevSecOps – Here’s How They Fit Together](https://securityboulevard.com/2021/02/devops-vs-devsecops-heres-how-they-fit-together/)
- [opensource.com: How to adopt DevSecOps successfully](https://opensource.com/article/21/2/devsecops) Integrating security throughout the software development lifecycle is important, but it's not always easy.
- [devops.com: DevSecOps Trends to Know For 2021](https://devops.com/devsecops-trends-for-2021/)
- [devops.com: From Agile to DevOps to DevSecOps: The Next Evolution](https://devops.com/from-agile-to-devops-to-devsecops-the-next-evolution/)
- [permission.site](https://permission.site/) How much stuff one can do from a web browser these days—scary stuff. Stay safe. Disable JS and most of stuff won't work at all.
- [ais.com: Leaping into DevSecOps from DevOps](https://www.ais.com/leaping-into-devsecops-from-devops/)
- [infoq.com: The Defense Department's Journey with DevSecOps](https://www.infoq.com/news/2020/06/defense-department-devsecops/)
- [amazon.com: Building end-to-end AWS DevSecOps CI/CD pipeline with open source SCA, SAST and DAST tools](https://aws.amazon.com/blogs/devops/building-end-to-end-aws-devsecops-ci-cd-pipeline-with-open-source-sca-sast-and-dast-tools/)
- [infoq.com: 9 Trends That Are Influencing the Adoption of Devops and Devsecops in 2021](https://www.infoq.com/articles/devops-secure-trends/)
- [addteq.com: The REAL Difference between DevOps and DevSecOps](https://www.addteq.com/blog/2021/03/the-real-difference-between-devops-and-devsecops)
- [invensislearning.com: Difference between DevOps and DevSecOps](https://www.invensislearning.com/blog/devops-vs-devsecops/)
- [techerati.com: DevSecOps: Eight tips for truly securing software](https://www.techerati.com/features-hub/opinions/devsecops-eight-tips-for-truly-securing-software/)
- [devops.com: SecDevOps is the Solution to Cybersecurity 🌟](https://devops.com/secdevops-is-the-solution-to-cybersecurity/)
- [techrepublic.com: DevOps is getting code released faster than ever. But security is lagging behind](https://www.techrepublic.com/article/devops-is-getting-code-released-faster-than-ever-but-security-is-lagging-behind/)
- [redeszone.net: No configurar bien la nube es culpable de la mayoría de vulnerabilidades](https://www.redeszone.net/noticias/seguridad/configurar-mal-nube-vulnerabilidades/)
- [cybersecuritydive.com: Relationships between DevOps, security warm slowly](https://www.cybersecuritydive.com/news/developer-security-gitlab-devsecops/) Some hurdles stem from miscommunication, or balancing quick product releases with undesired security gaps. **"Security people need developers to be more like security people and developers need security people to be more like developers."** James Arlen, CISO at Aiven.
- [bbvanexttechnologies.com: Filosofía DevSecOps en el desarrollo de aplicaciones sobre Azure](https://www.bbvanexttechnologies.com/blogs/filosofia-devsecops-en-el-desarrollo-de-aplicaciones-sobre-azure/)
- [harness.io: Automated DevSecOps with StackHawk and Harness](https://harness.io/blog/continuous-delivery/automated-devsecops/)
- [cloudify.co: Understanding DevSecOps And Its Challenges](https://cloudify.co/blog/overcoming-devsecops-delivery-pipeline-challenges/)
- [containerjournal.com: The What and Why of Cloud-Native Security](https://containerjournal.com/editorial-calendar/cloud-native-security/the-what-and-why-of-cloud-native-security/)
- [sysdig.com: Top vulnerability assessment and management best practices](https://sysdig.com/blog/vulnerability-assessment/)
- [thenewstack.io: Where Are You on the DevSecOps Maturity Curve?](https://thenewstack.io/where-are-you-on-the-devsecops-maturity-curve/)
- [thenewstack.io: The Top 5 Secrets Management Mistakes and How to Avoid Them](https://thenewstack.io/the-top-5-secrets-management-mistakes-and-how-to-avoid-them/)
- [arsouyes.org: PKCS, pem, der, key, crt,...](https://www.arsouyes.org/en/blog/2021/2021-06-21_PKCS_pem_der_key_crt) Interesting read on security and ssl/tls certificates
- [torq.io: 5 Security Automation Examples for Non-Developers](https://torq.io/blog/5-security-automation-examples-for-non-developers/)
- [infoq.com: Serverless Security: What's Left to Protect?](https://www.infoq.com/articles/serverless-security/)
- [dqindia.com: Secure your CI/CD pipeline with these tips from experts](https://www.dqindia.com/secure-cicd-pipeline-tips-experts/)
- [thenewstack.io: The DevSecOps Skillsets Required for Cloud Deployments](https://thenewstack.io/the-devsecops-skillsets-required-for-cloud-deployments/)
- [devblogs.microsoft.com: You can’t have security for DevOps until you have DevOps for security](https://devblogs.microsoft.com/engineering-at-microsoft/you-cant-have-security-for-devops-until-you-have-devops-for-security/)
- [goteleport.com: Anatomy of a Cloud Infrastructure Attack via a Pull Request](https://goteleport.com/blog/hack-via-pull-request/)
- [cncf/tag-security: CNCF Security Technical Advisory Group 🌟](https://github.com/cncf/tag-security) CNCF Security Technical Advisory Group -- secure access, policy control, privacy, auditing, explainability and more!
- [enterprisersproject.com: 5 DevSecOps open source projects to know](https://enterprisersproject.com/article/2021/8/5-devsecops-open-source-projects-know) Teams that embrace the DevSecOps approach make security an integral part of the entire application life cycle. These open source projects aim to help
	- [Clair](https://github.com/quay/clair)
	- [Sigstore](https://www.sigstore.dev/)
	- [KubeLinter](https://github.com/stackrox/kube-linter)
	- [Open Policy Agent and Gatekeeper](https://github.com/open-policy-agent/gatekeeper)
	- [Falco](https://falco.org/)
- [thenewstack.io: 10 Steps to Simplify Your DevSecOps](https://thenewstack.io/10-steps-to-simplify-your-devsecops/)
	1. Promote a DevSecOps Culture 
	2. Empower Teams to Build Security into the SDLC
	3. Plan Security Activities
	4. Improve Speed and Scale with Automation
	5. Start Early with Small Changes
	6. Tie in the Out-of-Band Activities
	7. Manage Security Vulnerabilities as Software Defects
	8. Collect and Analyze Data at Every Stage
	9. Learn from Your Failures
	10. Improve Velocity with Scalable Governance
- [dzone: Top 10 Application Security Articles to Read Now](https://dzone.com/articles/top-10-application-security-articles) See the 10 most popular articles on Application Security with topics covering bot attacks, resolving thefts, testing tools, security best practices, and more!
- [redhat.com: 5 ways for teams to create an automation-first mentality](https://www.redhat.com/sysadmin/automation-first-mentality) DevSecOps can provide a competitive edge for your organization. Use these five strategies to get started.
- [devops.com: Transform Mobile DevOps into Mobile DevSecOps](https://devops.com/transform-mobile-devops-into-mobile-devsecops/)
- [softwebsolutions.com: What is DevSecOps and why your business needs it](https://www.softwebsolutions.com/resources/devops-security-tools-benefits.html)
- [containerjournal.com: Siloscape: The Dark Side of Kubernetes](https://containerjournal.com/features/siloscape-the-dark-side-of-kubernetes/) **Siloscape is the first known malware to operate exclusively from within a container and target backdoors inside poorly configured Kubernetes clusters. Prizmant details how the malware collects data at the cluster level, making any hosted databases, user credentials and any business-critical data inside an easy and obvious target for the autonomous attacker.**
- [thenewstack.io: Infrastructure-as-Code: 6 Best Practices for Securing Applications 🌟](https://thenewstack.io/infrastructure-as-code-6-best-practices-for-securing-applications/)
- [devops.com: Securing Your Software Development Pipelines](https://devops.com/securing-your-software-development-pipelines/)
- [thenewstack.io: How GitOps Benefits from Security-as-Code](https://thenewstack.io/how-gitops-benefits-from-security-as-code/)
- [devops.com: Tips for a Successful DevSecOps Life Cycle](https://devops.com/tips-for-a-successful-devsecops-life-cycle/)
- [blog.aquasec.com: Advanced Persistent Threat Techniques Used in Container Attacks](https://blog.aquasec.com/advanced-persistent-threat-techniques-container-attacks) In this blog, you will explore advanced persistent threat techniques used in container attacks, learn how rootkits work, and how adversaries are using them to attack cloud native environments.
- [thenewstack.io: 5 Misconceptions About DevSecOps](https://thenewstack.io/5-misconceptions-about-devsecops/)
- [thenewstack.io: Why Cloud Native Systems Demand a Zero Trust Approach](https://thenewstack.io/why-cloud-native-systems-demand-a-zero-trust-approach/)
- [==redhat.com: Considerations for implementing DevSecOps practices. Checklist== 🌟](https://www.redhat.com/en/resources/considerations-implementing-devsecops-checklist)
- [==dzone: Security Matters: Vulnerability Scanning Done Right!== 🌟](https://dzone.com/articles/security-matters-vulnerability-scanning-done-right-1) Security has become the priority in every company these days. Let's see how vulnerability scanning is done the right way.
- [==redhat.com: Getting DevSecOps to production and beyond==](https://www.redhat.com/architect/devsecops-enterprise-architecture) Building security into DevOps practices helps safeguard the organization across the software development lifecycle.

## Kubernetes Security Compliance Frameworks
- [==armosec.io: Kubernetes Security Compliance Frameworks== 🌟](https://www.armosec.io/blog/kubernetes-security-frameworks-and-guidance/) 
	- The challenge of administering security and maintaining compliance in a Kubernetes ecosystem is typically the same: an increasingly dynamic, changing landscape, be it new approaches of cyberattacks or adhering to changing regulations. Kubernetes security requires a complex and multifaceted approach since an effective strategy needs to:
		- Ensure clean code
		- Provide full observability
		- Prevent the exchange of information with untrusted services
		- Produce digital signatures for clean code and trusted applications
	- Since Kubernetes follows a loosely coupled architecture, securing the ecosystem involves a cross-combination of best practices, tools, and processes. It is also recommended to consider frameworks that issue specific guidelines for easing the complexity of administering the security and compliance of a Kubernetes ecosystem. Such frameworks help organizations create flexible, iterative, and cost-effective approaches to keeping clusters and applications safe and compliant while ensuring optimum performance. A typical framework’s guidance on Kubernetes security and compliance should essentially consider:
		- Architecture best practices
		- Security within CI/CD pipelines
		- Resource protection
		- Container runtime protection
		- Supply chain security
		- Network security
		- Vulnerability scanning
		- Secrets management and protection

## Zero Trust Security
- [dzone.com: What Is Zero Trust Security?](https://dzone.com/articles/what-is-zero-trust-security) Zero Trust security is an IT security framework that treats everyone and everything to be hostile (in a good way!).

## Authentication and Authorization
- [thenewstack.io: How Do Authentication and Authorization Differ?](https://thenewstack.io/how-do-authentication-and-authorization-differ/)
- [==osohq.com: Patterns for Authorization in Microservices==](https://www.osohq.com/post/microservices-authorization-patterns)

## Quality Gates
- [dzone: DevOps Pipeline Quality Gates: A Double-Edged Sword](https://dzone.com/articles/devops-pipeline-quality-gates-a-double-edged-sword) In theory, quality gates seem like a no-brainer, but it does come with a catch.
## 16 Gates 
- [medium: Focusing on the DevOps Pipeline 🌟](https://medium.com/capital-one-tech/focusing-on-the-devops-pipeline-topo-pal-833d15edf0bd) Delivering High Quality Working Software Faster with Agile DevOps. At Capital One, we design pipelines using the concept of the “16 Gates”. These are our guiding design principles and they are:
	- Source code version control
	- Optimum branching strategy
	- Static analysis
	- More than 80% code coverage
	- Vulnerability scan
	- Open source scan
	- Artifact version control
	- Auto provisioning
	- Immutable servers
	- Integration testing
	- Performance testing
	- Build deploy testing automated for every commit
	- Automated rollback
	- Automated change order
	- Zero downtime release
	- Feature toggle
- [github.com/hygieia/Hygieia 🌟](https://github.com/hygieia/Hygieia) CapitalOne DevOps Dashboard

## Kubernetes Threat Modelling
- [marcolancini.it: The Current State of Kubernetes Threat Modelling](https://www.marcolancini.it/2020/blog-kubernetes-threat-modelling/)

## Kubernetes Config Security Threats
- [cncf.io: Identifying Kubernetes Config Security Threats: Pods Running as Root](https://www.cncf.io/blog/2020/06/16/identifying-kubernetes-config-security-threats-pods-running-as-root/)
- [mirantis.com: Introduction to Istio Ingress: The easy way to manage incoming Kubernetes app traffic](https://www.mirantis.com/blog/introduction-to-istio-ingress-the-easy-way-to-manage-incoming-kubernetes-app-traffic/) Leaving your cluster exposed can be risky. That's why you need Istio Ingress, which only exposes the part that handles incoming traffic & allows routing rules based on routes, headers, IP addresses and more.
- [thenewstack.io: How Kubernetes vulnerabilities have shifted since the first attacks](https://thenewstack.io/how-kubernetes-vulnerabilities-have-shifted-since-the-first-api-attacks/)

## Security Linting on Kubernetes
- [kubeLinter 🌟](https://github.com/stackrox/kube-linter) KubeLinter is a static analysis tool that checks Kubernetes YAML files and Helm charts to ensure the applications represented in them adhere to best practices.
- [thenewstack.io: StackRox KubeLinter Brings Security Linting to Kubernetes](https://thenewstack.io/stackrox-kubelinter-brings-security-linting-to-kubernetes/)

## IaC and Security
- [thenewstack.io: Security Insights into Infrastructure-as-Code](https://thenewstack.io/security-insights-into-infrastructure-as-code/)

## Multi-Level Security (MLS) vs Multi-Category Security (MCS). Make Secure Pipelines with Podman and Containers
- [Why you should be using Multi-Category Security (MCS) for your Linux containers](https://www.redhat.com/en/blog/why-you-should-be-using-multi-category-security-your-linux-containers)
- [Using Podman and Containers to make a more secure pipeline](https://www.redhat.com/en/blog/using-container-technology-make-trusted-pipeline)

## Project Calico
* [Project Calico](https://www.projectcalico.org/) Secure networking for the cloud native era
* [thenewstack.io: Project Calico: Kubernetes Security as SaaS](https://thenewstack.io/project-calico-kubernetes-security-as-saas/)

## The Falco Project
- [Falco.org](https://falco.org) Cloud-Native runtime security
- [==sysdig.com: Getting started with runtime security and Falco==](https://sysdig.com/blog/intro-runtime-security-falco/)

## Security Patterns for Microservice Architectures
- [Security Patterns for Microservice Architectures](https://developer.okta.com/blog/2020/03/23/microservice-security-patterns)

## Anchore Container Security Solutions for DevSecOps
- [Anchore](https://anchore.com) Container image inspection and policy-based compliance
- [thenewstack.io: Anchore: Scan Your Container Images for Vulnerabilities from the Command Line](https://thenewstack.io/anchore-scan-your-container-images-for-vulnerabilities-from-the-command-line/)

## Twistlock and Threat Stack Container Security
- [Twistlock](https://www.twistlock.com/)
- [Threat Stack](https://www.threatstack.com/)
- [dzone: A Twistlock and Threat Stack Comparison](https://dzone.com/articles/a-twistlock-and-threat-stack-comparison) Compare two of the most popular tools available for container security, and how their different approaches breed different solutions.

## OWASP
- [vashishtsumit89.medium.com: Security/Pen Testing: A guide to run OWASP Zap headless in containers for CI/CD pipeline](https://vashishtsumit89.medium.com/security-pen-testing-a-guide-to-run-owasp-zap-headless-in-containers-for-ci-cd-pipeline-ddb580dae3c8)
- [redeszone.net: OWASP ZAP, audita la seguridad de webs y evita vulnerabilidades](https://www.redeszone.net/tutoriales/seguridad/owasp-zap-auditar-seguridad-web/)
- [sonarqube.org: OWASP Top 10 - We’ve got you covered!](https://www.sonarqube.org/features/security/owasp/) See issues in the 10 most critical security risk categories in your web applications.
- [cloud.google.com: OWASP Top 10 mitigation options on Google Cloud 🌟](https://cloud.google.com/architecture/owasp-top-ten-mitigation#product_overviews) Terrific guidance in this paper that explains each attack vector and which product(s) can help
- [thenewstack.io: Latest OWASP Top 10 Surfaces Web Development Security Bugs](https://thenewstack.io/the-latest-owasp-top-10-looks-a-lot-like-the-old-owasp/)
- [thenewstack.io: OWASP Top 10: A Guide to the Worst Software Vulnerabilities](https://thenewstack.io/owasp-top-10-a-guide-to-the-worst-software-vulnerabilities/)

## Source Code Audit
- [==securecoding.com: Code Audit: How to Ensure Compliance for an Application==](https://www.securecoding.com/blog/code-audit-how-to-ensure-compliance-for-an-application/) A source code audit is a process of analyzing the source code of an application with the objective of discovering security vulnerabilities, security design problems, and places of potential improvement in programming practices. After the analysis, a report is generated that is used to implement a range of measures that guarantee the security and reliability of the code. Code audits can be carried out in parallel with penetration tests. They can test the exploitability of code vulnerabilities to better estimate the risk they pose. Ideally, code audits are performed throughout the application lifecycle. The faster a vulnerability is discovered, the easier it is to fix!

## StackRox
- [stackrox.com](https://www.stackrox.com/)
- [redhat.com: Red Hat to Acquire Kubernetes-Native Security Leader StackRox](https://www.redhat.com/en/about/press-releases/red-hat-acquire-kubernetes-native-security-leader-stackrox)

## Secure Container Based CI/CD Workflows. Vulnerability Scanner for Container Images
- [trivy](https://github.com/aquasecurity/trivy) A Simple and Comprehensive Vulnerability Scanner for Container Images, Git Repositories and Filesystems. Suitable for CI
	- [blog.aquasec.com: A Security Review of Docker Official Images: Which Do You Trust? (with trivy)](https://blog.aquasec.com/docker-official-images)
	- [dev.to: Terraform IaC Scanning with Trivy](https://dev.to/pwd9000/terraform-iac-scanning-with-trivy-3cai)
- [returngis.net: Buscar vulnerabilidades en imágenes de Docker con Snyk](https://www.returngis.net/2021/09/buscar-vulnerabilidades-en-imagenes-de-docker-con-snyk/)
- [iximiuz.com: The need for slimmer containers. Scanning official Python images with Snyk](https://iximiuz.com/en/posts/thick-container-vulnerabilities/)
- [gkovan.medium.com: A Zero Trust Approach for Securing the Supply Chain of Microservices Packaged as Container Images (sigstore, kyverno, openshift tekton, quarkus) 🌟](https://gkovan.medium.com/a-zero-trust-approach-for-securing-the-supply-chain-of-microservices-packaged-as-container-images-89d2f5b7293b)
- [thenewstack.io: Find Vulnerabilities in Container Images with Docker Scan](https://thenewstack.io/find-vulnerabilities-in-container-images-with-docker-scan/)

### Securing Kubernetes With Anchore
- [Securing Kubernetes With Anchore](https://anchore.com/kubernetes/)
- [Anchore: Secure Container Based CI/CD Workflows](https://anchore.com/cicd/)
- [Jenkins Plugin: Anchore Container Image Scanner](https://plugins.jenkins.io/anchore-container-scanner/)

### Secure Containers with Notary or Cosign
- [Notary](https://github.com/notaryproject/notary) Notary is a project that allows anyone to have trust over arbitrary collections of data
- [infracloud.io: Enforcing Image Trust on Docker Containers using Notary](https://www.infracloud.io/blogs/enforcing-image-trust-docker-containers-notary/)
- [medium: Verify Container Image Signatures in Kubernetes using Notary or Cosign or both](https://medium.com/sse-blog/verify-container-image-signatures-in-kubernetes-using-notary-or-cosign-or-both-c25d9e79ec45) Connaisseur v2.0 adds support for multiple keys and signature solutions.
- [infracloud.io: How to Secure Containers with Cosign and Distroless Images](https://www.infracloud.io/blogs/secure-containers-cosign-distroless-images/)
- [appvia.io: Tutorial: Keyless Sign and Verify Your Container Images With Cosign](https://www.appvia.io/blog/tutorial-keyless-sign-and-verify-your-container-images)
- [==github.blog: Safeguard your containers with new container signing capability in GitHub Actions (cosign)==](https://github.blog/2021-12-06-safeguard-container-signing-capability-actions/)

## GitHub security
- [GitHub security: what does it take to protect your company from credentials leaking on GitHub? 🌟](https://blog.gitguardian.com/github-security/)

## Databases in DMZ and Intranet
- [Databases in DMZ and Intranet](https://security.stackexchange.com/questions/58167/databases-in-dmz-and-intranet)

## Removing Credentials From Git Repo
- [medium: The Easiest Way To Remove Checked In Credentials From A Git Repo](https://medium.com/@tanmay.avinash.deshpande/the-easiest-way-to-remove-checked-in-credentials-from-a-git-repo-704a373b94e3)

## Pentesting
- [forbes.com: DevOps Drives Pentesting Delivered As A Service](https://www.forbes.com/sites/chenxiwang/2020/06/17/devops-drives-pentesting-delivered-as-a-service/)
- [emagined.com: How to conduct a penetration test](https://www.emagined.com/news-notes/2020/6/8/how-to-conduct-a-penetration-test)
- [securityboulevard.com: Kubernetes Pentest Methodology Part 3](https://securityboulevard.com/2019/11/kubernetes-pentest-methodology-part-3/)

## SQL Injection
- [patchthenet.medium.com: Introduction to SQL Injection](https://patchthenet.medium.com/introduction-to-sql-injection-sql-injection-for-beginners-579c00431d40)

## Credential Managers
### keycloak
- [keycloak.org](https://www.keycloak.org/) Open Source Identity and Access Management For Modern Applications and Services
- [Securing Kubernetes Apps with Keycloak and Gatekeeper](https://fdk.codes/securing-kubernetes-apps-with-keycloak-and-gatekeeper/)
- [Authorizing multi-language microservices with Louketo Proxy](https://developers.redhat.com/blog/2020/08/03/authorizing-multi-language-microservices-with-louketo-proxy/)
- [developers.redhat.com: A deep dive into Keycloak](https://developers.redhat.com/blog/2020/08/07/a-deep-dive-into-keycloak/)
- [blog.getambassador.io: Step-by-Step Centralized Authentication for Kubernetes with Keycloak and the Ambassador Edge Stack](https://blog.getambassador.io/centralized-authentication-with-keycloak-and-ambassador-edge-stack-d509ffbc7b6f)
- [blog.sighup.io: How to run Keycloak in HA on Kubernetes](https://blog.sighup.io/keycloak-ha-on-kubernetes/) How to setup Keycloak, the Open Source Identity and Access Management, in HA on Kubernetes.
- [developers.redhat.com: Authentication and authorization using the Keycloak REST API](https://developers.redhat.com/blog/2020/11/24/authentication-and-authorization-using-the-keycloak-rest-api/)
- [faun.pub: Integrate Keycloak with HashiCorp Vault](https://faun.pub/integrate-keycloak-with-hashicorp-vault-5264a873dd2f) A How-To guide using Terraform
- [openshift.com: Geographically Distributed Stateful Workloads - Part 3: Keycloak](https://www.openshift.com/blog/geographically-distributed-stateful-workloads-part-3-keycloak)

### Git Credential Manager Core
- [Git Credential Manager Core](https://github.com/microsoft/Git-Credential-Manager-Core) GCM Core is a free, open-source, cross-platform credential manager for Git.
- [Git Credential Manager Core: Building a universal authentication experience](https://github.blog/2020-07-02-git-credential-manager-core-building-a-universal-authentication-experience/)

## Secrets Management
- [blog.gitguardian.com: Secrets in source code (episode 2/3). Why secrets in git are such a problem](https://blog.gitguardian.com/secrets-credentials-api-git/)
- [harness.io: Managing Secrets in CI/CD Pipelines 🌟](https://harness.io/blog/devops/secrets-management-ci-cd/) How has your organization dealt with the challenge of managing secrets while delivering with CI/CD pipelines? Learn how to improve your process in the article.
- [smallstep.com: How to Handle Secrets on the Command Line 🌟](https://smallstep.com/blog/command-line-secrets/)
- [cloud.google.com: Analyze secrets with Cloud Asset Inventory](https://cloud.google.com/secret-manager/docs/analyze-resources) Query information about all the secrets across your entire GoogleCloudTech organization! Secret Manager is now integrated with Asset Inventory!
- [sops: Simple and flexible tool for managing secrets 🌟](https://github.com/mozilla/sops)
- [jenkins-x.io: Setting up the secrets for your installation](https://jenkins-x.io/v3/admin/setup/secrets/) Jenkins X 3.x uses Kubernetes External Secrets to manage populating secrets from your underlying secret store.
- [fpcomplete.com: Announcing Amber, encrypted secrets management](https://www.fpcomplete.com/blog/announcing-amber-ci-secret-tool/)
- [jfrog.com: How to protect your secrets with Spectral and JFrog Pipelines](https://jfrog.com/blog/how-to-protect-your-secrets-with-spectral-and-jfrog-pipelines/)
- [github.com/keilerkonzept/aws-secretsmanager-files](https://pkg.go.dev/github.com/keilerkonzept/aws-secretsmanager-files) Writes AWS Secrets Manager secrets to files on disk. Single binary, no dependencies. osx & linux & windows.
- [medium: How to Handle Secrets Like a Pro Using Gitops](https://medium.com/containers-101/how-to-handle-secrets-like-a-pro-using-gitops-f3b812536434)
- [youtube: Which of your Kubernetes Apps are accessing Secrets? 🌟](https://www.youtube.com/watch?v=6UF-QxiRGms&ab_channel=Kubevious) How do you know which apps across all your clusters are using Kubernetes Secrets? How are you sure that your secrets are not leaking? In the next 5 minutes, you will learn right that. 
- [jenkins-x/gsm-controller](https://github.com/jenkins-x/gsm-controller) gsm-controller is a Kubernetes controller that copies secrets from Google Secrets Manager into Kubernetes secrets. The controller watches Kubernetes secrets looking for an annotation, if the annotation is not found on the secret nothing more is done.
- [GoogleCloudPlatform/secrets-store-csi-driver-provider-gcp: Google Secret Manager Provider for Secret Store CSI Driver](https://github.com/GoogleCloudPlatform/secrets-store-csi-driver-provider-gcp) Google Secret Manager provider for the Secret Store CSI Driver. Allows you to access secrets stored in Secret Manager as files mounted in Kubernetes pods.
- [devops.com: DevOps Teams Struggling to Keep Secrets](https://devops.com/devops-teams-struggling-to-keep-secrets/) A growing number of organizations are suffering security incidents related to exposed secrets in DevOps CI/CD pipelines, according to a recent ThycoticCentrify report. The study paints a troubling picture: Only 5% of survey respondents said most of their development teams use the same secrets management processes and tools. The incidents run the gamut, from secrets published in the clear in public cloud code repositories to insecure third-party code to vulnerabilities in the organization’s own code or configurations.
- [==thorsten-hans.com: Encrypt your Kubernetes Secrets with Mozilla SOPS==](https://www.thorsten-hans.com/encrypt-your-kubernetes-secrets-with-mozilla-sops) By default, Kubernetes Secrets (secrets) are stored with base64 encoding in YAML files. The lack of encryption for secrets often leads to the question of how to store secrets securely. Obviously, you don’t want to put your sensitive configuration data into a git repository, because it is just encoded. echo <base64_representation> | base64 -d.
	- **A typical solution is using services like Azure Key Vault, or HashiCorp Vault to persist sensitive data. Those services can be integrated with Kubernetes by using the Secrets Store CIS driver. However, relying on an additional service means that you have to manage and maintain that service in addition to Kubernetes. Additionally, depending on the service you use to store your sensitive data, some sensitive configuration must be stored somewhere to configure the CIS driver.**
	- As an alternative, you can use Mozilla SOPS (SOPS) to encrypt and decrypt your Kubernetes secret files. **Secrets that are encrypted via SOPS can be stored in source control.** Encrypted secrets will be decrypted locally just before they’ll be deployed to Kubernetes. This article demonstrates how to encrypt and decrypt Kubernetes secrets (YAML files) using SOPS in combination with Azure Key Vault, which allows you to store your secrets along with other Kubernetes manifests directly in git.

### AWS Secret Manager
- [medium: AWS Secret Manager: Protect sensitive information and functionality 🌟](https://medium.com/avmconsulting-blog/aws-secret-manager-protect-sensitive-information-and-functionality-f520e15293f4) Protect Your Secrets in ApplicationsSecrets are frequently used to protect sensitive information and functionality.
- [blog.opstree.com: AWS Secret Manager](https://blog.opstree.com/2021/11/16/aws-secret-manager/)
- [aws/secrets-store-csi-driver-provider-aws: AWS Secrets Manager and Config Provider for Secret Store CSI Driver](https://github.com/aws/secrets-store-csi-driver-provider-aws) AWS offers two services to manage secrets and parameters conveniently in your code. [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/) allows you to easily rotate, manage, and retrieve database credentials, API keys, certificates, and other secrets throughout their lifecycle. [AWS Systems Manager Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html) provides hierarchical storage for configuration data. The AWS provider for the [Secrets Store CSI Driver](https://github.com/kubernetes-sigs/secrets-store-csi-driver) allows you to make secrets stored in Secrets Manager and parameters stored in Parameter Store appear as files mounted in Kubernetes pods. 

### Password Hashing
- [pyca/bcrypt](https://github.com/pyca/bcrypt) Modern(-ish) password hashing for your software and your servers. 
- [argon2-cffi](https://argon2-cffi.readthedocs.io)
- [docs.python.org: scrypt (standard library)](https://docs.python.org/3/library/hashlib.html#hashlib.scrypt)
- [cryptography.io: scrypt (cryptography)](https://cryptography.io/en/latest/hazmat/primitives/key-derivation-functions/#cryptography.hazmat.primitives.kdf.scrypt.Scrypt)

### Store private data in git repo
- [git-secret.io](https://git-secret.io/)
- [git-cipher](https://github.com/wincent/git-cipher)

### HashiCorp Vault
- [hashicorp/vault](https://github.com/hashicorp/vault) A tool for secrets management, encryption as a service, and privileged access management
- [hashicorp/vault-csi-provider: HashiCorp Vault Provider for Secrets Store CSI Driver](https://github.com/hashicorp/vault-csi-provider) HashiCorp Vault provider for the Secrets Store CSI driver allows you to get secrets stored in Vault and use the Secrets Store CSI driver interface to mount them into Kubernetes pods
- [vaultproject.io](https://www.vaultproject.io/) Manage Secrets and Protect Sensitive Data. Secure, store and tightly control access to tokens, passwords, certificates, encryption keys for protecting secrets and other sensitive data using a UI, CLI, or HTTP API.
- [medium: Coding for Secrets Reliability with HashiCorp Vault](https://medium.com/hashicorp-engineering/coding-for-secrets-reliability-with-hashicorp-vault-2090dd8667e)
- [hashicorp.com: Vault & Kubernetes: Better Together](https://www.hashicorp.com/resources/vault-and-kubernetes-better-together/)
- OpenShift Blogs:
    - https://www.openshift.com/blog/managing-secrets-openshift-vault-integration
    - https://www.openshift.com/blog/vault-integration-using-kubernetes-authentication-method
    - https://www.openshift.com/blog/integrating-vault-with-legacy-applications
    - https://www.openshift.com/blog/integrating-hashicorp-vault-in-openshift-4
- [Vault Learning Resources: Vault 1.5 features and more](https://www.hashicorp.com/blog/learn-vault-1-5)
- [medium: Securing K8s Ingress Traffic with HashiCorp Vault PKIaaS and JetStack Cert-Manager](https://medium.com/hashicorp-engineering/securing-k8s-ingress-traffic-with-hashicorp-vault-pkiaas-and-jetstack-cert-manager-cb46195742ca)
- [hashicorp.com: Automate Secret Injection into CI/CD Workflows with the GitHub Action for Vault](https://www.hashicorp.com/blog/vault-github-action)
- [hashicorp.com: Use AWS Lambda Extensions to Securely Retrieve Secrets From HashiCorp Vault](https://www.hashicorp.com/blog/aws-lambda-extensions-for-hashicorp-vault) Developers no longer have to make their Lambda functions Vault-aware.
- [github.com/kelseyhightower: Serverless Vault with Cloud Run](https://github.com/kelseyhightower/serverless-vault-with-cloud-run) This tutorial walks you through deploying Hashicorp's Vault on Cloud Run, Google Cloud's container based Serverless compute platform.
- [confluent.io: How to Manage Secrets for Confluent with Kubernetes and HashiCorp Vault](https://www.confluent.io/blog/manage-secrets-with-kubernetes-and-hashicorp-vault/)
- [digitalvarys.com: Simple Introduction to HashiCorp Vault](https://digitalvarys.com/simple-introduction-to-hashicorp-vault/)
- [hashicorp.com: HCP Vault is now generally available on AWS 🌟](https://www.hashicorp.com/blog/vault-on-the-hashicorp-cloud-platform-ga)
- [hashicorp.com: Serverless Secrets with HashiCorp Vault](https://www.hashicorp.com/resources/serverless-secrets-vault) Learn how to securely store and retrieve credentials across providers for applications running within AWS Lambda, Azure Functions, and Google Cloud Functions.
- [thenewstack.io: HashiCorp Releases HCP Vault to Combat ‘Secrets Management’ Fatigue](https://thenewstack.io/hashicorps-releases-hcp-vault-to-combat-secrets-management-fatigue/)
- [datadoghq.com: Monitor HashiCorp Vault metrics and logs](https://www.datadoghq.com/blog/monitor-vault-metrics-and-logs/)
- [thenewstack.io: Reasons to Implement HashiCorp Vault and Other Zero Trust Tools](https://thenewstack.io/reasons-to-implement-hashicorp-vault-and-other-zero-trust-tools/)
- [hashicorp.com: Retrieve HashiCorp Vault Secrets with Kubernetes CSI](https://www.hashicorp.com/blog/retrieve-hashicorp-vault-secrets-with-kubernetes-csi) Learn how to use CSI to expose secrets on a volume within a Kubernetes pod and retrieve them using our beta Vault Provider for the Kubernetes Secrets Store CSI Driver.
- [testdriven.io: Running Vault and Consul on Kubernetes](https://testdriven.io/blog/running-vault-and-consul-on-kubernetes/)
- [hashicorp.com: Onboarding Applications to Vault Using Terraform: A Practical Guide 🌟](https://www.hashicorp.com/blog/onboarding-applications-to-vault-using-terraform-a-practical-guide) Learn how to build an automated HashiCorp Vault onboarding system with Terraform using sensible naming standards, ACL policy templates, pre-created application entities, and workflows driven by VCS and CI/CD.
- [hashicorp.com: Managing SSH Access at Scale with HashiCorp Vault](https://www.hashicorp.com/blog/managing-ssh-access-at-scale-with-hashicorp-vault) Learn how to build scalable, role-based SSH access with SSH certificates and HashiCorp Vault.
- [devopscube.com: How to Setup Vault in Kubernetes- Beginners Tutorial 🌟](https://devopscube.com/vault-in-kubernetes/)
- [hashicorp.com: Retrieve HashiCorp Vault Secrets with Kubernetes CSI 🌟](https://www.hashicorp.com/blog/retrieve-hashicorp-vault-secrets-with-kubernetes-csi) Learn how to use CSI to expose secrets on a volume within a Kubernetes pod and retrieve them using our beta Vault Provider for the Kubernetes Secrets Store CSI Driver.
- [devopscube.com: Vault Agent Injector Tutorial: Inject Secrets to Pods Using Vault Agent](https://devopscube.com/vault-agent-injector-tutorial/)
- [hashicorp.com: Announcing HashiCorp Vault 1.8](https://www.hashicorp.com/blog/vault-1-8)
- [hashicorp.com: A Kubernetes User's Guide to HashiCorp Nomad Secret Management](https://www.hashicorp.com/blog/a-kubernetes-user-s-guide-to-hashicorp-nomad-secret-management) Learn how secrets management in Kubernetes compares to HashiCorp Nomad, and see why HashiCorp Vault is a powerful solution for both.
- [igorzhivilo.com: Scheduled backup of Vault secrets with Jenkins on Kubernetes](https://igorzhivilo.com/vault/scheduled-backup-vault-secrets/) If you ever wondered how to save the secrets of HashiCorp's Vault on a daily basis.
- [hashicorp.com: HashiCorp Vault Use Cases and Best Practices on Azure](https://www.hashicorp.com/blog/hashicorp-vault-use-cases-and-best-practices-on-azure)
- [==medium: Install Hashicorp Vault on Kubernetes using Helm - Part 1== | Marco Franssen](https://marcofranssen.nl/install-hashicorp-vault-on-kubernetes-using-helm-part-1)
	- [==medium: Install Hashicorp Vault on Kubernetes using Helm — Part 2== | Marco Franssen](https://medium.com/@marco.franssen/install-hashicorp-vault-on-kubernetes-using-helm-part-2-d612cf6c0c91)

#### HashiCorp Vault Agent 
- [Vault Agent 🌟](https://www.vaultproject.io/docs/agent)
- [harness.io: Tutorial: How to Use the New Vault Agent Integration Method With Harness](https://harness.io/blog/devops/vault-agent-secrets-management)
- [harness.io: Tutorial: Vault Agent Advanced Use Case With Kubernetes Delegates and Shared Volumes 🌟](https://harness.io/blog/devops/vault-agent-kubernetes-delegates)
- [hashicorp.com: Why Use the Vault Agent for Secrets Management?](https://www.hashicorp.com/blog/why-use-the-vault-agent-for-secrets-management)

### Azure Key Vault 
- [docs.microsoft.com: Azure Key Vault](https://docs.microsoft.com/en-us/azure/key-vault/general/overview)
- [azure.github.io: Azure Key Vault Provider for Secrets Store CSI Driver](https://azure.github.io/secrets-store-csi-driver-provider-azure/)
- [==akv2k8s.io: Azure Key Vault to Kubernetes akv2k8s== 🌟](https://akv2k8s.io/) Azure Key Vault to Kubernetes (akv2k8s) makes Azure Key Vault secrets, certificates and keys available in Kubernetes and/or your application - in a simple and secure way
	- [Azure Key Vault to Kubernetes](https://github.com/SparebankenVest/azure-key-vault-to-kubernetes) Azure Key Vault to Kubernetes (akv2k8s for short) makes it simple and secure to use Azure Key Vault secrets, keys and certificates in Kubernetes.
- [Neoteroi/essentials-configuration-keyvault](https://github.com/Neoteroi/essentials-configuration-keyvault) Azure Key Vault source for essentials-configuration
- [==techcommunity.microsoft.com: In preview: Azure Key Vault secrets provider extension for Arc enabled Kubernetes clusters==](https://techcommunity.microsoft.com/t5/azure-arc-blog/in-preview-azure-key-vault-secrets-provider-extension-for-arc/ba-p/3002160)

### CyberArk and Ansible
- [ansible.com: Simplifying secrets management with CyberArk and Red Hat Ansible Automation Platform](https://www.ansible.com/blog/simplifying-secrets-management-with-cyberark-and-red-hat-ansible-automation-platform)
- [ansible.com: Automating Security with CyberArk and Red Hat Ansible Automation Platform](https://www.ansible.com/blog/automating-security-with-cyberark-and-red-hat-ansible-automation-platform)

### CyberArk Conjur
- [conjur.org](https://www.conjur.org/)
- [infracloud.io: Securing Kubernetes Secrets with Conjur 🌟](https://www.infracloud.io/blogs/securing-kubernetes-secrets-conjur)

### SOPS for Kubernetes
- [dev.to: Manage your secrets in Git with SOPS for Kubernetes 🌟](https://dev.to/stack-labs/manage-your-secrets-in-git-with-sops-for-kubernetes-57me)

### Alternatives with Kubernetes External Secrets
- [GitOps secret management with bitnami-labs Sealed Secret and GoDaddy Kubernetes External Secrets 🌟](https://www.openshift.com/blog/gitops-secret-management)
	- [Kubernetes External Secrets 🌟](https://github.com/external-secrets/kubernetes-external-secrets) Integrate external secret management systems with Kubernetes. Kubernetes External Secrets allows you to use external secret management systems, like AWS Secrets Manager or HashiCorp Vault, to securely add secrets in Kubernetes.
	- [thenewstack.io: GoDaddy’s Project to Secure, Rotate Kubernetes Secrets 🌟](https://thenewstack.io/godaddys-innovative-project-to-secure-and-rotate-kubernetes-secrets/)
- [aws.amazon.com: Managing secrets deployment in Kubernetes using Sealed Secrets 🌟](https://aws.amazon.com/blogs/opensource/managing-secrets-deployment-in-kubernetes-using-sealed-secrets/)
- [dzone: Managing Secrets Deployment in GitOps Workflow 🌟](https://dzone.com/articles/managing-kubernetes-secrets) The importance of keeping your secrets safe.
- [blog.container-solutions.com: The Birth of the External Secrets Community](https://blog.container-solutions.com/the-birth-of-the-external-secrets-community)
- [itnext.io: Secrets injection at runtime from external Vault into Kubernetes — POC](https://itnext.io/secrets-injection-from-external-vault-into-kubernetes-poc-83a52c8cf5cb)
- [jx-secret-postrenderer 🌟](https://github.com/jenkins-x-plugins/jx-secret-postrenderer) a helm postrenderer for working with helm and Kubernetes External Secrets. This post renderer lets you use helm charts which contain Secret resources and have those secrets managed by Kubernetes External Secrets without having to modify your charts. Want seamless support for kubernetes external secrets with existing helm charts? but you're not using Jenkins X yet? then why not try this helm post renderer.
- [thenewstack.io: Managing Kubernetes Secrets with AWS Secrets Manager 🌟](https://thenewstack.io/managing-kubernetes-secrets-with-aws-secrets-manager/)
- [K8s Vault Webhook 🌟](https://ot-container-kit.github.io/k8s-vault-webhook/) - [github: k8s-vault-webhook](https://github.com/OT-CONTAINER-KIT/k8s-vault-webhook) A k8s vault webhook is a Kubernetes webhook that can inject secrets into Kubernetes resources by connecting to multiple secret managers
- [portworx.com: Implementing Data Security on Red Hat OpenShift 🌟](https://portworx.com/implementing-data-security-on-red-hat-openshift/)

## Serverless Security Best Practices
- [10 Serverless security best practices](https://snyk.io/blog/10-serverless-security-best-practices/)

## Docker Images & Container Security
- [thehackernews.com: Docker Images Containing Cryptojacking Malware Distributed via Docker Hub](https://thehackernews.com/2020/06/cryptocurrency-docker-image.html)
- [sysdig.com: 12 Container image scanning best practices to adopt in production](https://sysdig.com/blog/image-scanning-best-practices/)
- [infracloud.io: The Ten Commandments of Container Security](https://www.infracloud.io/blogs/top-10-things-for-container-security/)
- [medium: KubeSecOps Pipeline(Container security) in a cloudnative ecosystem](https://medium.com/@vaib16dec/kubesecops-pipeline-container-security-in-a-cloudnative-ecosystem-e59bf19a713d)
- [sysdig.com: Sysdig 2021 container security and usage report: Shifting left is not enough 🌟](https://sysdig.com/blog/sysdig-2021-container-security-usage-report/)
- [itnext.io: Hardening Docker and Kubernetes with seccomp 🌟](https://itnext.io/hardening-docker-and-kubernetes-with-seccomp-a88b1b4e2111)
- [redhat.com: Improving Linux container security with seccomp 🌟](https://www.redhat.com/sysadmin/container-security-seccomp) Try this method of using an OCI runtime hook for tracing syscalls before you build a container.
- [openshift.com: Signing and Verifying Container Images 🌟](https://www.openshift.com/blog/signing-and-verifying-container-images)
- [redhat.com: Introducing Red Hat Vulnerability Scanner Certification](https://www.redhat.com/en/blog/introducing-red-hat-vulnerability-scanner-certification)
- [docs.microsoft.com: Introduction to Azure Defender for container registries](https://docs.microsoft.com/en-us/azure/security-center/defender-for-container-registries-introduction#when-are-images-scanned) Defender for Container Registries Continuous Image Scan for vulnerabilities is now available for General Availability (GA)
- [techbeacon.com: 17 open-source container security tools 🌟](https://techbeacon.com/security/17-open-source-container-security-tools)
- [about.gitlab.com: How to secure your container images with GitLab and Grype](https://about.gitlab.com/blog/2021/07/28/secure-container-images-with-gitlab-and-grype/) - [grype: a vulnerability scanner for container images and filesystems](https://github.com/anchore/grype)
- [GoogleContainerTools/container-structure-test](https://github.com/GoogleContainerTools/container-structure-test) validate the structure of your container images
- [dynatrace.com: Container security: What it is, why it’s tricky, and how to do it right](https://www.dynatrace.com/news/blog/what-is-container-security/)

### Sigstore 
- [==sigstore.dev==](https://www.sigstore.dev/) A new standard for signing, verifying and protecting software. Making sure your software’s what it claims to be.
	- [youtube: Hands-on Introduction to sigstore | Rawkode Live](https://www.youtube.com/watch?v=fZfd4orrn8Y&ab_channel=RawkodeAcademy) In this tutorial, you’ll learn how to sign and verify container images with co-sign, with and without a private key. 
- [==opensource.com: Sign and verify container images with this open source tool (sigstore)==](https://opensource.com/article/21/12/sigstore-container-images) The sigstore project aims at securing supply chain technology.

### Container security best practices
- [sysdig.com: Container security best practices: Ultimate guide 🌟](https://sysdig.com/blog/container-security-best-practices)

## Pod Security Policies
- [octetz.com: Setting Up Pod Security Policies](https://octetz.com/docs/2018/2018-12-07-psp/) By default, Kubernetes allows anything capable of creating a Pod to run a fairly privileged container that can compromise a system. Pod Security Policies protect clusters from privileged pods by ensuring the requester is authorised.
- [infracloud.io: Kubernetes Pod Security Policies with Open Policy Agent](https://www.infracloud.io/kubernetes-pod-security-policies-opa/) In this blog post, you will learn about the Pod Security Policy admission controller. Then you will see how Open Policy Agent can implement Pod Security Policies.

## Kubernetes Network Policies
- [medium.com: K8s Network Policies Demystified and Simplified 🌟](https://medium.com/swlh/k8s-network-policies-demystified-and-simplified-18f5ea9848e2)
- [blog.nody.cc: Verify your Kubernetes Cluster Network Policies: From Faith to Proof](https://blog.nody.cc/posts/2020-06-kubernetes-network-policy-verification/)
- [medium: Kubernetes Network Policies: Are They Really Useful?](https://medium.com/@senthilrch/kubernetes-network-polices-are-they-really-useful-c3a153c49316)

## Static Analysis SAST
- [DevSecOps – Static Analysis SAST with Jenkins Pipeline](https://digitalvarys.com/devsecops-static-analysis-sast-with-jenkins-pipeline/)

## Kubernetes Security Tools 
- [europeclouds.com: Implementing Aqua Security to Secure Kubernetes](https://www.europeclouds.com/blog/implementing-aqua-security-to-secure-kubernetes)
- [Pomerium](https://github.com/pomerium/pomerium) is an identity-aware proxy that enables secure access to internal applications. Pomerium brings consistent authz/authn, tooling, and auditing across cloud and on-premise deployments. No VPN or cloud provider account is required
- [cloud.redhat.com: Top Open Source Kubernetes Security Tools of 2021 🌟🌟](https://cloud.redhat.com/blog/top-open-source-kubernetes-security-tools-of-2021)
- [fluentbit.io](https://fluentbit.io) Fluent Bit is an open source Log Processor and Forwarder which allows you to collect any data like metrics and logs from different sources, enrich them with filters and send them to multiple destinations. It's the preferred choice for containerized environments like Kubernetes.
	- [falco.org: Detect Malicious Behaviour on Kubernetes API Server through gathering Audit Logs by using FluentBit - Part 2](https://falco.org/blog/detect-malicious-behaviour-on-kubernetes-api-server-through-gathering-audit-logs-by-using-fluentbit-part-2/)
  
## Helm Charts Security. Helm Secrets
- [medium: Who’s at the Helm?](https://dlorenc.medium.com/whos-at-the-helm-1101c37bf0f1) Or, how to deploy 25+ CVEs to prod in one command!
* [itnext.io: Helm 3 — Secrets management, an alternative approach 🌟](https://itnext.io/helm-3-secrets-management-4f23041f05c3)
* [==itnext.io: Manage Auto-generated Secrets In Your Helm Charts== 🌟](https://itnext.io/manage-auto-generated-secrets-in-your-helm-charts-5aee48ba6918)

## Password Recovery
- [hashcat](https://hashcat.net/hashcat/)

## Attacks on Kubernetes via Misconfigured Argo Workflows
- [intezer.com: New Attacks on Kubernetes via Misconfigured Argo Workflows](https://www.intezer.com/blog/container-security/new-attacks-on-kubernetes-via-misconfigured-argo-workflows/)

## Books
- [Microservices Security in Action](https://medium.facilelogin.com/microservices-security-in-action-933072043ad7)

## CVEs
- [sysdig.com: Mitigating CVE-2021-20291: DoS affecting CRI-O and Podman](https://sysdig.com/blog/cve-2021-20291-cri-o-podman/)
- [armosec.io: Use Kubescape to check if your Kubernetes clusters are exposed to the latest K8s Symlink vulnerability (CVE-2021-25741)](https://www.armosec.io/blog/kubescape-checks-if-kubernetes-exposed-to-k8s-symlink-vulnerability-cve202125741)

### Log4j Log4Shell
- [medium: CVE-2021–44228: finding Log4j vulnerable k8s pods with bash & trivy](https://medium.com/linkbynet/cve-2021-44228-finding-log4j-vulnerable-k8s-pods-with-bash-trivy-caa10905744d)
- [sysdig.com: Mitigating log4j with Runtime-based Kubernetes Network Policies](https://sysdig.com/blog/mitigating-log4j-kubernetes-network-policies/)
- [github.com/aws-samples: Apache Log4j2 CVE-2021-44228 node agent](https://github.com/aws-samples/kubernetes-log4j-cve-2021-44228-node-agent) AWS has developed an RPM that performs a JVM-level hot-patch which disables JNDI lookups from the Log4j2 library, mitigating Log4j2 CVE-2021-44228. **The Apache Log4j2 CVE-2021-44228 node agent is an open source project built by the Kubernetes team at AWS. It is designed to run as a DaemonSet and mitigate the impact of Log4j2 CVE-2021-44228, which affects applications running Apache Log4j2 versions < 2.15.0 when processing inputs from untrusted sources. Running this DeamonSet will patch JVMs running in containers as well as on the host.**
- [proferosec/log4jScanner](https://github.com/proferosec/log4jScanner) This tool provides you with the ability to scan internal (only) subnets for vulnerable log4j web services. 
- [Apache Log4j Security Vulnerabilities](https://logging.apache.org/log4j/2.x/security.html)
- [cloud.redhat.com: Log4Shell: Practical Mitigations and Impact Analysis of the Log4j Vulnerabilities](https://cloud.redhat.com/blog/log4shell-practical-mitigations-and-impact-analysis)
- [edition.cnn.com: The Log4j security flaw could impact the entire internet. Here's what you should know](https://edition.cnn.com/2021/12/15/tech/log4j-vulnerability/index.html)
- [yahoo/check-log4j](https://github.com/yahoo/check-log4j) To determine if a host is vulnerable to log4j CVE‐2021‐44228
- [welivesecurity.com: Lo que todo líder de una empresa debe saber sobre Log4Shell](https://www.welivesecurity.com/la-es/2021/12/16/que-deben-saber-lideres-empresas-sobre-log4shell/) Se están detectando cientos de miles de intentos de ataque que buscan explotar la vulnerabilidad.
- [genbeta.com: "Internet está en llamas": Cloudflare ha detectado más de 24.600 ataques por minuto que explotaban la vulnerabilidad Log4Shell](https://www.genbeta.com/actualidad/internet-esta-llamas-cloudflare-ha-detectado-24-600-ataques-minuto-que-explotaban-vulnerabilidad-log4shell)
- [dynatrace.com: Log4Shell vulnerability](https://www.dynatrace.com/resource-center/log4j-vulnerability)
- [Maelstromage/Log4jSherlock](https://github.com/Maelstromage/Log4jSherlock) Log4j Scanner coded in Powershell, so you can run it in windows! This tool scans for JAR, WAR, EAR, JPI, HPI that contain the effected JndiLookup.class even in nested files. Scans nested files searches for the effected JNDI class. pulls version and reports in CSV, JSON, and txt log. reports error i.e. access issues to folders where files could be missed.

## Powershell
- [it.slashdot.org: And the Top Source of Critical Security Threats Is...PowerShell](https://it.slashdot.org/story/21/05/22/041242/and-the-top-source-of-critical-security-threats-ispowershell) Microsoft's CLI management tool was the source of more than a third of critical security threats detected by Cisco in the second half of 2020, according to eSecurity Planet.

## Let's Encrypt SSL certificates
- [techrepublic.com: How to create Let's Encrypt SSL certificates with acme.sh on Linux](https://www.techrepublic.com/article/how-to-create-lets-encrypt-ssl-certificates-with-acme-sh-on-linux/)
## More Security Tools
- [zdnet.com: Google releases new open-source security software program: Scorecards](https://www.zdnet.com/article/google-releases-new-open-source-security-software-program-scorecards/) How safe is that open-source software in the Git library, the one with the questionable history? Scorecard 2.0 can quickly tell you just how secure, or not, it really is.
- [sysadminxpert.com: How to do Security Auditing of CentOS System Using Lynis Tool](https://sysadminxpert.com/how-to-do-security-auditing-of-centos-system-using-lynis-tool/)
- [tryhackme.com: Metasploit: Introduction](https://tryhackme.com/room/metasploitintro) An introduction to the main components of the Metasploit Framework. Metasploit is a powerful tool that can support all phases of a penetration testing engagement
- [bridgecrew](https://bridgecrew.io) The codified cloud security platform for developers. Complete security and compliance visibility streamlined into developer-friendly workflows.
	- [bridgecrew.io: Tutorial: Incorporate IaC Security in your CI/CD pipeline with Bridgecrew, Jenkins, and GitHub](https://bridgecrew.io/blog/tutorial-incorporate-iac-security-in-your-ci-cd-pipeline-with-bridgecrew-jenkins-and-github)
- [curiefense/curiefense](https://github.com/curiefense/curiefense) Curiefense extends Envoy proxy to defend against a variety of threats, including SQL and command injection, cross site scripting (XSS), account takeovers (ATOs) and more