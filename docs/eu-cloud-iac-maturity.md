# IaC Automation and Portability on European Sovereign Clouds

Technical reference comparing Infrastructure-as-Code (IaC) automation maturity, API coverage, Crossplane control planes, Cluster API providers, and multi-cloud portability across European Sovereign Clouds versus US Hyperscalers (AWS/Azure/GCP = 100% baseline).

1. [Official Terraform and OpenTofu Providers for European Clouds](#official-terraform-and-opentofu-providers-for-european-clouds)
2. [Portable Hypervisor and Private Cloud IaC Providers](#portable-hypervisor-and-private-cloud-iac-providers)
3. [Crossplane and Cluster API (CAPI) Multi-Cloud Control Planes](#crossplane-and-cluster-api-capi-multi-cloud-control-planes)

## Official Terraform and OpenTofu Providers for European Clouds

- **(2026)** [OVHcloud Official Terraform Provider](https://github.com/ovh/terraform-provider-ovh) 🌟 - Official OpenTofu/Terraform provider automating OVHcloud Public Cloud, Managed Kubernetes (MKS), vRack networking, KMS, IAM, Object Storage, and dedicated servers.
- **(2026)** [Scaleway Official Terraform Provider](https://github.com/scaleway/terraform-provider-scaleway) 🌟 - High-coverage IaC provider automating Scaleway Instances, Kapsule/Kosmos Kubernetes, Managed PostgreSQL/Redis, IAM/RBAC, Serverless Containers/Functions, and AI Endpoints.
- **(2026)** [IONOS Cloud Official Terraform Provider](https://github.com/ionos-cloud/terraform-provider-ionoscloud) 🌟 - Comprehensive provider for IONOS Virtual Data Centers (VDC), Managed Kubernetes, MariaDB/Postgres DBaaS, Network Load Balancers, and S3 Object Storage.
- **(2026)** [STACKIT Official Terraform Provider](https://github.com/stackitcloud/terraform-provider-stackit) 🌟 - Official Schwarz Digits IaC provider managing STACKIT Kubernetes Engine (SKE), OpenStack VMs, Load Balancers, Observability, and DBaaS resources.
- **(2026)** [Hetzner Cloud Official Terraform Provider](https://github.com/hetznercloud/terraform-provider-hcloud) 🌟 - Fast, ultra-reliable OpenTofu/Terraform provider for Hetzner Cloud servers, private networks, firewalls, volumes, load balancers, and autoscaling node pools.
- **(2026)** [3DS OUTSCALE Official Terraform Provider](https://github.com/outscale/terraform-provider-outscale) 🌟 - Official IaC provider for SecNumCloud-qualified 3DS OUTSCALE infrastructure covering OKS Kubernetes, Nets/VPCs, security groups, and volumes.
- **(2026)** [Exoscale Official Terraform Provider](https://github.com/exoscale/terraform-provider-exoscale) 🌟 - Official provider for Swiss/EU Exoscale Compute, SKS Managed Kubernetes, DBAAS, SOS Object Storage, and IAM API keys.
- **(2026)** [UpCloud Official Terraform Provider](https://github.com/UpCloudLtd/terraform-provider-upcloud) 🌟 - Official provider supporting UpCloud Managed Kubernetes, MaxIOPS storage, Managed Databases, SDN private networks, and Madrid (`es-mad1`) deployments.
- **(2026)** [Civo Official Terraform Provider](https://github.com/civo/terraform-provider-civo) 🌟 - Lightweight IaC provider for Civo K3s/Talos Managed Kubernetes clusters, firewalls, networks, and UK Sovereign workloads.
- **(2026)** [Open Telekom Cloud Terraform Provider](https://github.com/opentelekomcloud/terraform-provider-opentelekomcloud) 🌟 - Mature enterprise IaC provider covering Open Telekom Cloud VPCs, CCE Kubernetes, RDS, KMS, and German sovereign compliance policies.
- **(2026)** [Nebius Official Terraform Provider](https://github.com/nebius/terraform-provider-nebius) 🌟 - Official OpenTofu/Terraform provider for Nebius AI GPU clusters, MK8s Kubernetes, Filesystem/S3 storage, and InfiniBand GPU fabrics.

## Portable Hypervisor and Private Cloud IaC Providers

- **(2026)** [OpenStack Standard Terraform Provider](https://github.com/terraform-provider-openstack/terraform-provider-openstack) 🌟 - Universal open-source IaC provider enabling write-once infrastructure modules across European OpenStack sovereign clouds (Cleura, Elastx, Stackscale, City Cloud, OVH/STACKIT OpenStack layers).
- **(2026)** [VMware Cloud Director (VCD) Terraform Provider](https://github.com/vmware/terraform-provider-vcd) 🌟 - Standardized IaC provider widely compatible with Spanish and European VCSP clouds (Arsys, Gigas, Alhambra IT, Telefonica Tech VDC, Acens) running vCD NSX-T Edge Gateways and OrgVDCs.
- **(2026)** [Proxmox VE Terraform Provider (bpg/proxmox)](https://github.com/bpg/terraform-provider-proxmox) 🌟 - Actively maintained declarative provider enabling hyperscaler-grade VM, LXC, SDN, cloud-init, and Ceph/ZFS automation inside private Proxmox data centers.
- **(2026)** [Kube-Hetzner: Production Talos/K3s Terraform Module](https://github.com/kube-hetzner/terraform-hcloud-kube-hetzner) 🌟 - Battle-tested OpenTofu/Terraform module deploying HA auto-upgrading Kubernetes clusters with MicroOS/k3s on Hetzner Cloud at a fraction of hyperscaler EKS/AKS cost.

## Crossplane and Cluster API (CAPI) Multi-Cloud Control Planes

- **(2026)** [IONOS Cloud Official Crossplane Provider](https://github.com/ionos-cloud/crossplane-provider-ionoscloud) 🌟 - Native Kubernetes control plane allowing GitOps teams to reconcile IONOS Virtual Data Centers and Managed K8s continuously via Argo CD and Crossplane XRDs.
- **(2026)** [Scaleway Official Crossplane Provider](https://github.com/scaleway/crossplane-provider-scaleway) 🌟 - Official Upjet-based Crossplane provider exposing Scaleway compute, Kubernetes, and database primitives as Kubernetes CRDs.
- **(2026)** [Cluster API Provider Hetzner (CAPH by Syself)](https://github.com/syself/cluster-api-provider-hetzner) 🌟 - CNCF Cluster API provider managing full self-healing Kubernetes lifecycle across Hetzner Cloud VMs and Dedicated bare-metal Robot servers.
- **(2026)** [Cluster API Provider Proxmox (CAPMOX by IONOS)](https://github.com/ionos-cloud/cluster-api-provider-proxmox) 🌟 - Enterprise Cluster API provider built by IONOS Cloud for declarative multi-cluster Kubernetes orchestration directly on Proxmox VE clusters.
- **(2026)** [Cluster API Provider OpenStack (CAPO)](https://github.com/kubernetes-sigs/cluster-api-provider-openstack) 🌟 - Official Kubernetes SIGs CAPI provider delivering standardized multi-cluster lifecycle across European OpenStack sovereign clouds.
- **(2026)** [Cluster API Provider CloudStack (CAPC)](https://github.com/kubernetes-sigs/cluster-api-provider-cloudstack) 🌟 - Official Kubernetes SIGs provider turning Apache CloudStack private DCs into declarative GitOps Kubernetes fleets.
- **(2026)** [Cluster API Provider VMware Cloud Director (CAPVCD)](https://github.com/vmware/cluster-api-provider-cloud-director) 🌟 - Declarative Cluster API lifecycle driver for Spanish and European sovereign MSPs running VMware Cloud Director.
