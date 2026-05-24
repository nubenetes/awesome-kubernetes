# Kubernetes Storage

!!! info "Architectural Context"
    Detailed reference for Kubernetes Storage in the context of The Container Stack.

## Standard Reference

  - [thenewstack.io: How Kubernetes provides networking and storage to applications](https://thenewstack.io/how-kubernetes-provides-networking-and-storage-to-applications)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: A Guide to Running Stateful Applications in Kubernetes](https://thenewstack.io/a-guide-to-running-stateful-applications-in-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [forbes.com: 5 Cloud Native Storage Startups To Watch Out For In 2019](https://www.forbes.com/sites/janakirammsv/2019/06/28/5-cloud-native-storage-startups-to-watch-out-for-in-2019)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [howtoforge.com: Storage in Kubernetes 🌟](https://www.howtoforge.com/storage-in-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [softwareengineeringdaily.com: Why Is Storage On Kubernetes So Hard? 🌟](https://softwareengineeringdaily.com/2019/01/11/why-is-storage-on-kubernetes-is-so-hard)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: Compute and Storage Should Be Decoupled for Log Management' at Scale](https://thenewstack.io/why-compute-and-storage-should-be-decoupled-for-log-management-at-scale)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [gitlab.com: Kubernetes storage provider benchmarks](https://gitlab.com/mrman/k8s-storage-provider-benchmarks)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: Beyond Block and File: COSI Enables Object Storage in Kubernetes' 🌟](https://thenewstack.io/beyond-block-and-file-cosi-enables-object-storage-in-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: When Is Decentralized Storage the Right Choice?](https://thenewstack.io/when-is-decentralized-storage-the-right-choice)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: The Biggest Gap in Kubernetes Storage Architecture?](https://thenewstack.io/whats-the-biggest-gap-in-kubernetes-storage-architecture)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [kylezsembery.com: Persistent Storage in Kubernetes](https://www.kylezsembery.com/persistent-storage-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: Stateful Workloads on Kubernetes with Container Attached' Storage 🌟](https://thenewstack.io/stateful-workloads-on-kubernetes-with-container-attached-storage)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [developers.redhat.com: How to maximize data storage for microservices and' Kubernetes, Part 1: An introduction 🌟](https://developers.redhat.com/articles/2021/08/11/how-maximize-data-storage-microservices-and-kubernetes-part-1-introduction)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: The Growth of State in Kubernetes](https://thenewstack.io/the-growth-of-state-in-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [itnext.io: Highly Available NFS cluster in Kubernetes, a cloud vendor independent' storage solution](https://itnext.io/highly-available-nfs-cluster-in-kubernetes-a-cloud-vendor-independent-storage-solution-f9a314cfdfcc)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [armosec.io: Data Storage in Kubernetes](https://www.armosec.io/blog/kubernetes-data-storage)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [infoq.com: Best Practices for Running Stateful Applications on Kubernetes](https://www.infoq.com/articles/kubernetes-stateful-applications)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [itnext.io: Temporary Storage for Kubernetes Pods](https://itnext.io/temporary-storage-for-kubernetes-pods-f8330ad8db88)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [danielmangum.com: K8s ASA: The Storage Interface](https://danielmangum.com/posts/k8s-asa-the-storage-interface)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [kubermatic.com: Keeping the State of Apps 5: Introduction to Storage Classes](https://www.kubermatic.com/blog/keeping-the-state-of-apps-5-introduction-to-storage-classes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [itnext.io: Kubernetes: PersistentVolume and PersistentVolumeClaim — an overview' with examples](https://itnext.io/kubernetes-persistentvolume-and-persistentvolumeclaim-an-overview-with-examples-3c5688222f99)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: Persistent Volumes: Separating Compute and Storage](https://thenewstack.io/persistent-volumes-separating-compute-and-storage)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [developers.redhat.com: Persistent storage in action: Understanding Red Hat' OpenShift’s persistent volume framework 🌟](https://developers.redhat.com/blog/2020/10/22/persistent-storage-in-action-understanding-red-hat-openshifts-persistent-volume-framework)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [itnext.io: Resizing StatefulSet Persistent Volumes with zero downtime 🌟](https://itnext.io/resizing-statefulset-persistent-volumes-with-zero-downtime-916ebc65b1d4)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [github.com/kubernetes-sigs: Local Persistence Volume Static Provisioner' 🌟](https://github.com/kubernetes-sigs/sig-storage-local-static-provisioner) <span class='md-tag md-tag--info'>⭐ 1198</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [linkedin.com/pulse: What are Kubernetes Persistent Volumes?](https://www.linkedin.com/pulse/what-kubernetes-persistent-volumes-gyan-prakash-1f)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [kubermatic.com: Keeping the State of Apps 1: Introduction to Volume and' volumeMounts](https://www.kubermatic.com/blog/keeping-the-state-of-apps-1-introduction-to-volume-and-volumemounts)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [adamtheautomator.com: Effortless Storage Management With Kubernetes PVC' 🌟](https://adamtheautomator.com/kubernetes-pvc)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [openebs/zfs-localpv](https://github.com/openebs/zfs-localpv) <span class='md-tag md-tag--info'>⭐ 561</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [spacelift.io: Kubernetes Persistent Volumes – Tutorial and Examples](https://spacelift.io/blog/kubernetes-persistent-volumes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [matthewpalmer.net: Filesystem vs Volume vs Persistent Volume 🌟](https://matthewpalmer.net/kubernetes-app-developer/articles/kubernetes-volumes-example-nfs-persistent-volume.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Digital Ocean: Kuberntes PVC ReadWriteMany access mode alternative](https://www.digitalocean.com/community/questions/kuberntes-pvc-readwritemany-access-mode-alternative)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [itnext.io: State of Persistent Storage in K8s — A Benchmark](https://itnext.io/state-of-persistent-storage-in-k8s-a-benchmark-77a96bb1ac29)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [itnext.io: Using Rook On A K3s Cluster](https://itnext.io/using-rook-on-a-k3s-cluster-8a97a75ba25e)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Reduxio](https://www.reduxio.com)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [OpenEBS](https://openebs.io)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [openebs/dynamic-localpv-provisioner: Dynamic Kubernetes Local Persistent' Volumes](https://github.com/openebs/dynamic-localpv-provisioner) <span class='md-tag md-tag--info'>⭐ 207</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [openebs/lvm-localpv](https://github.com/openebs/lvm-localpv) <span class='md-tag md-tag--info'>⭐ 341</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Longhorn](https://longhorn.io)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: Rancher Donates its ‘Longhorn’ Kubernetes Persistent Storage' Software to CNCF](https://thenewstack.io/rancher-donates-its-longhorn-kubernetes-persistent-storage-software-to-cncf)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [linbit.com: LINSTOR - kubernetes persistent container storage](https://linbit.com/kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [iomesh.com](https://www.iomesh.com)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [iomesh.com: Outperforming Peer Products, IOMesh Takes Cloud Native Storage' to the Next Level](https://www.iomesh.com/blog/announcing_iomesh_preview)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [libopenstorage/stork: Stork - Storage Operator Runtime for Kubernetes](https://github.com/libopenstorage/stork) <span class='md-tag md-tag--info'>⭐ 401</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [simplyblock: simplyblock.io](https://simplyblock.io)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [kubernetes-csi.github.io](https://kubernetes-csi.github.io)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [github.com/kubernetes-csi](https://github.com/kubernetes-csi)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [SMB CSI Driver for Kubernetes](https://github.com/kubernetes-csi/csi-driver-smb) <span class='md-tag md-tag--info'>⭐ 639</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [github.com/yandex-cloud: CSI for S3](https://github.com/yandex-cloud/k8s-csi-s3) <span class='md-tag md-tag--info'>⭐ 855</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [sklar.rocks: How the CSI (Container Storage Interface) Works](https://sklar.rocks/how-container-storage-interface-works)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [next.redhat.com: Introducing VolSync: your data, anywhere](https://next.redhat.com/2021/08/23/introducing-volsync-your-data-anywhere)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>


---
💡 **Explore Related:** [Kubernetes On Premise](./kubernetes-on-premise.md) | [Kubernetes Based Devel](./kubernetes-based-devel.md) | [Kubernetes Bigdata](./kubernetes-bigdata.md)

