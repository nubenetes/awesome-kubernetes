# Docker

1. [Introduction and Tutorials](#introduction-and-tutorials)
2. [Docker Best Practices](#docker-best-practices)
3. [Docker Networking](#docker-networking)
4. [Docker Volumes](#docker-volumes)
5. [Debugging](#debugging)
6. [Docker CLI](#docker-cli)
7. [Docker Extensions](#docker-extensions)
8. [Docker Swarm](#docker-swarm)
9. [Awesome Lists](#awesome-lists)
10. [Docker VS Kubernetes](#docker-vs-kubernetes)
11. [Docker Patterns and Antipatterns](#docker-patterns-and-antipatterns)
12. [Docker Security](#docker-security)
13. [How To Build a Smaller Docker Image and write dockerfiles efficiently](#how-to-build-a-smaller-docker-image-and-write-dockerfiles-efficiently)
14. [Reducing Build Time](#reducing-build-time)
15. [Modify containers without rebuilding](#modify-containers-without-rebuilding)
16. [Docker Tools](#docker-tools)
17. [Docker and WSL2](#docker-and-wsl2)
18. [Docker and Docker Swarm Cheat sheets](#docker-and-docker-swarm-cheat-sheets)
19. [Docker Compose](#docker-compose)
20. [Moving Linux Services Into Containers](#moving-linux-services-into-containers)
21. [Windows Containers](#windows-containers)
22. [Portainer](#portainer)
23. [DockStation](#dockstation)
24. [Linux Container Base Images](#linux-container-base-images)
25. [Blogs](#blogs)
26. [Cloud Native Buildpacks](#cloud-native-buildpacks)
27. [Alternatives to Docker. Available alternatives to Docker for OCI compliant container image building](#alternatives-to-docker-available-alternatives-to-docker-for-oci-compliant-container-image-building)
28. [Videos and Podcasts](#videos-and-podcasts)
29. [Tweets](#tweets)

## Introduction and Tutorials

- [Wikipedia.org: Docker](https://en.wikipedia.org/wiki/Docker_(software))
- [Dzone refcard: Getting Started with Docker](https://dzone.com/refcardz/getting-started-with-docker-1)
- [Dzone refcard: Java Containerization 🌟](https://dzone.com/refcardz/java-containerization)
- [americanexpress.io: **Do Not Run Dockerized Applications as Root** 🌟](https://americanexpress.io/do-not-run-dockerized-applications-as-root/)
- [medium.com: Removing Docker Images, Containers, and Volumes with Ease](https://medium.com/@jon.froiland/removing-docker-images-containers-and-volumes-with-ease-fdf16bebccec)
- [medium.freecodecamp.com: A Beginner-Friendly Introduction to Containers, VMs and Docker](https://medium.freecodecamp.com/a-beginner-friendly-introduction-to-containers-vms-and-docker-79a9e3e119b)
- [Google Play: Learning Solution - Learn Docker 🌟](https://play.google.com/store/apps/details?id=com.LearningSolution.LearnDocker&hl=en)
- [Play with docker 🌟](https://labs.play-with-docker.com/) A simple, interactive and fun playground to learn Docker
- [medium: Strategies of docker images optimization](https://medium.com/sciforce/strategies-of-docker-images-optimization-2ca9cc5719b6)
- [Dzone: Docker explained, an introductory guide to docker](https://dzone.com/articles/docker-explained-an-introductory-guide-to-docker)
- [Dzone: everything you need to know about docker](https://dzone.com/articles/everything-you-need-to-know-about-docker)
- [Dzone: a start to finish guide to docker with java](https://dzone.com/articles/a-start-to-finish-guide-to-docker-with-java)
- [**GitHub build-push-action**](https://github.com/docker/build-push-action) Build+push official Docker GitHub action
- [itnext.io: Getting Started with Docker: Facts You Should Know 🌟](https://itnext.io/getting-started-with-docker-facts-you-should-know-d000e5815598)
- [jfrog.com: A Beginner’s Guide to Understanding and Building Docker Images 🌟](https://jfrog.com/knowledge-base/a-beginners-guide-to-understanding-and-building-docker-images/)
- [Broken by default: why you should avoid most Dockerfile example 🌟](https://pythonspeed.com/articles/dockerizing-python-is-hard/)
- [geekflare.com: docker tutorials](https://geekflare.com/docker-tutorials/)
- [medium: What is Docker, Why should you use it in simple words](https://medium.com/@shahinghasemy/what-is-docker-why-should-you-use-it-in-simple-words-cc5e6160f9db)
- [docker.com: Top Questions for Getting Started with Docker 🌟](https://www.docker.com/blog/top-questions-for-getting-started-with-docker/)
- [medium: How to Start Working With Docker Containers](https://medium.com/swlh/how-to-start-working-with-docker-containers-72b73ca60e0c)
- [dzone: Mitigating DevOps Repository Risks](https://dzone.com/articles/mitigating-devops-repository-risks) Docker is in the news for two reasons: Image retention limits and download throttling. Let's discuss both and see the better alternatives.
- [Top 18 Docker commands for Automation Tester/Devops/SDET/Test Lead? 🌟](https://automationreinvented.blogspot.com/2020/02/top-18-docker-commands-for-aytomation.html)
- [A Gentle Introduction to Using a Docker Container as a Dev Environment 🌟](https://css-tricks.com/a-gentle-introduction-to-using-a-docker-container-as-a-dev-environment/)
- [docs.docker.com: Deploying Docker containers on ECS](https://docs.docker.com/engine/context/ecs-integration/)
    - [AWS and Docker collaborate to simplify the developer experience](https://aws.amazon.com/blogs/containers/aws-docker-collaborate-simplify-developer-experience/)
    - [From Docker Straight to AWS](https://www.docker.com/blog/from-docker-straight-to-aws/)
- [A Gentle Introduction to Using a Docker Container as a Dev Environment](https://css-tricks.com/a-gentle-introduction-to-using-a-docker-container-as-a-dev-environment/)
- [martinheinz.dev: It's Time to Forget About Docker 🌟](https://martinheinz.dev/blog/35)
- [docker.com: Docker Hub Experimental CLI tool](https://www.docker.com/blog/docker-hub-experimental-cli-tool/)
- [docker.com: Year in Review: The Most Viewed Docker Blog Posts of 2020 Part 1 🌟](https://www.docker.com/blog/year-in-review-the-most-viewed-docker-blog-posts-of-2020-part-1/)
- [docker.com: Year in Review: The Most Viewed Docker Blog Posts of 2020 Part 2 🌟](https://www.docker.com/blog/year-in-review-the-most-viewed-docker-blog-posts-of-2020-part-2/)
- [adictosaltrabajo.com: Cómo crear y desplegar microservicios con Spring Boot, Spring Cloud Netflix y Docker](https://www.adictosaltrabajo.com/2020/12/22/como-crear-y-desplegar-microservicios-con-spring-boot-spring-cloud-netflix-y-docker/)
- [cloudsavvyit.com: How to Use Cron With Your Docker Containers](https://www.cloudsavvyit.com/9033/how-to-use-cron-with-your-docker-containers/)
- [infoq.com: Docker Hub and JFrog Partnership Removes Image Pull Limits for Artifactory Users](https://www.infoq.com/news/2021/01/docker-jfrog-partnership/)
- [technology.doximity.com: Buildpacks vs Dockerfiles 🌟](https://technology.doximity.com/articles/buildpacks-vs-dockerfiles) Exploring the tradeoffs of building container images at scale
- [docker.com: Containerized Python Development – Part 1](https://www.docker.com/blog/containerized-python-development-part-1/)
    - [docker.com: Containerized Python Development – Part 2](https://www.docker.com/blog/containerized-python-development-part-2/)
    - [docker.com: Containerized Python Development – Part 3](https://www.docker.com/blog/containerized-python-development-part-3/)
- [pythonspeed.com: The worst so-called “best practice” for Docker](https://pythonspeed.com/articles/security-updates-in-docker/)
- [developers.redhat.com: Making environment variables accessible in front-end containers](https://developers.redhat.com/blog/2021/03/04/making-environment-variables-accessible-in-front-end-containers/)
- [towardsdatascience.com: Have you heard about our lord and savior Docker?](https://towardsdatascience.com/docker-101-ee3d2b8ace11) Introduction to working with Docker and creating your own development environment
- [medium: Dockerizing a REST API in Python Less Than 9 MB and Based on scratch Image](https://medium.com/analytics-vidhya/dockerizing-a-rest-api-in-python-less-than-9-mb-and-based-on-scratch-image-ef0ee3ad3f0a)
- [datamechanics.co: Optimized Apache Spark Docker Images](https://www.datamechanics.co/blog-post/optimized-spark-docker-images-now-available)
- [theskillpedia.com: Managing docker images - openshift tutorial](https://www.theskillpedia.com/managing-docker-images-openshift-tutorial/)
- [iximiuz.com: Container Networking Is Simple!](https://iximiuz.com/en/posts/container-networking-is-simple/)
- [r-bloggers.com: Dockerizing Shiny Applications](https://www.r-bloggers.com/2021/05/dockerizing-shiny-applications/)
- [pythonspeed.com: Docker can slow down your code and distort your benchmarks](https://pythonspeed.com/articles/docker-performance-overhead/)
- [turbofuture.com: A Beginners Guide to Containers and Docker](https://turbofuture.com/computers/introductiontodocker)
- [releasehub.com: Cutting Build Time In Half with Docker’s Buildx Kubernetes Driver](https://releasehub.com/blog/cutting-build-time-in-half-docker-buildx-kubernetes)
- [medium.com/nttlabs: Kubernetes driver for Docker BuildX](https://medium.com/nttlabs/buildx-kubernetes-ad0fe59b0c64) In this article, you will learn how Docker BuildX supports building images using BuildKit pods on a Kubernetes cluster. Docker BuildX, the extended version of docker build CLI, now supports distributed image building using Kubernetes!
- [linuxadictos.com: Docker presenta nuevas capacidades para desarrolladores](https://www.linuxadictos.com/docker-presenta-nuevas-capacidades-para-desarrolladores.html)
- [grafana.com: Docker Integration for Grafana Cloud](https://grafana.com/docs/grafana-cloud/reference/integrations/integration-docker/) Docker is an open platform for developing, shipping, and running applications. Docker enables you to separate your applications from your infrastructure so you can deliver software quickly.
- [dev.to: Docker CMD vs ENTRYPOINT: explaining the difference](https://dev.to/hood/docker-cmd-vs-entrypoint-explaining-the-difference-55g7)
- [blog.gougousis.net: File Permissions: the painful side of Docker 🌟](https://blog.gougousis.net/file-permissions-the-painful-side-of-docker/)
    - ["Excellent description of user ids and access rights in Docker; it’s a non trivial issue and there’s no silver bullet other than to avoid running your containers with a privileged user. As a bonus, I personally like openshift approach (random UIDs belonging to the super user GID)"](https://twitter.com/agarcia)
- [katacoda.com: Learn Docker & Containers using Interactive Browser-Based Scenarios 🌟](https://www.katacoda.com/courses/docker)
- [medium: Push Docker Image To Docker Hub](https://medium.com/codex/push-docker-image-to-docker-hub-acc978c76ad) Create Docker hub account and push Docker image.
- [blog.thundra.io: Why Should You Run All Your Tests in Docker? 🌟](https://blog.thundra.io/why-should-you-run-all-your-tests-in-docker)
- [returngis.net: Crea hosts de Docker con Docker Machine en Microsoft Azure](https://www.returngis.net/2021/08/crea-hosts-de-docker-con-docker-machine-en-microsoft-azure/)
- [dev.to: Docker 101!](https://dev.to/kubona_my/docker-101-124e)
- [pawelurbanek.com: asdf and Docker for Managing Local Development Dependencies](https://pawelurbanek.com/asdf-docker-development)
- [tecmint.com: How to Install Docker on Rocky Linux and AlmaLinux](https://www.tecmint.com/install-docker-in-rocky-linux-and-almalinux/)
- [blog.adoptium.net: Using Jlink in Dockerfiles instead of a JRE](https://blog.adoptium.net/2021/08/using-jlink-in-dockerfiles/)
- [cloudsavvyit.com: How to SSH into a Docker container](https://www.cloudsavvyit.com/13937/how-to-ssh-into-a-docker-container/)
- [cloudsavvyit.com: How to use docker cp to copy files between host and containers](https://www.cloudsavvyit.com/13987/how-to-use-docker-cp-to-copy-files-between-host-and-containers/)
- [baeldung.com: Deploying a Java War in a Docker Container](https://www.baeldung.com/docker-deploy-java-war)
- [returngis.net: Explorar gráficamente el contenido de un volumen de Docker](https://www.returngis.net/2021/08/explorar-graficamente-el-contenido-de-un-volumen-de-docker/)
- [opensource.com: What is a container image?](https://opensource.com/article/21/8/container-image) A container image contains a packaged application, along with its dependencies, and information on what processes it runs when launched.
- [zdnet.com: Docker changes its subscription plans, usage rules, and product line](https://www.zdnet.com/article/docker-changes-its-subscription-plans-usage-rules-and-product-line/)
- [servethehome.com: Docker Abruptly Starts Charging Many Users for Docker Desktop](https://www.servethehome.com/docker-abruptly-starts-charging-many-users-for-docker-desktop/)
- [matt-rickard.com: An Overview of Docker Desktop Alternatives](https://matt-rickard.com/docker-desktop-alternatives/)
- [blog.aquasec.com: How Do Containers Contain? Container Isolation Techniques](https://blog.aquasec.com/container-isolation-techniques)
- [infoworld.com: How Docker broke in half](https://www.infoworld.com/article/3632142/how-docker-broke-in-half.html) The game changing container company is a shell of its former self. What happened to one of the hottest enterprise technology businesses of the cloud era?
- [cloudsavvyit.com: How to Pass Environment Variables to Docker Containers](https://www.cloudsavvyit.com/14081/how-to-pass-environment-variables-to-docker-containers/)
- [dev.to: One does not "just containerize" an app](https://dev.to/tylerlwsmith/one-does-not-just-containerize-an-app-5eae)
    - The Docker ecosystem is filled with leaky abstractions. The utopian vision of Docker containers is a world where a developer can grab a base container for a language, copy in their code with a minimal Dockerfile, and be ready to develop and deploy instantly.
    - Unfortunately, this landscape is filled with per-language gotchas that make this world a far cry from reality. Here are some of the wonky things I've run into when working with containers.
- [cloudsavvyit.com: How To Clean Up and Delete Docker Images](https://www.cloudsavvyit.com/14191/how-to-clean-up-and-delete-docker-images/)
- [==itnext.io: Software development in containers — a cookbook== 🌟🌟🌟](https://itnext.io/software-development-in-containers-a-cookbook-2ba14d07e535) A guide to developing containerized software
- [dev.to: How to create a production Docker image](https://dev.to/abdorah/how-to-create-production-docker-image-ready-for-deployment-4bbe)
- [dev.to: How to run docker on Windows without Docker Desktop](https://dev.to/_nicolas_louis_/how-to-run-docker-on-windows-without-docker-desktop-hik)
- [dev.to: Beginner's guide to Docker and Docker CLI commands](https://dev.to/paru429/beginner-s-guide-to-docker-and-docker-cli-commands-1p75)
- [freecodecamp.org: Learn How to Deploy 12 Apps to AWS, Azure, & Google Cloud](https://www.freecodecamp.org/news/learn-how-to-deploy-12-apps-to-aws-azure-google-cloud/)
- [cloudsavvyit.com: How to Assign a Static IP to a Docker Container](https://www.cloudsavvyit.com/14508/how-to-assign-a-static-ip-to-a-docker-container/)
- [cloudsavvyit.com: How to Inspect a Docker Image’s Content Without Starting a Container](https://www.cloudsavvyit.com/14663/how-to-inspect-a-docker-images-content-without-starting-a-container/)
- [freecodecamp.org: Why You Should Start Using Docker Right Now](https://www.freecodecamp.org/news/why-you-should-start-using-docker-now/)
- [infoworld.com: Docker really did change the world](https://www.infoworld.com/article/3639596/docker-really-did-change-the-world.html) Developers quickly understood the value of containers for building cloud-native applications, and that the Docker command-line tool was better than all of the bells and whistles they got with PaaS.
- [cloudsavvyit.com: How (and Why) to Run Docker Inside Docker](https://www.cloudsavvyit.com/14890/how-and-why-to-run-docker-inside-docker/)
- [cloudsavvyit.com: What’s the Difference Between Exposing and Publishing a Docker Port?](https://www.cloudsavvyit.com/14880/whats-the-difference-between-exposing-and-publishing-a-docker-port/)
- [==clavinjune.dev: Working With Remote Docker Using Docker Context==](https://clavinjune.dev/en/blogs/working-with-remote-docker-using-docker-context/) This is a cheatsheet for working with docker context to connect remote docker locally. Might help you to work with remote docker without manually SSH to the remote server.
- [cloudsavvyit.com: How to Add a Volume to an Existing Docker Container](https://www.cloudsavvyit.com/14973/how-to-add-a-volume-to-an-existing-docker-container/)
- [cloudsavvyit.com: How to Manage Docker Engine Plugins](https://www.cloudsavvyit.com/15066/how-to-manage-docker-engine-plugins)
- [==iximiuz.com: Learning Containers From The Bottom Up== | Ivan Velichko 🌟🌟🌟](https://iximiuz.com/en/posts/container-learning-path/) Efficient Learning Path to Grasp Containers Fundamentals
- [thenewstack.io: The Time to Decide on Docker Desktop Has Arrived](https://thenewstack.io/the-time-to-decide-on-docker-desktop-has-arrived/)
- [codeproject.com: How to Create an Image in Docker using Python](https://www.codeproject.com/Tips/5323808/How-To-Create-An-Image-In-Docker-Using-Python)
- [thenewstack.io: How to Share Data Between Docker Containers](https://thenewstack.io/how-to-share-data-between-docker-containers/)
- [iximiuz.com: Containers 101: attach vs. exec - what's the difference?](https://iximiuz.com/en/posts/containers-101-attach-vs-exec/)
- [acloudguru.com: Docker COPY vs ADD: What’s the difference?](https://acloudguru.com/blog/engineering/docker-copy-vs-add-whats-the-difference)
- [thenewstack.io: How to Run Docker in Rootless Mode](https://thenewstack.io/how-to-run-docker-in-rootless-mode/)
- [mjovanc.com: Get started with Docker and Docker Compose](https://mjovanc.com/get-started-with-docker-and-docker-compose-cddcb5a3f3b9)
- [dev.to: Docker: Explained to a 5 year old. 👶🏻](https://dev.to/dhravya/docker-explained-to-a-5-year-old-2cbg)
- [nishnit007.medium.com: A Journey from Dockerfile to Application Deployment on Kubernetes For Beginners](https://nishnit007.medium.com/a-journey-from-dockerfile-to-application-deployment-on-kubernetes-for-beginners-fea1eb0f3581)
- [freecodecamp.org: Docker Cache – How to Do a Clean Image Rebuild and Clear Docker's Cache](https://www.freecodecamp.org/news/docker-cache-tutorial/)
- [==dev.to: Docker 101: Introduction to Docker==](https://dev.to/signoz/docker-101-introduction-to-docker-1kbm)
- [blog.devgenius.io: K8s — Advanced Container Knowledge](https://blog.devgenius.io/k8s-advanced-container-knowledge-fcc45a2f6db8)
- [medium.com/@joelbelton: Optimising Docker Performance — The Key 4 Techniques You Need](https://medium.com/@joelbelton/optimising-docker-performance-the-key-4-techniques-you-need-6440cfebb650)
- [kubesimplify.com: The secret gems behind building container images, Enter: BuildKit & Docker Buildx](https://kubesimplify.com/the-secret-gems-behind-building-container-images-enter-buildkit-and-docker-buildx)
- [medium.com/geekculture: Docker — Limit Container CPU Usage 🌟](https://medium.com/geekculture/docker-limit-container-cpu-usage-11eb8ee0de5a)
- [devtron.ai: Understand CMD and ENTRYPOINT Differences in Docker](https://devtron.ai/blog/cmd-and-entrypoint-differences/)
- [fatehmuhammad.medium.com: Introduction to Docker | part 1](https://fatehmuhammad.medium.com/introduction-to-docker-part-1-3cff7559e372)
- [cloudnativeislamabad.hashnode.dev: Introduction to Docker | part 1 🌟](https://cloudnativeislamabad.hashnode.dev/introduction-to-docker-part-1)
- [==docker-curriculum.com: A Docker Tutorial for Beginners 🌟==](https://docker-curriculum.com/)
- [hostinger.in: What Is Docker and How Does It Work? – Docker Explained](https://www.hostinger.in/tutorials/what-is-docker)
- [blog.devgenius.io: Container — Namespace Introduction](https://blog.devgenius.io/container-namespace-introduction-6a1e26f8707a) Introduction to common container namespaces
- [viblo.asia: How to prevent out-of-disk space when using Docker?](https://viblo.asia/p/how-to-prevent-out-of-disk-space-when-using-docker-english-WR5JRDBrVGv)
- [iximiuz.com: What Actually Happens When You Publish a Container Port 🌟](https://iximiuz.com/en/posts/docker-publish-container-ports/) "Port publishing" seems to be a term coined by Docker. But "port forwarding" aka "port mapping - as a form of socket redirection - was a well-known trick well before the invention of containers. How are the two different?
- [iximiuz.com: How To Publish a Port of a Running Container 🌟](https://iximiuz.com/en/posts/docker-publish-port-of-running-container/)
- [medium.com/@BeNitinAgarwal: Lifecycle of Docker Container](https://medium.com/@BeNitinAgarwal/lifecycle-of-docker-container-d2da9f85959)
- [docker.com: Docker Compose: What’s New, What’s Changing, What’s Next](https://www.docker.com/blog/new-docker-compose-v2-and-v1-deprecation/)
- [medium.com/@i180826: Using Docker to build React App](https://medium.com/@i180826/using-docker-to-build-react-app-49862615e6f8)
- [dev.to: Simplify Your Dockerfile wiyth Rust programming language| Kamesh Sampath](https://dev.to/kameshsampath/simplify-your-dockerfile-1j5k)
- [itprotoday.com: Is Docker Still Worth Learning for IT Operations Teams? Probably Not](https://www.itprotoday.com/it-operations/docker-still-worth-learning-it-operations-teams-probably-not) While Docker isn't dead, Docker tooling may be. Here's why learning Docker tools isn't as important as it once was, especially for ITOps teams.
- [kennybrast.medium.com: How I Used Docker to Create a Python Dev Environment](https://kennybrast.medium.com/how-i-used-docker-to-create-a-python-dev-environment-48a5d31ae277)
- [==youtube: Docker 101 (Workshop) how an application can be run using Docker containers. First, you'll learn how to take an application all the way from source code to a running container. Docker-compose, networking, multi-stage and more== 🌟](https://www.youtube.com/watch?v=0mxhS7H6bxM)
- [codementor.io: Docker: What's Under the Hood?](https://www.codementor.io/blog/docker-technology-5x1kilcbow) How does Docker work? Get a better understanding of the skeleton of Docker, Virtualization, and future development
- [dev.to/javinpaul: My Favorite Free Courses to Learn Docker and Containers in 2023](https://dev.to/javinpaul/my-favorite-free-courses-to-learn-docker-and-containers-in-2023-1ldo)
- [tonylixu.medium.com: Docker RUN vs CMD vs ENTRYPOINT](https://tonylixu.medium.com/docker-run-vs-cmd-vs-entrypoint-57f248b95889) Differences between three Docker build instructions
- [==dev.to: Building a Robust CI/CD Pipeline with Docker: A Comprehensive Guide==](https://dev.to/itsahsanmangal/building-a-robust-cicd-pipeline-with-docker-a-comprehensive-guide-4k8b) By adopting CI/CD, you can ensure your code is consistently tested & validated, reducing the likelihood of introducing errors and increasing overall software quality.
- [==dev.to: Docker : From Zero to Hero 🛸 ( part 1) | Prasenjeet Kumar==](https://dev.to/prasenjeetsymon/docker-from-zero-to-hero-part-1-3a45) Docker is a tool that allows you to package, distribute and run apps as containers. It provides an efficient & consistent way to deploy apps across different environments, from dev to prod.
- [dzone: Components of Container Management](https://dzone.com/articles/components-of-container-management) Strategizing beyond build and run: Explore the benefits of containers that are widely evident around the cloud-native world and its modernization journey.
- [devopscube.com: How to Build Docker Image : Comprehensive Beginners Guide](https://devopscube.com/build-docker-image/)
- [pointbase.hashnode.dev: Understand Docker layers by example : RUN instructions Impact](https://pointbase.hashnode.dev/understand-docker-layers-by-example-run-instructions-impact)

## Docker Best Practices

- [blog.docker.com: Intro Guide to Dockerfile Best Practices 🌟](https://blog.docker.com/2019/07/intro-guide-to-dockerfile-best-practices/)
- [docker.com: Intro Guide to Dockerfile Best Practices](https://www.docker.com/blog/intro-guide-to-dockerfile-best-practices/)
- [docker.com: Speed Up Your Development Flow With These Dockerfile Best Practices](https://www.docker.com/blog/speed-up-your-development-flow-with-these-dockerfile-best-practices/)
- [sysdig.com: Top 20 Dockerfile best practices 🌟](https://sysdig.com/blog/dockerfile-best-practices/)
- [testdriven.io: Docker Best Practices for Python Developers](https://testdriven.io/blog/docker-best-practices/)
- [==dev.to: Top 8 Docker Best Practices for using Docker in Production== 🌟](https://dev.to/techworld_with_nana/top-8-docker-best-practices-for-using-docker-in-production-1m39)
- [dev.to: Top 5 Docker Best Practices](https://dev.to/karanpratapsingh/top-5-docker-best-practices-57oh)
- [==stevelasker.blog: Docker Tagging: Best practices for tagging and versioning docker images==](https://stevelasker.blog/2018/03/01/docker-tagging-best-practices-for-tagging-and-versioning-docker-images/)
- [faun.pub: Dockerfile Best Practices for Developers | Pavan Belagatti](https://faun.pub/dockerfile-best-practices-for-developers-87a2c19b4abe)
- [azeynalli1990.medium.com: 15 Best Practices when working with Docker](https://azeynalli1990.medium.com/15-best-practices-when-working-with-docker-720d2d8de202)

## Docker Networking

- [hwchiu.medium.com: Docker Networking Model — Introduction](https://hwchiu.medium.com/docker-networking-model-introduction-194a2a2c9b68) This article provides an overview of several basic network models for Docker Containers:
    - None
    - Host
    - Bridge
    - Container:$ID

## Docker Volumes

- [medium: Understanding Docker Volumes, Mounts and Layers and How to Manage Data in Containers](https://medium.com/nycdev/understanding-docker-volumes-mounts-and-layers-9fa17befa493)
- [spacelift.io: Docker Volumes – Guide with Examples](https://spacelift.io/blog/docker-volumes) Volumes are a mechanism for storing data outside containers. All volumes are managed by Docker & stored in dedicated directory on your host, usually /var/lib/docker/volumes for Linux systems
- [docs.netapp.com: Work with docker volumes - Astra Trident 🌟](https://docs.netapp.com/us-en/trident/trident-docker/volumes-docker.html)

## Debugging

- [betterprogramming.pub: 5 Simple Tips For Debugging Docker Containers 🌟](https://betterprogramming.pub/5-simple-tips-for-debugging-docker-containers-271cb3dee77a) Smoke out annoying container problems with minimal insanity
- [iximiuz.com: Docker: How To Debug Distroless And Slim Containers 🌟](https://iximiuz.com/en/posts/docker-debug-slim-containers/) A handy way to troubleshoot containers lacking a shell and/or debugging tools (e.g, scratch, slim, or distroless)

## Docker CLI

- [docs.docker.com: docker buildx imagetools](https://docs.docker.com/engine/reference/commandline/buildx_imagetools/) Commands to work on images in registry
- Who is still copying images between registries with:
    - docker cli:
        - docker pull <src>
        - docker tag <src> <dst>
        - docker push <dst>
    - Use:
        - crane cp <src> <dst>
    - Or even:
        - cosign cp <src> <dst>

    - It's faster, and supports multi-arch (and cosign copies signatures/sboms/attestations)

## Docker Extensions

- [==dev.to: 9 Docker Extensions Every Developer Must Try==](https://dev.to/docker/9-docker-extensions-every-developer-must-try-1no2)
- [github.com/Saniewski/mongo-express-docker-extension](https://github.com/Saniewski/mongo-express-docker-extension) Docker Extension for creating and running an embedded instance of Mongo Express connected to any accessible MongoDB server.

## Docker Swarm

- [Docker Swarm](kubernetes-alternatives.md#docker-swarm)

## Awesome Lists

- [Awesome Docker 🌟](https://github.com/veggiemonk/awesome-docker)
- [Awesome Compose 🌟](https://github.com/docker/awesome-compose)
- [github.com/pabpereza/curated-dockerfiles-examples: Curated Dockerfiles examples](https://github.com/pabpereza/curated-dockerfiles-examples) Public repository dedicated to guide the use of multi-stage and distroless dockerfile examples in docker, or other containers technologies, with the objetive to create secured templates for new developments

## Docker VS Kubernetes

- [blog.testproject.io: A Comparison of Kubernetes and Docker](https://blog.testproject.io/2021/06/21/a-comparison-of-kubernetes-and-docker/)
- [==containerjournal.com: What’s the Difference Between Docker and Kubernetes?==](https://containerjournal.com/features/whats-the-difference-between-docker-and-kubernetes/)
- [peoplactive.com: Kubernetes Vs Docker – Which to Adopt?](https://peoplactive.com/kubernetes-vs-docker-swarm-difference)

## Docker Patterns and Antipatterns

- [codefresh.io: Docker anti-patterns 🌟](https://codefresh.io/containers/docker-anti-patterns/)
- [medium: Docker anti-patterns | Codefresh](https://medium.com/containers-101/docker-anti-patterns-ad2a1fcd5ce1)
    - Creating Docker files that are not transparent.
    - Creating Dockerfiles that have side effects.
    - Confusing images used for deployment with those used for development.
    - Building different images per environment.

## Docker Security

- [thehackernews.com: Docker Images Containing Cryptojacking Malware Distributed via Docker Hub](https://thehackernews.com/2020/06/cryptocurrency-docker-image.html)
- [acloudguru.com: 10 Docker Security Best Practices to Cut Container Chaos](https://acloudguru.com/blog/engineering/10-docker-security-best-practices-to-cut-container-chaos)
- [brianchristner.io: How to use Docker Security Scan Locally](https://brianchristner.io/how-to-use-docker-scan/) Docker included a new command called `docker scan` that scans local images against the Snyk security engine, providing you with security visibility into your local Dockerfiles and images.
- [snyk.io: 10 Docker Security Best Practices 🌟](https://snyk.io/blog/10-docker-image-security-best-practices/)
- [cheatsheetseries.owasp.org: Docker Security Cheat Sheet 🌟🌟](https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html)
- [==augmentedmind.de: Docker optimization guide: the 12 best tips to optimize Docker image security==](https://www.augmentedmind.de/2022/02/20/optimize-docker-image-security/)
- [infoq.com: Is Docker Secure Enough?](https://www.infoq.com/articles/securing-docker/)
- [clickittech.com: The Ultimate Docker Security Best Practices for Your Node.js Application](https://www.clickittech.com/devops/docker-security-best-practices/) Top 12 Docker Security Best Practices
- [infosecwriteups.com: Attacking and securing Docker containers](https://infosecwriteups.com/attacking-and-securing-docker-containers-cc8c80f05b5b)
- [securitylabs.datadoghq.com: Container security fundamentals: Exploring containers as processes](https://securitylabs.datadoghq.com/articles/container-security-fundamentals-part-1/)

## How To Build a Smaller Docker Image and write dockerfiles efficiently

- [developers.redhat.com: Keep it small: a closer look at Docker image sizing](https://developers.redhat.com/blog/2016/03/09/more-about-docker-images-size/)
- [medium: How to build a smaller Docker image](https://medium.com/@gdiener/how-to-build-a-smaller-docker-image-76779e18d48a) When you’re building a Docker image it’s important to keep the size under control. Having small images means ensuring faster deployment and transfers.
- [itsopensource.com: How to Reduce Node Docker Image Size by 10X](https://itsopensource.com/how-to-reduce-node-docker-image-size-by-ten-times/)
- [blog.bitsrc.io: Best Practices for Writing a Dockerfile](https://blog.bitsrc.io/best-practices-for-writing-a-dockerfile-68893706c3) Optimize your Docker Image by following these best practices from day one.
- [sequoia.makes.software: Reducing Docker Image Size (Particularly for Kubernetes Environments) 🌟](https://sequoia.makes.software/reducing-docker-image-size-particularly-for-kubernetes-environments/)
- [itnext.io: Building Docker Images The Proper Way 🌟](https://itnext.io/building-docker-images-the-proper-way-3c9807524582) Let’s optimize Docker builds to create much smaller and more secure Docker images in a fraction of the usual build time…
- [returngis.net: Reduce el tamaño de tus imágenes con Dockerfiles multi-stage](https://www.returngis.net/2021/08/reduce-el-tamano-de-tus-imagenes-con-dockerfiles-multi-stage/)
- [==slim.ai==](https://www.slim.ai/) Build secure containers, faster. Secure your software supply chain.
    - [slim.ai: Automatically reduce Docker container size using DockerSlim](https://www.slim.ai/blog/automatically-reduce-docker-container-size-using-dockerslim.html)
    - [youtube: The need for Slim Docker Container Images with @DockerSlim & Slim.AI](https://www.youtube.com/watch?v=1o14tIEhZL0)
    - [==slim.ai: Slim Docker Extension== 🌟](https://www.slim.ai/docs/docker-desktop-extension.html)
- [learnk8s.io: 3 simple tricks for smaller Docker images 🌟](https://learnk8s.io/blog/smaller-docker-images) When it comes to building Docker containers, you should always strive for smaller images. **Images that share layers and are smaller in size are quicker to transfer and deploy.**
- [contains.dev: Optimizing Docker image size and why it matters](https://contains.dev/blog/optimizing-docker-image-size)
- [==jpetazzo.github.io: Anti-Patterns When Building Container Images==](http://jpetazzo.github.io/2021/11/30/docker-build-container-images-antipatterns/)
- [developers.redhat.com: Reduce the size of container images with DockerSlim](https://developers.redhat.com/articles/2022/01/17/reduce-size-container-images-dockerslim)
- [docker.com: Reduce Your Image Size with the Dive-In Docker Extension](https://www.docker.com/blog/reduce-your-image-size-with-the-dive-in-docker-extension/)
- [==medium.com/vantageai: How to make your Python Docker images secure, fast & small== 🌟](https://medium.com/vantageai/how-to-make-your-python-docker-images-secure-fast-small-b3a6870373a0) Exploring Image Layers and Implementing Multistage Builds
- [blog.devgenius.io: DevOps in K8s — Write Dockerfile Efficiently 🌟](https://blog.devgenius.io/devops-in-k8s-write-dockerfile-efficiently-37eaedf87163)
- [piotrminkowski.com: Slim Docker Images for Java](https://piotrminkowski.com/2023/11/07/slim-docker-images-for-java/)
- [bhupesh.me: How I reduced the size of my very first published docker image by 40% - A lesson in dockerizing shell scripts 🌟](https://bhupesh.me/publishing-my-first-ever-dockerfile-optimization-ugit/)
    - The author details their journey of reducing the size of their Docker image by 40%, from 31.4 MB to 17.6 MB
    - They discuss optimization attempts, multi-stage builds, removing unnecessary binaries and dependencies, and using `scratch` as the base image
- [medium.com/@RoussiAbel: Optimizing java base docker images size from 674Mb to 58Mb](https://medium.com/@RoussiAbel/optimizing-java-base-docker-images-size-from-674mb-to-58mb-c1b7c911f622)

## Reducing Build Time

- [nrmitchi.com: One Simple Trick for Building Images Faster 🌟](https://www.nrmitchi.com/2020/10/one-simple-trick-for-building-images-faster/?utm_sq=gkugwn5n5s)
    - ``BUILDKIT_INLINE_CACHE=1 build-arg`` is a neat flag that you could add to your docker build to reduce the build time upto 89%
- [pythonspeed.com: Docker BuildKit: faster builds, new features, and now it’s stable](https://pythonspeed.com/articles/docker-buildkit/) Building Docker images can be slow, and Docker’s build system is also missing some critical security features, in particular the ability to use build secrets without leaking them. So over the past few years the Docker developers have been working on a new backend for building images, BuildKit.
- [pauldally.medium.com: Structuring Dockerfiles For Productivity](https://pauldally.medium.com/structuring-dockerfiles-for-productivity-2681de4815a4)

## Modify containers without rebuilding

- [cloudowski.com: How to modify containers without rebuilding their image](https://cloudowski.com/articles/how-to-modify-containers-wihtout-rebuilding/)

## Docker Tools

- [Top 50 Docker Tools](https://blog.inedo.com/top-50-docker-tools)
- [docker-ecs-plugin: Docker Releases Plugin for Simplified Deployments into AWS ECS and Fargate](https://www.infoq.com/news/2020/07/docker-ecs-plugin/)
- [dive 🌟](https://github.com/wagoodman/dive) A tool for exploring a docker image, layer contents, and discovering ways to shrink the size of your Docker/OCI image. Use the dive tool to analyze a Docker image of your application. What did I learn? While Jib creates 3 layers for Spring Boot app (dependencies, resources and classes), Paketo Buildpacks places resources and classes in the same layer.
- [ctop 🌟](https://github.com/bcicen/ctop) Top-like interface for container metrics
- [phpdocker](https://github.com/sherifabdlnaby/phpdocker) Production Grade, Rootless, Pre-configured, Extendable, and Multistage
PHP Docker Image for Cloud Native Deployments (and Kubernetes)
- [dev.to: Use Kool to Dockerize Your Local Development Environment the Right Way](https://dev.to/kooldev/use-kool-to-dockerize-your-local-development-environment-the-right-way-18gl)
- [sematext: Monitor Docker Metrics & Logs 🌟](https://sematext.com/docker/) Full Docker observability: Docker metrics, logs, and events. Yes, Kubernetes & Swarm, too!
- [stepchowfun/docuum: Docuum: LRU eviction of Docker images 🌟](https://github.com/stepchowfun/docuum) Docuum performs least recently used (LRU) eviction of Docker images.
    - Docker's built-in docker image prune --all --filter until=… command serves a similar purpose. However, the built-in solution isn't ideal since it uses the image creation time, rather than the last usage time, to determine which images to remove. That means it can delete frequently used images, which may be expensive to rebuild.
    - **Docuum is ideal for use cases such as continuous integration (CI) workers, developer workstations, or any other environment in which Docker images accumulate on disk over time.** Docuum works well with tools like Toast and Docker Compose.
    - Docuum is used by Airbnb on its fleet of 1.5k+ CI workers.

- [cloudsavvyit.com: 10 Tools That Complement Docker](https://www.cloudsavvyit.com/15158/10-tools-that-complement-docker/)
- [==cybersecsi/RAUDI==](https://github.com/cybersecsi/RAUDI) A repo to automatically generate and keep updated a series of Docker images through GitHub Actions.
- [grosser/preoomkiller](https://github.com/grosser/preoomkiller) Softly kills your process with SIGTERM before it runs out of memory. Made for processes that run inside docker.
- [==ory/dockertest==](https://github.com/ory/dockertest) Write better integration tests! Dockertest helps you boot up ephermal docker images for your Go tests with minimal work. Use Docker to run your Golang integration tests against third party services on Microsoft Windows, Mac OSX and Linux!
- [==hadolint/hadolint: Haskell Dockerfile Linter==](https://github.com/hadolint/hadolint) Dockerfile linter, validate inline bash, written in Haskell
- [==ttl.sh: Anonymous & ephemeral Docker image registry 🌟==](https://ttl.sh/) Free to use. No need to sign-up. Open source.
- [==buildg: Interactive debugger for Dockerfile== 🌟](https://github.com/ktock/buildg) Interactive debugger for Dockerfile, with support for IDEs (VS Code, Emacs, Neovim, etc.)
    - [infoq.com: Debugging Large and Complex Dockerfiles Gets Easier with Buildg](https://www.infoq.com/news/2022/09/debug-dockerfiles-buildg/)
- [==github.com/google/go-containerregistry== 🌟](https://github.com/google/go-containerregistry) Go library and CLIs for working with container registries
- [==jesseduffield/lazydocker==](https://github.com/jesseduffield/lazydocker) The lazier way to manage everything docker
- [==docker.com: Docker and Ambassador Labs Announce Telepresence for Docker, Improving the Kubernetes Development Experience== 🌟](https://www.docker.com/blog/telepresence-for-docker/) - [==telepresence for docker==](https://www.docker.com/products/telepresence-for-docker/)
    - Telepresence for Docker simplifies how teams develop and test on Kubernetes. This Kubernetes development tool seamlessly creates a remote-to-local dev environment, so your teams can enjoy the ease and flexibility of local development with the collaboration and integration of a cloud development cluster.
    - You don’t need to be a Kubernetes expert, deal with K8s configuration or maintenance, or turn to expensive cloud virtual machines for your developers to quickly and efficiently develop on K8s. Telepresence for Docker is Kubernetes development simplified.
- [github.com/containrrr/watchtower](https://github.com/containrrr/watchtower) A process for automating Docker container base image updates. With watchtower you can update the running version of your containerized app simply by pushing a new image to the Docker Hub or your image registry. Watchtower will pull down the new image, gracefully shut down the existing container and restart it.

## Docker and WSL2

- [Creating the best Linux Development experience on Windows & WSL 2](https://www.docker.com/blog/creating-the-best-linux-development-experience-on-windows-wsl-2/)
- [andrewlock.net: Installing Docker Desktop for Windows and WSL 2](https://andrewlock.net/installing-docker-desktop-for-windows/)
- [medium.com/@adeelsubhan25: How to setup and build Docker Images on Windows](https://medium.com/@adeelsubhan25/how-to-setup-and-build-docker-images-on-windows-baf252152aca)

## Docker and Docker Swarm Cheat sheets

- [Docker and Docker Swarm Cheat Sheets](cheatsheets.md)

## Docker Compose

- [freecodecamp.org: a beginners guide to docker - how to create a client server side with docker compose](https://www.freecodecamp.org/news/a-beginners-guide-to-docker-how-to-create-a-client-server-side-with-docker-compose-12c8cf0ae0aa/)
- [docker.com: Announcing the Compose Specification 🌟](https://www.docker.com/blog/announcing-the-compose-specification/)
- [infoworld.com: Docker's Compose specification is now an open standard](https://www.infoworld.com/article/3536573/dockers-compose-specification-is-now-an-open-standard.html) Docker’s system for creating applications from multiple containers is now available on GitHub for all to contribute to.
- [theregister.co.uk: Compose yourselves – Docker has published multi-container app spec, needs contributors to help maintain and develop it](https://www.theregister.co.uk/2020/04/08/docker_opens_up_compose_specification/) Now focused on developers, firm wants its tools to be more universally useful. Keep it light(weight), though.
- [Awesome Compose](https://github.com/docker/awesome-compose)
- [Visual docker-compose.yml file generator 🌟](https://nuxx.io/)
- [medium: How can we easily and visually explain the Docker Compose 🌟](https://medium.com/clarusway/how-can-we-easily-and-visually-explain-the-docker-compose-53df77e9f046)
- [docker.com: Docker Compose for Amazon ECS Now Available](https://www.docker.com/blog/docker-compose-for-amazon-ecs-now-available/)
- [==geshan.com.np: Postgres with Docker and Docker compose a step-by-step guide for beginners==](https://geshan.com.np/blog/2021/12/docker-postgres/)
- [==codesolid.com: How To Use Docker and Docker Compose With Python==](https://codesolid.com/how-to-use-docker-with-python/)
- [releasehub.com: 6 Docker Compose Best Practices for Dev and Prod](https://releasehub.com/blog/6-docker-compose-best-practices-for-dev-and-prod)

## Moving Linux Services Into Containers

- [crunchtools.com: A Hacker’s Guide to Moving Linux Services into Containers. Epic 15 page blog post showing people how to move Wordpress (php), Mediawiki (php), and Request Tracker (perl) into containers](http://crunchtools.com/moving-linux-services-to-containers/)

## Windows Containers

- [medium: Windows Containers (personal) cheat sheet](https://medium.com/@sebagomez/windows-containers-personal-cheat-sheet-95c1c4d6bdf5)
- [techcommunity.microsoft.com: IIS Central Certificate Store and Windows containers](https://techcommunity.microsoft.com/t5/itops-talk-blog/iis-central-certificate-store-and-windows-containers/ba-p/4181509)

## Portainer

- [Portainer 🌟](https://www.portainer.io/) Making Docker management easy
- [Portainer Community Edition](https://www.portainer.io/products/community-edition)
- [thenewstack.io: Deploy a Persistent Kubernetes Application with Portainer](https://thenewstack.io/deploy-a-persistent-kubernetes-application-with-portainer/) Here's how to make sure all the contents of your container stay intact even after you delete the container itself.

## DockStation

- [dockstation.io](https://dockstation.io/)

## Linux Container Base Images

- [crunchtools.com: A Comparison of Linux Container Images](http://crunchtools.com/comparison-linux-container-images/)
- [kubedex.com: Base images comparison](https://kubedex.com/base-images/)
- [developers.redhat.com: Red Hat Universal Base Images for Docker users](https://developers.redhat.com/blog/2020/03/24/red-hat-universal-base-images-for-docker-users/)
    - [developers.redhat.com: book: Red Hat Universal Base Images (UBI)](https://developers.redhat.com/books/red-hat-universal-base-images-ubi)
- [dev.to: The best Docker base image for your Python application](https://dev.to/pmutua/the-best-docker-base-image-for-your-python-application-3o83)
- [Red Hat Universal Base Images - hub.docker.com/u/redhat: UBI 8 standard, minimal, micro, and init from DockerHub 🌟](https://hub.docker.com/u/redhat)
- [developers.redhat.com: Red Hat Universal Base Image and Docker Hub: Why should developers care?](https://developers.redhat.com/articles/2021/05/25/red-hat-universal-base-image-and-docker-hub-why-should-developers-care)
- [redhat.com: Red Hat Brings Red Hat Universal Base Image to Docker Hub](https://www.redhat.com/en/about/press-releases/red-hat-brings-red-hat-universal-base-image-docker-hub) Verified content from the world’s leading enterprise Linux platform aimed at helping developers and operators build more secure and scalable containerized solutions from the industry’s leading container registry

## Blogs

- [Digital Ocean: Docker Tutorials](https://www.digitalocean.com/community/tags/docker)

## Cloud Native Buildpacks

- [buildpacks.io: Cloud Native Buildpacks 🌟](https://buildpacks.io/) transform your application source code into images that can run on any cloud.
- [altoros.com: Streamlining the Creation of Docker Images with Cloud Native Buildpacks](https://www.altoros.com/blog/streamlining-the-creation-of-docker-images-with-cloud-native-buildpacks/) The new Cloud Native Buildpacks framework changes the obnoxious development chore of Dockerfile writing into a simple, automated operations pipeline. When deploying apps to Kubernetes or other container-as-a-service platforms, the proliferation of nonstandard, unauditable containers built manually via Dockerfiles is a real problem. A few products have emerged to solve this problem, among them Cloud Native Buildpacks (СNB). In this blog post, we explore the capabilities of these buildpacks and explain how to use them in build pipelines to deliver standardized, auditable images as artifacts suitable for deployment.
- [thenewstack.io: Container Images the Easy Way with Cloud Native Buildpacks](https://thenewstack.io/container-images-the-easy-way-with-cloud-native-buildpacks/)
- [dev.to/pmbanugo: Goodbye Dockerfiles: Build Secure & Optimised Node.js Container Images with Cloud Native Buildpacks](https://dev.to/pmbanugo/goodbye-dockerfiles-build-secure-optimised-nodejs-container-images-with-cloud-native-buildpacks-489p)

## Alternatives to Docker. Available alternatives to Docker for OCI compliant container image building

- [blog.alexellis.io: Building containers without Docker 🌟](https://blog.alexellis.io/building-containers-without-docker/)
- [medium: nerdctl: Docker-compatible CLI for contaiNERD](https://medium.com/nttlabs/nerdctl-359311b32d0e)
- [jfrog.com: THE BASICS: 7 Alternatives to Docker: All-in-One Solutions and Standalone Container Tools 🌟](https://jfrog.com/knowledge-base/the-basics-7-alternatives-to-docker-all-in-one-solutions-and-standalone-container-tools/)
- [nerdctl 🌟](https://github.com/containerd/nerdctl) Docker-compatible CLI for containerd
- [img](https://github.com/genuinetools/img)
- [jib](https://github.com/GoogleContainerTools/jib)
- [kaniko](https://github.com/GoogleContainerTools/kaniko)
- [buildah](https://buildah.io/)
- [buildkit](https://docs.docker.com/develop/develop-images/build_enhancements/)
- [podman](https://podman.io/)
- [==blog.logrocket.com: Top Docker alternatives for 2022==](https://blog.logrocket.com/top-docker-alternatives-2022/)
- [itnext.io: Replace Docker Desktop with lima](https://itnext.io/replace-docker-desktop-with-lima-88ec6f9d6a19) - [lima-vm/lima](https://github.com/lima-vm/lima)
- [dzone: Alternatives to Docker Desktop](https://dzone.com/articles/alternatives-to-docker-desktop) Have $5 to spend monthly? Do you want to avoid the fee? There are a couple of alternatives that can replace Docker Desktop with a free solution.
- [dzone: Docker Alternatives: 10 Alternatives to Docker for Your SaaS Application](https://dzone.com/articles/docker-alternatives-10-alternatives-to-docker-for)

## Videos and Podcasts

<details>
  <summary>Click to expand!</summary>

<center>
<iframe width="560" height="315" src="https://www.youtube.com/embed/9_s3h_GVzZc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<iframe width="560" height="315" src="https://www.youtube.com/embed/3c-iBn73dDE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<iframe width="560" height="315" src="https://www.youtube.com/embed/p2PH_YPCsis" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<iframe width="560" height="315" src="https://www.youtube.com/embed/vWSRWpOPHws" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<iframe width="560" height="315" src="https://www.youtube.com/embed/ZowjOhpAcIc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<iframe width="560" height="315" src="https://www.youtube.com/embed/n-JwAM6XF88" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
<iframe width="560" height="315" src="https://www.youtube.com/embed/EnJ7qX9fkcU" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
<iframe width="560" height="315" src="https://www.youtube.com/embed/0mxhS7H6bxM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</center>
</details>

## Tweets

<details>
  <summary>Click to expand!</summary>

<center>
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Environment variables in Docker:<br><br>Environment variables are dynamic-named values that affect how our app will behave when running.<br><br>We can define them with Docker:<br>- at runtime<br>- in the Dockerfile<br>- in the Compose file (2 ways)<br><br>Let&#39;s see in detail in 1 minute:<br><br>1/5</p>&mdash; Francesco Ciulla (@FrancescoCiull4) <a href="https://twitter.com/FrancescoCiull4/status/1393448190729465856?ref_src=twsrc%5Etfw">May 15, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Introduction to Docker🐳<a href="https://twitter.com/Docker?ref_src=twsrc%5Etfw">@Docker</a> is an open-source platform for deploying and managing containerized applications. It allows developers to easily package their applications into containers that can be deployed on every machine with a valid Docker installation.<br><br>Thread 🧵👇</p>&mdash; Gabriel Tanner (@GabrielTanner14) <a href="https://twitter.com/GabrielTanner14/status/1470411963884707844?ref_src=twsrc%5Etfw">December 13, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">How to grasp Containers and Docker (Mega Thread)<br><br>When I started using containers back in 2015, I thought they were tiny virtual machines with a subsecond startup time.<br><br>It was easy to follow tutorials from the Internet on how to put your Python or Node.js app into a container...</p>&mdash; Ivan Velichko (@iximiuz) <a href="https://twitter.com/iximiuz/status/1423984739514454033?ref_src=twsrc%5Etfw">August 7, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Okay <a href="https://twitter.com/awscloud?ref_src=twsrc%5Etfw">@awscloud</a> Lambda folks: when should I use Docker containers as the packaging format for functions vs. using native runtimes? Looking for general guidance here.</p>&mdash; Corey Quinn (@QuinnyPig) <a href="https://twitter.com/QuinnyPig/status/1508532216984313859?ref_src=twsrc%5Etfw">March 28, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Mostly bc of the package size limit.<br>Standard code zip: max 250 MB<br>Docker image: max 10 GB<br><br>If you do anything in Python with ML libs, you will need Docker...<br><br>Why use native runtimes otherwise? Cold start.<br>Docker: 750-1000 ms<br>Node/Python: 250-300 ms</p>&mdash; Maciej Radzikowski (@radzikowski_m) <a href="https://twitter.com/radzikowski_m/status/1508535101512204292?ref_src=twsrc%5Etfw">March 28, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Docker Compose + DockerSlim = ❤️<a href="https://twitter.com/DockerSlim?ref_src=twsrc%5Etfw">@DockerSlim</a> can make your images much smaller (hence, faster and securer), but it requires launching containers for runtime analysis.<br><br>Real apps, though, rarely run in isolation... Docker knew that and built Compose.<br><br>Now, behold the synergy! 🔽 <a href="https://t.co/n6NlJokC95">pic.twitter.com/n6NlJokC95</a></p>&mdash; Ivan Velichko (@iximiuz) <a href="https://twitter.com/iximiuz/status/1547233568610566144?ref_src=twsrc%5Etfw">July 13, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Debunking Container Myths 🧵<br><br>A (never-ending) series of articles that I started writing a couple of years ago to fix my own misconceptions about containers 🔽 <a href="https://t.co/bD7Iw48ere">pic.twitter.com/bD7Iw48ere</a></p>&mdash; Ivan Velichko (@iximiuz) <a href="https://twitter.com/iximiuz/status/1563851156417298434?ref_src=twsrc%5Etfw">August 28, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">What Is a Distroless Container Image? 🧵<br><br>Go (programming language) is famous for its statically linked binaries. You can take a Go executable, drop it into a &quot;FROM scratch&quot; container, and call it a day.<br><br>But there might be a problem (keep reading) 👇 <a href="https://t.co/kskCI3rqCC">pic.twitter.com/kskCI3rqCC</a></p>&mdash; Ivan Velichko (@iximiuz) <a href="https://twitter.com/iximiuz/status/1566827552781524995?ref_src=twsrc%5Etfw">September 5, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Who is still copying images between registries with: <br> docker pull &lt;src&gt;<br> docker tag &lt;src&gt; &lt;dst&gt;<br> docker push &lt;dst&gt;<br><br>Use:<br> crane cp &lt;src&gt; &lt;dst&gt;<br><br>Or even:<br> cosign cp &lt;src&gt; &lt;dst&gt;<br><br>It&#39;s faster, and supports multi-arch (and cosign copies signatures/sboms/attestations)</p>&mdash; Matt Moore ⛓🚀 (@mattomata) <a href="https://twitter.com/mattomata/status/1580369338879836160?ref_src=twsrc%5Etfw">October 13, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Want to master Docker and become a container expert<br>...but don&#39;t know how to even start? 🔽<br><br>Here is the learning order that helped me:<br><br>1. Containers: how Linux does them<br>2. Images: why they are needed<br>3. Managers: many containers, one host<br>4. Orchestrators: many hosts, one app <a href="https://t.co/HaXaGnSMkU">pic.twitter.com/HaXaGnSMkU</a></p>&mdash; Ivan Velichko (@iximiuz) <a href="https://twitter.com/iximiuz/status/1601166357826981888?ref_src=twsrc%5Etfw">December 9, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</center>
</details>
