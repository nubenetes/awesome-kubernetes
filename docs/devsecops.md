# Security and DevSecOps. Container Security
- [Introduction](#introduction)
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
- [Security Patterns for Microservice Architectures](#security-patterns-for-microservice-architectures)
- [Anchore Container Security Solutions for DevSecOps](#anchore-container-security-solutions-for-devsecops)
- [Twistlock and Threat Stack Container Security](#twistlock-and-threat-stack-container-security)
- [OWASP](#owasp)
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
	- [Store private data in git repo](#store-private-data-in-git-repo)
	- [HashiCorp Vault](#hashicorp-vault)
		- [HashiCorp Vault Agent](#hashicorp-vault-agent)
	- [Azure Key Vault to Kubernetes akv2k8s](#azure-key-vault-to-kubernetes-akv2k8s)
	- [CyberArk and Ansible](#cyberark-and-ansible)
	- [CyberArk Conjur](#cyberark-conjur)
	- [SOPS for Kubernetes](#sops-for-kubernetes)
	- [Alternatives with Kubernetes External Secrets](#alternatives-with-kubernetes-external-secrets)
- [Serverless Security Best Practices](#serverless-security-best-practices)
- [Docker Images & Container Security](#docker-images--container-security)
	- [Container security best practices](#container-security-best-practices)
- [Pod Security Policies](#pod-security-policies)
- [Kubernetes Network Policies](#kubernetes-network-policies)
- [Static Analysis SAST](#static-analysis-sast)
- [Kubernetes Security Tools](#kubernetes-security-tools)
- [Helm Charts Security](#helm-charts-security)
- [Password Recovery](#password-recovery)
- [Attacks on Kubernetes via Misconfigured Argo Workflows](#attacks-on-kubernetes-via-misconfigured-argo-workflows)
- [Books](#books)
- [CVEs](#cves)
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

## Zero Trust Security
- [dzone.com: What Is Zero Trust Security?](https://dzone.com/articles/what-is-zero-trust-security) Zero Trust security is an IT security framework that treats everyone and everything to be hostile (in a good way!).

## Authentication and Authorization
- [thenewstack.io: How Do Authentication and Authorization Differ?](https://thenewstack.io/how-do-authentication-and-authorization-differ/)

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
- [medium: AWS Secret Manager: Protect sensitive information and functionality 🌟](https://medium.com/avmconsulting-blog/aws-secret-manager-protect-sensitive-information-and-functionality-f520e15293f4) Protect Your Secrets in ApplicationsSecrets are frequently used to protect sensitive information and functionality.
- [fpcomplete.com: Announcing Amber, encrypted secrets management](https://www.fpcomplete.com/blog/announcing-amber-ci-secret-tool/)
- [jfrog.com: How to protect your secrets with Spectral and JFrog Pipelines](https://jfrog.com/blog/how-to-protect-your-secrets-with-spectral-and-jfrog-pipelines/)
- [github.com/keilerkonzept/aws-secretsmanager-files](https://pkg.go.dev/github.com/keilerkonzept/aws-secretsmanager-files) Writes AWS Secrets Manager secrets to files on disk. Single binary, no dependencies. osx & linux & windows.
- [medium: How to Handle Secrets Like a Pro Using Gitops](https://medium.com/containers-101/how-to-handle-secrets-like-a-pro-using-gitops-f3b812536434)
- [youtube: Which of your Kubernetes Apps are accessing Secrets? 🌟](https://www.youtube.com/watch?v=6UF-QxiRGms&ab_channel=Kubevious) How do you know which apps across all your clusters are using Kubernetes Secrets? How are you sure that your secrets are not leaking? In the next 5 minutes, you will learn right that. 
- [jenkins-x/gsm-controller](https://github.com/jenkins-x/gsm-controller) gsm-controller is a Kubernetes controller that copies secrets from Google Secrets Manager into Kubernetes secrets. The controller watches Kubernetes secrets looking for an annotation, if the annotation is not found on the secret nothing more is done.
- [GoogleCloudPlatform/secrets-store-csi-driver-provider-gcp: Google Secret Manager Provider for Secret Store CSI Driver](https://github.com/GoogleCloudPlatform/secrets-store-csi-driver-provider-gcp) Google Secret Manager provider for the Secret Store CSI Driver. Allows you to access secrets stored in Secret Manager as files mounted in Kubernetes pods.

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

#### HashiCorp Vault Agent 
- [Vault Agent 🌟](https://www.vaultproject.io/docs/agent)
- [harness.io: Tutorial: How to Use the New Vault Agent Integration Method With Harness](https://harness.io/blog/devops/vault-agent-secrets-management)
- [harness.io: Tutorial: Vault Agent Advanced Use Case With Kubernetes Delegates and Shared Volumes 🌟](https://harness.io/blog/devops/vault-agent-kubernetes-delegates)
- [hashicorp.com: Why Use the Vault Agent for Secrets Management?](https://www.hashicorp.com/blog/why-use-the-vault-agent-for-secrets-management)

### Azure Key Vault to Kubernetes akv2k8s
- [akv2k8s.io 🌟](https://akv2k8s.io/) Azure Key Vault to Kubernetes (akv2k8s) makes Azure Key Vault secrets, certificates and keys available in Kubernetes and/or your application - in a simple and secure way

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
- [sigstore.dev](https://www.sigstore.dev/) A new standard for signing, verifying and protecting software. Making sure your software’s what it claims to be.
	- [youtube: Hands-on Introduction to sigstore | Rawkode Live](https://www.youtube.com/watch?v=fZfd4orrn8Y&ab_channel=RawkodeAcademy) In this tutorial, you’ll learn how to sign and verify container images with co-sign, with and without a private key. 
- [GoogleContainerTools/container-structure-test](https://github.com/GoogleContainerTools/container-structure-test) validate the structure of your container images
- [dynatrace.com: Container security: What it is, why it’s tricky, and how to do it right](https://www.dynatrace.com/news/blog/what-is-container-security/)

### Container security best practices
- [sysdig.com: Container security best practices: Ultimate guide 🌟](https://sysdig.com/blog/container-security-best-practices)

## Pod Security Policies
- [octetz.com: Setting Up Pod Security Policies](https://octetz.com/docs/2018/2018-12-07-psp/) By default, Kubernetes allows anything capable of creating a Pod to run a fairly privileged container that can compromise a system. Pod Security Policies protect clusters from privileged pods by ensuring the requester is authorised.
- [infracloud.io: Kubernetes Pod Security Policies with Open Policy Agent](https://www.infracloud.io/kubernetes-pod-security-policies-opa/) In this blog post, you will learn about the Pod Security Policy admission controller. Then you will see how Open Policy Agent can implement Pod Security Policies.

## Kubernetes Network Policies
- [medium.com: K8s Network Policies Demystified and Simplified 🌟](https://medium.com/swlh/k8s-network-policies-demystified-and-simplified-18f5ea9848e2)
- [blog.nody.cc: Verify your Kubernetes Cluster Network Policies: From Faith to Proof](https://blog.nody.cc/posts/2020-06-kubernetes-network-policy-verification/)

## Static Analysis SAST
- [DevSecOps – Static Analysis SAST with Jenkins Pipeline](https://digitalvarys.com/devsecops-static-analysis-sast-with-jenkins-pipeline/)

## Kubernetes Security Tools 
- [europeclouds.com: Implementing Aqua Security to Secure Kubernetes](https://www.europeclouds.com/blog/implementing-aqua-security-to-secure-kubernetes)
- [Pomerium](https://github.com/pomerium/pomerium) is an identity-aware proxy that enables secure access to internal applications. Pomerium brings consistent authz/authn, tooling, and auditing across cloud and on-premise deployments. No VPN or cloud provider account is required
- [cloud.redhat.com: Top Open Source Kubernetes Security Tools of 2021 🌟🌟](https://cloud.redhat.com/blog/top-open-source-kubernetes-security-tools-of-2021)
- [fluentbit.io](https://fluentbit.io) Fluent Bit is an open source Log Processor and Forwarder which allows you to collect any data like metrics and logs from different sources, enrich them with filters and send them to multiple destinations. It's the preferred choice for containerized environments like Kubernetes.
	- [falco.org: Detect Malicious Behaviour on Kubernetes API Server through gathering Audit Logs by using FluentBit - Part 2](https://falco.org/blog/detect-malicious-behaviour-on-kubernetes-api-server-through-gathering-audit-logs-by-using-fluentbit-part-2/)
  
## Helm Charts Security
- [medium: Who’s at the Helm?](https://dlorenc.medium.com/whos-at-the-helm-1101c37bf0f1) Or, how to deploy 25+ CVEs to prod in one command!

## Password Recovery
- [hashcat](https://hashcat.net/hashcat/)

## Attacks on Kubernetes via Misconfigured Argo Workflows
- [intezer.com: New Attacks on Kubernetes via Misconfigured Argo Workflows](https://www.intezer.com/blog/container-security/new-attacks-on-kubernetes-via-misconfigured-argo-workflows/)

## Books
- [Microservices Security in Action](https://medium.facilelogin.com/microservices-security-in-action-933072043ad7)

## CVEs
- [sysdig.com: Mitigating CVE-2021-20291: DoS affecting CRI-O and Podman](https://sysdig.com/blog/cve-2021-20291-cri-o-podman/)

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
