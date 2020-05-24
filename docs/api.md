# APIs with SOAP, REST and gRPC
- [APIs](#apis)
- [Motivation](#motivation)
- [Types of API Protocols](#types-of-api-protocols)
    - [SOAP API Protocol (Simple Object Access Protocol)](#soap-api-protocol-simple-object-access-protocol)
    - [REST API Protocol (Representational State Transfer)](#rest-api-protocol-representational-state-transfer)
        - [OpenAPI Specification (originally known as the Swagger Specification)](#openapi-specification-originally-known-as-the-swagger-specification)
    - [RPC API Protocol (Remote Procedure Call)](#rpc-api-protocol-remote-procedure-call)
        - [gRPC](#grpc)
- [Comparisons](#comparisons)
    - [SOAP vs REST](#soap-vs-rest)
    - [REST vs OpenAPI vs gRPC](#rest-vs-openapi-vs-grpc)
- [Tools](#tools)
    - [API Testing](#api-testing)
    - [GraphQL](#graphql)
- [Free Web Services (Public APIs)](#free-web-services-public-apis)
- [Related](#related)

## APIs
- [wikipedia: API Application Programming Interface](https://simple.wikipedia.org/wiki/Application_programming_interface)
- [apifriends.com: What is an API?](https://apifriends.com/api-management/what-is-an-api/)
- [axway.com: What is API Management?](https://www.axway.com/en/products/api-management/what-is-api-management)
- [mulesoft.com: APIs versus web services](https://blogs.mulesoft.com/dev/api-dev/apis-versus-web-services/)
- [Youtube Playlist: Introduction to APIs](https://www.youtube.com/playlist?list=PLM-7VG-sgbtBBnWb2Jc5kufgtWYEmiMAw)
- [Devdocs.io API Documentation](https://devdocs.io/)

## Motivation
- [APIs published, APIs consumed: mainstream enterprises increasingly behave like software vendors](https://www.zdnet.com/article/apis-published-apis-consumed-mainstream-enterprises-increasingly-behave-like-software-vendors/) Mainstream enterprises increasingly reach out to customers with APIs, digital services. Unlike software providers though, many still have mostly on-premises infrastructure. 

## Types of API Protocols
- [apifriends.com: What are the different types of APIs? 🌟](https://apifriends.com/api-creation/different-types-apis/) Types of API Protocols: SOAP, REST and RPC

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

#### OpenAPI Specification (originally known as the Swagger Specification)
- [OpenAPI](https://www.openapis.org/) evolved from the [Swagger](https://swagger.io/) project. Swagger started out as a specification for documenting RESTful APIs. Later on, tools to generate client and server code and generating of test cases were added. While the original Swagger Specification was donated to the Linux Foundation and renamed the OpenAPI, Swagger remains one of the most widely used open-source toolsets for developing OpenAPIs.
- [Wikipedia: OpenAPI Specification 🌟](https://en.wikipedia.org/wiki/OpenAPI_Specification)
- [OpenAPI FAQ. What is OpenAPI Specification (OAS)? OpenAPI Specification](https://www.openapis.org/faq) The OAS defines a standard, programming language-agnostic interface description for REST APIs, which allows both humans and computers to discover and understand the capabilities of a service without requiring access to source code, additional documentation, or inspection of network traffic.
- [apis.guru/openapi-directory: large archive of sample OpenAPI descriptions](https://apis.guru/openapi-directory/)

### RPC API Protocol (Remote Procedure Call)
- [wikipedia: RPC Remote Procedure Call](https://en.wikipedia.org/wiki/Remote_procedure_call)

#### gRPC
- [gRPC](https://grpc.io/)
- [wikipedia: gRPC](https://en.wikipedia.org/wiki/GRPC)

## Comparisons
### SOAP vs REST
- [geeksforgeeks.org: Difference between REST API and SOAP API](https://www.geeksforgeeks.org/difference-between-rest-api-and-soap-api/)
- [dzone: A Comprehensive Guide to REST vs. SOAP](https://dzone.com/articles/comprehensive-guide-rest-vs-soap) Learn the primary differences between REST and SOAP APIs, each one's benefits, and when it's appropriate to use the two.
- [dzone: Web Services Architecture – When to Use SOAP vs REST](https://dzone.com/articles/web-services-architecture) Learn why SOAP (Simple Object Access Protocol) and REST (Representation State Transfer) are popular with developers working on system integration projects.
- [dzone: Comparing RESTful APIs and SOAP APIs Using MuleSoft as an Example](https://dzone.com/articles/comparing-restful-apis-and-soap-apis) 
- [reply.com: Web Services: SOAP and REST - A Simple Introduction](https://www.reply.com/solidsoft-reply/en/content/webservices-soap-and-rest-a-simple-introduction) 
    - SOAP is a communications protocol while REST is a set of architectural principles for data transmission.
    - REST was designed to be a more straightforward and easy to implement alternative to heavyweight SOAP for web service access. SOAP functions well in distributed environments where REST assumes a direct point to point communication. Also, SOAP allows for services to describe themselves to clients and in some languages allows for automation. On the other hand, REST is fast as less processing is required, uses less bandwidth and is closer to technologies used in web design. 
    - The choice on which to use is totally dependent on what the requirement. For example, SOAP is a better choice for applications that have complex API so as to describe the services and methods, where formal contracts are agreed for the exchange format, where a guaranteed level of security is required etc. REST will be preferred when limiting bandwidth and resources, when operations are can be stateless and the information can be cached.

### REST vs OpenAPI vs gRPC
- [REST vs. gRPC: Battle of the APIs](https://code.tutsplus.com/tutorials/rest-vs-grpc-battle-of-the-apis--cms-30711)
- [Comparing OpenAPI With gRPC 🌟](https://dzone.com/articles/comparing-openapi-with-grpc) OpenAPI is a great choice due to its interoperability. On the other hand, gRPC offers a better performance. Luckily, you don't have to choose one or the other.

## Tools
### API Testing
* [softwaretestingportal.com: API Testing, Key Terminologies and more...](http://www.softwaretestingportal.com/2020/03/31/api-testing/)
* [dzone.com: 10 API Testing Tips for Beginners (SOAP and REST)](https://dzone.com/articles/10-api-testing-tips-for-beginners-soap-amp-rest) Let's take a look at ten API testing tips for beginners with a focus on REST APIs and SOAP APIs. 

### GraphQL
- [GraphQL](https://graphql.org/) A query language for your API
- [How is the OpenAPI Specification different from GraphQL?](https://www.openapis.org/faq) How are screws better than nails? Both are useful tools that solve similar problems in slightly different ways. OpenAPI Specification offers a declarative contract that defines the structure of API requests and responses as discrete operations. GraphQL prefers an interface style that is more like querying a database and is best suited to graph databases. 

## Free Web Services (Public APIs)
- [free-web-services.com](http://free-web-services.com/)
- [SwaggerHub: Free Web Service](https://swagger.io/tools/swaggerhub/)
- [programmableweb.com](https://www.programmableweb.com/)
- [any-api.com](https://any-api.com/)
- [Rapid API](https://rapidapi.com/)

## Related
- [medium: Do I Need an API Gateway if I Use a Service Mesh? 🌟](https://blog.christianposta.com/microservices/do-i-need-an-api-gateway-if-i-have-a-service-mesh/)
* [Dzone: How to Create a REST API With Spring Boot](https://dzone.com/articles/how-to-create-rest-api-with-spring-boot)
* [Dzone: Step-By-Step Spring Boot RESTful Web Service Complete Example](https://dzone.com/articles/spring-boot-restful-web-service-complete-example)
* [Creando un API REST en Java (parte 1)](https://www.oscarblancarteblog.com/2018/06/25/creando-un-api-rest-en-java-parte-1/)