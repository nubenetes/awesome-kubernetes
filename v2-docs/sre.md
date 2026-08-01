---
description: "Top SRE resources for 2026, AI-ranked: Skills for Real Engineers, OpenSLO specification and more — curated Cloud Native tools, guides and references."
---
# Site Reliability Engineering (SRE)

!!! tip "Nubenetes V2 Elite Portal"
    You are browsing the AI-Curated V2 Elite Edition. Looking for the exhaustive list of references? Check out the [**V1 Historical Archive**](/v1/sre/).

!!! info "Architectural Context"
    Detailed reference for Site Reliability Engineering (SRE) in the context of Platform & Site Reliability.

## Architectural Foundations

### Kubernetes Tools

#### General Reference

  - [dzone: SRE vs. DevOps: SRE Is to DevOps What Scrum Is to Agile](https://dzone.com/articles/sre-vs-devopssre-is-to-devops-what-scrum-is-to-agi)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering dzone: SRE vs. DevOps: SRE Is to DevOps What Scrum Is to Agile in the Kubernetes Tools ecosystem.
  - [cncf.io: DevOps vs. SRE](https://www.cncf.io/blog/2020/07/17/site-reliability-engineering-sre-101-with-devops-vs-sre)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering cncf.io: DevOps vs. SRE in the Kubernetes Tools ecosystem.
  - [cncf.io: DevOps vs. SRE vs. Platform Engineering? The gaps might be smaller' than you think](https://www.cncf.io/blog/2022/07/01/devops-vs-sre-vs-platform-engineering-the-gaps-might-be-smaller-than-you-think)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering ==cncf.io: DevOps vs. SRE vs. Platform Engineering? The gaps might be smaller' than you think== in the Kubernetes Tools ecosystem.
  - [dzone.com: DevOps vs. SRE vs. Platform Engineer vs. Cloud Engineer](https://dzone.com/articles/devops-vs-sre-vs-platform-engineer-vs-cloud-engine)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering dzone.com: DevOps vs. SRE vs. Platform Engineer vs. Cloud Engineer in the Kubernetes Tools ecosystem.
## Careers

### DevOps and SRE

#### Skills Development

  - **(2022)** [dev.to: What You Need to Break into DevOps and SRE](https://dev.to/thenjdevopsguy/what-you-need-to-break-into-devops-and-sre-3fp5)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A foundational roadmap detailing the core operating system, networking, programming, and configuration management capabilities required to break into modern DevOps and SRE roles.
## Cloud Infrastructure

### Managed Kubernetes

#### Site Reliability Engineering

  - **(2021)** [openshift.com: From Ops to SRE - Evolution of the OpenShift Dedicated Team](https://www.redhat.com/en/blog/from-ops-to-sre-evolution-of-the-openshift-dedicated-team)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Analyses the operational and structural evolution of Red Hat's OpenShift Dedicated SRE team. Documents the shift from classic system administration to an automation-first SRE model to govern fleet-scale, multi-tenant Kubernetes platforms at high availability.
## Continuous Delivery

### Feature Management

#### Reliability Engineering

  - **(2021)** [devops.com: How SREs Benefit From Feature Flags](https://devops.com/how-sres-benefit-from-feature-flags)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Investigates the role of feature flags in risk mitigation. Demonstrates how isolating application deployment from runtime feature activation enables SREs to instantly disable buggy paths without executing a full application rollback.
### SLO Validation

#### REST Apis

  - **(2022)** [thenewstack.io: Validate Service-Level Objectives of REST APIs Using Iter8](https://thenewstack.io/validate-service-level-objectives-of-rest-apis-using-iter8) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Demonstrates utilizing Iter8 to execute programmatic SLO assertions on REST endpoints. Ideal for modern CI/CD patterns validating performance bounds before traffic transitions to production.
## Infrastructure  Bare Metal  UEFI Firmware And PXE Boot Optimization

  - **(2026)** [**How we reduced core unit boot time from hours to minutes**](https://blog.cloudflare.com/optimizing-core-unit-boot-time) <span class='md-tag md-tag--warning'>[EN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — This technical post explores how Cloudflare diagnosed and optimized a critical UEFI-stage boot bottleneck affecting their Gen12 bare-metal fleet of nearly 2,000 servers. Engineers traced the multi-hour reboot delays to an unoptimized linear search through empty network boot interfaces triggered after routine firmware updates. The resolution involved explicit PXE network boot sequence declarations, custom UEFI configuration validation steps using a stateful `uefi-same-hex` boolean flag, and iPXE automation that brought reboots down from hours to minutes.
## Observability

### Monitoring

#### SRE Fundamentals

  - **(2021)** [circonus.com: Monitoring for Success: What All SREs Need to Know](https://www.circonus.com/2021/04/monitoring-for-success-what-all-sres-need-to-know)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Examines monitoring frameworks focused on business outcomes rather than raw resource metrics. Guides SREs on setting up context-rich telemetry pipelines that prioritize application-level user experience over physical host utilization.
### Service Level Objectives

#### Community Events

  - **(2021)** [SLOconf](https://www.sloconf.com)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Official site of SLOconf, the premier developer conference and community space focused entirely on Service Level Objectives, error budgets, and reliability-driven service platforms.
#### Declarative Standards

  - **(2021)** [==OpenSLO specification 🌟==](https://github.com/OpenSLO/OpenSLO) <span class='md-tag md-tag--info'>⭐ 1496</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-cb0643a4" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 7 L 10 6 L 20 2 L 30 7 L 40 12 L 50 5" fill="none" stroke="url(#spark-grad-cb0643a4)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The vendor-agnostic OpenSLO specification defines standard YAML schemas for declaring SLOs, SLIs, and error budgets. In 2026, it remains the standard for orchestrating declarative system health models inside GitOps automation.
#### Gitops

  - **(2022)** [thenewstack.io: Automate User Satisfaction with This GitOps-Friendly Spec for Service Level Objectives](https://thenewstack.io/automate-user-satisfaction-with-this-gitops-friendly-spec-for-service-level-objectives) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explores using GitOps mechanics to track reliability definitions. Outlines managing SLO declarations as declarative code in Git repository workflows to programmatically configure observability tools.
#### Google Best Practices

  - **(2020)** [sre.google: The Art of SLOs](https://sre.google/resources/practices-and-processes/art-of-slos) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Google's structural guide to defining user-centric Service Level Indicators (SLIs) and Service Level Objectives (SLOs). Features processes to prevent metric fatigue and map indicators directly to consumer utility.
### Site Reliability Engineering (1)

#### Root Cause Analysis

  - **(2021)** [youtube: Platform9’s Madhura Maskasky says observability is also essential for diagnosing and debugging in order for SREs to "get to the root cause quickly enough so that you can feed that back to the development teams." 🌟](https://www.youtube.com/watch?v=tgRPlAQpHYk&ab_channel=TheNewStack)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Video analysis featuring Platform9 discussing the strategic role of observability in debugging distributed cloud-native infrastructures. Emphasizes establishing tight engineering feedback loops between SREs and application developer teams to dramatically reduce Mean Time to Resolution (MTTR).
## Operations

### Organizational Design

#### Operating Models

  - **(2022)** [thenewstack.io: Centralized vs. Decentralized Operations](https://thenewstack.io/sharing-the-operations-burden-centralized-vs-decentralized) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Analyzes the architectural and operational trade-offs of centralized operations versus decentralized embedded-SRE teams. Helps platform architects structure their engineering departments based on business unit autonomy and release velocity.
### Platform Engineering

#### Organizational Design (1)

  - **(2022)** [devops.com: SRE Vs. Platform Engineering: What’s the Difference?](https://devops.com/sre-vs-platform-engineering-whats-the-difference)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Differentiates the core focuses of Platform Engineering and SRE. Analyzes how SRE teams protect application reliability, while Platform Engineering optimizes developer velocity by packaging tools into Internal Developer Platforms (IDPs).
#### Strategic Alignment

  - **(2022)** [thenewstack.io: SRE vs. DevOps? Successful Platform Engineering Needs Both](https://thenewstack.io/sre-vs-devops-successful-platform-engineering-needs-both)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Argues that successful modern Platform Engineering requires marrying DevOps velocity patterns with SRE reliability practices inside the developer platform tooling layer.
### SRE Vs DevOps

#### Conceptual Frameworks

  - **(2022)** [dev.to: DevOps vs SRE: What's The Difference?](https://dev.to/thenjdevopsguy/devops-vs-sre-what-s-the-difference-560d)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Presents a clear conceptual division between DevOps and SRE. Articulates the common industry saying 'SRE implements DevOps' by demonstrating how SRE tools like SLOs and error budgets concretely measure DevOps goals.
  - **(2022)** [phoenixnap.com: SRE Vs. DevOps: Differences Explained 🌟](https://phoenixnap.com/blog/sre-vs-devops)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Deep-dive analysis comparing the technical implementation differences between DevOps practices and SRE methods. Concretely defines metrics like SLIs, SLOs, and SLA relationships.
#### Tooling

  - **(2021)** [youtube: Viktor Farcic - What is the difference between SRE and DevOps?](https://www.youtube.com/watch?v=jgW4r9FxItI&ab_channel=DevOpsToolkitbyViktorFarcic)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Technical video analysis contrasting the conceptual responsibilities of DevOps and SRE. Explores modern architectural pillars including service meshes, declarative GitOps workflows, DevSecOps integrations, and platform-driven self-healing mechanisms.
### Site Reliability Engineering (2)

#### Best Practices

  - **(2022)** [linkedin.com: SRE: Key Insights-"Done the right way”](https://www.linkedin.com/pulse/sre-key-insights-done-right-way-shankar-muniyappa)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Outlines foundational SRE principles emphasizing the alignment of software engineering practices with operations. Discusses error budgets, blameless postmortems, and building self-healing systems as pillars to avoid organizational friction.
  - **(2022)** [infracloud.io: Site Reliability Engineering (SRE) Best Practices](https://www.infracloud.io/blogs/sre-best-practices)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Compiles architectural and cultural patterns for establishing cloud-native SRE. Key focuses include automated toil elimination, disaster recovery automation, chaos engineering practices, and objective-based release gates.
#### Career Lifecycle

  - **(2021)** [devops.com: Day in the Life of a Site Reliability Engineer (SRE)](https://devops.com/day-in-the-life-of-a-site-reliability-engineer-sre)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An informative run-through of the operational reality of SRE. Explains typical workflows, on-call paging procedures, metric reviews, postmortem writing, and automated tool-building shifts.
#### Cloud Native Ecosystem

  - **(2022)** [thenewstack.io: How the SRE Experience Is Changing with Cloud Native 🌟](https://thenewstack.io/how-the-sre-experience-is-changing-with-cloud-native) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Discusses how the shift to highly dynamic microservices and declarative Kubernetes operators has changed SRE workloads. SREs now prioritize building internal control planes and standardizing platform telemetry over manual server patching.
#### Enterprise Architecture

  - **(2021)** [thenewstack.io: Google SRE: Site Reliability Engineering at a Global Scale](https://thenewstack.io/google-sre-site-reliability-engineering-at-a-global-scale) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Examines Google's massive-scale SRE methodologies. Detail-oriented profile covering how Google applies engineering to operations, manages error budgets across global infrastructures, and structures on-call shifts to protect engineering sanity.
#### Google Best Practices (1)

  - **(2020)** [cloud.google.com: SRE at Google: Our complete list of CRE life lessons 🌟](https://cloud.google.com/blog/products/devops-sre/sre-at-google-our-complete-list-of-cre-life-lessons) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A comprehensive aggregation of operational lessons compiled by Google's Customer Reliability Engineering (CRE) team. This resource serves as a core blueprint for implementing user-focused SLOs, identifying operational anti-patterns, and structuring incident communication paths.
#### Google SRE Book

  - **(2016)** [sre.google: sre-book - The Evolving SRE Engagement Model](https://sre.google/sre-book/evolving-sre-engagement-model) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Core chapter from Google's SRE Book defining the Service Engagement Model. Outlines operational boundaries, launch-readiness reviews, service onboarding criteria, and the programmatic handback of unstable systems to development teams.
#### Incident Management

  - **(2021)** [infoq.com: Observing and Understanding Failures: SRE Apprentices](https://www.infoq.com/presentations/sre-apprentices)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — InfoQ presentation highlighting pedagogical methods for onboarding junior SREs. Focuses on developing systemic mental models for debugging multi-tier failures and safely operating complex, distributed live environments.
#### Industry Trends

  - **(2022)** [devops.com: How the SRE Role Is Evolving](https://devops.com/how-the-sre-role-is-evolving)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Tracks the industry evolution of SRE from isolated teams to a core cross-functional engineering practice. Highlights the transition from managing static infrastructure to developing programmatic automation platforms.
#### Podcasts

  - **(2021)** [sre.google/prodcast](https://sre.google/prodcast)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Google's 'Prodcast' SRE series. Features in-depth architectural and organizational conversations with Google operations engineers regarding multi-region failovers, disaster planning, and fleet-wide maintenance.
#### Scalability

  - **(2021)** [toolbox.com: Site Reliability Engineering: What Is It and How Can It Help Scale Operations? 🌟](https://www.toolbox.com/tech/devops/articles/automating-sre-to-scale-operations)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Details how SRE scaling models prevent traditional operating overhead from scaling linearly with system volume. Emphasizes shifting operational efforts into reusable platform engineering products.
#### Skills Development (1)

  - **(2022)** [devops.com: Top Nine Skills for SREs to Master 🌟](https://devops.com/top-nine-skills-for-sres-to-master)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Highlights nine critical technical skills for SREs, including writing high-quality infrastructure automation, building telemetry dashboards, designing reliable distributed networks, and mastering cloud platform paradigms.
#### Tooling (1)

  - **(2022)** [getcortexapp.com: A guide to the best SRE tools](https://www.cortex.io/post/a-guide-to-the-best-sre-tools)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Cortex's architectural guide evaluating modern SRE tooling stacks. Highlights service catalogs, central tracking, alert deduplication, automated runbooks, and performance benchmarking.
  - **(2021)** [thenewstack.io: The Site Reliability Engineering Tool Stack](https://thenewstack.io/the-site-reliability-engineering-tool-stack)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explores the fundamental tooling categories necessary for robust SRE practices, spanning declarative Infrastructure as Code (IaC), performance profiling, on-call management, and automated monitoring integrations.
  - **(2021)** [thenewstack.io: The Best Site Reliability Engineering Tools in 2021](https://thenewstack.io/the-best-site-reliability-engineering-tools-in-2021)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An evaluative overview of top-tier reliability platforms. Focuses on tools addressing continuous anomaly detection, SLO dashboards, chaos engineering, and incident management pipelines.
## Reliability Engineering (1)

### Cloud Native Paradigms

  - **(2019)** [devops.com: SRE vs. DevOps vs. Cloud Native: The Server Cage Match](https://devops.com/sre-devops-cloud-native-server-cage-match)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A high-energy analysis contrasting SRE, DevOps, and Cloud Native architectures. Explores how container orchestration, microservices, and micro-deployments mandate both cultural DevOps adjustments and programmatic SRE automation to survive at scale.
### SRE

#### Best Practices (1)

  - **(2016)** [Google: What is Site Reliability Engineering (SRE)?](https://sre.google) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Google's central hub for SRE methodologies, offering deep documentation on managing risk, service level objectives, monitoring, alerting, and elimination of toil. Essential reading for system architects establishing production-readiness checklists.
### SRE Vs DevOps (1)

#### Industry Analysis

  - **(2019)** [devops.com: SRE vs. DevOps — a False Distinction?](https://devops.com/sre-vs-devops-false-distinction)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Deconstructs the industry debate regarding SRE and DevOps, arguing that comparing them creates a false dichotomy. Suggests that successful engineering organizations merge the collaborative philosophy of DevOps with the analytical, code-driven rigor of SRE.
#### Introductory Frameworks

  - **(2018)** [devops.com: Site Reliability Engineering 101: DevOps Versus SRE](https://devops.com/site-reliability-engineering-101-devops-versus-sre)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Provides an entry-level comparison of SRE and DevOps methodologies. Explains key tenets of both schools of thought, with a focus on how teams share operational ownership and handle blameless post-mortems to foster high-velocity engineering.
#### Open Source Culture

  - **(2018)** [opensource.com: What is an SRE and how does it relate to DevOps?](https://opensource.com/article/18/10/sre-startup)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An open-source community exploration of SRE's role within fast-paced startup environments. Outlines how small engineering teams can apply SRE principles incrementally without the overhead of massive dedicated operations divisions.
#### Organizational Frameworks

  - **(2018)** [cloud.google.com: SRE vs. DevOps: competing standards or close friends?](https://cloud.google.com/blog/products/devops-sre)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A key Google conceptual piece defining SRE as a concrete class implementation of the DevOps interface. Contrasts organizational goals, highlighting how SRE materializes abstract DevOps ideals through structured, software-oriented reliability standards.
#### Professional Roles

  - **(2019)** [linkedin: DevOps vs Site Reliability Engineering](https://www.linkedin.com/pulse/devops-vs-site-reliability-engineering-sean-washington)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A professional field perspective outlining differences in day-to-day responsibilities between SREs and DevOps engineers. Synthesizes roles to show that while DevOps builds the automated deployment pipelines, SRE builds the automated telemetry and resilience guardrails.
#### Synergies

  - **(2020)** [thenewstack.io: Where Site Reliability Engineering Overlaps with DevOps](https://thenewstack.io/where-the-site-reliability-engineer-role-overlaps-with-devops)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Examines the functional overlaps between SREs and DevOps professionals. Highlights how monitoring, CI/CD automation, and shared configuration management unify these roles into a cohesive system reliability and deployment delivery vehicle.
## Software Engineering

### Professional Development

#### Core Architectures

  - **(2025)** [==Skills for Real Engineers==](https://github.com/mattpocock/skills) <span class='md-tag md-tag--info'>⭐ 128202</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-1ae169fb" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 10 L 10 9 L 20 4 L 30 5 L 40 11 L 50 5" fill="none" stroke="url(#spark-grad-1ae169fb)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — An exceptionally popular repository detailing the foundational principles, design philosophies, and architectural protocols required for master-level software delivery. While the curator focuses on career advancement, live engineering practice indicates that mastering these fundamentals is vital to surviving rapid AI development shifts. It represents an elite reference for engineering standardizations.

---
💡 **Explore Related:** [Developerportals](./developerportals.md) | [QA](./qa.md) | [Project Management Tools](./project-management-tools.md)

🔗 **See Also:** [AWS Pricing](./aws-pricing.md) | [Ansible](./ansible.md)

