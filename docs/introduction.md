# Introduction. From Java EE To Cloud Native. Microservice Architecture. Openshift VS Kubernetes
- [Introduction](#introduction)
- [Disaster Recovery](#disaster-recovery)
- [Multi Cloud](#multi-cloud)
- [Cloud Automation](#cloud-automation)
- [Microservices Best Practices](#microservices-best-practices)
- [Microservice Patterns](#microservice-patterns)
- [Cloud Migration Checklist](#cloud-migration-checklist)
- [Microservices Failures](#microservices-failures)
- [Transform Legacy Java Apps to Microservices with automation tools](#transform-legacy-java-apps-to-microservices-with-automation-tools)
- [Namespaces for Data Structuring](#namespaces-for-data-structuring)
- [From SysAdmin to Architect](#from-sysadmin-to-architect)
- [Raft Consensus Algorithm](#raft-consensus-algorithm)
- [PaaS](#paas)
- [Micro Frontends](#micro-frontends)
- [Modular Monolith](#modular-monolith)
- [From Java EE To Cloud Native](#from-java-ee-to-cloud-native)
- [Monolith to Microservices Using the Strangler Pattern](#monolith-to-microservices-using-the-strangler-pattern)
- [Openshift VS Kubernetes](#openshift-vs-kubernetes)
- [Career Path](#career-path)
- [Full Stack Developer's Roadmap](#full-stack-developers-roadmap)
- [Software Development Models](#software-development-models)
- [Software Development Tools](#software-development-tools)
- [vFunction. A system to transform monolithic Java applications into microservices](#vfunction-a-system-to-transform-monolithic-java-applications-into-microservices)
- [Bunch of Images](#bunch-of-images)
- [Videos](#videos)
- [Tweets](#tweets)

## Introduction
* [developers.redhat.com: Why Kubernetes is The New Application Server](https://developers.redhat.com/blog/2018/06/28/why-kubernetes-is-the-new-application-server/)
* [Dzone.com: Kubernetes in 10 minutes: A Complete Guide](https://dzone.com/articles/kubernetes-in-10-minutes-a-complete-guide-to-look)
* [redhat.com: Why choose Red Hat for microservices?](https://www.redhat.com/en/topics/microservices/why-choose-red-hat-microservices)
* [Monoliths are the future](https://changelog.com/posts/monoliths-are-the-future)
* [weave.works: Going Cloud Native: 6 essential things you need to know](https://www.weave.works/technologies/going-cloud-native-6-essential-things-you-need-to-know/)
* [Operators and Sidecars Are the New Model for Software Delivery](https://thenewstack.io/operators-and-sidecars-are-the-new-model-for-software-delivery/)
* [Dzone: What Is Kubernetes?](https://dzone.com/articles/what-is-kubernetes-in-devops) 
* [jaxenter.com: Practical Implications for Adopting a Multi-Cluster, Multi-Cloud Kubernetes Strategy](https://jaxenter.com/kubernetes-practical-implications-171647.html)
* [jaxenter.com: Six Essential Kubernetes Extensions to Add to Your Toolkit 🌟](https://jaxenter.com/kubernetes-extensions-172215.html)
* [thoughtworks.com: Kubernetes](https://www.thoughtworks.com/radar/platforms/kubernetes)
* [addwebsolution.com: How Kubernetes helps businesses manage their IT infrastructure?](https://addwebsolution.com/blog/how-kubernetes-helps-businesses-manage-their-it-infrastructure)
* [Dzone: How to Kill Your Developer Productivity](https://dzone.com/articles/how-to-kill-your-developer-productivity-humanitec)
* [loves.cloud: Kubernetes: An Introduction](https://loves.cloud/kubernetes-an-introduction/)
* [thenewstack.io: Microservices vs. Monoliths: An Operational Comparison](https://thenewstack.io/microservices-vs-monoliths-an-operational-comparison/)
* [weave.works: 6 Business Benefits of Kubernetes](https://www.weave.works/blog/6-business-benefits-of-kubernetes)
* [ituser.es: Las principales habilidades que un arquitecto cloud necesita para triunfar](https://www.ituser.es/opinion/2020/07/las-principales-habilidades-que-un-arquitecto-cloud-necesita-para-triunfar)
* [Introducing Domain-Oriented Microservice Architecture 🌟](https://eng.uber.com/microservice-architecture/)
* [Monolithic versus Microservice architecture](https://www.enterprisetimes.co.uk/2020/07/23/monolithic-versus-microservice-architecture)
* [Modernize legacy applications with containers, microservices](https://searchcloudcomputing.techtarget.com/feature/Modernize-legacy-applications-with-containers-microservices) To break down monolithic apps and modernize them for cloud deployment, enterprise development teams continue to turn to containers and microservices.
* [blog.heroku.com: Deconstructing Monolithic Applications into Services](https://blog.heroku.com/monolithic-applications-into-services)
* [vmware.com: How to Deconstruct a Monolith using Microservices – Getting Ready for Cloud-Native](https://blogs.vmware.com/vov/2018/08/06/how-to-deconstruct-a-monolith-using-microservices-getting-ready-for-cloud-native/)
* [thenewstack.io: 7 Best Practices to Build and Maintain Resilient Applications and Infrastructure](https://thenewstack.io/7-best-practices-to-build-and-maintain-resilient-applications-and-infrastructure/)
* [viewnext.com: Front End vs Back End (spanish)](https://www.viewnext.com/front-end-vs-back-end/)
* [thenewstack.io: What is the modern cloud native stack? 🌟🌟](https://thenewstack.io/what-is-the-modern-cloud-native-stack/)
* [thenewstack.io: Do I Really Need Kubernetes? 🌟](https://thenewstack.io/do-i-really-need-kubernetes/)
* [cncf.io: Top 7 challenges to becoming cloud native](https://www.cncf.io/blog/2020/09/15/top-7-challenges-to-becoming-cloud-native/)
* [dewanahmed.com: When to go K8s-native - A tale of CI/CD servers](https://www.dewanahmed.com/post/tekton-k8snative-cicd-pt1/)
* [lavanguardia.com: Por qué la transformación digital es mentira 🌟](https://www.lavanguardia.com/economia/20201014/484036217179/transformacion-digital-empresas-foncillas-pf-video-seo-lv.html)
* [devops.com: 6 Advantages of Microservices](https://devops.com/6-advantages-of-microservices/)
* [cloudpundit.com: Don’t boil the ocean to create your cloud 🌟](https://cloudpundit.com/2020/09/22/dont-boil-the-ocean-to-create-your-cloud/)
* [hcltech.com: DevOps Tools and Technologies to Manage Microservices 🌟](https://www.hcltech.com/blogs/devops-tools-and-technologies-manage-microservices) 
* [redhat.com: A sysadmin's guide to containerizing applications](https://www.redhat.com/sysadmin/containerizing-applications) Curious how to containerize your Linux applications? Learn by example, and understand the challenges of various application types and how to overcome them.
* [opensource.com: 6 container concepts you need to understand](https://opensource.com/article/20/12/containers-101) Containers are everywhere, and they've radically changed the IT landscape. What do you need to know about them?
* [devops.com: Why Boring Tech is Best to Avoid a Microservices Mess](https://devops.com/why-boring-tech-is-best-to-avoid-a-microservices-mess/)
* [blog.upbound.io: Managed Services Don’t Always Lead to Vendor Lock-In 🌟](https://blog.upbound.io/managed-services-dont-always-lead-to-vendor-lock-in/)
* [softwareengineeringdaily.com: Kubernetes vs. Serverless with Matt Ward (podcast) 🌟](https://softwareengineeringdaily.com/2020/12/29/kubernetes-vs-serverless-with-matt-ward-repeat/)
* [softwareengineeringdaily.com: The Rise of Platform Engineering 🌟](https://softwareengineeringdaily.com/2020/02/13/setting-the-stage-for-platform-engineering/)
* [thenewstack.io: 3 Reasons Why You Can’t Afford to Ignore Cloud Native Computing 🌟](https://thenewstack.io/3-reasons-why-you-cant-afford-to-ignore-cloud-native-computing/)
* [thenewstack.io: Defining a Different Kubernetes User Interface for the Next Decade](https://thenewstack.io/defining-a-different-kubernetes-user-interface-for-the-next-decade/)
* [thenewstack.io: React in Real-Time with Event-Driven APIs](https://thenewstack.io/react-in-real-time-with-event-driven-apis/)
* [codeopinion.com: Splitting up a Monolith into Microservices 🌟](https://codeopinion.com/splitting-up-a-monolith-into-microservices/)
* [towardsdatascience.com: Learning From Microservices — as a Data Engineer 🌟](https://towardsdatascience.com/learning-from-microservices-as-a-data-engineer-1334ce13876c) Why Software Engineers moved to microservices and how we could learn from their experience 
* [javarevisited.blogspot.com: Why Every Programmer, DevOps Engineer Should learn Docker and Kubernetes in 2020](https://javarevisited.blogspot.com/2020/11/why-devops-engineer-learn-docker-kubernetes.html)
* [techrepublic.com: Kubernetes will deliver the app store experience for enterprise software, says Weaveworks CEO](https://www.techrepublic.com/article/kubernetes-will-deliver-the-app-store-experience-for-enterprise-software-says-weaveworks-ceo/)
* [shahirdaya.medium.com: What does it mean to be Cloud Native? 🌟](https://shahirdaya.medium.com/what-does-it-mean-to-be-cloud-native-12360a324571)
* [enterprisersproject.com: 5 hybrid cloud trends to watch in 2021](https://enterprisersproject.com/article/2021/1/5-hybrid-cloud-trends-2021) As hybrid cloud becomes the go-to model for enterprise IT, watch for these trends. Experts discuss cloud platform changes, workload fit, security, and related issues
* [sysadminxpert.com: Scalability and Costs in the Cloud](https://sysadminxpert.com/scalability-and-costs-in-the-cloud/)
* [cloudify.co: Your Guide to Infrastructure Automation & Hybrid Cloud Orchestration 🌟](https://cloudify.co/everything-you-need-to-know-about-hybrid-cloud/)
* [jaxenter.com: Kubernetes Is Much Bigger Than Containers: Here’s Where It Will Go Next](https://jaxenter.com/kubernetes-bigger-173675.html)
* [skamille.medium.com: Make Boring Plans](https://skamille.medium.com/make-boring-plans-9438ce5cb053)
* [cloud-melon.com: Under the hood of Kubernetes and microservices](https://cloud-melon.com/2019/12/26/under-the-hood-of-kubernetes-and-microservices/)
* [thenewstack.io: Study: Silos Are the Chief Impediment to IT and Business Value](https://thenewstack.io/study-silos-are-chief-impediment-to-it-and-business-value/)
* [dzone: 10 Mandatory Services You Should Consider Adopting in AWS and Azure 🌟](https://dzone.com/articles/10-mandatory-services-you-should-consider-adopting) Thanks to the cloud revolution, the software engineering industry went from struggling to maintain IT infrastructure to selling software for subscription within a decade.
* [thenewstack.io: Prepare to Adopt the Cloud: A 10-Step Cloud Migration Checklist 🌟](https://thenewstack.io/prepare-to-adopt-the-cloud-a-10-step-cloud-migration-checklist/)
* [devprojournal.com: Containers, Kubernetes and Software Development in 2021](https://www.devprojournal.com/technology-trends/kubernetes/containers-kubernetes-and-software-development-in-2021/) Advice, expertise, and tools are available to help you get started developing with containers.
* [infoq.com: Migrating Monoliths to Microservices with Decomposition and Incremental Changes](https://www.infoq.com/articles/migrating-monoliths-to-microservices-with-decomposition/)
* [getcortexapp.com: Why You Need a Microservices Catalog Tool](https://www.getcortexapp.com/post/why-you-need-a-microservices-catalog-tool)
* [ringcentral.co.uk: Software as a Service (SaaS)](https://www.ringcentral.co.uk/gb/en/blog/definitions/software-as-a-service-saas/)
* [levelup.gitconnected.com: Multi-Tenant Architecture](https://levelup.gitconnected.com/multi-tenant-architecture-8c1f597e069c)
* [shopify.engineering: Keeping Developers Happy with a Fast CI](https://shopify.engineering/faster-shopify-ci)
* [infoq.com: Saga Orchestration for Microservices Using the Outbox Pattern](https://www.infoq.com/articles/saga-orchestration-outbox/)
* [medium: A Design Analysis of Cloud-based Microservices Architecture at Netflix](https://medium.com/swlh/a-design-analysis-of-cloud-based-microservices-architecture-at-netflix-98836b2da45f) A comprehensive system design analysis of microservices architecture at Netflix to power its global video streaming services
* [analyticsinsight.net: Cloud Computing is the inevitable future of Data Analytics](https://www.analyticsinsight.net/cloud-computing-is-the-inevitable-future-of-data-analytics/)
* [zdnet.com: Multicloud deployments surge as Microsoft Azure duels with AWS](https://www.zdnet.com/google-amp/article/multicloud-deployments-surge-as-microsoft-azure-duels-with-aws/) All of the public cloud players are showing solid growth as the multicloud pie expands. Azure is closing the gap on AWS, but Google Cloud is making big inroads too.
* [blog.container-solutions.com: How Mature Is Your Microservices Architecture? 🌟](https://blog.container-solutions.com/how-mature-is-your-microservices-architecture)
* [techerati.com: Microservices in the Cloud-Native Era](https://www.techerati.com/features-hub/opinions/microservices-in-the-cloud-native-era/)
* [thenewstack.io: The Cloud Native Landscape: Platforms Explained](https://thenewstack.io/the-cloud-native-landscape-platforms-explained/)
* [thenewstack.io: Are Private Clouds Proliferating?](https://thenewstack.io/google-and-oracle-cloud-adoption-doubles-among-enterprises-3/)
* [thenewstack.io: Multicloud Challenges and Solutions](https://thenewstack.io/multicloud-challenges-and-solutions)
* [makeuseof.com: hich Container System Should You Use: Kubernetes or Docker?](https://www.makeuseof.com/kubernetes-or-docker/) Choosing a container system for is a straightforward choice between two systems. Should you choose Kubernetes or Docker?
* [infoworld.com: The decline of Heroku PaaS](https://www.infoworld.com/article/3614210/the-decline-of-heroku.html)
* [infoq.com: Principles for Microservice Design: Think IDEALS, Rather than SOLID](https://www.infoq.com/articles/microservices-design-ideals/)
* [thenewstack.io: The Scalability Myth](https://thenewstack.io/the-scalability-myth/)
* [thenewstack.io: The 4 Definitions of Multicloud: Part 1 — Data Portability](https://thenewstack.io/the-4-definitions-of-multicloud-part-1-data-portability/)
* [thenewstack.io: Multicloud Paves the Way for Cloud Native Resiliency Models](https://thenewstack.io/multicloud-paves-the-way-for-cloud-native-resiliency-models/)
* [techerati.com: Microservices in the Cloud-Native Era](https://www.techerati.com/features-hub/opinions/microservices-in-the-cloud-native-era/)
* [infoworld.com: 3 cloud architecture mistakes we all make, but shouldn't](https://www.infoworld.com/article/3616211/3-cloud-architecture-mistakes-we-all-make-but-shouldnt.html)
* [ringcentral.co.uk: Cloud Management 🌟](https://www.ringcentral.co.uk/gb/en/blog/definitions/cloud-management/)
* [rudderstack.com: Reinventing the On-Prem Deployment Model](https://rudderstack.com/blog/reinventing-the-on-prem-deployment-model)
* [medium: Honestly, We Shouldn’t Have Used Microservices](https://medium.com/codex/honestly-we-shouldnt-have-used-microservices-443582def48b)
* [hashicorp.com: Why Microservices? 🌟](https://www.hashicorp.com/resources/why-microservices)
* [stackoverflow.blog: Using Kubernetes to rethink your system architecture and ease technical debt 🌟](https://stackoverflow.blog/2021/05/19/rethinking-system-architecture-can-kubernetes-help-to-solve-rewrite-anxiety/)
* [thenewstack.io: Private vs. Public Cloud: How Kubernetes Shifts the Balance](https://thenewstack.io/private-vs-public-cloud-how-kubernetes-shifts-the-balance/)
* [medium: Microservices Architecture From A to Z 🌟](https://medium.com/swlh/microservices-architecture-from-a-to-z-7287da1c5d28)
* [skycrafters.io: Do Containers Really Contain? Virtual Machines vs. Containers 🌟](https://skycrafters.io/blog/2021/06/08/do-containers-really-contain/) 
* [itprotoday.com: Who's Winning in the Container Software Market 🌟](https://www.itprotoday.com/containers/whos-winning-container-software-market) Thanks to its container customer training, the $1 billion container software market is Red Hat’s to lose. Where do the other players stand?
* [cloud.google.com: What is Kubernetes? 🌟](https://cloud.google.com/learn/what-is-kubernetes)
* [simform.com: What is Multi Cloud? Why you Need a Multi Cloud Strategy?](https://www.simform.com/multi-cloud-strategy/)
* [blog.min.io: Mono Clouds vs Multi-Clouds & Hybrid Clouds](https://blog.min.io/monoclouds-vs-multiclouds-hybridclouds/)
* [xataka.com: La deuda técnica, un lastre para las tecnológicas: un estudio señala que los informáticos pierden casi un día de trabajo a la semana para solventarlas](https://www.xataka.com/pro/deuda-tecnica-lastre-para-tecnologicas-estudio-senala-que-informaticos-pierden-casi-dia-trabajo-a-semana-para-solventarlas)
* [dev.to: When it Pays to Choose Microservices 🌟](https://dev.to/typeable/when-it-pays-to-choose-microservices-12h5)
* [acloudguru.com: Public cloud vs private cloud: What’s the difference? 🌟](https://acloudguru.com/blog/business/public-cloud-vs-private-cloud-whats-the-difference)
* [medium: Container Fundamentals — Part 1](https://medium.com/techbeatly/container-fundamentals-part-i-445881a81b7)
* [thenewstack.io: The Future of Microservices? More Abstractions](https://thenewstack.io/the-future-of-microservices-more-abstractions/)
* [thenewstack.io: Transform and Future-Proof Your Architecture with MACH](https://thenewstack.io/transform-and-future-proof-your-architecture-with-mach/) Why Do So Many Companies Remain in These ‘Bad Marriages’ with Monolithic Vendors? Enter MACH (Microservices, API-first, Cloud native, Headless)
* [yellow.systems: How to Make a Scalable Web Application: Architecture, Technologies, Cost](https://yellow.systems/blog/how-to-build-a-scalable-web-application)
* [opensource.com: What do we call post-modern system administrators?](https://opensource.com/article/21/7/system-administrators) Our community discusses the responsibilities, possible titles, and potential skills of today's sysadmins.
* [thenewstack.io: Cloud Engineers Try Policy-as-Code to Cure Misconfiguration Woes](https://thenewstack.io/cloud-engineers-try-policy-as-code-to-cure-misconfiguration-woes/)
* [dzone: The Origins of Technical Debt](https://dzone.com/articles/the-origins-of-technical-debt) According to research in the topic, 59% of business leaders in Norway said technical debt was their primary obstacle preventing them from innovating.
* [acloudguru.com: 7 Common Cloud Adoption Mistakes (ebook)](https://go.acloudguru.com/cloud-adoption-mistakes-ebook)
* [medium: What is microservices and why is it different? 🌟](https://medium.com/microservices-for-net-developers/what-is-microservices-and-why-is-it-different-fac017cb8cf4)
* [dzone: How Your Application Architecture Has Evolved 🌟🌟](https://dzone.com/articles/how-your-application-architecture-evolved) In this post, I will discuss how application architecture, in my opinion, has evolved in the last few years and what has been the driving factor for each evolution.
* [simform.com: 6 Multi-Cloud Architecture Designs for an Effective Cloud Strategy 🌟](https://www.simform.com/blog/multi-cloud-architecture/)
* [dzone: A Study of Hosting and Managing on Hybrid Multi-Cloud 🌟](https://dzone.com/articles/a-study-of-hosting-and-managing-on-hybrid-multi-cl) This is my study of a real customer use case on GitOps, multi-cloud management system and, securing dynamic infrastructure secrets, using Red Hat’s open source technology
* [simform.com: Cloud Migration ebook](https://www.simform.com/cloud-migration-ebook/)
* [blog.snapblocs.com: Architecture as a Service: The Evolution of Cloud Computing “as a Service”](https://www.blog.snapblocs.com/post/architecture-as-a-service-theevolution-of-cloud-computing-asaservice)
* [n-ix.com: How to reduce your technical debt: An ultimate guide](https://www.n-ix.com/reduce-technical-debt/)
* [fylamynt.com: Mastering Cloud Automation in the Cloud-Native Era 🌟](https://www.fylamynt.com/post/mastering-cloud-automation-in-the-cloud-native-era) As cloud computing is increasingly getting adopted all over, automation is taking a prime stage these days in the cloud-native space to streamline and manage various IT-related tasks. In this article, we will discuss cloud automation and various aspects related in brief.
* [dynatrace.com: What are microservices? All you need to know](https://www.dynatrace.com/news/blog/what-are-microservices/)
* [medium: Monoliths vs Microservices](https://medium.com/getdefault-in/monoliths-vs-microservices-59cff20bb106)
* [dzone: Guaranteed Ways of Failing With Microservices](https://dzone.com/articles/guaranteed-ways-of-failing-with-microservices) Microservices cannot be used in every context. It is perfectly fine to not use microservices in applications that are small and can be managed easily as monolithic.
* [dzone: Top 6 Time Wastes as a Software Engineer](https://dzone.com/articles/top-time-wastes-as-a-software-engineer) Increase your productivity and advance in your career by avoiding these 6 time wastes.
* [thenewstack.io: Reasons to Opt for a Multicloud Strategy](https://thenewstack.io/reasons-to-opt-for-a-multicloud-strategy/)
* [developers.redhat.com: devnation/summer-camp 🌟](https://developers.redhat.com/devnation/summer-camp) A great resource to learn cloud-native, kubernetes, event-driven architecture and more.
* [community.hpe.com: Containers vs. VMs: What’s the difference?](https://community.hpe.com/t5/HPE-Ezmeral-Uncut/Containers-vs-VMs-What-s-the-difference/ba-p/7147090)
* [hiralee.medium.com: Software Architecture vs Design](https://hiralee.medium.com/software-design-vs-architecture-1da0a94322a4)
* [blog.deref.io: Containers Don't Solve Everything 🌟](https://blog.deref.io/containers-dont-solve-everything/) Our industry has made incredible strides in the past decade, thanks in part to technologies like Docker, Docker Compose, and Kubernetes. However, we are still figuring out how to do development in the heterogeneous environments in which we live.
* [thenewstack.io: Stop Technical Debt Before It Damages Your Company](https://thenewstack.io/stop-technical-debt-before-it-damages-your-company/)
* [geeksforgeeks.org: Microservice Architecture – Introduction, Challeneges & Best Practices](https://www.geeksforgeeks.org/microservice-architecture-introduction-challeneges-best-practices/)
* [redhat.com: Use automation to combat your increased workload](https://www.redhat.com/sysadmin/automation-combat-increased-workload)Tired of mundane, tedious, boring tasks? Automation improves your efficiency and frees your time to focus on new and innovative opportunities.
* [zdnet.com: Benefits of cloud computing: The pros and cons](https://www.zdnet.com/google-amp/article/cloud-computing-pros-and-cons/) A list of advantages and disadvantages of cloud computing, including some you may not know existed.
* [thenewstack.io: Intention-as Code: Making Self-Healing Infrastructure Work](https://thenewstack.io/intention-as-code-making-self-healing-infrastructure-work/) **Reliability is Non-Negotiable**

## Disaster Recovery
* [thenewstack.io: Disaster Recovery Is Different for the Cloud](https://thenewstack.io/disaster-recovery-is-different-for-the-cloud/)

## Multi Cloud
- [acloudguru.com: Sharing data in the cloud: 4 patterns you should know](https://acloudguru.com/blog/business/sharing-data-in-the-cloud-four-patterns-everyone-should-know)
- [architectelevator.com: Multi Cloud Architecture: Decisions and Options](https://architectelevator.com/cloud/hybrid-multi-cloud/) Multi cloud means different things to different people. A decision model helps bust the buzzwords and show the options clearly.
- [softwebsolutions.com: Why enterprises need to adopt a multi-cloud strategy](https://www.softwebsolutions.com/resources/multi-cloud-adoption-strategy.html)
## Cloud Automation
* [zdnet.com: The year ahead in DevOps and agile: bring on the automation, bring on the business involvement](https://www.zdnet.com/article/the-year-ahead-in-devops-and-agile-more-automation-more-business-involvement-needed/) DevOps has an automation problem, while agile has an identification problem. Both face organizational problems. Both are needed in the digital transformation shaping the months ahead.
* [thenewstack.io: What Is Cloud Automation and How Does It Benefit IT Teams? 🌟](https://thenewstack.io/what-is-cloud-automation-and-how-does-it-benefit-it-teams)

## Microservices Best Practices
- [dzone: 7 Microservices Best Practices for Developers 🌟](https://dzone.com/articles/7-microservices-best-practices-for-developers) In this article, we’ll look at some microservices best practices and suggest a few ways to help you design, orchestrate, and secure your microservices architecture.

## Microservice Patterns
- [capstonec.com: You Will Love These Cloud-native App Architecture Patterns 🌟](https://capstonec.com/2020/10/08/cloud-native-app-architecture-patterns)
- [developers.redhat.com: Application modernization patterns with Apache Kafka, Debezium, and Kubernetes](https://developers.redhat.com/articles/2021/06/14/application-modernization-patterns-apache-kafka-debezium-and-kubernetes)
- [blog.couchbase.com: 4 Patterns for Microservices Architecture in Couchbase](https://blog.couchbase.com/microservices-architecture-in-couchbase/)
- [medium: Pragmatic Microservices 🌟](https://medium.com/microservices-in-practice/microservices-in-practice-7a3e85b6624c)
- [infoq.com: Turning Microservices Inside-Out](https://www.infoq.com/articles/microservices-inside-out/) Your microservices should be more than simple RESTful APIs. They should also be publishing important events, such as a change feed. 
- [dotnetcurry.com: Microservices Architecture Pattern 🌟](https://www.dotnetcurry.com/microsoft-azure/microservices-architecture)
- [geeksarray.com: Microservice Architecture Pattern for Architects 🌟](https://geeksarray.com/blog/microservice-architecture-pattern-for-architects)

## Cloud Migration Checklist
- [betterprogramming.pub: A Cloud Migration Questionnaire for Solution Architects 🌟🌟](https://betterprogramming.pub/a-cloud-migration-questionnaire-for-solution-architects-dec7ffcf063e) The questions you must ask your customers before migrating their on-premise workload to AWS Cloud:
    - Why do you want to migrate to the cloud?
    - How many code changes can you afford as part of migration?
    - What type of database are you using?
    - What type of load balancers are you using?
    - What application servers and versions are you using?
    - What operating system are you using?
    - Is your application public facing?
    - Is your application stateful or stateless?
    - Is your application containerized?
    - What are the current resource requirements of the servers?
    - How is your workload variation?
    - What are your logging and monitoring requirements?
    - What is your current backup strategy?

## Microservices Failures
- [world.hey.com: Disasters I've seen in a microservices world 🌟🌟](https://world.hey.com/joaoqalves/disasters-i-ve-seen-in-a-microservices-world-a9137a51)

## Transform Legacy Java Apps to Microservices with automation tools
- [devops.com: Transform Legacy Java Apps to Microservices with vFunction](https://devops.com/transform-legacy-java-apps-to-microservices/)
- [devops.com: Function Automates Conversion of Java Apps to Microservices](https://devops.com/vfunction-automates-conversion-of-java-apps-to-microservices/)

## Namespaces for Data Structuring
* [blog.appsignal.com: Microservices Monitoring: Using Namespaces for Data Structuring 🌟](https://blog.appsignal.com/2021/01/06/microservices-monitoring-using-namespaces-for-data-structuring.html)

## From SysAdmin to Architect
- [redhat.com: 5 strategies to shift your career from sysadmin to architect](https://www.redhat.com/architect/from-sysadmin-to-architect) Many engineers make the shift from hands-on-keyboard system administration to building architectures as an architect. Here are five ways they make the shift.

## Raft Consensus Algorithm
- [The Raft Consensus Algorithm 🌟](https://raft.github.io/) [etcd](https://github.com/etcd-io/etcd) is a “distributed reliable key-value store for the most critical data of a distributed system”. It uses the Raft consensus algorithm which was designed to be easy to understand, to scale, and to operate. The protocol and the etcd implementation were very quickly adopted by large distributed systems like Kubernetes, large distributed databases or messaging frameworks, where consensus and strong consistency is a must. 

## PaaS
- [What is Platform as a Service Software?](https://www.trustradius.com/platform-as-a-service-paas)

## Micro Frontends
- [dzone: Micro Frontends With Example 🌟](https://dzone.com/articles/micro-frontends-by-example-8) Monolithic frontends are difficult to maintain, develop, test, and deploy. The solution is micro frontends. It is a type of architecture that can increase effectiveness and efficiency across teams.

## Modular Monolith
- [kamilgrzybek.com: Modular Monolith: A Primer 🌟](https://www.kamilgrzybek.com/design/modular-monolith-primer/)

## From Java EE To Cloud Native
- [wikipedia: Java Enterprise Edition (Java EE)](https://en.wikipedia.org/wiki/Java_Platform,_Enterprise_Edition)
- [lightbend.com: From Java EE To Cloud Native: The End Of The Heavyweight Era 🌟](https://www.lightbend.com/white-papers-and-reports/java-ee-to-cloud-native-modernization)

## Monolith to Microservices Using the Strangler Pattern
- [dzone: Monolith to Microservices Using the Strangler Pattern 🌟](https://dzone.com/articles/monolith-to-microservices-using-the-strangler-patt) The Strangler Pattern is a popular design pattern to incrementally transform your monolithic application into microservices by replacing a particular functionality with a new service. Once the new functionality is ready, the old component is strangled, the new service is put into use, and the old component is decommissioned altogether.
- [overops.com: Strangler Pattern: How to Deal With Legacy Code During the Container Revolution](https://www.overops.com/blog/strangler-pattern-how-to-keep-sane-with-legacy-monolith-applications/)

## Openshift VS Kubernetes
* [cloudowski.com: 10 most important differences between OpenShift and Kubernetes 🌟](https://cloudowski.com/articles/10-differences-between-openshift-and-kubernetes/)
* [Dzone.com: 4 Cluster Management Tools to Compare](https://dzone.com/articles/4-cluster-management-tools-to-compare)
* [Dzone.com: A Comparison of Kubernetes Distributions](https://dzone.com/articles/kubernetes-distributions-how-do-i-choose-one)
* [thestack.com: OpenShift in a world of KaaS 🌟](https://techerati.com/the-stack-archive/cloud/2018/10/18/openshift-in-a-world-of-kaas/)
* [medium.com: The Differences Between Kubernetes and Openshift](https://medium.com/levvel-consulting/the-differences-between-kubernetes-and-openshift-ae778059a90e)
* [blog.netsil.com: Kubernetes vs Openshift vs Tectonic: Comparing Enterprise Options](https://blog.netsil.com/kubernetes-vs-openshift-vs-tectonic-comparing-enterprise-options-e3a34dc60519)
* [kubedex.com: Kubernetes On-Prem, OpenShift vs PKS vs Rancher](https://kubedex.com/redhat-openshift-vs-pivotal-pks-vs-rancher/)
    * [reddit.com: OpenShift vs PKS vs Rancher 🌟](https://www.reddit.com/r/kubernetes/comments/9qxeuw/openshift_vs_pks_vs_rancher/)
* [elastisys.com: OpenShift Features and Their Kubernetes Counterparts 🌟](https://elastisys.com/2018/11/06/openshift-features-kubernetes-counterparts/)
* [medium.com: Kubernetes — What Is It, What Problems Does It Solve and How Does It Compare With Alternatives?](https://medium.com/@srikanth.k/kubernetes-what-is-it-what-problems-does-it-solve-how-does-it-compare-with-its-alternatives-937fe80b754f)
* [spec-india.com: Kubernetes VS Openshift (July 23rd 2019)](https://www.spec-india.com/blog/kubernetes-vs-openshift)
* [phoenixnap.com: Kubernetes vs OpenShift: Key Differences Compared 🌟](https://phoenixnap.com/blog/kubernetes-vs-openshift)
* [crn.com: Red Hat CEO: We Have A ‘Head Start’ Over VMware, Competitors In Kubernetes](https://www.crn.com/slide-shows/cloud/red-hat-ceo-we-have-a-head-start-over-vmware-competitors-in-kubernetes) Red Hat CEO Paul Cormier speaks with CRN about the role IBM has played in Red Hat’s channel strategy, how the company has preserved its independence under Big Blue, and why Red Hat will win in the ultra-competitive Kubernetes market.
* [redhat.com ebook: Red Hat OpenShift and Kubernetes ... what's the difference? 🌟](https://www.redhat.com/en/resources/openshift-and-kubernetes-whats-the-difference-ebook) 
* [levelup.gitconnected.com: OpenShift — The Next Level of Kubernetes](https://levelup.gitconnected.com/openshift-the-next-level-of-kubernetes-6d58ad722b26) Things you should need to know about OpenShift

## Career Path
- [Kelsey Hightower Fireside Chat: An Unconventional Path to IT and Some Life Advice](https://www.hashicorp.com/resources/kelsey-hightower-fireside-chat-an-unconventional-path-to-it-and-some-life-advice/?utm_source=linkedin)
- [forbes.com: 13 Signs You’re Selling Yourself Short In Your Career](https://www.forbes.com/sites/adunolaadeshola/2021/04/28/13-signs-youre-selling-yourself-short-in-your-career/)

## Full Stack Developer's Roadmap
- [Full Stack Developer's Roadmap 🌟](https://dev.to/ender_minyard/full-stack-developer-s-roadmap-2k12)

## Software Development Models
- [dzone: 7 Software Development Models You Should Know](https://dzone.com/articles/7-software-development-models-you-should-know) Software Development Models are integral to the success (or failure) of a project. Here are 7 models you should know, from Waterfall to the V-Model to Scrum.

## Software Development Tools
- [ubiqum.com: 20 Software Development Tools that will make you more productive](https://ubiqum.com/blog/20-software-development-tools-that-will-make-you-more-productive/)
- [sloboda-studio.com: Python Tools for Machine Learning](https://sloboda-studio.com/blog/python-tools-for-machine-learning/)

## vFunction. A system to transform monolithic Java applications into microservices
- [vFunction](https://vfunction.com/) vFunction accelerates your journey to cloud native by automating Java app modernization.
- [thenewstack.io: vFunction Transforms Monolithic Java to Microservices](https://thenewstack.io/vfunction-transforms-monolithic-java-to-microservices/)

## Bunch of Images
<details>
  <summary>Click to expand!</summary>

<center>

[![microservices infographic](images/microservices-infographic.png)](https://www.weave.works/technologies/going-cloud-native-6-essential-things-you-need-to-know)

[![you dont need kubenetes](images/you_dont_need_kubernetes.jpg)](https://twitter.com/a_sykim)

[![sw consumers](images/softwareconsumers-1.png)](https://thenewstack.io/operators-and-sidecars-are-the-new-model-for-software-delivery)

[![Openshift SaaS VS Kubernetes SaaS](images/openshift-vs-kubernetes-saas.png)](https://proteon.com/2018/10/18/openshift-in-a-world-of-kubernetes-as-a-service/)

[![Openshift VS Kubernetes](images/openshift_vs_kubernetes.jpeg)](https://www.linkedin.com/feed/update/urn:li:activity:6459657167300583424)

[![Kubernetes on its own is not enough](images/k8s-not-enough.jpg)](https://twitter.com/brendandburns)

[![how mature is your microservices architecture](images/MicroservicesMaturityMatrix.jpg)](https://blog.container-solutions.com/how-mature-is-your-microservices-architecture)
</center>
</details>

## Videos
<details>
  <summary>Click to expand!</summary>

<center>
<iframe src="https://www.youtube.com/embed/Q6i0LK4vHsU" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</center>
</details>

## Tweets
<details>
  <summary>Click to expand!</summary>

<center>
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Questions to quickly spot red flags of a software project:<br><br>- how long does the CI pipeline take?<br>- how long is the onboarding process?<br>- how short are the working cycles?<br>- what type of tests are integrated in the QA?<br>- is there any micromanagement?<br><br>What else would you add?</p>&mdash; Daniel Moka⚡ (@dmokafa) <a href="https://twitter.com/dmokafa/status/1358385361588781067?ref_src=twsrc%5Etfw">February 7, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">THREAD<br><br>The <a href="https://twitter.com/learnk8s?ref_src=twsrc%5Etfw">@Learnk8s</a> Twitter account is expanding!<br><br>Starting today you will be able to follow 4x more news:<br><br>- Security focus Kubernetes news<br>- Kubernetes for devs and architects<br>- Job offers<br>- And … a surprise (read on)<br><br>Let me explain <a href="https://t.co/pAQJYw8Fn6">pic.twitter.com/pAQJYw8Fn6</a></p>&mdash; Daniele Polencic (@danielepolencic) <a href="https://twitter.com/danielepolencic/status/1389187636493918213?ref_src=twsrc%5Etfw">May 3, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">just read the words &quot;large monoliths are unmaintainable&quot;<br><br>NO<br><br>poorly structured systems are unmaintainable, regardless of the cardinality of their deployment topology</p>&mdash; Matt Stine (@mstine) <a href="https://twitter.com/mstine/status/1390373898286518274?ref_src=twsrc%5Etfw">May 6, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Micro Services Architecture Vs Monolith Architecture:<br><br> 🧵👇🏻 <a href="https://t.co/8W8Nvi9eJk">pic.twitter.com/8W8Nvi9eJk</a></p>&mdash; Sunil Kumar (@sunilc_) <a href="https://twitter.com/sunilc_/status/1401064227347976192?ref_src=twsrc%5Etfw">June 5, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">You don&#39;t need access to a credit card or AWS account in order to learn more about DevOps. <br><br>Start for free with Docker and GitHub. <br><br>Spend time to learn how to set up docker files and combine them with GitHub actions to automate your build process.</p>&mdash; Danny (@dannysteenman) <a href="https://twitter.com/dannysteenman/status/1417069210425958402?ref_src=twsrc%5Etfw">July 19, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Everyone sensible in IT has been saying for years that if you buy COTS (commercial off-the-shelf software packages) you shouldn’t customize it - it’s wildly expensive and you end up with something hard to maintain and almost impossible to upgrade.</p>&mdash; Jez Humble (@jezhumble) <a href="https://twitter.com/jezhumble/status/1422924762750210049?ref_src=twsrc%5Etfw">August 4, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">COTS is for business processes that aren’t strategic to your org. So you should MODIFY YOUR BUSINESS PROCESS TO FIT WHAT THE SOFTWARE DOES OUT OF THE BOX! Sorry for shouting, I’m old.</p>&mdash; Jez Humble (@jezhumble) <a href="https://twitter.com/jezhumble/status/1422924763647778821?ref_src=twsrc%5Etfw">August 4, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">The top 5 most widely used Cloud platforms according to the Stack Overflow Developer survey 2021:<br><br>1. AWS - 59%<br>2. Azure - 32% <br>3. GCP - 29%<br>4. Heroku - 21%<br>5. DigitalOcean - 18% <a href="https://t.co/56cqg70gZo">pic.twitter.com/56cqg70gZo</a></p>&mdash; Danny  (@dannysteenman) <a href="https://twitter.com/dannysteenman/status/1430390741583290375?ref_src=twsrc%5Etfw">August 25, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">💫 Cloud Knowledge 101<br><br>☁️ Public vs. Private vs. Hybrid Cloud ☁️<br><br>A quick comparison of these concepts 🧵👇</p>&mdash; Simon ☁️ (@simonholdorf) <a href="https://twitter.com/simonholdorf/status/1442170013226438660?ref_src=twsrc%5Etfw">September 26, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</center>
</details>