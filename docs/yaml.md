# YAML and JSON. Templating YAML with YAML Processors. Static Checking of Kubernetes YAML Files

1. [Introduction. Templating YAML Files](#introduction-templating-yaml-files)
    1. [K8s YAML tips](#k8s-yaml-tips)
    2. [YAML anchors and aliases](#yaml-anchors-and-aliases)
    3. [YAML Processors](#yaml-processors)
    4. [YAML Validators](#yaml-validators)
    5. [Other YAML Tools. How to create Kubernetes YAML files](#other-yaml-tools-how-to-create-kubernetes-yaml-files)
    6. [Kubernetes examples](#kubernetes-examples)
    7. [Helm and Kustomize](#helm-and-kustomize)
2. [JSON. Templating JSON Files](#json-templating-json-files)
    1. [JSONPath query language](#jsonpath-query-language)
    2. [JSON in Ansible](#json-in-ansible)
    3. [JSON formatting with jq](#json-formatting-with-jq)
    4. [JSON Tools](#json-tools)
    5. [Kubernetes JSON Schemas](#kubernetes-json-schemas)
3. [Static Checking of Kubernetes YAML Files. Kubernetes YAML Validation Tools](#static-checking-of-kubernetes-yaml-files-kubernetes-yaml-validation-tools)
4. [Alternatives](#alternatives)
5. [Base64](#base64)
6. [Videos](#videos)
7. [Tweets](#tweets)

## Introduction. Templating YAML Files

- [wikipedia: YAML](https://en.wikipedia.org/wiki/YAML)
- [redhat.com: YAML for beginners](https://www.redhat.com/sysadmin/yaml-beginners) YAML is an easy, expressive, data-oriented language that distinguishes itself from document markup languages.
- [thoughtworks.com: Templating in YAML](https://www.thoughtworks.com/radar/techniques/templating-in-yaml) As infrastructures grow in complexity, so do the configuration files that define them. Tools such as [AWS CloudFormation](https://aws.amazon.com/cloudformation/), [Kubernetes](https://www.thoughtworks.com/radar/platforms/kubernetes) and [Helm](https://www.thoughtworks.com/radar/tools/helm) expect configuration files in JSON or YAML syntax, presumably in an attempt to make them easy to write and process. However, in most cases, teams quickly reach the point where they have some parts that are similar but not quite the same, for example, when the same service must be deployed in different regions with a slightly different setup. For such cases tools offer templating in YAML (or JSON), which has caused a huge amount of [frustration with practitioners](https://leebriggs.co.uk/blog/2019/02/07/why-are-we-templating-yaml.html). The problem is that the syntax of JSON and YAML requires all sorts of awkward compromises to graft templating features such as conditionals and loops into the files. **We recommend using an API from a programming language instead or, when this is not an option, a templating system in a programming language, either a general-purpose language such as Python or something specialized such as [Jsonnet](https://jsonnet.org/).**
- [Steve Horsfield: DevOps tricks - Templating YAML files](https://stevehorsfield.wordpress.com/2019/08/13/devops-tricks-templating-yaml-files/) Basic text tools fall foul of YAML’s indentation sensitivity. On the other hand, **YAML tools like [ytt](https://get-ytt.io/) are pretty difficult to interpret.** In my case, I opted for a small [jq](https://stedolan.github.io/jq/) program executed via [yq](https://mikefarah.gitbook.io/yq/).
- [redhat.com: Understanding YAML for Ansible. Validating YAML files with YAMLlint 🌟](https://www.redhat.com/sysadmin/understanding-yaml-ansible) Ansible playbooks are written in YAML, YAML Ain't Markup Language. Understanding YAML syntax is a key to success with Ansible.
- [linuxhandbook.com: YAML Basics Every DevOps Engineer Must Know 🌟](https://linuxhandbook.com/yaml-basics/)
- [developers.redhat.com: How to configure YAML schema to make editing files easier](https://developers.redhat.com/blog/2020/11/25/how-to-configure-yaml-schema-to-make-editing-files-easier/)
- [kubernetestutorials.com: Kubernetes : Introduction to YAML 🌟](https://kubernetestutorials.com/kubernetes-tutorials/kubernetes-introduction-to-yaml/)
- [betterprogramming.pub: YAML Tutorial: Get Started With YAML in 5 Minutes](https://betterprogramming.pub/yaml-tutorial-get-started-with-yaml-in-5-minutes-549d462972d8) Syntax, salient features, and advanced features.
- [abhisheksaini.hashnode.dev: YAML For Data Representation?](https://abhisheksaini.hashnode.dev/yaml-for-representation) YAML is a better option than JSON when comes to representation of Data
- [boxunix.com: A Better Way of Organizing Your Kubernetes Manifest Files 🌟](https://boxunix.com/2020/05/15/a-better-way-of-organizing-your-kubernetes-manifest-files/)
- [opensource.com: Make YAML as easy as it looks](https://opensource.com/article/21/9/yaml-cheat-sheet) YAML looks simple so why is it so hard to write? Learn the two secrets to YAML success.
- [javascript.plainenglish.io: Everything You Need To Know About YAML Files](https://javascript.plainenglish.io/everything-you-need-to-know-about-yaml-files-5423358cc5c9) Learning about YAML gives you an advantage over your peers since it literally makes programming and configuring cloud computing resources easier.
- [w3schools.io: YAML - yaml vs yml file](https://www.w3schools.io/file/yaml-vs-yml/)
- [==blog.devgenius.io: YAML with Python==](https://blog.devgenius.io/yaml-with-python-d6787a9bd8ab) This article aims to outline the basics of YAML and write a simple python script that reads configuration details from a YAML file.
- [==realpython.com: YAML: The Missing Battery in Python==](https://realpython.com/python-yaml/) Python lacks built-in support for the YAML data format, commonly used for configuration and serialization, despite clear similarities between the two languages. In this tutorial, you’ll learn how to work with YAML in Python using the available third-party libraries, with a focus on PyYAML.
- [==kubesimplify.com: A Simplified Guide To YAML==](https://kubesimplify.com/a-simplified-guide-to-yaml)
- [betterprogramming.pub: 10 Things You Might Not Know About YAML](https://betterprogramming.pub/10-things-you-might-not-know-about-yaml-b0589da547c) Harness the true power of YAML
- [==spacelift.io/blog/yaml==](https://spacelift.io/blog/yaml) YAML Tutorial : A Complete Language Guide with Examples
- [ruudvanasseldonk.com: The yaml document from hell](https://ruudvanasseldonk.com/2023/01/11/the-yaml-document-from-hell)
- [itnext.io: Python, YAML, and Kubernetes — The Art of Mastering Configuration](https://itnext.io/python-yaml-and-kubernetes-the-art-of-mastering-configuration-cd60029b3f62) A practical guide to simplifying Kubernetes configuration management with Python and YAML

### K8s YAML tips

- [itnext.io: Kubernetes YAML Tips | Daniele Polencic 🌟](https://itnext.io/kubernetes-yaml-tips-and-tricks-904a2c0b2b81)

### YAML anchors and aliases

- [yaml.org: Anchors and Aliases](https://yaml.org/spec/1.2/spec.html#id2765878)
- [support.atlassian.com: YAML anchors and aliases](https://support.atlassian.com/bitbucket-cloud/docs/yaml-anchors/)
- [medium: Don’t Repeat Yourself with Anchors, Aliases and Extensions in Docker Compose Files](https://medium.com/@kinghuang/docker-compose-anchors-aliases-extensions-a1e4105d70bd)
- [docs.ansible.com: YAML anchors and aliases: sharing variable values](https://docs.ansible.com/ansible/latest/user_guide/playbooks_advanced_syntax.html#yaml-anchors-and-aliases-sharing-variable-values)

### YAML Processors

- [github.com/topics/yaml-processor](https://github.com/topics/yaml-processor)
- [ytt](https://get-ytt.io/) is a templating tool that understands YAML structure allowing you to focus on your data instead of how to properly escape it.
- You should use tools such as [yq](https://mikefarah.gitbook.io/yq/) and kustomize to template YAML resources instead of relying on tools that interpolate strings such as [Helm](https://helm.sh/).
- [yq 🌟](https://mikefarah.gitbook.io/yq/) is a lightweight and portable command-line YAML processor. The aim of the project is to be the [jq](https://github.com/stedolan/jq) or sed of yaml files. `yq` allows to query the yaml tree and highlights it:
    - ```k get svc a -o yaml | yq r -```
    - [dev.to: yq : A command line tool that will help you handle your YAML resources better 🌟](https://dev.to/vikcodes/yq-a-command-line-tool-that-will-help-you-handle-your-yaml-resources-better-8j9)
    - [towardsdatascience.com: yq: Mastering YAML Processing in Command Line 🌟](https://towardsdatascience.com/yq-mastering-yaml-processing-in-command-line-e1ff5ebc0823) Learn to parse and manipulate YAML files more efficiently using yq command-line utility and this simple cheat sheet
    - [betterprogramming.pub: My Cheatsheet for the “yq” Tool](https://betterprogramming.pub/my-yq-cheatsheet-34f2b672ee58) Parsing Kubernetes YAML with yq. `yq` is a convenient tool for creating, updating and mangling Kubernetes YAML files. In this tutorial, you will learn how to use it as well as some practical tips and tricks.
- [Kapitan](https://kapitan.dev/) Generic templated configuration management for Kubernetes, Terraform and other things.
- [azohra/yaml.sh](https://github.com/azohra/yaml.sh) A YAML parser completely in bash. [Yaml.sh — YAML Sans Helm](https://medium.com/@KarlKFI/yaml-sh-yaml-sans-helm-e983a3dfdaec)
- [yh - YAML Highlighter](https://github.com/andreazorzetto/yh) is YAML syntax highlighter that works nicely with kubectl output
- [Kubectl output options 🌟](https://gist.github.com/so0k/42313dbb3b547a0f51a547bb968696ba)

### YAML Validators

- [==yamllint.com: YAML Lint - The YAML Validator==](http://www.yamllint.com)
- [==codebeautify.org/yaml-validator==](https://codebeautify.org/yaml-validator)
- [==jsonformatter.org/yaml-validator==](https://jsonformatter.org/yaml-validator)

### Other YAML Tools. How to create Kubernetes YAML files

- [==onlineyamltools.com== 🌟](https://onlineyamltools.com)
- [avencera/yamine](https://github.com/avencera/yamine) A simple CLI for combining json and yaml files
- [k8syaml.com 🌟](https://k8syaml.com) Kubernetes YAML Generator - Powered by Octopus
- [itnext.io: How to create Kubernetes YAML files 🌟](https://itnext.io/how-to-create-kubernetes-yaml-files-abb8426eeb45) - [ref2 at hackernoon.com](https://hackernoon.com/how-to-create-kubernetes-yaml-files)
- [datree.io](https://www.datree.io) Prevent Kubernetes Misconfigurations From Reaching Production
    - [dev.to: Automating quality checks for Kubernetes YAMLs](https://dev.to/wkrzywiec/automating-quality-checks-for-kubernetes-yamls-398)
- [23andMe/Yamale](https://github.com/23andMe/Yamale) A schema and validator for YAML. Ensure that your schema definitions come from internal or trusted sources. Yamale does not protect against intentionally malicious schemas.
- [==instrumenta/kubeval==](https://github.com/instrumenta/kubeval) Validate your Kubernetes configuration files, supports multiple Kubernetes versions. kubeval is a tool for validating a Kubernetes YAML or JSON configuration file. It does so using schemas generated from the Kubernetes OpenAPI specification, and therefore can validate schemas for multiple versions of Kubernetes.
- [medium.com/@slashben81: How to write a YAML file for Kubernetes? | ARMO](https://medium.com/@slashben81/how-to-write-a-yaml-file-for-kubernetes-armo-76f29e533b1f)
- [linkedin.com/pulse: How to write YAML file for Kubernetes | Megha S.k](https://www.linkedin.com/pulse/how-write-yaml-file-kubernetes-megha-s-k)
- [dotnet-helpers.com: How to Convert YAML to JSON / JSON to YAML using PowerShell](https://dotnet-helpers.com/powershell/convert-yaml-to-json-or-json-to-yaml-using-powershell/)
- [yamline.com](https://yamline.com/) Format, validate, compare, and convert YAML data

### Kubernetes examples

- [Kubernetes examples 🌟](https://k8s-examples.container-solutions.com/) A series of YAML references with canonical and as-simple-as-possible demonstrations of kubernetes functionality and features.

### Helm and Kustomize

- [dex.dev: YAML Templating Solutions: Helm & Kustomize](https://www.dex.dev/dex-videos/templating-solutions) Writing config files by hand is like coding with Notepad instead of an IDE. Let's find a better way, and take an overview of the popular solutions Helm & Kustomize.
- [medium.com/geekculture: Convert Kubernetes YAML Files Into Helm Charts](https://medium.com/geekculture/convert-kubernetes-yaml-files-into-helm-charts-4107de079455) - [Helmify](https://github.com/arttor/helmify)

## JSON. Templating JSON Files

- [wikipedia: JSON](https://en.wikipedia.org/wiki/JSON)
- [json.org: Introducing JSON](https://www.json.org/json-en.html)
- [Jsonnet](https://jsonnet.org/) A data templating language for app and tool developers
- [Building a high performance JSON parser](https://dave.cheney.net/high-performance-json.html)
- [json-schema.org: Understanding JSON Schema 🌟](https://json-schema.org/understanding-json-schema/)
- [dzone.com: The Ultimate JSON Library: JSON.simple vs. GSON vs. Jackson vs. JSONP](https://dzone.com/articles/the-ultimate-json-library-jsonsimple-vs-gson-vs-ja) We ran a benchmark test in 2017 and again in 2021 to see how fast four of the most popular JSON libraries for Java parse different sizes of files.
- [buger/jsonparser](https://github.com/buger/jsonparser) One of the fastest alternative JSON parser for Go that does not require schema
- [dev.to: The JSON trick 25% of Python devs don't know about](https://dev.to/codereviewdoctor/the-json-trick-25-of-python-devs-dont-know-about-including-devs-at-microsoft-sentry-unicef-and-more-4h10) Reading and writing JSON files in Python.
- [dev.to: Convert nested JSON to simple JSON in Javascript](https://dev.to/urstrulyvishwak/convert-nested-json-to-simple-json-in-javascript-4a34)
- [pythonspeed.com: Processing large JSON files in Python without running out of memory](https://pythonspeed.com/articles/json-memory-streaming/)
- [thenewstack.io: Why (and How) You Should Manage JSON with SQL](https://thenewstack.io/why-and-how-you-should-manage-json-with-sql/)
- [betterprogramming.pub: How to Make JSON and Python Talk to Each Other](https://betterprogramming.pub/how-to-make-json-and-python-talk-to-each-other-41531d58e59d) Processing and creating JSON data in Python
- [betterprogramming.pub: Exploring JSON, JSON5, and Circular References](https://betterprogramming.pub/exploring-json-json5-and-circular-references-2b5b0c5de532) An in-depth guide on JavaScript Object Notation (JSON)
- [automationreinvented.blogspot.com: What is Json Schema and how to perform schema validation using Rest Assured?](https://automationreinvented.blogspot.com/2022/03/what-is-json-schema-and-how-to-perform.html)
- [==schemastore.org/json: JSON Schema Store== 🌟](https://www.schemastore.org/json/)

### JSONPath query language

- [blog.mariano.cloud: Do you even JSONPath?](https://blog.mariano.cloud/do-you-even-jsonpath) JSONPath as in a JSON query language that enables you to interact with a JSON structured data set. In this article, you will learn how to use JSONPath expressions to parse and format responses from the Kubernetes API.

### JSON in Ansible

- [opensource.com: 5 ways to process JSON data in Ansible 🌟](https://opensource.com/article/21/4/process-json-data-ansible) Structured data is friendly for automation, and you can take full advantage of it with Ansible.

### JSON formatting with jq

- [about.gitlab.com: Tips for productive DevOps workflows: JSON formatting with jq and CI/CD linting automation](https://about.gitlab.com/blog/2021/04/21/devops-workflows-json-format-jq-ci-cd-lint/)
- ```jq -C '.' data.json | less -R``` Use jq to pretty print some JSON data with ANSI color coded syntax and use -R in less to process the color.
- [github.com/ilyash/show-struct](https://github.com/ilyash/show-struct) Shows possible jq paths in a JSON file
- [github.com/01mf02/jaq](https://github.com/01mf02/jaq) A jq clone focussed on correctness, speed, and simplicity

### JSON Tools

- [==jsoncrack.com: JSON Crack 🌟🌟==](https://jsoncrack.com) **Seamlessly visualize your JSON data instantly into graphs**
- [github.com/tomnomnom/gron 🌟](https://github.com/tomnomnom/gron) Make JSON greppable!
- [github.com/ynqa/jnv 🌟](https://github.com/ynqa/jnv) Interactive JSON filter using jq
- [github.com/JFryy/qq](https://github.com/JFryy/qq) jq inspired (and gojq dependent) interoperable config format transcoder with interactive querying.
- [jsoning.com](https://jsoning.com/) A toolset including a formatter, comparer, JSONPath tester, patch generator, and data generator

### Kubernetes JSON Schemas

- [github: Kubernetes JSON Schemas 🌟](https://github.com/instrumenta/kubernetes-json-schema) Schemas for every version of every object in every version of Kubernetes

## Static Checking of Kubernetes YAML Files. Kubernetes YAML Validation Tools

- The ecosystem of static checking of Kubernetes YAML files can be grouped in the following categories:
    - **API validators**: Tools in this category validate a given YAML manifest against the Kubernetes API server.
    - **Built-in checkers**: Tools in this category bundle opinionated checks for security, best practices, etc.
    - **Custom validators**: Tools in this category allow writing custom checks in several languages such as Rego and Javascript.
- [Validating Kubernetes YAML for best practice and policies 🌟](https://learnk8s.io/validating-kubernetes-yaml) In this article, you will learn and compare six different tools:
    - [Kubeval](https://www.kubeval.com/)
    - [Kube-score 🌟](https://github.com/zegl/kube-score) **Kubernetes object analysis with recommendations for improved reliability and security. kube-score is a opensource tool that performs static code analysis of Kubernetes object definitions. The output is a list of recommendations where one can improve to make application more secure and resilient.**
    - [Config-lint](https://stelligent.github.io/config-lint)
    - [Copper](https://github.com/cloud66-oss/copper)
    - [Conftest](https://www.conftest.dev/)
    - [Polaris](https://github.com/FairwindsOps/polaris)
- [kubevious.io: Top Kubernetes YAML Validation Tools](https://kubevious.io/blog/post/top-kubernetes-yaml-validation-tools/)
- [KubeLinter](https://github.com/stackrox/kube-linter) KubeLinter is a static analysis tool that checks Kubernetes YAML files and Helm charts to ensure the applications represented in them adhere to best practices.
    - [==thomasthornton.cloud: Analyze your Kubernetes YAML files and Helm Charts to ensure best practices using KubeLinter in Azure DevOps Pipeline==](https://thomasthornton.cloud/2022/04/13/analyze-your-kubernetes-yaml-files-and-helm-charts-to-ensure-best-practices-using-kuberlinter-in-azure-devops-pipeline/)
- [medium.com/@jonathan_37674: How to validate Kubernetes YAML files? | ARMO](https://medium.com/@jonathan_37674/how-to-validate-kubernetes-yaml-files-armo-e45dd006d633) Explore defining Kubernetes applications using YAML configs and the various steps we can take to effectively validate these config definitions.

## Alternatives

- [ketch](https://theketch.io) - [civo.com: Deployments without YAML using Ketch](https://www.civo.com/learn/deployments-without-yaml-using-ketch)
    - [ketch: Getting Started](https://learn.theketch.io/docs/getting-started)
    - [github.com/shipa-corp/ketch](https://github.com/shipa-corp/ketch/) Ketch is an application delivery framework that facilitates the deployment and management of applications on Kubernetes using a simple command line interface.
    - [dzone.com: Use Ketch to Deploy Apps on Kubernetes Without YAML](https://dzone.com/articles/how-to-use-ketch-to-deploy-applications-on-kuberne) An open-source project for deploying and managing applications on Kubernetes with a command-line interface.
- [shipa.io: DevOps Challenge – Kubernetes Deployment: Ketch vs YAML](https://www.shipa.io/ketch/devops-challenge-kubernetes-deployment-ketch-vs-yaml/)
- [naml: Not another markup language](https://github.com/kris-nova/naml) Framework for replacing Kubernetes YAML with Go.
- [jvns.ca: A list of new(ish) command line tools](https://jvns.ca/blog/2022/04/12/a-list-of-new-ish--command-line-tools/)
    - [jq](https://stedolan.github.io/jq/) (a great JSON-wrangling tool)
    - [jc](https://github.com/kellyjonbrazil/jc) (convert various tools’ output into JSON)
    - [jo](https://github.com/jpmens/jo) (create JSON objects)
    - [yq](https://github.com/mikefarah/yq) (like jq, but for YAML). there’s also another yq
    - [fx](https://github.com/antonmedv/fx) (interactive json tool)
    - [jless](https://github.com/PaulJuliusMartinez/jless) (json pager)
    - [xsv](https://github.com/BurntSushi/xsv) (a command line tool for csv files, from burntsushi)
    - [visidata](https://www.visidata.org/) (“an interactive multitool for tabular data”)
    - [miller](https://github.com/johnkerl/miller) (“like awk/sed/cut/join/sort for CSV/TSV/JSON/JSON lines”)
- [kislyuk/yq](https://github.com/kislyuk/yq) Command-line YAML, XML, TOML processor - jq wrapper for YAML/XML/TOML documents. Worth noting that there are two implementations of yq, the other one being https://github.com/kislyuk/yq. It's a simple(r) wrapper around jq in Python, so it does support everything jq does, as opposed to the Go implementation, which reimplements jq but probably not fully.

## Base64

- [base64encode.org](https://www.base64encode.org/) Base64 Decode and Encode

## Videos

??? note "Click to expand!"

    <center>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/1uFVr15xDGg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/qmDzcu5uY1I" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/iiADhChRriM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/1uFVr15xDGg?si=I-cySo1Uui5z-LUQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
    </center>

## Tweets

??? note "Click to expand!"

    <center>
    <blockquote class="twitter-tweet"><p lang="es" dir="ltr">¿A quién se le ocurrió que sería buena idea el no tener comentarios en ficheros JSON?</p>&mdash; Coding Potions ⚗️ (@CodingPotions) <a href="https://twitter.com/CodingPotions/status/1489608445003280391?ref_src=twsrc%5Etfw">February 4, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

    <blockquote class="twitter-tweet"><p lang="en" dir="ltr">Do you know all the YAML tricks and gotchas?<br><br>Are there any YAML tips for Kubernetes?<br><br>Read along! <a href="https://t.co/BXszAVR4sd">pic.twitter.com/BXszAVR4sd</a></p>&mdash; Daniele Polencic — @danielepolencic@hachyderm.io (@danielepolencic) <a href="https://twitter.com/danielepolencic/status/1620055199053406208?ref_src=twsrc%5Etfw">January 30, 2023</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
    </center>
