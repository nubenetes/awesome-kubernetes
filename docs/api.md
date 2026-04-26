# APIs with SOAP, REST and gRPC

1. [APIs](#apis)
2. [From RESTful to Event-Driven APIs](#from-restful-to-event-driven-apis)
3. [API Gateway vs. Load Balancer: What's The Difference?](#api-gateway-vs-load-balancer-whats-the-difference)
4. [Python FastAPI](#python-fastapi)
5. [Python REST APIs with flask](#python-rest-apis-with-flask)
6. [Motivation](#motivation)
7. [State of the API Report](#state-of-the-api-report)
    1. [Postman State of the API Report](#postman-state-of-the-api-report)
    2. [Smartbear State of the API Report](#smartbear-state-of-the-api-report)
8. [Types of API Protocols. Interprocess Communication in Microservices](#types-of-api-protocols-interprocess-communication-in-microservices)
    1. [SOAP API Protocol (Simple Object Access Protocol)](#soap-api-protocol-simple-object-access-protocol)
    2. [REST API Protocol (Representational State Transfer)](#rest-api-protocol-representational-state-transfer)
        1. [OpenAPI Specification (originally known as the Swagger Specification)](#openapi-specification-originally-known-as-the-swagger-specification)
    3. [RPC API Protocol (Remote Procedure Call)](#rpc-api-protocol-remote-procedure-call)
        1. [gRPC](#grpc)
    4. [Asynchronous APIs](#asynchronous-apis)
        1. [WebSockets](#websockets)
        2. [Socket.io](#socketio)
        3. [AsyncAPI](#asyncapi)
9. [Comparisons](#comparisons)
    1. [SOAP vs REST](#soap-vs-rest)
    2. [REST vs OpenAPI vs gRPC](#rest-vs-openapi-vs-grpc)
    3. [REST vs GraphQL vs gRPC](#rest-vs-graphql-vs-grpc)
10. [Tools](#tools)
     1. [API Testing](#api-testing)
     2. [GraphQL](#graphql)
         1. [Hasura](#hasura)
11. [Browser APIs](#browser-apis)
12. [API Security](#api-security)
13. [Free Web Services (Public APIs)](#free-web-services-public-apis)
14. [Open Banking](#open-banking)
15. [RPA](#rpa)
16. [API Ops](#api-ops)
17. [Related](#related)
18. [Video APIs](#video-apis)
19. [API Business Models](#api-business-models)
20. [Videos](#videos)
21. [Images](#images)
22. [Tweets](#tweets)

## APIs

- [postman.com: What is an API?](https://www.postman.com/what-is-an-api)
- [==github.com/public-apis/public-apis: Try Public APIs for free== 🌟](https://github.com/public-apis/public-apis) **A collective list of free APIs. Explore popular APIs and see them work in Postman.**
- [mulesoft.com: APIs versus web services](https://blogs.mulesoft.com/dev/api-dev/apis-versus-web-services/)
- [Youtube Playlist: Introduction to APIs](https://www.youtube.com/playlist?list=PLM-7VG-sgbtBBnWb2Jc5kufgtWYEmiMAw)
- [==Devdocs.io API Documentation== 🌟](https://devdocs.io/)
- [thenewstack.io: 5 Ways to Succeed with an API Gateway](https://thenewstack.io/5-ways-to-succeed-with-an-api-gateway/)
- [redhat.com: An Architect's guide to APIs: SOAP, REST, GraphQL, and gRPC 🌟](https://www.redhat.com/architect/apis-soap-rest-graphql-grpc) There are many strategies for data exchange. Here's a primer on four essentials.
- [rapidapi.com: API vs Microservices [What’s the Difference?]](https://rapidapi.com/blog/api-vs-microservices-whats-the-differences/)
- [snipcart.com: API vs. Microservices: A Beginners Guide to Understand Them 🌟](https://snipcart.com/blog/api-vs-microservices-architecture)
- [youtube: Local CRUD API Express App with Docker in 5 min](https://www.youtube.com/watch?v=UxZiDZsQoZI&ab_channel=TinyStacks)
- [freecodecamp.org: REST API Best Practices – REST Endpoint Design Examples 🌟](https://www.freecodecamp.org/news/rest-api-best-practices-rest-endpoint-design-examples/)
- [troyhunt.com: Your API versioning is wrong, which is why I decided to do it 3 different wrong ways](https://www.troyhunt.com/your-api-versioning-is-wrong-which-is/)
- [infoq.com: A Standardized, Specification-Driven API Lifecycle](https://www.infoq.com/articles/Standardized-Specification-Driven-API-Lifecycle/)
- [genbeta.com: Hace 20 años, este correo de Jeff Bezos en Amazon cambió para siempre la forma en que programamos apps](https://www.genbeta.com/desarrollo/hace-20-anos-este-correo-jeff-bezos-amazon-cambio-para-siempre-forma-que-programamos-apps) Un aspecto fundamental del valor de una API reside en su 'efecto red': siendo un conjunto de 'bloques de construcción digitales', cuanto mayor sea el número de funcionalidades que proporcione más cosas valiosas permitirá crear. El texto completo de la ya conocida como 'API Mandate' ('Orden API') es el siguiente:
    - Todos los equipos expondrán a partir de ahora sus datos y funcionalidad a través de interfaces de servicio.
    - Los equipos deben comunicarse entre sí a través de estas interfaces.
    - No se permitirá ninguna otra forma de comunicación entre procesos: nada de vinculación directa, ni lecturas directas del depósito de datos de otro equipo, ni modelo de memoria compartida, ni ninguna clase de puertas traseras: la única comunicación permitida será mediante llamadas a la interfaz de servicio a través de la red.
    - No importa qué tecnología utilicéis: HTTP, Corba, Pubsub, protocolos personalizados? da igual.
    - Todas las interfaces de servicio, sin excepción, deberán diseñarse desde cero para que sean externalizables. Es decir, el equipo debe planificar y diseñar para poder exponer la interfaz a los desarrolladores en el mundo exterior. Sin excepciones.
    - Cualquiera que no haga esto será despedido.
- [thenewstack.io: How to Achieve API Governance](https://thenewstack.io/how-to-achieve-api-governance/) With APIs popping up everywhere, API strategy demands common design patterns, central discoverability, and putting users first.
- [freecodecamp.org: REST API Design Best Practices Handbook – How to Build a REST API with JavaScript, Node.js, and Express.js](https://www.freecodecamp.org/news/rest-api-design-best-practices-build-a-rest-api/) When you're working with APIs, there are some basic best practices you should follow. And if you really want to learn how they work, build one yourself. In this guide Jean-Marc goes over each best practice as you build a REST API w/ JS, Node, & Express.
- [infoq.com: Modern API Development and Deployment, from API Gateways to Sidecars](https://www.infoq.com/presentations/api-design-implement-document/)
- [==freecodecamp.org: Public APIs Developers Can Use in Their Projects==](https://www.freecodecamp.org/news/public-apis-for-developers/)
- [postman.com: API versioning](https://www.postman.com/api-platform/api-versioning/) Learn how API versioning enables teams to make changes to their API without creating problems for consumers.

## From RESTful to Event-Driven APIs

- [foojay.io: The Evolution of APIs: From RESTful to Event-Driven](https://foojay.io/today/the-evolution-of-apis-from-restful-to-event-driven/)

## API Gateway vs. Load Balancer: What's The Difference?

- [blog.hubspot.com: API Gateway vs. Load Balancer: What's The Difference?](https://blog.hubspot.com/website/api-gateway-vs-load-balancer#:~:text=An%20API%20gateway%20vs.,network%20traffic%20across%20multiple%20servers) An API gateway vs. load balancer comparison can be boiled down to the fact that they both manage traffic entering your website or application but have different roles. An API gateway handles authentication and security policies, while a load balancer API distributes network traffic across multiple servers.

## Python FastAPI


## Python REST APIs with flask


## Motivation

- [APIs published, APIs consumed: mainstream enterprises increasingly behave like software vendors](https://www.zdnet.com/article/apis-published-apis-consumed-mainstream-enterprises-increasingly-behave-like-software-vendors/) Mainstream enterprises increasingly reach out to customers with APIs, digital services. Unlike software providers though, many still have mostly on-premises infrastructure.
- [You Bet That APIs Power DevOps Tools](http://seguridad-informacion.blogspot.com/2020/07/you-bet-that-apis-power-devops-tools.html)

## State of the API Report

### Postman State of the API Report

- [postman.com: 2019 Postman State of the API Report 🌟](https://www.postman.com/resources/infographics/api-survey-2019/)

### Smartbear State of the API Report

- [smartbear.com: The State of API 2019 Report 🌟](https://smartbear.com/resources/ebooks/the-state-of-api-2019-report/)

## Types of API Protocols. Interprocess Communication in Microservices

- [vishnuch.tech: Interprocess Communication in Microservices 🌟](https://vishnuch.tech/interprocess-communication-in-microservices) Different IPC methods in microservices like REST API, gRPC, Kafka, RabbitMQ, etc... which developers should know.

### SOAP API Protocol (Simple Object Access Protocol)

- [geeksforgeeks.org: Basics of SOAP – Simple Object Access Protocol](https://www.geeksforgeeks.org/basics-of-soap-simple-object-access-protocol/)
- For information about the latest work on SOAP and a full list of SOAP specifications refer to the [W3C Technical Reports](https://www.w3.org/TR/)
- [guru99.com: SOAP Web Services Tutorial: Simple Object Access Protocol. What is SOAP?](https://www.guru99.com/soap-simple-object-access-protocol.html)
- [jitendrazaa.com: Create SOAP message using Java](http://www.jitendrazaa.com/blog/java/create-soap-message-using-java/)

### REST API Protocol (Representational State Transfer)

- [geeksforgeeks.org: REST API (Introduction)](https://www.geeksforgeeks.org/rest-api-introduction/)
- [geeksforgeeks.org: REST API Architectural Constraints](https://www.geeksforgeeks.org/rest-api-architectural-constraints/)
- [mulesoft.com: What is a RESTful API?](https://www.mulesoft.com/resources/api/restful-api)
- [dev.to: Make your own API under 30 lines of code 🌟](https://dev.to/shreyazz/make-your-own-api-under-30-lines-of-code-4doh)
- [freecodecamp.org: What is REST? Rest API Definition for Beginners](https://www.freecodecamp.org/news/what-is-rest-rest-api-definition-for-beginners/)
- [==javarevisited.blogspot.com: How to send POST Request with JSON Payload using Curl Command in Linux to Test RESTful Web Services?==](https://javarevisited.blogspot.com/2022/08/how-to-post-json-data-with-curl-command.html)
- [blog.bytebytego.com: EP94: REST API Cheatsheet](https://blog.bytebytego.com/p/ep94-rest-api-cheatsheet)
- [==freecodecamp.org: The REST API Handbook – How to Build, Test, Consume, and Document REST APIs==](https://www.freecodecamp.org/news/build-consume-and-document-a-rest-api/)

#### OpenAPI Specification (originally known as the Swagger Specification)


### RPC API Protocol (Remote Procedure Call)

- [open-rpc.org lightweight RPC framework 🌟](https://open-rpc.org/) It layers an interface description on top of JSON-RPC 2.0 and ships with a few tools to help you design, document, and test your APIs.

#### gRPC

- [gRPC](https://grpc.io/)
- [developers.googleblog.com: Introducing gRPC, a new open source HTTP/2 RPC Framework](https://developers.googleblog.com/2015/02/introducing-grpc-new-open-source-http2.html)
- [blog.getambassador.io: Implementing gRPC-Web with Emissary-ingress](https://blog.getambassador.io/implementing-grpc-web-with-emissary-ingress-22aa0d86aac) In this article, you'll learn how to implement gRPC-Web (a JavaScript implementation of gRPC for browser clients) with Emissary-ingress — an Envoy-based API gateway and Ingress controller

### Asynchronous APIs

#### WebSockets

- [The State of Real-Time Web in 2016](https://banksco.de/p/state-of-realtime-web-2016.html)
- [spring.io: YMNNALFT: Websockets](https://spring.io/blog/2021/01/25/ymnnalft-websockets) Welcome to another installment of You May Not Need Another Library For That (YMNNALFT)!
- [==grafana.com: How to use WebSockets to visualize real-time IoT data in Grafana==](https://grafana.com/blog/2022/04/05/how-to-use-websockets-to-visualize-real-time-iot-data-in-grafana/)

#### Socket.io

- [Socket.io](https://socket.io)

#### AsyncAPI

- [AsyncAPI](https://www.asyncapi.com/) Building the future of event-driven architecture. Open source tools to easily build and maintain your event-driven architecture. All powered by the AsyncAPI specification, the industry standard for defining asynchronous APIs.
- [thenewstack.io: AsyncAPI Could Be the Default API Format for Event-Driven Architectures](https://thenewstack.io/asyncapi-could-be-the-default-api-format-for-event-driven-architectures/)
- [microcks.io: Simulating CloudEvents with AsyncAPI and Microcks](https://microcks.io/blog/simulating-cloudevents-with-asyncapi/)
    - The rise of Event Driven Architecture (EDA) is a necessary evolution step towards cloud-native applications. Events are the ultimate weapon to decouple your microservices within your architecture. They are bringing great benefits like space and time decoupling, better resiliency and elasticity.
    - But events come also with challenges! One of the first you are facing when starting up as a development team - aside the technology choice - is how to describe these events structure? Another challenge that comes very quickly after being: How can we efficiently work as a team without having to wait for someone else’s events?
    - We’ll explore those particular two challenges and see how to simulate events using CloudEvents, AsyncAPI and Microcks.
    - AsyncAPI is an industry standard for defining asynchronous APIs. Our long-term goal is to make working with EDAs as easy as it is to work with REST APIs.
    - Microcks is an Open source Kubernetes-native tool for mocking/simulating and testing APIs. One purpose of Microcks is to turn your API contract (OpenAPI, AsyncAPI, Postman Collection) into live mocks in seconds. It means that once it has imported your AsyncAPI contract, Microcks start producing mock events on a message broker at a defined frequency. Using Microcks you can then simulate CloudEvents in seconds, without writing a single line of code. Microcks will allow the team relying on input events to start working without waiting for the team coding the event publication.
- [asyncapi.com: AsyncAPI and CloudEvents](https://www.asyncapi.com/blog/asyncapi-cloud-events) I've been receiving the same question for a long time now: Should I use CloudEvents or AsyncAPI? — And my response has always been the same: it depends!
    - CloudEvents: a specification for describing event data in a common way. CloudEvents seeks to ease event declaration and delivery across services, platforms and beyond!
    - AsyncAPI: Create machine-readable definitions of your event-driven APIs.

## Comparisons

- [blog.logrocket.com: GraphQL vs. gRPC vs. REST: Choosing the right API](https://blog.logrocket.com/graphql-vs-grpc-vs-rest-choosing-right-api/)

### SOAP vs REST

- [geeksforgeeks.org: Difference between REST API and SOAP API](https://www.geeksforgeeks.org/difference-between-rest-api-and-soap-api/)
- [reply.com: Web Services: SOAP and REST - A Simple Introduction](https://www.reply.com/solidsoft-reply/en/content/webservices-soap-and-rest-a-simple-introduction)
    - SOAP is a communications protocol while REST is a set of architectural principles for data transmission.
    - REST was designed to be a more straightforward and easy to implement alternative to heavyweight SOAP for web service access. SOAP functions well in distributed environments where REST assumes a direct point to point communication. Also, SOAP allows for services to describe themselves to clients and in some languages allows for automation. On the other hand, REST is fast as less processing is required, uses less bandwidth and is closer to technologies used in web design.
    - The choice on which to use is totally dependent on what the requirement. For example, SOAP is a better choice for applications that have complex API so as to describe the services and methods, where formal contracts are agreed for the exchange format, where a guaranteed level of security is required etc. REST will be preferred when limiting bandwidth and resources, when operations are can be stateless and the information can be cached.

### REST vs OpenAPI vs gRPC

- [imaginarycloud.com: gRPC vs REST: Comparing APIs Architectural Styles](https://www.imaginarycloud.com/blog/grpc-vs-rest/)

### REST vs GraphQL vs gRPC

- [danhacks.com: REST vs. GraphQL vs. gRPC](https://www.danhacks.com/software/grpc-rest-graphql.html)

## Tools

- [OpenAPI Generator 🌟](https://openapi-generator.tech/) Generate clients, servers, and documentation from OpenAPI 2.0/3.x documents
- [dev.to: 7 API Tools for REST Developers and Testers](https://dev.to/javinpaul/7-api-tools-for-rest-developers-and-testers-n67)

### API Testing

- [softwaretestingportal.com: API Testing, Key Terminologies and more...](http://www.softwaretestingportal.com/2020/03/31/api-testing/)
- [mockoon 🌟](https://mockoon.com/) Create mock APIs in seconds. Mockoon is the easiest and quickest way to run mock API locally. No remote deployment, no account required, open source.
- [mockapy](https://pythonium.net/mockapy) Create mock APIs from a JSON object and customize their behavior using a Python rule engine. Open source.
- [thenewstack.io: 4 Essential Tools for Protecting APIs and Web Applications](https://thenewstack.io/4-essential-tools-for-protecting-apis-and-web-applications/)
- [youtube: API Testing Part 1- API Core Concepts](https://www.youtube.com/watch?v=b0D_bkcT4a4&t=1s&ab_channel=SoftwareDiagnosticsCenter)
- [microcks.io 🌟](https://microcks.io/) Open source Kubernetes Native tool for API Mocking and Testing. If you are looking for a tool that helps in microservices API testing on Kubernetes it is worth taking a look at microcksio. It supports OpenAPI 3 and e.g. Kafka with [Avro encoding](https://microcks.io/documentation/guides/avro-messaging/)
- [tricentis.com: Getting started with automated continuous performance testing](https://www.tricentis.com/blog/automated-continuous-performance-testing)
- [dev.to: Top 15 Automated API Testing Tools](https://dev.to/katalon/top-15-automated-api-testing-tools-lasted-update-32ip)
- [opensource.com: 3 ways to test your API with Python](https://opensource.com/article/21/9/unit-test-python) Unit testing can be daunting, but these Python modules will make your life much easier.

### GraphQL

- [GraphQL](https://graphql.org/) A query language for your API
- [thenewstack.io: Why Backend Developers Should Fall in Love with GraphQL too](https://thenewstack.io/why-backend-developers-should-fall-in-love-with-graphql-too/)
- [world.hey.com: Another REST vs GraphQL comparison](https://world.hey.com/sammy.henningsson/another-rest-vs-graphql-comparison-8e8357bb)

#### Hasura

- [Hasura 🌟](https://hasura.io/) Instant realtime GraphQL APIs for all your data
    - Build modern apps and APIs 10x faster
    - TickInstant GraphQL & REST APIs
    - TickBuilt in authorization for secure data access
    - TickOpen source

## Browser APIs


## API Security

- [biztechmagazine.com: 6 Steps to Improved API Security](https://biztechmagazine.com/article/2021/07/6-steps-improved-api-security) Application programming interfaces are critical to businesses. Tech leaders must do more to protect them.
- [portswigger.net: Introducing vAPI – an open source lab environment to learn about API security](https://portswigger.net/daily-swig/introducing-vapi-an-open-source-lab-environment-to-learn-about-api-security)
- [thenewstack.io: Developer, Beware: The 3 API Security Risks You Can’t Overlook](https://thenewstack.io/developer-beware-the-3-api-security-risks-you-cant-overlook/)

## Free Web Services (Public APIs)

- [free-web-services.com](http://free-web-services.com/)
- [SwaggerHub: Free Web Service](https://swagger.io/tools/swaggerhub/)
- [any-api.com](https://any-api.com/)
- [Rapid API](https://rapidapi.com/)

## Open Banking

- [thenewstack.io: A Digital Transformation Journey in the Banking Sector](https://thenewstack.io/a-digital-transformation-journey-in-the-banking-sector/)

## RPA

- [thenewstack.io: True Success in Process Automation Requires Microservices](https://thenewstack.io/true-success-in-process-automation-requires-microservices/)

## API Ops

- [thenewstack.io: How Platform Ops Teams Should Think About API Strategy](https://thenewstack.io/how-platform-ops-teams-should-think-about-api-strategy/) **Platform Ops Is API Ops**

## Related

- [medium: Do I Need an API Gateway if I Use a Service Mesh? 🌟](https://blog.christianposta.com/microservices/do-i-need-an-api-gateway-if-i-have-a-service-mesh/)
- [Creando un API REST en Java (parte 1)](https://www.oscarblancarteblog.com/2018/06/25/creando-un-api-rest-en-java-parte-1/)
- [dev.to: Rapid API Creation with AWS Amplify](https://dev.to/fllstck/rapid-api-creation-with-aws-amplify-3c8i)
- [openapi-comment-parser](https://github.com/bee-travels/openapi-comment-parser) A clean and simple way to document your code for generating OpenAPI (Swagger) specs.

## Video APIs

- [Mux: The API to Video](https://mux.com/)
    - [softwareengineeringdaily.com: Kubernetes vs. Serverless with Matt Ward (podcast) 🌟](https://softwareengineeringdaily.com/2020/12/29/kubernetes-vs-serverless-with-matt-ward-repeat/)

## API Business Models

- [API Business Models. 20 Models in 20 Minutes](https://www.infoq.com/presentations/API-Business-Models/)

## Videos

??? note "Click to expand!"

	<center>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/yWzKJPw_VzM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
	</center>

## Images

??? note "Click to expand!"

	<center>
	[![top 10 api testing tools](images/summarising_top_10_api_testing_tools.png){: style="width:50%"}](https://blog.testproject.io/2020/06/25/top-10-api-testing-tools-to-watch-in-2020/)

	[![20 API Business Models](images/api_business_models.jpg)](https://www.infoq.com/presentations/API-Business-Models/)

	![gRPC vs REST vs GraphQL comparison](images/grpc_vs_rest_vs_graphql.png)

	![REST API Design](images/REST_API_Design.jfif)

    [![REST vs GrapQL](images/rest_vs_graphql.jfif)](https://t.co/AF9GfbgBWZ)
	</center>

## Tweets

<details>
  <summary>Click to expand!</summary>

<center>
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">People complain about tooling fatigue but web dev in 2021 is 10x simpler than in 2011. You just gotta pick the right tools.<br><br>Infra: <a href="https://twitter.com/PulumiCorp?ref_src=twsrc%5Etfw">@PulumiCorp</a> <br>Data: <a href="https://twitter.com/PostgreSQL?ref_src=twsrc%5Etfw">@PostgreSQL</a> <br>API: <a href="https://twitter.com/HasuraHQ?ref_src=twsrc%5Etfw">@HasuraHQ</a> <br>Frontend: <a href="https://twitter.com/vercel?ref_src=twsrc%5Etfw">@vercel</a>&#39;s NextJS<br><br>And no proprietary bullshit—100% open source!</p>&mdash; gunar.uk (@gunar) <a href="https://twitter.com/gunar/status/1395744592071323651?ref_src=twsrc%5Etfw">May 21, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">/1 REST is the most common communication standard between computers over the internet. What is it? Why is it so popular? Let&#39;s take a look at this thread. <a href="https://t.co/GBdBcC56aF">pic.twitter.com/GBdBcC56aF</a></p>&mdash; Alex Xu (@alexxubyte) <a href="https://twitter.com/alexxubyte/status/1562840039142281216?ref_src=twsrc%5Etfw">August 25, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Optimize API performance with these 5 tips.<br><br>Thread🧵👇</p>&mdash; RapidAPI (@Rapid_API) <a href="https://twitter.com/Rapid_API/status/1583599981369303040?ref_src=twsrc%5Etfw">October 21, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">API Testing. What is it?<br><br>Thread 🧵👇</p>&mdash; RapidAPI (@Rapid_API) <a href="https://twitter.com/Rapid_API/status/1584530377686646784?ref_src=twsrc%5Etfw">October 24, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Authentication vs. Authorization – What&#39;s the difference?<br><br>A thread 🧵</p>&mdash; RapidAPI (@Rapid_API) <a href="https://twitter.com/Rapid_API/status/1585617284562812928?ref_src=twsrc%5Etfw">October 27, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Let&#39;s discuss how we can handle CORS in Express.<br><br>Thread 🧵👇</p>&mdash; RapidAPI (@Rapid_API) <a href="https://twitter.com/Rapid_API/status/1585680710945439744?ref_src=twsrc%5Etfw">October 27, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">HTTP headers that developers should be aware of.<br><br>Thread🧵👇</p>&mdash; RapidAPI (@Rapid_API) <a href="https://twitter.com/Rapid_API/status/1590690709299929090?ref_src=twsrc%5Etfw">November 10, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">OAuth2, features, and advantages.<br><br>Thread 🧵👇</p>&mdash; RapidAPI (@Rapid_API) <a href="https://twitter.com/Rapid_API/status/1591229825393491968?ref_src=twsrc%5Etfw">November 12, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">How to increase API performance?<br><br>Thread 🧵👇</p>&mdash; RapidAPI (@Rapid_API) <a href="https://twitter.com/Rapid_API/status/1591167663165898754?ref_src=twsrc%5Etfw">November 11, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Different Architectural Styles of APIs<br><br>Thread 🧵👇</p>&mdash; RapidAPI (@Rapid_API) <a href="https://twitter.com/Rapid_API/status/1595938033559375874?ref_src=twsrc%5Etfw">November 25, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">What is GraphQL? When should we use it?<br><br>How is GraphQL the same as REST? How are they different? Let’s dive deeper.<br><br>Watch here: <a href="https://t.co/AF9GfbgBWZ">https://t.co/AF9GfbgBWZ</a> <a href="https://t.co/EUgGe82rNu">pic.twitter.com/EUgGe82rNu</a></p>&mdash; Bytebytego (@bytebytego) <a href="https://twitter.com/bytebytego/status/1597376508821405696?ref_src=twsrc%5Etfw">November 28, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Local Storage. What is it?<br><br>Thread 🧵👇</p>&mdash; RapidAPI (@Rapid_API) <a href="https://twitter.com/Rapid_API/status/1597364461681131520?ref_src=twsrc%5Etfw">November 28, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Best Practices for Securing API Keys<br><br>Thread 🧵👇</p>&mdash; RapidAPI (@Rapid_API) <a href="https://twitter.com/Rapid_API/status/1602364128382914582?ref_src=twsrc%5Etfw">December 12, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">API Authentication methods<br><br>Thread 🧵👇</p>&mdash; RapidAPI (@Rapid_API) <a href="https://twitter.com/Rapid_API/status/1607357310875193350?ref_src=twsrc%5Etfw">December 26, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Here, we&#39;ll discuss the three most commonly used API authentication techniques:<br><br>- HTTP Authentication<br>- API Keys (Bearer token, JSON Web Token)<br>- OAuth</p>&mdash; RapidAPI (@Rapid_API) <a href="https://twitter.com/Rapid_API/status/1607357314989694977?ref_src=twsrc%5Etfw">December 26, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">HTTP Status codes worth knowing about<br><br>Thread 🧵👇</p>&mdash; RapidAPI (@Rapid_API) <a href="https://twitter.com/Rapid_API/status/1607542503623860224?ref_src=twsrc%5Etfw">December 27, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">What exactly is CORS, and how does it work?<br><br>Thread 🧵</p>&mdash; RapidAPI (@Rapid_API) <a href="https://twitter.com/Rapid_API/status/1607718404038840320?ref_src=twsrc%5Etfw">December 27, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">What is an API? <a href="https://t.co/FBQfcGDsdh">pic.twitter.com/FBQfcGDsdh</a></p>&mdash; RapidAPI (@Rapid_API) <a href="https://twitter.com/Rapid_API/status/1607913741215207424?ref_src=twsrc%5Etfw">December 28, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Difference between API Authentication and API Authorization.<br><br>Thread 🧵👇</p>&mdash; RapidAPI (@Rapid_API) <a href="https://twitter.com/Rapid_API/status/1608077094952607746?ref_src=twsrc%5Etfw">December 28, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">How does JSON web token (JWT) authentication work?<br><br>Thread 🧵👇🏻</p>&mdash; RapidAPI (@Rapid_API) <a href="https://twitter.com/Rapid_API/status/1608267311022211074?ref_src=twsrc%5Etfw">December 29, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">What is the difference between an API and a Microservice?<br><br>Thread 🧵👇</p>&mdash; RapidAPI (@Rapid_API) <a href="https://twitter.com/Rapid_API/status/1608443951840632835?ref_src=twsrc%5Etfw">December 29, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">API security best practices 👇<br><br>{ 1 / 6 } <a href="https://t.co/0IjjK7zhWv">pic.twitter.com/0IjjK7zhWv</a></p>&mdash; RapidAPI (@Rapid_API) <a href="https://twitter.com/Rapid_API/status/1608825046750855169?ref_src=twsrc%5Etfw">December 30, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">What is a REST API?<br><br>Thread 🧵👇</p>&mdash; Rapid (@Rapid_API) <a href="https://twitter.com/Rapid_API/status/1620059239069716484?ref_src=twsrc%5Etfw">January 30, 2023</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">10 API related terms that every developer should be aware of<br><br>Thread 🧵👇</p>&mdash; Rapid (@Rapid_API) <a href="https://twitter.com/Rapid_API/status/1622595951369093120?ref_src=twsrc%5Etfw">February 6, 2023</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">What are CRUD operations?<br><br>Thread 🧵👇</p>&mdash; Rapid (@Rapid_API) <a href="https://twitter.com/Rapid_API/status/1622708700212350976?ref_src=twsrc%5Etfw">February 6, 2023</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">How do Webhooks work?👇 <a href="https://t.co/9CQ76uhY4l">pic.twitter.com/9CQ76uhY4l</a></p>&mdash; Rapid (@Rapid_API) <a href="https://twitter.com/Rapid_API/status/1622958145281597441?ref_src=twsrc%5Etfw">February 7, 2023</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">How to use Axios to make API requests.<br><br>Thread 🧵👇</p>&mdash; Rapid (@Rapid_API) <a href="https://twitter.com/Rapid_API/status/1622737929436114945?ref_src=twsrc%5Etfw">February 6, 2023</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Five GPT-3 based APIs for your next side project.<br><br>Thread 🧵👇</p>&mdash; Rapid (@Rapid_API) <a href="https://twitter.com/Rapid_API/status/1623027032710955008?ref_src=twsrc%5Etfw">February 7, 2023</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">API Design best practices<br><br>Thread 🧵👇</p>&mdash; Rapid (@Rapid_API) <a href="https://twitter.com/Rapid_API/status/1623754827611209730?ref_src=twsrc%5Etfw">February 9, 2023</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">HTTP 2xx Status Codes worth knowing about<br><br>Thread 🧵👇</p>&mdash; Rapid (@Rapid_API) <a href="https://twitter.com/Rapid_API/status/1623802395703533568?ref_src=twsrc%5Etfw">February 9, 2023</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">What&#39;s the difference between the HTTP methods PUT and PATCH?<br> <br>A thread 👇<br><br>{ 1 / 5 } <a href="https://t.co/lTCpIGU9l3">pic.twitter.com/lTCpIGU9l3</a></p>&mdash; Rapid (@Rapid_API) <a href="https://twitter.com/Rapid_API/status/1624045287172984832?ref_src=twsrc%5Etfw">February 10, 2023</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">What&#39;s the difference between API and microservice?<br><br>Thread 🧵👇</p>&mdash; Rapid (@Rapid_API) <a href="https://twitter.com/Rapid_API/status/1625606823561535496?ref_src=twsrc%5Etfw">February 14, 2023</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Top location APIs that you can use in your next project<br><br>Thread 🧵👇</p>&mdash; Rapid (@Rapid_API) <a href="https://twitter.com/Rapid_API/status/1625986027604045825?ref_src=twsrc%5Etfw">February 15, 2023</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Cloud and APIs. How does it work?<br><br>Thread 🧵👇</p>&mdash; Rapid (@Rapid_API) <a href="https://twitter.com/Rapid_API/status/1626944612550975489?ref_src=twsrc%5Etfw">February 18, 2023</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">8 APIs that you can use in your next side project<br><br>Thread 🧵👇</p>&mdash; Rapid (@Rapid_API) <a href="https://twitter.com/Rapid_API/status/1627739094418616320?ref_src=twsrc%5Etfw">February 20, 2023</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">How does JSON web token (JWT) authentication work?<br><br>Thread 🧵👇</p>&mdash; Rapid (@Rapid_API) <a href="https://twitter.com/Rapid_API/status/1628393919124852738?ref_src=twsrc%5Etfw">February 22, 2023</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">REST API development tips 👇<br><br>{ 1 / 6 } <a href="https://t.co/9L2QKReuRp">pic.twitter.com/9L2QKReuRp</a></p>&mdash; Rapid (@Rapid_API) <a href="https://twitter.com/Rapid_API/status/1629104010916503554?ref_src=twsrc%5Etfw">February 24, 2023</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Benefits of API caching 👇🧵</p>&mdash; Rapid (@Rapid_API) <a href="https://twitter.com/Rapid_API/status/1629269919610044416?ref_src=twsrc%5Etfw">February 24, 2023</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Difference between API and Webhook<br><br>Thread 🧵👇</p>&mdash; Rapid (@Rapid_API) <a href="https://twitter.com/Rapid_API/status/1630273097994575873?ref_src=twsrc%5Etfw">February 27, 2023</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">/1 What are the API architectural styles?<br><br>The diagram below shows the common API architectural styles in one picture:<br><br>1. REST<br>2. GraphQL<br>3. Web socket<br>4. Webhook<br>5. gRPC<br>6. SOAP <a href="https://t.co/ojmpp12A09">pic.twitter.com/ojmpp12A09</a></p>&mdash; Alex Xu (@alexxubyte) <a href="https://twitter.com/alexxubyte/status/1630247687114330120?ref_src=twsrc%5Etfw">February 27, 2023</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Introduction to GraphQL queries.<br><br>A thread 🧵👇</p>&mdash; Rapid (@Rapid_API) <a href="https://twitter.com/Rapid_API/status/1633900716703006738?ref_src=twsrc%5Etfw">March 9, 2023</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Let’s talk about different API testing methods.<br><br>Thread 🧵👇</p>&mdash; Rapid (@Rapid_API) <a href="https://twitter.com/Rapid_API/status/1635264412574535682?ref_src=twsrc%5Etfw">March 13, 2023</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">API Integration. What is it?<br><br>Thread 🧵👇</p>&mdash; Rapid (@Rapid_API) <a href="https://twitter.com/Rapid_API/status/1635688708098732055?ref_src=twsrc%5Etfw">March 14, 2023</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">How to avoid API rate limits?<br><br>A thread 🧵👇</p>&mdash; Rapid (@Rapid_API) <a href="https://twitter.com/Rapid_API/status/1635989229879676930?ref_src=twsrc%5Etfw">March 15, 2023</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Difference between JSON and XML<br><br>- Structure<br>- Performance<br>- Compatibility<br>- Usage<br>- Supported types<br>- Readability<br>- Flexibility<br><br>Thread 🧵👇</p>&mdash; Rapid (@Rapid_API) <a href="https://twitter.com/Rapid_API/status/1636854650748928000?ref_src=twsrc%5Etfw">March 17, 2023</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Let&#39;s talk about APIs<br><br>- What is an API<br>- Usage of APIs<br>- Types of APIs<br>- Benefits of APIs<br><br>Thread 🧵👇</p>&mdash; Rapid (@Rapid_API) <a href="https://twitter.com/Rapid_API/status/1638604947162841090?ref_src=twsrc%5Etfw">March 22, 2023</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Let’s learn about OAuth<br><br>Thread 🧵👇</p>&mdash; Rapid (@Rapid_API) <a href="https://twitter.com/Rapid_API/status/1640700244454170625?ref_src=twsrc%5Etfw">March 28, 2023</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Different API Authentication Methods<br><br>1️⃣ Basic Auth<br>2️⃣ API Keys<br>3️⃣ OAuth 2.0<br>4️⃣ JSON Web Tokens<br>5️⃣ Header API Authentication<br><br>Thread 🧵👇</p>&mdash; Rapid (@Rapid_API) <a href="https://twitter.com/Rapid_API/status/1644036496863936513?ref_src=twsrc%5Etfw">April 6, 2023</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">API Design Principles and Best Practices.<br><br>❯ Focus on User Experience<br>❯ Embrace RESTful Principles<br>❯ Use Consistent Naming Conventions<br>❯ Versioning &amp; Backward Compatibility<br>❯ Error Handling and Messaging<br>❯ Pagination and Filtering<br>❯ Security and Authentication<br><br>Thread🧵👇</p>&mdash; Rapid (@Rapid_API) <a href="https://twitter.com/Rapid_API/status/1646215102360858624?ref_src=twsrc%5Etfw">April 12, 2023</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">API documentation.<br><br>Tools, Techniques, and Importance:<br><br>Thread🧵👇</p>&mdash; Rapid (@Rapid_API) <a href="https://twitter.com/Rapid_API/status/1646279275304345600?ref_src=twsrc%5Etfw">April 12, 2023</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">GraphQL APIs: concepts, advantages, and use cases<br><br>Thread 🧵👇</p>&mdash; Rapid (@Rapid_API) <a href="https://twitter.com/Rapid_API/status/1646498485452300289?ref_src=twsrc%5Etfw">April 13, 2023</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">HTTP HEAD method. When is it used?<br><br>Thread 🧵👇</p>&mdash; Rapid (@Rapid_API) <a href="https://twitter.com/Rapid_API/status/1645899271315808257?ref_src=twsrc%5Etfw">April 11, 2023</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</center>
</details>