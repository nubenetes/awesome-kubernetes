# DevSecOps and Security. Container

1. [Introduction](#introduction)
2. [Kubernetes Security Compliance Frameworks](#kubernetes-security-compliance-frameworks)
3. [Zero Trust Security](#zero-trust-security)
4. [Authentication and Authorization](#authentication-and-authorization)
    1. [OpenID Connect and OAuth 2.0](#openid-connect-and-oauth-20)
5. [Quality Gates](#quality-gates)
6. [16 Gates](#16-gates)
7. [Kubernetes Threat Modelling](#kubernetes-threat-modelling)
8. [Kubernetes Config Security Threats](#kubernetes-config-security-threats)
    1. [Kubernetes Ingress Security](#kubernetes-ingress-security)
9. [Security Linting on Kubernetes](#security-linting-on-kubernetes)
10. [IaC and Security](#iac-and-security)
11. [Multi-Level Security (MLS) vs Multi-Category Security (MCS). Make Secure Pipelines with Podman and Containers](#multi-level-security-mls-vs-multi-category-security-mcs-make-secure-pipelines-with-podman-and-containers)
12. [Project Calico](#project-calico)
13. [The Falco Project](#the-falco-project)
14. [Security Patterns for Microservice Architectures](#security-patterns-for-microservice-architectures)
15. [Anchore Container Security Solutions for DevSecOps](#anchore-container-security-solutions-for-devsecops)
16. [Twistlock and Threat Stack Container Security](#twistlock-and-threat-stack-container-security)
17. [OWASP](#owasp)
18. [Source Code Audit](#source-code-audit)
19. [StackRox](#stackrox)
20. [Secure Container Based CI/CD Workflows. Vulnerability Scanner for Container Images](#secure-container-based-cicd-workflows-vulnerability-scanner-for-container-images)
     1. [Securing Kubernetes With Anchore](#securing-kubernetes-with-anchore)
     2. [Container Signing. Secure Containers with Notary or Cosign](#container-signing-secure-containers-with-notary-or-cosign)
21. [GitHub security](#github-security)
22. [Databases in DMZ and Intranet](#databases-in-dmz-and-intranet)
23. [Removing Credentials From Git Repo](#removing-credentials-from-git-repo)
24. [Pentesting](#pentesting)
25. [SQL Injection](#sql-injection)
26. [Credential Managers](#credential-managers)
     1. [keycloak](#keycloak)
     2. [Git Credential Manager Core](#git-credential-manager-core)
27. [Secrets Management](#secrets-management)
     1. [Anti Patterns. Wrong Secrets](#anti-patterns-wrong-secrets)
     2. [AWS Secret Manager](#aws-secret-manager)
     3. [Password Hashing](#password-hashing)
     4. [Store private data in git repo](#store-private-data-in-git-repo)
     5. [HashiCorp Vault](#hashicorp-vault)
         1. [HashiCorp Vault Agent](#hashicorp-vault-agent)
     6. [Azure Key Vault](#azure-key-vault)
     7. [CyberArk and Ansible](#cyberark-and-ansible)
     8. [CyberArk Conjur](#cyberark-conjur)
     9. [SOPS for Kubernetes](#sops-for-kubernetes)
     10. [AKS Secrets](#aks-secrets)
     11. [Kapitan](#kapitan)
     12. [Alternatives with Kubernetes External Secrets](#alternatives-with-kubernetes-external-secrets)
     13. [Bitwarden](#bitwarden)
28. [Serverless Security Best Practices](#serverless-security-best-practices)
29. [Docker Images and Container Security](#docker-images-and-container-security)
     1. [Sigstore](#sigstore)
     2. [Container security best practices](#container-security-best-practices)
30. [Pod Security Policies](#pod-security-policies)
31. [Kubernetes Network Policies](#kubernetes-network-policies)
32. [Static Analysis SAST](#static-analysis-sast)
33. [Kubernetes Security Tools](#kubernetes-security-tools)
34. [Helm Charts Security. Helm Secrets](#helm-charts-security-helm-secrets)
35. [Password Recovery](#password-recovery)
36. [Attacks on Kubernetes via Misconfigured Argo Workflows](#attacks-on-kubernetes-via-misconfigured-argo-workflows)
37. [PKI](#pki)
38. [Network Intrusion Tools](#network-intrusion-tools)
39. [Other Security Tools](#other-security-tools)
     1. [Torq. No code Security Automation](#torq-no-code-security-automation)
     2. [Security-Guard](#security-guard)
40. [Books](#books)
41. [CVEs](#cves)
     1. [Log4j Log4Shell](#log4j-log4shell)
42. [Powershell](#powershell)
43. [Nmap scripts](#nmap-scripts)
44. [Let's Encrypt SSL certificates](#lets-encrypt-ssl-certificates)
45. [WAF Web Application Firewall](#waf-web-application-firewall)
46. [More Security Tools](#more-security-tools)
47. [Videos](#videos)
48. [Twitter](#twitter)

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
    - [==edidiongasikpo.com: How to Give Developers Secure Access to Kubernetes Clusters== 🌟](https://edidiongasikpo.com/how-to-give-developers-secure-access-to-kubernetes-clusters)
- [cncf/tag-security: CNCF Security Technical Advisory Group 🌟](https://github.com/cncf/tag-security) CNCF Security Technical Advisory Group -- secure access, policy control, privacy, auditing, explainability and more!
- [enterprisersproject.com: 5 DevSecOps open source projects to know](https://enterprisersproject.com/article/2021/8/5-devsecops-open-source-projects-know) Teams that embrace the DevSecOps approach make security an integral part of the entire application life cycle. These open source projects aim to help
    - [Clair](https://github.com/quay/clair)
    - [Sigstore](https://www.sigstore.dev/)
    - [KubeLinter](https://github.com/stackrox/kube-linter)
        - [thomasthornton.cloud: Enforcing Kubernetes best practices and simplifying Kubernetes Configuration Validation with Kube-Linter and GitHub Actions](https://thomasthornton.cloud/2024/01/31/enforcing-kubernetes-best-practices-and-simplifying-kubernetes-configuration-validation-with-kube-linter-and-github-actions/)
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
- [opensource.com: 5 open source security resources from 2021](https://opensource.com/article/21/12/open-source-security) This countdown is for the security articles for 2021 you need to read right now.
- [==redhat.com: Red Hat's approach to DevSecOps==](https://www.redhat.com/en/topics/security/devsecops/approach)
- [thenewstack.io: Open Source Democratized Software. Now Let’s Democratize Security](https://thenewstack.io/open-source-democratized-software-now-lets-democratize-security/)
- [==goteleport.com: Why DevSecOps is Going Passwordless==](https://goteleport.com/blog/devsecops-passwordless)
- [==infosecwriteups.com: How I Discovered Thousands of Open Databases on AWS==](https://infosecwriteups.com/how-i-discovered-thousands-of-open-databases-on-aws-764729aa7f32) My journey on finding and reporting databases with sensitive data about Fortune-500 companies, Hospitals, Crypto platforms, Startups during due diligence, and more.
- [thenewstack.io: Want Real Cybersecurity Progress? Redefine the Security Team](https://thenewstack.io/want-real-cybersecurity-progress-redefine-the-security-team/)
- [devops.com: Taking a DevSecOps Approach to API Security](https://devops.com/why-traditional-approaches-to-api-security-dont-work/)
- [devops.com: Continuous Security: The Next Evolution of CI/CD](https://devops.com/continuous-security-the-next-evolution-of-ci-cd/)
- [==about.gitlab.com: Fantastic Infrastructure as Code security attacks and how to find them==](https://about.gitlab.com/blog/2022/02/17/fantastic-infrastructure-as-code-security-attacks-and-how-to-find-them/) **IaC Security Scanning with Kubernetes**
- [devops.com: How to Seamlessly Transition to DevSecOps](https://devops.com/how-to-seamlessly-transition-to-devsecops/) **DevSecOps Isn’t Simple**
    - In the last few months, the cybersecurity world has been taken by storm following the discovery of the Log4Shell vulnerability. The zero-day had the potential to put much of the connected world at risk and left security teams scrambling to quickly apply security patches to software just before Christmas 2021.
    - As a result of the chaos caused by Log4Shell, many organizations kicked off the new year by carrying out security assessments to identify ways to improve detection and mitigation of future vulnerabilities. One approach that is gaining a lot of attention is DevSecOps.
    - DevSecOps introduces and automates security in the earlier phases of the software development life cycle rather than bolting it on at the end. The approach saves money, saves time on tedious manual tasks, helps organizations meet regulatory compliance requirements and significantly reduces the risk of critical security bugs being found after an application’s final build.
    - However, when it comes to kicking off DevSecOps projects, there are a few challenges application security teams need to overcome first to ensure their programs fit seamlessly into CI/CD pipelines.
- [==bridgecrew.io: 6 key Kubernetes DevSecOps principles: People, processes, technology==](https://bridgecrew.io/blog/kubernetes-devsecops-principles/)
- [==research.nccgroup.com: 10 real-world stories of how we’ve compromised CI/CD pipelines==](https://research.nccgroup.com/2022/01/13/10-real-world-stories-of-how-weve-compromised-ci-cd-pipelines/)
- [thenewstack.io: SecOps in a Post-COVID World: 3 Security Trends to Watch](https://thenewstack.io/secops-in-a-post-covid-world-3-security-trends-to-watch/)
- [==medium.com/microservices-learning: How to implement security for microservices==](https://medium.com/microservices-learning/how-to-implement-security-for-microservices-89b140d3e555)
- [==kubernetes.io: Overview of Cloud Native Security==](https://kubernetes.io/docs/concepts/security/overview/) This overview defines a model for thinking about Kubernetes security in the context of Cloud Native security. **The 4C's of Cloud Native security:**
    - Cloud
    - Clusters
    - Containers
    - Code
- [sysdig.com: Triaging a Malicious Docker Container](https://sysdig.com/blog/triaging-malicious-docker-container/) Malicious Docker containers are a relatively new form of attack, taking advantage of an exposed Docker API or vulnerable host to do their evil plotting.​​
- [blog.sonatype.com: Python Packages Upload Your AWS Keys, env vars, Secrets to the Web](https://blog.sonatype.com/python-packages-upload-your-aws-keys-env-vars-secrets-to-web) Last week, Sonatype discovered multiple Python packages that not only exfiltrate your secrets—AWS credentials and environment variables but rather upload these to a publicly exposed endpoint. These packages were discovered by Sonatype's automated malware detection system, offered as a part of Nexus platform products, including Nexus Firewall.
- [medium.com/@anshuman2121: DevSecOps: Implement security on CICD Pipeline](https://medium.com/@anshuman2121/devsecops-implement-security-on-cicd-pipeline-19eb7aa22626)
- [medium.com/@jonathan_37674: What have we learned from scanning over 10K Kubernetes Clusters? 🌟](https://medium.com/@jonathan_37674/what-have-we-learned-from-scanning-over-10k-kubernetes-clusters-b0ac6b250427) Plan ahead and fight for  fight misconfiguration and vulnerabilities across the SDLC with **KubeScape**, OS security platform providing a multi-cloud K8s single pane of glass.
- [bleepingcomputer.com: Over 900,000 Kubernetes instances found exposed online](https://www.bleepingcomputer.com/news/security/over-900-000-kubernetes-instances-found-exposed-online/)
    - Over 900,000 misconfigured Kubernetes clusters were found exposed on the internet to potentially malicious scans, some even vulnerable to data-exposing cyberattacks.
    - Kubernetes is a highly versatile open-source container orchestration system for hosting online services and managing containerized workloads via a uniform API interface.
    - It enjoys massive adoption and growth rates thanks to its scalability, flexibility in multi-cloud environments, portability, cost, app development, and system deployment time reductions.
    - If Kubernetes isn’t configured properly, remote actors might be able to access internal resources and private assets that weren’t meant to be made public.
    - Additionally, depending on the configuration, intruders could sometimes escalate their privileges from containers to break isolation and pivot to host processes, granting them intial access to internal corporate networks for futher attacks.
- [sysdig.com: How to apply security at the source using GitOps | Eduardo Mínguez 🌟](https://sysdig.com/blog/gitops-iac-security-source/)
- [==medium.com/technology-hits: Incomplete Guide for Securing Containerized Environment== 🌟](https://medium.com/technology-hits/incomplete-guide-for-securing-containerized-environment-78b57fc3238) And Understanding How Containers Present Unique Security Challenges. This article contains a collection of best practices and tips regarding securing containerized environments.
- [medium.com/@jonathan_37674: How to Keep your CI/CD Pipelines Secure? | ARMO](https://medium.com/@jonathan_37674/how-to-keep-your-ci-cd-pipelines-secure-armo-8e962bc51fb6) CI/CD sits at the core of DevOps. The main aim of CICD is to automate & streamline app development process by making small changes & adding incrementally. It helps in pushing features faster with fewer errors.
- [freecodecamp.org: Authentication vs Authorization – What's the Difference?](https://www.freecodecamp.org/news/whats-the-difference-between-authentication-and-authorisation/)
- [==betanews.com: Cloud security is complex -- but most vulnerabilities fall into three key categories==](https://betanews.com/2022/10/22/cloud-security-is-complex-but-most-vulnerabilities-fall-into-three-key-categories/)
- [==medium.com/@pbijjala: Container security, an eco system view==](https://medium.com/@pbijjala/container-security-an-eco-system-183dbffdf2d8)
- [containerjournal.com: Kubernetes Security in Your CI/CD Pipeline](https://containerjournal.com/features/kubernetes-security-in-your-ci-cd-pipeline/)
- [acloudguru.com: Cloud security risks: Why you should make apps Secure by Design](https://acloudguru.com/blog/engineering/cloud-apps-secure-by-design)
- [medium.com/google-cloud: Shifting (even further) Left on Kubernetes Resource Compliance](https://medium.com/google-cloud/shifting-even-further-left-on-kubernetes-resource-compliance-8f96fb8c72eb) Shifting left can help organizations optimize their use of fully-managed cloud environments and managed services, and tools like Open Policy Agent and Gatekeeper can help organizations ensure compliance in these environments
- [hmaslowski.com: macOS Security hardening with Microsoft Intune](https://hmaslowski.com/home/f/macos-security-hardening-with-microsoft-intune)
- [kubewarden.io: Scanning secrets in environment variables](https://www.kubewarden.io/blog/2022/10/env-var-secrets/) This tutorial will teach you how to scan secrets in environment variables using Kubewarden and the  env-variable-secrets-scanner-policy
- [dzone.com: How To Manage Vulnerabilities in Modern Cloud-Native Applications](https://dzone.com/articles/how-to-manage-vulnerabilities-in-modern-cloud-nati) The article describes how to secure cloud-native applications to identify, manage, and remediate vulnerabilities across the tech stack and ways of integrating security.
- [auth0.com: A Passwordless Future! Passkeys for Java Developers](https://auth0.com/blog/webauthn-and-passkeys-for-java-developers/) Passkeys and WebAuthn for Java developers. Learn how to get started with passkeys for your Java and Spring Boot applications.
- [infracloud.io: How to Prevent Secret Leaks in Your Repositories](https://www.infracloud.io/blogs/prevent-secret-leaks-in-repositories/)
- [blog.devops.dev: End-to-End DevSecOps Kubernetes Project](https://blog.devops.dev/end-to-end-devsecops-kubernetes-project-4259f90722ef) In today’s rapidly evolving tech landscape, deploying applications using Kubernetes has become a crucial aspect of modern software development. This guide provides a detailed walkthrough for setting up an end-to-end Kubernetes project, covering everything from infrastructure provisioning to application deployment and monitoring.
- [blog.stackademic.com: Advanced End-to-End DevSecOps Kubernetes Three-Tier Project using AWS EKS, ArgoCD, Prometheus, Grafana, and Jenkins](https://blog.stackademic.com/advanced-end-to-end-devsecops-kubernetes-three-tier-project-using-aws-eks-argocd-prometheus-fbbfdb956d1a)

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

- [dzone.com: What Is Zero Trust Security? 🌟](https://dzone.com/articles/what-is-zero-trust-security) Zero Trust security is an IT security framework that treats everyone and everything to be hostile (in a good way!).
- [thenewstack.io: Secured Access to Kubernetes from Anywhere with Zero Trust | Tenry Fu 🌟](https://thenewstack.io/secured-access-to-kubernetes-from-anywhere-with-zero-trust/)
- [rafay.co: Securing Access to Kubernetes Environments with Zero Trust | Kyle Hunter 🌟](https://rafay.co/the-kubernetes-current/securing-access-to-kubernetes-environments-with-zero-trust/)
- [securityboulevard.com: Implementing Zero-Trust Security With Service Mesh and Kubernetes](https://securityboulevard.com/2022/10/implementing-zero-trust-security-with-service-mesh-and-kubernetes/)
- [cncf.io: Seven zero trust rules for Kubernetes](https://www.cncf.io/blog/2022/11/04/seven-zero-trust-rules-for-kubernetes/)
- [rtinsights.com: Implementing Zero Trust for Kubernetes](https://www.rtinsights.com/implementing-zero-trust-for-kubernetes/)
- [cisecurity.org: Where Does Zero Trust Begin and Why is it Important?](https://www.cisecurity.org/insights/blog/where-does-zero-trust-begin-and-why-is-it-important)
- [devops.com: DevOps Security: Your Complete Checklist](https://devops.com/devops-security-your-complete-checklist)

## Authentication and Authorization

- [thenewstack.io: How Do Authentication and Authorization Differ?](https://thenewstack.io/how-do-authentication-and-authorization-differ/)
- [==osohq.com: Patterns for Authorization in Microservices==](https://www.osohq.com/post/microservices-authorization-patterns)

### OpenID Connect and OAuth 2.0

- [medium.com/getindata-blog: OAuth2-based authentication on Istio-powered Kubernetes clusters 🌟](https://medium.com/getindata-blog/oauth2-based-authentication-on-istio-powered-kubernetes-clusters-2bd0999b7332) Starting with Envoy 1.17, authentication and authorization to Istio clusters don't require setting up external services if you decide to use OAuth2 Learn how it works in this hands-on tutorial.
- [==oauth2-proxy/oauth2-proxy: OAuth2 Proxy== 🌟](https://github.com/oauth2-proxy/oauth2-proxy) A reverse proxy that provides authentication with Google, Azure, OpenID Connect and many more identity providers.
- [manfredmlange.medium.com: Containerized Keycloak in Development](https://manfredmlange.medium.com/containerized-keycloak-in-development-2f9d079ec4a3) How to set up an OpenID Connect compliant development environment with Docker?
- [redis.com: JSON Web Tokens (JWTs) are Not Safe (ebook)](https://redis.com/docs/json-web-tokens-jwts-are-not-safe)
- [dev.to/fidalmathew: Session-Based vs. Token-Based Authentication: Which is better?](https://dev.to/fidalmathew/session-based-vs-token-based-authentication-which-is-better-227o)
- [dev.to/irakan: Is JWT really a good fit for authentication?](https://dev.to/irakan/is-jwt-really-a-good-fit-for-authentication-1khm)

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
- [thenewstack.io: How Kubernetes vulnerabilities have shifted since the first attacks](https://thenewstack.io/how-kubernetes-vulnerabilities-have-shifted-since-the-first-api-attacks/)

### Kubernetes Ingress Security

- [mirantis.com: Introduction to Istio Ingress: The easy way to manage incoming Kubernetes app traffic](https://www.mirantis.com/blog/introduction-to-istio-ingress-the-easy-way-to-manage-incoming-kubernetes-app-traffic/) Leaving your cluster exposed can be risky. That's why you need Istio Ingress, which only exposes the part that handles incoming traffic & allows routing rules based on routes, headers, IP addresses and more.
- [==armosec.io: How to secure Kubernetes Ingress?==](https://www.armosec.io/blog/kubernetes-ingress-security/) This article will look into how you can secure Ingress resources via adding TLS to Ingress and then procuring TLS/SSL certificates.

## Security Linting on Kubernetes

- [kubeLinter 🌟](https://github.com/stackrox/kube-linter) KubeLinter is a static analysis tool that checks Kubernetes YAML files and Helm charts to ensure the applications represented in them adhere to best practices.
- [thenewstack.io: StackRox KubeLinter Brings Security Linting to Kubernetes](https://thenewstack.io/stackrox-kubelinter-brings-security-linting-to-kubernetes/)
- [github.com/yannh/kubeconform 🌟](https://github.com/yannh/kubeconform) **A FAST Kubernetes manifests validator, with support for Custom Resources!**

## IaC and Security

- [thenewstack.io: Security Insights into Infrastructure-as-Code](https://thenewstack.io/security-insights-into-infrastructure-as-code/)

## Multi-Level Security (MLS) vs Multi-Category Security (MCS). Make Secure Pipelines with Podman and Containers

- [Why you should be using Multi-Category Security (MCS) for your Linux containers](https://www.redhat.com/en/blog/why-you-should-be-using-multi-category-security-your-linux-containers)
- [Using Podman and Containers to make a more secure pipeline](https://www.redhat.com/en/blog/using-container-technology-make-trusted-pipeline)

## Project Calico

- [Project Calico](https://www.projectcalico.org/) Secure networking for the cloud native era
- [thenewstack.io: Project Calico: Kubernetes Security as SaaS](https://thenewstack.io/project-calico-kubernetes-security-as-saas/)

## The Falco Project

- [Falco.org](https://falco.org) Cloud-Native runtime security
- [==sysdig.com: Getting started with runtime security and Falco==](https://sysdig.com/blog/intro-runtime-security-falco/)
- [betterprogramming.pub: Kubernetes Security With Falco](https://betterprogramming.pub/kubernetes-security-with-falco-2eb060d3ae7d) Comprehensive runtime security for your containers with a hands-on demo.

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
- [==owasp.org: OWASP API Security Project== 🌟](https://owasp.org/www-project-api-security)
- [traceable.ai: Use the OWASP API Top 10 To Secure Your APIs](https://www.traceable.ai/blog-post/use-the-owasp-api-top-10-to-secure-your-apis) The [==OWASP API Top 10==](https://owasp.org/www-project-api-security/) documents the risks associated with API development. Here are the vulnerabilities highlighted in the most recent OWASP API Top 10:
	1. Broken Object Level Authorization (BOLA)
	2. Broken User Authentication
	3. Excessive Data Exposure
	4. Lack of Resources and Rate Limiting
	5. Broken Function Level Authorization
	6. Mass Assignment
	7. Security Misconfiguration
	8. Injection
	9. Improper Assets Management
	10. Insufficient Logging and Monitoring

- [cequence.ai: The OWASP API Security Top 10 From a Real-World Perspective](https://www.cequence.ai/blog/owasp-api-security-top-10-from-a-real-world-perspective/)
- [securityonline.info: VAmPI: Vulnerable REST API with OWASP top 10 vulnerabilities](https://securityonline.info/vampi-vulnerable-rest-api-with-owasp-top-10-vulnerabilities/)
- [==github.com/OWASP: OWASP Kubernetes Top 10== 🌟](https://github.com/OWASP/www-project-kubernetes-top-ten)

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
- [medium.com/@nanditasahu031: DevSecOps — Implementing Secure CI/CD Pipelines 🌟](https://medium.com/@nanditasahu031/devsecops-implementing-secure-ci-cd-pipelines-9653726b4916)
- [deepfence/YaraHunter](https://github.com/deepfence/YaraHunter) Malware scanner for cloud-native, as part of CI/CD and at Runtime. Deepfence YaraHunter scans container images, running Docker containers, and filesystems to find indicators of malware. It uses a YARA ruleset to identify resources that match known malware signatures, and may indicate that the container or filesystem has been compromised. - https://deepfence.io/

### Securing Kubernetes With Anchore

- [Securing Kubernetes With Anchore](https://anchore.com/kubernetes/)
- [Anchore: Secure Container Based CI/CD Workflows](https://anchore.com/cicd/)
- [Jenkins Plugin: Anchore Container Image Scanner](https://plugins.jenkins.io/anchore-container-scanner/)

### Container Signing. Secure Containers with Notary or Cosign

- [Notary](https://github.com/notaryproject/notary) Notary is a project that allows anyone to have trust over arbitrary collections of data
- [Cosign: Container Signing](https://github.com/sigstore/cosign) Container Signing, Verification and Storage in an OCI registry. Cosign supports:
    - Hardware and KMS signing
    - Bring-your-own PKI
    - Our free OIDC PKI (Fulcio)
    - Built-in binary transparency and timestamping service (Rekor)
- [infracloud.io: Enforcing Image Trust on Docker Containers using Notary](https://www.infracloud.io/blogs/enforcing-image-trust-docker-containers-notary/)
- [medium: Verify Container Image Signatures in Kubernetes using Notary or Cosign or both](https://medium.com/sse-blog/verify-container-image-signatures-in-kubernetes-using-notary-or-cosign-or-both-c25d9e79ec45) Connaisseur v2.0 adds support for multiple keys and signature solutions.
- [infracloud.io: How to Secure Containers with Cosign and Distroless Images](https://www.infracloud.io/blogs/secure-containers-cosign-distroless-images/)
- [appvia.io: Tutorial: Keyless Sign and Verify Your Container Images With Cosign](https://www.appvia.io/blog/tutorial-keyless-sign-and-verify-your-container-images)
- [==github.blog: Safeguard your containers with new container signing capability in GitHub Actions (cosign)==](https://github.blog/2021-12-06-safeguard-container-signing-capability-actions/)
- [chrisns/cosign-keyless-demo: Cosign Keyless GitHub Action Demo](https://github.com/chrisns/cosign-keyless-demo) Proof of concept that uses cosign and GitHub's in built OIDC for actions to sign container images, providing a proof that what is in the registry came from your GitHub action.
- [blog.chainguard.dev: How To Verify Cosigned Container Images In Amazon ECS](https://blog.chainguard.dev/cosign-verify-ecs/)
- [justinpolidori.it: Secure Your Docker Images With Cosign (and OPA Gatekeeper)](https://www.justinpolidori.it/posts/20220116_sign_images_with_cosign_and_verify_with_gatekeeper/) Learn how combining Gatekeeper + Cosign for image signature validation with the new external_data feature lets you stop untrusted docker images from being deployed on your Kubernetes cluster.
- [sysdig.com: How to secure Kubernetes deployment with signature verification](https://sysdig.com/blog/secure-kubernetes-deployment-signature-verification/) Cosign and Connaisseur allow us to secure the Kubernetes deployment with signature verification, ensuring that our images do not change
- [medium.com/@slimm609: Secure image signing with Cosign and AWS KMS](https://medium.com/@slimm609/secure-image-signing-with-cosign-and-aws-kms-82bc25d7fdae)
- [itnext.io: Securing Kubernetes Workloads: A Practical Approach to Signed and Encrypted Container Images](https://itnext.io/securing-kubernetes-workloads-a-practical-approach-to-signed-and-encrypted-container-images-ff6e98b65bcd) Podman — one tool to rule them all

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
- [blog.flant.com: Running fault-tolerant Keycloak with Infinispan in Kubernetes](https://blog.flant.com/ha-keycloak-infinispan-kubernetes/)
- [baeldung.com: A Quick Guide to Using Keycloak with Spring Boot](https://www.baeldung.com/spring-boot-keycloak)
- [==medium.com/@charled.breteche: Securing Grafana with Keycloak SSO==](https://medium.com/@charled.breteche/securing-grafana-with-keycloak-sso-d01fec05d984) In this article you will learn how to deploy and configure Keycloak in a local Kubernetes cluster, then deploy Grafana and use the Keycloak instance for authentication and authorization
- [dev.to: KeyCloak with Nginx Ingress](https://dev.to/aws-builders/keycloak-with-nginx-ingress-6fo)
- [medium.com/@amirhosseineidy: Kubernetes authentication with keycloak oidc](https://medium.com/@amirhosseineidy/kubernetes-authentication-with-keycloak-oidc-63571eaeed61)
- [medium.com/@martin.hodges: How to install Keycloak IAM on your Kubernetes cluster, backed by Postgres](https://medium.com/@martin.hodges/how-to-install-keycloak-iam-on-your-kubernetes-cluster-backed-by-postgres-1228eae4faeb) In this article I look at installing Keycloak and integrating with a Kong API Gateway inside a Kubernetes cluster to provide an OAuth and OIDC solution for your services.

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
- [developers.redhat.com: Protect secrets in Git with the clean/smudge filter](https://developers.redhat.com/articles/2022/02/02/protect-secrets-git-cleansmudge-filter)
- [kubeopsskills/cloud-secret-resolvers: Cloud Secret Resolvers (CSR)](https://github.com/kubeopsskills/cloud-secret-resolvers) Cloud Secret Resolvers is a set of tools to help your applications (on Kubernetes) to retrieve any credentials from cloud managed vaults without the needed to write additional boilerplate code in your applications!.
- [thenewstack.io: Managing Secrets in Your DevOps Pipeline](https://thenewstack.io/managing-secrets-in-your-devops-pipeline/)
- [==thenewstack.io: Kubernetes Secrets Management: 3 Approaches, 9 Best Practices==](https://thenewstack.io/kubernetes-secrets-management-3-approaches-9-best-practices/) Developers must make early design choices about where to store secrets, how to retrieve them and how to make them available in an application.
- [siddhivinayak-sk.medium.com: Kubeseal & SealedSecret: Make your ‘secrets’ secure in SCM by using ‘sealed secret’](https://siddhivinayak-sk.medium.com/kubeseal-sealedsecret-make-your-secrets-secure-in-scm-by-using-sealed-secret-4631bcb39bf8) In this article, you will learn the theory and practice behind encrypting your secrets with SealedSecret & Kubeseal

### Anti Patterns. Wrong Secrets

- [==commjoen/wrongsecrets: OWASP WrongSecrets==](https://github.com/commjoen/wrongsecrets) Examples with how to not use secrets. Welcome to the OWASP WrongSecrets p0wnable app. With this app, we have packed various ways of how to not store your secrets. These can help you to realize whether your secret management is ok. The challenge is to find all the different secrets by means of various tools and techniques.

### AWS Secret Manager

- [medium: AWS Secret Manager: Protect sensitive information and functionality 🌟](https://medium.com/avmconsulting-blog/aws-secret-manager-protect-sensitive-information-and-functionality-f520e15293f4) Protect Your Secrets in ApplicationsSecrets are frequently used to protect sensitive information and functionality.
- [blog.opstree.com: AWS Secret Manager](https://blog.opstree.com/2021/11/16/aws-secret-manager/)
- [aws/secrets-store-csi-driver-provider-aws: AWS Secrets Manager and Config Provider for Secret Store CSI Driver](https://github.com/aws/secrets-store-csi-driver-provider-aws) AWS offers two services to manage secrets and parameters conveniently in your code. [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/) allows you to easily rotate, manage, and retrieve database credentials, API keys, certificates, and other secrets throughout their lifecycle. [AWS Systems Manager Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html) provides hierarchical storage for configuration data. The AWS provider for the [Secrets Store CSI Driver](https://github.com/kubernetes-sigs/secrets-store-csi-driver) allows you to make secrets stored in Secrets Manager and parameters stored in Parameter Store appear as files mounted in Kubernetes pods.
- [medium.com/@ishana98dadhich: Integrating AWS Secret Manager with EKS and use Secrets inside the Pods: Part-1](https://medium.com/@ishana98dadhich/integrating-aws-secret-manager-with-eks-and-use-secrets-inside-the-pods-part-1-1938b0c3c2fb) This blog provides you enough details on how you can use secrets (managed by AWS Secrets Manager) inside AWS EKS pods.
- [==unixarena.com: Terraform – Source credentials from AWS secret Manager==](https://www.unixarena.com/2022/04/terraform-source-credentials-from-aws-secret-manager.html/)

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
- [piotrminkowski.com: Vault on Kubernetes with Spring Cloud](https://piotrminkowski.com/2021/12/30/vault-on-kubernetes-with-spring-cloud/)
- [hashicorp.com: Integrating Azure AD Identity with HashiCorp Vault — Part 1: Azure Application Auth via OIDC](https://www.hashicorp.com/blog/integrating-azure-ad-identity-hashicorp-vault-part-1-application-auth-oidc)
- [==medium.com/@pratyush.mathur: Secrets Management Using Vault in K8S==](https://medium.com/@pratyush.mathur/secrets-management-using-vault-in-k8s-272462c37fd8)
- [hashicorp.com: Kubernetes Vault Integration via Sidecar Agent Injector vs. CSI Provider](https://www.hashicorp.com/blog/kubernetes-vault-integration-via-sidecar-agent-injector-vs-csi-provider) In this post, you will explore the different methods of integrating HashiCorp Vault with Kubernetes and learn how to choose the best solution for your use case.
- [hashicorp.com: Manage Kubernetes Secrets for Flux with HashiCorp Vault](https://www.hashicorp.com/blog/manage-kubernetes-secrets-for-flux-with-hashicorp-vault) Configure the Secrets Store CSI driver with HashiCorp Vault to securely inject secrets into **Flux** or other GitOps tools on Kubernetes.
- [==hashicorp.com: How to Integrate Your Application with Vault: Static Secrets==](https://www.hashicorp.com/blog/how-to-integrate-your-application-with-vault-static-secrets) Learn how to retrieve static secrets from HashiCorp Vault in a real-world setting using a new sample application.
- [blog.devops.dev: Using Vault in Kubernetes Production for Security Engineers](https://blog.devops.dev/using-vault-in-kubernetes-production-for-security-engineers-54d2f0aca4d1)
- [hashicorp.com: HashiCorp Vault 1.11 Adds Kubernetes Secrets Engine, PKI Updates, and More 🌟](https://www.hashicorp.com/blog/vault-1-11)
    - Favorite OSS feature is the K8S secrets engine that can generate K8S service accounts as dynamic secrets.
    - Favorite Ent feature is that Autopilot can now perform safe, automated upgrades.
    - Plus a dozen other improvements...

- [medium.com/@nikhil.purva: Securing Kubernetes Secrets with HashiCorp Vault](https://medium.com/@nikhil.purva/securing-kubernetes-secrets-with-hashicorp-vault-a9555728e095)
- [hashicorp.com: The State of Vault and Kubernetes, and Future Plans](https://www.hashicorp.com/blog/the-state-of-vault-and-kubernetes-and-future-plans) Get an overview of the most common ways to use HashiCorp Vault and Kubernetes together, and get a preview of a new method we're considering.
- [alexandre-vazquez.com: How To Inject Secrets in Pods To Improve Security with Hashicorp Vault in 5 Minutes 🌟](https://alexandre-vazquez.com/inject-secrets-in-pods-using-hashicorp-vault/)
- [adfinis.com: Secret zero with ACME](https://adfinis.com/en/blog/secret-zero-with-acme/) As of Vault 1.14, the HashiCorp Vault PKI engine can issue certificates using the standard ACME protocol. The Automatic Certificate Management Environment (ACME) was made popular by Let’s Encrypt, which has been the default mechanism to request valid certificates from a public CA for over 10 years.
- [medium.com/@martin.hodges: Introduction to Vault to provide secret management in your Kubernetes cluster](https://medium.com/@martin.hodges/introduction-to-vault-to-provide-secret-management-in-your-kubernetes-cluster-658b58372569) One of the core Kubernetes resources is a Secret. However, these Secrets are not actually secure, as anyone with access to the cluster may be able to read and update the secret. This article introduces Vault into the cluster to securely manage secrets.
    - [medium.com/@martin.hodges: Enabling TLS on your Vault cluster on Kubernetes](https://medium.com/@martin.hodges/enabling-tls-on-your-vault-cluster-on-kubernetes-0d20439b13d0) In this article I look at adding TLS secured connections to our unprotected Vault cluster. We will do this to ensure our secrets remain, well, secret.
- [medium.com/@calvineotieno010: Managing Application Secrets with Hashicorp Vault](https://medium.com/@calvineotieno010/managing-application-secrets-with-hashicorp-vault-8efb5e1d87fd)
- [medium.com/@muppedaanvesh: A Hands-On Guide to Vault in Kubernetes](https://medium.com/@muppedaanvesh/a-hand-on-guide-to-vault-in-kubernetes-%EF%B8%8F-1daf73f331bd) Manage k8s Secrets Using HashiCorp Vault: With Practical Examples

#### HashiCorp Vault Agent

- [Vault Agent 🌟](https://www.vaultproject.io/docs/agent)
- [harness.io: Tutorial: How to Use the New Vault Agent Integration Method With Harness](https://harness.io/blog/devops/vault-agent-secrets-management)
- [harness.io: Tutorial: Vault Agent Advanced Use Case With Kubernetes Delegates and Shared Volumes 🌟](https://harness.io/blog/devops/vault-agent-kubernetes-delegates)
- [hashicorp.com: Why Use the Vault Agent for Secrets Management?](https://www.hashicorp.com/blog/why-use-the-vault-agent-for-secrets-management)
- [medium.com/nerd-for-tech: PKI Certs Injection to K8s Pods with Vault Agent Injector](https://medium.com/nerd-for-tech/pki-certs-injection-to-k8s-pods-with-vault-agent-injector-d97482b48f3d) In this article, you'll learn how to use the Vault Agent Injector to dynamically generate and Inject PKI Certs to Pods by rendering secrets to a shared volume, containers within the pod will consume Vault secrets without being Vault aware.
- [hashicorp.com: Refresh Secrets for Kubernetes Applications with Vault Agent](https://www.hashicorp.com/blog/refresh-secrets-for-kubernetes-applications-with-vault-agent) Learn the system signal and live reload methods for updating Kubernetes applications when secrets change. See an example via a Spring Boot application.

### Azure Key Vault

- [docs.microsoft.com: Azure Key Vault](https://docs.microsoft.com/en-us/azure/key-vault/general/overview)
- [azure.github.io: Azure Key Vault Provider for Secrets Store CSI Driver](https://azure.github.io/secrets-store-csi-driver-provider-azure/)
- [==akv2k8s.io: Azure Key Vault to Kubernetes akv2k8s== 🌟](https://akv2k8s.io/) Azure Key Vault to Kubernetes (akv2k8s) makes Azure Key Vault secrets, certificates and keys available in Kubernetes and/or your application - in a simple and secure way
    - [Azure Key Vault to Kubernetes](https://github.com/SparebankenVest/azure-key-vault-to-kubernetes) Azure Key Vault to Kubernetes (akv2k8s for short) makes it simple and secure to use Azure Key Vault secrets, keys and certificates in Kubernetes.
- [Neoteroi/essentials-configuration-keyvault](https://github.com/Neoteroi/essentials-configuration-keyvault) Azure Key Vault source for essentials-configuration
- [==techcommunity.microsoft.com: In preview: Azure Key Vault secrets provider extension for Arc enabled Kubernetes clusters==](https://techcommunity.microsoft.com/t5/azure-arc-blog/in-preview-azure-key-vault-secrets-provider-extension-for-arc/ba-p/3002160)
- [vcloud-lab.com: Create Azure Key Vault Certificates on Azure Portal and Powershell](http://vcloud-lab.com/entries/microsoft-azure/-create-azure-key-vault-certificates-on-azure-portal-and-powershell)

### CyberArk and Ansible

- [ansible.com: Simplifying secrets management with CyberArk and Red Hat Ansible Automation Platform](https://www.ansible.com/blog/simplifying-secrets-management-with-cyberark-and-red-hat-ansible-automation-platform)
- [ansible.com: Automating Security with CyberArk and Red Hat Ansible Automation Platform](https://www.ansible.com/blog/automating-security-with-cyberark-and-red-hat-ansible-automation-platform)

### CyberArk Conjur

- [conjur.org](https://www.conjur.org/)
- [infracloud.io: Securing Kubernetes Secrets with Conjur 🌟](https://www.infracloud.io/blogs/securing-kubernetes-secrets-conjur)

### SOPS for Kubernetes

- [dev.to: Manage your secrets in Git with SOPS for Kubernetes 🌟](https://dev.to/stack-labs/manage-your-secrets-in-git-with-sops-for-kubernetes-57me)

### AKS Secrets

- [==mehighlow.medium.com: Hardened-AKS/Secrets==](https://mehighlow.medium.com/hardened-aks-secrets-82351c43eac4) Commonly, an application requires access to data and, usually, such access must be restricted. So, you need to provide your pod/deployment/replicaSet/DaemonSet with secrets. Learn how you can do so in AKS

### Kapitan

- [Kapitan: Generic templated configuration management for Kubernetes, Terraform and other things](https://kapitan.dev)
- [medium: Declarative secret management for GitOps with Kapitan](https://medium.com/kapitan-blog/declarative-secret-management-for-gitops-with-kapitan-b3c596eab088)

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

### Bitwarden

- [thenewstack.io: Walkthrough: Bitwarden’s New Secrets Manager](https://thenewstack.io/walkthrough-bitwardens-new-secrets-manager/)
- [morey.tech: Bitwarden and External Secrets](https://morey.tech/technical%20blog/Bitwarden-And-External-Secrets/)

## Serverless Security Best Practices

- [10 Serverless security best practices](https://snyk.io/blog/10-serverless-security-best-practices/)

## Docker Images and Container Security

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
- [betterprogramming.pub: Secure Your Kubernetes Cluster With Seccomp](https://betterprogramming.pub/secure-your-kubernetes-cluster-with-seccomp-9403ecf831b2) A hands-on guide to applying the principle of least-privilege on container’s syscalls

### Sigstore

- [==sigstore.dev==](https://www.sigstore.dev/) A new standard for signing, verifying and protecting software. Making sure your software’s what it claims to be.
    - [youtube: Hands-on Introduction to sigstore | Rawkode Live](https://www.youtube.com/watch?v=fZfd4orrn8Y&ab_channel=RawkodeAcademy) In this tutorial, you’ll learn how to sign and verify container images with co-sign, with and without a private key.
- [==opensource.com: Sign and verify container images with this open source tool (sigstore)==](https://opensource.com/article/21/12/sigstore-container-images) The sigstore project aims at securing supply chain technology.

### Container security best practices

- [sysdig.com: Container security best practices: Ultimate guide 🌟](https://sysdig.com/blog/container-security-best-practices)
- [dzone: A Practical Guide for Container Security](https://dzone.com/articles/a-practical-guide-for-container-security) Explore container security's fundamental principles and strategies, learn 2 specific methods, and examine tools and techniques for securing keys, tokens, and passwords.

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
- [kubearmor.io](https://kubearmor.io/) Runtime protection for Kubernetes & other cloud Workloads. KubeArmor uses eBPF and Linux Security Modules (LSM) to provide policy based system
to restrict any unwanted, malicious behavior of cloud-native workloads at runtime.
    - [itnext.io: Protecting Your Kubernetes Environment With KubeArmor](https://itnext.io/protecting-your-kubernetes-environment-with-kubearmor-76b02fc2209b) In this article, you will learn how to use KubeArmor to define policies and protect your containerized workloads. You will test the setup against the ShellShock vulnerability and compare it to AppArmor.

## Helm Charts Security. Helm Secrets

- [medium: Who’s at the Helm?](https://dlorenc.medium.com/whos-at-the-helm-1101c37bf0f1) Or, how to deploy 25+ CVEs to prod in one command!
- [itnext.io: Helm 3 — Secrets management, an alternative approach 🌟](https://itnext.io/helm-3-secrets-management-4f23041f05c3)
- [==itnext.io: Manage Auto-generated Secrets In Your Helm Charts== 🌟](https://itnext.io/manage-auto-generated-secrets-in-your-helm-charts-5aee48ba6918)
- [dev-vibe.medium.com: Encrypt Helm sensitive data](https://dev-vibe.medium.com/encrypt-helm-sensitive-data-9d7622e41d00) A guide on how to stay safe when pushing helm values files containing Your passwords and other sensitive data to the version control tool.

## Password Recovery

- [hashcat](https://hashcat.net/hashcat/)

## Attacks on Kubernetes via Misconfigured Argo Workflows

- [intezer.com: New Attacks on Kubernetes via Misconfigured Argo Workflows](https://www.intezer.com/blog/container-security/new-attacks-on-kubernetes-via-misconfigured-argo-workflows/)

## PKI

- [==devops.com: How to Automate PKI for DevOps With Open Source Tools==](https://devops.com/how-to-automate-pki-for-devops-with-open-source-tools/) The ultimate goal of PKI for DevOps is to provision PKI credentials for business applications without hard-coded secrets, which is one less risk to concern the security team. The goal of DevOps for PKI is to automatically deploy a completely configured PKI solution, which is one less roadblock for DevOps teams.

## Network Intrusion Tools

- [==cybersecsi/HOUDINI: Hundreds of Offensive and Useful Docker Images for Network Intrusion==](https://github.com/cybersecsi/HOUDINI) - https://houdini.secsi.io

## Other Security Tools

- [itnext.io: Top 6 Threat Detection Tools for Containers](https://itnext.io/top-6-threat-detection-tools-for-containers-3dd80b77777e) Essentials to Securing Threats for Containerized Cloud-Native Applications
- [thenewstack.io: AWS Open Sources Security Tools](https://thenewstack.io/aws-open-sources-security-tools/) AWS is open sourcing its Cedar policy language and authorization engine and Snapchange, an open source snapshot-based fuzzing tool.

### Torq. No code Security Automation

- https://torq.io No-code Security Automation
- [sentinelone.com: Reducing Human Effort in Cybersecurity | Why We Are Investing in Torq’s Automation Platform](https://www.sentinelone.com/blog/reducing-human-effort-in-cybersecurity-why-we-are-investing-in-torqs-automation-platform/)

### Security-Guard

- [pkg.go.dev/knative.dev/security-guard](https://pkg.go.dev/knative.dev/security-guard)
- [developer.ibm.com: Secure microservices by monitoring behavior](https://developer.ibm.com/articles/secure-microservices-by-monitoring-behavior/) An open source Kubernetes-native extension to secure containerized applications.

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
- [blog.mimacom.com: A Summary of log4j Exploit in a Log4shell - What Happened and What You Can Do About It](https://blog.mimacom.com/log4j-in-a-log4shell/)
- [cyberscoop.com: The Log4j flaw is the latest reminder that quick security fixes are easier said than done](https://www.cyberscoop.com/log4j-hack-security-update-ransomware/)
- [vpnranks.com: Belgian Defense Ministry Under Cyber Attack Due to Log4j Vulnerability](https://www.vpnranks.com/news/belgian-defense-ministry-under-cyber-attack-due-to-log4j-vulnerability/)
- [dynatrace.com: Log4Shell vulnerability discovery and mitigation require automatic and intelligent observability](https://www.dynatrace.com/news/blog/log4shell-vulnerability-discovery-and-mitigation)
- [thenewstack.io: Yet Another Log4j Security Problem Appears](https://thenewstack.io/yet-another-log4j-security-problem-appears)
- [==cisagov/log4j-scanner==](https://github.com/cisagov/log4j-scanner) **log4j-scanner is a project derived from other members of the open-source community by CISA to help organizations identify potentially vulnerable web services affected by the log4j vulnerabilities.**
- [venturebeat.com: What Log4Shell teaches us about open source security](https://venturebeat.com/2021/12/18/what-log4shell-teaches-us-about-open-source-security/)
- [tanzu.vmware.com: Log4Shell Vulnerability Spotlights the Importance of Adopting Trusted Open Source Software Providers for the Enterprise](https://tanzu.vmware.com/developer/blog/log4shell-vulnerability-spotlights-the-importance-of-adopting-trusted-open-source-software-providers-for-the-enterprise/)
- [==google/log4jscanner==](https://github.com/google/log4jscanner) A log4j vulnerability filesystem scanner and Go package for analyzing JAR files.
- [thehackernews.com: Microsoft Warns of Continued Attacks Exploiting Apache Log4j Vulnerabilities](https://thehackernews.com/2022/01/microsoft-warns-of-continued-attacks.html)
- [zdnet.com: Log4j: Google and IBM call for list of critical open source projects](https://www.zdnet.com/article/log4j-after-white-house-meeting-google-calls-for-list-of-critical-open-source-projects/) After attending a meeting at the White House, Google also proposed creating an organization to serve as a marketplace for open source maintenance.

## Powershell

- [it.slashdot.org: And the Top Source of Critical Security Threats Is...PowerShell](https://it.slashdot.org/story/21/05/22/041242/and-the-top-source-of-critical-security-threats-ispowershell) Microsoft's CLI management tool was the source of more than a third of critical security threats detected by Cisco in the second half of 2020, according to eSecurity Planet.

## Nmap scripts

- [therecord.media: UK government plans to release Nmap scripts for finding vulnerabilities](https://therecord.media/uk-government-plans-to-release-nmap-scripts-for-finding-vulnerabilities/)
    - [ncsc.gov.uk: Introducing Scanning Made Easy](https://www.ncsc.gov.uk/blog-post/introducing-scanning-made-easy) Trial project makes vulnerability scanning easier.

## Let's Encrypt SSL certificates

- [techrepublic.com: How to create Let's Encrypt SSL certificates with acme.sh on Linux](https://www.techrepublic.com/article/how-to-create-lets-encrypt-ssl-certificates-with-acme-sh-on-linux/)

## WAF Web Application Firewall

- [thenewstack.io: WAF: Securing Applications at the Edge](https://thenewstack.io/waf-securing-applications-at-the-edge/)

## More Security Tools

- [zdnet.com: Google releases new open-source security software program: Scorecards](https://www.zdnet.com/article/google-releases-new-open-source-security-software-program-scorecards/) How safe is that open-source software in the Git library, the one with the questionable history? Scorecard 2.0 can quickly tell you just how secure, or not, it really is.
- [sysadminxpert.com: How to do Security Auditing of CentOS System Using Lynis Tool](https://sysadminxpert.com/how-to-do-security-auditing-of-centos-system-using-lynis-tool/)
- [tryhackme.com: Metasploit: Introduction](https://tryhackme.com/room/metasploitintro) An introduction to the main components of the Metasploit Framework. Metasploit is a powerful tool that can support all phases of a penetration testing engagement
- [bridgecrew](https://bridgecrew.io) The codified cloud security platform for developers. Complete security and compliance visibility streamlined into developer-friendly workflows.
    - [bridgecrew.io: Tutorial: Incorporate IaC Security in your CI/CD pipeline with Bridgecrew, Jenkins, and GitHub](https://bridgecrew.io/blog/tutorial-incorporate-iac-security-in-your-ci-cd-pipeline-with-bridgecrew-jenkins-and-github)
- [curiefense/curiefense](https://github.com/curiefense/curiefense) Curiefense extends Envoy proxy to defend against a variety of threats, including SQL and command injection, cross site scripting (XSS), account takeovers (ATOs) and more
- [==socket.dev: Introducing Socket==](https://socket.dev/blog/introducing-socket) Socket's mission is to make open source safer. A platform that protects your most critical apps from software supply chain attacks.
- [itbusinessedge.com: Okta vs. Azure AD: IAM Tool Comparison](https://www.itbusinessedge.com/security/okta-vs-azure-ad/)
- [deepfence/ThreatMapper 🌟](https://github.com/deepfence/ThreatMapper/) 🔥 🔥 Open source cloud native security observability platform. Linux, K8s, AWS Fargate and more. 🔥 🔥 ThreatMapper hunts for vulnerabilities in your production platforms and ranks these vulnerabilities based on their risk of exploitation. You can then prioritize the issues that present the greatest risk to the security of your applications.
- [github.com/goauthentik/authentik](https://github.com/goauthentik/authentik) authentik is an open-source Identity Provider focused on flexibility and versatility
- [github.com/openappsec/openappsec](https://github.com/openappsec/openappsec) open-appsec provides preemptive web app & API threat protection against OWASP-Top-10 and zero-day attacks. It can be deployed as an add-on to Kubernetes Ingress, NGINX, Envoy and API Gateways.
- [==Microsoft Security Copilot==](https://www.microsoft.com/en-us/security/business/ai-machine-learning/microsoft-security-copilot)
- [==github.com/prowler-cloud/prowler== 🌟🌟](https://github.com/prowler-cloud/prowler) **Prowler is an Open Source Security tool for AWS, Azure and GCP to perform Cloud Security best practices assessments, audits, incident response, compliance, continuous monitoring, hardening and forensics readiness. Includes CIS, NIST 800, NIST CSF, CISA, FedRAMP, PCI-DSS, GDPR, HIPAA, FFIEC, SOC2, GXP, Well-Architected Security, ENS and more.**

## Videos

??? note "Click to expand!"

	<center>
	<iframe width="560" height="315" src="https://www.youtube.com/embed/nrhxNNH5lt0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
	</center>

## Twitter

??? note "Click to expand!"

	<center>
	<blockquote class="twitter-tweet"><p lang="en" dir="ltr">End to End Encryption Explained<a href="https://twitter.com/hashtag/infosec?src=hash&amp;ref_src=twsrc%5Etfw">#infosec</a> <a href="https://twitter.com/hashtag/cybersecurity?src=hash&amp;ref_src=twsrc%5Etfw">#cybersecurity</a> <a href="https://twitter.com/hashtag/pentesting?src=hash&amp;ref_src=twsrc%5Etfw">#pentesting</a> <a href="https://twitter.com/hashtag/oscp?src=hash&amp;ref_src=twsrc%5Etfw">#oscp</a> <a href="https://twitter.com/hashtag/informationsecurity?src=hash&amp;ref_src=twsrc%5Etfw">#informationsecurity</a> <a href="https://twitter.com/hashtag/hacking?src=hash&amp;ref_src=twsrc%5Etfw">#hacking</a> <a href="https://twitter.com/hashtag/cissp?src=hash&amp;ref_src=twsrc%5Etfw">#cissp</a> <a href="https://twitter.com/hashtag/redteam?src=hash&amp;ref_src=twsrc%5Etfw">#redteam</a> <a href="https://twitter.com/hashtag/technology?src=hash&amp;ref_src=twsrc%5Etfw">#technology</a> <a href="https://twitter.com/hashtag/DataSecurity?src=hash&amp;ref_src=twsrc%5Etfw">#DataSecurity</a> <a href="https://twitter.com/hashtag/CyberSec?src=hash&amp;ref_src=twsrc%5Etfw">#CyberSec</a> <a href="https://twitter.com/hashtag/Hackers?src=hash&amp;ref_src=twsrc%5Etfw">#Hackers</a> <a href="https://twitter.com/hashtag/tools?src=hash&amp;ref_src=twsrc%5Etfw">#tools</a> <a href="https://twitter.com/hashtag/bugbountytips?src=hash&amp;ref_src=twsrc%5Etfw">#bugbountytips</a> <a href="https://twitter.com/hashtag/Linux?src=hash&amp;ref_src=twsrc%5Etfw">#Linux</a> <a href="https://twitter.com/hashtag/infosec?src=hash&amp;ref_src=twsrc%5Etfw">#infosec</a> <a href="https://twitter.com/hashtag/itsecurity?src=hash&amp;ref_src=twsrc%5Etfw">#itsecurity</a> <a href="https://twitter.com/hashtag/cybersecuritytips?src=hash&amp;ref_src=twsrc%5Etfw">#cybersecuritytips</a> <a href="https://twitter.com/hashtag/securitybreach?src=hash&amp;ref_src=twsrc%5Etfw">#securitybreach</a> <a href="https://twitter.com/hashtag/encryption?src=hash&amp;ref_src=twsrc%5Etfw">#encryption</a> <a href="https://t.co/eejf8JL9VF">pic.twitter.com/eejf8JL9VF</a></p>&mdash; Shubham Sharma (@Shubham_pen) <a href="https://twitter.com/Shubham_pen/status/1492781841383890946?ref_src=twsrc%5Etfw">February 13, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
	<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Critical Log Review Checklist For Security Incidents - by <a href="https://twitter.com/SANSInstitute?ref_src=twsrc%5Etfw">@SANSInstitute</a> <a href="https://twitter.com/hashtag/infosec?src=hash&amp;ref_src=twsrc%5Etfw">#infosec</a> <a href="https://twitter.com/hashtag/cybersecurity?src=hash&amp;ref_src=twsrc%5Etfw">#cybersecurity</a> <a href="https://twitter.com/hashtag/pentesting?src=hash&amp;ref_src=twsrc%5Etfw">#pentesting</a> <a href="https://twitter.com/hashtag/oscp?src=hash&amp;ref_src=twsrc%5Etfw">#oscp</a> <a href="https://twitter.com/hashtag/informationsecurity?src=hash&amp;ref_src=twsrc%5Etfw">#informationsecurity</a> <a href="https://twitter.com/hashtag/hacking?src=hash&amp;ref_src=twsrc%5Etfw">#hacking</a> <a href="https://twitter.com/hashtag/cissp?src=hash&amp;ref_src=twsrc%5Etfw">#cissp</a> <a href="https://twitter.com/hashtag/redteam?src=hash&amp;ref_src=twsrc%5Etfw">#redteam</a> <a href="https://twitter.com/hashtag/technology?src=hash&amp;ref_src=twsrc%5Etfw">#technology</a> <a href="https://twitter.com/hashtag/DataSecurity?src=hash&amp;ref_src=twsrc%5Etfw">#DataSecurity</a> <a href="https://twitter.com/hashtag/CyberSec?src=hash&amp;ref_src=twsrc%5Etfw">#CyberSec</a> <a href="https://twitter.com/hashtag/Hackers?src=hash&amp;ref_src=twsrc%5Etfw">#Hackers</a> <a href="https://twitter.com/hashtag/tools?src=hash&amp;ref_src=twsrc%5Etfw">#tools</a> <a href="https://twitter.com/hashtag/bugbountytips?src=hash&amp;ref_src=twsrc%5Etfw">#bugbountytips</a> <a href="https://twitter.com/hashtag/Linux?src=hash&amp;ref_src=twsrc%5Etfw">#Linux</a> <a href="https://twitter.com/hashtag/infosec?src=hash&amp;ref_src=twsrc%5Etfw">#infosec</a> <a href="https://twitter.com/hashtag/itsecurity?src=hash&amp;ref_src=twsrc%5Etfw">#itsecurity</a> <a href="https://twitter.com/hashtag/cybersecuritytips?src=hash&amp;ref_src=twsrc%5Etfw">#cybersecuritytips</a> <a href="https://t.co/4zWIq1pkYO">pic.twitter.com/4zWIq1pkYO</a></p>&mdash; Shubham Sharma (@Shubham_pen) <a href="https://twitter.com/Shubham_pen/status/1492812040490024961?ref_src=twsrc%5Etfw">February 13, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
	</center>