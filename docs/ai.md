# Artificial Intelligence

1. [Introduction](#introduction)
2. [Machine Learning](#machine-learning)
3. [Transformers Library](#transformers-library)
4. [LLMOps](#llmops)
5. [The MAD (ML/AI/Data) Landscape](#the-mad-mlaidata-landscape)
6. [OpenAI](#openai)
7. [Kubernetes and AI](#kubernetes-and-ai)
8. [IaC Terraform and AI](#iac-terraform-and-ai)
9. [IaC CloudFormation and AI](#iac-cloudformation-and-ai)
10. [Programming](#programming)
11. [Medical Imaging](#medical-imaging)
12. [Computer Vision](#computer-vision)
13. [AIOps](#aiops)
14. [Other Tools](#other-tools)
15. [Videos](#videos)

## Introduction

- [==guru99.com: Artificial Intelligence Tutorial for Beginners: Learn Basics of AI== 🌟🌟🌟](https://www.guru99.com/ai-tutorial.html)
- [==technologyreview.com: Andrew Ng: Forget about building an AI-first business. Start with a mission== 🌟](https://www.technologyreview.com/2021/03/26/1021258/ai-pioneer-andrew-ng-machine-learning-business) An AI pioneer reflects on how companies can use machine learning to transform their operations and solve critical problems.
    - [==technologyreview.es: "Las empresas que empiezan a lo grande con la IA fracasan más"== 🌟](https://www.technologyreview.es/s/13258/las-empresas-que-empiezan-lo-grande-con-la-ia-fracasan-mas) El pionero de la inteligencia artificial Andrew Ng asegura que es más importante tener buenos datos, aunque sean escasos, que muchos, pero mal etiquetados. Cree que todas las empresas deben empezar a pensar en la tecnología con proyectos rápidos, pero pequeños, y escalarlos si resulta que funcionan.
    - [cio.com: Make Better AI Infrastructure Decisions: Why Hybrid Cloud is a Solid Fit 🌟](https://www.cio.com/article/350337/make-better-ai-infrastructure-decisions-why-hybrid-cloud-is-a-solid-fit.html) The unique demands of AI workloads drive increasing popularity of pairing on-premises infrastructure with cloud.
- [hipertextual.com: Diferencias entre Inteligencia Artificial, Machine Learning y Deep Learning](https://hipertextual.com/2023/02/diferencias-ia-machine-learning)
- [businessinsider.es: Los ingenieros de software están aterrorizados ante la posibilidad de ser sustituidos por la IA](https://www.businessinsider.es/tecnologia/ingenieros-software-estan-aterrorizados-posibilidad-ser-sustituidos-ia-1238112)
- [computerhoy.com: ¿Qué es el 'Deep Learning' y por qué se considera una revolución en la inteligencia artificial?](https://computerhoy.20minutos.es)
- [poloclub.github.io: What is a Convolutional Neural Network?](https://poloclub.github.io/cnn-explainer)
- [freecodecamp.org: Ace Your Deep Learning Job Interview](https://www.freecodecamp.org/news/ace-your-deep-learning-job-interview)
- [freecodecamp.org: Deep Learning Fundamentals Handbook – What You Need to Know to Start Your Career in AI](https://www.freecodecamp.org/news/deep-learning-fundamentals-handbook-start-a-career-in-ai)
- [==aman.ai/primers/ai: Distilled AI==](https://aman.ai/primers/ai) Here’s a hand-picked selection of articles on AI fundamentals/concepts that cover the entire process of building neural nets to training them to evaluating results.
    - [==aman.ai/primers/ai/LLM: Primers - Overview of Large Language Models==](https://aman.ai/primers/ai/LLM)
- [forbesargentina.com: Por qué Nvidia, Google y Microsoft apuestan miles de millones en modelos LLM de IA Generativa para biotecnología](https://www.forbesargentina.com/innovacion/por-nvidia-google-microsoft-apuestan-miles-millones-modelos-llm-ia-generativa-biotecnologia-n49278)
- [youtube: AWS re:Invent 2023 - From hype to impact: Building a generative AI architecture (ARC217)](https://www.youtube.com/watch?v=1Lat8dP7Eq0) Generative AI represents a paradigm shift for how companies operate today. Generative AI is empowering developers to reimagine customer experiences and applications while transforming virtually every industry. Organizations are rapidly innovating to create the right architecture for scaling generative AI securely, economically, and responsibly to deliver business value. In this talk, learn how leaders are modernizing their data foundation, selecting industry-leading foundation models, and deploying purpose-built accelerators to unlock the possibilities of generative AI.

## Machine Learning
  - [Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course?hl=es-419) 🌟 - A practical and accelerated introduction to Google's machine learning, featuring a series of animated videos, interactive visualizations, and hands-on exercises. This course covers foundational concepts like regression and classification models, linear regression, loss, gradient descent, and hyperparameter tuning.

- [==github.com/microsoft/ML-For-Beginners: Machine Learning for Beginners - A Curriculum==](https://github.com/microsoft/ML-For-Beginners)
- [==amazon.science/base-tts-samples==](https://www.amazon.science/base-tts-samples) BASE TTS: Audio samples. Audio samples for the paper [BASE TTS: Lessons from building a billion-parameter text-to-speech model on 100K hours of data](https://www.amazon.science/publications/base-tts-lessons-from-building-a-billion-parameter-text-to-speech-model-on-100k-hours-of-data).

## Transformers Library

- [github.com/NielsRogge/Transformers-Tutorials](https://github.com/NielsRogge/Transformers-Tutorials)
- [aman.ai: Transformers](https://aman.ai/primers/ai/transformers)
- [aman.ai: Primers • Bidirectional Encoder Representations from Transformers (BERT)](https://aman.ai/primers/ai/bert)
- [aman.ai: Primers • Generative Pre-trained Transformer (GPT)](https://aman.ai/primers/ai/gpt)

## LLMOps
  - [Development Environments for Cloud Agents](https://cursor.com/blog/cloud-agent-development-environments) 🌟 -Cursor's new tools for configuring development environments for cloud agents. It highlights the importance of robust environments for agents to perform end-to-end engineering tasks, including accessing codebases, dependencies, credentials, and build systems. The feature supports multi-repo environments, allowing agents to reason across multiple codebases, which is crucial for microservice architectures.
  - [Cursor AI Fundamentals Course](https://cursor.com/es/learn) - Official tutorials for Cursor, covering AI fundamentals including models, tokens, hallucinations, agents, MCP, skills, and context. The course is in Spanish and consists of 13 modules.
  - [Cursor Bugbot Effort Levels Documentation](https://cursor.com/docs/bugbot) - Documentation for Cursor's Bugbot, introducing 'effort levels' for users on usage-based plans. These levels can be configured via the Bugbot dashboard.
  - [Claude Code in Action](https://anthropic.skilljar.com/claude-code-in-action) - *(Related to ai-agents-mcp topic)*
  - [LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) 🌟 - A GitHub repository that provides a step-by-step implementation of a ChatGPT-like Large Language Model (LLM) using PyTorch, covering development, pretraining, and finetuning.
  - [Claude Code Best Practice](https://github.com/shanraisshan/claude-code-best-practice) - *(Related to ai-agents-mcp topic)*
  - [Docker for LLMs](https://www.docker.com/llm) - *(Related to docker topic)*
  - [Learn to Manage Investments and Cost Efficiency of Azure and AI Workloads](https://techcommunity.microsoft.com/blog/finopsblog/learn-to-manage-investments-and-cost-efficiency-of-azure-and-ai-workloads/4396862) - *(Related to finops topic)*
  - [How to run Deepseek R1 LLMs on GPU Droplets](https://www.digitalocean.com/community/tutorials/deepseek-r1-gpu-droplets) 🌟 - This tutorial guides users on deploying the Deepseek R1 series of open-source Large Language Models (LLMs) on DigitalOcean's GPU Droplets. It leverages Ollama for easy model execution, focusing on the reasoning capabilities of these new LLMs and their potential to match proprietary alternatives.
  - [Automate Pull Request Descriptions in Azure DevOps with Azure OpenAI](https://johnlokerse.dev/2025/02/10/automate-pull-request-descriptions-in-azure-devops-with-azure-openai) - *(Related to cicd topic)*

- [github.com/tensorchord/Awesome-LLMOps: Awesome LLMOps](https://github.com/tensorchord/Awesome-LLMOps) An awesome & curated list of best LLMOps tools for developers
- [valohai.com/blog/llmops/](https://valohai.com/blog/llmops) LLMOps: MLOps for Large Language Models
- [github.com/mlabonne/llm-course](https://github.com/mlabonne/llm-course) Course to get into Large Language Models (LLMs) with roadmaps and Colab notebooks.
- [itnext.io: Deploy Flexible and Custom Setups with Anything LLM on Kubernetes](https://itnext.io/deploy-flexible-and-custom-setups-with-anything-llm-on-kubernetes-a2b5687f2bcc?gi=6ae60398d669) Step-by-Step Guide to Deploy Anything LLM with OpenAI, Azure AI, and Ollama

## The MAD (ML/AI/Data) Landscape
  - [Ignore Prior Instructions: AI Still Befuddled by Basic Reasoning](https://thenewstack.io/ignore-prior-instructions-ai-still-befuddled-by-basic-reasoning) - An article discussing the limitations of current AI models, particularly their struggles with understanding and acting upon explicit instructions and basic reasoning, even when the instructions are clear. It highlights how AI can still be 'befuddled' by simple logical tasks.

- [mad.firstmark.com: The MAD (ML/AI/Data) Landscape](https://mad.firstmark.com)

## OpenAI
  - [Claude 101: Free Guides to Master Claude](https://claude101.com) - A comprehensive collection of free guides for learning and mastering Anthropic's Claude AI model, covering beginner to expert levels. The content includes guides on basic usage, prompting techniques, certification, team collaboration, design integration, skill creation, advanced techniques for avoiding AI limitations and biases, and using Claude for coding and computer interaction.

- [github.com/openai/openai-cookbook: OpenAI Cookbook](https://github.com/openai/openai-cookbook) Examples and guides for using the OpenAI API
- [xataka.com: Microsoft no quiere poner todos los huevos en la misma cesta: anuncia una asociación con Mistral AI, la OpenAI de Europa](https://www.xataka.com/robotica-e-ia/microsoft-no-quiere-poner-todos-huevos-cesta-anuncia-asociacion-mistral-ai-openai-europa)
    - Mistral AI accederá a la infraestructura en la nube de Azure AI para desarrollar sus modelos y ofrecerlos comercialmente
    - La startup, con sede en París, acaba de lanzar su modelo de lenguaje Mistral Large y su chatbot conversacional Le Chat

## Kubernetes and AI
  - [Introducing Kiro: AWS Agentic AI-Based IDE](https://markrosscloud.medium.com/introducing-kiro-aws-agentic-ai-based-ide-cded711b1409) -Kiro, an AI-based IDE designed to leverage agentic AI for cloud development, specifically mentioning its integration with AWS and potential for Kubernetes environments.
  - [Limitless Kubernetes Scaling for AI and Data-intensive Workloads: The AKS Fleet Strategy](https://blog.aks.azure.com/2025/04/02/Scaling-Kubernetes-for-AI-and-Data-intensive-Workloads) - *(Related to kubernetes topic)*
  - [Warp: The Agentic Development Environment](https://www.warp.dev) - *(Related to kubernetes-tools topic)*

- [==k8sgpt.ai==](https://k8sgpt.ai) K8sGPT is a tool for scanning your kubernetes clusters, diagnosing and triaging issues in simple english. It has SRE experience codified into its analyzers and helps to pull out the most relevant information to enrich it with AI.
- [collabnix.com: The Rise of Kubernetes and AI – Kubectl OpenAI plugin](https://collabnix.com/the-rise-of-kubernetes-and-ai-kubectl-openai-plugin)

## IaC Terraform and AI
  - [Terraform 2.0 in Practice: Using AI to Generate Infrastructure as Code](https://markaicode.com/terraform-ai-infrastructure-as-code) - *(Related to terraform topic)*
  - [Discussion: Where is AI Still Completely Useless?](https://www.reddit.com/r/Terraform/comments/1l7my1x/where_is_ai_still_completely_useless_for) - A Reddit discussion exploring the current limitations of AI and identifying areas where it remains ineffective or completely useless. The conversation touches on various domains and tasks.
  - [AI Meets Terraform: Prompt Strategies for Test Generation](https://masterpoint.io/blog/ai-meets-tf-prompt-strategies-for-test-generation) 🌟 - This article details the experience of developing and refining an LLM prompt using Cursor and Claude Code to generate meaningful Terraform tests. It explores various experimental approaches, emphasizes strategies for creating "durable prompts," and shares the final prompt in a GitHub repository. The content highlights the value of AI in Infrastructure as Code (IaC) workflows, specifically for writing tests for Terraform child modules, and provides takeaways for crafting effective prompts.
  - [AWS Well-Architected IaC Analyzer](https://github.com/aws-samples/well-architected-iac-analyzer) - *(Related to aws-architecture topic)*

- [hashicorp.com: Accelerate your Terraform development with Amazon CodeWhisperer](https://www.hashicorp.com/blog/accelerate-your-terraform-development-with-amazon-codewhisperer)

## IaC CloudFormation and AI

- [IDE extension for AWS Application Composer enhances visual modern applications development with AI-generated IaC](https://aws.amazon.com/blogs/aws/ide-extension-for-aws-application-composer-enhances-visual-modern-applications-development-with-ai-generated-iac)

## Programming
  - **(2025)** [cursor.com: Cursor AI Code Editor](https://cursor.com) 🌟 - The premier AI-first code editor, built as a fork of VS Code, offering features like Cursor Tab (smart autocomplete), Cmd+K (inline edits), Composer (multi-file agentic code generation), and deep codebase indexing.
  - [Tech companies cutting devs for AI](https://www.reddit.com/r/ProgrammerHumor/comments/1tbzih8/techcompaniescuttingdevsforai) - A Reddit post from r/ProgrammerHumor discussing the trend of tech companies reducing their developer workforce in favor of AI.
  - [Extend your coding agent with .NET Skills](https://devblogs.microsoft.com/dotnet/extend-your-coding-agent-with-dotnet-skills) 🌟 - This blog post introduces the dotnet/skills repository, a collection of agent skills designed to enhance coding agents for .NET developers. These skills provide specialized knowledge and context that coding agents can discover and utilize, improving their ability to solve tasks with less trial and error. The post explains the concept of agent skills and their adherence to the Agent Skills specification, which is supported by various coding agents like GitHub Copilot CLI, Visual Studio, and VS Code.
  - [Best Practices for Using GitHub Copilot](https://docs.github.com/en/copilot/get-started/best-practices) 🌟 - A guide detailing the strengths, weaknesses, and optimal usage scenarios for GitHub Copilot, differentiating between inline suggestions and Copilot Chat for various coding tasks, including writing tests, debugging, code generation, and explanation.
  - [Programming with GitHub Copilot Agent Mode](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/programming-with-github-copilot-agent-mode/4400630) 🌟 - This article explores the capabilities of GitHub Copilot's agent mode, detailing how it can assist developers in various programming tasks. It highlights its potential to streamline workflows and enhance productivity within development environments.
  - [Google Launches Gemini Code Assist, Challenging GitHub Copilot with Generous Free Tier](https://www.xataka.com/robotica-e-ia/google-lanza-misil-github-copilot-su-asistente-programacion-ofrece-mucho-uso-gratuito-que-microsoft) - Google has introduced Gemini Code Assist, an AI-powered programming assistant that aims to compete with GitHub Copilot. A key differentiator is its significantly larger free usage tier, offering 180,000 queries per month compared to GitHub Copilot's 2,000, making it a more accessible option for developers to explore and adopt.

- [xataka.com: https://www.xataka.com/servicios/copilot-chatgpt-gpt-4-han-cambiado-para-siempre-mundo-programacion-esto-que-opinan-expertos](https://www.xataka.com/servicios/copilot-chatgpt-gpt-4-han-cambiado-para-siempre-mundo-programacion-esto-que-opinan-expertos)

## Medical Imaging
  - [Microsoft Dragon Copilot: Unified Voice AI Assistant for Healthcare](https://news.microsoft.com/source/2025/03/03/microsoft-dragon-copilot-provides-the-healthcare-industrys-first-unified-voice-ai-assistant-that-enables-clinicians-to-streamline-clinical-documentation-surface-information-and-automate-task) - Microsoft announces Dragon Copilot, a voice AI assistant for the healthcare industry that combines Dragon Medical One and DAX Copilot. It aims to streamline clinical documentation, improve information retrieval, and automate tasks for clinicians, ultimately enhancing well-being, efficiency, and patient experiences.

- [blog.redbrickai.com: F.A.S.T. ⚡️ Meta AI’s Segment Anything for Medical Imaging](https://blog.redbrickai.com/blog-posts/fast-meta-sam-for-medical-imaging)

## Computer Vision

- [github.com/SkalskiP/top-cvpr-2023-papers](https://github.com/SkalskiP/top-cvpr-2023-papers) This repository is a curated collection of the most exciting and influential CVPR 2023 papers.

## AIOps
  - [OpenOps: No-Code FinOps Automation Platform with AI](https://github.com/openops-cloud/openops) - *(Related to finops topic)*
- [HolmesGPT (Robusta)](https://github.com/HolmesGPT/holmesgpt) - Agentic alert investigation for Kubernetes.
- [CAST AI](https://cast.ai) - AI-driven Kubernetes cost optimization and autonomous rightsizing.
- [apmdigest.com: What Can AIOps Do For IT Ops? - Part 1](https://www.apmdigest.com/aiops-itops-1)
    - [apmdigest.com: What Can AIOps Do For IT Ops? - Part 2](https://www.apmdigest.com/aiops-itops-2)
    - [apmdigest.com: What Can AIOps Do For IT Ops? - Part 3](https://www.apmdigest.com/aiops-itops-3)
    - [apmdigest.com: What Can AIOps Do For IT Ops? - Part 4](https://www.apmdigest.com/aiops-itops-4)
    - [apmdigest.com: What Can AIOps Do For IT Ops? - Part 5](https://www.apmdigest.com/aiops-itops-5)
- [thenewstack.io: The Urgency Driving AIOps into Your Enterprise](https://thenewstack.io/the-urgency-driving-aiops-into-your-enterprise)
- [thenewstack.io: Intelligent Automation: What’s the Missing Piece of AIOps?](https://thenewstack.io/intelligent-automation-whats-the-missing-piece-of-aiops)
- [infoworld.com: 5 best practices for securing CI/CD pipelines](https://www.infoworld.com/article/2336728/5-best-practices-for-securing-cicd-pipelines.html) Build in
security from the beginning with continuous testing, automation, zero trust, and AIops.
- [infoq.com: AIOps: Site Reliability Engineering at Scale](https://www.infoq.com/articles/aiops-reliability-engineering)
- [hashicorp.com: Accelerating AI adoption on Azure with Terraform](https://www.hashicorp.com/blog/accelerating-ai-adoption-on-azure-with-terraform)
- [hashicorp.com: AI for infrastructure management](https://www.hashicorp.com/solutions/ai-infrastructure-management) Accelerate your IT operations and support AIOps implementation with HashiCorp.
- [platformengineering.org: AI is changing the future of platform engineering. Are you ready?](https://platformengineering.org/blog/ai-is-changing-the-future-of-platform-engineering-are-you-ready) AI is changing the future of platform engineering. And the future is much closer than you might think.
- [aws.amazon.com/blogs/industries: BMW Group Develops a GenAI Assistant to Accelerate Infrastructure Optimization on AWS](https://aws.amazon.com/blogs/industries/bmw-group-develops-a-genai-assistant-to-accelerate-infrastructure-optimization-on-aws)

## Other Tools
  - [Cerebras AI](https://www.cerebras.ai) - Cerebras offers an AI platform with a free API providing access to various large language models like GPT OSS, Qwen, GLM, and Llama. The service boasts high request limits, fast inference, and options for cloud serving, dedicated scaling, and on-premise deployment. Their hardware, the Wafer-Scale Engine, is designed for ultra-fast AI workloads.
  - [GitHub Copilot CLI for Beginners: Getting Started](https://github.blog/ai-and-ml/github-copilot/github-copilot-cli-for-beginners-getting-started-with-github-copilot-cli) - A beginner's guide to GitHub Copilot CLI, introducing its capabilities for bringing AI assistance directly into the terminal for faster workflow and code generation. Covers installation, authentication, and initial prompt usage.
  - [Using Workspaces for AI Changes Across Multiple Repos](https://ettema.dev/posts/ai-multi-repo-workspaces) - This article explores a workflow for using AI development tools, like GitHub Copilot, when changes span multiple repositories. It proposes creating feature-specific multi-root workspaces in IDEs (e.g., VS Code) to provide AI agents with comprehensive context across different codebases, improving efficiency compared to single-repo operations.
  - [Awesome NotebookLM Slide Prompts](https://github.com/serenakeyitan/awesome-notebookLM-prompts) - A curated collection of NotebookLM and Kael.im slide prompts, sourced from various creative platforms like WeChat, blogs, RED creators, and Twitter/X power users. These prompts are designed to be used with AI tools for generating presentations from documents, notes, and transcripts.
  - [Tabularis: Open Source Desktop Client for Modern Databases with AI and MCP Integration](https://github.com/TabularisDB/tabularis/blob/main/README.es.md) - *(Related to kubernetes-tools topic)*
  - [Skills for Real Engineers](https://github.com/mattpocock/skills) - A GitHub repository containing a collection of agent skills designed for real engineering tasks, focusing on composability, adaptability, and ease of use. These skills aim to assist in developing real applications by providing a more controlled and debuggable approach compared to other development methodologies.
  - [Google Agents CLI](https://github.com/google/agents-cli) 🌟 - The CLI and skills that turn any coding assistant into an expert at creating, evaluating, and deploying AI agents on Google Cloud. It integrates with Gemini CLI, Claude Code, and Codex.
  - [Draw.io MCP for Diagram Generation: Why It’s Worth Using](https://thomasthornton.cloud/draw-io-mcp-for-diagram-generation-why-its-worth-using) - *(Related to cloud-arch-diagrams topic)*
  - [Claude Code Templates](https://github.com/davila7/claude-code-templates) - A GitHub repository containing a CLI tool for configuring and monitoring Claude Code, a project potentially related to AI-driven code generation or assistance.
  - [Quiz Grader](https://github.com/ned1313/quiz-grader) - A GitHub repository containing a certification quiz application and question generator with prompt creator, designed to assist users in studying for technology certification exams through AI-generated practice questions.
  - [Azure DevOps MCP Server Public Preview](https://devblogs.microsoft.com/devops/azure-devops-mcp-server-public-preview) - This blog post announces the public preview of Azure DevOps MCP Server, a local tool that enhances AI assistants like GitHub Copilot by providing them with rich, real-time context from Azure DevOps environments. It enables AI to access and interact with work items, pull requests, test plans, builds, releases, and wiki pages, offering more tailored and accurate responses without data leaving the user's system. The post includes an example of generating test cases from user stories and links to setup instructions.
  - [Awesome MCP Servers](https://github.com/punkpeye/awesome-mcp-servers) - *(Related to ai-agents-mcp topic)*

- [github.com/jupyterlab/jupyter-ai](https://github.com/jupyterlab/jupyter-ai) A generative AI extension for JupyterLab
- [github.com/XingangPan/DragGAN](https://github.com/XingangPan/DragGAN) Drag Your GAN: Interactive Point-based Manipulation on the Generative Image Manifold

## Videos

??? note "Click to expand!"

    <center markdown="1">

    <iframe width="560" height="315" src="https://www.youtube.com/embed/oypdocrbTOE?si=MGkt9GFgQqGvE7Na" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/MRIv2IwFTPg?si=F07g869i6yIfqRdg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/uwbHOpp9xkc?si=Qyql35WTedGaOsxs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/eNIqz_noix8?si=PDx7Xqu4bJocLdao" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/M5QHwkkHgAA?si=yoygGsgi0QL4N8Ul" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

    </center>

  - **(2026)** [Amazon ECS introduces new high-resolution metrics for faster service auto scaling](https://aws.amazon.com/blogs/aws/amazon-ecs-introduces-new-high-resolution-metrics-for-faster-service-auto-scaling) 🌟 - Amazon ECS adds 20-second high-resolution metrics for Target Tracking policies, decreasing scale-out trigger delay by 76% and end-to-end task provisioning time by 72%.
