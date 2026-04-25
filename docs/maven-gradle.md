# Maven, Gradle & SDKMAN

1. [Apache Maven](#apache-maven)
    1. [Scaffolding a project with Maven (maven archetype)](#scaffolding-a-project-with-maven-maven-archetype)
    2. [Maven Tests](#maven-tests)
    3. [Dependency Resolution in Maven](#dependency-resolution-in-maven)
    4. [Maven and Docker](#maven-and-docker)
    5. [IDEs](#ides)
        1. [Intellij IDEA](#intellij-idea)
    6. [Maven Plugins](#maven-plugins)
    7. [Maven Cheat Sheets](#maven-cheat-sheets)
    8. [Other Commands](#other-commands)
    9. [Docker Maven Plugin (fabric8)](#docker-maven-plugin-fabric8)
    10. [Fabric8 Maven Plugin (deprecated)](#fabric8-maven-plugin-deprecated)
2. [Eclipse JKube (formerly known as Fabric8 Maven Plugin) - Kubernetes & OpenShift Maven and Gradle Plugins](#eclipse-jkube-formerly-known-as-fabric8-maven-plugin---kubernetes--openshift-maven-and-gradle-plugins)
3. [Gradle](#gradle)
    1. [Gradle Cheat Sheets](#gradle-cheat-sheets)
4. [SDKMAN](#sdkman)
5. [Related Tools](#related-tools)

## Apache Maven

- [maven.apache.org](https://maven.apache.org/)
	- [apache/maven-mvnd](https://github.com/apache/maven-mvnd) Apache Maven Daemon. Easy way to speed up local build especially in multi-module Maven project - use Maven Daemon (mvnd)! mvnd builds Spring Cloud AWS 28% faster than traditional mvn command 
- [howtodoinjava.com/maven](https://howtodoinjava.com/maven/)
- [maarten.mulders.it: What's New in Maven 4](https://maarten.mulders.it/2020/11/whats-new-in-maven-4/)
- [dev.to: Maven Plugin Configuration - The (Unknown) Tiny Details](https://dev.to/khmarbaise/maven-plugin-configuration-the-unknown-tiny-details-1emm)
- [ashishtechmill.com: Demystifying Google Container Tool Jib: Java Image Builder](https://ashishtechmill.com/demystifying-google-container-tool-jib-java-image-builder) This article covers some internals of image layering created by container image builder Jib and explore what distroless images are and their benefits.
- Maven 3.8.2 is available now! It contains several fixes and non invasive backports from the Maven 4 branch. 
- [phauer.com: Why I Moved Back from Gradle to Maven](https://phauer.com/2018/moving-back-from-gradle-to-maven/)
- [rieckpil.de: Maven Setup For Testing Java Applications](https://rieckpil.de/maven-setup-for-testing-java-applications/)

### Scaffolding a project with Maven (maven archetype)

- [vogella.com: Maven for Building Java application - Tutorial](https://www.vogella.com/tutorials/ApacheMaven/article.html)
- [maven.apache.org: Introduction to the Standard Directory Layout](http://maven.apache.org/guides/introduction/introduction-to-the-standard-directory-layout.html)
- [Handwritten Maven archetype project scaffolding](http://www.programmersought.com/article/1858176023/)

### Maven Tests


### Dependency Resolution in Maven

- [Apache Maven Dependency Analyzer](https://maven.apache.org/shared/maven-dependency-analyzer/index.html)

```bash
mvn dependency:analyze  (shows you the usage of listed and unlisted dependencies)
mvn dependency:resolve  (give me a list of everything I have declared, a nice way to avoid reading the POM file)
mvn dependency:tree     (how you got something on your classpath)
```

### Maven and Docker


### IDEs

- [code.visualstudio.com: Java Project Management in VS Code](https://code.visualstudio.com/docs/java/java-project)

#### Intellij IDEA

- [jetbrains.com/help/idea/maven-support.html](https://www.jetbrains.com/help/idea/maven-support.html)
- [howtodoinjava.com: Maven IntelliJ Idea Project](https://howtodoinjava.com/maven/how-to-convert-maven-java-project-to-intellij-idea-project/)

### Maven Plugins

- [Apache Maven Changelog Plugin](https://maven.apache.org/plugins/maven-changelog-plugin/)
- [Apache Maven Checkstyle Plugin](https://maven.apache.org/plugins/maven-checkstyle-plugin/)
- [Apache Maven Javadoc Plugin](https://maven.apache.org/plugins/maven-javadoc-plugin/)
- [Maven Surefire Report Plugin](https://maven.apache.org/surefire/maven-surefire-report-plugin/)

### Maven Cheat Sheets

- [Maven Cheat Sheets](cheatsheets.md)

### Other Commands

- Display contents of a jar file:

```bash
jar tf target/example-1.0.0-SNAPSHOT.jar
```

### Docker Maven Plugin (fabric8)

- [docker-maven-plugin](https://github.com/fabric8io/docker-maven-plugin) This is a Maven plugin for building Docker images and managing containers for integration tests. It works with Maven 3.0.5 and Docker 1.6.0 or later.

### Fabric8 Maven Plugin (deprecated)


## Eclipse JKube (formerly known as Fabric8 Maven Plugin) - Kubernetes & OpenShift Maven and Gradle Plugins

- [Eclipse JKube 🌟](https://www.eclipse.org/jkube/) Cloud-Native Java Applications without a hassle. Eclipse JKube is a collection of plugins and libraries that are used for building container images using Docker, JIB or S2I build strategies. Eclipse JKube generates and deploys Kubernetes/OpenShift manifests at compile time too. It brings your Java applications on to Kubernetes and OpenShift by leveraging the tasks required to make your application cloud-native. Eclipse JKube also provides a set of tools such as watch, debug, log, etc. to improve your developer experience.
- [GitHub: Eclipse JKube](https://github.com/eclipse/jkube)
- [eclipse.org: Migration Guide for projects using Fabric8 Maven Plugin to Eclipse JKube 🌟](https://www.eclipse.org/jkube/docs/migration-guide/)
- [YouTube: Deploying a Quarkus application into Kubernetes using JKube | Cloud Tool Time | Marc Nuri 🌟](https://www.youtube.com/watch?v=HDDfdZqwM1E&ab_channel=EclipseFoundation)
- [blog.marcnuri.com: Eclipse JKube introduction: Java tools and plugins for Kubernetes and OpenShift](https://blog.marcnuri.com/eclipse-jkube-introduction-kubernetes-openshift)
- [blog.marcnuri.com: Eclipse JKube 1.4.0 is now available!](https://blog.marcnuri.com/eclipse-jkube-1-4-0)

## Gradle

- [gradle.org](https://gradle.org/)
- [docs.gradle.org: Getting Started](https://docs.gradle.org/current/userguide/getting_started.html)
- [Playing with gradle](https://develosapiens.wordpress.com/2015/05/08/playing-with-gradle/)

### Gradle Cheat Sheets

- [Gradle Cheat Sheets](cheatsheets.md)

## SDKMAN

- [SdkMan](https://sdkman.io/) is a tool for managing parallel versions of multiple Software Development Kits on most Unix based systems. It provides a convenient Command Line Interface (CLI) and API for installing, switching, removing and listing Candidates. Formerly known as **GVM** the **Groovy enVironment Manager**, it was inspired by the very useful [RVM](https://rvm.io/) and [rbenv](https://github.com/sstephenson/rbenv) tools, used at large by the Ruby community.
- [Using Jenkins Pipeline parallel stages to build Maven project with different JDKs](https://e.printstacktrace.blog/using-jenkins-pipeline-parallel-stages-to-build-maven-project-with-different-jdks/)
- **Demo:** A single Jenkinsfile, a Java Maven project, a single Dockerfile, multiple Java versions build and tested in parallel thanks to SDKMAN:
    - [Using SDKMAN! as a docker image for Jenkins Pipeline - a step by step guide 🌟](https://e.printstacktrace.blog/using-sdkman-as-a-docker-image-for-jenkins-pipeline-a-step-by-step-guide/)
    - [Multiple Java versions in a single Jenkins Pipeline using Docker and SDKMAN🌟](https://www.youtube.com/watch?v=j1lH3vOhucw) In this video, I show you how you can use Jenkins Declarative Pipeline to create a build pipeline that compiles the Maven Java project using three different Java versions (8, 11, and 15.) You will learn how to use a matrix section of the Jenkins Pipeline to define parallel stages, as well as how to create a Docker image that provides both Java and Maven using the powerful SDKMAN command-line tool. After watching this video you should feel comfortable with setting up multiple parallel stages to build your Java project using different versions of the compiler. And what is most important - it does not require creating Dockerfiles for each Java version. I will show you how to build the pipeline using just a single Dockerfile that does the job. 
    - [Jenkins Pipeline Maven build demo](https://github.com/wololock/jenkine-pipeline-maven-demo/tree/sdkman)

## Related Tools

- [jitpack.io 🌟](https://jitpack.io) Easy to use package repository for Git. Publish your JVM and Android libraries. Publishing your own library to the Maven Central repository may be a painful experience. Therefore, you may just create a GitHub Release for your library, and then include it as a dependency using jitpack.
- [JBang](https://www.jbang.dev/) Run Java code directly. Reuse Maven dependencies with ease. Lets Students, Educators and Professional Developers create, edit and run self-contained source-only Java programs with unprecedented ease.