# Maven & Gradle
- [Apache Maven](#apache-maven)
    - [Scaffolding a project with Maven (maven archetype)](#scaffolding-a-project-with-maven-maven-archetype)
    - [Maven Tests](#maven-tests)
    - [Dependency Resolution in Maven](#dependency-resolution-in-maven)
    - [Maven and Docker](#maven-and-docker)
    - [IDEs](#ides)
        - [Intellij IDEA](#intellij-idea)
    - [Maven Plugins](#maven-plugins)
    - [Maven Cheat Sheets](#maven-cheat-sheets)
    - [Other Commands](#other-commands)
    - [Fabric8 Maven Plugin](#fabric8-maven-plugin)
- [Gradle](#gradle)
    - [Gradle Cheat Sheets](#gradle-cheat-sheets)

## Apache Maven
* [Wikipedia.org: Apache Maven](https://en.wikipedia.org/wiki/Apache_Maven)
* [maven.apache.org](https://maven.apache.org/)
* [twitter.com/ASFMavenProject: The official twitter feed of the Apache Maven Project](https://twitter.com/ASFMavenProject)
* [twitter.com/ASFMavenRelease: Maven Plugin Release](https://twitter.com/ASFMavenRelease) Tweets of plugin releases
* [Dzone.com: Starting with Apache Maven](https://dzone.com/articles/starting-with-apache-maven)
* [Dzone.com: Maven Demystified](https://dzone.com/articles/maven-demystified)
* [Dzone.com: Creating a Maven Archetype](https://dzone.com/articles/create-maven-archetype-1)
* [Dzone refcard: Apache Maven 2](https://dzone.com/asset/download/212)
* [Dzone refcard: Getting Started with Maven Repository Management](https://dzone.com/asset/download/223)
* [Dzone: Installing Maven With Your JDK](https://dzone.com/articles/installing-maven)
* [Dzone: 10 Effective Tips on Using Maven](https://dzone.com/articles/10-effective-tips-on-using-maven)
* [Dzone: Building Java Applications With Maven](https://dzone.com/articles/building-java-applications-with-maven)
* [howtodoinjava.com/maven](https://howtodoinjava.com/maven/)

### Scaffolding a project with Maven (maven archetype)
* [vogella.com: Maven for Building Java application - Tutorial](https://www.vogella.com/tutorials/ApacheMaven/article.html)
* [maven.apache.org: Introduction to the Standard Directory Layout](http://maven.apache.org/guides/introduction/introduction-to-the-standard-directory-layout.html)
* [Handwritten Maven archetype project scaffolding](http://www.programmersought.com/article/1858176023/)
* [programmer.ink: Maven scaffolding best practices](https://programmer.ink/think/maven-scaffolding-best-practices.html)
* [Create the scaffolding for your microservice](http://fuse.labs.osecloud.com/fuse/creating-a-microservices-project-with-maven/) We will use an existing maven archetype that assembles a CDI-based Camel java project that we will then alter to implement the service.

### Maven Tests
* [Dzone: Maven Skipping Tests](https://dzone.com/articles/maven-skipping-tests)
* [Dzone: Integration Tests with Maven](https://dzone.com/articles/integration-tests-with-maven)
* [Dzone.com: Running Cucumber with Maven](https://dzone.com/articles/running-cucumber-with-maven)

### Dependency Resolution in Maven
* [Apache Maven Dependency Analyzer](https://maven.apache.org/shared/maven-dependency-analyzer/index.html)
* [Dzone.com: Solving Dependency conflicts in maven](https://dzone.com/articles/solving-dependency-conflicts-in-maven)
* [Dzone.com: Taming Maven: Transitive Dependency Pitfalls](https://dzone.com/articles/taming-maven-transitive-dependency-pitfalls)
* [Dzone.com: Maven Dependency Management Without Going Full Maven](https://dzone.com/articles/maven-dependency-management-without-going-full-mav) If you like using Maven to manage your projects, check out the MyEclipse IDE with its dependencies only mode, allowing you to take advantage of just this feature

```
mvn dependency:analyze  (shows you the usage of listed and unlisted dependencies)
mvn dependency:resolve  (give me a list of everything I have declared, a nice way to avoid reading the POM file)
mvn dependency:tree     (how you got something on your classpath)
```

### Maven and Docker
* [Dzone: Meet the Docker Maven Plugin!](https://dzone.com/articles/meet-the-docker-maven-plugin) 

### IDEs
* [Dzone: Maven, Eclipse, and Java 9](https://dzone.com/articles/maven-eclipse-and-java-9) Eclipse users who use Maven are used to the M2E plugin issue of having your JRE reset on you. But there's an additional gotcha between Java 8 and Java 9. 
* [code.visualstudio.com: Java Project Management in VS Code](https://code.visualstudio.com/docs/java/java-project)
* [medium.com: Instalación de Java y Visual Studio Code en plataformas Windows](https://medium.com/habasconchocos/instalaci%C3%B3n-de-java-y-visual-studio-code-en-plataformas-windows-1fa47a69497f)

#### Intellij IDEA
* [jetbrains.com/help/idea/maven-support.html](https://www.jetbrains.com/help/idea/maven-support.html)
* [Dzone: Maven IntelliJ Idea Project](https://dzone.com/articles/importing-a-maven-project-in-intellij-idea)
* [vaadin.com/learn/tutorials/import-maven-project-intellij-idea](https://vaadin.com/learn/tutorials/import-maven-project-intellij-idea)
* [javaspringvaadin.wordpress.com: Crea un Proyecto Maven desde el IDE IntelliJ IDEA](https://javaspringvaadin.wordpress.com/2018/05/22/mavenintellijidea/)
* [howtodoinjava.com: Maven IntelliJ Idea Project](https://howtodoinjava.com/maven/how-to-convert-maven-java-project-to-intellij-idea-project/)

### Maven Plugins
* [Apache Maven Changelog Plugin](https://maven.apache.org/plugins/maven-changelog-plugin/)
* [Apache Maven Checkstyle Plugin](https://maven.apache.org/plugins/maven-checkstyle-plugin/)
* [Apache Maven Javadoc Plugin](https://maven.apache.org/plugins/maven-javadoc-plugin/)
* [Maven Surefire Report Plugin](https://maven.apache.org/surefire/maven-surefire-report-plugin/)

### Maven Cheat Sheets
* [Maven Cheat Sheets](cheatsheets.md)

### Other Commands
* Display contents of a jar file:

```bash
jar tf target/example-1.0.0-SNAPSHOT.jar
```

### Fabric8 Maven Plugin
- [developers.redhat.com: How the fabric8 Maven plug-in deploys Java applications to OpenShift](https://developers.redhat.com/blog/2020/05/28/how-the-fabric8-maven-plug-in-deploys-java-applications-to-openshift/)

## Gradle
- [gradle.org](https://gradle.org/)
- [docs.gradle.org: Getting Started](https://docs.gradle.org/current/userguide/getting_started.html)
- [Dzone: "Refined" Gradle](https://dzone.com/articles/refined-gradle)
- [Dzone: simplify your script build with gradle](https://dzone.com/articles/simplify-your-script-build-with-gradle)
- [Dzone: build a java app with gradle](https://dzone.com/articles/build-a-java-app-with-gradle)
- [Playing with gradle](https://develosapiens.wordpress.com/2015/05/08/playing-with-gradle/)

### Gradle Cheat Sheets
- [Gradle Cheat Sheets](cheatsheets.md)