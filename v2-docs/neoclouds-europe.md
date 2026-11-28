---
type: curation-hub
okf_version: "0.3"
name: "European Neoclouds and Country AI Factories"
dimension: "Neoclouds & GPU AI Clouds"
resource_count: 30
fresh_2025_2026_count: 30
trust: verified
freshness: active
provenance: "https://github.com/nubenetes/awesome-kubernetes/blob/master/docs/neoclouds-europe.md"
description: "Curated, AI-ranked European Neoclouds & Country AI Factories resources for the 2026 Cloud Native architect: top-tier tools, guides and references (Neoclouds &."
---
# European Neoclouds and Country AI Factories

!!! tip "Nubenetes V2 Elite Portal"
    You are browsing the AI-Curated V2 Elite Edition. Looking for the exhaustive list of references? Check out the [**V1 Historical Archive**](/v1/neoclouds-europe/).

!!! info "Architectural Context"
    Detailed reference for European Neoclouds and Country AI Factories in the context of Neoclouds & GPU AI Clouds.

!!! abstract "Deep-Dive Topic Pages"
    [Neoclouds Overview & Sovereign Overlap](neoclouds.md) · [EU Sovereign Cloud Overview & TCO](eu-sovereign-cloud.md) · [Netherlands & Benelux Cloud & DCs](eu-cloud-benelux.md) · [France Sovereign Cloud & Private DCs](eu-cloud-france.md) · [Germany Sovereign Cloud & Private DCs](eu-cloud-germany.md) · [Spain Sovereign Cloud & Private DCs](eu-cloud-spain.md) · [Italy Sovereign Cloud & Private DCs](eu-cloud-italy.md) · [Nordics Green Cloud & AI Factories](eu-cloud-nordics.md) · [Switzerland & Austria (Alpine Sovereign)](eu-cloud-switzerland-dach.md) · [United Kingdom Sovereign Cloud & DCs](eu-cloud-uk.md) · [GPU Fabrics, Slurm vs K8s & Storage](neoclouds-architecture-stack.md) · [Neocloud IaC Maturity, GPU FinOps & SLAs](neoclouds-iac-finops-sla.md)

## Pre-Sales Field Guide: European Neoclouds and Country AI Factories

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


## European Sovereign Cloud and Private Dcs

### France Sovereign Cloud and Private Dcs

