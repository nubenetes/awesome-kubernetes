"""Pre-sales & solution-architecture blueprints for the global Neoclouds & GPU AI Clouds pillar."""

NEOCLOUDS_BLUEPRINTS: dict[str, str] = {
    "neoclouds.md": """## Executive Architecture: Global Neoclouds vs Hyperscalers and Sovereign Cloud (2026)

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
""",

    "neoclouds-europe.md": """## Pre-Sales Field Guide: European Neoclouds and Country AI Factories

1. [European Country AI Factories and Sovereign Neocloud Hubs](#european-country-ai-factories-and-sovereign-neocloud-hubs)
2. [Netherlands and Benelux Neoclouds](#netherlands-and-benelux-neoclouds)
3. [France Neoclouds and AI Factories](#france-neoclouds-and-ai-factories)
4. [Germany Neoclouds and Exascale AI](#germany-neoclouds-and-exascale-ai)
5. [Spain Liquid-Cooled AI and MareNostrum 5](#spain-liquid-cooled-ai-and-marenostrum-5)
6. [Italy GPU Clouds and IT4LIA AI Factory](#italy-gpu-clouds-and-it4lia-ai-factory)
7. [Nordics Green Hydro and Geothermal AI Clouds](#nordics-green-hydro-and-geothermal-ai-clouds)
8. [Switzerland and Austria Alpine AI Clouds](#switzerland-and-austria-alpine-ai-clouds)
9. [United Kingdom Neoclouds and Isambard-AI](#united-kingdom-neoclouds-and-isambard-ai)
10. [EuroHPC AI Factories and EU AI Act Positioning](#eurohpc-ai-factories-and-eu-ai-act-positioning)

### European Country AI Factories and Sovereign Neocloud Hubs

Europe leads globally in combining **high-density liquid-cooled NVIDIA AI Factories** with **L4 jurisdictional sovereignty** ([`GDPR`](https://gdpr.eu), [`EU AI Act`](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai), [`DORA`](https://eur-lex.europa.eu/eli/reg/2022/2554/oj)) across the **EU/EEA Perimeter** plus **Switzerland &amp; the United Kingdom** (*Non-EU [Adequacy](https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/adequacy-decisions_en) sovereign hubs*). Every card jumps directly to detailed sections with clickable links to every official provider and sister **European Sovereign Cloud** guide:

<div class="eu-hub-grid" aria-label="European Country Neocloud Hubs">
  <a class="eu-hub-link" href="#netherlands-and-benelux-neoclouds">
    <article class="eu-hub-card">
      <header>
        <span class="eu-hub-flag" aria-hidden="true">🇳🇱</span>
        <span class="eu-hub-title">Netherlands &amp; Benelux</span>
        <span class="eu-hub-badge">EU · Nebius HQ</span>
      </header>
      <p>Nebius AI Cloud · Leafcloud heat-reuse GPUs · Gcore Luxembourg Inference</p>
      <footer><span class="eu-hub-cta">Jump to NL/LU →</span></footer>
    </article>
  </a>
  <a class="eu-hub-link" href="#france-neoclouds-and-ai-factories">
    <article class="eu-hub-card">
      <header>
        <span class="eu-hub-flag" aria-hidden="true">🇫🇷</span>
        <span class="eu-hub-title">France</span>
        <span class="eu-hub-badge">EU · SecNum · Nuclear</span>
      </header>
      <p>Scaleway AI · OVHcloud AI · Fluidstack FR · Mistral AI · DATA4 · Jean Zay</p>
      <footer><span class="eu-hub-cta">Jump to FR →</span></footer>
    </article>
  </a>
  <a class="eu-hub-link" href="#germany-neoclouds-and-exascale-ai">
    <article class="eu-hub-card">
      <header>
        <span class="eu-hub-flag" aria-hidden="true">🇩🇪</span>
        <span class="eu-hub-title">Germany</span>
        <span class="eu-hub-badge">EU · BSI C5 · Exascale</span>
      </header>
      <p>Northern Data Taiga · IONOS H200 · Cloud&amp;Heat DLC · JUPITER GH200</p>
      <footer><span class="eu-hub-cta">Jump to DE →</span></footer>
    </article>
  </a>
  <a class="eu-hub-link" href="#spain-liquid-cooled-ai-and-marenostrum-5">
    <article class="eu-hub-card">
      <header>
        <span class="eu-hub-flag" aria-hidden="true">🇪🇸</span>
        <span class="eu-hub-title">Spain</span>
        <span class="eu-hub-badge">EU · ENS Alto · Solar</span>
      </header>
      <p>Merlin-Edged GB200 racks · BSC MareNostrum 5 AI Factory · Stackscale · Telefonica</p>
      <footer><span class="eu-hub-cta">Jump to ES →</span></footer>
    </article>
  </a>
  <a class="eu-hub-link" href="#italy-gpu-clouds-and-it4lia-ai-factory">
    <article class="eu-hub-card">
      <header>
        <span class="eu-hub-flag" aria-hidden="true">🇮🇹</span>
        <span class="eu-hub-title">Italy</span>
        <span class="eu-hub-badge">EU · ACN AI3 · Bologna</span>
      </header>
      <p>Seeweb H100/B300 · Regolo.ai · Aruba AI3 · CINECA Leonardo &amp; IT4LIA</p>
      <footer><span class="eu-hub-cta">Jump to IT →</span></footer>
    </article>
  </a>
  <a class="eu-hub-link" href="#nordics-green-hydro-and-geothermal-ai-clouds">
    <article class="eu-hub-card">
      <header>
        <span class="eu-hub-flag" aria-hidden="true">🇸🇪</span>
        <span class="eu-hub-title">Nordics</span>
        <span class="eu-hub-badge">EU/EEA · Hydro / Geo</span>
      </header>
      <p>Nebius Mantsala · Verda (DataCrunch) · atNorth · Green Mountain · Verne · LUMI</p>
      <footer><span class="eu-hub-cta">Jump to Nordics →</span></footer>
    </article>
  </a>
  <a class="eu-hub-link" href="#switzerland-and-austria-alpine-ai-clouds">
    <article class="eu-hub-card">
      <header>
        <span class="eu-hub-flag" aria-hidden="true">🇨🇭</span>
        <span class="eu-hub-title">Switzerland &amp; Austria</span>
        <span class="eu-hub-badge">CH Non-EU + AT EU</span>
      </header>
      <p>CSCS Alps 10k+ GH200 · Exoscale GPU · Infomaniak AI · VSHN · Anexia</p>
      <footer><span class="eu-hub-cta">Jump to CH/AT →</span></footer>
    </article>
  </a>
  <a class="eu-hub-link" href="#united-kingdom-neoclouds-and-isambard-ai">
    <article class="eu-hub-card">
      <header>
        <span class="eu-hub-flag" aria-hidden="true">🇬🇧</span>
        <span class="eu-hub-title">United Kingdom</span>
        <span class="eu-hub-badge">Non-EU · NCSC · AI</span>
      </header>
      <p>Nscale Sovereign AI · Civo RelaxAI · Isambard-AI (plus CoreWeave UK L1 baseline)</p>
      <footer><span class="eu-hub-cta">Jump to UK →</span></footer>
    </article>
  </a>
</div>

| European Jurisdiction | Flagship Commercial Neoclouds (Clickable Official Links) | Sovereign Legal Tier &amp; Energy Edge | Public HPC / AI Factory Anchor | Sister Generalist Sovereign Guide |
| :--- | :--- | :--- | :--- | :--- |
| [**Netherlands &amp; Benelux** *(EU)*](#netherlands-and-benelux-neoclouds) | [**Nebius AI Cloud**](https://nebius.com), [**Leafcloud**](https://www.leaf.cloud), [**Gcore**](https://gcore.com/cloud/ai-gpu) | **L4 Dutch/LU** · EU-listed HQ (**Nebius Group N.V.**), [AMS-IX](https://www.ams-ix.net/ams) 14+ Tbps peering | [SURF Snellius](https://www.surf.nl/en/services/compute/snellius-the-national-supercomputer) / [LuxProvide MeluXina](https://www.luxprovide.lu) | [Netherlands &amp; Benelux Sovereign](/eu-cloud-benelux/) |
| [**France** *(EU)*](#france-neoclouds-and-ai-factories) | [**Scaleway AI**](https://www.scaleway.com/en/gpu-instances), [**Scaleway GenAI APIs**](https://www.scaleway.com/en/generative-apis), [**OVHcloud AI**](https://www.ovhcloud.com/en/public-cloud/ai-training), [**Mistral AI**](https://mistral.ai), [**Fluidstack FR**](https://fluidstack.io), [**DATA4**](https://www.data4group.com/en) | **L4 French/EU** · Nuclear base-load power (**EUR 0.05–0.07/kWh**) &amp; [SecNumCloud](https://cyber.gouv.fr/en/secnumcloud-for-cloud-service-providers) ecosystem | [GENCI Jean Zay](https://www.genci.fr/en) (IDRIS Saclay) + France AI Factory | [France Sovereign Cloud](/eu-cloud-france/) |
| [**Germany** *(EU)*](#germany-neoclouds-and-exascale-ai) | [**Northern Data (Taiga Cloud)**](https://www.taigacloud.com), [**IONOS AI**](https://www.ionos.com/servers/gpu-server), [**Cloud&amp;Heat**](https://www.cloudandheat.com), [**STACKIT AI**](https://stackit.com/en) | **L4 German** · **[BSI C5](https://www.bsi.bund.de/EN/Themen/Unternehmen-und-Organisationen/Informationen-und-Empfehlungen/Empfehlungen-nach-Angriffszielen/Cloud-Computing/Kriterienkatalog-C5/kriterienkatalog-c5_node.html) / ISO 27001**; strict Works Council &amp; BaFin AI governance | [FZJ JUPITER Exascale](https://www.fz-juelich.de/en/jsc/systems/supercomputers/jupiter) (~24,000 GH200) | [Germany Sovereign Cloud](/eu-cloud-germany/) |
| [**Spain** *(EU)*](#spain-liquid-cooled-ai-and-marenostrum-5) | [**Merlin-Edged**](https://edged.es), [**Stackscale**](https://www.stackscale.com), [**Arsys**](https://www.arsys.es/cloud), [**Alhambra IT**](https://alhambrait.com/en), [**Gigas**](https://gigas.com/en), [**Telefonica Tech**](https://telefonicatech.com/en) | **L4 Spanish** · **[ENS Alto](https://ens.ccn.cni.es/en)**, abundant Iberian solar PPAs + LatAm/Africa subsea edge | [BSC MareNostrum 5 &amp; AI Factory](https://www.bsc.es/research-and-development/ai-factory) | [Spain Sovereign Cloud](/eu-cloud-spain/) |
| [**Italy** *(EU)*](#italy-gpu-clouds-and-it4lia-ai-factory) | [**Seeweb**](https://www.seeweb.it/en), [**Regolo.ai**](https://regolo.ai), [**Aruba Cloud**](https://www.arubacloud.com), [**WIIT**](https://www.wiit.cloud/en) | **L4 Italian** · **[ACN QC3 / AI3](https://www.acn.gov.it/portale/en/home)** qualification &amp; national [PSN](https://www.polostrategiconazionale.it) | [EuroHPC Leonardo](https://www.eurohpc-ju.europa.eu/supercomputers/our-supercomputers_en) &amp; [DAMA Bologna IT4LIA](https://damatecnopolo.it) | [Italy Sovereign Cloud](/eu-cloud-italy/) |
| [**Nordics (FI/SE/NO/IS)** *(EU+EEA)*](#nordics-green-hydro-and-geothermal-ai-clouds) | [**Nebius Mantsala**](https://nebius.com), [**Verda (DataCrunch)**](https://verda.com), [**atNorth**](https://atnorth.com), [**Green Mountain**](https://greenmountain.no), [**Verne**](https://www.verneglobal.com), [**Bulk**](https://bulkinfrastructure.com), [**Evroc**](https://evroc.com), *([Crusoe IS](https://crusoe.ai) = L1)* | Lowest EU kWh (**hydro/geothermal EUR 0.025–0.045/kWh**) + free cold-air/district heat reuse | [CSC LUMI](https://lumi-supercomputer.eu) (Kajaani) &amp; Nordic AI Factories | [Nordics Green Cloud](/eu-cloud-nordics/) |
| [**Switzerland &amp; Austria** *(CH Non-EU + AT EU)*](#switzerland-and-austria-alpine-ai-clouds) | [**Exoscale GPU**](https://www.exoscale.com/gpu), [**Infomaniak AI**](https://www.infomaniak.com/en/hosting/public-cloud), [**VSHN**](https://www.vshn.ch/en)/[**APPUiO**](https://www.appuio.ch), [**Anexia**](https://anexia.com/en) | **Zero US CLOUD Act** · **[FINMA](https://www.finma.ch/en) / [revDSG](https://www.fedlex.admin.ch/eli/cc/2022/491/en)** banking &amp; pharma neutrality | [CSCS Alps](https://www.cscs.ch/computers/alps) (Lugano, 10,000+ GH200 GPUs) | [Switzerland &amp; Austria Sovereign](/eu-cloud-switzerland-dach/) |
| [**United Kingdom** *(Non-EU · Adequacy)*](#united-kingdom-neoclouds-and-isambard-ai) | [**Nscale**](https://nscale.com), [**Civo RelaxAI**](https://www.civo.com/ai), *([CoreWeave](https://coreweave.com) / [Lambda UK](https://lambda.ai) = L1)* | UK **[NCSC](https://www.ncsc.gov.uk/collection/cloud) / [UK GDPR](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources)** AI Growth Zones + [LINX London](https://www.linx.net) latency | [Univ. of Bristol Isambard-AI](https://docs.isambard.ac.uk) (5,448 GH200) | [United Kingdom Sovereign](/eu-cloud-uk/) |

### Netherlands and Benelux Neoclouds

- [**Nebius AI Cloud**](https://nebius.com) **(Amsterdam HQ — Europe's Flagship Listed Neocloud):** Headquartered in Amsterdam (`Nebius Group`), Nebius pairs thousands of **NVIDIA H100, H200, and Blackwell B200** GPUs connected via **3.2 Tbps [InfiniBand NDR](https://www.nvidia.com/en-us/networking/quantum2)** (clustered in **Mantsala Finland** and Paris) with [**Managed Kubernetes (MK8s)**](https://nebius.com/compute/kubernetes), managed [**Slurm**](https://slurm.schedmd.com), S3 Object Storage, shared NVMe filesystems ([docs](https://docs.nebius.com)), and an [official Terraform provider (`nebius/nebius`)](https://github.com/nebius/terraform-provider-nebius).
- [**Leafcloud**](https://www.leaf.cloud) **(Amsterdam):** Sustainable Kubernetes and [OpenStack](https://www.openstack.org) cloud placing compute and GPU servers inside urban heat networks, offsetting cooling costs and emissions for European green SaaS and Edge inference workloads.
- [**Gcore**](https://gcore.com/cloud/ai-gpu) **(Luxembourg HQ):** Specialized European edge and AI inference Neocloud ([`G-Core/gcore` Terraform](https://github.com/G-Core/terraform-provider-gcore)) delivering low-latency OpenAI-compatible open-weight inference APIs (`Everywhere Inference`) and bare-metal GPU pods across Frankfurt, Amsterdam, Luxembourg, and Madrid.
- **Sister Guide:** [Netherlands &amp; Benelux Sovereign Cloud &amp; DCs](/eu-cloud-benelux/)

### France Neoclouds and AI Factories

- [**Scaleway AI &amp; GPU Instances**](https://www.scaleway.com/en/gpu-instances) **(Iliad Group, Paris):** Europe's top developer-experience cloud for elastic AI (**L4, L40S, H100 SXM5, B200** pods), seamlessly attaching into **Kapsule / Kosmos Kubernetes**, backed by **85% [Terraform](https://github.com/scaleway/terraform-provider-scaleway) &amp; [Crossplane](https://github.com/scaleway/crossplane-provider-scaleway) maturity**, managed [`vLLM`](https://github.com/vllm-project/vllm) [**Serverless Generative APIs**](https://www.scaleway.com/en/generative-apis), and nuclear-backed Paris DC5 eco-cooling.
- [**OVHcloud AI Training &amp; Bare Metal**](https://www.ovhcloud.com/en/public-cloud/ai-training) **(Roubaix / Paris / Gravelines):** Industrial French sovereign cloud offering L40S/H100 compute integrated directly with [**OVH MKS**](https://www.ovhcloud.com/en-ie/public-cloud/kubernetes) and **zero internet egress fees**, eliminating dataset transfer shock when moving multi-terabyte multimodal data lakes across Europe.
- **Paris AI Cluster Ecosystem ([Mistral AI](https://mistral.ai), [Fluidstack FR](https://fluidstack.io), [DATA4 Paris-Saclay](https://www.data4group.com/en), [GENCI Jean Zay](https://www.genci.fr/en)):** Low-carbon nuclear grid electricity plus Paris's deep AI research talent pool make France Continental Europe's highest-density commercial + open-weight inference epicenter.
- **Sister Guide:** [France Sovereign Cloud &amp; Private DCs](/eu-cloud-france/)

### Germany Neoclouds and Exascale AI

- [**Northern Data Group &amp; Taiga Cloud**](https://www.taigacloud.com) **(Frankfurt HQ):** One of Europe's largest pure-play NVIDIA Cloud Partners operating tens of thousands of renewable-powered **H100/H200** GPUs tuned for enterprise LLM fine-tuning, life-sciences compute, and strict [GDPR](https://gdpr.eu) data processing.
- [**IONOS Cloud GPU &amp; AI Model Hub**](https://www.ionos.com/servers/gpu-server) **(Montabaur / Frankfurt / Berlin):** Combines [**BSI C5 Type 2**](https://www.bsi.bund.de/EN/Themen/Unternehmen-und-Organisationen/Informationen-und-Empfehlungen/Empfehlungen-nach-Angriffszielen/Cloud-Computing/Kriterienkatalog-C5/kriterienkatalog-c5_node.html) enterprise compliance with **H100/H200** sovereign compute and GDPR-compliant open-weight API endpoints, integrating cleanly with [**Arsys Spain**](https://www.arsys.es/cloud) and [**STACKIT**](https://stackit.com/en) German sovereign architectures.
- [**Cloud&amp;Heat Technologies**](https://www.cloudandheat.com) **(Dresden):** Direct hot-water liquid-cooled OpenStack and Kubernetes sovereign AI infrastructure capturing waste heat cleanly at minimal PUE for German industry (`Mittelstand` / automotive [`TISAX`](https://enx.com/en-US/TISAX)).
- [**JUPITER Exascale**](https://www.fz-juelich.de/en/jsc/systems/supercomputers/jupiter) **(Juelich):** Europe's first exascale AI supercomputer (~24,000 NVIDIA GH200 Grace Hopper Superchips), establishing Germany as Continental Europe's sovereign foundation-model training anchor.
- **Sister Guide:** [Germany Sovereign Cloud &amp; Private DCs](/eu-cloud-germany/)

### Spain Liquid-Cooled AI and MareNostrum 5

- [**Merlin-Edged AI Campuses**](https://edged.es) **(Madrid-Getafe, Barcelona, Bilbao-Arasur):** Zero-water, ultra-dense (**70–130+ kW/rack**) liquid-cooled colocation engineered by [**MERLIN Properties**](https://www.merlinproperties.com/en/data-centers) specifically for [**NVIDIA GB200 NVL72**](https://www.nvidia.com/en-us/data-center/gb200-nvl72) Neocloud tenants and sovereign Iberian AI deployments powered by solar/wind PPAs.
- [**Barcelona Supercomputing Center (MareNostrum 5 &amp; Barcelona AI Factory)**](https://www.bsc.es/research-and-development/ai-factory) **(Barcelona):** Hosting thousands of NVIDIA H100s alongside open European/Iberian multilingual foundation weights (**Salamandra / ALIA**), accessible to Spanish &amp; EU startups via [**EuroHPC AI Factory grants**](https://eurohpc-ju.europa.eu/ai-factories_en).
- **Sovereign Enterprise Layer ([Telefonica Tech](https://telefonicatech.com/en), [Stackscale](https://www.stackscale.com), [Arsys](https://www.arsys.es/cloud), [Gigas](https://gigas.com/en), [Alhambra IT](https://alhambrait.com/en)):** Anchor corporate [**ENS Alto**](https://ens.ccn.cni.es/en) private RAG, vector databases, and inference gateways directly inside Madrid/Barcelona Tier IV/ENS Alto facilities, bursting large training epochs into **BSC / Merlin-Edged** or EU Neocloud partners.
- **Sister Guide:** [Spain Sovereign Cloud &amp; Private DCs](/eu-cloud-spain/)

### Italy GPU Clouds and IT4LIA AI Factory

- [**Seeweb**](https://www.seeweb.it/en) **&amp;** [**Regolo.ai**](https://regolo.ai) **(Frosinone / Milan):** Pioneer Italian Cloud and Sovereign Neocloud offering bare-metal and Kubernetes **H100 / L40S / Blackwell-series** pods integrated natively with [OpenTofu](https://opentofu.org) &amp; [**SkyPilot**](https://skypilot.readthedocs.io), plus **Regolo.ai** for low-latency OpenAI-compatible European inference.
- [**Aruba Cloud**](https://www.arubacloud.com) **([`AI3 / ACN QC3`](https://www.acn.gov.it/portale/en/home), Bergamo &amp; Rome) +** [**DAMA Technopolo**](https://damatecnopolo.it) **([EuroHPC Leonardo](https://www.eurohpc-ju.europa.eu/supercomputers/our-supercomputers_en) &amp; `IT4LIA`):** Italy's flagship [Global Cloud Data Center](https://www.datacenter.it) campuses and Bologna's supercomputing hub unite public-sector ACN clearance with sovereign NVIDIA Exascale capacity, paired with [**WIIT**](https://www.wiit.cloud/en) for DORA-regulated enterprise cloud.
- **Sister Guide:** [Italy Sovereign Cloud &amp; Private DCs](/eu-cloud-italy/)

### Nordics Green Hydro and Geothermal AI Clouds

- **Nordic AI Factory Operators ([Nebius Mantsala](https://nebius.com), [Verda / DataCrunch](https://verda.com), [atNorth](https://atnorth.com), [Green Mountain](https://greenmountain.no), [Verne](https://www.verneglobal.com), [Bulk Infrastructure](https://bulkinfrastructure.com), [Evroc](https://evroc.com), [CSC LUMI](https://lumi-supercomputer.eu)):** Industrial electricity at **EUR 0.025–0.045/kWh** (2x–4x cheaper than Germany/UK), cold ambient air, and waste-heat district networks across Finland, Sweden, Norway, and Iceland give European Neoclouds an insurmountable OpEx advantage for multi-week pre-training runs. Helsinki-headquartered [**Verda**](https://verda.com) (formerly DataCrunch) complements [**Nebius**](https://nebius.com) with instant H100/H200/B200 clusters on 100% Nordic renewable energy.
- **Jurisdiction Caveat on Iceland ([Crusoe](https://crusoe.ai)):** Always verify corporate legal ownership: US-headquartered **Crusoe** builds large geothermal clusters in Iceland (**L1 European geographic residency, US corporate control**), whereas **Nebius, Verda, atNorth, Green Mountain, Verne, Bulk, Evroc, and CSC LUMI** keep ownership inside Europe.
- **Sister Guide:** [Nordics Green Cloud &amp; AI Factories](/eu-cloud-nordics/)

### Switzerland and Austria Alpine AI Clouds

- [**CSCS Alps**](https://www.cscs.ch/computers/alps) **(Lugano) +** [**Exoscale GPU**](https://www.exoscale.com/gpu) **+** [**Infomaniak AI**](https://www.infomaniak.com/en/hosting/public-cloud) **+** [**VSHN**](https://www.vshn.ch/en)/[**APPUiO**](https://www.appuio.ch) **+** [**Anexia**](https://anexia.com/en) **(AT):** For Swiss private banks ([**FINMA**](https://www.finma.ch/en)) and Basel biotech/pharma under **Zero US CLOUD Act** mandates, pairing Exoscale's Swiss GPU zones or Infomaniak Sovereign AI endpoints with VSHN APPUiO [**Red Hat OpenShift AI**](https://www.redhat.com/en/products/ai/openshift-ai) keeps weights and patient/financial RAG under Swiss [revDSG](https://www.fedlex.admin.ch/eli/cc/2022/491/en), while **Anexia** anchors Austrian EU-resident AI workloads.
- **Sister Guide:** [Switzerland &amp; Austria Sovereign Cloud](/eu-cloud-switzerland-dach/)

### United Kingdom Neoclouds and Isambard-AI

- [**Nscale**](https://nscale.com) **(London HQ) &amp;** [**Civo RelaxAI**](https://www.civo.com/ai) **+** [**Isambard-AI**](https://docs.isambard.ac.uk) **(Bristol):** Vertically integrated British-headquartered Neoclouds delivering [**NCSC**](https://www.ncsc.gov.uk/collection/cloud)-aligned sovereign H100/B200 clusters (**Nscale** across UK/Nordic green power with [`nscaledev/nscale` Terraform](https://github.com/nscaledev/terraform-provider-nscale); **Civo** sub-90s K3s/[Talos](https://www.talos.dev) sovereign pods without egress fees) alongside Britain's 5,448-GH200 national supercomputer at Bristol.
- **Post-Brexit EU vs UK Note ([CoreWeave](https://coreweave.com) &amp; [Lambda](https://lambda.ai) UK):** UK sovereign clouds (`Nscale` UK, `Civo` LON1) satisfy British **UK GDPR / G-Cloud / FCA** sovereignty (relying on conditional [EU Adequacy](https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/adequacy-decisions_en) for EU data, not EU-27-only `SecNumCloud`/`ENS`), whereas US-owned **CoreWeave** and **Lambda** UK regions are **L1 UK Data Residency** under US parent jurisdiction.
- **Sister Guide:** [United Kingdom Sovereign Cloud &amp; DCs](/eu-cloud-uk/)

### EuroHPC AI Factories and EU AI Act Positioning

!!! tip "Pre-Sales Playbook: Combining Commercial EU Neoclouds with EuroHPC AI Factories"
    Under the [**European Union's AI Factories Initiative**](https://eurohpc-ju.europa.eu/ai-factories_en) ([MareNostrum 5](https://www.bsc.es/research-and-development/ai-factory) Barcelona, [JUPITER](https://www.fz-juelich.de/en/jsc/systems/supercomputers/jupiter) Juelich, [DAMA / IT4LIA](https://damatecnopolo.it) Bologna, [LUMI](https://lumi-supercomputer.eu) Finland, [Jean Zay](https://www.genci.fr/en) France, [MeluXina](https://www.luxprovide.lu) Luxembourg), qualifying European AI startups, universities, and SMEs can apply for **non-dilutive compute grants** to train sovereign open-weight models (`EuroLLM, Salamandra, Teuken`, [Mistral](https://mistral.ai)), then seamlessly graduate production 24x7 Kubernetes serving and commercial fine-tuning onto [**Nebius**](https://nebius.com), [**Scaleway**](https://www.scaleway.com/en/gpu-instances), [**Verda**](https://verda.com), [**OVHcloud**](https://www.ovhcloud.com/en/public-cloud/ai-training), [**IONOS**](https://www.ionos.com/servers/gpu-server), [**Seeweb**](https://www.seeweb.it/en), or [**Nscale**](https://nscale.com) under [**EU AI Act**](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) lineage traceability.
""",

    "neoclouds-north-america.md": """## Pre-Sales Field Guide: North America Neoclouds (United States and Canada)

1. [Why North America Anchors Global Hyperscale GPU Capacity](#why-north-america-anchors-global-hyperscale-gpu-capacity)
2. [Comprehensive US and Canada Neocloud Pre-Sales Matrix](#comprehensive-us-and-canada-neocloud-pre-sales-matrix)
3. [Pure-Play Training vs Serverless Inference vs Energy-First Operators](#pure-play-training-vs-serverless-inference-vs-energy-first-operators)
4. [North American Cross-Border and CLOUD Act Considerations](#north-american-cross-border-and-cloud-act-considerations)

### Why North America Anchors Global Hyperscale GPU Capacity

North America concentrates the largest commercial multi-thousand-GPU [**NVIDIA Blackwell GB200 NVL72**](https://www.nvidia.com/en-us/data-center/gb200-nvl72), [**H200**](https://www.nvidia.com/en-us/data-center/h200), and [**AMD Instinct MI300X/MI325X**](https://www.amd.com/en/products/accelerators/instinct/mi300/mi300x.html) deployments worldwide, driven by:

- **Direct [NVIDIA Exemplar Partner](https://www.nvidia.com/en-us/data-center/gpu-cloud-computing/partners) Priority Allocation:** Early access to [**CoreWeave**](https://coreweave.com) and [**Lambda**](https://lambda.ai) clusters packing 10,000+ interconnected GPUs inside single non-blocking [InfiniBand](https://www.nvidia.com/en-us/networking/quantum2) fabrics months before general hyperscaler availability.
- **Low-Cost Power Corridors (`Texas ERCOT, North Dakota, Pacific Northwest Hydro, Quebec Hydro`):** Sub-**$0.04/kWh (~EUR 0.037/kWh)** industrial power attracts gigawatt-scale liquid-cooled campuses operated by [**Crusoe**](https://crusoe.ai), [**Applied Digital**](https://www.applieddigital.com), [**IREN**](https://iren.com), [**Cirrascale**](https://www.cirrascale.com), and [**QScale**](https://qscale.com).
- **Specialized AMD Instinct &amp; Compound Inference Ecosystem:** [**TensorWave**](https://tensorwave.com) pioneers pure-play AMD MI300X/MI325X high-VRAM clusters, [**Prime Intellect**](https://www.primeintellect.ai) aggregates decentralized/multi-cloud RL &amp; pre-training fabrics, while [**Together AI**](https://www.together.ai), [**Fireworks AI**](https://fireworks.ai), [**Baseten**](https://www.baseten.co), [**Modal**](https://modal.com), and [**RunPod**](https://www.runpod.io) compress per-token serving costs via custom CUDA/[SGLang](https://github.com/sgl-project/sglang)/[TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) engines.

### Comprehensive US and Canada Neocloud Pre-Sales Matrix

| Provider (Clickable) | HQ &amp; Primary Footprints | Accelerator Lineup | Fabric &amp; Orchestration Stack | Indicative 2026 Rate (`USD / GPU-hr` &amp; `EUR eq.`) | IaC &amp; Automation Maturity | Optimal Pre-Sales Fit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [**CoreWeave**](https://coreweave.com) | Livingston NJ (US); 30+ DCs (US, UK, EU) | **H100, H200, B200, [GB200 NVL72](https://www.nvidia.com/en-us/data-center/gb200-nvl72)** | **3.2 Tbps [Quantum-2](https://www.nvidia.com/en-us/networking/quantum2)/X800 IB**, [CKS Docs](https://docs.coreweave.com), [**SUNK (Slurm on K8s)**](https://github.com/coreweave/sunk-anywhere), [WEKA](https://docs.weka.io)/[VAST](https://www.vastdata.com) | **$2.25 – $4.95+** *(EUR 2.07 – 4.55+)* via reserved contracts | **~75%** (CKS/[OpenTofu](https://opentofu.org) + [SUNK](https://github.com/coreweave/sunk-anywhere) &amp; [Tensorizer](https://github.com/coreweave/tensorizer)) | **Frontier/enterprise multi-node pre-training** requiring [ClusterMAX](https://www.clustermax.ai) Platinum-grade RDMA efficiency &amp; automated XID self-healing |
| [**Lambda**](https://lambda.ai) | San Jose CA (US); Texas, Utah, Illinois, UK | **H100, H200, B200 / GB200**, 1-Click Clusters | **3.2 Tbps Quantum-2 InfiniBand**, Bare Metal / [Lambda Docs](https://docs.lambda.ai) + [Slurm](https://slurm.schedmd.com) | **$2.49 – $3.49** *(EUR 2.29 – 3.21)* | **~60%** (Cloud API, [SkyPilot](https://skypilot.readthedocs.io), [Ansible](https://docs.ansible.com)/Slurm) | Fast engineering teams wanting **turnkey [PyTorch](https://pytorch.org)/InfiniBand clusters** without hyperscaler approval friction |
| [**Crusoe Cloud**](https://crusoe.ai) | Denver CO (US); Abilene TX Mega-Campuses, ND, WY, Iceland | **H100, H200, GB200, [AMD MI300X](https://www.amd.com/en/products/accelerators/instinct/mi300/mi300x.html)** | **InfiniBand NDR**, [Crusoe Docs](https://docs.crusoe.ai), Managed K8s &amp; Slurm on green/stranded energy | **$1.95 – $3.40** *(EUR 1.79 – 3.13)* | **~70%** ([`crusoecloud/crusoe`](https://github.com/crusoecloud/terraform-provider-crusoe) Terraform, CLI, [SkyPilot](https://skypilot.readthedocs.io)) | ESG-conscious enterprises &amp; mega-cluster labs (**Stargate/Abilene ecosystem**) prioritizing clean-energy TCO |
| [**TensorWave**](https://tensorwave.com) | Las Vegas NV (US) | **[AMD Instinct MI300X](https://www.amd.com/en/products/accelerators/instinct/mi300/mi300x.html) (192 GB) &amp; MI325X (256 GB)** | High-speed 400G RoCEv2/IB, MK8s / [Slurm](https://slurm.schedmd.com) / [**ROCm 6+**](https://rocm.docs.amd.com) / [vLLM](https://github.com/vllm-project/vllm) | **$1.58 – $2.45** *(EUR 1.45 – 2.25)* | **~60%** (K8s, Slurm, ROCm containers) | **70B–405B inference &amp; long-context RAG** maximizing VRAM/EUR and diversifying away from single-vendor CUDA lock-in |
| [**Voltage Park**](https://voltagepark.com) &amp; [**Prime Intellect**](https://www.primeintellect.ai) | Seattle / Palo Alto / San Francisco (US); TX, VA, WA | **NVIDIA H100 / H200 / B200** bare-metal &amp; federated RL fabrics | InfiniBand NDR, Bare-Metal, Kubernetes, distributed RL training orchestration | **$1.85 – $2.49** *(EUR 1.70 – 2.29)* | **~55–65%** (REST APIs, K8s bootstrapping, distributed RL SDKs) | Cost-sensitive training, synthetic reasoning RL, and fine-tuning teams demanding **flat transparent pricing** |
| [**Together AI**](https://www.together.ai) &amp; [**Fireworks AI**](https://fireworks.ai) | San Francisco &amp; Redwood City CA (US) | **H100, H200, B200** + Compound Serverless Engines | FlashAttention / FireAttention FP8/FP4 kernels ([Fireworks Docs](https://docs.fireworks.ai)), Dedicated + Serverless APIs | **$1.95 – $3.00** *(EUR 1.79 – 2.76)* + per-token | **~65%** (OpenAI-compatible SDKs, LoRA fine-tuning, Dedicated Endpoints) | AI product teams wanting **sub-second TTFT agentic JSON/function-calling + autoscaled custom-weight serving** |
| [**Baseten**](https://www.baseten.co) &amp; [**Modal**](https://modal.com) | San Francisco &amp; New York (US); multi-cloud/dedicated pods | **H100, H200, B200, L40S, A100** serverless GPU runtimes | Python-native serverless containers (`Modal`), [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) Truss chains (`Baseten`), sub-second cold boot | Per-second GPU / dedicated reservation | **~75%** (Declarative Python-as-Code CI/CD + multi-region autoscale) | **Bursty multimodal, voice/video, and custom Python ML pipelines** scaling from `0` to `100+` GPUs in seconds |
| [**IREN**](https://iren.com) · [**Applied Digital**](https://www.applieddigital.com) · [**Cirrascale**](https://www.cirrascale.com) | Texas, British Columbia, North Dakota, San Diego | High-density liquid-cooled **H100/H200/Blackwell** &amp; custom AI racks | Direct-to-chip DLC, InfiniBand pods on 100% renewable / cold-climate grid power | Wholesale / Contracted cluster pricing | **~50–60%** (Bare-metal cluster, [Slurm](https://slurm.schedmd.com) &amp; Colo-plus-Cloud) | **10–100 MW single-tenant AI factories** avoiding slow hyperscaler DC delivery queues |
| [**Fluidstack**](https://fluidstack.io) **/** [**Hyperstack**](https://www.hyperstack.cloud) | NY / London / Toronto | **H100, A100, L40S, B200** | Bare-metal/VM GPU clusters ([Fluidstack Eng](https://engineering.fluidstack.com)), fast NVMe hibernation | **$1.90 – $2.65** *(EUR 1.75 – 2.44)* | **~65%** (API, [OpenTofu](https://opentofu.org)/[SkyPilot](https://skypilot.readthedocs.io)) | Rapid burst clusters across **North America + Europe/Canada** with single billing |
| [**Vultr Cloud GPU**](https://docs.vultr.com/products/compute/instances/cloud-gpu) **&amp;** [**DigitalOcean**](https://www.digitalocean.com/products/gpu-droplets) | Global US/CA/EU/APAC regions | **H100, A100, L40S, AMD MI300X** (`Vultr`) | Cloud VMs, Bare Metal, Managed Kubernetes (`VKE`/`DOKS`), included bandwidth pools | **$2.15 – $2.99** *(EUR 1.98 – 2.75)* | **~80%** ([`vultr`](https://github.com/vultr/terraform-provider-vultr) &amp; [`digitalocean`](https://github.com/digitalocean/terraform-provider-digitalocean) Official Terraform) | Teams valuing **standard DevOps Terraform maturity** + global regional inference latency over massive IB clusters |
| [**RunPod**](https://www.runpod.io) | Mount Laurel NJ (US); 30+ global Secure Cloud DCs | **H100, H200, B200, L40S, RTX 4090/5090** | Secure Cloud container pods, **Serverless [vLLM](https://github.com/vllm-project/vllm) FlashBoot**, Network NVMe Volumes | **$1.99 – $2.89** *(EUR 1.83 – 2.66)* for H100 | **~70%** ([`runpod/runpod` Official Terraform](https://github.com/runpod/terraform-provider-runpod) + [SkyPilot](https://skypilot.readthedocs.io)) | Fast developer iteration, CI GPU runners, and **cold-start-sensitive autoscale inference** |
| [**QScale**](https://qscale.com) &amp; [**Cohere**](https://cohere.com) **(Canada)** | Levis Quebec &amp; Toronto (Canada) | High-density **Quebec Hydro AI Campuses** (`QScale`) + **Enterprise Sovereign LLMs/RAG** (`Cohere`) | Liquid-cooled zero-water campuses powered by **100% Quebec Hydro** + private VPC/on-prem Command models | Enterprise wholesale / Sovereign licensing | Colocation / Sovereign Partner APIs &amp; K8s Helm charts | **Canadian &amp; [PIPEDA](https://www.priv.gc.ca/en/privacy-topics/privacy-laws-in-canada/the-personal-information-protection-and-electronic-documents-act-pipeda)/Quebec Law 25 sovereign AI** outside US territory |

### Pure-Play Training vs Serverless Inference vs Energy-First Operators

1. **Multi-Node Model Training (`&gt; 32 GPUs`):** Eliminate VM providers lacking non-blocking [InfiniBand](https://www.nvidia.com/en-us/networking/quantum2) or [Spectrum-X](https://www.nvidia.com/en-us/networking/spectrumx) RoCEv2 RDMA (`3.2+ Tbps` per 8-GPU node). Standardize shortlist on [**CoreWeave**](https://coreweave.com), [**Crusoe**](https://crusoe.ai), [**Lambda**](https://lambda.ai), [**TensorWave**](https://tensorwave.com), [**Voltage Park**](https://voltagepark.com), or [**Nebius US**](https://nebius.com) (**Kansas City / New Jersey**).
2. **Low-Latency Serverless &amp; Bursty Inference:** Standardize on [**Together AI**](https://www.together.ai), [**Fireworks AI**](https://fireworks.ai), [**Baseten**](https://www.baseten.co), [**Modal**](https://modal.com), or [**RunPod Serverless**](https://www.runpod.io), using [**LiteLLM**](https://github.com/BerriAI/litellm) or [**Gateway API Inference Extension**](https://github.com/kubernetes-sigs/gateway-api-inference-extension) to route seamlessly across regions.
3. **High-VRAM Inference Economics (AMD vs NVIDIA):** Whenever a **Llama-3.3 70B / Llama-4 / Qwen 72B+** or long-context coding model spills across multiple H100s purely due to KV-cache memory, **8x [AMD MI300X/MI325X](https://www.amd.com/en/products/accelerators/instinct/mi300/mi300x.html) on [TensorWave](https://tensorwave.com) or [Vultr](https://docs.vultr.com/products/compute/instances/cloud-gpu)** cuts total node count in half by fitting massive weights + KV cache into **1.5–2.0 TB unified HBM3e**.

### North American Cross-Border and CLOUD Act Considerations

!!! warning "Pre-Sales Advisory for European &amp; Canadian Clients Deploying in US Neoclouds"
    - **US CLOUD Act Exposure:** Every US-headquartered Neocloud ([CoreWeave](https://coreweave.com), [Lambda](https://lambda.ai), [Crusoe](https://crusoe.ai), [Together](https://www.together.ai), [Fireworks](https://fireworks.ai), [Baseten](https://www.baseten.co), [Modal](https://modal.com), [RunPod](https://www.runpod.io), [Vultr](https://docs.vultr.com/products/compute/instances/cloud-gpu)) falls under **US federal jurisdiction**, even when hosting servers inside Canada, Iceland, or London. Regulated EU financial/healthcare clients MUST restrict those deployments strictly to **anonymized/public training datasets or Level-1 workloads** (see [European Sovereign Cloud](/eu-sovereign-cloud/)).
    - **Quebec &amp; Canadian Sovereignty ([`PIPEDA`](https://www.priv.gc.ca/en/privacy-topics/privacy-laws-in-canada/the-personal-information-protection-and-electronic-documents-act-pipeda) / `Quebec Law 25`):** Canadian public bodies, banks, and AI startups sensitive to US subpoenas should prioritize Canadian-owned hydro campuses ([**QScale Quebec**](https://qscale.com)) and Canadian model stacks ([**Cohere**](https://cohere.com)) rather than defaulting to `AWS us-east-1`.
""",

    "neoclouds-apac.md": """## Pre-Sales Field Guide: Asia-Pacific Neoclouds and AI Clouds

1. [Strategic Drivers of Asia-Pacific Sovereign Neoclouds](#strategic-drivers-of-asia-pacific-sovereign-neoclouds)
2. [Comprehensive APAC Neocloud Pre-Sales Matrix](#comprehensive-apac-neocloud-pre-sales-matrix)
3. [Japan, India, ASEAN/Australia and South Korea Playbooks](#japan-india-aseanaustralia-and-south-korea-playbooks)

### Strategic Drivers of Asia-Pacific Sovereign Neoclouds

Asia-Pacific exhibits the strongest **public-private Sovereign AI industrial policy** outside Europe and the Gulf:

- **Japan (`METI Economic Security Cloud Subsidies` &amp; [APPI](https://www.ppc.go.jp/en)):** Tokyo subsidizes domestic cloud compute through [**Sakura Internet**](https://www.sakura.ad.jp) (`Koukaryoku`), [**SoftBank**](https://www.softbank.jp/en) (`Infrinia / GB200`), [**Preferred Networks**](https://preferred.jp/en), and [**GMO Internet**](https://www.gmo.jp/en) to eliminate total dependence on US clouds under Japan's [**Personal Information Protection Commission (`APPI`)**](https://www.ppc.go.jp/en) framework.
- **India ([IndiaAI Mission](https://indiaai.gov.in) &amp; [MeitY](https://www.meity.gov.in) 18,000+ GPU Empanelment):** Government-subsidized hourly rates drive rapid expansion across [**Yotta Shakti Cloud**](https://shakticloud.ai), [**Neysa**](https://neysa.ai), [**E2E Networks**](https://www.e2enetworks.com), [**Sify Technologies**](https://www.sifytechnologies.com), and [**Tata Communications**](https://www.tatacommunications.com) under India's **Digital Personal Data Protection (DPDP) Act**.
- **Singapore &amp; Australia (`Tropical Liquid Immersion + Hydro`):** [**Firmus**](https://firmus.co) / [**Sustainable Metal Cloud (SMC)**](https://smc.co) slashes cooling electricity by up to 50% using closed-loop **HyperCube total liquid immersion**, linking [**MAS TRM**](https://www.mas.gov.sg/regulation/guidelines/technology-risk-management-guidelines)-regulated Singapore latency ([**Singtel RE:AI**](https://re-ai.ai)) with 100% hydroelectric Tasmanian compute and [**Australian ISM / IRAP**](https://www.cyber.gov.au/ism)-ready [**NEXTDC**](https://www.nextdc.com) and [**Macquarie Data Centres**](https://macquariedatacentres.com) campuses.

### Comprehensive APAC Neocloud Pre-Sales Matrix

| Provider (Clickable) | Country &amp; Core Campuses | Accelerator &amp; Cooling Architecture | Compliance &amp; Sovereign Status | Orchestration &amp; IaC Stack | Pre-Sales Sweet Spot |
| :--- | :--- | :--- | :--- | :--- | :--- |
| [**Sakura Internet**](https://www.sakura.ad.jp) (`Koukaryoku`) | **Japan** (Ishikari Hokkaido clean-energy DCs) | Thousands of [**NVIDIA H100**](https://www.nvidia.com/en-us/data-center/h100) / [**H200**](https://www.nvidia.com/en-us/data-center/h200) / **B200** GPUs; container cold-climate cooling | **100% Japanese Sovereign** · METI Economic Security Certified · [APPI](https://www.ppc.go.jp/en) compliant | Bare Metal, Managed Compute, [Slurm](https://slurm.schedmd.com) / Kubernetes AI containers | Japanese LLM pre-training, Tokyo financial/manufacturing sovereign AI |
| [**SoftBank**](https://www.softbank.jp/en) Sovereign AI &amp; AI-RAN | **Japan** (Hokkaido/Tomakomai &amp; Sakai mega AI DCs) | **NVIDIA DGX SuperPOD &amp; [GB200 NVL72](https://www.nvidia.com/en-us/data-center/gb200-nvl72)** factories + Infrinia AI Cloud OS | **Japanese Telco Sovereign** · Japanese Govt backed | Kubernetes-as-a-Service + Inference-as-a-Service (`Infrinia`) | National-scale Japanese telecom, robotics, and multimodal foundation training |
| [**Preferred Networks**](https://preferred.jp/en) &amp; [**GMO**](https://www.gmo.jp/en) | **Japan** (Tokyo / domestic campuses) | Custom **MN-Core2/3 ASIC** supercomputers ([`PFN`](https://preferred.jp/en)) + **NVIDIA H200** ([`GMO`](https://www.gmo.jp/en)) | **Japanese Domestic Legal Ownership** · [APPI](https://www.ppc.go.jp/en) | [PyTorch](https://pytorch.org) compiler stacks (`MN-Core`), enterprise Japanese managed GPUs | Ultra-efficient Japanese frontier research + localized enterprise GPUaaS |
| [**Yotta Shakti Cloud**](https://shakticloud.ai) | **India** (Navi Mumbai NM1, Greater Noida D1) | Large-scale **NVIDIA H100 / B200** liquid-cooled [InfiniBand](https://www.nvidia.com/en-us/networking/quantum2) clusters | **Indian Sovereign (L4)** · [IndiaAI](https://indiaai.gov.in) Empaneled · **DPDP / [MeitY](https://www.meity.gov.in)** | Kubernetes, [Slurm](https://slurm.schedmd.com), Managed InfiniBand clusters, AI Labs PaaS | Large-scale Indic sovereign models, banking RAG, and hyperscale public sector India workloads |
| [**Neysa**](https://neysa.ai) (`Velocis`) | **India** (Mumbai &amp; pan-India / emerging PoPs) | **NVIDIA InfiniBand GPU Clusters** + modular AI acceleration pods | **Indian Headquartered** · [IndiaAI](https://indiaai.gov.in) Empaneled | End-to-end **Velocis** MLOps, Kubernetes orchestration, GPU observability | Enterprises wanting **managed full-lifecycle MLOps + India local billing** |
| [**E2E Networks**](https://www.e2enetworks.com) &amp; [**Sify**](https://www.sifytechnologies.com) | **India** (Delhi NCR / Noida, Mumbai, Chennai, Bangalore) | **NVIDIA H100 / H200 InfiniBand** (`E2E TIR`) &amp; liquid-cooled DGX-ready campuses (`Sify`) | **Indian Sovereign / Listed** · [MeitY](https://www.meity.gov.in)/[IndiaAI](https://indiaai.gov.in) Empaneled | **TIR AI Platform**, Kubernetes, [OpenTofu](https://opentofu.org)/API, plus [**Tata Communications**](https://www.tatacommunications.com) fabric | Startups, SaaS, and enterprises avoiding hyperscaler INR billing shock |
| [**Firmus**](https://firmus.co) &amp; [**Sustainable Metal Cloud (`SMC`)**](https://smc.co) | **Singapore &amp; Australia (Tasmania)** | **HyperCube Total Liquid Immersion** (**H100 / B200 / [GB200](https://www.nvidia.com/en-us/data-center/gb200-nvl72)**), ultra-low PUE | Singapore &amp; Australian corporate entities; **100% hydro power (Tasmania)** | Managed Bare-Metal K8s / [Slurm](https://slurm.schedmd.com) clusters + [InfiniBand NDR](https://www.nvidia.com/en-us/networking/quantum2) | High-sustainability APAC training &amp; lowest net energy-per-FLOP in SE Asia/Oceania |
| [**Singtel `RE:AI`**](https://re-ai.ai) (Nxera) | **Singapore, Thailand, Indonesia (`ASEAN`)** | **NVIDIA DGX/H100/Blackwell** inside sustainable **Nxera** AI campuses | **ASEAN Sovereign Telco Cloud** ([**MAS TRM**](https://www.mas.gov.sg/regulation/guidelines/technology-risk-management-guidelines) / PDPA aligned) | **Singtel Paragon** multi-cloud orchestration, GPUaaS, Token-as-a-Service | Regulated **ASEAN banks, telcos, and smart-nation workloads** across Singapore/Jakarta/Bangkok |
| [**NEXTDC**](https://www.nextdc.com) · [**Macquarie**](https://macquariedatacentres.com) · [**ResetData**](https://resetdata.com.au) | **Australia** (Sydney S3/S4/IC3, Canberra, Melbourne M3/M4) | **NVIDIA DGX-ready** direct liquid cooling &amp; CBD immersion pods ([`ResetData`](https://resetdata.com.au)) | **Australian [ISM / IRAP PROTECTED](https://www.cyber.gov.au/ism)** sovereign facilities | Cross-connect cloud fabric + Bare-Metal/Private K8s sovereign AI stacks | Australian defence, federal government (`IRAP`), and low-latency ASX financial inference |
| [**NAVER Cloud**](https://www.ncloud.com) ([Corp](https://www.navercorp.com/en)) &amp; [**NHN Cloud**](https://www.nhncloud.com) | **South Korea** (Sejong City `GAK`, Gwangju National AI DC) | Multi-thousand-GPU national AI clusters | **CSAP South Korean Public Cloud Certified** | Kubernetes, HyperCLOVA enterprise AI pipelines, domestic MLOps | South Korean regulated public sector, healthcare, and Korean-sovereign RAG |
| [**YTL Power Green AI**](https://www.ytlpowerinternational.com) (Johor) | **Malaysia** (Johor 500 MW Solar Park adjacent to Singapore) | Utility-scale solar-powered **NVIDIA GB200 / Blackwell** hyperscale campus | Cross-Strait Johor-Singapore Special Economic Zone spillover | Dedicated wholesale AI campuses for Asian hyperscale/Neocloud tenants | Low-latency **Singapore inference spillover** where island grid/land constraints block 100+ MW builds |

### Japan, India, ASEAN/Australia and South Korea Playbooks

1. **Japan Public-Sector / Automotive AI:** Anchor training in [**Sakura Internet**](https://www.sakura.ad.jp) (`Koukaryoku` Hokkaido), [**SoftBank**](https://www.softbank.jp/en), or [**GMO GPU Cloud**](https://www.gmo.jp/en) to qualify for domestic Japanese security/METI and [**APPI**](https://www.ppc.go.jp/en) baselines without exposing weights to foreign jurisdictions.
2. **India FinTech &amp; Sovereign Indic LLMs:** Leverage [**IndiaAI Mission**](https://indiaai.gov.in) empanelment via [**Yotta Shakti Cloud**](https://shakticloud.ai), [**E2E Networks**](https://www.e2enetworks.com), [**Neysa**](https://neysa.ai), or [**Sify**](https://www.sifytechnologies.com) for transparent INR economics and **RBI / [MeitY](https://www.meity.gov.in) DPDP Act** data localization.
3. **Singapore-to-Australia Green AI Arbitrage:** Place latency-sensitive inference &amp; [**MAS TRM**](https://www.mas.gov.sg/regulation/guidelines/technology-risk-management-guidelines)-regulated RAG inside [**Singtel RE:AI**](https://re-ai.ai) (Singapore) or [**NEXTDC**](https://www.nextdc.com)/[**Macquarie**](https://macquariedatacentres.com) (Sydney/Canberra [IRAP](https://www.cyber.gov.au/ism)) while batch-training checkpoints over submarine links in Tasmanian 100% hydro [**Firmus**](https://firmus.co)/[**SMC**](https://smc.co) immersion pods.
""",

    "neoclouds-mena.md": """## Pre-Sales Field Guide: Middle East and GCC Sovereign AI Factories

1. [Why the Gulf Is Building Gigawatt-Scale Sovereign AI Factories](#why-the-gulf-is-building-gigawatt-scale-sovereign-ai-factories)
2. [Comprehensive MENA and GCC AI Cloud Pre-Sales Matrix](#comprehensive-mena-and-gcc-ai-cloud-pre-sales-matrix)
3. [Export Governance, Data Residency and EMEA Latency Arbitrage](#export-governance-data-residency-and-emea-latency-arbitrage)
4. [MENA Enterprise and Sovereign Public-Sector Playbooks](#mena-enterprise-and-sovereign-public-sector-playbooks)

### Why the Gulf Is Building Gigawatt-Scale Sovereign AI Factories

Backed by sovereign wealth capital and abundant utility-scale energy (**solar + nuclear + natural gas**) across the **UAE, Saudi Arabia, and Qatar**, the GCC has transformed from a regional cloud consumer into one of the world's most ambitious builders of **national AI Factories**:

- **Sovereign Non-Hyperscaler Silicon Diversity:** [**Core42**](https://www.core42.ai) / [**G42**](https://www.g42.ai) pairs ultra-large [**Cerebras Wafer-Scale Engine (`Condor Galaxy`)**](https://www.cerebras.ai) clusters with [**NVIDIA H100**](https://www.nvidia.com/en-us/data-center/h100)/[**GB200**](https://www.nvidia.com/en-us/data-center/gb200-nvl72) infrastructure in Abu Dhabi, while [**HUMAIN**](https://www.humain.com), [**center3**](https://www.center3.com), [**Aramco Digital**](https://www.aramcodigital.com), and [**Ooredoo**](https://www.ooredoo.com) build nationwide [**NVIDIA Cloud Partner**](https://www.nvidia.com/en-us/data-center/gpu-cloud-computing/partners) footprints.
- **Arabic Sovereign Frontier Models ([TII Falcon](https://github.com/tiiuae), [SDAIA ALLAM](https://sdaia.gov.sa/en), [Inception Jais](https://huggingface.co/inceptionai)):** Trillion-token sovereign models trained domestically inside the UAE and Saudi Arabia establish turnkey Arabic-English enterprise AI baselines.
- **Subsea Crossroads (Europe–Africa–India–Asia):** Landing corridors through **Fujairah, Jeddah, and Doha** connect [**Marseille**](https://www.digitalrealty.com/data-centers/emea/marseille) European hubs, African fintechs, and South Asian enterprises directly into low-cost GCC solar/nuclear AI compute ([**Moro Hub**](https://www.morohub.com), [**Khazna**](https://khaznadatacenters.com)).

### Comprehensive MENA and GCC AI Cloud Pre-Sales Matrix

| Provider / Operator (Clickable) | Country &amp; Primary Campuses | AI Compute &amp; Silicon Architecture | Sovereignty &amp; Compliance Regimes | Platform Stack &amp; Ecosystem | Optimal Pre-Sales Fit |
| :--- | :--- | :--- | :--- | :--- | :--- |
| [**Core42**](https://www.core42.ai) ([**`G42` Group**](https://www.g42.ai)) | **UAE** (Abu Dhabi, Dubai — hosted inside [**Khazna**](https://khaznadatacenters.com)) | [**Cerebras WSE (`Condor Galaxy`)**](https://www.cerebras.ai) + massive **NVIDIA GPU** pods + Sovereign [Azure](https://azure.microsoft.com) integration | **L4 UAE Sovereign** · UAE IAS / NESA national clearance &amp; health data residency | **Compass API**, Compass Vector/Inference, Sovereign Cloud &amp; [**Jais**](https://huggingface.co/inceptionai) / [**Falcon**](https://github.com/tiiuae) hosting | UAE government ministries, ADNOC/energy AI, genomics, and Middle East healthcare requiring ultra-fast Cerebras/NVIDIA inference |
| [**Khazna Data Centers**](https://khaznadatacenters.com) &amp; [**Moro Hub (DEWA)**](https://www.morohub.com) | **UAE &amp; MENA Expansion** (Abu Dhabi Masdar, Dubai Solar Park) | Wholesale **100+ MW liquid-cooled hyperscale AI campuses** &amp; solar-powered Tier III+ green halls (`Moro Hub`) | Tier III+ carrier-neutral UAE sovereign physical perimeter | Dedicated customer AI halls, [**OpenShift**](https://www.redhat.com/en/products/ai/openshift-ai)/K8s sovereign private clouds &amp; cloud interconnects | High-density single-tenant enterprise cages, ESG solar mandates &amp; national sovereign Neocloud expansion |
| [**HUMAIN**](https://www.humain.com) (PIF Saudi AI Champion) | **Saudi Arabia** (Riyadh / NEOM / Red Sea mega-hubs) | Multi-hundred-MW [**NVIDIA GB200 NVL72**](https://www.nvidia.com/en-us/data-center/gb200-nvl72) &amp; specialized AI partner infrastructure | **100% Saudi PIF Sovereign** · [**SDAIA**](https://sdaia.gov.sa/en) / [**Saudi NCA**](https://nca.gov.sa/en) ECC &amp; CCC alignment | Full-stack national AI factories, **ALLAM** Arabic models, regional inference APIs | Saudi Vision 2030 giga-projects, financial banking AI, and Arabic enterprise automation |
| [**center3 (`STC`)**](https://www.center3.com) **&amp;** [**Aramco Digital**](https://www.aramcodigital.com) | **Saudi Arabia** (Riyadh, Jeddah, Dammam) | Liquid-cooled AI-ready DCs + industrial sovereign edge/core compute | **[Saudi NCA](https://nca.gov.sa/en) Critical Controls** · strict in-Kingdom PDPL localization | Carrier-neutral subsea IXP hubs (`2Africa`, Blue-Raman) + industrial AI digital twins | **Energy, petrochemicals, telecom, and public-sector AI** demanding non-negotiable in-Kingdom custody |
| [**Ooredoo NCP**](https://www.ooredoo.com) | **Qatar, Oman, Kuwait, Iraq, Tunisia** | Distributed regional **NVIDIA H100/H200/Blackwell** telco AI clusters | Local national residency inside each **MENA jurisdiction** | Telecom-hosted GPUaaS, sovereign [**NVIDIA NIM**](https://www.nvidia.com/en-us/ai) microservices, [vLLM](https://github.com/vllm-project/vllm) API gateways | Multi-country MENA banks &amp; oil/gas firms needing in-country GPU compliance outside US regions |
| [**MEEZA**](https://www.meeza.net) (`M-VAULT` Doha) | **Qatar** (Doha Knowledge Village &amp; M-VAULT 1–5) | Enterprise cloud, high-density Tier III+ private halls, managed AI/security | **Qatari Sovereign** · NCSA Qatar compliance, ISO 27001/27017 | Managed VMware/[OpenShift](https://www.redhat.com/en/technologies/cloud-computing/openshift/virtualization)/Kubernetes + local Qatari SOC | Qatari financial, logistics, and government workloads requiring Tier III+ domestic isolation |

### Export Governance, Data Residency and EMEA Latency Arbitrage

!!! info "Pre-Sales Compliance Reality Check for GCC AI Projects"
    1. **Jurisdictional Data Rules (`UAE PDPL` / `Saudi PDPL` / [Saudi NCA Cloud Cybersecurity Controls](https://nca.gov.sa/en)):** Saudi **NCA CCC** and **UAE healthcare/defense mandates** explicitly require primary data, telemetry logs, and model fine-tuning checkpoints to remain physically inside national borders under domestic legal oversight.
    2. **Semiconductor Export &amp; Supply Chain Vetting:** When scoping **&gt;1,000-GPU training clusters** in MENA, confirm US BIS / verified [**NVIDIA Cloud Partner**](https://www.nvidia.com/en-us/data-center/gpu-cloud-computing/partners) allocation lead times upfront and verify whether workload pipelines require clean separation between US partner cloud tenants and domestic sovereign fabrics ([**Core42**](https://www.core42.ai) / [**HUMAIN**](https://www.humain.com)).

### MENA Enterprise and Sovereign Public-Sector Playbooks

1. **Saudi Regulated Banking &amp; Energy AI (`NCA CCC` + `PDPL`):** Deploy in-Kingdom [**vLLM**](https://github.com/vllm-project/vllm) / [**Red Hat OpenShift AI**](https://www.redhat.com/en/products/ai/openshift-ai) inference and Arabic **ALLAM** RAG inside [**HUMAIN**](https://www.humain.com), [**center3**](https://www.center3.com), or [**Aramco Digital**](https://www.aramcodigital.com) Riyadh/Dammam halls with zero cross-border prompt egress.
2. **UAE Government, Healthcare &amp; High-Speed Arabic Inference:** Pair [**Core42**](https://www.core42.ai) Compass APIs ([**Jais**](https://huggingface.co/inceptionai) / [**TII Falcon**](https://github.com/tiiuae) on [**Cerebras**](https://www.cerebras.ai) &amp; NVIDIA pods) with dedicated sovereign cages in [**Khazna**](https://khaznadatacenters.com) or 100% solar [**Moro Hub**](https://www.morohub.com).
3. **Multi-Country Gulf Telecom &amp; Financial Footprint (`Qatar / Oman / Kuwait`):** Standardize portable Kubernetes + [**OpenTofu**](https://opentofu.org) + [**LiteLLM**](https://github.com/BerriAI/litellm) deployments across [**Ooredoo NCP**](https://www.ooredoo.com) and [**MEEZA**](https://www.meeza.net) Doha (`M-VAULT`), keeping each subsidiary's customer PII strictly inside its national regulator's perimeter.
""",

    "neoclouds-latam-africa.md": """## Pre-Sales Field Guide: Latin America and Africa AI Cloud Hubs

1. [Renewable Power Economics and Regional Sovereignty in the Global South](#renewable-power-economics-and-regional-sovereignty-in-the-global-south)
2. [Comprehensive Latin America and Africa AI Cloud Matrix](#comprehensive-latin-america-and-africa-ai-cloud-matrix)
3. [Pre-Sales Design Rules for LatAm and Africa AI Workloads](#pre-sales-design-rules-for-latam-and-africa-ai-workloads)

### Renewable Power Economics and Regional Sovereignty in the Global South

Enterprise AI deployments across **Latin America** and **Africa** historically endured **120–180 ms round-trip latency** and expensive USD currency exposure backhauling every token to `us-east-1` or `eu-west-1`. Two structural shifts now reshape pre-sales architecture in both continents:

- **Latin America's Clean-Energy &amp; Subsea AI Corridors (`Brazil, Chile, Mexico, Colombia`):** Brazil's **85%+ hydro/wind/solar grid** + [**IX.br**](https://ix.br) paired with direct South Atlantic fiber to Iberia (`Fortaleza–Lisbon–Madrid`) turns [**ODATA**](https://odatadc.com), [**Scala**](https://scaladatacenters.com), [**Elea AI City**](https://eleadatacenters.com), [**Magalu Cloud**](https://magalu.cloud), [**Ascenty**](https://ascenty.com), [**SONDA**](https://www.sonda.com), and [**KIO**](https://www.kio.tech/en) into high-density AI powerhouses under **LGPD** sovereignty.
- **Africa's First Continental NVIDIA AI Factories ([Cassava Technologies](https://www.cassavatechnologies.com) &amp; [Cassava AI](https://www.cassava.ai)):** Rather than shipping African financial, telco, medical, and agricultural datasets overseas, [**Cassava AI**](https://www.cassava.ai) + [**Africa Data Centres**](https://www.africadatacentres.com), [**Teraco**](https://www.teraco.co.za), and [**Raxio**](https://raxiogroup.com) deploy liquid-cooled GPU and edge inference capacity across **South Africa, Kenya (geothermal), Nigeria, Egypt, and Morocco** tied directly into the [**Liquid Intelligent Technologies**](https://liquid.tech) **110,000+ km fiber spine**.

### Comprehensive Latin America and Africa AI Cloud Matrix

| Operator / Platform (Clickable) | Continental Footprint | AI Infrastructure &amp; Cooling | Regulatory &amp; Power Advantage | Connectivity &amp; Stack Integration | Optimal Pre-Sales Fit |
| :--- | :--- | :--- | :--- | :--- | :--- |
| [**ODATA**](https://odatadc.com) (`Aligned Data Centers`) | **Brazil (SP/RJ), Mexico (Queretaro), Chile (Santiago), Colombia** | **Delta Cube** high-density liquid/air hybrid cooling ready for **AI Neocloud deployments** | **100% certified renewable PPAs** + **LGPD / LFPDPPP** local hosting | Major cloud/GPU tenant campuses directly wired into regional metro fiber rings | Hyperscale &amp; enterprise AI tenant halls needing uniform SLA across **4 largest LatAm economies** |
| [**Elea Data Centers**](https://eleadatacenters.com) (`Rio AI City`) | **Brazil** (Rio de Janeiro, Sao Paulo, Brasilia, Porto Alegre, Curitiba) | Sustainable multi-campus **Rio AI City** project scaling clean-power AI capacity | **100% Brazilian hydro renewable power**; Tier III+ financial compliance | Edge-to-core national Brazilian footprint + [**IX.br**](https://ix.br) sub-10 ms user latency | **Brazilian fintech (`PIX` ecosystem), telecom, and retail RAG/inference** |
| [**Magalu Cloud**](https://magalu.cloud) &amp; [**SONDA**](https://www.sonda.com) | **Brazil** (Sao Paulo/Northeast — `Magalu`) &amp; **Chile / Pan-LatAm** (`SONDA`) | **100% Brazilian Sovereign Public Cloud &amp; GPUs** (`Magalu`) + Regional Sovereign AI Cloud (`SONDA`) | **Local BRL / CLP billing** (zero USD FX shock) + strict **LGPD / Chilean data residency** | Kubernetes, VMs, S3-compatible object storage, [**OpenTofu**](https://opentofu.org), enterprise AI integration | Brazilian &amp; Andean public sector, retail, and SMBs escaping USD hyperscaler billing &amp; US CLOUD Act |
| [**KIO Networks**](https://www.kio.tech/en) **&amp;** [**Cirion**](https://www.ciriontechnologies.com) | **Mexico** (Queretaro, Monterrey, Mexico City), **LatAm** (18 DCs across BR, CL, AR, PE, CO), plus **Spain** bridge | Private enterprise GPU/cloud hosting + carrier-neutral high-power colocation | Connects **Mexico/LatAm** sovereignty directly across [**Spain (`/eu-cloud-spain/`)**](/eu-cloud-spain/) | Deep **18-DC subsea/terrestrial fiber mesh** lowering pan-regional MPLS/WAN costs | Ibero-American banking/insurance/manufacturing unifying **Madrid + Mexico + Bogota + Sao Paulo** |
| [**Digital Realty SP**](https://www.digitalrealty.com/data-centers/americas/sao-paulo) · [**Scala**](https://scaladatacenters.com) · [**Ascenty**](https://ascenty.com) | **Sao Paulo, Campinas, Tambore, Queretaro, Santiago, Bogota** | High-wattage wholesale campuses (**10–100+ MW**) supporting DLC GPU clusters | Deep Tier III+ financial certifications (**PCI-DSS, SOC2, ISO 27001**) | Direct [**IX.br**](https://ix.br) (`PTT Metro`) peering &amp; multi-cloud fabric (`ServiceFabric`) | Global multinationals colocating **private [OpenShift AI](https://www.redhat.com/en/products/ai/openshift-ai) / NVIDIA Enterprise racks** locally |
| [**Cassava AI**](https://www.cassava.ai) **&amp;** [**Africa Data Centres**](https://www.africadatacentres.com) | **South Africa (JHB, CPT), Kenya (Nairobi), Nigeria (Lagos), Egypt (Cairo), Morocco** | **Africa's first [NVIDIA Cloud Partner](https://www.nvidia.com/en-us/data-center/gpu-cloud-computing/partners) AI Factory** rolling out thousands of liquid-cooled GPUs regionally | **POPIA (ZA), NDPA (NG), Kenya DPA** localization + Kenya geothermal clean grid | Integrated directly with [**Liquid fiber**](https://liquid.tech) + [**MTN**](https://www.mtn.com) enterprise cloud ecosystems | Sovereign African banking, telco, healthcare, and localized multilingual African LLMs |
| [**Teraco**](https://www.teraco.co.za) **&amp;** [**Raxio Group**](https://raxiogroup.com) | **South Africa** (Johannesburg/Cape Town — `Teraco`) &amp; **East/West/Central Africa** (`Raxio`) | **Africa's largest interconnection hub** (`Teraco NAPAfrica`) + **Tier III regional edge DCs** (`Raxio`) | Utility-scale solar wheeling (`Teraco`) + Ethiopia/Uganda hydro grids &amp; central-bank residency laws | Carrier-neutral IXP peering eliminating expensive European hairpin latency | Pan-African banks, mobile money (`M-Pesa`/`MoMo`), &amp; low-latency [**vLLM**](https://github.com/vllm-project/vllm) regional inference |

### Pre-Sales Design Rules for LatAm and Africa AI Workloads

1. **Split Training vs Inference Across Continents Intelligently:** Unless full sovereign air-gap mandates training inside Sao Paulo/Johannesburg/Nairobi, train massive open-weight foundation models on ultra-low-cost hydro/wind [**Nordics**](/neoclouds-europe/) / [**North America**](/neoclouds-north-america/) / [**Brazil**](https://eleadatacenters.com) mega-hubs, then distribute **FP8/AWQ quantized [`vLLM`](https://github.com/vllm-project/vllm) inference** to [**KIO Queretaro**](https://www.kio.tech/en), [**Sao Paulo**](https://www.digitalrealty.com/data-centers/americas/sao-paulo)/[**Magalu Cloud**](https://magalu.cloud), [**ODATA Santiago**](https://odatadc.com)/[**SONDA**](https://www.sonda.com), [**Teraco Johannesburg**](https://www.teraco.co.za), or [**Africa Data Centres Nairobi**](https://www.africadatacentres.com) for sub-40 ms regional UX and strict local PII retention.
2. **Use Iberia–Brazil Direct Fiber for Ibero-American Sovereignty:** Spanish/Portuguese multinationals serving Brazil and Southern Cone markets can run **zero-US-transit AI pipelines** linking **Madrid** ([/eu-cloud-spain/](/eu-cloud-spain/) — [Merlin-Edged](https://edged.es) / [Stackscale](https://www.stackscale.com)) directly to **Sao Paulo** (`LGPD` + [EU Adequacy](https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/adequacy-decisions_en) corridors via [**IX.br**](https://ix.br)).
3. **Budget for Generator/Battery Autonomy in Developing Grids:** Outside top-tier Brazilian/Chilean/South African financial DCs ([**Scala**](https://scaladatacenters.com), [**Ascenty**](https://ascenty.com), [**Teraco**](https://www.teraco.co.za)), always verify Tier III+ **N+1 / 2N diesel + BESS autonomy and grid stability SLAs** before placing stateful 24x7 inference endpoints locally.
""",

    "neoclouds-architecture-stack.md": """## Pre-Sales Engineering Blueprint: GPU Fabrics, InfiniBand, Slurm vs Kubernetes and AI Storage

1. [GPU Silicon and Memory Hierarchy (NVIDIA Blackwell vs AMD Instinct)](#gpu-silicon-and-memory-hierarchy-nvidia-blackwell-vs-amd-instinct)
2. [AI Networking Fabrics: NVLink vs InfiniBand vs Spectrum-X RoCEv2](#ai-networking-fabrics-nvlink-vs-infiniband-vs-spectrum-x-rocev2)
3. [Slurm vs Kubernetes GPU Schedulers and SUNK Convergence](#slurm-vs-kubernetes-gpu-schedulers-and-sunk-convergence)
4. [Reference Neocloud AI Factory Stack (Mermaid Diagram)](#reference-neocloud-ai-factory-stack-mermaid-diagram)
5. [Parallel Storage and High-Speed Checkpointing (WEKA, VAST, DDN Lustre)](#parallel-storage-and-high-speed-checkpointing-weka-vast-ddn-lustre)

### GPU Silicon and Memory Hierarchy (NVIDIA Blackwell vs AMD Instinct)

Selecting the wrong GPU SKU is the fastest way to burn budget in a Neocloud deal. Match **workload memory &amp; precision profile** to **HBM capacity and NVLink domain size**:

| Accelerator SKU (Clickable) | HBM Capacity &amp; Memory Bandwidth | Native Low-Precision Compute | Intra-Node / Intra-Rack Link | Optimal Workload Profile (Pre-Sales Selection Rule) |
| :--- | :--- | :--- | :--- | :--- |
| [**NVIDIA H100 SXM5**](https://www.nvidia.com/en-us/data-center/h100) (`8x Node`) | **640 GB HBM3** *(80 GB/GPU; 3.35 TB/s)* | **FP8 / BF16** (Transformer Engine) | **900 GB/s NVLink Gen4** (8 GPUs) | Proven sweet spot for **fine-tuning, 8B–70B inference, LoRA**, and widest [PyTorch](https://pytorch.org)/CUDA compatibility at lowest spot rates |
| [**NVIDIA H200 SXM**](https://www.nvidia.com/en-us/data-center/h200) (`8x Node`) | **1.13 TB HBM3e** *(141 GB/GPU; 4.8 TB/s)* | **FP8 / BF16** | **900 GB/s NVLink Gen4** (8 GPUs) | **1.8x memory bandwidth boost** speeds up memory-bound **70B–405B LLM decoding &amp; long-context KV cache** dramatically |
| [**NVIDIA B200 &amp; GB200 NVL72**](https://www.nvidia.com/en-us/data-center/gb200-nvl72) | **192 GB HBM3e/GPU** *(13.8 TB unified across NVL72 rack @ 8 TB/s)* | **FP4 / FP8** (2nd Gen Transformer Engine) | **1.8 TB/s NVLink Gen5/GPU** (**130 TB/s Rack Coherence**) | **Trillion-parameter MoE training &amp; disaggregated reasoning (`DeepSeek/Llama-4`)**: keeps massive MoE experts in a single coherent NVLink fabric |
| [**AMD Instinct MI300X / MI325X**](https://www.amd.com/en/products/accelerators/instinct/mi300/mi300x.html) (`8x Node`) | **1.54 TB – 2.05 TB HBM3e** *(192–256 GB/GPU; 5.3–6.0 TB/s)* | **FP8 / BF16** ([**ROCm 6+**](https://rocm.docs.amd.com) / [vLLM](https://github.com/vllm-project/vllm)) | **896 GB/s Infinity Fabric** (8 GPUs) | **Inference TCO Killer:** Hosts huge open-weight models (`Qwen-72B`, `Llama-405B`) on **fewer GPUs without multi-node TP latency** ([TensorWave](https://tensorwave.com), [Vultr](https://docs.vultr.com/products/compute/instances/cloud-gpu)) |
| [**NVIDIA L40S**](https://www.nvidia.com/en-us/data-center/l40s) (`PCIe`) | **48 GB GDDR6/GPU** *(864 GB/s)* | **FP8 / BF16** | PCIe Gen4 (No NVLink) | Cost-effective **8B–32B inference, embeddings, image/video gen, VDI/CAD** where cross-GPU [NCCL](https://github.com/NVIDIA/nccl) AllReduce is unnecessary |

### AI Networking Fabrics: NVLink vs InfiniBand vs Spectrum-X RoCEv2

!!! danger "Why Standard Cloud Ethernet Kills Multi-Node Training Scaling"
    In distributed LLM training (`Tensor / Pipeline / FSDP`), GPUs synchronize gradients on every step via [**NCCL**](https://github.com/NVIDIA/nccl) `AllReduce / AlltoAll`. Standard TCP/IP VPC Ethernet suffers packet drops and ECMP hash collisions — collapsing cluster **Model FLOPs Utilization (MFU)** from **50%+ down to &lt;15%** across 32+ GPUs. Always audit the **Rail-Optimized Non-Blocking Backend Fabric** and [**BlueField-3 DPU**](https://www.nvidia.com/en-us/networking/products/data-processing-unit) north-south isolation:

| Network Fabric Tier (Clickable) | Per-GPU NIC Bandwidth | Protocol &amp; Congestion Architecture | Neocloud Footprint Examples | When Mandatory |
| :--- | :--- | :--- | :--- | :--- |
| **1. Scale-Up Domain (`NVLink / NVSwitch`)** | **900 GB/s – 1.8 TB/s** *(~7.2–14.4 Tbps!)* | Memory-coherent GPU-to-GPU switch fabric inside single node (`8 GPUs`) or [**GB200 NVL72 Rack**](https://www.nvidia.com/en-us/data-center/gb200-nvl72) (`72 GPUs`) | All SXM / HGX / DGX / NVL72 Neoclouds | **Required** for Tensor Parallelism (`TP=4/8/72`) &amp; Mixture-of-Experts routing |
| **2. Lossless InfiniBand ([`Quantum-2 NDR`](https://www.nvidia.com/en-us/networking/quantum2) / `X800`)** | **400 Gbps – 800 Gbps per GPU** *(3.2–6.4 Tbps/8-GPU node)* | Lossless credit-based link flow control, [**GPUDirect RDMA**](https://developer.nvidia.com/gpudirect), **SHARP** in-network reduction | [**CoreWeave**](https://coreweave.com), [**Nebius**](https://nebius.com), [**Crusoe**](https://crusoe.ai), [**Lambda**](https://lambda.ai), [**Nscale**](https://nscale.com), [**Verda**](https://verda.com), [**Taiga**](https://www.taigacloud.com), [**Yotta**](https://shakticloud.ai) | **Mandatory** for **64–4,096+ GPU multi-node pre-training** &amp; dense RLHF |
| **3. AI-Tuned Ethernet ([`NVIDIA Spectrum-X`](https://www.nvidia.com/en-us/networking/spectrumx) / `RoCEv2`)** | **400 Gbps per GPU** | Adaptive packet spraying + [**BlueField-3 SuperNIC/DPU**](https://www.nvidia.com/en-us/networking/products/data-processing-unit) congestion control (~95% effective link utilization) | Modern multi-tenant K8s inference clouds ([**Scaleway**](https://www.scaleway.com/en/gpu-instances), [**TensorWave**](https://tensorwave.com)) | Great for **disaggregated [`llm-d`](https://github.com/llm-d/llm-d) prefill/decode inference**, [KubeRay](https://github.com/ray-project/kuberay), &amp; **16–128 GPU fine-tuning** |
| **4. Standard Frontend Cloud VPC Ethernet** | **10G – 100G Shared** | Standard Linux TCP/IP &amp; overlay VXLAN ([Cilium](https://cilium.io)) | General VPS / budget PCIe clouds ([RunPod](https://www.runpod.io), [Civo](https://www.civo.com/ai), [Hetzner](https://www.hetzner.com/cloud)) | Acceptable **ONLY for single-node inference (`&lt;=8 GPUs`), embeddings, or RAG APIs** |

### Slurm vs Kubernetes GPU Schedulers and SUNK Convergence

| Orchestrator Pattern (Clickable) | Operational Model | Strengths for AI Teams | Weaknesses / Operational Traps | Where Used Best |
| :--- | :--- | :--- | :--- | :--- |
| [**Bare-Metal Slurm**](https://slurm.schedmd.com) | Traditional HPC batch daemon (`sbatch` / `srun` / PMIx) | Zero container scheduling latency; native InfiniBand topology awareness; loved by ML research PhDs | Awkward for 24x7 microservices, rolling upgrades, API gateways, and multi-tenant isolation | **Pure pre-training research labs** dedicating static blocks (`256–2,048 GPUs`) to 1–2 training jobs |
| **Kubernetes + [KAI Scheduler](https://github.com/NVIDIA/KAI-Scheduler) / [Kueue](https://github.com/kubernetes-sigs/kueue) / [Volcano](https://volcano.sh) + [GPU Operator](https://github.com/NVIDIA/gpu-operator)** | Declarative CNCF control plane + gang queuing + [**LeaderWorkerSet (`LWS`)**](https://github.com/kubernetes-sigs/lws) + **Dynamic Resource Allocation (DRA)** | Unified platform for **batch training ([KubeRay](https://github.com/ray-project/kuberay)) + autoscaled serving ([vLLM](https://github.com/vllm-project/vllm) / [SGLang](https://github.com/sgl-project/sglang) / [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) / [`llm-d`](https://github.com/llm-d/llm-d))** | Plain default `kube-scheduler` lacks gang co-scheduling (`all-or-nothing`) without **Kueue / KAI / Volcano** | **Enterprise Platform Teams &amp; Inference Fleets** running mixed RAG, serving, and LoRA training |
| [**SUNK (`CoreWeave Slurm on K8s`)**](https://github.com/coreweave/sunk-anywhere) | Runs [Slurm](https://slurm.schedmd.com) **workers as Kubernetes Pods** inside one unified cluster | **Best of Both Worlds:** ML researchers submit `sbatch` jobs while Platform SREs manage drivers, autoscaling, [DCGM](https://github.com/NVIDIA/dcgm-exporter), and idle-capacity inference reclaim via K8s | Slightly steeper initial cluster engineering outside [CoreWeave](https://docs.coreweave.com)/managed templates | **Medium-to-large Neocloud tenants** needing zero idle GPU gap between day-time research and night-time batch evals |

### Reference Neocloud AI Factory Stack (Mermaid Diagram)

```mermaid
%%{init: {'themeVariables': {'fontSize': '13px'}, 'flowchart': {'htmlLabels': false, 'nodeSpacing': 20, 'rankSpacing': 68, 'padding': 12}}}%%
flowchart LR
    A(["Enterprise AI<br/>Cluster Input"]) --> B{{"Primary Workload<br/>Pattern?"}}

    B -->|"Multi-Node Train"| B1["Training Scheduler<br/>Slurm or CoreWeave SUNK<br/>Gang Topology Placement"]
    B -->|"Online Serving"| B2["Kubernetes Serving<br/>KAI / Kueue + KubeRay<br/>vLLM & llm-d Disagg"]

    B1 --> C["Non-Blocking Fabric<br/>InfiniBand NDR or X800<br/>or Spectrum-X RoCEv2"]
    C --> D["Parallel AI Storage<br/>WEKA · VAST · DDN Lustre<br/>Fast Checkpointing"]

    B2 --> E["KV-Cache & Gateway<br/>K8s Gateway Inference Ext<br/>LiteLLM Multi-Provider"]
    E --> F["Goodput Telemetry<br/>NVIDIA DCGM Exporter<br/>XID Alerts + OpenCost"]
```

### Parallel Storage and High-Speed Checkpointing (WEKA, VAST, DDN Lustre)

Training a 70B–405B+ model emits **terabyte-scale optimizer checkpoints every 30–60 minutes**. If checkpoints stall because standard S3/NFS saturates at 2 GB/s, **thousands of EUR/hr of idle GPUs burn waiting on disk I/O**.

1. **Tier 0 — Local Node NVMe Scratch (`PCIe Gen5 RAID0`):** **50–100+ GB/s/node** for dataset prefetch shuffles and ephemeral scratch. Volatile if node fails!
2. **Tier 1 — Parallel AI Filesystem ([`WEKA`](https://docs.weka.io) / [`VAST Data`](https://www.vastdata.com) / [`DDN`](https://www.ddn.com) [`Lustre`](https://www.lustre.org)):** **Sub-millisecond POSIX + [GPUDirect Storage](https://developer.nvidia.com/gpudirect) RDMA** scaling to hundreds of GB/s–TB/s aggregate, finishing full cluster checkpoints in **&lt; 60 seconds**. Mandatory on every serious pre-training Neocloud engagement ([CoreWeave](https://coreweave.com), [Nebius](https://nebius.com), [Nscale](https://nscale.com), [EuroHPC](https://eurohpc-ju.europa.eu/ai-factories_en)).
3. **Tier 2 — Sovereign Object Storage (`S3` / [Ceph](https://ceph.io/en)):** Durable model weight artifact registry, raw curated corpus buckets, and [**CoreWeave Tensorizer**](https://github.com/coreweave/tensorizer) / [**Model Streamer**](https://github.com/dsx-ai-factory/model-streamer) fast cold-boot streaming into inference containers.
""",

    "neoclouds-iac-finops-sla.md": """## Pre-Sales Engineering Guide: Neocloud IaC Maturity, GPU FinOps and Goodput SLAs

1. [Neocloud IaC Coverage Scorecard (vs Hyperscalers = 100%)](#neocloud-iac-coverage-scorecard-vs-hyperscalers-100)
2. [Multi-Neocloud Portability Pattern (OpenTofu + SkyPilot + LiteLLM)](#multi-neocloud-portability-pattern-opentofu-skypilot-litellm)
3. [Goodput vs Uptime: Multi-Node GPU MTBF and Checkpointing SLAs](#goodput-vs-uptime-multi-node-gpu-mtbf-and-checkpointing-slas)
4. [GPU FinOps: Spot vs Bare Metal vs Token API Break-Even Rules](#gpu-finops-spot-vs-bare-metal-vs-token-api-break-even-rules)

### Neocloud IaC Coverage Scorecard (vs Hyperscalers = 100%)

Do **not** promise hyperscaler-style 250-resource Terraform breadth on every Neocloud. Instead, audit whether a provider automates the **5 critical GPU lifecycle primitives** (`GPU Cluster/NodeGroup, InfiniBand VPC, Parallel FS, S3, OIDC/IAM`) in [**OpenTofu**](https://opentofu.org) / Terraform:

| Provider (Clickable) | [OpenTofu](https://opentofu.org) / Terraform Coverage (vs AWS/Azure = 100%) | Official Provider / Repo | Managed Kubernetes &amp; [Slurm](https://slurm.schedmd.com) Provisioning | Primary Day-2 IaC Gaps &amp; Mitigation Strategy |
| :--- | :---: | :--- | :--- | :--- |
| [**Scaleway**](https://www.scaleway.com/en/gpu-instances) (FR/EU) | **85%** | [`scaleway/scaleway`](https://github.com/scaleway/terraform-provider-scaleway) + [Crossplane](https://github.com/scaleway/crossplane-provider-scaleway) | Declarative **Kapsule / Kosmos K8s** GPU node pools + IAM + S3 + VPC | Top EU DevOps experience; minor frontier Blackwell allocation limits still use console/account quota requests. |
| [**Vultr**](https://docs.vultr.com/products/compute/instances/cloud-gpu) &amp; [**DigitalOcean**](https://www.digitalocean.com/products/gpu-droplets) | **80%** | [`vultr/vultr`](https://github.com/vultr/terraform-provider-vultr) · [`digitalocean`](https://github.com/digitalocean/terraform-provider-digitalocean) | Official VKE/DOKS K8s + Cloud GPU VMs + Bare Metal + BGP/VPC | Lacks multi-node lossless InfiniBand fabrics; treat as distributed single-node inference/CI target. |
| [**Nebius**](https://nebius.com) (NL/FI/FR/US) | **75%** | [`nebius/nebius`](https://github.com/nebius/terraform-provider-nebius) ([docs](https://docs.nebius.com)) | [**MK8s GPU node groups**](https://nebius.com/compute/kubernetes), InfiniBand fabrics, Shared FS, S3, IAM cleanly in HCL | Younger provider surface for non-GPU PaaS; pair cleanly with [**Argo CD**](https://argo-cd.readthedocs.io) &amp; [**CloudNativePG**](https://cloudnative-pg.io) inside MK8s. |
| [**CoreWeave**](https://coreweave.com) (US/EU) | **70%** *(K8s-First)* | [CoreWeave Docs](https://docs.coreweave.com) + [**`coreweave/sunk-anywhere`**](https://github.com/coreweave/sunk-anywhere) | Everything centers on Kubernetes CRDs (`CKS`, `SUNK`, virtual-servers via K8s API) | Different mental model from AWS EC2 IAM: **treat CoreWeave Kubernetes itself as your control plane** via [Argo CD](https://argo-cd.readthedocs.io) / [Helm](https://helm.sh). |
| [**Crusoe Cloud**](https://crusoe.ai) (US/IS) | **70%** | [`crusoecloud/crusoe`](https://github.com/crusoecloud/terraform-provider-crusoe) ([docs](https://docs.crusoe.ai)) | Declarative InfiniBand partition networks, GPU VMs, K8s &amp; NVMe volumes | Multi-hundred-GPU physical InfiniBand topology reservations remain account-coordinated upfront. |
| [**Civo**](https://www.civo.com/ai) (UK) &amp; [**Gcore**](https://gcore.com/cloud/ai-gpu) (LU) | **75%** | [`civo/civo`](https://github.com/civo/terraform-provider-civo) · [`G-Core/gcore`](https://github.com/G-Core/terraform-provider-gcore) | Ultra-fast declarative K3s/[Talos](https://www.talos.dev) + GPU worker pools + S3 + Edge AI | Smaller DC catalogs; easy multi-cloud inclusion via standard K8s/[Helm](https://helm.sh)/[Pulumi](https://www.pulumi.com). |
| [**Nscale**](https://nscale.com) (UK/EU) &amp; [**Verda**](https://verda.com) (FI) | **65%** | [`nscaledev/nscale`](https://github.com/nscaledev/terraform-provider-nscale) + Verda REST/SDK | Declarative VPCs, GPU clusters, AI filesystems &amp; compute instances | Rapidly evolving provider APIs; verify multi-node [Slurm](https://slurm.schedmd.com)/K8s cluster bootstrapping scripts in POC. |
| [**RunPod**](https://www.runpod.io) · [**Modal**](https://modal.com) · [**Baseten**](https://www.baseten.co) | **65–75%** | [`runpod/runpod`](https://github.com/runpod/terraform-provider-runpod) + Python-as-Code SDKs | Automates GPU pods, Serverless [vLLM](https://github.com/vllm-project/vllm)/[TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) endpoints, Network Volumes | Lack of enterprise L2/BGP peering restricts them to containerized inference or stateless CI bursts. |
| [**Lambda**](https://lambda.ai) / [**Voltage Park**](https://voltagepark.com) / Regional | **45 – 60%** | Cloud REST APIs + [**SkyPilot**](https://github.com/skypilot-org/skypilot) + [Ansible](https://docs.ansible.com) (`1-Click` Slurm/SSH) | Reservation-based cluster spin-up; heavy reliance on post-provision Ansible/Slurm | Wrap bare-metal clusters declaratively via **SkyPilot + [Ansible](https://docs.ansible.com) + [Argo CD](https://argo-cd.readthedocs.io)** rather than bespoke scripts. |

### Multi-Neocloud Portability Pattern (OpenTofu + SkyPilot + LiteLLM)

Never let a single GPU vendor hold your AI roadmap hostage when spot prices spike or new silicon launches. Enforce this **3-Layer Decoupling Stack**:

```yaml
# 1. SkyPilot task YAML: portable across Nebius, Lambda, Crusoe, RunPod, Civo, AWS, GCP
resources:
  accelerators: H100:8
  infra: nebius          # Fail over automatically across clouds/regions (`any_of`)
  disk_size: 2048
file_mounts:
  /checkpoints:
    source: s3://acme-eu-sovereign-checkpoints/llama-ft/
    mode: MOUNT
run: |
  torchrun --nproc_per_node=8 train.py --resume-from /checkpoints/latest
```

1. **Compute Layer ([`OpenTofu`](https://opentofu.org) `+` [`SkyPilot`](https://github.com/skypilot-org/skypilot) `+` [`Cluster API`](https://cluster-api.sigs.k8s.io)):** Provision base clusters cleanly via OpenTofu, or let **SkyPilot** ([docs](https://skypilot.readthedocs.io)) hunt spare `8x H100 / H200` capacity automatically across [**Nebius**](https://nebius.com), [**Lambda**](https://lambda.ai), [**Crusoe**](https://crusoe.ai), [**Fluidstack**](https://fluidstack.io), [**RunPod**](https://www.runpod.io), and hyperscalers with automated spot recovery.
2. **State &amp; Weight Layer (`EU/Local S3 + Async Sync`):** Store datasets, tokenized shards, and safetensors checkpoints outside proprietary local disks inside **cross-region S3 buckets** ([**Scaleway FR**](https://www.scaleway.com/en/gpu-instances) / [**OVHcloud**](https://www.ovhcloud.com/en/public-cloud/ai-training) / [**Nebius**](https://nebius.com) / [AWS](https://aws.amazon.com)) and stream cold boots via [**Tensorizer**](https://github.com/coreweave/tensorizer).
3. **Inference Routing Layer ([`Gateway API Inference Extension`](https://github.com/kubernetes-sigs/gateway-api-inference-extension) `+` [`LeaderWorkerSet`](https://github.com/kubernetes-sigs/lws) `+` [`LiteLLM`](https://github.com/BerriAI/litellm)):** Expose a single internal OpenAI-compatible URL to apps; dynamically split traffic between **on-prem/Neocloud [vLLM](https://github.com/vllm-project/vllm)/[`SGLang`](https://github.com/sgl-project/sglang)/[`llm-d`](https://github.com/llm-d/llm-d) pods** and **Serverless fallback APIs** ([Together](https://www.together.ai) / [Fireworks](https://fireworks.ai) / [Baseten](https://www.baseten.co) / [Regolo](https://regolo.ai) / [Bedrock](https://aws.amazon.com/bedrock)).

### Goodput vs Uptime: Multi-Node GPU MTBF and Checkpointing SLAs

!!! danger "Why Standard 99.9% Cloud Uptime SLAs Mislead Distributed Training Teams"
    A single [**NVIDIA H100**](https://www.nvidia.com/en-us/data-center/h100)/[**GB200**](https://www.nvidia.com/en-us/data-center/gb200-nvl72) SXM system contains thousands of high-power solder joints, optical transceivers, HBM dies, and liquid cooling manifolds. Across a **1,024-GPU training cluster**, empirical hardware/IB link **Mean Time Between Interruptions (MTBI)** drops to roughly **1–3 failures per day**! A naive provider boasting "99.9% host uptime" gives you **zero protection** if silent InfiniBand bit errors slow training by 35% without triggering a VM reboot.

Pre-sales architects MUST replace generic VM uptime clauses with **Goodput &amp; Fabric SLAs**:

| Metric / SLA Clause | Naive Hyperscaler VM Contract | Production Neocloud ([`ClusterMAX Platinum/Gold`](https://www.clustermax.ai)) Standard | Mandatory Automation &amp; Pre-Sales Check |
| :--- | :--- | :--- | :--- |
| **Effective Goodput Ratio** | Not guaranteed (noisy neighbors / TCP backoff silently cut MFU) | **85%+ of theoretical `nccl-tests` AllReduce bus bandwidth** guaranteed continuously | Run [**`coreweave/nccl-tests`**](https://github.com/coreweave/nccl-tests) burn-in **before** accepting handover of any multi-node reservation. |
| **Proactive XID / ECC Replacement** | Ticket required; slow multi-hour VM stop/start &amp; manual investigation | Automated [**NVIDIA DCGM Exporter**](https://github.com/NVIDIA/dcgm-exporter) detecting XID critical errors ([**DCGM Guide**](https://docs.nvidia.com/datacenter/dcgm/latest/user-guide)) and hot-swapping warm spares in **&lt; 5 min** | Require pre-allocated **2–5% hot-standby spare nodes** in every `&gt;= 128-GPU` reserved contract. |
| **Inference RPO / RTO (Serving)** | Multi-AZ load balancing within single hyperscaler region | **RPO = 0** (immutable [Argo CD](https://argo-cd.readthedocs.io) prompts + S3 weights) · **RTO &lt; 30s** via active-active [**LiteLLM**](https://github.com/BerriAI/litellm) / [Gateway API](https://github.com/kubernetes-sigs/gateway-api-inference-extension) multi-vendor failover | Never serve mission-critical RAG from a **single-DC Neocloud zone**; mirror quantized [vLLM](https://github.com/vllm-project/vllm) replica across a secondary DC/provider. |
| **Training Checkpoint RPO** | Customer-managed EBS/S3 scripts | **RPO = 15–30 min** via **async [WEKA](https://docs.weka.io)/[VAST](https://www.vastdata.com)/[Lustre](https://www.lustre.org) write + S3 mirror** | Verify **checkpoint serialization latency &lt; 60s** so frequent saves consume `&lt; 3%` of paid GPU-hours. |

### GPU FinOps: Spot vs Bare Metal vs Token API Break-Even Rules

*Financial engineering rules validated via [**OpenCost**](https://github.com/opencost/opencost), [**Grafana**](https://grafana.com), and real-time cluster telemetry (`EUR` baseline):*

1. **Break-Even Threshold (Serverless Token API vs Dedicated 24x7 GPUs):** Stay on pay-per-token APIs ([**Together AI**](https://www.together.ai), [**Fireworks**](https://fireworks.ai), [**Baseten**](https://www.baseten.co), [**Scaleway Generative APIs**](https://www.scaleway.com/en/generative-apis), [**Regolo.ai**](https://regolo.ai), [**AWS Bedrock**](https://aws.amazon.com/bedrock), [**Azure AI Foundry**](https://azure.microsoft.com/en-us/products/ai-foundry), [**Vertex AI**](https://cloud.google.com/vertex-ai)) whenever aggregate sustained concurrency utilizes **`&lt; 35–45%`** of a dedicated **8x H100/L40S pod** over 24 hours. Above **45% continuous duty cycle**, self-hosting quantized [**vLLM**](https://github.com/vllm-project/vllm) / [**SGLang**](https://github.com/sgl-project/sglang) / [**`llm-d`**](https://github.com/llm-d/llm-d) on a Neocloud yields **40–70% immediate monthly EUR savings**.
2. **Preemptible Spot vs Reserved Bare Metal:** Use **Spot / On-Demand Preemptible (`30–50% cheaper`)** via [**SkyPilot**](https://github.com/skypilot-org/skypilot) exclusively for stateless evals, synthetic data generation, embeddings, and LoRA sweeps (`&lt; 4h` jobs). Lock **3-to-12-month Reserved Bare-Metal Clusters** ONLY once training architectures stabilize above 60% schedule fill.
3. **Eliminate 'Zombie Notebooks &amp; Idle H100s':** Enforce [**NVIDIA KAI Scheduler**](https://github.com/NVIDIA/KAI-Scheduler) / [**Kueue**](https://github.com/kubernetes-sigs/kueue) / [**Volcano**](https://volcano.sh) time-slicing or MIG (`1g.10gb` / `3g.40gb`) for developer notebooks and automated idle-reaper policies (`scale-to-zero` after 15 min idle VRAM) so **EUR 2.00+/hr GPUs** never sit burning budget overnight.
""",
}
