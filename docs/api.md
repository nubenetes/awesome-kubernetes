# APIs with SOAP, REST and gRPC
- [APIs](#apis)
- [Python FastAPI](#python-fastapi)
- [Motivation](#motivation)
- [API Testing Interview Questions](#api-testing-interview-questions)
- [State of the API Report](#state-of-the-api-report)
	- [Postman State of the API Report](#postman-state-of-the-api-report)
	- [Smartbear State of the API Report](#smartbear-state-of-the-api-report)
- [Types of API Protocols. Interprocess Communication in Microservices](#types-of-api-protocols-interprocess-communication-in-microservices)
	- [SOAP API Protocol (Simple Object Access Protocol)](#soap-api-protocol-simple-object-access-protocol)
	- [REST API Protocol (Representational State Transfer)](#rest-api-protocol-representational-state-transfer)
		- [OpenAPI Specification (originally known as the Swagger Specification)](#openapi-specification-originally-known-as-the-swagger-specification)
	- [RPC API Protocol (Remote Procedure Call)](#rpc-api-protocol-remote-procedure-call)
		- [gRPC](#grpc)
	- [Asynchronous APIs](#asynchronous-apis)
		- [AsyncAPI](#asyncapi)
- [Comparisons](#comparisons)
	- [SOAP vs REST](#soap-vs-rest)
	- [REST vs OpenAPI vs gRPC](#rest-vs-openapi-vs-grpc)
	- [REST vs GraphQL vs gRPC](#rest-vs-graphql-vs-grpc)
- [Tools](#tools)
	- [API Testing](#api-testing)
	- [GraphQL](#graphql)
		- [Hasura](#hasura)
- [API Security](#api-security)
- [Free Web Services (Public APIs)](#free-web-services-public-apis)
- [Open Banking](#open-banking)
- [RPA](#rpa)
- [Related](#related)
- [Video APIs](#video-apis)
- [API Business Models](#api-business-models)
- [Images](#images)
- [Tweets](#tweets)

## APIs
- [wikipedia: API Application Programming Interface](https://simple.wikipedia.org/wiki/Application_programming_interface)
- [apifriends.com: What is an API?](https://apifriends.com/api-management/what-is-an-api/)
- [axway.com: What is API Management?](https://www.axway.com/en/products/api-management/what-is-api-management)
- [mulesoft.com: APIs versus web services](https://blogs.mulesoft.com/dev/api-dev/apis-versus-web-services/)
- [Youtube Playlist: Introduction to APIs](https://www.youtube.com/playlist?list=PLM-7VG-sgbtBBnWb2Jc5kufgtWYEmiMAw)
- [Devdocs.io API Documentation 🌟](https://devdocs.io/)
- [Dzone: 5 Tips for Better REST API Design](https://dzone.com/articles/my-5-tips-for-better-restapi-design) Good API design is difficult. Maintaining backwards compatibility, effectively testing, handling upgrades, etc. is hard to manage. Check out this guide for help!
- [thenewstack.io: 5 Ways to Succeed with an API Gateway](https://thenewstack.io/5-ways-to-succeed-with-an-api-gateway/)
- [redhat.com: An Architect's guide to APIs: SOAP, REST, GraphQL, and gRPC 🌟](https://www.redhat.com/architect/apis-soap-rest-graphql-grpc) There are many strategies for data exchange. Here's a primer on four essentials.
- [dev.to: Why RESTful API rules are not enough or good for you to design good apis?](https://dev.to/calidion/why-restful-api-rules-are-not-enough-or-good-for-you-to-design-good-apis-3530)
- [dzone: Why Is REST API Architecture Gaining Popularity in the Digital Industry? 🌟](https://dzone.com/articles/why-is-rest-api-architecture-gaining-popularity-in)
- [amazicworld.com: Why APIs can’t be missed when it comes to DevOps](https://amazicworld.com/why-apis-cant-be-missed-when-it-comes-to-devops/)
- [medium: API Gateway Part 1](https://medium.com/easyread/api-gateway-part-1-7901ba703f9) Understanding how API Gateway Works
	- [medium: API Gateway Part 2](https://medium.com/easyread/api-gateway-part-2-7264ee5be187) 
- [rapidapi.com: API vs Microservices [What’s the Difference?]](https://rapidapi.com/blog/api-vs-microservices-whats-the-differences/)
- [snipcart.com: API vs. Microservices: A Beginners Guide to Understand Them 🌟](https://snipcart.com/blog/api-vs-microservices-architecture)
- [youtube: Local CRUD API Express App with Docker in 5 min](https://www.youtube.com/watch?v=UxZiDZsQoZI&ab_channel=TinyStacks)
- [levelup.gitconnected.com: What’s Wrong With Your CRUD APIs— Besides Everything?](https://levelup.gitconnected.com/whats-wrong-with-your-crudy-interfaces-besides-everything-bde4f4c8cb8a)
- [freecodecamp.org: REST API Best Practices – REST Endpoint Design Examples 🌟](https://www.freecodecamp.org/news/rest-api-best-practices-rest-endpoint-design-examples/)
- [dzone: API Throttling Strategies When Clients Exceed Their Limit](https://dzone.com/articles/api-throttling-strategies) Here's how to handle clients exceeding API rate limits, as well as a few alternate strategies to explore and implement.
- [abdulrwahab.medium.com: API Architecture — Design Best Practices for REST APIs](https://abdulrwahab.medium.com/api-architecture-best-practices-for-designing-rest-apis-bf907025f5f)
- [blog.bitsrc.io: API vs Microservices — Are you using 2 terms for the same concept?](https://blog.bitsrc.io/api-vs-microservices-are-you-using-2-terms-for-the-same-concept-b51f13f5974e) No, you’re not, but let me explain

## Python FastAPI
- [writersbyte.com: Introduction to APIs with Python FastAPI](https://writersbyte.com/introduction-to-apis-with-python-fastapi/)

## Motivation
- [APIs published, APIs consumed: mainstream enterprises increasingly behave like software vendors](https://www.zdnet.com/article/apis-published-apis-consumed-mainstream-enterprises-increasingly-behave-like-software-vendors/) Mainstream enterprises increasingly reach out to customers with APIs, digital services. Unlike software providers though, many still have mostly on-premises infrastructure. 
- [You Bet That APIs Power DevOps Tools](http://seguridad-informacion.blogspot.com/2020/07/you-bet-that-apis-power-devops-tools.html)

## API Testing Interview Questions
- [automationreinvented.blogspot.com: Top 30 API Testing Interview Questions & Answers for SDET/API Automation-Rest Assured? SET-03](https://automationreinvented.blogspot.com/2020/11/top-30-api-testing-interview-questions.html)

## State of the API Report
### Postman State of the API Report
- [postman.com: 2019 Postman State of the API Report 🌟](https://www.postman.com/resources/infographics/api-survey-2019/)
- [blog.postman.com: You Can Now Capture Responses Using the Postman Proxy](https://blog.postman.com/capture-responses-using-the-postman-proxy/)

### Smartbear State of the API Report
- [smartbear.com: The State of API 2019 Report 🌟](https://smartbear.com/resources/ebooks/the-state-of-api-2019-report/)

## Types of API Protocols. Interprocess Communication in Microservices
- [apifriends.com: What are the different types of APIs? 🌟](https://apifriends.com/api-creation/different-types-apis/) Types of API Protocols: SOAP, REST and RPC
- [vishnuch.tech: Interprocess Communication in Microservices 🌟](https://vishnuch.tech/interprocess-communication-in-microservices) Different IPC methods in microservices like REST API, gRPC, Kafka, RabbitMQ, etc... which developers should know.

### SOAP API Protocol (Simple Object Access Protocol)
- [wikipedia: SOAP](https://en.wikipedia.org/wiki/SOAP)
- [geeksforgeeks.org: Basics of SOAP – Simple Object Access Protocol](https://www.geeksforgeeks.org/basics-of-soap-simple-object-access-protocol/)
- For information about the latest work on SOAP and a full list of SOAP specifications refer to the [W3C Technical Reports](https://www.w3.org/TR/)
- [guru99.com: SOAP Web Services Tutorial: Simple Object Access Protocol. What is SOAP?](https://www.guru99.com/soap-simple-object-access-protocol.html)
- [jitendrazaa.com: Create SOAP message using Java](http://www.jitendrazaa.com/blog/java/create-soap-message-using-java/)
- [dzone: Creating a SOAP Web Service With Spring Boot Starter Web Services](https://dzone.com/articles/creating-a-soap-web-service-with-spring-boot-start) In this post, we cover the concepts of SOAP and REST and show you all the code you need to use SOAP web services in a Spring Boot app.
  
### REST API Protocol (Representational State Transfer)
- [wikipedia: REST](https://en.wikipedia.org/wiki/Representational_state_transfer)
- [geeksforgeeks.org: REST API (Introduction)](https://www.geeksforgeeks.org/rest-api-introduction/)
- [geeksforgeeks.org: REST API Architectural Constraints](https://www.geeksforgeeks.org/rest-api-architectural-constraints/)
- [mulesoft.com: What is a RESTful API?](https://www.mulesoft.com/resources/api/restful-api)
- [Dzone refcard: Foundations of **RESTful Architecture** 🌟](https://dzone.com/refcardz/rest-foundations-restful)
- [Dzone: REST API tutorials](https://dzone.com/articles/rest-api-tutorials)
- [dev.to: Make your own API under 30 lines of code 🌟](https://dev.to/shreyazz/make-your-own-api-under-30-lines-of-code-4doh)
- [dzone: REST API Versioning Strategies](https://dzone.com/articles/rest-api-versioning-strategies-1) Today microservices are a hot trend for developing cloud-native applications. API versioning helps to iterate faster when the needed changes are identified.

#### OpenAPI Specification (originally known as the Swagger Specification)
- [OpenAPI](https://www.openapis.org/) evolved from the [Swagger](https://swagger.io/) project. Swagger started out as a specification for documenting RESTful APIs. Later on, tools to generate client and server code and generating of test cases were added. While the original Swagger Specification was donated to the Linux Foundation and renamed the OpenAPI, Swagger remains one of the most widely used open-source toolsets for developing OpenAPIs.
- [Wikipedia: OpenAPI Specification 🌟](https://en.wikipedia.org/wiki/OpenAPI_Specification)
- [OpenAPI FAQ. What is OpenAPI Specification (OAS)? OpenAPI Specification](https://www.openapis.org/faq) The OAS defines a standard, programming language-agnostic interface description for REST APIs, which allows both humans and computers to discover and understand the capabilities of a service without requiring access to source code, additional documentation, or inspection of network traffic.
- [apis.guru/openapi-directory: large archive of sample OpenAPI descriptions](https://apis.guru/openapi-directory/)

### RPC API Protocol (Remote Procedure Call)
- [wikipedia: RPC Remote Procedure Call](https://en.wikipedia.org/wiki/Remote_procedure_call)
- [open-rpc.org lightweight RPC framework 🌟](https://open-rpc.org/) It layers an interface description on top of JSON-RPC 2.0 and ships with a few tools to help you design, document, and test your APIs. 

#### gRPC
- [gRPC](https://grpc.io/)
- [wikipedia: gRPC](https://en.wikipedia.org/wiki/GRPC)
- [developers.googleblog.com: Introducing gRPC, a new open source HTTP/2 RPC Framework](https://developers.googleblog.com/2015/02/introducing-grpc-new-open-source-http2.html)
- [nordicapis.com: Using gRPC to Connect a Microservices Ecosystem](https://nordicapis.com/using-grpc-to-connect-a-microservices-ecosystem/)
- [cncf.io: Think gRPC, when you are architecting modern microservices!](https://www.cncf.io/blog/2021/07/19/think-grpc-when-you-are-architecting-modern-microservices/)
- [itnext.io: A minimalist guide to gRPC](https://itnext.io/a-minimalist-guide-to-grpc-e4d556293422) REST API is good but is it really the best option that we have?

### Asynchronous APIs 
#### AsyncAPI
- [AsyncAPI](https://www.asyncapi.com/) Building the future of event-driven architecture. Open source tools to easily build and maintain your event-driven architecture. All powered by the AsyncAPI specification, the industry standard for defining asynchronous APIs.
- [thenewstack.io: AsyncAPI Could Be the Default API Format for Event-Driven Architectures](https://thenewstack.io/asyncapi-could-be-the-default-api-format-for-event-driven-architectures/)

## Comparisons
- [blog.bitsrc.io: Not All Microservices Need to Be REST — 3 Alternatives to the Classic](https://blog.bitsrc.io/not-all-microservices-need-to-be-rest-3-alternatives-to-the-classic-41cedbf1a907)
- [levelup.gitconnected.com: Truth About { SOAP vs REST vs GRPC vs GraphQL } Checklist](https://levelup.gitconnected.com/truth-about-soap-vs-rest-vs-grpc-vs-graphql-checklist-f50bcb475adf)
- [medium: REST, RPC, GraphQL… What to choose?](https://medium.com/geekculture/rest-rpc-graphql-what-to-choose-c57c78c0593d) API protocols comparison from the practical straightpoint
### SOAP vs REST
- [geeksforgeeks.org: Difference between REST API and SOAP API](https://www.geeksforgeeks.org/difference-between-rest-api-and-soap-api/)
- [dzone: A Comprehensive Guide to REST vs. SOAP](https://dzone.com/articles/comprehensive-guide-rest-vs-soap) Learn the primary differences between REST and SOAP APIs, each one's benefits, and when it's appropriate to use the two.
- [dzone: Web Services Architecture – When to Use SOAP vs REST](https://dzone.com/articles/web-services-architecture) Learn why SOAP (Simple Object Access Protocol) and REST (Representation State Transfer) are popular with developers working on system integration projects.
- [dzone: Comparing RESTful APIs and SOAP APIs Using MuleSoft as an Example](https://dzone.com/articles/comparing-restful-apis-and-soap-apis) 
- [reply.com: Web Services: SOAP and REST - A Simple Introduction](https://www.reply.com/solidsoft-reply/en/content/webservices-soap-and-rest-a-simple-introduction) 
    - SOAP is a communications protocol while REST is a set of architectural principles for data transmission.
    - REST was designed to be a more straightforward and easy to implement alternative to heavyweight SOAP for web service access. SOAP functions well in distributed environments where REST assumes a direct point to point communication. Also, SOAP allows for services to describe themselves to clients and in some languages allows for automation. On the other hand, REST is fast as less processing is required, uses less bandwidth and is closer to technologies used in web design. 
    - The choice on which to use is totally dependent on what the requirement. For example, SOAP is a better choice for applications that have complex API so as to describe the services and methods, where formal contracts are agreed for the exchange format, where a guaranteed level of security is required etc. REST will be preferred when limiting bandwidth and resources, when operations are can be stateless and the information can be cached.
- [baeldung.com: REST vs SOAP](https://www.baeldung.com/cs/rest-vs-soap)

### REST vs OpenAPI vs gRPC
- [REST vs. gRPC: Battle of the APIs](https://code.tutsplus.com/tutorials/rest-vs-grpc-battle-of-the-apis--cms-30711)
- [Comparing OpenAPI With gRPC 🌟](https://dzone.com/articles/comparing-openapi-with-grpc) OpenAPI is a great choice due to its interoperability. On the other hand, gRPC offers a better performance. Luckily, you don't have to choose one or the other.
- [imaginarycloud.com: gRPC vs REST: Comparing APIs Architectural Styles](https://www.imaginarycloud.com/blog/grpc-vs-rest/)
### REST vs GraphQL vs gRPC
- [danhacks.com: REST vs. GraphQL vs. gRPC](https://www.danhacks.com/software/grpc-rest-graphql.html)

## Tools
### API Testing
* [softwaretestingportal.com: API Testing, Key Terminologies and more...](http://www.softwaretestingportal.com/2020/03/31/api-testing/)
* [dzone.com: 10 API Testing Tips for Beginners (SOAP and REST)](https://dzone.com/articles/10-api-testing-tips-for-beginners-soap-amp-rest) Let's take a look at ten API testing tips for beginners with a focus on REST APIs and SOAP APIs. 
* [blog.testproject.io: Top 10 API Testing Tools to Watch in 2020 🌟](https://blog.testproject.io/2020/06/25/top-10-api-testing-tools-to-watch-in-2020/)
* [mockoon 🌟](https://mockoon.com/) Create mock APIs in seconds. Mockoon is the easiest and quickest way to run mock API locally. No remote deployment, no account required, open source.
* [thenewstack.io: 4 Essential Tools for Protecting APIs and Web Applications](https://thenewstack.io/4-essential-tools-for-protecting-apis-and-web-applications/)
* [youtube: API Testing Part 1- API Core Concepts](https://www.youtube.com/watch?v=b0D_bkcT4a4&t=1s&ab_channel=SoftwareDiagnosticsCenter)
* [blog.testproject.io: API Testing 101 🌟](https://blog.testproject.io/2021/06/16/api-testing-101/)
* [microcks.io 🌟](https://microcks.io/) Open source Kubernetes Native tool for API Mocking and Testing. If you are looking for a tool that helps in microservices API testing on Kubernetes it is worth taking a look at microcksio. It supports OpenAPI 3 and e.g. Kafka with [Avro encoding](https://microcks.io/documentation/guides/avro-messaging/)
* [tricentis.com: Getting started with automated continuous performance testing](https://www.tricentis.com/blog/automated-continuous-performance-testing)
* [dev.to: Top 15 Automated API Testing Tools](https://dev.to/katalon/top-15-automated-api-testing-tools-lasted-update-32ip)
* [opensource.com: 3 ways to test your API with Python](https://opensource.com/article/21/9/unit-test-python) Unit testing can be daunting, but these Python modules will make your life much easier.

### GraphQL
- [GraphQL](https://graphql.org/) A query language for your API
- [How is the OpenAPI Specification different from GraphQL?](https://www.openapis.org/faq) How are screws better than nails? Both are useful tools that solve similar problems in slightly different ways. OpenAPI Specification offers a declarative contract that defines the structure of API requests and responses as discrete operations. GraphQL prefers an interface style that is more like querying a database and is best suited to graph databases. 
- [Hasura Launches Beta of GraphQL-Based Remote Joins Tool](https://devops.com/hansura-launches-beta-of-graphql-based-remote-joins-tool/)
- [thenewstack.io: Why Backend Developers Should Fall in Love with GraphQL too](https://thenewstack.io/why-backend-developers-should-fall-in-love-with-graphql-too/)
- [blog.dream11engineering.com: Lessons learned from running GraphQL at scale](https://blog.dream11engineering.com/lessons-learned-from-running-graphql-at-scale-2ad60b3cefeb)
- [world.hey.com: Another REST vs GraphQL comparison](https://world.hey.com/sammy.henningsson/another-rest-vs-graphql-comparison-8e8357bb)
- [dzone: A Schema Architecture for Microservices](https://dzone.com/articles/a-schema-architecture-for-microservices)

#### Hasura
- [Hasura 🌟](https://hasura.io/) Instant realtime GraphQL APIs for all your data
	- Build modern apps and APIs 10x faster
	- TickInstant GraphQL & REST APIs
	- TickBuilt in authorization for secure data access
	- TickOpen source

## API Security
- [devops.com: Web Application Security is not API Security 🌟](https://devops.com/web-application-security-is-not-api-security/)
- [biztechmagazine.com: 6 Steps to Improved API Security](https://biztechmagazine.com/article/2021/07/6-steps-improved-api-security) Application programming interfaces are critical to businesses. Tech leaders must do more to protect them.
- [portswigger.net: Introducing vAPI – an open source lab environment to learn about API security](https://portswigger.net/daily-swig/introducing-vapi-an-open-source-lab-environment-to-learn-about-api-security)

## Free Web Services (Public APIs)
- [free-web-services.com](http://free-web-services.com/)
- [SwaggerHub: Free Web Service](https://swagger.io/tools/swaggerhub/)
- [programmableweb.com](https://www.programmableweb.com/)
- [any-api.com](https://any-api.com/)
- [Rapid API](https://rapidapi.com/)

## Open Banking
- [Open Banking](https://en.wikipedia.org/wiki/Open_banking)
- [thenewstack.io: A Digital Transformation Journey in the Banking Sector](https://thenewstack.io/a-digital-transformation-journey-in-the-banking-sector/)

## RPA
- [thenewstack.io: True Success in Process Automation Requires Microservices](https://thenewstack.io/true-success-in-process-automation-requires-microservices/)

## Related
- [medium: Do I Need an API Gateway if I Use a Service Mesh? 🌟](https://blog.christianposta.com/microservices/do-i-need-an-api-gateway-if-i-have-a-service-mesh/)
* [Dzone: How to Create a REST API With Spring Boot](https://dzone.com/articles/how-to-create-rest-api-with-spring-boot)
* [Dzone: Step-By-Step Spring Boot RESTful Web Service Complete Example](https://dzone.com/articles/spring-boot-restful-web-service-complete-example)
* [Creando un API REST en Java (parte 1)](https://www.oscarblancarteblog.com/2018/06/25/creando-un-api-rest-en-java-parte-1/)
* [dev.to: Rapid API Creation with AWS Amplify](https://dev.to/fllstck/rapid-api-creation-with-aws-amplify-3c8i)
* [portal.dev](https://portal.dev/) Build beautiful API documentation. Portal lets you create, publish, and maintain your API docs with ease.
* [openapi-comment-parser](https://github.com/bee-travels/openapi-comment-parser) A clean and simple way to document your code for generating OpenAPI (Swagger) specs.
    * [IBM creates an open source tool to simplify API documentation](https://www.techrepublic.com/article/ibm-creates-an-open-source-tool-to-simplify-api-documentation/)

## Video APIs
* [Mux: The API to Video](https://mux.com/)
	* [softwareengineeringdaily.com: Kubernetes vs. Serverless with Matt Ward (podcast) 🌟](https://softwareengineeringdaily.com/2020/12/29/kubernetes-vs-serverless-with-matt-ward-repeat/)

## API Business Models
- [API Business Models. 20 Models in 20 Minutes](https://www.infoq.com/presentations/API-Business-Models/)

## Images
??? note "Click to expand!"

	<center>
	[![top 10 api testing tools](images/summarising_top_10_api_testing_tools.png){: style="width:50%"}](https://blog.testproject.io/2020/06/25/top-10-api-testing-tools-to-watch-in-2020/)

	[![20 API Business Models](images/api_business_models.jpg)](https://www.infoq.com/presentations/API-Business-Models/)
	</center>

## Tweets
<details>
  <summary>Click to expand!</summary>

<center>
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">People complain about tooling fatigue but web dev in 2021 is 10x simpler than in 2011. You just gotta pick the right tools.<br><br>Infra: <a href="https://twitter.com/PulumiCorp?ref_src=twsrc%5Etfw">@PulumiCorp</a> <br>Data: <a href="https://twitter.com/PostgreSQL?ref_src=twsrc%5Etfw">@PostgreSQL</a> <br>API: <a href="https://twitter.com/HasuraHQ?ref_src=twsrc%5Etfw">@HasuraHQ</a> <br>Frontend: <a href="https://twitter.com/vercel?ref_src=twsrc%5Etfw">@vercel</a>&#39;s NextJS<br><br>And no proprietary bullshit—100% open source!</p>&mdash; gunar.uk (@gunar) <a href="https://twitter.com/gunar/status/1395744592071323651?ref_src=twsrc%5Etfw">May 21, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</center>
</details>