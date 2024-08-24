# Golang - Go

1. [Introduction](#introduction)
2. [Design Patterns](#design-patterns)
3. [Tutorials](#tutorials)
4. [Kubernetes Client Go](#kubernetes-client-go)
5. [Building container images](#building-container-images)
6. [Go cheatsheets](#go-cheatsheets)
7. [Go Frameworks and libraries](#go-frameworks-and-libraries)
8. [Go packages](#go-packages)
9. [Go Tools](#go-tools)
10. [Go Books](#go-books)
11. [Go Samples](#go-samples)
12. [Dockerfile for go](#dockerfile-for-go)
13. [Videos](#videos)
14. [Tweets](#tweets)

## Introduction

- [golang.org](https://golang.org/)
- [github.com/golang/go](https://github.com/golang/go)
- [wikipedia: Go](https://en.wikipedia.org/wiki/Go_(programming_language))
- [golang-design/history](https://github.com/golang-design/history) Go: A Documentary. This document collects many interesting (publicly observable) issues, discussions, proposals, CLs, and talks from the Go development process, which intents to offer a comprehensive reference of the Go history.
- [Awesome Go 🌟](https://github.com/avelino/awesome-go)
- [Zepto is a lightweight framework for the development of microservices & web services in golang](https://github.com/go-zepto/zepto)
- [medium: Microservices in Go](https://medium.com/seek-blog/microservices-in-go-2fc1570f6800)
- [search.gocenter.io: JFrog Go Center](https://search.gocenter.io/) Host your Go-based applications for free on the JFrog Platform.
- [dev.to: Deploying Your First Golang Webapp](https://dev.to/heroku/deploying-your-first-golang-webapp-11b3)
- [eli.thegreenplace.net: REST Servers in Go: Part 4 - using OpenAPI and Swagger](https://eli.thegreenplace.net/2021/rest-servers-in-go-part-4-using-openapi-and-swagger/)
- [blog.getambassador.io: Debugging Go Microservices in Kubernetes with VScode](https://blog.getambassador.io/debugging-go-microservices-in-kubernetes-with-vscode-a36beb48ef1) Tutorial: Learn to debug Go microservices locally while testing against dependencies in a remote Kubernetes cluster
- [developers.redhat.com: Using Delve to debug Go programs on Red Hat Enterprise Linux](https://developers.redhat.com/blog/2021/03/03/using-delve-to-debug-go-programs-on-red-hat-enterprise-linux/)
- [Golang for Node.js Developers](https://github.com/miguelmota/golang-for-nodejs-developers)
- [The Ultimate Go Study Guide](https://github.com/hoanhan101/ultimate-go)
- [ammeon.com: Profiling golang microservices for high throughput on kubernetes/openshift clusters](https://www.ammeon.com/profiling-golang-microservices-for-high-throughput-on-kubernetes-openshift-clusters/)
- [cyberciti.biz: How to install Go [golang] on Ubuntu Linux](https://www.cyberciti.biz/faq/how-to-install-gol-ang-on-ubuntu-linux/)
- [developer.okta.com: Elasticsearch in Go: A Developer's Guide](https://developer.okta.com/blog/2021/04/23/elasticsearch-go-developers-guide)
- [go-ini/ini](https://github.com/go-ini/ini) Package ini provides INI file read and write functionality in Go
- [rakyll/go-test-trace 🌟](https://github.com/rakyll/go-test-trace) Go test with tracing. go-test-trace is like go test but it also generates distributed traces. Generated traces are exported in OTLP to a OpenTelemetry collector. You need to run go-test-trace alongside a collector to export data to distributed tracing service.
- [hashicorp.com: 8 Best Practices for Writing Secure Go Code](https://www.hashicorp.com/resources/8-best-practices-for-writing-secure-go-code)
- [thenewstack.io: Getting Started with Go and InfluxDB](https://thenewstack.io/getting-started-with-go-and-influxdb/)
- [go.dev: A new search experience on pkg.go.dev](https://go.dev/blog/pkgsite-search-redesign)
- [quii/learn-go-with-tests](https://github.com/quii/learn-go-with-tests) Learn Go with test-driven development
- [itnext.io: Go Does Not Need a Java Style GC](https://itnext.io/go-does-not-need-a-java-style-gc-ac99b8d26c60) Why does Go not need a fancy expensive garbage collector like Java and C#? - [erik-engheim.medium.com: Go Does Not Need a Java Style GC](https://erik-engheim.medium.com/go-does-not-need-a-java-style-gc-ac99b8d26c60)
- [levelup.gitconnected.com: Generics in Go: Viva La Revolution!](https://levelup.gitconnected.com/generics-in-go-viva-la-revolution-e27898bf5495)
- [teivah.medium.com: When to Use Generics in Go?](https://teivah.medium.com/when-to-use-generics-in-go-36d49c1aeda)
- [dev.to: JSON Schema Validation in Golang](https://dev.to/franciscomendes10866/how-to-validate-data-in-golang-1f87)
- [blog.logrocket.com: How to build a blockchain from scratch with Go](https://blog.logrocket.com/how-to-build-blockchain-from-scratch-go/)
- [dev.to: Rate limiting HTTP requests in Go using Redis](https://dev.to/mauriciolinhares/rate-limiting-http-requests-in-go-using-redis-51m7)
- [dev.to: Understanding and Crafting HTTP Middlewares in Go](https://dev.to/theghostmac/understanding-and-crafting-http-middlewares-in-go-3183)
- [dev.to: Getting started with Go-Lang](https://dev.to/treva123mutebi/getting-started-with-go-lang-1g0)
- [miguelmota/golang-for-nodejs-developers](https://github.com/miguelmota/golang-for-nodejs-developers) Examples of Golang compared to Node.js for learning
- [blog.logrocket.com: Building a simple app with Go and PostgreSQL](https://blog.logrocket.com/building-simple-app-go-postgresql/)
- [datastation.multiprocess.io: Speeding up Go's builtin JSON encoder up to 55% for large arrays of objects](https://datastation.multiprocess.io/blog/2022-03-03-improving-go-json-encoding-performance-for-large-arrays-of-objects.html)
- [betterprogramming.pub: Writing My First Microservice Using Go](https://betterprogramming.pub/my-first-microservice-using-golang-c5cf69f1376d)
- [dev.to/mavensingh: Advantages and Disadvantages of Go](https://dev.to/mavensingh/advantages-and-disadvantages-of-go-5gha)
- [levelup.gitconnected.com: Concurrency in Go: shared memory](https://levelup.gitconnected.com/concurrency-in-go-shared-memory-a2ef201b396b)
- [luk4z7/go-concurrency-guide: Go Concurrency Guide 🌟](https://github.com/luk4z7/go-concurrency-guide) Practical concurrency guide in Go, communication by channels, patterns
- [medium.com/datascale: Know GOMAXPROCS before deploying your GO app to Kubernetes](https://medium.com/datascale/know-gomaxprocs-before-deploying-your-go-app-to-kubernetes-7a458fb63af1) In this article, you will learn why setting GOMAXPROCS for your Go apps is crucial in Kubernetes. And you'll discover why it's better to assign a full-core CPU to your Go containers.
- [dev.to: Getting Started With Go (golang) | Michael Levan](https://dev.to/thenjdevopsguy/getting-started-with-go-golang-5eh8)

## Design Patterns

- [aly.arriqaaq.com: Golang Design Patterns in Kubernetes](https://aly.arriqaaq.com/golang-design-patterns/)
- [==github.com/paliimx: Data Structures and Algorithms implementation in Go==](https://github.com/paliimx/Data-Structures-and-Algorithms) **Clean and simple implementation in Go**

## Tutorials

- [==dev.to: Create a Restful API with Golang from scratch== 🌟](https://dev.to/pacheco/create-a-restful-api-with-golang-from-scratch-42g2)
- [itnext.io: Generically working with Kubernetes objects in Go](https://itnext.io/generically-working-with-kubernetes-resources-in-go-53bce678f887) Using the unstructured package from k8s API machinery

## Kubernetes Client Go

- [An example of using dynamic client of k8s.io/client-go](https://ymmt2005.hatenablog.com/entry/2020/04/14/An_example_of_using_dynamic_client_of_k8s.io/client-go)
- [medium: Using the Go client framework 🌟](https://medium.com/programming-kubernetes/building-stuff-with-the-kubernetes-api-part-4-using-go-b1d0e3c1c899)
- [iximiuz.com: How To Call Kubernetes API using Go - Types and Common Machinery](https://iximiuz.com/en/posts/kubernetes-api-go-types-and-common-machinery/)
- [itnext.io: Generically working with Kubernetes objects in Go](https://itnext.io/generically-working-with-kubernetes-resources-in-go-53bce678f887) Using the unstructured package from k8s API machinery. In this post you’ll learn how to work with live Kubernetes objects in Go using the typed and dynamic clients available from the API machinery sub-project client-go.
- [medium.com/codex: Explore client-go Informer Patterns](https://medium.com/codex/explore-client-go-informer-patterns-4415bb5f1fbd) Invoke the Kubernetes resources without overloading the cluster. Many popular Kubernetes tools such as K9s are based on client-go. They use the informer pattern to continuously refresh data without posing additional pressure to the API Server. Learn how the informer pattern works in this article.
- [dev.to: Watch and react to Kubernetes objects changes](https://dev.to/lucasepe/watch-and-react-to-kubernetes-objects-changes-3kcg) client-go is the official client library for the Go programming language. In this article, you will learn how to use RESTClient to watch and then react to namespaces changes.
- [shahin-mahmud.medium.com: Write your first Kubernetes operator in go](https://shahin-mahmud.medium.com/write-your-first-kubernetes-operator-in-go-177047337eae)
- [collabnix.com: Kubernetes CRUD Operation using Go on Docker Desktop](https://collabnix.com/kubernetes-crud-operation-using-go-on-docker-desktop/)
- [blog.kubesimplify.com: Perform CRUD Operations on Kubernetes Using Golang 🌟](https://blog.kubesimplify.com/perform-crud-operations-on-kubernetes-using-golang)

## Building container images

- [ahmet.im: Building container images in Go](https://ahmet.im/blog/building-container-images-in-go/)

## Go cheatsheets

- [devhints.io/go: Go cheatsheet](https://devhints.io/go)
- [github.com: golang-cheat-sheet](https://github.com/a8m/golang-cheat-sheet)
- [jimmysong.io/cheatsheets/go](https://jimmysong.io/cheatsheets/go)
- [simplecheatsheet.com/tag/golang-cheat-sheet](https://simplecheatsheet.com/tag/golang-cheat-sheet/)
- [a8m/golang-cheat-sheet](https://github.com/a8m/golang-cheat-sheet) An overview of Go syntax and features.

## Go Frameworks and libraries

- [go-micro](https://github.com/asim/go-micro) Go Micro is a framework for distributed systems development
- [dapr.io](https://dapr.io)
- [reddit.com: What is the best microservice framework in Go?](https://www.reddit.com/r/golang/comments/jnv4bd/what_is_the_best_microservice_framework_in_go/)
- [Masterminds/sprig: Sprig: Template functions for Go templates](https://github.com/Masterminds/sprig) Useful template functions for Go templates. The Go language comes with a built-in template language, but not very many template functions. Sprig is a library that provides more than 100 commonly used template functions.
- [go-kratos/kratos](https://github.com/go-kratos/kratos) A modular-designed and easy-to-use __microservices framework__ in Go.
- [gnet](https://github.com/panjf2000/gnet) 🚀 gnet is a high-performance, lightweight, non-blocking, event-driven networking framework written in pure Go./ gnet
- [dsa0x/sicher](https://github.com/dsa0x/sicher) Sicher is a go module that allows secure storage of encrypted credentials in a version control system.
- [ggicci/httpin: HTTP Input for Go](https://github.com/ggicci/httpin) Decode an HTTP request into a custom struct
- [kubernetes-sigs/e2e-framework](https://github.com/kubernetes-sigs/e2e-framework) A Go framework for end-to-end testing of components running in Kubernetes clusters.
- [forbearing/k8s](https://github.com/forbearing/k8s) This Go library implements various handlers to more easily manipulate kubernetes resources such as pods, deployments, etc, inside or outside a Kubernetes cluster
- [medium.com/vedcraft: Top Microservices Frameworks in Go](https://medium.com/vedcraft/top-microservices-frameworks-in-go-762445c30dd6) Go has been designed to be a modern language — there are scenarios where you don’t need a package or framework as you can leverage standard packages (such as net/http).

## Go packages

- [cap](https://github.com/hashicorp/cap) A collection of authentication Go packages related to OIDC, JWKs and Distributed Claims.
- [volatiletech/sqlboiler](https://github.com/volatiletech/sqlboiler) Generate a Go ORM tailored to your database schema.

## Go Tools

- [jcchavezs/porto](https://github.com/jcchavezs/porto) Tool for adding [vanity imports](https://sagikazarmark.hu/blog/vanity-import-paths-in-go/) URI to Go files. If you want to enforce vanity import paths, it automates the addition of the import directive.
- [mholt/json-to-go](https://github.com/mholt/json-to-go) Translates JSON into a Go type in your browser instantly (original)
- [curl-to-go](https://mholt.github.io/curl-to-go/) Instantly convert curl commands to Go code
- [kkdai/youtube](https://github.com/kkdai/youtube) Download Youtube Video in Golang
- [==github.com/iawia002/lux== 🌟](https://github.com/iawia002/lux) 👾 **Fast and simple video download library and CLI tool written in Go**
- [github.com/Email-Dashboard:](https://github.com/Email-Dashboard/Email-Dashboard) An interactive emailing management service with scheduling, templating, tracking and A/B testing.
- [==gobrew== 🌟](https://github.com/kevincobain2000/gobrew) Go version manager. Super simple tool to install and manage Go versions. Install go without root. Gobrew doesn't require shell rehash.
- [github.com/groundcover-com: Container Restarts Watcher](https://github.com/groundcover-com/blog/tree/main/blog_k8s_containers_restarts)
- [create-go-app/cli](https://github.com/create-go-app/cli) Create a new production-ready project with backend, frontend and deploy automation by running one CLI command!
- [Delve: a debugger for the Go Programming Language](https://github.com/derekparker/delve)
    - [alexsniffin.medium.com: Debugging Remotely with Go in Kubernetes](https://alexsniffin.medium.com/debugging-remotely-in-kubernetes-with-go-fda4f3332316) In this tutorial, you will learn how to debug an application deployed in Kubernetes remotely using VS Code and Delve

## Go Books

- https://github.com/dariubs/GoBooks
- https://lets-go.alexedwards.net Learn to Build Professional Web Applications with Go

## Go Samples

- [inancgumus/learngo 🌟](https://github.com/inancgumus/learngo) A Huge Number of Go Examples, Exercises and Quizzes.
- [==GoogleCloudPlatform/golang-samples: Sample apps and code written for Google Cloud in the Go programming language.==](https://github.com/GoogleCloudPlatform/golang-samples)
- [rehacktive/caffeine](https://github.com/rehacktive/caffeine) A very basic REST service for JSON data - enough for prototyping and MVPs!
- [ebosas/microservices](https://github.com/ebosas/microservices) A microservices example in Go
- [iximiuz/client-go-examples](https://github.com/iximiuz/client-go-examples) Collection of mini-programs demonstrating Kubernetes client-go usage. If you're writing controllers or any other form of automation on top of Kubernetes, this repository with Go examples might come in handy.
- [Mathieu-Desrochers/Learning-Go](https://github.com/Mathieu-Desrochers/Learning-Go) Minimal working examples of Go's unique features.

## Dockerfile for go

- [==dev.to: Dockerfile for Go==](https://dev.to/youngyoshie/dockerfile-for-go-4jjp)
- [dev.to: Dockerize a GoLang HTTP server and deploy it on Kubernetes](https://dev.to/aksrao1998/dockerize-a-golang-http-server-and-deploy-it-on-kubernetes-592j)

## Videos

??? note "Click to expand!"

	<center>
	<iframe width="560" height="315" src="https://www.youtube.com/embed/yyUHQIec83I" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
	</center>

## Tweets

- [twitter.com/GolangRepos](https://twitter.com/GolangRepos)

<details>
  <summary>Click to expand!</summary>

<center>
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">If I were a system administrator looking to learn a new programming language it would be Go.<br><br>So many of our tools including Kubernetes, Prometheus, and Terraform are written, and extended, in Go that it&#39;s almost a requirement next to learning Bash. <a href="https://t.co/OfZmGo4uP5">https://t.co/OfZmGo4uP5</a></p>&mdash; Kelsey Hightower (@kelseyhightower) <a href="https://twitter.com/kelseyhightower/status/1336097427586129920?ref_src=twsrc%5Etfw">December 7, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">✨ Freshly released: go-test-trace. Allows you to generate distributed trace spans from <a href="https://twitter.com/hashtag/golang?src=hash&amp;ref_src=twsrc%5Etfw">#golang</a> test cases and can participate into an existing distributed trace. Useful to diagnose CI/CD or to run locally. <a href="https://t.co/ypLt3sg5MW">https://t.co/ypLt3sg5MW</a> <a href="https://t.co/hGfNJUxi81">pic.twitter.com/hGfNJUxi81</a></p>&mdash; Jaana Dogan ヤナ ドガン (@rakyll) <a href="https://twitter.com/rakyll/status/1440368144430759949?ref_src=twsrc%5Etfw">September 21, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">How I write HTTP services in <a href="https://twitter.com/hashtag/golang?src=hash&amp;ref_src=twsrc%5Etfw">#golang</a> has changed over the years... here&#39;s my current style.<br><br>(Please consider sharing this with somebody you know who&#39;s learning Go.)<br><br>It&#39;s a yarn... 🧶<br><br>1/13</p>&mdash; Mat Ryer (@matryer) <a href="https://twitter.com/matryer/status/1445013230858952705?ref_src=twsrc%5Etfw">October 4, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Working with Kubernetes Objects in Go 🔽<br><br>How data structures from our beloved YAML manifests are represented as Go structs and interfaces.<br><br>(a sneak peek from my work-in-progress article on k8s .io/api and k8s .io/apimachinery modules) <a href="https://t.co/yLTP3riQOb">pic.twitter.com/yLTP3riQOb</a></p>&mdash; Ivan Velichko (@iximiuz) <a href="https://twitter.com/iximiuz/status/1484913470160228354?ref_src=twsrc%5Etfw">January 22, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">What is runtime.Scheme in Kubernetes Go code?<br><br>I&#39;d been confused by this concept for quite some time. Turns out - it&#39;s just a fancy object factory.<br><br>Scheme is a registry maintaining a mapping of Kinds (strings) to Types (structs).<br><br>Schemes are dynamic - new types can be appended. <a href="https://t.co/7o3UYO1HH3">pic.twitter.com/7o3UYO1HH3</a></p>&mdash; Ivan Velichko (@iximiuz) <a href="https://twitter.com/iximiuz/status/1485704726595477515?ref_src=twsrc%5Etfw">January 24, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</center>
</details>