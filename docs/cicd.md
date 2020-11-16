# CI/CD
- [Introduction](#introduction)
- [CI/CD Continuous Integration and Continuous Delivery](#cicd-continuous-integration-and-continuous-delivery)
- [Security in CI/CD](#security-in-cicd)
- [Deployment Strategies](#deployment-strategies)
- [CI/CD with Kubernetes](#cicd-with-kubernetes)
- [CI/CD with OpenShift](#cicd-with-openshift)
- [CI/CD with AWS](#cicd-with-aws)
- [Reports on the Enterprise CI/CD Market](#reports-on-the-enterprise-cicd-market)
- [Awesome Lists](#awesome-lists)

## Introduction
* [opensource.com: What is CI/CD?](https://opensource.com/article/18/8/what-cicd)
* [Wikipedia.org: DevOps](https://en.wikipedia.org/wiki/DevOps)
* [Wikipedia.org: Continuous Integration](https://en.wikipedia.org/wiki/Continuous_integration)
* [Wikipedia.org: Continuous Delivery](https://en.wikipedia.org/wiki/Continuous_delivery)

<center>
[![CD Artifact Management](images/cd-artifact-management.jpg)](https://www.thoughtworks.com/insights/continuous-delivery)
</center>

## CI/CD Continuous Integration and Continuous Delivery
* [DZone: Continuous Integration: Servers and Tools](https://dzone.com/refcardz/continuous-integration-servers) Learning to Utilize DevOps with Servers and Tools
* [sdtimes.com: CI/CD pipelines are expanding 🌟](https://sdtimes.com/devops/ci-cd-pipelines-are-expanding/) The “basic” CI/CD pipeline includes five processes, which are: merge, build, test, package and deploy. All of these are individually defined so readers have a common reference point. The basic pipeline includes sub-pipelines associated with each step, such as moving artifacts from a build into a repository.
* [devopsonline.co.uk: ChatOps, DevOps, ScrumOps and 5 Other Ops religions](https://www.devopsonline.co.uk/chatops-devops-scrumops-and-5-other-ops-religions/)
* [opensource.com: A beginner's guide to building DevOps pipelines with open source tools](https://opensource.com/article/19/4/devops-pipeline) If you're new to DevOps, check out this five-step process for building your first pipeline.
* [acloud.guru: How youtr org predicts your CI/CD pipeline](https://info.acloud.guru/resources/brazeal-how-your-org-predicts-your-ci/cd-pipeline)
* [dev.to: CI/CD Continuous Integration & Delivery Explained 🌟🌟](https://dev.to/semaphore/ci-cd-continuous-integration-delivery-explained-75l)
* [mindtheproduct.com: The Product Managers’ Guide to Continuous Delivery and DevOps 🌟🌟](https://www.mindtheproduct.com/what-the-hell-are-ci-cd-and-devops-a-cheatsheet-for-the-rest-of-us/)
* [tech.buzzfeed.com: Continuous Deployments at BuzzFeed](https://tech.buzzfeed.com/continuous-deployments-at-buzzfeed-d171f76c1ac4)
* [Dzone refcard: Continuous Delivery - Patterns and Anti-Patterns in the Software Lifecycle 🌟](https://dzone.com/refcardz/continuous-delivery-patterns)
* [infoworld.com: What is CI/CD? Continuous integration and continuous delivery explained](https://www.infoworld.com/article/3271126/what-is-cicd-continuous-integration-and-continuous-delivery-explained.html) The CI/CD pipeline is one of the best practices for devops teams to implement, for delivering code changes more frequently and reliably
* [devops.com: How to Implement an Effective CI/CD Pipeline](https://devops.com/how-to-implement-an-effective-ci-cd-pipeline/)
* [ammeon.com: 5 Tips For Building A CI/CD Pipeline](https://www.ammeon.com/5-tips-for-building-ci-cd-pipeline/)
* [medium: What is CI/CD Pipeline in DevOps? 🌟🌟](https://medium.com/faun/what-is-ci-cd-pipeline-in-devops-6fba17a76e73) Understanding the Importance of CI/CD Pipeline.
* [aws.amazon.com: Automating safe, hands-off deployments 🌟🌟](https://aws.amazon.com/es/builders-library/automating-safe-hands-off-deployments/)
* [techuz.com: What is CI/CD? An Introduction to Continuous Integration, Continuous Deployment and CI/CD Pipeline](https://www.techuz.com/blog/what-is-ci-cd-an-introduction-to-continuous-integration-continuous-deployment-and-ci-cd-pipeline/)
* [kodekloud.com: What is CI/CD Pipeline in DevOps](https://kodekloud.com/blog/208192/what-is-ci-cd-pipeline-in-devops) CI/CD plays an important role in your DevOps implementation path.
Here are some important things to consider while building a CI/CD pipeline: 
    * Peer code review
    * Build in a containerized environment
    * Shorten the feedback loop
    * Do CI first
    * Compare efficiency
    * Insert security checkpoints in the pipeline
    * Implement an easy way to rollback
    * Proactively monitor your CD pipeline

* [medium: How to build an efficient CI/CD pipeline 🌟🌟](https://medium.com/@sanjayaben/how-to-build-an-efficient-ci-cd-pipeline-b5738ad567c8)
* [medium: Continuous Kubernetes blue-green deployments on Azure using Nginx, AppGateway or TrafficManager — part 2](https://medium.com/@denniszielke/continuous-kubernetes-blue-green-deployments-on-azure-using-nginx-appgateway-or-trafficmanager-4490bce29cb)
* [Asking for Help Is a Best Practice When Building a CI/CD Pipeline](https://www.cloudbees.com/case-study/asking-help-best-practice-when-building-cicd-pipeline)
* [developers.redhat.com: The present and future of CI/CD with GitOps on Red Hat OpenShift](https://developers.redhat.com/blog/2020/09/03/the-present-and-future-of-ci-cd-with-gitops-on-red-hat-openshift/)
* [dewanahmed.com: When to go k8s-native - A tale of CI/CD servers](https://www.dewanahmed.com/post/tekton-k8snative-cicd-pt1/)
* [CI/CD Best Practices 🌟](https://blog.bitsrc.io/ci-cd-best-practices-bca0ef665677)
* [harness.io: What is a CI/CD Platform and why should I care? 🌟](https://harness.io/2020/10/what-is-cicd-platform-why-should-i-care/)
* [harness.io: 3 Ways to Use Automation in CI/CD Pipelines](https://thenewstack.io/3-ways-to-use-automation-in-ci-cd-pipelines/)
* [cloudbees.com: 7 Tips for Creating A Successful CI/CD Pipeline 🌟](https://www.cloudbees.com/blog/tips-creating-successful-cicd-pipeline)
* [gitconnected.com: Blue-Green with Canary Deployment — A Novel approach](https://levelup.gitconnected.com/blue-green-with-canary-deployment-a-novel-approach-2cee77ff564d)
* [dzone: CI/CD Pipeline: Demystifying The Complexities](https://dzone.com/articles/cicd-pipeline-demystifying-the-complexities) Get a high-level overview of CI/CD pipelines and the components that make up a DevOps process, and some of the challenges and benefits of a CI/CD pipeline.

## Security in CI/CD
* [CI Checks Are Not Enough: Combat Configuration Drift in Kubernetes Resources](https://thenewstack.io/ci-checks-are-not-enough-combat-configuration-drift-in-kubernetes-resources/)

## Deployment Strategies
- [blog.container-solutions.com: Deployment Strategies 🌟](https://blog.container-solutions.com/deployment-strategies) 
    - It really depends on the needs and budget. When releasing to development/staging environments, a recreate or ramped deployment is usually a good choice. When it comes to production, a ramped or blue/green deployment is usually a good fit, but proper testing of the new platform is necessary. 
    - Blue/green and shadow strategies have more impact on the budget as it requires double resource capacity. If the application lacks in tests or if there is little confidence about the impact/stability of the software, then a canary, a/b testing or shadow release can be used. If your business requires testing of a new feature amongst a specific pool of users that can be filtered depending on some parameters like geolocation, language, operating system or browser features, then you may want to use the a/b testing technique.
    - Last but not least, a shadow release is complex and requires extra work to mock egress traffic which is mandatory when calling external dependencies with mutable actions (email, bank, etc.). However, this technique can be useful when migrating to a new database technology and use shadow traffic to monitor system performance under load.

<center>
[![deployment strategies](images/K8s_deployment_strategies.png)](https://blog.container-solutions.com/deployment-strategies)
</center>

## CI/CD with Kubernetes
* [blog.sonatype.com: Achieving CI and CD With Kubernetes 🌟](https://blog.sonatype.com/achieving-ci/cd-with-kubernetes)
* [thenewstack.io: 7 features that make kubernetes ideal for CI/CD](https://thenewstack.io/7-features-that-make-kubernetes-ideal-for-ci-cd/)
* [thenewstack.io: CI/CD with kubernetes 🌟](https://thenewstack.io/ebooks/kubernetes/ci-cd-with-kubernetes/)

## CI/CD with OpenShift
* [developers.redhat.com: The present and future of CI/CD with GitOps on Red Hat OpenShift 🌟](https://developers.redhat.com/blog/2020/09/03/the-present-and-future-of-ci-cd-with-gitops-on-red-hat-openshift/)

## CI/CD with AWS
* [mediatemple.net: Cloud-Native CI/CD Workflows in AWS: 3 Use Cases](https://mediatemple.net/blog/cloud-hosting/cicd-workflows-aws-3-use-cases/)
* [trek10.com: Enterprise CI/CD on AWS: a pragmatic approach](https://www.trek10.com/blog/pragmatic-enterprise-cicd) How can we work within the constraints of a large organization to develop CI/CD flows that help us deploy applications quickly, safely, and accountably on AWS?

## Reports on the Enterprise CI/CD Market
* [GigaOm's Radar for Enterprise CI/CD 🌟](https://jfrog.com/whitepaper/gigaom-radar-for-enterprise-ci-cd/) is a must-see report for any DevOps enthusiast. The goal of an end-to-end Continuous Integration/Continuous Delivery (CI/CD) pipeline is to deliver software-based innovation and business value at both speed and scale. CI/CD plays a very important role in the company's DevOps journey. Keeping several factors in mind, Gigaom has come up with it'sown research and presented who leads and who lags in the CI/CD market.

[![gigaom cicd radar](images/gigaom_cicd_radar.jpg)](https://jfrog.com/whitepaper/gigaom-radar-for-enterprise-ci-cd/)

## Awesome Lists
* [Awesome CI/CD 🌟](https://github.com/cicdops/awesome-ciandcd)

<center>
<iframe src="https://www.youtube.com/embed/N8R3-eNVoEc" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
</center>
<center>
<iframe src="https://www.youtube.com/embed/65BnTLcDAJI" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
</center>




