# QA: Software Quality Test Automation
- [Introduction](#introduction)
- [Testing Frameworks](#testing-frameworks)
- [Release Testing](#release-testing)
- [Tools](#tools)
- [Performance Testing](#performance-testing)
- [Kubernetes conformance testing tools](#kubernetes-conformance-testing-tools)
- [Codeless Automation Testing](#codeless-automation-testing)
- [Images](#images)
- [Tweets](#tweets)

## Introduction
* [Awesome Test Automation](https://github.com/atinfo/awesome-test-automation)
* [Awesome Software Quality](https://github.com/ligurio/awesome-software-quality)
* [softwaretestguideforu.com: What is system testing? How to perform system testing?](https://www.softwaretestguideforu.com/2020/06/what-is-system-testinghow-to-perform.html)
* [linkedin.com/pulse: Importance of API Automation Testing 🌟](https://www.linkedin.com/pulse/importance-api-automation-testing-manish-saini/)
* [automationreinvented.blogspot.com: Top 40 API Automation testing interview question for SDET and Automation QA ?](https://automationreinvented.blogspot.com/2021/03/top-40-api-testing-interview-question.html)
* [thenewstack.io: Optimizing App Performance in a Multicloud Stack](https://thenewstack.io/optimizing-app-performance-in-a-multicloud-stack/)
* [botplayautomation.com: Automation Testing Implementation Guide](https://www.botplayautomation.com/post/what-is-automation-testing-the-need-for-automation-testing-automation-testing-implementation-guide)
* [botplayautomation.com: Types of Software Testing](https://www.botplayautomation.com/post/types-of-software-testing)
* [botplayautomation.com: Automation & Manual Testing Best Practices](https://www.botplayautomation.com/post/best-practices-to-follow-in-software-testing-manual-and-automation-testing)
* [botplayautomation.com: How to write a Software Test Plan?](https://www.botplayautomation.com/post/how-to-write-a-test-plan)
* [blog.thundra.io: 4 Software Testing Roles](https://blog.thundra.io/4-software-testing-roles)
* [lambdatest.com: TestNG vs JUnit : Which testing framework should you choose?](https://www.lambdatest.com/blog/testng-vs-junit-which-testing-framework-should-you-choose/)
* [botplayautomation.com: Common mistakes test teams make in automation testing and how to fix them](https://www.botplayautomation.com/post/common-mistakes-test-teams-make-in-automation-testing-and-how-to-fix-them)
* [blog.testproject.io: A Complete Guide to Test Automation Framework 🌟](https://blog.testproject.io/2021/06/17/a-complete-guide-to-test-automation-framework/) 
    * [Test Automation Framework: TestProject](https://testproject.io/) TestProject is a free end-to-end test automation platform for web, mobile, and API testing that’s supported by
the #1 test automation community.
* [botplayautomation.com: Automation Test Plan](https://www.botplayautomation.com/post/automation-test-plan)
* [devops.com: Continuous Testing Practices (Part 1) 🌟](https://devops.com/continuous-testing-practices-part-1/)
    * [devops.com: Continuous Testing Practices – Part 2 🌟](https://devops.com/continuous-testing-practices-part-2/)
* [boozangfromthetrenches.com: Root Cause Analysis in Test Automation](https://boozangfromthetrenches.com/root-cause-analysis-in-test-automation/9)
* [copyconstruct.medium.com: Testing in Production, the safe way 🌟🌟🌟](https://copyconstruct.medium.com/testing-in-production-the-safe-way-18ca102d0ef1)
* [blog.thundra.io: How to Fix Your Failing End-to-End Tests?](https://blog.thundra.io/how-to-fix-your-failing-end-to-end-tests)
* [rookout.com: How Real-Time Debugging Improves Reliability](https://www.rookout.com/blog/how-real-time-debugging-improves-reliability)
* [itnext.io: Software Development Is Misunderstood 🌟](https://itnext.io/software-development-is-misunderstood-quality-is-fastest-way-to-get-code-into-production-f1f5a0792c69) Quality is fastest way to get code into production. **Non-developers focus on creating code, developers focus on creating maintainable code**
* [blog.testproject.io: The 10–10–10 Rule of Test Automation](https://blog.testproject.io/2021/07/21/the-10-10-10-rule-of-test-automation/)
* [blog.testproject.io: End to End Testing](https://blog.testproject.io/2021/07/22/end-to-end-testing/)
* [blog.testproject.io: REST API Automation From Scratch 🌟](https://blog.testproject.io/2021/07/28/rest-api-automation-from-scratch/)
* [dzone: Checklist for API Verification 🌟](https://dzone.com/articles/checklist-for-api-verification) These days where Applications talk to each other using API, the verification of any message between the applications/microservices needs to be verified. This checklist includes some best practices for API verification.
* [thenewstack.io: 7 Benefits of Testing in Isolation](https://thenewstack.io/7-benefits-of-testing-in-isolation/)
* [dzone: A Detailed Comparison: Unit Testing vs. Functional Testing](https://dzone.com/articles/detailed-comparison-unit-testing-vs-functional-testing) The main goal of any testing is to deliver a quality product with find the right job balance between unit testing and functional testing.
* [dzone: Microservice Testing Strategies](https://dzone.com/articles/microservice-testing-strategies) This article contains Microservice testing strategies. Learn more about testing in layered architectures.
* [dzone: We Are Testing Software Incorrectly and It's Costly](https://dzone.com/articles/we-are-testing-software-incorrectly-and-its-costly) We should write tests to enable developers to move fast with confidence. Code is always evolving, so question everything, collect experience, and judge for yourself.
* [thenewstack.io: Error Handling from Backends to the Frontend](https://thenewstack.io/error-handling-from-backends-to-the-frontend/)
* [==lambdatest.com: Top Automation Testing Trends To Look Out In 2021==](https://www.lambdatest.com/blog/top-automation-testing-trends-2021)
* [==betterprogramming.pub: Why We Quit Unit Testing Classes to Focus On a Behavioral Approach==](https://betterprogramming.pub/quit-unit-testing-classes-and-use-a-behavior-oriented-approach-306a667f9a31) Why you should consider avoiding class-level tests, in favor of a behavior-oriented approach

## Testing Frameworks
* [JUnit](https://junit.org)
    * [lambdatest.com](https://www.lambdatest.com/blog/junit5-extensions/) A Comprehensive Guide On JUnit 5 Extensions 
* [TestNG](https://testng.org)
* [Spock Framework](https://spockframework.org)
* [testsvision.com: 6 Popular Automation Testing Frameworks & Tools](https://testsvision.com/6-popular-automation-testing-frameworks-tools/)

## Release Testing
- [launchdarkly.com: Release Testing Explained 🌟](https://launchdarkly.com/blog/get-a-detailed-explanation-of-release-testing-several/) Release testing refers to coding practices and test strategies that give teams confidence that a software release candidate is ready for users. Release testing aims to find and eliminate errors and bugs from a software release so that it can be released to users. Let’s dive in and explore several methods used to perform release testing.

## Tools
* [collabnix.com: The Ultimate Docker Tutorial for Automation Testing](https://collabnix.com/the-ultimate-docker-tutorial-for-automation-testing/)
    * [TestProject](https://testproject.io/) Free Test Automation for All.
* [Allure Report 🌟](https://github.com/allure-framework/allure2)
    * [Allure Jenkins Plugin 🌟](https://plugins.jenkins.io/allure-jenkins-plugin/) This plugin allows to automatically generate [Allure Report](http://allure.qatools.ru/) and attach it to build during Jenkins job run.
* [venturebeat.com: Reflect brings automated no-code web testing to the cloud](https://venturebeat.com/2021/01/22/reflect-brings-automated-no-code-web-testing-to-the-cloud/)
* [Semgrep](https://semgrep.dev/) Static analysis at ludicrous speed. Find bugs and enforce code standards
    * [meetup.com: A single open-source security scanner for most languages on Jenkins](https://www.meetup.com/es/Jenkins-online-meetup/events/276135789/) As software security is becoming an increasingly bigger organization risk, static and dynamic analysis are becoming indispensable. However most popular open-source static analysis scanners cover only a handful of languages, or offer limited security rules. In this talk, we’ll present Semgrep, an open-source static analysis tool that support 12+ languages, and simplifies writing custom rules for organization-specific code patterns. In addition, we’ll show how to integrate Semgrep into a Jenkins Pipeline for scanning every commit or PR.
* [testcontainers 🌟](https://github.com/testcontainers) Testcontainers is a Java library that supports JUnit tests, providing lightweight, throwaway instances of common databases, Selenium web browsers, or anything else that can run in a Docker container.
    * [testcontainers.org](https://www.testcontainers.org)
    * [thenewstack.io: Testcontainers Integration Library Gets Commercial Backing with AtomicJar](https://thenewstack.io/testcontainers-integration-library-gets-commercial-backing-with-atomicjar/)
    * [spinscale.de: Using Testcontainers To Test Elasticsearch Plugins](https://spinscale.de/posts/2021-08-25-using-testcontainers-to-test-elasticsearch-plugins.html)
    * [testcontainers-spring-boot 🌟](https://github.com/Playtika/testcontainers-spring-boot) Container auto-configurations for spring-boot based integration tests. If you use Testcontainers with Spring Boot you may be interested in the Playtika_Ltd Testcontainers library that provides auto-configurations for springboot based integration tests. It contains modules e.g. for kafka rabbitmq mongodb
    * [atomicjar.com: Announcing Testcontainers Cloud: Integration Testing has never been easier](https://www.atomicjar.com/2021/11/announcing-testcontainers-cloud/) Ever wished for integration tests to be faster, easier, and more efficient? Wish no more! We're happy to announce Testcontainers Cloud - a lightweight, fast, and secure integration testing platform for everyone.
* [Metabob](https://www.metabob.com/) Metabob is an AI Static Analysis Tool that enables developers to quickly identify the causes behind errors and performance sinks. An AI-assisted tool to visualize and debug Python code.
* [dzone: Top Microservices Testing Tools Testers Should Know About](https://dzone.com/articles/top-microservices-testing-tools-testers-should-kno)
* [SystemTap](https://sourceware.org/systemtap/)
    * [developers.redhat.com: Opening black boxes with statement tracing (SystemTap)](https://developers.redhat.com/articles/2021/08/04/opening-black-boxes-statement-tracing)
* [auchenberg/volkswagen](https://github.com/auchenberg/volkswagen) Volkswagen detects when your tests are being run in a CI server, and makes them pass.
* [getxray.app: 7 benefits of using a Test Management App vs. Excel](https://www.getxray.app/blog/7-benefits-of-using-a-test-management-app-vs.-excel)
* [==google/clusterfuzzlite== 🌟](https://github.com/google/clusterfuzzlite) ClusterFuzzLite - Simple continuous [fuzzing](https://en.wikipedia.org/wiki/Fuzzing) that runs in CI.
    * [thenewstack.io: Google Introduces ClusterFuzzLite Security Tool for CI/CD](https://thenewstack.io/google-introduces-clusterfuzzlite-security-tool-for-ci-cd/)
* [convert.com: Top 10 A/B Testing Tools That Are Good for the Next 5 Years (Vetted by Features, Privacy, Maturity & Price)](https://www.convert.com/blog/a-b-testing/a-b-testing-tools-2022-beyond/)
* [==K6 Cloud==](https://k6.io/cloud/) Managed performance testing for engineering teams
    * [grafana.com: How to build performance tests into your CI pipeline with k6, GitHub Actions, and Grafana](https://grafana.com/blog/2021/11/29/how-to-build-performance-tests-into-your-ci-pipeline-with-k6-github-actions-and-grafana/)
* [==circleci.com: Unit testing vs integration testing== 🌟](https://circleci.com/blog/unit-testing-vs-integration-testing/)

## Performance Testing
- [devops.com: Best Practices for Application Performance Testing](https://devops.com/best-practices-for-application-performance-testing/)

## Kubernetes conformance testing tools
- Mastercard, for example, checks every deployment with Kubernetes conformance testing tools such as sonobuoy and kubench.
- [sonobuoy](https://github.com/vmware-tanzu/sonobuoy) is a diagnostic tool that makes it easier to understand the state of a Kubernetes cluster by running a set of plugins (including Kubernetes conformance tests) in an accessible and non-destructive manner. It is a customizable, extendable, and cluster-agnostic way to generate clear, informative reports about your cluster.
- [kubench](https://github.com/vincentserpoul/kubench) Benchmark different containerized applications within a kubernetes cluster.

## Codeless Automation Testing
- [botplayautomation.com](https://www.botplayautomation.com/)
- [botplayautomation.com: Benefits of Codeless (no code) Automation Testing](https://www.botplayautomation.com/post/benefits-of-codeless-automation-testing)

## Images
??? note "Click to expand!"

    <center>
    ![tests in prod](images/testinprodmeme.jfif)
    </center>

## Tweets
<details>
  <summary>Click to expand!</summary>

<center>
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">If your code has no tests, then:<br><br>- it is not clean<br>- it is not complete<br>- it is not correct<br>- it is not documented<br>- it is not verified<br>- it is not working<br><br>And most importantly: It is not quality.</p>&mdash; Daniel Moka⚡ (@dmokafa) <a href="https://twitter.com/dmokafa/status/1365995255322001409?ref_src=twsrc%5Etfw">February 28, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">The term &quot;legacy&quot; is not about time or author. It is about quality.</p>&mdash; Mario Cervera (@macerub) <a href="https://twitter.com/macerub/status/1441072867974725636?ref_src=twsrc%5Etfw">September 23, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</center>
</details>