# QA/TestOps - Continuous Testing. Software Quality Test Automation

1. [Introduction](#introduction)
2. [Blogs](#blogs)
3. [Testing Frameworks](#testing-frameworks)
4. [Release Testing](#release-testing)
5. [Tools](#tools)
6. [Performance Testing](#performance-testing)
7. [Kubernetes conformance testing tools](#kubernetes-conformance-testing-tools)
8. [Codeless Automation Testing](#codeless-automation-testing)
9. [Images](#images)
10. [Tweets](#tweets)

## Introduction

- [Awesome Test Automation](https://github.com/atinfo/awesome-test-automation)
- [Awesome Software Quality](https://github.com/ligurio/awesome-software-quality)
- [linkedin.com/pulse: Importance of API Automation Testing 🌟](https://www.linkedin.com/pulse/importance-api-automation-testing-manish-saini/)
- [thenewstack.io: Optimizing App Performance in a Multicloud Stack](https://thenewstack.io/optimizing-app-performance-in-a-multicloud-stack/)
- [lambdatest.com: TestNG vs JUnit : Which testing framework should you choose?](https://www.lambdatest.com/blog/testng-vs-junit-which-testing-framework-should-you-choose/)
the #1 test automation community.
- [rookout.com: How Real-Time Debugging Improves Reliability](https://www.rookout.com/blog/how-real-time-debugging-improves-reliability)
- [thenewstack.io: 7 Benefits of Testing in Isolation](https://thenewstack.io/7-benefits-of-testing-in-isolation/)
- [thenewstack.io: Error Handling from Backends to the Frontend](https://thenewstack.io/error-handling-from-backends-to-the-frontend/)
- [==lambdatest.com: Top Automation Testing Trends To Look Out In 2021==](https://www.lambdatest.com/blog/top-automation-testing-trends-2021)
- [dev.to: Test-Driven-Development with Django: Unit Testing & Integration testing with Docker, Flask & Github Actions](https://dev.to/koladev/test-driven-development-with-django-unit-testing-integration-testing-with-docker-flask-github-actions-2047)
- [smashingmagazine.com: Testing Pipeline 101 For Frontend Testing](https://www.smashingmagazine.com/2022/02/testing-pipeline-101-frontend-testing/)
- [infoq.com: Maintaining Software Quality with Microservices](https://www.infoq.com/presentations/microservices-software-quality/)
- [speakerdeck.com/thockin: Code Review in Kubernetes](https://speakerdeck.com/thockin/code-review-in-kubernetes)
- [getxray.app: The top 5 software testing trends of 2022](https://www.getxray.app/blog/the-top-5-software-testing-trends-of-2022)
- [linkedin.com: Microservices are testable in isolation 🌟](https://www.linkedin.com/pulse/microservices-testable-isolation-chris-richardson/)
- [softwaretestingsapiens.com: Roadmap to learn API Testing in Just 30 days](https://www.softwaretestingsapiens.com/roadmap-to-learn-api-testing/)

## Blogs

- https://automationqahub.com/
- https://www.botplayautomation.com/
- https://www.lambdatest.com/
- https://blog.testproject.io/

## Testing Frameworks

- [JUnit](https://junit.org)
    - [lambdatest.com](https://www.lambdatest.com/blog/junit5-extensions/) A Comprehensive Guide On JUnit 5 Extensions
- [TestNG](https://testng.org)
- [Spock Framework](https://spockframework.org)
- [opensource.com: Perform unit tests using GoogleTest and CTest](https://opensource.com/article/22/1/unit-testing-googletest-ctest) Using unit tests will likely improve your code's quality and do so without disturbing your workflow.

## Release Testing

- [launchdarkly.com: Release Testing Explained 🌟](https://launchdarkly.com/blog/get-a-detailed-explanation-of-release-testing-several/) Release testing refers to coding practices and test strategies that give teams confidence that a software release candidate is ready for users. Release testing aims to find and eliminate errors and bugs from a software release so that it can be released to users. Let’s dive in and explore several methods used to perform release testing.

## Tools

- [Chainsaw - The ultimate end to end testing tool for Kubernetes operators](https://github.com/kyverno/chainsaw)
- [collabnix.com: The Ultimate Docker Tutorial for Automation Testing](https://collabnix.com/the-ultimate-docker-tutorial-for-automation-testing/)
- [Allure Report 🌟](https://github.com/allure-framework/allure2)
    - [Allure Jenkins Plugin 🌟](https://plugins.jenkins.io/allure-jenkins-plugin/) This plugin allows to automatically generate [Allure Report](http://allure.qatools.ru/) and attach it to build during Jenkins job run.
- [Semgrep](https://semgrep.dev/) Static analysis at ludicrous speed. Find bugs and enforce code standards
    - [meetup.com: A single open-source security scanner for most languages on Jenkins](https://www.meetup.com/es/Jenkins-online-meetup/events/276135789/) As software security is becoming an increasingly bigger organization risk, static and dynamic analysis are becoming indispensable. However most popular open-source static analysis scanners cover only a handful of languages, or offer limited security rules. In this talk, we’ll present Semgrep, an open-source static analysis tool that support 12+ languages, and simplifies writing custom rules for organization-specific code patterns. In addition, we’ll show how to integrate Semgrep into a Jenkins Pipeline for scanning every commit or PR.
- [testcontainers 🌟](https://github.com/testcontainers) Testcontainers is a Java library that supports JUnit tests, providing lightweight, throwaway instances of common databases, Selenium web browsers, or anything else that can run in a Docker container.
    - [testcontainers.org](https://www.testcontainers.org)
    - [thenewstack.io: Testcontainers Integration Library Gets Commercial Backing with AtomicJar](https://thenewstack.io/testcontainers-integration-library-gets-commercial-backing-with-atomicjar/)
    - [spinscale.de: Using Testcontainers To Test Elasticsearch Plugins](https://spinscale.de/posts/2021-08-25-using-testcontainers-to-test-elasticsearch-plugins.html)
    - [testcontainers-spring-boot 🌟](https://github.com/Playtika/testcontainers-spring-boot) Container auto-configurations for spring-boot based integration tests. If you use Testcontainers with Spring Boot you may be interested in the Playtika_Ltd Testcontainers library that provides auto-configurations for springboot based integration tests. It contains modules e.g. for kafka rabbitmq mongodb
    - [atomicjar.com: Announcing Testcontainers Cloud: Integration Testing has never been easier](https://www.atomicjar.com/2021/11/announcing-testcontainers-cloud/) Ever wished for integration tests to be faster, easier, and more efficient? Wish no more! We're happy to announce Testcontainers Cloud - a lightweight, fast, and secure integration testing platform for everyone.
    - [vladmihalcea.com: Testcontainers Database Integration Testing](https://vladmihalcea.com/testcontainers-database-integration-testing/)
    - [thenewstack.io: How Testcontainers Is Demonstrating Value as a Key CI Tool](https://thenewstack.io/how-testcontainers-is-demonstrating-value-as-a-key-ci-tool/) Testcontainers is a library originally written in Java that helps developers run module-specific Docker containers while the app is being built in order to simplify integration testing.
- [Metabob](https://www.metabob.com/) Metabob is an AI Static Analysis Tool that enables developers to quickly identify the causes behind errors and performance sinks. An AI-assisted tool to visualize and debug Python code.
- [SystemTap](https://sourceware.org/systemtap/)
- [auchenberg/volkswagen](https://github.com/auchenberg/volkswagen) Volkswagen detects when your tests are being run in a CI server, and makes them pass.
- [getxray.app: 7 benefits of using a Test Management App vs. Excel](https://www.getxray.app/blog/7-benefits-of-using-a-test-management-app-vs.-excel)
- [==google/clusterfuzzlite== 🌟](https://github.com/google/clusterfuzzlite) ClusterFuzzLite - Simple continuous [fuzzing](https://en.wikipedia.org/wiki/Fuzzing) that runs in CI.
    - [thenewstack.io: Google Introduces ClusterFuzzLite Security Tool for CI/CD](https://thenewstack.io/google-introduces-clusterfuzzlite-security-tool-for-ci-cd/)
- [==circleci.com: Unit testing vs integration testing== 🌟](https://circleci.com/blog/unit-testing-vs-integration-testing/)
- [==reviewdog - A code review dog who keeps your codebase healthy.==](https://github.com/reviewdog/reviewdog) 🐶 Automated code review tool integrated with any code analysis tools regardless of programming language

## Performance Testing


## Kubernetes conformance testing tools

- Mastercard, for example, checks every deployment with Kubernetes conformance testing tools such as sonobuoy and kubench.
- [sonobuoy](https://github.com/vmware-tanzu/sonobuoy) is a diagnostic tool that makes it easier to understand the state of a Kubernetes cluster by running a set of plugins (including Kubernetes conformance tests) in an accessible and non-destructive manner. It is a customizable, extendable, and cluster-agnostic way to generate clear, informative reports about your cluster.
- [kubench](https://github.com/vincentserpoul/kubench) Benchmark different containerized applications within a kubernetes cluster.

## Codeless Automation Testing


## Images

??? note "Click to expand!"

    <center>
    ![tests in prod](images/testinprodmeme.jfif)
    ![10 must haves test automation](images/10-must-haves-test-automation.jfif)
    </center>

## Tweets

<details>
  <summary>Click to expand!</summary>

<center>
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">If your code has no tests, then:<br><br>- it is not clean<br>- it is not complete<br>- it is not correct<br>- it is not documented<br>- it is not verified<br>- it is not working<br><br>And most importantly: It is not quality.</p>&mdash; Daniel Moka⚡ (@dmokafa) <a href="https://twitter.com/dmokafa/status/1365995255322001409?ref_src=twsrc%5Etfw">February 28, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">The term &quot;legacy&quot; is not about time or author. It is about quality.</p>&mdash; Mario Cervera (@macerub) <a href="https://twitter.com/macerub/status/1441072867974725636?ref_src=twsrc%5Etfw">September 23, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Code review does not work (and asynchronous code review is particularly bad). As Deming said: &quot;You can not inspect quality into a product.&quot; NO form of code _review_ yields quality. Collaborative programming that assures that the defects don’t exist to begin with does.</p>&mdash; Allen Holub (@allenholub) <a href="https://twitter.com/allenholub/status/1482564778149175298?ref_src=twsrc%5Etfw">January 16, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Why refactor your code and keep up with dependency deprecations when you can get a new job every 3 years to avoid your own technical debt?</p>&mdash; Carla Notarobot 🤖👩🏻‍💻 (@CarlaNotarobot) <a href="https://twitter.com/CarlaNotarobot/status/1482715184028397571?ref_src=twsrc%5Etfw">January 16, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Software engineering, a haiku:<br><br>fuck fuck fuck fuck fuck<br>fuck fuck fu-oh hey it works<br>wait, no - fuck fuck fuck</p>&mdash; Kelly Vaughn (@kvlly) <a href="https://twitter.com/kvlly/status/1538310552451264512?ref_src=twsrc%5Etfw">June 18, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</center>
</details>