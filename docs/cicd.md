# Software Delivery Pipeline. CI/CD

1. [Introduction](#introduction)
2. [CI/CD Continuous Integration and Continuous Delivery](#cicd-continuous-integration-and-continuous-delivery)
3. [CI/CD Pipelines With Kubernetes](#cicd-pipelines-with-kubernetes)
4. [Observability](#observability)
5. [Code Review](#code-review)
6. [Security in CI/CD](#security-in-cicd)
7. [Progressive Delivery](#progressive-delivery)
8. [Deployment Strategies](#deployment-strategies)
9. [Pipeline Patterns](#pipeline-patterns)
10. [CI/CD with Kubernetes](#cicd-with-kubernetes)
11. [CI/CD with OpenShift](#cicd-with-openshift)
12. [CI/CD with AWS](#cicd-with-aws)
13. [Reports on the Enterprise CI/CD Market](#reports-on-the-enterprise-cicd-market)
14. [Tools](#tools)
15. [Awesome Lists](#awesome-lists)
16. [Images](#images)
17. [Videos](#videos)
18. [Tweets](#tweets)

## Introduction

- [opensource.com: What is CI/CD?](https://opensource.com/article/18/8/what-cicd)
- [Wikipedia.org: DevOps](https://en.wikipedia.org/wiki/DevOps)
- [Wikipedia.org: Continuous Integration](https://en.wikipedia.org/wiki/Continuous_integration)
- [Wikipedia.org: Continuous Delivery](https://en.wikipedia.org/wiki/Continuous_delivery)
- [martinfowler.com: Continuous Integration (original version)](https://martinfowler.com/articles/originalContinuousIntegration.html)

<center>
[![CD Artifact Management](images/cd-artifact-management.jpg)](https://www.thoughtworks.com/insights/continuous-delivery)
</center>

## CI/CD Continuous Integration and Continuous Delivery

- [DZone: Continuous Integration: Servers and Tools](https://dzone.com/refcardz/continuous-integration-servers) Learning to Utilize DevOps with Servers and Tools
- [sdtimes.com: CI/CD pipelines are expanding 🌟](https://sdtimes.com/devops/ci-cd-pipelines-are-expanding/) The “basic” CI/CD pipeline includes five processes, which are: merge, build, test, package and deploy. All of these are individually defined so readers have a common reference point. The basic pipeline includes sub-pipelines associated with each step, such as moving artifacts from a build into a repository.
- [devopsonline.co.uk: ChatOps, DevOps, ScrumOps and 5 Other Ops religions](https://www.devopsonline.co.uk/chatops-devops-scrumops-and-5-other-ops-religions/)
- [opensource.com: A beginner's guide to building DevOps pipelines with open source tools](https://opensource.com/article/19/4/devops-pipeline) If you're new to DevOps, check out this five-step process for building your first pipeline.
- [acloud.guru: How youtr org predicts your CI/CD pipeline](https://info.acloud.guru/resources/brazeal-how-your-org-predicts-your-ci/cd-pipeline)
- [dev.to: CI/CD Continuous Integration & Delivery Explained 🌟🌟](https://dev.to/semaphore/ci-cd-continuous-integration-delivery-explained-75l)
- [mindtheproduct.com: The Product Managers’ Guide to Continuous Delivery and DevOps 🌟🌟](https://www.mindtheproduct.com/what-the-hell-are-ci-cd-and-devops-a-cheatsheet-for-the-rest-of-us/)
- [tech.buzzfeed.com: Continuous Deployments at BuzzFeed](https://tech.buzzfeed.com/continuous-deployments-at-buzzfeed-d171f76c1ac4)
- [Dzone refcard: Continuous Delivery - Patterns and Anti-Patterns in the Software Lifecycle 🌟](https://dzone.com/refcardz/continuous-delivery-patterns)
- [infoworld.com: What is CI/CD? Continuous integration and continuous delivery explained](https://www.infoworld.com/article/3271126/what-is-cicd-continuous-integration-and-continuous-delivery-explained.html) The CI/CD pipeline is one of the best practices for devops teams to implement, for delivering code changes more frequently and reliably
- [devops.com: How to Implement an Effective CI/CD Pipeline](https://devops.com/how-to-implement-an-effective-ci-cd-pipeline/)
- [ammeon.com: 5 Tips For Building A CI/CD Pipeline](https://www.ammeon.com/5-tips-for-building-ci-cd-pipeline/)
- [medium: What is CI/CD Pipeline in DevOps? 🌟🌟](https://medium.com/faun/what-is-ci-cd-pipeline-in-devops-6fba17a76e73) Understanding the Importance of CI/CD Pipeline.
- [aws.amazon.com: Automating safe, hands-off deployments 🌟🌟](https://aws.amazon.com/es/builders-library/automating-safe-hands-off-deployments/)
- [techuz.com: What is CI/CD? An Introduction to Continuous Integration, Continuous Deployment and CI/CD Pipeline](https://www.techuz.com/blog/what-is-ci-cd-an-introduction-to-continuous-integration-continuous-deployment-and-ci-cd-pipeline/)
- [kodekloud.com: What is CI/CD Pipeline in DevOps](https://kodekloud.com/what-is-ci-cd-pipeline-in-devops) CI/CD plays an important role in your DevOps implementation path. Here are some important things to consider while building a CI/CD pipeline:
    - Peer code review
    - Build in a containerized environment
    - Shorten the feedback loop
    - Do CI first
    - Compare efficiency
    - Insert security checkpoints in the pipeline
    - Implement an easy way to rollback
    - Proactively monitor your CD pipeline
- [medium: How to build an efficient CI/CD pipeline 🌟🌟](https://medium.com/@sanjayaben/how-to-build-an-efficient-ci-cd-pipeline-b5738ad567c8)
- [Asking for Help Is a Best Practice When Building a CI/CD Pipeline](https://www.cloudbees.com/case-study/asking-help-best-practice-when-building-cicd-pipeline)
- [developers.redhat.com: The present and future of CI/CD with GitOps on Red Hat OpenShift](https://developers.redhat.com/blog/2020/09/03/the-present-and-future-of-ci-cd-with-gitops-on-red-hat-openshift/)
- [dewanahmed.com: When to go k8s-native - A tale of CI/CD servers](https://www.dewanahmed.com/post/tekton-k8snative-cicd-pt1/)
- [CI/CD Best Practices 🌟](https://blog.bitsrc.io/ci-cd-best-practices-bca0ef665677)
- [harness.io: What is a CI/CD Platform and why should I care? 🌟](https://harness.io/2020/10/what-is-cicd-platform-why-should-i-care/)
- [harness.io: 3 Ways to Use Automation in CI/CD Pipelines](https://thenewstack.io/3-ways-to-use-automation-in-ci-cd-pipelines/)
- [cloudbees.com: 7 Tips for Creating A Successful CI/CD Pipeline 🌟](https://www.cloudbees.com/blog/tips-creating-successful-cicd-pipeline)
- [dzone: CI/CD Pipeline: Demystifying The Complexities](https://dzone.com/articles/cicd-pipeline-demystifying-the-complexities) Get a high-level overview of CI/CD pipelines and the components that make up a DevOps process, and some of the challenges and benefits of a CI/CD pipeline.
- [javi-kata.medium.com: CI/CD the journey of a dummy team 🌟](https://javi-kata.medium.com/ci-cd-the-journey-of-a-dummy-team-f51a061684bc) This article tries to help people in how to achieve CI/CD starting from a feature branching model (gitflow).
- [thinkinglabs.io: Feature Branching considered evil 🌟](https://thinkinglabs.io/talks/feature-branching-considered-evil.html)
- [tripwire.com: Everything You Need to Know About CI/CD and Security](https://www.tripwire.com/state-of-security/devops/everything-need-to-know-about-ci-cd-security/)
- [harness.io: CI/CD Pipeline: Everything You Need to Know 🌟](https://harness.io/blog/continuous-delivery/ci-cd-pipeline/)
- [stackoverflow.blog: Fulfilling the promise of CI/CD 🌟](https://stackoverflow.blog/2021/01/19/fulfilling-the-promise-of-ci-cd/) When people say “CI/CD,” they are only talking about continuous integration. Nobody is talking about (or practicing) continuous deployment. AT ALL. It’s like we have all forgotten it exists. It's time to change that.
- [Top 5 CI/CD best practices for 2021 🌟](https://circleci.com/blog/top-5-ci-cd-best-practices/)
- [harness.io: What is Continuous Integration? 🌟](https://harness.io/blog/continuous-integration/what-is-continuous-integration/)
- [cd.foundation: 2021 Technology Trends and Predictions](https://cd.foundation/blog/2021/02/01/trends-that-will-define-ci-cd-in-2021/)
- [opsmx.com: What is a CI/CD Pipeline ?](https://www.opsmx.com/blog/what-is-a-ci-cd-pipeline)
- [continuousdelivery.com: Patterns 🌟](https://continuousdelivery.com/implementing/patterns/)
- [devops.com: 7 Popular Open Source CI/CD Tools](https://devops.com/7-popular-open-source-ci-cd-tools/)
- [testguild.com: Pipeline as Code with Mohamed Labouardy](https://testguild.com/podcast/automation/a345-mohamed/)
- [harness.io: Understanding the Phases of the Software Development Life Cycle](https://harness.io/blog/devops/software-development-life-cycle/)
- [cloudbees.com: Key Components of a CI/CD Pipeline](https://www.cloudbees.com/blog/ci-cd-pipeline)
- [blog.thundra.io: Why a CI/CD Pipeline Makes Good Business Sense](https://blog.thundra.io/why-a-ci/cd-pipeline-makes-good-business-sense)
- [jfrog.com: Cloud Native CI/CD: The Ultimate Checklist](https://jfrog.com/blog/cloud-native-ci-cd-the-ultimate-checklist/)
- [jfrog.com: How to Accelerate Software Delivery with Hybrid Cloud CI/CD (e-commerce) 🌟](https://jfrog.com/blog/how-to-accelerate-software-delivery-with-hybrid-cloud-ci-cd/)
- [harness.io: Streamlining CI/CD and Optimizing AWS Cloud Spend](https://harness.io/blog/continuous-integration/streamlining-ci-cd/)
- [sdtimes.com: The State of CI/CD](https://sdtimes.com/cicd/the-state-of-ci-cd/) “A few years ago, CI/CD started off as a method to help continuous deployment, but that definition of CI/CD is long defunct. CI/CD now has QA and security elements to it. We may have seen people refer to the current trend as DevSecOps. In my mind, DevSecOps is changing to be Dev-Infra-Sec-Ops (infrastructure-as-a-service) and will soon be called “Dev-Infra-Sec-Analytics-Ops (including analytics-as-a-service). One day the trend of CI/CD will eventually lead to touchless software development and maintenance. We are on the brink of major efficiency shift in the industry now and AI/ML and LCNC [low code/no code] technologies are enabling this shift.”
- [javacodegeeks.com: The Case Against CI/CD](https://www.javacodegeeks.com/2021/08/the-case-against-ci-cd.html) What’s the Point of CI/CD?
- [thenewstack.io: Improve Dev Experience to Maximize the Business Value of CD](https://thenewstack.io/improve-dev-experience-to-maximize-the-business-value-of-cd/)
- [community.dataminer.services: CI/CD and the Agile Principles](https://community.dataminer.services/ci-cd-and-the-agile-principles/)
- [medium: Automated Build and Deploy Pipelines for Kubernetes](https://medium.com/codezero-reflections/automated-build-and-deploy-pipelines-for-kubernetes-d268542cca52)
- [medium: Next Generation Kubernetes Deployments](https://medium.com/codezero-reflections/next-generation-kubernetes-deployments-12637eae9d68)
- [==levelup.gitconnected.com: Basics of CI/CD==](https://levelup.gitconnected.com/basics-of-ci-cd-a98340c60b04)
- [techrepublic.com: CI/CD platforms: How to choose the right continuous integration and delivery system for your business](https://www.techrepublic.com/article/how-to-choose-the-right-cicd-platform/)
- [==stackoverflow.blog: Fulfilling the promise of CI/CD==](https://stackoverflow.blog/2021/12/20/fulfilling-the-promise-of-ci-cd/) When people say “CI/CD,” they are only talking about continuous integration. Nobody is talking about (or practicing) continuous deployment. AT ALL. It’s like we have all forgotten it exists. It's time to change that.
- [==speakerdeck.com: Deployment Scripting != Continuous Delivery==](https://speakerdeck.com/devopslx/cd-and-optimized-cloud-spend?slide=12)
- [lambdatest.com: Top 10 CI/CD Pipeline Implementation Challenges And Solutions](https://www.lambdatest.com/blog/cicd-pipeline-challenges/)
- [devopsdigest.com: CI/CD Deployments: How to Expedite Across a Kubernetes Environment With DevOps Orchestration](https://www.devopsdigest.com/cicd-deployments-how-to-expedite-across-a-kubernetes-environment-with-devops-orchestration)
- [medium.com/softwareimprovementgroup: CI/CD best practices: How to set up your pipeline](https://medium.com/softwareimprovementgroup/ci-cd-best-practices-how-to-set-up-your-pipeline-4643eea14bfa)
- [medium.com/dynatrace-engineering: How to combine and automate infrastructure and application deployment in a microservice environment](https://medium.com/dynatrace-engineering/how-to-combine-and-automate-infrastructure-and-application-deployment-in-a-microservice-environment-a16b664bb8b5) A collection of best practices to improve your confidence in your deployed applications.
- [thenewstack.io: 4 Best Practices to Drive Successful Adoption of CI/CD](https://thenewstack.io/four-best-practices-to-drive-successful-adoption-of-ci-cd/)
- [about.gitlab.com: How to keep up with CI/CD best practices](https://about.gitlab.com/blog/2022/02/03/how-to-keep-up-with-ci-cd-best-practices/)
- [harness.io: Modern Software Delivery Best Practices & Software Delivery Management](https://harness.io/blog/software-delivery-best-practices/)
- [linkedin pulse: Enabling CI/CD to Boost DevOps | Pavan Belagatti](https://www.linkedin.com/pulse/enabling-cicd-boost-devops-pavan-belagatti/)
- [about.gitlab.com: How to learn CI/CD fast](https://about.gitlab.com/blog/2022/04/13/how-to-learn-ci-cd-fast/)
- [thenewstack.io: Are Monolith CI/CD Pipelines Killing Quality in Your Software?](https://thenewstack.io/are-monolith-ci-cd-pipelines-killing-quality-in-your-software/) This creates complex challenges for developers trying to push commits with confidence and DevOps teams responsible for fine-tuning their pipelines.
- [clickittech.com: CI/CD Best Practices: Top 10 Practices for Financial Services](https://www.clickittech.com/devops/ci-cd-best-practices/)
- [medium.com/@rifkikarimr: Continuous Integration and Continuous Deployment: Best Practices for DevOps 🌟](https://medium.com/@rifkikarimr/continuous-integration-and-continuous-deployment-best-practices-for-devops-b99eac071a5c) Explore the basics of CICD. What they're, why they’re important, how to set up CI/CD pipeline, the best practices for CI/CD, and how to overcome common challenges
- [==guru99.com: CI/CD Pipeline: Learn with Example== 🌟🌟🌟](https://www.guru99.com/ci-cd-pipeline.html) CICD automates the process of app delivery. It builds code, runs tests, helps to safely deploy new version of the app. It reduces manual errors, provides feedback, and allows fast product iterations.
- [==dzone.com: How To Build an Effective CI/CD Pipeline==](https://dzone.com/articles/how-to-build-an-effective-cicd-pipeline) This article leads you through an exploration of practical steps for creating pipelines that accelerate deployments.
- [groundcover.com: Cloud-native CI/CD? Yeah, that’s a thing 🌟](https://www.groundcover.com/blog/ci-cd-kubernetes) Discover how leveraging CI/CD pipelines based on Kubernetes gives organizations improved control and more efficient management, allowing for faster recovery and replication of runtime environments.
- [==spacelift.io: Kubernetes CI/CD Pipelines – 7 Best Practices and Tools | James Walker== 🌟](https://spacelift.io/blog/kubernetes-ci-cd) CICD pipelines enhance app delivery process by automating key stages like testing, security scanning, and deployment. Adopting pipeline-based workflow helps to ship more quickly.
- [thenewstack.io: Embracing Database Deployments in CI/CD Practices with Git](https://thenewstack.io/embracing-database-deployments-in-ci-cd-practices-with-git/) Databases have not been well integrated into the CI/CD tooling landscape, but applying git-like concepts can help.
- [hart-michael.medium.com: Why You Need Continuous Deployment](https://hart-michael.medium.com/why-you-need-continuous-deployment-93d7b5936523)

## CI/CD Pipelines With Kubernetes

- [==dzone.com: An Overview of CI/CD Pipelines With Kubernetes==](https://dzone.com/articles/an-overview-of-cicd-pipelines-with-kubernetes) Take a look at CI/CD approaches in a Kubernetes ecosystem, best practices for implementing an efficient CI/CD framework, and popular open-source CI/CD tools.
- [==thenewstack.io: Kubernetes CI/CD Pipelines Explained==](https://thenewstack.io/kubernetes-ci-cd-pipelines-explained/) Building an effective CI/CD pipeline requires diligent technical analysis, a generous amount of planning and choosing the right set of tools.

## Observability

- [==betanews.com: Overcoming observability challenges in the CI/CD Pipeline==](https://betanews.com/2022/01/26/overcoming-observability-challenges/)

## Code Review

- [developers.redhat.com: 10 tips for reviewing code you don't like](https://developers.redhat.com/blog/2019/07/08/10-tips-for-reviewing-code-you-dont-like)

## Security in CI/CD

- [CI Checks Are Not Enough: Combat Configuration Drift in Kubernetes Resources](https://thenewstack.io/ci-checks-are-not-enough-combat-configuration-drift-in-kubernetes-resources/)
- [devops.com: 8 Security Considerations for CI/CD](https://devops.com/8-security-considerations-for-ci-cd/)

## Progressive Delivery

- [split.io: Progressive Delivery](https://www.split.io/glossary/progressive-delivery/)
- [harness.io: Progressive Delivery: Everything You Need to Know](https://harness.io/blog/feature-flags/progressive-delivery/)
- [weave.works: Progressively Delivering Applications Across Cloud and On-Premise. Using Kuma & GitOps to implement canary releasing](https://www.weave.works/blog/progressively-delivering-applications-across-cloud-and-on-premise)

## Deployment Strategies

- [blog.container-solutions.com: Deployment Strategies 🌟](https://blog.container-solutions.com/deployment-strategies)
    - It really depends on the needs and budget. When releasing to development/staging environments, a recreate or ramped deployment is usually a good choice. When it comes to production, a ramped or blue/green deployment is usually a good fit, but proper testing of the new platform is necessary.
    - Blue/green and shadow strategies have more impact on the budget as it requires double resource capacity. If the application lacks in tests or if there is little confidence about the impact/stability of the software, then a canary, a/b testing or shadow release can be used. If your business requires testing of a new feature amongst a specific pool of users that can be filtered depending on some parameters like geolocation, language, operating system or browser features, then you may want to use the a/b testing technique.
    - Last but not least, a shadow release is complex and requires extra work to mock egress traffic which is mandatory when calling external dependencies with mutable actions (email, bank, etc.). However, this technique can be useful when migrating to a new database technology and use shadow traffic to monitor system performance under load.
- [harness.io: Intro to Deployment Strategies: Blue-Green, Canary, and More 🌟](https://harness.io/blog/continuous-verification/blue-green-canary-deployment-strategies/)
- [medium: Continuous Kubernetes blue-green deployments on Azure using Nginx, AppGateway or TrafficManager — part 2](https://medium.com/@denniszielke/continuous-kubernetes-blue-green-deployments-on-azure-using-nginx-appgateway-or-trafficmanager-4490bce29cb)
- [gitconnected.com: Blue-Green with Canary Deployment — A Novel approach](https://levelup.gitconnected.com/blue-green-with-canary-deployment-a-novel-approach-2cee77ff564d)
- [semaphoreci.com: Continuous Blue-Green Deployments With Kubernetes 🌟](https://semaphoreci.com/blog/continuous-blue-green-deployments-with-kubernetes)
- [cd.foundation: Intro to Deployment Strategies: Blue-Green, Canary, and More 🌟](https://cd.foundation/blog/2021/03/24/intro-to-deployment-strategies-blue-green-canary-and-more)
- [opsmx.com: What is Blue Green Deployment ?](https://www.opsmx.com/blog/blue-green-deployment/)
- [devopslearners.com: Blue-Green vs Canary Deployment](https://devopslearners.com/blue-green-vs-canary-deployment-76436d7f6bc1)
- [youtube: Kubernetes Deployment Strategies | DevOps FAQ | DevOps DevOps Interview Q&A ](https://www.youtube.com/watch?v=aU-EtdEOdlM)

<center>
[![deployment strategies](images/K8s_deployment_strategies.png)](https://blog.container-solutions.com/deployment-strategies)
</center>

## Pipeline Patterns

- [harness.io: Pipeline Patterns for CI/CD Pipelines 🌟](https://harness.io/blog/devops/deployment-pipeline-patterns/) **Button Push Pattern, Test Automation Pattern, Full Approval Pattern.**

## CI/CD with Kubernetes

- [blog.sonatype.com: Achieving CI and CD With Kubernetes 🌟](https://blog.sonatype.com/achieving-ci/cd-with-kubernetes)
- [Devtron Labs: Devtron provides a 'seamless,’ 'implementation agnostic uniform interface' across Kubernetes Life Cycle integrated with most Opensource and commercial tools](https://devtron.ai/)
- [thenewstack.io: 7 features that make kubernetes ideal for CI/CD](https://thenewstack.io/7-features-that-make-kubernetes-ideal-for-ci-cd/)
- [thenewstack.io: CI/CD with kubernetes 🌟](https://thenewstack.io/ebooks/kubernetes/ci-cd-with-kubernetes/)
- [harness.io: Kubernetes CI/CD Best Practices](https://harness.io/blog/kubernetes-ci-cd-best-practices/) With all of the benefits that Kubernetes has, having good CI/CD practices is key. Kubernetes did not magically erase the discipline that your CI/CD journey has taken you on before Kubernetes. Leverage Kubernetes’s strengths to further your CI/CD journey.

## CI/CD with OpenShift

- [developers.redhat.com: The present and future of CI/CD with GitOps on Red Hat OpenShift 🌟](https://developers.redhat.com/blog/2020/09/03/the-present-and-future-of-ci-cd-with-gitops-on-red-hat-openshift/)

## CI/CD with AWS

- [mediatemple.net: Cloud-Native CI/CD Workflows in AWS: 3 Use Cases](https://mediatemple.net/blog/cloud-hosting/cicd-workflows-aws-3-use-cases/)
- [trek10.com: Enterprise CI/CD on AWS: a pragmatic approach](https://www.trek10.com/blog/pragmatic-enterprise-cicd) How can we work within the constraints of a large organization to develop CI/CD flows that help us deploy applications quickly, safely, and accountably on AWS?

## Reports on the Enterprise CI/CD Market

- [GigaOm's Radar for Enterprise CI/CD 🌟](https://jfrog.com/whitepaper/gigaom-radar-for-enterprise-ci-cd/) is a must-see report for any DevOps enthusiast. The goal of an end-to-end Continuous Integration/Continuous Delivery (CI/CD) pipeline is to deliver software-based innovation and business value at both speed and scale. CI/CD plays a very important role in the company's DevOps journey. Keeping several factors in mind, Gigaom has come up with it'sown research and presented who leads and who lags in the CI/CD market.

<center>
[![gigaom cicd radar](images/gigaom_cicd_radar.jpg)](https://jfrog.com/whitepaper/gigaom-radar-for-enterprise-ci-cd/)
</center>

## Tools

- [plutora.com: Artifacts management tools](https://www.plutora.com/ci-cd-tools/artifacts-management-tools)
- [cloudbees.com: Continuous Delivery Tools: The 5 You Absolutely Need to Know in 2021](https://www.cloudbees.com/blog/cicd-tools-to-know-2021)
- [dzone: DevOps: CI/CD Tools to Watch Out for in 2022](https://dzone.com/articles/devops-cicd-tools-to-watch-out-for-in-2022) CI/CD is an integral part of any successful DevOps team. This list includes the finest CI/CD tools currently available in the market.
- [betterprogramming.pub: When Should You Self-Host CI Tools? | William Anderson](https://betterprogramming.pub/when-should-you-self-host-ci-tools-330fc38d2a6) How to decide whether you should self-host, go with a SaaS option, or bundle your choice of CI tool through a vendor

## Awesome Lists

- [Awesome CI/CD 🌟](https://github.com/cicdops/awesome-ciandcd)

## Images

??? note "Click to expand!"

    <center>
    ![cicd cheatsheet](images/cicd-cheatsheet.jfif)

    ![blue green deployment strategy](images/blue-green-deployment.jfif)

    [![cicd a basic release process](images/cicd-a-basic-release-process.jpg)](https://dzone.com/articles/how-to-build-an-effective-cicd-pipeline)
    </center>

## Videos

<details>
  <summary>Click to expand!</summary>

<center>
<iframe width="560" height="315" src="https://www.youtube.com/embed/N8R3-eNVoEc" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/65BnTLcDAJI" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/8g4qLzkpjeE?si=xcfl3ugsMGZ8Kthg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</center>
</details>

## Tweets

<details>
  <summary>Click to expand!</summary>

<center>
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">CI/CD is a must-know in DevOps. <br><br>Here&#39;s a dead simple guide to understanding it:</p>&mdash; Nikki Siapno (@NikkiSiapno) <a href="https://twitter.com/NikkiSiapno/status/1619966395965493248?ref_src=twsrc%5Etfw">January 30, 2023</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</center>
</details>