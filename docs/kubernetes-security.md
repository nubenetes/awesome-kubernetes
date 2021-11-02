# Kubernetes Security
- [Introduction](#introduction)
- [Service Accounts](#service-accounts)
- [Kubernetes Secrets](#kubernetes-secrets)
- [Encrypting the certificate for Kubernetes. SSL certificates with Let's Encrypt in Kubernetes Ingress via cert-manager](#encrypting-the-certificate-for-kubernetes-ssl-certificates-with-lets-encrypt-in-kubernetes-ingress-via-cert-manager)
- [RBAC](#rbac)
- [Admission Control](#admission-control)
- [Security Best Practices Across Build, Deploy, and Runtime Phases](#security-best-practices-across-build-deploy-and-runtime-phases)
- [Kubernetes Authentication and Authorization](#kubernetes-authentication-and-authorization)
    - [Kubernetes Authentication Methods](#kubernetes-authentication-methods)
    - [X.509 client certificates](#x509-client-certificates)
    - [Static HTTP Bearer Tokens](#static-http-bearer-tokens)
    - [OpenID Connect](#openid-connect)
    - [Implementing a custom Kubernetes authentication method](#implementing-a-custom-kubernetes-authentication-method)
- [Pod Security Policies (SCCs - Security Context Constraints in OpenShift)](#pod-security-policies-sccs---security-context-constraints-in-openshift)
- [EKS Security](#eks-security)
- [Tweets](#tweets)

## Introduction
* [cilium.io](https://cilium.io/)
* [Dzone - devops security at scale](https://dzone.com/articles/devops-security-at-scale)
* [Dzone - Kubernetes Policy Management with Kyverno](https://dzone.com/articles/kubernetes-policy-management-with-kyverno)
    * [github Kyverno - Kubernetes Native Policy Management](https://github.com/nirmata/kyverno/)
    * [nirmata.com: Auto-labeling Kubernetes resources with Kyverno](https://nirmata.com/2020/10/30/auto-labeling-kubernetes-resources-with-kyverno)
* [Dzone - OAuth 2.0](https://dzone.com/articles/oauth-20-beginners-guide)
* [Kubernetes Security Best Practices 🌟](https://github.com/freach/kubernetes-security-best-practice/blob/master/README.md#firewall-ports-fire)
* [jeffgeerling.com: Everyone might be a cluster-admin in your Kubernetes cluster](https://www.jeffgeerling.com/blog/2020/everyone-might-be-cluster-admin-your-kubernetes-cluster)
* [Microsoft.com: Attack matrix for Kubernetes 🌟](https://www.microsoft.com/security/blog/2020/04/02/attack-matrix-kubernetes/)
* [codeburst.io: 7 Kubernetes Security Best Practices You Must Follow](https://codeburst.io/7-kubernetes-security-best-practices-you-must-follow-ae32f1ed6444)
* [thenewstack.io: Laying the Groundwork for Kubernetes Security, Across Workloads, Pods and Users](https://thenewstack.io/laying-the-groundwork-for-kubernetes-security-across-workloads-pods-and-users/)
* [horovits.wordpress.com: Kubernetes Security Best Practices](https://horovits.wordpress.com/2020/07/15/kubernetes-security-best-practices/)
* [containerjournal.com: How to Secure Your Kubernetes Cluster 🌟](https://containerjournal.com/topics/container-security/how-to-secure-your-kubernetes-cluster/)
* [medium: How to Harden Your Kubernetes Cluster for Production 🌟](https://medium.com/better-programming/how-to-harden-your-kubernetes-cluster-for-production-7e47990efc2a)
* [kubernetes.io: Cloud native security for your clusters](https://kubernetes.io/blog/2020/11/18/cloud-native-security-for-your-clusters/)
* [tldrsec.com: Risk8s Business: Risk Analysis of Kubernetes Clusters 🌟](https://tldrsec.com/guides/kubernetes/) A zero-to-hero guide for assessing the security risk of your Kubernetes cluster and hardening it.
* [microsoft.com: Threat matrix for Kubernetes 🌟](https://www.microsoft.com/security/blog/2020/04/02/attack-matrix-kubernetes/)
* [labs.bishopfox.com: Bad Pods: Kubernetes Pod Privilege Escalation 🌟](https://labs.bishopfox.com/tech-blog/bad-pods-kubernetes-pod-privilege-escalation) What are the risks associated with overly permissive pod creation in Kubernetes? The answer varies based on which of the host’s namespaces and security contexts are allowed. In this post, I will describe eight insecure pod configurations and the corresponding methods to perform privilege escalation. This article and the accompanying repository were created to help penetration testers and administrators better understand common misconfiguration scenarios.
* [sysdig.com: Kubernetes Security Guide 🌟](https://sysdig.com/resources/ebooks/kubernetes-security-guide/) Best practices, guidance and steps for implementing Kubernetes security.
* [resources.whitesourcesoftware.com: Kubernetes Security Best Practices 🌟](https://resources.whitesourcesoftware.com/blog-whitesource/kubernetes-security)
* [sysdig.com: Getting started with Kubernetes audit logs and Falco 🌟](https://sysdig.com/blog/kubernetes-audit-log-falco/)
* [thenewstack.io: Jetstack Secure Promises to Ease Kubernetes TLS Security](https://thenewstack.io/jetstack-secure-promises-to-ease-kubernetes-tls-security/)
* [thenewstack.io: Best Practices for Securely Setting up a Kubernetes Cluster](https://thenewstack.io/best-practices-for-securely-setting-up-a-kubernetes-cluster/)
* [stackrox/Kubernetes_Security_Specialist_Study_Guide 🌟](https://github.com/stackrox/Kubernetes_Security_Specialist_Study_Guide)
* [thenewstack.io: A Security Comparison of Docker, CRI-O and Containerd 🌟](https://thenewstack.io/a-security-comparison-of-docker-cri-o-and-containerd/)
* [github.com/stackrox: Certified Kubernetes Security Specialist Study Guide 🌟](https://github.com/stackrox/Kubernetes_Security_Specialist_Study_Guide)
* [youtube: Kubernetes Security: Attacking and Defending K8s Clusters - by Magno Logan](https://www.youtube.com/watch?v=OOHmg1J_8ck&ab_channel=RedTeamVillage)
* [cncf.io: Kubernetes Security 🌟](https://www.cncf.io/blog/2021/03/22/kubernetes-security/)
* [microsoft.com: Secure containerized environments with updated threat matrix for Kubernetes](https://www.microsoft.com/security/blog/2021/03/23/secure-containerized-environments-with-updated-threat-matrix-for-kubernetes/)
* [kyverno.io 🌟](https://kyverno.io/) Kubernetes Native Policy Management. Open Policy Agent? That’s old school. Securely manage workloads on your kubernetesio clusters with this handy new tool, Kyverno.Kyverno is a policy engine designed for Kubernetes. With Kyverno, policies are managed as Kubernetes resources and no new language is required to write policies. This allows using familiar tools such as kubectl, git, and kustomize to manage policies. Kyverno policies can validate, mutate, and generate Kubernetes resources. The Kyverno CLI can be used to test policies and validate resources as part of a CI/CD pipeline. [youtube: The Way of the Future | Kubernetes Policy Management with Kyverno](https://www.youtube.com/watch?v=8fgrjBnxqi0&t=270s&ab_channel=AppSecEngineer) - [youtube: Securing and Automating Kubernetes with Kyverno](https://www.youtube.com/watch?v=0cJAfmQ7Emg&ab_channel=CloudNativeIslamabad)
    * [kyverno.io/policies 🌟](https://kyverno.io/policies/) K8s policies available in the community repository
* [cyberark.com: Attacking Kubernetes Clusters Through Your Network Plumbing: Part 1](https://www.cyberark.com/resources/threat-research-blog/attacking-kubernetes-clusters-through-your-network-plumbing-part-1?utm_sq=goa40uvlx1)
* [redkubes.com: 10 Kubernetes Security Risks & Best Practices](https://redkubes.com/10-kubernetes-security-risks-best-practices/)
* [thenewstack.io: Defend the Core: Kubernetes Security at Every Layer](https://thenewstack.io/defend-the-core-kubernetes-security-at-every-layer/)
* [techmanyu.com: Kubernetes Security with Kube-bench and Kube-hunter 🌟](https://www.techmanyu.com/kubernetes-security-with-kube-bench-and-kube-hunter-6765bf44ebc6)
    * [kube-bench 🌟](https://github.com/aquasecurity/kube-bench) Checks whether Kubernetes is deployed according to security best practices as defined in the CIS Kubernetes Benchmark
    * [kube-hunter 🌟](https://github.com/aquasecurity/kube-hunter) Hunt for security weaknesses in Kubernetes clusters
    * [k21academy.com: Secure and Harden Kubernetes, AKS and EKS Cluster with kube-bench, kube-hunter and CIS Benchmarks 🌟](https://k21academy.com/docker-kubernetes/kubernetes-security/kube-bench-cis/)
* [Analyze Kubernetes Audit logs using Falco 🌟](https://github.com/developer-guy/falco-analyze-audit-log-from-k3s-cluster) Detect intrusions that happened in your Kubernetes cluster through audit logs using Falco
* [blog.kasten.io: Kubernetes Ransomware Protection with Kasten K10 v4.0](https://blog.kasten.io/ransomware-protection-kasten-k10-v4)
* [helpnetsecurity.com: Kubestriker: A security auditing tool for Kubernetes clusters 🌟](https://www.helpnetsecurity.com/2021/05/04/security-kubernetes/) Kubestriker is an open-source, platform-agnostic tool for identifying security misconfigurations in Kubernetes clusters.
* [Kubernetes Goat 🌟](https://madhuakula.com/kubernetes-goat) is designed to be an intentionally vulnerable cluster environment to learn and practice Kubernetes security.
* [itnext.io: How-To: Kubernetes Cluster Network Security 🌟](https://itnext.io/how-to-kubernetes-cluster-network-security-f19bc99161f5)
* [gist.github.com: How to protect your ~/.kube/ configuration](https://gist.github.com/PatrLind/e651d3cbc3bf68e4bd9fcc9568cbd3fb)
* [levelup.gitconnected.com: Enforce Audit Policy in Kubernetes (k8s)](https://levelup.gitconnected.com/enforce-audit-policy-in-kubernetes-k8s-34e504733300)
* [snyk.io: 10 Kubernetes Security Context settings you should understand](https://snyk.io/blog/10-kubernetes-security-context-settings-you-should-understand/)
* [magalix.com: Top 8 Kubernetes Security Best Practices 🌟](https://www.magalix.com/blog/top-8-kubernetes-security-best-practices)
* [redhat.com: The State of Kubernetes Security](https://www.redhat.com/en/blog/state-kubernetes-security)
* [igorzhivilo.com: Network policy and Calico CNI to Secure a Kubernetes cluster](https://igorzhivilo.com/saas/network-policy-calico-kubernetes/)
* [fairwinds.com: Discover the Top 5 Kubernetes Security Mistakes You're (Probably) Making](https://www.fairwinds.com/blog/top-5-kubernetes-security-mistakes)
* [tigera.io: Kubernetes security policy design: 10 critical best practices 🌟](https://www.tigera.io/blog/kubernetes-security-policy-10-critical-best-practices/)
* [empresas.blogthinkbig.com: Descubierta una vulnerabilidad en Kubernetes que permite acceso a redes restringidas (CVE-2020-8562)](https://empresas.blogthinkbig.com/descubierta-vulnerabilidad-kubernetes-permite-acceso-redes-restringidas-cve-2020-8562/)
* [thenewstack.io: Kubernetes: An Examination of Major Attacks 🌟](https://thenewstack.io/kubernetes-an-examination-of-major-attacks/) Constant vigilance is required to ensure that cloud infrastructure is locked down and that DevSecOps teams have the right tools for the job. 
* [nsa.gov: NSA, CISA release Kubernetes Hardening Guidance 🌟🌟](https://www.nsa.gov/News-Features/Feature-Stories/Article-View/Article/2716980/nsa-cisa-release-kubernetes-hardening-guidance/)
    * [Kubernetes Hardening Guidance 🌟🌟](https://media.defense.gov/2021/Aug/03/2002820425/-1/-1/1/CTR_KUBERNETES%20HARDENING%20GUIDANCE.PDF)
    * [thenewstack.io: The NSA Can Help Secure Your Kubernetes Clusters](https://thenewstack.io/the-nsa-can-help-you-secure-your-kubernetes-clusters/)
    * [therecord.media: NSA, CISA publish Kubernetes hardening guide 🌟🌟](https://therecord.media/nsa-cisa-publish-kubernetes-hardening-guide/)
        - Scan containers and Pods for vulnerabilities or misconfigurations. 
        - Run containers and Pods with the least privileges possible.  
        - Use network separation to control the amount of damage a compromise can cause.  
        - Use firewalls to limit unneeded network connectivity and encryption to protect confidentiality.  
        - Use strong authentication and authorization to limit user and administrator access as well as to limit the attack surface.
        - Use log auditing so that administrators can monitor activity and be alerted to potential malicious activity.
        - Periodically review all Kubernetes settings and use vulnerability scans to help ensure risks are appropriately accounted for and security patches are applied.
    * [cloud.redhat.com: OpenShift and the NSA-CISA ‘Kubernetes Hardening Guidance’](https://cloud.redhat.com/blog/openshift-and-the-nsa-cisa-kubernetes-hardening-guidance) Red Hat OpenShift is the quickest path to meeting the NSA’s Kubernetes hardening guidance
    * [Kubescape 🌟](https://github.com/armosec/kubescape) **kubescape is the first tool for testing if Kubernetes is deployed securely as defined in Kubernetes Hardening Guidance by to NSA and CISA.** Tests are configured with YAML files, making this tool easy to update as test specifications evolve.
        * [infoq.com: Armo Releases Kubescape K8s Security Testing Tool: Q&A with VP Jonathan Kaftzan](https://www.infoq.com/news/2021/09/kubescape/)
    * [infoq.com](https://www.infoq.com/news/2021/09/kubernetes-hardening-guidance/) NSA and CISA Publish Kubernetes Hardening Guidance
    * [csoonline.com: Kubernetes hardening: Drilling down on the NSA/CISA guidance](https://www.csoonline.com/article/3629049/kubernetes-hardening-drilling-down-on-the-nsa-cisa-guidance.html) The new guidance gives a solid foundation for hardening Kubernetes container environments. These are its key components and why they are important.
* [cloud.redhat.com: Top Open Source Kubernetes Security Tools of 2021 🌟🌟](https://cloud.redhat.com/blog/top-open-source-kubernetes-security-tools-of-2021)
* [cncf.io: How to secure your Kubernetes control plane and node components](https://www.cncf.io/blog/2021/08/20/how-to-secure-your-kubernetes-control-plane-and-node-components/)
* [redhat.com: State of Kubernetes Security Report - Spring 2021 (PDF) 🌟](https://www.redhat.com/rhdc/managed-files/cl-state-kubernetes-security-report-ebook-f29117-202106-en.pdf)
* [kubernetes.io: Overview of Cloud Native Security 🌟🌟](https://kubernetes.io/docs/concepts/security/overview/) This overview defines a model for thinking about Kubernetes security in the context of Cloud Native security.
* [elastisys.com: NSA and CISA Kubernetes Security Guidance: Summarized and Explained](https://elastisys.com/nsa-and-cisa-kubernetes-security-guidance-summarized-and-explained/)
* [learn.hashicorp.com: Integrate a Kubernetes Cluster with an External Vault 🌟](https://learn.hashicorp.com/tutorials/vault/kubernetes-external-vault)
* [talkingquickly.co.uk: Kubernetes Single Sign On - A detailed guide 🌟](http://www.talkingquickly.co.uk/kubernetes-sso-a-detailed-guide)
* [armosec.io: A Practical Guide to the Different Compliance Kubernetes Security Frameworks and How They Fit Together 🌟🌟](https://www.armosec.io/blog/kubernetes-security-frameworks-and-guidance)
* [thenewstack.io: How to Secure Kubernetes, the OS of the Cloud](https://thenewstack.io/how-to-secure-kubernetes-the-os-of-the-cloud/)
* [akhilsharma.work: The 4C's of Kubernetes Security](https://akhilsharma.work/the-4cs-of-kubernetes-security/)
* Kubernetes security thing: Always be careful of what you are letting your users choose for usernames. If someone has a username of **system:kube-controller-manager** on an external Identity system, Kubernetes will quite happily give them the rights of the controller manager. The **--oidc-username-prefix** and **--oidc-groups-prefix** flags are userful for preventing this in OIDC integrations.

<center>
[![kubernetes security mindmap](images/k8s_securitymindmap.jpg)](https://www.blackhat.com/)
</center>

## Service Accounts
* Service account is an important concept in terms of Kubernetes security. You can relate it to AWS instance roles and google cloud instance service account if you have a cloud background. By default, every pod gets assigned a default service account if you don't specify a custom service account. Service account allows pods to make calls to the API server to manage the cluster resources using ClusterRoles or resources scoped to a namespace using Roles. Also, you can use the Service account token from external applications to make API calls to the kubernetes API server. 
    * [devopscube.com: How To Create Kubernetes Service Account For API Access](https://devopscube.com/kubernetes-api-access-service-account/)
    * [devopscube.com: How to Create kubernetes Role for Service Account](https://devopscube.com/create-kubernetes-role/)
    * [github.com/scriptcamp/kubernetes-serviceaccount-example](https://github.com/scriptcamp/kubernetes-serviceaccount-example) Example Kubernetes manifests to create service account mapped to Rolebinding.
* [medium: Working with Service Account In Kubernetes 🌟](https://medium.com/the-programmer/working-with-service-account-in-kubernetes-df129cb4d1cc) How to configure a service account in Kubernetes and manage it?
* [github.com/dvob/k8s-s2s-auth: Kubernetes Service Accounts 🌟](https://github.com/dvob/k8s-s2s-auth) Service accounts are well known in Kubernetes to access the Kubernets API from within the cluster. This is often used for infrastructure components like operators and controllers. But we can also use service accounts to implement authentication in our own applications. This README tries to give an overview on how service accounts work and and shows a couple of variants how you can use them for authentication. Further this repository contains an example Go service which shows how to implement the authentication in an application.
* [sandeepbaldawa.medium.com: Service Accounts in K8s (Kubernetes)](https://sandeepbaldawa.medium.com/service-accounts-in-k8s-kubernetes-2779ee4fb331)

## Kubernetes Secrets
- [cncf.io: Revealing the secrets of Kubernetes secrets 🌟](https://www.cncf.io/blog/2021/04/22/revealing-the-secrets-of-kubernetes-secrets) In this article you will learn how to protect Secrets in your Kubernetes cluster
- [Hands on your first Kubernetes secrets 🌟](https://www.padok.fr/en/blog/kubernetes-secrets)
- [dev.to: Store your Kubernetes Secrets in Git thanks to Kubeseal. Hello SealedSecret! 🌟](https://dev.to/stack-labs/store-your-kubernetes-secrets-in-git-thanks-to-kubeseal-hello-sealedsecret-2i6h)
- [blog.doit-intl.com: Kubernetes and Secrets Management in the Cloud](https://blog.doit-intl.com/kubernetes-and-secrets-management-in-cloud-858533c20dca)
- [itnext.io: Effective Secrets with Vault and Kubernetes](https://itnext.io/effective-secrets-with-vault-and-kubernetes-9af5f5c04d06)  
- [kubernetes.io: Encrypting Secret Data at Rest 🌟](https://kubernetes.io/docs/tasks/administer-cluster/encrypt-data/)
- ["Kubernetes base64 encodes secrets because that makes arbitrary data play nice with JSON. It had nothing to do with the security model (or lack thereof). It did not occur to us at the time that people could mistake base64 for some form of encryption"](https://twitter.com/originalavalamp)
    * ["I've always wondered how folks expect a system would be able to protect data at rest like that. If the public key and private key are local on the machine - nothing is secure no matter what algorithm is used"](https://twitter.com/jwendlandt)
    * ["The issue is not new or unique to k8s. There is a general confusion between encoding and encryption. Ask any web dev about base64, and there is a good chance they'll tell you it's encryption"](https://twitter.com/codingsafari)
    * ["The test is clearly wrong if that is the word used, literally everything is encoded somehow. If they meant encrypted instead, then it's half true, secrets are encrypted in transit but only at rest if a KMS plugin is used"](https://twitter.com/originalavalamp)
    * ["The semantics are important. Easy to grant an RBAC policy like "read only except secrets"](https://twitter.com/tsh4k)
    * ["I just meant that base64 prevents you from logging a secret in plain text by accident… but many more layers are required to keep your secrets secret"](https://twitter.com/SWengThomas)
    * "You need to configure how the key is managed and ideally opt into something like KMS plugin (which depends on how the cluster is hosted) to make it good"
- [redhat.com: Managing secrets for Kubernetes pods](https://www.redhat.com/sysadmin/managing-secrets-kubernetes-pods)
- [enterprisersproject.com: How to explain Kubernetes Secrets in plain English 🌟](https://enterprisersproject.com/article/2019/8/kubernetes-secrets-explained-plain-english) What is a Kubernetes secret? How does this type of Kubernetes object increase security? How do you create a Kubernetes secret? What are some best practices? Experts break it down
- [millionvisit.blogspot.com: Kubernetes for Developers #19: Manage app credentials using Kubernetes Secrets 🌟](http://millionvisit.blogspot.com/2021/07/kubernetes-for-developers-19-manage-app-credentials-using-Kubernetes-Secrets.html)
- [kubermatic.com: Keeping the State of Apps Part 2: Introduction to Secrets](https://www.kubermatic.com/blog/keeping-the-state-of-apps-part-2-introduction-to-secrets/)
- [medium: Kubernetes Secrets Explained](https://medium.com/codex/kubernetes-secrets-explained-f45baf8cefa7)

## Encrypting the certificate for Kubernetes. SSL certificates with Let's Encrypt in Kubernetes Ingress via cert-manager
* [Kubernetes Certs](https://github.com/jetstack/cert-manager/)
* [Using SSL certificates from Let’s Encrypt in your Kubernetes Ingress via cert-manager 🌟](https://medium.com/flant-com/cert-manager-lets-encrypt-ssl-certs-for-kubernetes-7642e463bbce)
* [medium: Encrypting the certificate for Kubernetes (Let’s Encrypt) 🌟](https://medium.com/avmconsulting-blog/encrypting-the-certificate-for-kubernetes-lets-encrypt-805d2bf88b2a)
* [rejupillai.com: Let’s Encrypt the Web (for free)](https://www.rejupillai.com/index.php/2021/03/06/configure-tls-on-gke-ingress-for-free-with-lets-encrypt/)
* [betterprogramming.pub: Kubernetes and SSL Certificate Management 🌟](https://betterprogramming.pub/kubernetes-and-ssl-certificate-management-5f6a4b6f5ae9) Manage SSL certificate orders in K8s with Helm and Let’s Encrypt. 

## RBAC
* [Configure RBAC in Kubernetes Like a Boss 🌟](https://medium.com/trendyol-tech/configure-rbac-in-kubernetes-like-a-boss-665e2a8665dd) Learn how to configure RBAC in kubernetes. In this post, you will configure RBAC both with kubectl and yaml definitions.
* [infracloud.io: How to setup Role based access (RBAC) to Kubernetes Cluster 🌟](https://www.infracloud.io/blogs/role-based-access-kubernetes)
* [Kubernetes RBAC Permission Manager 🌟](https://toolbox.kali-linuxtr.net/kubernetes-rbac-permission-manager.tool)
* [Krane 🌟](https://github.com/appvia/krane) is a Kubernetes RBAC static analysis tool. It identifies potential security risks in K8s RBAC design and makes suggestions on how to mitigate them. Krane dashboard presents current RBAC security posture and lets you navigate through its definition.
* [rbac.dev 🌟🌟🌟](https://rbac.dev) advocacy site for Kubernetes RBAC. A site dedicated to good practices and tooling around Kubernetes RBAC. Both pull requests and issues are welcome.
    * For recipes, tips and tricks around RBAC see [recipes.rbac.dev 🌟](https://recipes.rbac.dev/)
* [github.com/clvx/k8s-rbac-model: Kubernetes RBAC Model](https://github.com/clvx/k8s-rbac-model) This is a implementation of a RBAC model for a multi project multi tenant Kubernetes cluster.
* [loft.sh: Kubernetes RBAC: Basics and Advanced Patterns](https://loft.sh/blog/kubernetes-rbac-basics-and-advanced-patterns/)

## Admission Control 
- [blog.styra.com: Why RBAC is not enough for kubernetes security 🌟🌟](https://blog.styra.com/blog/why-rbac-is-not-enough-for-kubernetes-api-security)
- [medium: Single Sign-On in Kubernetes 🌟](https://medium.com/@andriisumko/single-sign-on-in-kubernetes-1ad9528350ed)

## Security Best Practices Across Build, Deploy, and Runtime Phases
- [Kubernetes Security 101: Risks and 29 Best Practices 🌟](https://www.stackrox.com/post/2020/05/kubernetes-security-101/)
- Build Phase:
    1. Use minimal base images
    2. Don’t add unnecessary components
    3. Use up-to-date images only
    4. Use an image scanner to identify known vulnerabilities
    5. Integrate security into your CI/CD pipeline
    6. Label non-fixable vulnerabilities
- Deploy Phase:
    1. Use namespaces to isolate sensitive workloads
    2. Use Kubernetes network policies to control traffic between pods and clusters
    3. Prevent overly permissive access to secrets
    4. Assess the privileges used by containers
    5. Assess image provenance, including registries
    6. Extend your image scanning to deploy phase
    7. Use labels and annotations appropriately
    8. Enable Kubernetes role-based access control (RBAC)
- Runtime Phase:
    1. Leverage contextual information in Kubernetes
    2. Extend vulnerability scanning to running deployments
    3. Use Kubernetes built-in controls when available to tighten security
    4. Monitor network traffic to limit unnecessary or insecure communication
    5. Leverage process whitelisting
    6. Compare and analyze different runtime activity in pods of the same deployments
    7. If breached, scale suspicious pods to zero
- [thenewstack.io: 6 Kubernetes Security Best Practices 🌟](https://thenewstack.io/6-kubernetes-security-best-practices/)
- [kodekloud.com: Kubernetes Security Best Practices](https://kodekloud.com/kubernetes-security-best-practices/)

<center>
[![kubernetes security controls landscape](images/kubernetes-security-controls-landscape.jpg)](https://www.stackrox.com/post/2020/05/kubernetes-security-101/)
</center>

## Kubernetes Authentication and Authorization
* [kubernetes.io: Authenticating](https://kubernetes.io/docs/reference/access-authn-authz/authentication/)
* [kubernetes.io: Access Clusters Using the Kubernetes API](https://kubernetes.io/docs/tasks/administer-cluster/access-cluster-api/)
* [kubernetes.io: Accesing Clusters](https://kubernetes.io/docs/tasks/access-application-cluster/access-cluster/)
* [magalix.com: kubernetes authentication 🌟](https://www.magalix.com/blog/kubernetes-authentication)
* [magalix.com: kubernetes authorization 🌟](https://www.magalix.com/blog/kubernetes-authorization)
* [kubernetes login](https://blog.christianposta.com/kubernetes/logging-into-a-kubernetes-cluster-with-kubectl/)
* [learnk8s.io: Authentication between microservices using Kubernetes identities 🌟](https://learnk8s.io/microservices-authentication-kubernetes)
* [gravitational.com: How to Set Up Kubernetes SSO with SAML](https://gravitational.com/blog/kubernetes-sso-saml/)

### Kubernetes Authentication Methods
Kubernetes supports several authentication methods out-of-the-box, such as X.509 client certificates, static HTTP bearer tokens, and OpenID Connect.

### X.509 client certificates
* [Kubernetes Authentication and Authorization with X509 client certificates](https://medium.com/@sureshpalemoni/kubernetes-authentication-and-authorization-with-x509-client-certificates-edbc3517c10)

### Static HTTP Bearer Tokens 
* [kubernetes.io: Access Clusters Using the Kubernetes API](https://kubernetes.io/docs/tasks/administer-cluster/access-cluster-api/)
* [stackoverflow: Accessing the Kubernetes REST end points using bearer token](https://stackoverflow.com/questions/56214715/accessing-the-kubernetes-rest-end-points-using-bearer-token)

### OpenID Connect
* [OpenID Connect](https://openid.net/)

### Implementing a custom Kubernetes authentication method 
* [Implementing a custom Kubernetes authentication method](https://learnk8s.io/kubernetes-custom-authentication)

## Pod Security Policies (SCCs - Security Context Constraints in OpenShift)
* [Pod Security Policy (SCC in OpenShift) 🌟](https://kubernetes.io/docs/concepts/policy/pod-security-policy/)
* [rancher.com: Enhancing Kubernetes Security with Pod Security Policies, Part 1](https://rancher.com/blog/2020/pod-security-policies-part-1)
    * [rancher.com: Enhancing Kubernetes Security with Pod Security Policies, Part 2](https://rancher.com/blog/2020/pod-security-policies-part-2)
* [developer.squareup.com: Kubernetes Pod Security Policies (PSP)](https://developer.squareup.com/blog/kubernetes-pod-security-policies/) an example with exception management
* [itnext.io: Implementing a Secure-First Pod Security Policy Architecture](https://itnext.io/implementing-a-restricted-first-pod-security-policyarchitecture-af4e906593b0)
* [Neon Mirrors: Kubernetes Policy Comparison: OPA/Gatekeeper vs Kyverno](https://kind-brown-cfb734.netlify.app/post/2021-02/kubernetes-policy-comparison-opa-gatekeeper-vs-kyverno/)

## EKS Security
* [Security Group Rules EKS](https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html)
* [EC2 ENI and IP Limit](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html#AvailableIpPerENI)
* [Calico in EKS](https://docs.aws.amazon.com/eks/latest/userguide/calico.html )
* [Amazon EKS Best Practices Guide for Security 🌟](https://aws.github.io/aws-eks-best-practices/)
    * [EKS Best Practices Guide for Security 🌟](https://aws.github.io/aws-eks-best-practices/iam/)
* [medium.com: Securing Kubernetes Dashboard on EKS with Pomerium](https://medium.com/dev-genius/securing-kubernetes-dashboard-on-eks-with-pomerium-e98c47610e2f)

## Tweets
<details>
  <summary>Click to expand!</summary>

<center>
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Kubernetes base64 encodes secrets because that makes arbitrary data play nice with JSON. It had nothing to do with the security model (or lack thereof). It did not occur to us at the time that people could mistake base64 for some form of encryption.</p>&mdash; Daniel Smith (@originalavalamp) <a href="https://twitter.com/originalavalamp/status/1411755706861064192?ref_src=twsrc%5Etfw">July 4, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr"><a href="https://twitter.com/hashtag/OAuth?src=hash&amp;ref_src=twsrc%5Etfw">#OAuth</a> has 4 Flows for retrieving an Access Token.<br><br>If you have worked with it, you know how difficult is it to remember what is what.<br><br>A Zine says a lot, seriously a lot. Check this out.<br>Idea credits <a href="https://twitter.com/b0rk?ref_src=twsrc%5Etfw">@b0rk</a> <a href="https://twitter.com/hashtag/IAM?src=hash&amp;ref_src=twsrc%5Etfw">#IAM</a> <a href="https://twitter.com/hashtag/security?src=hash&amp;ref_src=twsrc%5Etfw">#security</a> <a href="https://twitter.com/hashtag/infosec?src=hash&amp;ref_src=twsrc%5Etfw">#infosec</a> <a href="https://twitter.com/hashtag/webdev?src=hash&amp;ref_src=twsrc%5Etfw">#webdev</a> <a href="https://twitter.com/hashtag/web?src=hash&amp;ref_src=twsrc%5Etfw">#web</a> <a href="https://twitter.com/hashtag/webcomic?src=hash&amp;ref_src=twsrc%5Etfw">#webcomic</a> <a href="https://twitter.com/hashtag/webcomics?src=hash&amp;ref_src=twsrc%5Etfw">#webcomics</a> <br>RT if useful <a href="https://t.co/fbrls0V08K">pic.twitter.com/fbrls0V08K</a></p>&mdash; Rohit (@sec_r0) <a href="https://twitter.com/sec_r0/status/1347603985096724493?ref_src=twsrc%5Etfw">January 8, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Kubernetes security best practices in short -<br><br>A Thread 👇 <a href="https://t.co/kehRjXuiEw">pic.twitter.com/kehRjXuiEw</a></p>&mdash; Rakesh Jain (@devops_tech) <a href="https://twitter.com/devops_tech/status/1446919546586087432?ref_src=twsrc%5Etfw">October 9, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Kubernetes security thing: Always be careful of what you are letting your users choose for usernames. If somone has a username of system:kube-controller-manager on an external Identity system, Kubernetes will quite happily give them the rights of the controller manager :)</p>&mdash; Rory McCune (@raesene) <a href="https://twitter.com/raesene/status/1455154869925449736?ref_src=twsrc%5Etfw">November 1, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</center>
</details>