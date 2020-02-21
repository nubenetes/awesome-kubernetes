# Maven
* [Wikipedia.org: Apache Maven](https://en.wikipedia.org/wiki/Apache_Maven)
* [https://maven.apache.org/](https://maven.apache.org/)
  * [Apache Maven Dependency Analyzer](https://maven.apache.org/shared/maven-dependency-analyzer/index.html)
* [Dzone.com: Starting with Apache Maven](https://dzone.com/articles/starting-with-apache-maven)
* [Dzone.com: Solving Dependency conflicts in maven](https://dzone.com/articles/solving-dependency-conflicts-in-maven)
* [Dzone refcard: Apache Maven 2](https://dzone.com/asset/download/212)
* [Dzone refcard: Getting Started with Maven Repository Management](https://dzone.com/asset/download/223)


## Dependency resolution in maven

```
mvn dependency:analyze  (shows you the usage of listed and unlisted dependencies)
mvn dependency:resolve  (give me a list of everything I have declared, a nice way to avoid reading the POM file)
mvn dependency:tree     (how you got something on your classpath)
```

## jar commands
```
jar tf target/example-1.0.0-SNAPSHOT.jar
```
