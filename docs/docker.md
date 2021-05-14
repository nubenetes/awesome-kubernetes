# Docker
- [Introduction and Tutorials](#introduction-and-tutorials)
- [Docker Patterns and Antipatterns](#docker-patterns-and-antipatterns)
- [Security](#security)
- [How To Build a Smaller Docker Image](#how-to-build-a-smaller-docker-image)
- [Reducing Build Time](#reducing-build-time)
- [Modify containers without rebuilding](#modify-containers-without-rebuilding)
- [Docker Tools](#docker-tools)
- [Docker and WSL2](#docker-and-wsl2)
- [Docker Cheat sheet](#docker-cheat-sheet)
- [Docker Compose](#docker-compose)
- [Moving Linux Services Into Containers](#moving-linux-services-into-containers)
- [Portainer](#portainer)
- [DockStation](#dockstation)
- [Linux Container Base Images](#linux-container-base-images)
- [Blogs](#blogs)
- [Awesome Lists](#awesome-lists)
- [Cloud Native Buildpacks](#cloud-native-buildpacks)
- [Alternatives to Docker](#alternatives-to-docker)

## Introduction and Tutorials
* [Wikipedia.org: Docker](https://en.wikipedia.org/wiki/Docker_(software))
* [Awesome Docker](https://github.com/veggiemonk/awesome-docker)
* [Dzone refcard: Getting Started with Docker](https://dzone.com/refcardz/getting-started-with-docker-1)
* [Dzone refcard: Java Containerization 🌟](https://dzone.com/refcardz/java-containerization)
* [americanexpress.io: **Do Not Run Dockerized Applications as Root** 🌟](https://americanexpress.io/do-not-run-dockerized-applications-as-root/)
* [medium.com: Removing Docker Images, Containers, and Volumes with Ease](https://medium.com/@jon.froiland/removing-docker-images-containers-and-volumes-with-ease-fdf16bebccec)
* [medium.freecodecamp.com: A Beginner-Friendly Introduction to Containers, VMs and Docker](https://medium.freecodecamp.com/a-beginner-friendly-introduction-to-containers-vms-and-docker-79a9e3e119b)
* [Google Play: Learning Solution - Learn Docker 🌟](https://play.google.com/store/apps/details?id=com.LearningSolution.LearnDocker&hl=en)
* [Play with docker 🌟](https://labs.play-with-docker.com/) A simple, interactive and fun playground to learn Docker
* [blog.docker.com: Intro Guide to Dockerfile Best Practices 🌟](https://blog.docker.com/2019/07/intro-guide-to-dockerfile-best-practices/)
* [medium: Strategies of docker images optimization](https://medium.com/sciforce/strategies-of-docker-images-optimization-2ca9cc5719b6)
* [Dzone: Docker explained, an introductory guide to docker](https://dzone.com/articles/docker-explained-an-introductory-guide-to-docker)
* [Dzone: everything you need to know about docker](https://dzone.com/articles/everything-you-need-to-know-about-docker)
* [Dzone: a start to finish guide to docker with java](https://dzone.com/articles/a-start-to-finish-guide-to-docker-with-java)
* [docker.com: Intro Guide to Dockerfile Best Practices](https://www.docker.com/blog/intro-guide-to-dockerfile-best-practices/)
* [**GitHub build-push-action**](https://github.com/docker/build-push-action) Build+push official Docker GitHub action
* [docker.com: Speed Up Your Development Flow With These Dockerfile Best Practices](https://www.docker.com/blog/speed-up-your-development-flow-with-these-dockerfile-best-practices/)
* [itnext.io: Getting Started with Docker: Facts You Should Know 🌟](https://itnext.io/getting-started-with-docker-facts-you-should-know-d000e5815598)
* [jfrog.com: A Beginner’s Guide to Understanding and Building Docker Images 🌟](https://jfrog.com/knowledge-base/a-beginners-guide-to-understanding-and-building-docker-images/)
* [Broken by default: why you should avoid most Dockerfile example 🌟](https://pythonspeed.com/articles/dockerizing-python-is-hard/)
* [geekflare.com: docker tutorials](https://geekflare.com/docker-tutorials/)
* [medium: What is Docker, Why should you use it in simple words](https://medium.com/@shahinghasemy/what-is-docker-why-should-you-use-it-in-simple-words-cc5e6160f9db)
* [docker.com: Top Questions for Getting Started with Docker 🌟](https://www.docker.com/blog/top-questions-for-getting-started-with-docker/)
* [medium: How to Start Working With Docker Containers](https://medium.com/swlh/how-to-start-working-with-docker-containers-72b73ca60e0c)
* [dzone: Mitigating DevOps Repository Risks](https://dzone.com/articles/mitigating-devops-repository-risks) Docker is in the news for two reasons: Image retention limits and download throttling. Let's discuss both and see the better alternatives.
* [Top 18 Docker commands for Automation Tester/Devops/SDET/Test Lead?](https://automationreinvented.blogspot.com/2020/02/top-18-docker-commands-for-aytomation.html)
* [A Gentle Introduction to Using a Docker Container as a Dev Environment 🌟](https://css-tricks.com/a-gentle-introduction-to-using-a-docker-container-as-a-dev-environment/)
* [docs.docker.com: Deploying Docker containers on ECS](https://docs.docker.com/engine/context/ecs-integration/)
    * [AWS and Docker collaborate to simplify the developer experience](https://aws.amazon.com/blogs/containers/aws-docker-collaborate-simplify-developer-experience/)
    * [From Docker Straight to AWS](https://www.docker.com/blog/from-docker-straight-to-aws/)
* [medium: Understanding Docker Volumes, Mounts and Layers and How to Manage Data in Containers](https://medium.com/nycdev/understanding-docker-volumes-mounts-and-layers-9fa17befa493)
* [A Gentle Introduction to Using a Docker Container as a Dev Environment](https://css-tricks.com/a-gentle-introduction-to-using-a-docker-container-as-a-dev-environment/)
* [martinheinz.dev: It's Time to Forget About Docker 🌟](https://martinheinz.dev/blog/35)
* [docker.com: Docker Hub Experimental CLI tool](https://www.docker.com/blog/docker-hub-experimental-cli-tool/)
* [docker.com: Year in Review: The Most Viewed Docker Blog Posts of 2020 Part 1 🌟](https://www.docker.com/blog/year-in-review-the-most-viewed-docker-blog-posts-of-2020-part-1/)
* [docker.com: Year in Review: The Most Viewed Docker Blog Posts of 2020 Part 2 🌟](https://www.docker.com/blog/year-in-review-the-most-viewed-docker-blog-posts-of-2020-part-2/)
* [adictosaltrabajo.com: Cómo crear y desplegar microservicios con Spring Boot, Spring Cloud Netflix y Docker](https://www.adictosaltrabajo.com/2020/12/22/como-crear-y-desplegar-microservicios-con-spring-boot-spring-cloud-netflix-y-docker/)
* [cloudsavvyit.com: How to Use Cron With Your Docker Containers](https://www.cloudsavvyit.com/9033/how-to-use-cron-with-your-docker-containers/)
* [infoq.com: Docker Hub and JFrog Partnership Removes Image Pull Limits for Artifactory Users](https://www.infoq.com/news/2021/01/docker-jfrog-partnership/) 
* [technology.doximity.com: Buildpacks vs Dockerfiles 🌟](https://technology.doximity.com/articles/buildpacks-vs-dockerfiles) Exploring the tradeoffs of building container images at scale
* [docker.com: Containerized Python Development – Part 1](https://www.docker.com/blog/containerized-python-development-part-1/)
    * [docker.com: Containerized Python Development – Part 2](https://www.docker.com/blog/containerized-python-development-part-2/)
    * [docker.com: Containerized Python Development – Part 3](https://www.docker.com/blog/containerized-python-development-part-3/)
* [sysdig.com: Top 20 Dockerfile best practices 🌟](https://sysdig.com/blog/dockerfile-best-practices/)
* [pythonspeed.com: The worst so-called “best practice” for Docker](https://pythonspeed.com/articles/security-updates-in-docker/)
* [developers.redhat.com: Making environment variables accessible in front-end containers](https://developers.redhat.com/blog/2021/03/04/making-environment-variables-accessible-in-front-end-containers/)
* [towardsdatascience.com: Have you heard about our lord and savior Docker?](https://towardsdatascience.com/docker-101-ee3d2b8ace11) Introduction to working with Docker and creating your own development environment
* [medium: Dockerizing a REST API in Python Less Than 9 MB and Based on scratch Image](https://medium.com/analytics-vidhya/dockerizing-a-rest-api-in-python-less-than-9-mb-and-based-on-scratch-image-ef0ee3ad3f0a)
* [datamechanics.co: Optimized Apache Spark Docker Images](https://www.datamechanics.co/blog-post/optimized-spark-docker-images-now-available)
* [theskillpedia.com: Managing docker images - openshift tutorial](https://www.theskillpedia.com/managing-docker-images-openshift-tutorial/)
* [iximiuz.com: Container Networking Is Simple!](https://iximiuz.com/en/posts/container-networking-is-simple/)
* [r-bloggers.com: Dockerizing Shiny Applications](https://www.r-bloggers.com/2021/05/dockerizing-shiny-applications/)
* [pythonspeed.com: Docker can slow down your code and distort your benchmarks](https://pythonspeed.com/articles/docker-performance-overhead/)

## Docker Patterns and Antipatterns
- [codefresh.io: Docker anti-patterns 🌟](https://codefresh.io/containers/docker-anti-patterns/)

## Security
- [thehackernews.com: Docker Images Containing Cryptojacking Malware Distributed via Docker Hub](https://thehackernews.com/2020/06/cryptocurrency-docker-image.html)
- [acloudguru.com: 10 Docker Security Best Practices to Cut Container Chaos](https://acloudguru.com/blog/engineering/10-docker-security-best-practices-to-cut-container-chaos)
- [brianchristner.io: How to use Docker Security Scan Locally](https://brianchristner.io/how-to-use-docker-scan/) Docker included a new command called `docker scan` that scans local images against the Snyk security engine, providing you with security visibility into your local Dockerfiles and images.
- [snyk.io: 10 Docker Security Best Practices 🌟](https://snyk.io/blog/10-docker-image-security-best-practices/)
  
## How To Build a Smaller Docker Image
* [developers.redhat.com: Keep it small: a closer look at Docker image sizing](https://developers.redhat.com/blog/2016/03/09/more-about-docker-images-size/)
* [medium: How to build a smaller Docker image](https://medium.com/@gdiener/how-to-build-a-smaller-docker-image-76779e18d48a) When you’re building a Docker image it’s important to keep the size under control. Having small images means ensuring faster deployment and transfers.
* [itsopensource.com: How to Reduce Node Docker Image Size by 10X](https://itsopensource.com/how-to-reduce-node-docker-image-size-by-ten-times/)
* [blog.bitsrc.io: Best Practices for Writing a Dockerfile](https://blog.bitsrc.io/best-practices-for-writing-a-dockerfile-68893706c3) Optimize your Docker Image by following these best practices from day one.
* [sequoia.makes.software: Reducing Docker Image Size (Particularly for Kubernetes Environments) 🌟](https://sequoia.makes.software/reducing-docker-image-size-particularly-for-kubernetes-environments/)
* [itnext.io: Building Docker Images The Proper Way 🌟](https://itnext.io/building-docker-images-the-proper-way-3c9807524582) Let’s optimize Docker builds to create much smaller and more secure Docker images in a fraction of the usual build time…

## Reducing Build Time
* [nrmitchi.com: One Simple Trick for Building Images Faster 🌟](https://www.nrmitchi.com/2020/10/one-simple-trick-for-building-images-faster/?utm_sq=gkugwn5n5s)
    * ``BUILDKIT_INLINE_CACHE=1 build-arg`` is a neat flag that you could add to your docker build to reduce the build time upto 89%
* [pythonspeed.com: Docker BuildKit: faster builds, new features, and now it’s stable](https://pythonspeed.com/articles/docker-buildkit/) Building Docker images can be slow, and Docker’s build system is also missing some critical security features, in particular the ability to use build secrets without leaking them. So over the past few years the Docker developers have been working on a new backend for building images, BuildKit.

## Modify containers without rebuilding
* [cloudowski.com: How to modify containers without rebuilding their image](https://cloudowski.com/articles/how-to-modify-containers-wihtout-rebuilding/)

## Docker Tools
- [Top 50 Docker Tools](https://blog.inedo.com/top-50-docker-tools)
- [docker-ecs-plugin: Docker Releases Plugin for Simplified Deployments into AWS ECS and Fargate](https://www.infoq.com/news/2020/07/docker-ecs-plugin/)
- [dive 🌟](https://github.com/wagoodman/dive) A tool for exploring a docker image, layer contents, and discovering ways to shrink the size of your Docker/OCI image. Use the dive tool to analyze a Docker image of your application. What did I learn? While Jib creates 3 layers for Spring Boot app (dependencies, resources and classes), Paketo Buildpacks places resources and classes in the same layer.

## Docker and WSL2
- [Creating the best Linux Development experience on Windows & WSL 2](https://www.docker.com/blog/creating-the-best-linux-development-experience-on-windows-wsl-2/)
- [andrewlock.net: Installing Docker Desktop for Windows and WSL 2](https://andrewlock.net/installing-docker-desktop-for-windows/)

## Docker Cheat sheet
* [Docker Cheat Sheets](cheatsheets.md)

## Docker Compose
- [freecodecamp.org: a beginners guide to docker - how to create a client server side with docker compose](https://www.freecodecamp.org/news/a-beginners-guide-to-docker-how-to-create-a-client-server-side-with-docker-compose-12c8cf0ae0aa/)
* [docker.com: Announcing the Compose Specification 🌟](https://www.docker.com/blog/announcing-the-compose-specification/)
* [infoworld.com: Docker's Compose specification is now an open standard](https://www.infoworld.com/article/3536573/dockers-compose-specification-is-now-an-open-standard.html) Docker’s system for creating applications from multiple containers is now available on GitHub for all to contribute to.
* [theregister.co.uk: Compose yourselves – Docker has published multi-container app spec, needs contributors to help maintain and develop it](https://www.theregister.co.uk/2020/04/08/docker_opens_up_compose_specification/) Now focused on developers, firm wants its tools to be more universally useful. Keep it light(weight), though.
* [Awesome Compose](https://github.com/docker/awesome-compose)
* [Visual docker-compose.yml file generator 🌟](https://nuxx.io/)
* [medium: How can we easily and visually explain the Docker Compose 🌟](https://medium.com/clarusway/how-can-we-easily-and-visually-explain-the-docker-compose-53df77e9f046)
* [docker.com: Docker Compose for Amazon ECS Now Available](https://www.docker.com/blog/docker-compose-for-amazon-ecs-now-available/)

## Moving Linux Services Into Containers
* [crunchtools.com: A Hacker’s Guide to Moving Linux Services into Containers. Epic 15 page blog post showing people how to move Wordpress (php), Mediawiki (php), and Request Tracker (perl) into containers](http://crunchtools.com/moving-linux-services-to-containers/)

## Portainer
* [Portainer 🌟](https://www.portainer.io/) Making Docker management easy
* [Portainer Community Edition](https://www.portainer.io/products/community-edition)

## DockStation
- [dockstation.io](https://dockstation.io/)

## Linux Container Base Images
* [crunchtools.com: A Comparison of Linux Container Images](http://crunchtools.com/comparison-linux-container-images/)
* [kubedex.com: Base images comparison](https://kubedex.com/base-images/)
* [developers.redhat.com: Red Hat Universal Base Images for Docker users](https://developers.redhat.com/blog/2020/03/24/red-hat-universal-base-images-for-docker-users/)
    * [book: Red Hat Universal Base Images (UBI)](https://developers.redhat.com/books/red-hat-universal-base-images-ubi)

## Blogs
- [Digital Ocean: Docker Tutorials](https://www.digitalocean.com/community/tags/docker)

## Awesome Lists
* [Awesome Docker 🌟](https://github.com/veggiemonk/awesome-docker)
* [Awesome Compose 🌟](https://github.com/docker/awesome-compose)

## Cloud Native Buildpacks
- [buildpacks.io: Cloud Native Buildpacks 🌟](https://buildpacks.io/) transform your application source code into images that can run on any cloud.
- [altoros.com: Streamlining the Creation of Docker Images with Cloud Native Buildpacks](https://www.altoros.com/blog/streamlining-the-creation-of-docker-images-with-cloud-native-buildpacks/) The new Cloud Native Buildpacks framework changes the obnoxious development chore of Dockerfile writing into a simple, automated operations pipeline. When deploying apps to Kubernetes or other container-as-a-service platforms, the proliferation of nonstandard, unauditable containers built manually via Dockerfiles is a real problem. A few products have emerged to solve this problem, among them Cloud Native Buildpacks (СNB). In this blog post, we explore the capabilities of these buildpacks and explain how to use them in build pipelines to deliver standardized, auditable images as artifacts suitable for deployment.

## Alternatives to Docker
- [blog.alexellis.io: Building containers without Docker 🌟](https://blog.alexellis.io/building-containers-without-docker/)
- [medium: nerdctl: Docker-compatible CLI for contaiNERD](https://medium.com/nttlabs/nerdctl-359311b32d0e)
- [jfrog.com: THE BASICS: 7 Alternatives to Docker: All-in-One Solutions and Standalone Container Tools 🌟](https://jfrog.com/knowledge-base/the-basics-7-alternatives-to-docker-all-in-one-solutions-and-standalone-container-tools/)

<iframe scrolling="no" frameborder="no" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/273312823&amp;color=ff5500"></iframe>

<iframe src="https://www.youtube.com/embed/n-JwAM6XF88" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

<iframe src="https://www.youtube.com/embed/EnJ7qX9fkcU" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