#### French Sovereign Cloud Providers Secnumcloud And AI Factories

  - **(2026)** [Mistral AI Sovereign Frontier Models](https://mistral.ai) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[LLM]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — Paris-based European AI champion delivering open-weight (Mistral/Mixtral/Codestral) and enterprise models optimized for self-hosted Kubernetes vLLM and European sovereign cloud AI endpoints.
### Germany Sovereign Cloud and Private Dcs

#### German Sovereign Cloud And Managed Kubernetes Providers

  - **(2026)** [Cloud&Heat German Green Sovereign Cloud](https://www.cloudandheat.com) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[HYPERVISOR]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — Dresden-based German sovereign OpenStack cloud and direct hot-water liquid-cooled AI compute operator designed for ultra-low PUE heat reuse and zero hyperscaler lock-in.
#### Private Colocation Interconnection And Eurohpc AI In Germany

  - **(2026)** [Juelich Supercomputing Centre: JUPITER Exascale AI](https://www.fz-juelich.de/en/jsc/systems/supercomputers/jupiter) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[GPU]</span> — Europe's first exascale EuroHPC supercomputer at Forschungszentrum Juelich featuring nearly 24,000 NVIDIA GH200 Grace Hopper Superchips to power sovereign European AI foundation model training.
### Italy Sovereign Cloud and Private Dcs

#### Italy Sovereign Cloud And ACN Qualified Providers

  - **(2026)** [Aruba Cloud (Global Cloud Data Centers)](https://www.arubacloud.com) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — Italy's flagship cloud and trust-services provider operating Tier IV hyper-efficient campuses near Milan (Ponte San Pietro) and Rome with Italian ACN QC3 and AI3 sovereign qualifications for public administration and regulated enterprises.
  - **(2026)** [Seeweb Cloud and GPU AI Infrastructure](https://www.seeweb.it/en) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[GPU]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — Independent Italian cloud and data center pioneer specializing in NVIDIA H100/L40S/A100 GPU clusters, Kubernetes, sovereign AI inference, and zero hyperscaler egress traps.
### Netherlands and Benelux Cloud and Dcs

#### Nordics Switzerland And Benelux Cloud And AI Providers

  - **(2026)** [Nebius Sovereign AI Cloud (Amsterdam HQ)](https://nebius.com) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[GPU]</span> <span class='md-tag md-tag--primary'>[NEOCLOUD]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — European-headquartered AI hyperscaler operating massive InfiniBand-interconnected NVIDIA H100, H200, and Blackwell B200 superclusters in Finland and France with Kubernetes (MK8s), Slurm, and Sovereign S3 storage.
### Nordics Green Cloud and AI Factories

#### Hydro And Geothermal AI Data Centers And Eurohpc Supercomputing

  - **(2026)** [Green Mountain Hydro-Powered Data Centers (Norway and UK)](https://greenmountain.no) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — World-renowned Norwegian ultra-low-PUE colocation operator running fjord-cooled and 100% hydro-powered AI and sovereign enterprise data centers (Stavanger, Rjukan, Oslo).
  - **(2026)** [LUMI Pre-Exascale Supercomputer (CSC Kajaani Finland)](https://lumi-supercomputer.eu) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> — One of Europe's cleanest pre-exascale EuroHPC supercomputers in Kajaani powered 100% by hydroelectricity with waste heat exported directly to the local municipal district heating grid.
#### Nordic Sovereign Cloud And 3-AZ Openstack Providers

  - **(2026)** [evroc: European Sovereign Hyperscale Cloud Initiative](https://evroc.com) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — Stockholm-headquartered initiative engineering high-security, sustainable European hyperscale cloud and AI data center regions exclusively under EU jurisdiction.
### Spain Sovereign Cloud and Private Dcs

#### Private Colocation Interconnection And Ai-ready Data Centers In Spain

  - **(2026)** [DATA4 Madrid Campus](https://www.data4group.com/en) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> — European data center operator (Alcobendas and San Agustin de Guadalix, Madrid) delivering high-density Tier III+ sovereign wholesale and retail colocation with 100% renewable PPA options.
### Switzerland and Austria alpine Sovereign

#### Alpine Private Colocation Interconnection And Supercomputing

  - **(2026)** [CSCS Alps Supercomputer (Lugano Switzerland)](https://www.cscs.ch/computers/alps) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[GPU]</span> — Swiss National Supercomputing Centre flagship NVIDIA Grace Hopper (GH200) system powering sovereign Swiss climate, biomedical, and open-weight AI research (Swiss AI Initiative).
## Germany Spain And Italy AI Cloud Hubs

  - **(2026)** [BSC MareNostrum 5 and Barcelona AI Factory](https://www.bsc.es/research-and-development/ai-factory) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[GPU]</span> <span class='md-tag md-tag--primary'>[NEOCLOUD]</span> — Spanish EuroHPC AI Factory at Barcelona Supercomputing Center providing NVIDIA H100 capacity and open multilingual European foundation models (ALIA/Salamandra).
  - **(2026)** [IONOS GPU Server and AI Cloud (Germany and EU)](https://www.ionos.com/servers/gpu-server) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[GPU]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — BSI C5-aligned German cloud provider offering sovereign GPU hosting and open-weight AI inference in German facilities (United Internet Group, parent of Arsys Spain).
  - **(2026)** [Merlin-Edged Zero-Water Liquid-Cooled AI Campuses (Spain)](https://edged.es) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[GPU]</span> <span class='md-tag md-tag--primary'>[NEOCLOUD]</span> — High-density liquid-cooled Spanish and European data centers across Madrid-Getafe, Barcelona, and Bilbao-Arasur built for 100+ kW NVIDIA GB200 AI Neocloud pods.
  - **(2026)** [Northern Data Group and Taiga Cloud (Frankfurt)](https://www.taigacloud.com) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[GPU]</span> <span class='md-tag md-tag--primary'>[NEOCLOUD]</span> — Frankfurt-headquartered European Neocloud operating massive 100% renewable-powered NVIDIA H100/H200 and liquid-cooled GPU clusters across Northern Europe.
  - **(2026)** [Regolo.ai (Seeweb Sovereign Inference Cloud)](https://regolo.ai) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[GPU]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — Italian-hosted sustainable AI inference platform delivering OpenAI-compatible open-weight endpoints running exclusively on renewable European GPUs with zero US data transit.
## Netherlands Benelux And France Neoclouds

  - **(2026)** [Gcore AI Infrastructure (Luxembourg HQ)](https://gcore.com/cloud/ai-gpu) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[GPU]</span> <span class='md-tag md-tag--primary'>[NEOCLOUD]</span> — European edge and GPU inference Neocloud headquartered in Luxembourg delivering low-latency H100/L40S Everywhere Inference PoPs and Bare Metal AI pods across Europe.
  - **(2026)** [Leafcloud: Dutch Sustainable Heat-Reuse Cloud](https://www.leaf.cloud) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[GPU]</span> <span class='md-tag md-tag--primary'>[HYPERVISOR]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — Amsterdam green sovereign Kubernetes and OpenStack cloud placing distributed GPU and compute nodes directly inside urban buildings for residential heating reuse.
  - **(2026)** [Nebius Managed Kubernetes for GPU (MK8s)](https://nebius.com/compute/kubernetes) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[GPU]</span> <span class='md-tag md-tag--primary'>[NEOCLOUD]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — Turnkey Kubernetes control plane integrated with NVIDIA InfiniBand RDMA, GPU Operator, shared Lustre-class filesystems, and official Terraform provisioning.
  - **(2026)** [OVHcloud Public Cloud AI Training](https://www.ovhcloud.com/en/public-cloud/ai-training) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[GPU]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — French sovereign cloud and AI training suite pairing GDPR/SecNumCloud-aligned data centers with zero egress fees and Managed Kubernetes GPU worker pools.
  - **(2026)** [Scaleway GPU Cloud (Paris / Iliad Group)](https://www.scaleway.com/en/gpu-instances) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[GPU]</span> <span class='md-tag md-tag--primary'>[NEOCLOUD]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — Leading French Neocloud offering H100 SXM5, L40S, and Blackwell GPU nodes integrated natively with Kapsule Kubernetes and Terraform (`scaleway/scaleway`).
  - **(2026)** [Scaleway Serverless Generative APIs](https://www.scaleway.com/en/generative-apis) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — European-hosted OpenAI-compatible serverless inference endpoints running open-weight Mistral, Llama, and DeepSeek models inside French data centers with GDPR and EU AI Act compliance.
## Nordics Alpine And UK Neoclouds Plus Eurohpc AI Factories

  - **(2026)** [atNorth Nordic High-Density AI Data Centers](https://atnorth.com) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[NEOCLOUD]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — Pan-Nordic Neocloud-ready AI data center platform across Iceland, Sweden, Finland, and Denmark delivering hydroelectric liquid cooling and PUE below 1.2.
  - **(2026)** [Civo Sovereign AI and Kubernetes (UK)](https://www.civo.com/ai) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[GPU]</span> <span class='md-tag md-tag--primary'>[NEOCLOUD]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — UK developer-first Neocloud delivering NCSC-aligned sovereign GPU compute and RelaxAI hosting without hyperscaler egress fees or multi-year lock-in.
  - **(2026)** [EuroHPC JU AI Factories Initiative](https://eurohpc-ju.europa.eu/ai-factories_en) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> — European Union federated program upgrading pan-European supercomputers (BSC Barcelona, CINECA DAMA Bologna, JUPITER Juelich, LUMI Kajaani) into accessible startup and SME AI Factories.
  - **(2026)** [Exoscale Swiss and European GPU Cloud](https://www.exoscale.com/gpu) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[GPU]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — Lausanne-headquartered cloud provider (A1 Telekom Austria Group) offering FINMA/GDPR-compliant NVIDIA GPU VMs and SKS Kubernetes across Switzerland and Austria.
  - **(2026)** [Isambard-AI National Supercomputing Documentation (UK)](https://docs.isambard.ac.uk) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[GPU]</span> <span class='md-tag md-tag--primary'>[NEOCLOUD]</span> — Official technical documentation for Britain's 5,448-GPU NVIDIA GH200 national AI supercomputer hosted by the University of Bristol.
  - **(2026)** [Nscale Sovereign AI Cloud (UK and Europe)](https://nscale.com) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[GPU]</span> <span class='md-tag md-tag--primary'>[NEOCLOUD]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — UK-headquartered vertically integrated Neocloud operating renewable liquid-cooled NVIDIA H100/B200 AI factories across Europe, the UK, and North America.
  - **(2026)** [Verda (formerly DataCrunch) Nordic Sovereign GPU Neocloud](https://verda.com) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[GPU]</span> <span class='md-tag md-tag--primary'>[NEOCLOUD]</span> — Helsinki-headquartered European AI Neocloud operating 100% renewable-powered NVIDIA H100, H200, and Blackwell B200 InfiniBand clusters across Finland and Iceland under EU jurisdiction.
  - **(2026)** [Verne High-Intensity Compute Campuses](https://www.verneglobal.com) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[GPU]</span> — Icelandic and Nordic supercomputing colocation specialist running gigawatt-scale liquid-cooled bare-metal GPU fabrics on geothermal and hydro power.

---
💡 **Explore Related:** [Neoclouds Overview, Sovereign Overlap & TCO](./neoclouds.md) | [North America Neoclouds (US & Canada)](./neoclouds-north-america.md) | [Asia-Pacific Neoclouds & AI Clouds](./neoclouds-apac.md)

🔗 **See Also:** [Hypervisors, IaaS, K8s & Sovereign AI](./eu-cloud-workloads-stack.md) | [Demos](./demos.md)

