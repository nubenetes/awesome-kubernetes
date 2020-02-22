# Maven
* [Wikipedia.org: Apache Maven](https://en.wikipedia.org/wiki/Apache_Maven)
* [https://maven.apache.org/](https://maven.apache.org/)
* [Dzone.com: Starting with Apache Maven](https://dzone.com/articles/starting-with-apache-maven)
* [Dzone.com: Maven Demystified](https://dzone.com/articles/maven-demystified)
* [Dzone.com: Creating a Maven Archetype](https://dzone.com/articles/create-maven-archetype-1)
* [Dzone refcard: Apache Maven 2](https://dzone.com/asset/download/212)
* [Dzone refcard: Getting Started with Maven Repository Management](https://dzone.com/asset/download/223)
* [Dzone: Installing Maven With Your JDK](https://dzone.com/articles/installing-maven)

## Maven Tests
* [Dzone: Maven Skipping Tests](https://dzone.com/articles/maven-skipping-tests)
* [Dzone: Integration Tests with Maven](https://dzone.com/articles/integration-tests-with-maven)
* [Dzone.com: Running Cucumber with Maven](https://dzone.com/articles/running-cucumber-with-maven)

## Dependency resolution in maven
* [Apache Maven Dependency Analyzer](https://maven.apache.org/shared/maven-dependency-analyzer/index.html)
* [Dzone.com: Solving Dependency conflicts in maven](https://dzone.com/articles/solving-dependency-conflicts-in-maven)
* [Dzone.com: Taming Maven: Transitive Dependency Pitfalls](https://dzone.com/articles/taming-maven-transitive-dependency-pitfalls)
* [Dzone.com: Maven Dependency Management Without Going Full Maven](https://dzone.com/articles/maven-dependency-management-without-going-full-mav) If you like using Maven to manage your projects, check out the MyEclipse IDE with its dependencies only mode, allowing you to take advantage of just this feature

```
mvn dependency:analyze  (shows you the usage of listed and unlisted dependencies)
mvn dependency:resolve  (give me a list of everything I have declared, a nice way to avoid reading the POM file)
mvn dependency:tree     (how you got something on your classpath)
```

## Maven and Docker
* [Dzone: Meet the Docker Maven Plugin!](https://dzone.com/articles/meet-the-docker-maven-plugin) 

## IDEs
* [Dzone: Maven, Eclipse, and Java 9](https://dzone.com/articles/maven-eclipse-and-java-9) Eclipse users who use Maven are used to the M2E plugin issue of having your JRE reset on you. But there's an additional gotcha between Java 8 and Java 9. 
* [code.visualstudio.com: Java Project Management in VS Code](https://code.visualstudio.com/docs/java/java-project)
* [medium.com: Instalación de Java y Visual Studio Code en plataformas Windows](https://medium.com/habasconchocos/instalaci%C3%B3n-de-java-y-visual-studio-code-en-plataformas-windows-1fa47a69497f)

## Other commands
```
jar tf target/example-1.0.0-SNAPSHOT.jar
```
