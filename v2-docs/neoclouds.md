---
type: curation-hub
okf_version: "0.3"
name: "Neoclouds Overview, Sovereign Overlap and Global GPU AI Clouds"
dimension: "Neoclouds & GPU AI Clouds"
resource_count: 16
fresh_2025_2026_count: 16
trust: verified
freshness: active
provenance: "https://github.com/nubenetes/awesome-kubernetes/blob/master/docs/neoclouds.md"
description: "Curated, AI-ranked Neoclouds Overview, Sovereign Overlap & TCO resources for the 2026 Cloud Native architect: top-tier tools, guides and references (Neoclouds &."
---
# Neoclouds Overview, Sovereign Overlap and Global GPU AI Clouds

!!! tip "Nubenetes V2 Elite Portal"
    You are browsing the AI-Curated V2 Elite Edition. Looking for the exhaustive list of references? Check out the [**V1 Historical Archive**](/v1/neoclouds/).

!!! info "Architectural Context"
    Detailed reference for Neoclouds Overview, Sovereign Overlap and Global GPU AI Clouds in the context of Neoclouds & GPU AI Clouds.

!!! abstract "Deep-Dive Topic Pages"
    [European Neoclouds & Country AI Factories](neoclouds-europe.md) · [North America Neoclouds (US & Canada)](neoclouds-north-america.md) · [Asia-Pacific Neoclouds & AI Clouds](neoclouds-apac.md) · [Middle East & GCC Sovereign AI Factories](neoclouds-mena.md) · [Latin America & Africa AI Cloud Hubs](neoclouds-latam-africa.md) · [GPU Fabrics, InfiniBand, Slurm vs K8s & Storage](neoclouds-architecture-stack.md) · [Neocloud IaC Maturity, GPU FinOps & SLAs](neoclouds-iac-finops-sla.md) · [EU Sovereign Cloud Overview & TCO](eu-sovereign-cloud.md)

## Executive Architecture: Global Neoclouds vs Hyperscalers and Sovereign Cloud (2026)

