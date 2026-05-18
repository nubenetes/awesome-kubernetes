# Maven Gradle

!!! info "Architectural Context"
    Detailed reference for Maven Gradle in the context of Developer Ecosystem.

## Table of Contents

---

  - [twitter.com/ASFMavenProject: The official twitter feed of the Apache Maven Project](https://x.com/ASFMavenProject)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [twitter.com/ASFMavenRelease: Maven Plugin Release](https://x.com/ASFMavenRelease)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [ashishtechmill.com: Demystifying Google Container Tool Jib: Java Image Builder](https://www.ashishtechmill.com/demystifying-google-container-tool-jib-java-image-builder)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [maven.apache.org: Introduction to the Standard Directory Layout](http://maven.apache.org/guides/introduction/introduction-to-the-standard-directory-layout.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Handwritten Maven archetype project scaffolding](http://www.programmersought.com/article/1858176023)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [howtodoinjava.com: Maven IntelliJ Idea Project](https://howtodoinjava.com/maven/maven-java-project-with-intellij-idea)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Eclipse JKube 🌟](https://eclipse.dev/jkube)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [GitHub: Eclipse JKube](https://github.com/eclipse-jkube/jkube)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [eclipse.org: Migration Guide for projects using Fabric8 Maven Plugin to Eclipse JKube 🌟](https://eclipse.dev/jkube/docs/migration-guide)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [maven.apache.org](https://maven.apache.org)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [apache/maven-mvnd](https://github.com/apache/maven-mvnd)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [howtodoinjava.com/maven](https://howtodoinjava.com/maven)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [maarten.mulders.it: What's New in Maven 4](https://maarten.mulders.it/2020/11/whats-new-in-maven-4)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [dev.to: Maven Plugin Configuration - The (Unknown) Tiny Details](https://dev.to/khmarbaise/maven-plugin-configuration-the-unknown-tiny-details-1emm)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.testproject.io: Getting Started with Maven in Less Than 10 Minutes – Part 1](https://blog.testproject.io/2021/06/28/getting-started-with-maven-part-1)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [phauer.com: Why I Moved Back from Gradle to Maven](https://phauer.com/2018/moving-back-from-gradle-to-maven)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [rieckpil.de: Maven Setup For Testing Java Applications](https://rieckpil.de/maven-setup-for-testing-java-applications)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [vogella.com: Maven for Building Java application - Tutorial](https://www.vogella.com/tutorials/ApacheMaven/article.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Apache Maven Dependency Analyzer](https://maven.apache.org/shared/maven-dependency-analyzer/index.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [code.visualstudio.com: Java Project Management in VS Code](https://code.visualstudio.com/docs/java/java-project)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [jetbrains.com/help/idea/maven-support.html](https://www.jetbrains.com/help/idea/maven-support.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Apache Maven Changelog Plugin](https://maven.apache.org/plugins/maven-changelog-plugin)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Apache Maven Checkstyle Plugin](https://maven.apache.org/plugins/maven-checkstyle-plugin)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Apache Maven Javadoc Plugin](https://maven.apache.org/plugins/maven-javadoc-plugin)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Maven Surefire Report Plugin](https://maven.apache.org/surefire/maven-surefire-report-plugin)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [docker-maven-plugin](https://github.com/fabric8io/docker-maven-plugin)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [developers.redhat.com: How the fabric8 Maven plug-in deploys Java applications to OpenShift](https://developers.redhat.com/blog/2020/06/02/how-the-fabric8-maven-plug-in-deploys-java-applications-to-openshift)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [developers.redhat.com: Migrating from Fabric8 Maven Plugin to Eclipse JKube 1.0.0](https://developers.redhat.com/blog/2020/09/21/migrating-from-fabric8-maven-plugin-to-eclipse-jkube-1-0-0)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [developers.redhat.com: Cloud-native Java applications made easy: Eclipse JKube 1.0.0 now available](https://developers.redhat.com/blog/2020/09/09/cloud-native-java-applications-made-easy-eclipse-jkube-1-0-0-now-available)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [developers.redhat.com: Java development on top of Kubernetes using Eclipse JKube](https://developers.redhat.com/blog/2020/08/24/java-development-on-top-of-kubernetes-using-eclipse-jkube)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [youtube: Deploying a Quarkus application into Kubernetes using JKube | Cloud Tool Time | Marc Nuri 🌟](https://www.youtube.com/watch?v=HDDfdZqwM1E&ab_channel=EclipseFoundation)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.marcnuri.com: Eclipse JKube introduction: Java tools and plugins for Kubernetes and OpenShift](https://blog.marcnuri.com/eclipse-jkube-introduction-kubernetes-openshift)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.marcnuri.com: Eclipse JKube 1.4.0 is now available!](https://blog.marcnuri.com/eclipse-jkube-1-4-0)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [gradle.org](https://gradle.org)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [docs.gradle.org: Getting Started](https://docs.gradle.org/current/userguide/getting_started.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Playing with gradle](https://develosapiens.wordpress.com/2015/05/08/playing-with-gradle)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [SdkMan](https://sdkman.io)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Using Jenkins Pipeline parallel stages to build Maven project with different JDKs](https://e.printstacktrace.blog/using-jenkins-pipeline-parallel-stages-to-build-maven-project-with-different-jdks)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Using SDKMAN! as a docker image for Jenkins Pipeline - a step by step guide 🌟](https://e.printstacktrace.blog/using-sdkman-as-a-docker-image-for-jenkins-pipeline-a-step-by-step-guide)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [jitpack.io 🌟](https://jitpack.io)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [JBang](https://www.jbang.dev)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
