# Kubernetes Troubleshooting

!!! info "Architectural Context"
    Detailed reference for Kubernetes Troubleshooting in the context of The Container Stack.

## Observability

### Capacity Management

#### Kernel Internals

##### Pod Throttling

  - **(2024)** [**CPU Limits in Kubernetes: Deep Dive into Pod Throttling and Kernel Interactions**](https://www.linkedin.com/pulse/cpu-limits-kubernetes-why-your-pod-idle-still-deep-dive-lazarev-k3m7f?utm_source=share&utm_medium=member_android&utm_campaign=share_via) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — A deep analysis of the Linux kernel's Completely Fair Scheduler (CFS) quotas and how they cause Kubernetes pod throttling despite low resource utilization. Indispensable for engineers diagnosing performance degradation under restrictive CPU limit settings.
## Observability and Performance

### Kubernetes Internals

#### Resource Management

  - **(2024)** [The Hidden CPU Throttling Crisis in Kubernetes Clusters](https://www.kubenatives.com/p/the-hidden-cpu-throttling-crisis) <span class='md-tag md-tag--warning'>[EN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An in-depth analysis exposing the silent threat of CPU throttling inside Kubernetes clusters caused by rigid CFS quota management. Demonstrates how microservices suffer latency spikes even with low aggregate CPU consumption.

---
💡 **Explore Related:** [Ocp4](./ocp4.md) | [Kubernetes Based Devel](./kubernetes-based-devel.md) | [Openshift](./openshift.md)