1. [Global Regional Hubs and Technical Pillars](#global-regional-hubs-and-technical-pillars)
2. [What Are Neoclouds and How They Differ From Hyperscalers](#what-are-neoclouds-and-how-they-differ-from-hyperscalers)
3. [Neoclouds vs Sovereign Cloud: Overlap, Convergence and Legal Distinction](#neoclouds-vs-sovereign-cloud-overlap-convergence-and-legal-distinction)
4. [Global Pre-Sales Architecture Decision Flow](#global-pre-sales-architecture-decision-flow)
5. [Global GPU Cost and TCO Benchmarks (EUR and USD vs Hyperscalers)](#global-gpu-cost-and-tco-benchmarks-eur-and-usd-vs-hyperscalers)
6. [When Does a Neocloud Win (Pre-Sales Playbook)](#when-does-a-neocloud-win-pre-sales-playbook)

### Global Regional Hubs and Technical Pillars

Nubenetes V2 maps the specialized global GPU cloud landscape across five continental markets and two cross-cutting engineering pillars, with deep country parity across Europe and direct clickable links to every official provider and stack component:

<div class="eu-hub-grid" aria-label="Global Regional Neocloud Guides">
  <a class="eu-hub-link" href="/neoclouds-europe/">
    <article class="eu-hub-card">
      <header>
        <span class="eu-hub-flag" aria-hidden="true">🇪🇺</span>
        <span class="eu-hub-title">Europe &amp; UK</span>
        <span class="eu-hub-badge">EU/EEA + CH &amp; UK</span>
      </header>
      <p>Nebius · Scaleway · Verda · Nscale · Taiga · Seeweb · OVH · Civo · EuroHPC</p>
      <footer><span class="eu-hub-cta">Explore Europe →</span></footer>
    </article>
  </a>
  <a class="eu-hub-link" href="/neoclouds-north-america/">
    <article class="eu-hub-card">
      <header>
        <span class="eu-hub-flag" aria-hidden="true">🇺🇸</span>
        <span class="eu-hub-title">North America</span>
        <span class="eu-hub-badge">US &amp; Canada</span>
      </header>
      <p>CoreWeave · Lambda · Crusoe · TensorWave · Together · Fireworks · Modal · QScale</p>
      <footer><span class="eu-hub-cta">Explore Americas →</span></footer>
    </article>
  </a>
  <a class="eu-hub-link" href="/neoclouds-apac/">
    <article class="eu-hub-card">
      <header>
        <span class="eu-hub-flag" aria-hidden="true">🌏</span>
        <span class="eu-hub-title">Asia-Pacific</span>
        <span class="eu-hub-badge">JP · IN · SG · AU · KR</span>
      </header>
      <p>Sakura Internet · SoftBank · Yotta Shakti · Neysa · E2E · Firmus SMC · Singtel RE:AI</p>
      <footer><span class="eu-hub-cta">Explore APAC →</span></footer>
    </article>
  </a>
  <a class="eu-hub-link" href="/neoclouds-mena/">
    <article class="eu-hub-card">
      <header>
        <span class="eu-hub-flag" aria-hidden="true">🏜️</span>
        <span class="eu-hub-title">Middle East &amp; GCC</span>
        <span class="eu-hub-badge">UAE · Saudi · Qatar</span>
      </header>
      <p>Core42 / G42 · Khazna · Moro Hub · HUMAIN · center3 · Aramco Digital · Ooredoo · MEEZA</p>
      <footer><span class="eu-hub-cta">Explore MENA →</span></footer>
    </article>
  </a>
  <a class="eu-hub-link" href="/neoclouds-latam-africa/">
    <article class="eu-hub-card">
      <header>
        <span class="eu-hub-flag" aria-hidden="true">🌎</span>
        <span class="eu-hub-title">LatAm &amp; Africa</span>
        <span class="eu-hub-badge">BR · CL · MX · ZA · KE</span>
      </header>
      <p>ODATA · Scala · Elea · Magalu Cloud · Ascenty · KIO · Cassava AI · Teraco · Raxio</p>
      <footer><span class="eu-hub-cta">Explore hubs →</span></footer>
    </article>
  </a>
</div>

<div class="eu-hub-grid eu-hub-grid--pillars" aria-label="Neocloud Engineering Pillars and Sovereign Bridge">
  <a class="eu-hub-link" href="/neoclouds-architecture-stack/">
    <article class="eu-hub-card">
      <header>
        <span class="eu-hub-flag" aria-hidden="true">🔌</span>
        <span class="eu-hub-title">GPU Fabrics, Slurm &amp; K8s</span>
        <span class="eu-hub-badge">IB NDR · NVL72 · llm-d</span>
      </header>
      <p>NVLink vs Quantum InfiniBand vs Spectrum-X RoCEv2, SUNK/Kueue/DRA, WEKA/VAST storage</p>
      <footer><span class="eu-hub-cta">Open architecture →</span></footer>
    </article>
  </a>
  <a class="eu-hub-link" href="/neoclouds-iac-finops-sla/">
    <article class="eu-hub-card">
      <header>
        <span class="eu-hub-flag" aria-hidden="true">🏗️</span>
        <span class="eu-hub-title">IaC, FinOps &amp; Goodput SLAs</span>
        <span class="eu-hub-badge">SkyPilot · OpenTofu</span>
      </header>
      <p>Terraform coverage vs hyperscalers, MTBF/checkpoint math, DCGM health &amp; GPU FinOps</p>
      <footer><span class="eu-hub-cta">Open scorecard →</span></footer>
    </article>
  </a>
  <a class="eu-hub-link" href="/eu-sovereign-cloud/">
    <article class="eu-hub-card">
      <header>
        <span class="eu-hub-flag" aria-hidden="true">🇪🇺</span>
        <span class="eu-hub-title">EU Sovereign Cloud Bridge</span>
        <span class="eu-hub-badge">DORA · ENS · BSI C5</span>
      </header>
      <p>Compare generalist L4 European sovereign clouds, private DCs, VMs &amp; Proxmox/K8s TCO</p>
      <footer><span class="eu-hub-cta">Open EU Sovereign →</span></footer>
    </article>
  </a>
</div>

| Region / Pillar | Core Neocloud Ecosystem (Clickable Official Links) | Dominant Jurisdiction &amp; Energy Edge | Pre-Sales Deep-Dive |
| :--- | :--- | :--- | :--- |
| **Europe &amp; UK (8 Country Hubs)** | [**Nebius**](https://nebius.com), [**Scaleway**](https://www.scaleway.com/en/gpu-instances), [**Verda**](https://verda.com), [**Nscale**](https://nscale.com), [**Taiga/Northern Data**](https://www.taigacloud.com), [**Seeweb**](https://www.seeweb.it/en)/[**Regolo.ai**](https://regolo.ai), [**OVHcloud AI**](https://www.ovhcloud.com/en/public-cloud/ai-training), [**IONOS AI**](https://www.ionos.com/servers/gpu-server), [**Civo**](https://www.civo.com/ai), [**Exoscale**](https://www.exoscale.com/gpu), plus [**EuroHPC AI Factories**](https://eurohpc-ju.europa.eu/ai-factories_en) | **L4 EU/EEA** ([`GDPR`](https://gdpr.eu), [`EU AI Act`](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai), [`DORA`](https://eur-lex.europa.eu/eli/reg/2022/2554/oj)) + **Non-EU CH/UK** ([`Adequacy`](https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/adequacy-decisions_en)) + Nordic/Iberian renewables | [European Neoclouds](/neoclouds-europe/) |
| **North America (US &amp; Canada)** | [**CoreWeave**](https://coreweave.com), [**Lambda**](https://lambda.ai), [**Crusoe**](https://crusoe.ai), [**TensorWave**](https://tensorwave.com) (AMD), [**Together AI**](https://www.together.ai), [**Fireworks**](https://fireworks.ai), [**Baseten**](https://www.baseten.co), [**Modal**](https://modal.com), [**Voltage Park**](https://voltagepark.com), [**Fluidstack**](https://fluidstack.io), [**IREN**](https://iren.com), [**Applied Digital**](https://www.applieddigital.com), [**RunPod**](https://www.runpod.io), [**Vultr**](https://docs.vultr.com/products/compute/instances/cloud-gpu), [**QScale**](https://qscale.com), [**Cohere**](https://cohere.com) | Largest H200/GB200 NVL72 cluster scale + Texas/Dakota/Quebec cheap hydro &amp; stranded power; **US CLOUD Act applies** to US entities | [North America Neoclouds](/neoclouds-north-america/) |
| **Asia-Pacific (APAC)** | [**Sakura Internet**](https://www.sakura.ad.jp), [**SoftBank**](https://www.softbank.jp/en), [**GMO**](https://www.gmo.jp/en) (JP); [**Yotta Shakti**](https://shakticloud.ai), [**Neysa**](https://neysa.ai), [**E2E**](https://www.e2enetworks.com), [**Sify**](https://www.sifytechnologies.com) (IN); [**Firmus**](https://firmus.co)/[**SMC**](https://smc.co), [**NEXTDC**](https://www.nextdc.com), [**Macquarie**](https://macquariedatacentres.com), [**Singtel RE:AI**](https://re-ai.ai) (SG/AU); [**NAVER Cloud**](https://www.ncloud.com)/[**NHN**](https://www.nhncloud.com) (KR) | Strong state subsidies (METI Japan, [**IndiaAI Mission**](https://indiaai.gov.in)) + tropical **liquid immersion cooling** ([Firmus](https://firmus.co) PUE ~1.05) | [APAC Neoclouds](/neoclouds-apac/) |
| **Middle East &amp; GCC (MENA)** | [**Core42**](https://www.core42.ai)/[**G42**](https://www.g42.ai), [**Khazna**](https://khaznadatacenters.com), [**Moro Hub**](https://www.morohub.com) (UAE); [**HUMAIN**](https://www.humain.com), [**center3**](https://www.center3.com), [**Aramco Digital**](https://www.aramcodigital.com) (SA); [**Ooredoo NCP**](https://www.ooredoo.com), [**MEEZA**](https://www.meeza.net) (QA) | Sovereign wealth gigawatt campuses + domestic [**Saudi NCA**](https://nca.gov.sa/en)/PDPL residency connecting EMEA and South Asia | [Middle East &amp; GCC](/neoclouds-mena/) |
| **Latin America &amp; Africa** | [**ODATA**](https://odatadc.com), [**Scala**](https://scaladatacenters.com), [**Elea AI City**](https://eleadatacenters.com), [**Magalu Cloud**](https://magalu.cloud), [**Ascenty**](https://ascenty.com), [**KIO**](https://www.kio.tech/en), [**Cirion**](https://www.ciriontechnologies.com), [**SONDA**](https://www.sonda.com) (LatAm); [**Cassava AI**](https://www.cassava.ai), [**Africa Data Centres**](https://www.africadatacentres.com), [**Teraco**](https://www.teraco.co.za), [**Raxio**](https://raxiogroup.com) (Africa) | Hydro renewable power (Brazil 85%+), [**IX.br**](https://ix.br) &amp; subsea links, continental LGPD &amp; POPIA sovereignty | [LatAm &amp; Africa Hubs](/neoclouds-latam-africa/) |
| **Systems &amp; Execution Engineering** | [**GB200 NVL72**](https://www.nvidia.com/en-us/data-center/gb200-nvl72), [**Quantum-2 IB**](https://www.nvidia.com/en-us/networking/quantum2), [**Spectrum-X**](https://www.nvidia.com/en-us/networking/spectrumx), [**MI300X**](https://www.amd.com/en/products/accelerators/instinct/mi300/mi300x.html), [**Slurm**](https://slurm.schedmd.com)/[**SUNK**](https://github.com/coreweave/sunk-anywhere), [**Kueue**](https://github.com/kubernetes-sigs/kueue)/[**vLLM**](https://github.com/vllm-project/vllm)/[**`llm-d`**](https://github.com/llm-d/llm-d), [**SkyPilot**](https://skypilot.readthedocs.io), [**WEKA**](https://docs.weka.io)/[**VAST**](https://www.vastdata.com) | Raw goodput efficiency, checkpoint I/O throughput, multi-provider [OpenTofu](https://opentofu.org)/[SkyPilot](https://skypilot.readthedocs.io) exit portability | [Fabrics &amp; Stack](/neoclouds-architecture-stack/) · [IaC &amp; SLAs](/neoclouds-iac-finops-sla/) |

### What Are Neoclouds and How They Differ From Hyperscalers

**Neoclouds** (short for *New Cloud* or *GPU-Native AI Cloud* providers) are specialized cloud infrastructure operators engineered **from the bare metal up specifically for parallel AI training, fine-tuning, and high-throughput inference**, rather than general-purpose enterprise web, ERP, and SaaS hosting.

Unlike [AWS](https://aws.amazon.com), [Azure](https://azure.microsoft.com), and [GCP](https://cloud.google.com) — which layer expensive multi-tenant SDN hypervisors, noisy VPC gateways, general-purpose control planes, and hefty internet egress markups over shared data center footprints — Neoclouds strip away general-purpose overhead to maximize **FLOPs, memory bandwidth, and Tokens-per-Second per EUR spent**:

1. **Archetype 1 — Bare-Metal &amp; Kubernetes GPU Clouds ([CoreWeave](https://coreweave.com), [Nebius](https://nebius.com), [Crusoe](https://crusoe.ai), [Lambda](https://lambda.ai), [Nscale](https://nscale.com), [Verda](https://verda.com), [Seeweb](https://www.seeweb.it/en)):** Direct bare-metal or ultra-thin virtualized access to multi-node [**NVIDIA H100**](https://www.nvidia.com/en-us/data-center/h100)/[**H200**](https://www.nvidia.com/en-us/data-center/h200)/[**GB200**](https://www.nvidia.com/en-us/data-center/gb200-nvl72) or [**AMD MI300X**](https://www.amd.com/en/products/accelerators/instinct/mi300/mi300x.html) pods wired with non-blocking **3.2 Tbps [Quantum-2 InfiniBand](https://www.nvidia.com/en-us/networking/quantum2)** or **[Spectrum-X RoCEv2](https://www.nvidia.com/en-us/networking/spectrumx)**, native [**Slurm**](https://slurm.schedmd.com) / [**SUNK**](https://github.com/coreweave/sunk-anywhere) / Managed Kubernetes, and [**WEKA**](https://docs.weka.io) / [**VAST**](https://www.vastdata.com) / [**Lustre**](https://www.lustre.org) shared NVMe filesystems.
2. **Archetype 2 — Serverless &amp; Compound Inference Clouds ([Together AI](https://www.together.ai), [Fireworks AI](https://fireworks.ai), [Baseten](https://www.baseten.co), [Modal](https://modal.com), [RunPod Serverless](https://www.runpod.io), [Scaleway Generative APIs](https://www.scaleway.com/en/generative-apis), [Regolo.ai](https://regolo.ai)):** Custom CUDA/[ROCm](https://rocm.docs.amd.com) inference engines ([**vLLM**](https://github.com/vllm-project/vllm), [**TensorRT-LLM**](https://github.com/NVIDIA/TensorRT-LLM), [**SGLang**](https://github.com/sgl-project/sglang), speculative decoding) delivering open-weight LLM tokens via OpenAI-compatible APIs at **50–80% lower EUR/token** than frontier proprietary APIs.
3. **Archetype 3 — Energy-First &amp; AI Factory Operators ([IREN](https://iren.com), [Applied Digital](https://www.applieddigital.com), [Merlin-Edged](https://edged.es), [atNorth](https://atnorth.com), [Green Mountain](https://greenmountain.no), [Firmus](https://firmus.co)/[SMC](https://smc.co), [QScale](https://qscale.com), [Khazna](https://khaznadatacenters.com)):** Power-and-cooling-led operators securing 50–500 MW substations, direct liquid/immersion cooling, and long-term hydro/geothermal/solar PPAs to host wholesale Neocloud and enterprise single-tenant GPU halls.

| Engineering &amp; Commercial Dimension | US Hyperscalers ([AWS](https://aws.amazon.com) / [Azure](https://azure.microsoft.com) / [GCP](https://cloud.google.com)) | Bare-Metal Neoclouds ([CoreWeave](https://coreweave.com) / [Nebius](https://nebius.com) / [Nscale](https://nscale.com) / [Crusoe](https://crusoe.ai)) | European Generalist Sovereign Clouds ([STACKIT](https://stackit.com/en) / [IONOS](https://cloud.ionos.com) / [Arsys](https://www.arsys.es/cloud) / [OUTSCALE](https://en.outscale.com)) |
| :--- | :--- | :--- | :--- |
| **Core Design Optimization** | 250+ general PaaS services (IAM, Serverless, BigQuery, Managed DBs) | **Raw GPU density, [NCCL](https://github.com/NVIDIA/nccl) AllReduce latency, high-speed checkpointing** | **Legal sovereignty, VMware/KVM enterprise hosting, [DORA](https://eur-lex.europa.eu/eli/reg/2022/2554/oj)/[NIS2](https://digital-strategy.ec.europa.eu/en/policies/nis2-directive) compliance** |
| **Multi-Node GPU Interconnect** | Mixed; top-tier EFA/IB (`p5`/`NDv5`) gated behind rigid quotas &amp; premium SKUs | **Standard lossless 400G/800G [InfiniBand](https://www.nvidia.com/en-us/networking/quantum2) or [Spectrum-X](https://www.nvidia.com/en-us/networking/spectrumx) RoCEv2** across pods | Mostly standard 10G–100G Ethernet (except dedicated AI partner partitions) |
| **Liquid Cooling &amp; GB200 Readiness** | Selective new retrofits; many legacy air-cooled racks | **Direct-to-chip liquid cooling (DLC) &amp; immersion built greenfield (80–130 kW/rack)** | Improving rapidly via partner campuses ([Merlin-Edged](https://edged.es), [DATA4](https://www.data4group.com/en), [Taiga](https://www.taigacloud.com)) |
| **Orchestration Interface** | AWS EKS / SageMaker / Batch / GCP GKE | **Kubernetes + [Slurm](https://slurm.schedmd.com) / [SUNK](https://github.com/coreweave/sunk-anywhere) + [KubeRay](https://github.com/ray-project/kuberay) + [OpenTofu](https://opentofu.org)** | VMware vCD / [OpenStack](https://www.openstack.org) / [Proxmox VE](https://www.proxmox.com/en/products/proxmox-virtual-environment/overview) / Managed K8s |
| **Network Egress Pricing** | Punitive (`~EUR 0.08/GB`), punishing hybrid dataset &amp; RAG syncing | **Zero or minimal included egress** for datasets, weights, and checkpoints | **Zero or ultra-low EUR egress**, ideal for steady data repatriation |
| **IaC &amp; Ecosystem Parity** | **~98–100%** (every service in Terraform/[OpenTofu](https://opentofu.org) Day 1) | **~55–80%** (focused cleanly on GPU clusters, K8s, VPC, S3, Shared FS) | **~45–85%** (via OpenStack, [`vmware/vcd`](https://github.com/vmware/terraform-provider-vcd), [`bpg/proxmox`](https://github.com/bpg/terraform-provider-proxmox)) |

### Neoclouds vs Sovereign Cloud: Overlap, Convergence and Legal Distinction

!!! warning "Critical Pre-Sales Rule: 'European Location' on a US Neocloud Does NOT Equal L4 Legal Sovereignty!"
    A frequent pre-sales mistake is conflating **Neoclouds** with **Sovereign Clouds**. [**CoreWeave**](https://coreweave.com) UK/EU, [**Crusoe**](https://crusoe.ai) Iceland, [**Lambda**](https://lambda.ai) London, and [**Vultr**](https://docs.vultr.com/products/compute/instances/cloud-gpu) Frankfurt operate modern GPU facilities inside Europe, yet remain **US-headquartered corporations** legally subject to the **US CLOUD Act / FISA 702** (**Level 1 Data Residency**, NOT Level 4 Legal Sovereignty). Furthermore, inside Europe itself, architects must distinguish **EU/EEA Sovereign Neoclouds** (`Nebius`, `Scaleway`, `OVHcloud`, `Verda`, `Taiga`, `Seeweb`) from **Non-EU European Neoclouds** in **Switzerland** (`Exoscale`, `FINMA`/`revDSG`) and the **Post-Brexit UK** (`Nscale`, `Civo` — governed by `UK GDPR`/`NCSC` under conditional [EU Adequacy](https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/adequacy-decisions_en), not eligible for EU-27-only `SecNumCloud`/`ENS` tenders).

Understanding where **Neoclouds** and **Sovereign Cloud** converge — and where they diverge — allows architects to classify every deal into the exact right quadrant:

| Quadrant | Legal Governance &amp; Ownership | Workloads Where It Wins | Representative Global &amp; European Examples (Clickable) |
| :--- | :--- | :--- | :--- |
| **1. L4 Sovereign Neoclouds (Overlap Sweet Spot)** | **100% non-US domestic corporate control** + sovereign AI compliance ([**EU AI Act**](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai), [**DORA**](https://eur-lex.europa.eu/eli/reg/2022/2554/oj), [**APPI**](https://www.ppc.go.jp/en), [**IndiaAI/MeitY**](https://indiaai.gov.in), [**Saudi NCA**](https://nca.gov.sa/en)) | Regulated healthcare/banking/government **open-weight LLM training &amp; private inference** inside domestic borders | **EU/EEA:** [**Nebius**](https://nebius.com) (NL), [**Scaleway AI**](https://www.scaleway.com/en/gpu-instances), [**OVHcloud AI**](https://www.ovhcloud.com/en/public-cloud/ai-training) (FR), [**Verda**](https://verda.com) (FI), [**Taiga**](https://www.taigacloud.com), [**IONOS AI**](https://www.ionos.com/servers/gpu-server) (DE), [**Seeweb**](https://www.seeweb.it/en)/[**Regolo.ai**](https://regolo.ai), [**Aruba AI3**](https://www.arubacloud.com) (IT), [**Merlin-Edged**](https://edged.es) + [**MareNostrum 5**](https://www.bsc.es/research-and-development/ai-factory) (ES) · **UK/CH (Non-EU):** [**Nscale**](https://nscale.com), [**Civo**](https://www.civo.com/ai) (UK), [**Exoscale**](https://www.exoscale.com/gpu) (CH) · **Global:** [**Sakura**](https://www.sakura.ad.jp)/[**SoftBank**](https://www.softbank.jp/en) (JP), [**Yotta**](https://shakticloud.ai)/[**Neysa**](https://neysa.ai)/[**E2E**](https://www.e2enetworks.com) (IN), [**Core42**](https://www.core42.ai)/[**HUMAIN**](https://www.humain.com)/[**Ooredoo**](https://www.ooredoo.com) (GCC), [**Cassava AI**](https://www.cassava.ai) (AF) |
| **2. US / Global Bare-Metal Neoclouds (L1 in EU)** | **US-headquartered** (CLOUD Act applies even when DCs sit in UK/Iceland/DE); maximum Blackwell rack scale | Unregulated SaaS, commercial AI startups, frontier R&amp;D, and massive non-PII open-weight training chasing lowest **EUR/FLOP** | [**CoreWeave**](https://coreweave.com), [**Lambda**](https://lambda.ai), [**Crusoe**](https://crusoe.ai), [**TensorWave**](https://tensorwave.com) (AMD), [**Voltage Park**](https://voltagepark.com), [**Fluidstack**](https://fluidstack.io), [**Applied Digital**](https://www.applieddigital.com), [**IREN**](https://iren.com), [**Together AI**](https://www.together.ai), [**Fireworks**](https://fireworks.ai), [**Baseten**](https://www.baseten.co), [**Modal**](https://modal.com), [**RunPod**](https://www.runpod.io) |
| **3. EU Generalist Sovereign Clouds &amp; Private DCs** | **L4 National Security Clearances** ([**ENS Alto**](https://ens.ccn.cni.es/en), [**SecNumCloud 3.2**](https://cyber.gouv.fr/en/secnumcloud-for-cloud-service-providers), [**BSI C5**](https://www.bsi.bund.de/EN/Themen/Unternehmen-und-Organisationen/Informationen-und-Empfehlungen/Empfehlungen-nach-Angriffszielen/Cloud-Computing/Kriterienkatalog-C5/kriterienkatalog-c5_node.html), [**ACN QC3**](https://www.acn.gov.it/portale/en/home), [**FINMA**](https://www.finma.ch/en)) | Core banking/ERP VMs, Post-Broadcom [**Proxmox**](https://www.proxmox.com/en/products/proxmox-virtual-environment/overview)/[**OpenStack**](https://www.openstack.org) exits, WORM ransomware vaults, regulated PostgreSQL/Kafka | [**Arsys**](https://www.arsys.es/cloud), [**Gigas**](https://gigas.com/en), [**Alhambra IT**](https://alhambrait.com/en), [**Stackscale**](https://www.stackscale.com) (ES); [**STACKIT**](https://stackit.com/en), [**IONOS**](https://cloud.ionos.com), [**Open Telekom**](https://www.open-telekom-cloud.com/en) (DE); [**3DS OUTSCALE**](https://en.outscale.com), [**Cloud Temple**](https://www.cloud-temple.com/en) (FR); [**WIIT**](https://www.wiit.cloud/en) (IT); [**Exoscale**](https://www.exoscale.com), [**cloudscale.ch**](https://www.cloudscale.ch/en) (CH); [**Elastx**](https://elastx.se/en), [**Cleura**](https://cleura.com) (Nordics) |
| **4. US Hyperscalers (Standard &amp; L2/L3 Sovereign Wrappers)** | **US-owned**, localized EU control-plane ops ([AWS ESC Brandenburg](https://aws.amazon.com/compliance/europe-digital-sovereignty), [S3NS](https://www.s3ns.io/en), [Bleu](https://www.bleucloud.fr/en)) | Heavy serverless/SaaS stacks ([**AWS Bedrock**](https://aws.amazon.com/bedrock), [**Azure AI Foundry**](https://azure.microsoft.com/en-us/products/ai-foundry), [**Google Vertex AI**](https://cloud.google.com/vertex-ai)) needing 200+ managed services under one contract | [**AWS**](https://aws.amazon.com), [**Microsoft Azure**](https://azure.microsoft.com), [**Google Cloud Platform**](https://cloud.google.com) |

!!! tip "2026 Winning Hybrid Reference Pattern: Sovereign Generalist Core + L4 Sovereign Neocloud"
    For regulated European enterprises under [**DORA**](https://eur-lex.europa.eu/eli/reg/2022/2554/oj) and the [**EU AI Act**](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai), **never rebuild your entire corporate ERP inside a GPU startup.** Keep sensitive transactional systems, KMS/HSM vaults, IAM, and PostgreSQL on your **L4 National Sovereign Cloud** ([/eu-sovereign-cloud/](/eu-sovereign-cloud/)), peer over local neutral IXPs ([**DE-CIX**](https://www.de-cix.net/en), [**AMS-IX**](https://www.ams-ix.net/ams), [**France-IX**](https://www.franceix.net/en), [**ESpanix**](https://www.espanix.net/en), [**MIX**](https://www.mix-it.net/en), [**LINX**](https://www.linx.net)), and burst RAG indexing, fine-tuning, and stateless [**vLLM**](https://github.com/vllm-project/vllm)/[**`llm-d`**](https://github.com/llm-d/llm-d) inference into a nearby **L4 Sovereign Neocloud** ([Nebius](https://nebius.com), [Scaleway](https://www.scaleway.com/en/gpu-instances), [Verda](https://verda.com), [IONOS](https://www.ionos.com/servers/gpu-server), [Seeweb](https://www.seeweb.it/en), [Nscale](https://nscale.com)).

### Global Pre-Sales Architecture Decision Flow

```mermaid
%%{init: {'themeVariables': {'fontSize': '13px'}, 'flowchart': {'htmlLabels': false, 'nodeSpacing': 20, 'rankSpacing': 68, 'padding': 12}}}%%
flowchart LR
    A(["AI Workload<br/>Assessment"]) --> B{{"L4 Non-US Legal<br/>Sovereignty?"}}

    B -->|"Yes"| C{{"Which Sovereign<br/>Region?"}}
    C -->|"Europe & UK"| C1["Europe L4 Sovereign<br/>Nebius · Scaleway · Verda<br/>Nscale · Taiga · Seeweb"]
    C -->|"Japan & India"| C2["Japan & India Sovereign<br/>Sakura · SoftBank · GMO<br/>Yotta Shakti · Neysa · E2E"]
    C -->|"GCC & Rest"| C3["GCC, AU & LatAm/Africa<br/>Core42 · HUMAIN · Ooredoo<br/>Firmus/SMC · Cassava AI"]

    B -->|"No"| D{{"Primary AI<br/>Workload Profile?"}}
    D -->|"Large IB Train"| D1["Pre-Training & RLHF<br/>CoreWeave · Nebius · Crusoe<br/>Lambda · TensorWave"]
    D -->|"K8s Inference"| D2["24x7 vLLM & llm-d Fleet<br/>Nebius · Scaleway · RunPod<br/>Vultr · Hyperstack · Civo"]
    D -->|"Token API"| D3["Serverless Inference<br/>Together · Fireworks · Modal<br/>Baseten · Scaleway · Regolo"]
    D -->|"Managed PaaS"| D4["Hyperscaler AI PaaS<br/>Bedrock · Azure Foundry<br/>Vertex AI Agent Engine"]
```

### Global GPU Cost and TCO Benchmarks (EUR and USD vs Hyperscalers)

*Indicative 2026 production run-rate benchmarks (`1 USD ≈ 0.92 EUR`) comparing standard hyperscaler SKUs against Neocloud on-demand and 12-month reserved commitments (excluding multi-year custom mega-commitments and variable hyperscaler egress surcharges):*

| Accelerated Node Spec | Network Fabric &amp; Typical VRAM | US Hyperscalers ([AWS](https://aws.amazon.com) / [Azure](https://azure.microsoft.com) / [GCP](https://cloud.google.com)) | US / Global Neoclouds ([CoreWeave](https://coreweave.com) / [Lambda](https://lambda.ai) / [Crusoe](https://crusoe.ai) / [TensorWave](https://tensorwave.com)) | EU &amp; UK Sovereign Neoclouds ([Nebius](https://nebius.com) / [Scaleway](https://www.scaleway.com/en/gpu-instances) / [Verda](https://verda.com) / [Taiga](https://www.taigacloud.com) / [Nscale](https://nscale.com) / [Seeweb](https://www.seeweb.it/en)) | Pre-Sales Savings &amp; TCO Drivers |
| :--- | :--- | :--- | :--- | :--- | :--- |
| [**8x NVIDIA H100 SXM5**](https://www.nvidia.com/en-us/data-center/h100) | [**3.2 Tbps InfiniBand NDR**](https://www.nvidia.com/en-us/networking/quantum2) · 640 GB HBM3 | **EUR 5.90 – 9.05 / GPU-hr** *($6.40 – $9.83/GPU-hr; ~EUR 34k–52k/node/mo)* | **EUR 1.75 – 2.75 / GPU-hr** *($1.90 – $2.99/GPU-hr; ~EUR 10k–16k/node/mo)* | **EUR 1.85 – 2.85 / GPU-hr** *($2.00 – $3.10/GPU-hr; EU VAT/SEPA billing)* | **55–72% cheaper** on Neoclouds; savings multiply when moving multi-TB training checkpoints (zero egress). |
| [**8x NVIDIA H200 SXM**](https://www.nvidia.com/en-us/data-center/h200) | [**3.2 Tbps IB NDR / X800**](https://www.nvidia.com/en-us/networking/quantum2) · **1.13 TB HBM3e** | **EUR 6.45 – 9.75 / GPU-hr** *($7.00 – $10.60/GPU-hr)* | **EUR 2.30 – 3.40 / GPU-hr** *($2.50 – $3.70/GPU-hr)* | **EUR 2.50 – 3.60 / GPU-hr** *($2.70 – $3.90/GPU-hr)* | **50–65% cheaper**; 141 GB HBM3e/GPU fits **Llama-3/DeepSeek 70B+ FP8 inside fewer nodes**, cutting TP comm overhead. |
| [**NVIDIA B200 / GB200 NVL72**](https://www.nvidia.com/en-us/data-center/gb200-nvl72) (Liquid-Cooled) | **NVLink 5 (130 TB/s/rack) + X800 IB** · 192 GB HBM3e/GPU | **Limited Gated Quotas** *(EUR 7.80–11.50+/GPU-hr eq.)* | **EUR 3.50 – 5.20 / GPU-hr** *($3.80 – $5.65/GPU-hr committed clusters)* | **EUR 3.70 – 5.45 / GPU-hr** *($4.00 – $5.90/GPU-hr via [Nebius](https://nebius.com)/[Nscale](https://nscale.com)/[Scaleway](https://www.scaleway.com/en/gpu-instances))* | Unlocked **Blackwell-ready 120 kW+ DLC racks** months ahead of general hyperscaler regional availability. |
| [**8x AMD Instinct MI300X / MI325X**](https://www.amd.com/en/products/accelerators/instinct/mi300/mi300x.html) | **400G RoCEv2 / IB** · **1.54 TB – 2.0 TB HBM3e** | **EUR 4.40 – 6.20 / GPU-hr** *(Azure ND MI300X v5)* | **EUR 1.45 – 2.30 / GPU-hr** *($1.58 – $2.50/GPU-hr via [TensorWave](https://tensorwave.com)/[Crusoe](https://crusoe.ai)/[Vultr](https://docs.vultr.com/products/compute/instances/cloud-gpu))* | **EUR 1.60 – 2.50 / GPU-hr** *([Nscale](https://nscale.com) / [Seeweb](https://www.seeweb.it/en) / [DigitalOcean](https://www.digitalocean.com/products/gpu-droplets) AMD pools)* | **2.4x VRAM/GPU vs H100** makes 8x MI300X ideal for **high-batch 405B inference without multi-node splitting**. |

### When Does a Neocloud Win (Pre-Sales Playbook)

| Customer Scenario | Winning Architectural Recommendation (Clickable) | Why Neoclouds Win Here | Pre-Sales Red Flag to Surface Early |
| :--- | :--- | :--- | :--- |
| **Multi-Node Pre-Training or Continuous Fine-Tuning (`64–2,048+ GPUs`)** | [**Nebius**](https://nebius.com) (EU/US), [**CoreWeave**](https://coreweave.com), [**Crusoe**](https://crusoe.ai), [**Lambda**](https://lambda.ai), [**Nscale**](https://nscale.com), [**Verda**](https://verda.com), or [**Taiga**](https://www.taigacloud.com) with [**Slurm**](https://slurm.schedmd.com) / [**SUNK**](https://github.com/coreweave/sunk-anywhere) + [**WEKA**](https://docs.weka.io)/[**Lustre**](https://www.lustre.org) | Lossless InfiniBand + proactive XID hardware replacement keeps cluster **Model FLOPs Utilization (MFU)** consistently **2x higher** than virtualized cloud VMs. | Never compare raw $/GPU-hr without factoring **[goodput](https://www.clustermax.ai)**: an unstable Ethernet cluster losing 15% of runtime to checkpoint/AllReduce retries costs *more*. |
| **Sustained 24x7 Open-Weight Inference ([`vLLM`](https://github.com/vllm-project/vllm) / [`SGLang`](https://github.com/sgl-project/sglang) / [`llm-d`](https://github.com/llm-d/llm-d))** | [**Scaleway**](https://www.scaleway.com/en/gpu-instances), [**Nebius**](https://nebius.com), [**RunPod**](https://www.runpod.io), [**TensorWave**](https://tensorwave.com) (MI300X), [**Seeweb**](https://www.seeweb.it/en) ([**Regolo.ai**](https://regolo.ai)), or [**Vultr**](https://docs.vultr.com/products/compute/instances/cloud-gpu) | Zero egress tax + dedicated GPU cost cuts per-million-token cost by **45–75%** once daily volume saturates a 4x–8x GPU pod. | Plan **multi-provider failover** ([**LiteLLM**](https://github.com/BerriAI/litellm) / [**Gateway API Inference Extension**](https://github.com/kubernetes-sigs/gateway-api-inference-extension)) because single-region Neoclouds occasionally face power maintenance windows. |
| **Regulated EU/National Banking, Public Sector &amp; Healthcare AI** | **L4 Sovereign Neocloud** ([Nebius](https://nebius.com), [Scaleway](https://www.scaleway.com/en/gpu-instances), [IONOS](https://www.ionos.com/servers/gpu-server), [Seeweb](https://www.seeweb.it/en), [Nscale](https://nscale.com), [Sakura](https://www.sakura.ad.jp), [Yotta](https://shakticloud.ai), [Core42](https://www.core42.ai)) **paired with [Sovereign Core](/eu-sovereign-cloud/)** | Meets [**EU AI Act**](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai), [**GDPR**](https://gdpr.eu), [**DORA**](https://eur-lex.europa.eu/eli/reg/2022/2554/oj), ENS/BSI/SecNumCloud/APPI/DPDP residency inside local national IXPs. | Verify **corporate ownership tree + EU vs UK/CH boundary** cleanly before promising "zero CLOUD Act" or `SecNumCloud` eligibility to a CISO. |
| **Bursty Agents, Batch Embeddings, or Frontier API Prototyping** | Keep [**AWS Bedrock**](https://aws.amazon.com/bedrock) / [**Azure AI Foundry**](https://azure.microsoft.com/en-us/products/ai-foundry) / [**Google Vertex AI**](https://cloud.google.com/vertex-ai) or serverless APIs ([**Together AI**](https://www.together.ai) / [**Fireworks**](https://fireworks.ai) / [**Baseten**](https://www.baseten.co) / [**Modal**](https://modal.com) / [**Scaleway Endpoints**](https://www.scaleway.com/en/generative-apis)) | Zero operational SRE burden for idle periods; pay strictly per active million tokens rather than idle 24x7 bare-metal GPU leases. | Never lock a startup with irregular traffic into a **12-month bare-metal reservation** before validating steady utilization above 55%. |


## European Neoclouds and Country AI Factories

### Netherlands Benelux And France Neoclouds

  - **(2026)** [Scaleway GPU Cloud (Paris / Iliad Group)](https://www.scaleway.com/en/gpu-instances) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[GPU]</span> <span class='md-tag md-tag--primary'>[NEOCLOUD]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — Leading French Neocloud offering H100 SXM5, L40S, and Blackwell GPU nodes integrated natively with Kapsule Kubernetes and Terraform (`scaleway/scaleway`).
### Nordics Alpine And UK Neoclouds Plus Eurohpc AI Factories

  - **(2026)** [Nscale Sovereign AI Cloud (UK and Europe)](https://nscale.com) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[GPU]</span> <span class='md-tag md-tag--primary'>[NEOCLOUD]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — UK-headquartered vertically integrated Neocloud operating renewable liquid-cooled NVIDIA H100/B200 AI factories across Europe, the UK, and North America.
  - **(2026)** [Verda (formerly DataCrunch) Nordic Sovereign GPU Neocloud](https://verda.com) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[GPU]</span> <span class='md-tag md-tag--primary'>[NEOCLOUD]</span> — Helsinki-headquartered European AI Neocloud operating 100% renewable-powered NVIDIA H100, H200, and Blackwell B200 InfiniBand clusters across Finland and Iceland under EU jurisdiction.
## European Sovereign Cloud and Private Dcs

### Netherlands and Benelux Cloud and Dcs

#### Nordics Switzerland And Benelux Cloud And AI Providers

  - **(2026)** [Nebius Sovereign AI Cloud (Amsterdam HQ)](https://nebius.com) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[GPU]</span> <span class='md-tag md-tag--primary'>[NEOCLOUD]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — European-headquartered AI hyperscaler operating massive InfiniBand-interconnected NVIDIA H100, H200, and Blackwell B200 superclusters in Finland and France with Kubernetes (MK8s), Slurm, and Sovereign S3 storage.
## Global Neocloud Reference Leaders And Benchmarks

  - **(2026)** [ClusterMAX: GPU Cloud Rating and Cluster Benchmarks](https://www.clustermax.ai) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[GPU]</span> <span class='md-tag md-tag--primary'>[NEOCLOUD]</span> — Independent engineering scorecard evaluating global Neoclouds and hyperscalers on NCCL multi-node fabric efficiency, Slurm and Kubernetes readiness, lifecycle automation, and effective goodput SLA.
  - **(2026)** [CoreWeave: Specialized GPU Hyperscaler](https://coreweave.com) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[GPU]</span> <span class='md-tag md-tag--primary'>[NEOCLOUD]</span> — Flagship North American NVIDIA Exemplar Cloud Partner operating bare-metal Kubernetes, SUNK (Slurm on Kubernetes), and InfiniBand NDR/X800 GPU fabrics across the US, UK, and Europe.
  - **(2026)** [Epoch AI: Compute Trends and AI Factory Economics](https://epoch.ai) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> — Research institute tracking frontier training cluster scaling, power envelopes, accelerator FLOP/watt ratios, and capital efficiency across global AI data centers.
  - **(2026)** [MLCommons: MLPerf Training and Inference Benchmarks](https://mlcommons.org) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[LLM]</span> — Open engineering consortium publishing audited distributed training and LLM inference benchmarks across specialized AI clouds and hyperscalers.
  - **(2026)** [NVIDIA Cloud Partners (NCP) Ecosystem](https://www.nvidia.com/en-us/data-center/gpu-cloud-computing/partners) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[GPU]</span> <span class='md-tag md-tag--primary'>[NEOCLOUD]</span> — Official NVIDIA directory and reference program for specialized GPU cloud providers building validated HGX/DGX H100, H200, Blackwell B200, and GB200 NVL72 AI clusters worldwide.
## Multi-cloud GPU Orchestration And Portability Reference

  - **(2026)** [Nebius AI Cloud Documentation and CLI](https://docs.nebius.com) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[GPU]</span> <span class='md-tag md-tag--primary'>[NEOCLOUD]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — Reference documentation for Nebius Managed Kubernetes (MK8s), Slurm GPU clusters, InfiniBand fabrics, Shared Filesystem, and Terraform automation.
  - **(2026)** [SkyPilot: Multi-Cloud and Neocloud AI Job Broker](https://skypilot.readthedocs.io) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[NEOCLOUD]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — Open-source UC Berkeley orchestration layer automating cluster provisioning, spot failover, and job queueing transparently across Neoclouds (Nebius, RunPod, Lambda, Fluidstack) and hyperscalers.
## North America Neoclouds US and Canada

### Large-scale Bare-metal Training Neoclouds

  - **(2026)** [CoreWeave Cloud Platform and Documentation](https://docs.coreweave.com) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[GPU]</span> <span class='md-tag md-tag--primary'>[NEOCLOUD]</span> — Pioneer US Neocloud engineered around non-blocking InfiniBand fabrics, Kubernetes-native GPU scheduling (CKS), Slurm on Kubernetes (SUNK), and multi-thousand-GPU NVIDIA Blackwell pods.
  - **(2026)** [Lambda Cloud and 1-Click Clusters](https://lambda.ai) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[GPU]</span> <span class='md-tag md-tag--primary'>[NEOCLOUD]</span> — San Jose AI compute specialist offering reserved NVIDIA HGX/Blackwell InfiniBand clusters, deep-learning stack images, and clean per-hour pricing vs AWS/Azure.
### Serverless Inference Elastic GPU And Canadian Green AI Hubs

  - **(2026)** [Baseten: High-Performance Model Inference Infrastructure](https://www.baseten.co) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[GPU]</span> <span class='md-tag md-tag--primary'>[LLM]</span> — Production ML inference platform pairing TensorRT-LLM model compilation and Truss Python packaging with sub-second autoscaling across dedicated and multi-cloud NVIDIA H100/B200 GPUs.
  - **(2026)** [Modal: Serverless Python GPU Cloud](https://modal.com) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[GPU]</span> — Developer-first serverless AI infrastructure spinning up containerized H100, H200, B200, and L40S GPU functions directly from Python code in sub-second cold boots with per-second billing.
## Sovereign Neoclouds Vs Global Bare-metal GPU Clouds

  - **(2026)** [Crusoe Cloud: Clean-Energy AI Infrastructure](https://crusoe.ai) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[GPU]</span> <span class='md-tag md-tag--primary'>[NEOCLOUD]</span> — Energy-first AI cloud co-locating gigawatt-scale NVIDIA and AMD GPU clusters at curtailed renewable and stranded energy sites across North America and Iceland.

---
💡 **Explore Related:** [European Neoclouds & Country AI Factories](./neoclouds-europe.md) | [North America Neoclouds (US & Canada)](./neoclouds-north-america.md) | [Asia-Pacific Neoclouds & AI Clouds](./neoclouds-apac.md)

🔗 **See Also:** [Hypervisors, IaaS, K8s & Sovereign AI](./eu-cloud-workloads-stack.md) | [MLOps](./mlops.md)

