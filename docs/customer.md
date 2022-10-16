# Customer Success Stories. Cloud Native Projects

1. [BMW IT-Zentrum (Munich)](#bmw-it-zentrum-munich)
    1. [BMW ConnectedDrive and OpenShift](#bmw-connecteddrive-and-openshift)
    2. [BMW InnovationLab](#bmw-innovationlab)
2. [Audi](#audi)
3. [Volkswagen](#volkswagen)
4. [Mercedes Benz](#mercedes-benz)
5. [IDRA Group](#idra-group)
6. [Carrefour Spain](#carrefour-spain)
7. [Decathlon](#decathlon)
8. [Deutsche Telekom](#deutsche-telekom)
9. [AstraZeneca](#astrazeneca)
10. [AI for Medical Imaging](#ai-for-medical-imaging)
11. [Videos](#videos)

## BMW IT-Zentrum (Munich)

- [BMW IT-Zentrum](https://www.facebook.com/pages/BMW-IT-Zentrum/122968844423716)
- CI/CD at BMW IT-Zentrum (2018):
    - Jenkins in OpenShift (CloudBees & OSS): Maven, Seed Job, Multibranch Pipelines, Merge BOTs, OpenShift Source-to-Image (S2I), Fabric8 Java Client Library for Kubernetes, JobDSL & Shared Libraries (groovy).
    - Requirements of each microservice (configurations) defined in a single json file.
    - Java Frameworks: Java EE (Jakarta EE) running on Payara.
    - HA-Proxy, SonarQube, Nexus3, JMeter, Selenium, etc.
    - Docker, Terraform, Packer, Ansible, YAML, Flyway, PostgreSQL.
    - Swagger, Postman, Visual Studio Code.
    - Atlassian: Confluence, Bitbucket, Jira, Crowd.
    - Hybrid Clouds: OpenStack on-premise clusters, OpenShift 3.10 on-premise clusters, AWS.
    - Dynatrace APM, Prometheus, Grafana.
    - Rocket Chat
    - BMC Remedy ITSM
    - DevOps with Scrum, GitOps, ITIL Incident Management Workflow, Remote Work.
    - International Deloitte team based in Munich and outside Germany: Germany, Poland, Albany, Bulgaria, Portugal, Spain.

### BMW ConnectedDrive and OpenShift

- [**BMW ConnectedDrive**:](https://www.bmw-connecteddrive.com/) BMW ConnectedDrive Platform helps drivers communicate with their cars. Initially, the platform was enabled for convenience type of features like locating the vehicle, sounding the horn, locking the car, remote car health check... As the adoption of electric cars grows, BMW decided to create an ultimate driving experience by adding new services addressing the unique challenges of electric vehicles, like locating the closest electric charging stations, monitoring the car battery... This addition of new services has been creating new challenges in terms of API security. 
- [Red Hat OpenShift Container Platform Takes Digital Innovation into the Fast Lane with Major European Automaker](https://www.redhat.com/es/about/press-releases/red-hat-openshift-container-platform-takes-digital-innovation-fast-lane-major-european-automaker)
- [BMW takes digital innovation into the fast lane with Red Hat Openshift Container Platform](https://www.linkedin.com/pulse/bmw-takes-digital-innovation-fast-lane-red-hat-openshift-mendus/)
- [Youtube: BMW enables the BMW Group to deliver the continuous service that today's consumers expect (video starts at 1:29:00)](https://www.youtube.com/watch?time_continue=5340&v=FUu4kMc0PL8): BMW Group started working with 4 Openshift clusters in 2016 to support ConnectedDrive, a solution that delivers IoT digital services since 20 years ago. It took them a full-time migration for 2 years with a big transformation of the culture of the company, migrating monolithic applications to microservices. This is a consequence of having 30% of growth of request rate, by selling 2.5 million of cars yearly, all of them connected. Traditional IT could not cope with this growth. In 2019 they have 19 Openshift Clusters worldwide, with 12000 containers, 300 microservices, and 1 Billion requests per week. Future plans are to move to OpenShift Dedicated in the Public Cloud since they need to be more scalable and resilient, while building an Artificial Intelligence platform with a Data Lake on the public cloud to offer the best possible experience to their customers.

### BMW InnovationLab

- [BMW InnovationLab](https://github.com/BMW-InnovationLab) This organization contains open source software for realtime computer vision published by the developers, partners and friends of the BMW InnovationLab.
- As we transform into a data-driven company, the BMW Group Technology Office conducted a virtual hackathon, together with the Google Cloud Handle 'Google Cloud' on machine learning.
- Google Cloud Handle’s machine learning capabilities were used to implement use cases — ranging from charging optimisation for our electric vehicles, to wheel classification along our assembly line.
- Artificial Intelligence is a key technology in our digital transformation, and we want to enable our colleagues across all disciplines to work with the latest technologies. We strive to offer our worldwide network of software developers the opportunity to view, change, and develop their own algorithms. These projects illustrate the range of solutions that AI can provide, from automatic image recognition to natural language processing.
- We also make selected algorithms available in an open source platform. “We expect the further open source development to lead to a rapid and agile advancement of the software,” says Kai Demtroeder, Head of Artificial Intelligence and Data Platforms at BMW Group IT.

## Audi

- [redhat.com: Audi builds developer environment with Red Hat OpenShift](https://www.redhat.com/en/resources/audi-case-study) Audi decided to use Red Hat OpenShift, an enterprise Kubernetes platform, as the foundation of **Kubika-O**, its new self-service developer environment, to speed and scale delivery of innovative projects.

## Volkswagen

- [redhat.com: The Volkswagen Group builds automated testing environment](https://www.redhat.com/en/success-stories/the-volkswagen-group)

## Mercedes Benz

- [infoworld.com: Why Mercedes-Benz runs on 900 Kubernetes clusters](https://www.infoworld.com/article/3664052/why-mercedes-benz-runs-on-900-kubernetes-clusters.html) The German automaker runs a massive fleet of Kubernetes clusters to support a wide range of project teams around the world. ‘For us, managing Kubernetes is not that hard.’
- [github.com/mercedes-benz](https://github.com/mercedes-benz)
- [genbeta.com: El software de los coches de Mercedes contiene código abierto y en vez de distribuirlo en GitHub usan un CD](https://www.genbeta.com/desarrollo/software-coches-mercedes-contiene-codigo-abierto-vez-distribuirlo-github-usan-cd)
- [youtube: Keynote: 7 Years of Running Kubernetes for Mercedes-Benz - Jens Erat, Peter Mueller, Sabine Wolz](https://www.youtube.com/watch?v=UmbjwSK9b3I)

## IDRA Group

- [teslarati.com: IDRA finishes 9,000-ton Giga Press; Tesla expecting it any day now](https://www.teslarati.com/idra-9000-ton-giga-press/)

## Carrefour Spain

- [Efficient Java in the cloud with Quarkus. Carrefour Spain’s test: Quarkus vs. Spring Boot](https://horizons.carrefour.com/efficient-java-in-the-cloud-with-quarkus) "This move will help our applications to become scalable, real time, resilient and, all in all, provide a better experience to our customers"

## Decathlon

- [quarkus.io: VCStream: a new messaging platform for DECATHLON’s Value Chain, built on Quarkus](https://quarkus.io/blog/decathlon-user-story/) Another successful Quarkus user story! Decathlon picking QuarkusIO over springboot

## Deutsche Telekom

- [thenewstack.io: How Deutsche Telekom Manages Edge Infrastructure with GitOps](https://thenewstack.io/how-deutsche-telekom-manages-edge-infrastructure-with-gitops/)

## AstraZeneca

- [aws.amazon.com: AstraZeneca’s Drug Design Program Built using AWS wins Innovation Award](https://aws.amazon.com/blogs/industries/astrazenecas-drug-design-program-built-using-aws-wins-innovation-award/)

## AI for Medical Imaging

- [healthitanalytics.com: AI for Medical Imaging Boosts Cancer Screenings with Provider Aid](https://healthitanalytics.com/news/ai-for-medical-imaging-boosts-cancer-screenings-with-provider-aid)

## Videos

<details>
  <summary>Click to expand!</summary>

  <center>
  <iframe width="560" height="315" src="https://www.youtube.com/embed/FUu4kMc0PL8?start=5340" frameborder="0" allowfullscreen></iframe>
  <iframe width="560" height="315" src="https://www.youtube.com/embed/UWNHjFFykj8" frameborder="0" allowfullscreen></iframe>
  <iframe width="560" height="315" src="https://www.youtube.com/embed/iMVqsirda_8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
  <iframe width="560" height="315" src="https://www.youtube.com/embed/shDoeks_crI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
  <iframe width="560" height="315" src="https://www.youtube.com/embed/iZL6DSl_xSk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
  <iframe width="560" height="315" src="https://www.youtube.com/embed/LUx9FJSeAl4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
  <iframe width="560" height="315" src="https://www.youtube.com/embed/oKnZvNF3FB4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
  <iframe width="560" height="315" src="https://www.youtube.com/embed/98kIAzye8gc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
  <iframe width="560" height="315" src="https://www.youtube.com/embed/UmbjwSK9b3I" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
  <iframe width="560" height="315" src="https://www.youtube.com/embed/aGQF5RvByNE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
  <iframe width="560" height="315" src="https://www.youtube.com/embed/T36Gr1OtdJk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
  <iframe width="560" height="315" src="https://www.youtube.com/embed/Qlguwy9JMSA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
  <iframe width="560" height="315" src="https://www.youtube.com/embed/7-4yOx1CnXE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
  <iframe width="560" height="315" src="https://www.youtube.com/embed/cdZZpaB2kDM?start=2024" frameborder="0" allowfullscreen></iframe>
  </center>

</details>