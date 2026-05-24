# Kubernetes Storage

!!! info "Architectural Context"
    Detailed reference for Kubernetes Storage in the context of The Container Stack.

## Standard Reference

  - [redbooks.ibm.com: IBM Storage for Red Hat OpenShift. IBM block storage & IBM Spectrum Scale](http://www.redbooks.ibm.com/abstracts/redp5565.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: The most popular cloud native solutions 🌟](https://thenewstack.io/cloud-native/the-most-popular-cloud-native-storage-solutions)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blocksandfiles.com: geless storage is the ‘answer’ to Kubernetes data challenges](https://www.blocksandfiles.com/container-storage/2020/12/22/storageless-storage-is-the-answer-to-kubernetes-data-challenges/1611647)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [rancher.com: What is Cloud-Native Storage?](https://www.suse.com/c/rancher_blog/what-is-cloud-native-storage)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [storj.io: Integrating Decentralized Cloud Storage with Duplicati](https://www.storj.io/cloud-object-storage)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [infoworld.com: Kubernetes object storage best practices](https://www.infoworld.com/article/2269961/kubernetes-object-storage-best-practices.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.flant.com: Comparing Ceph, LINSTOR, Mayastor, and Vitastor storage performance in Kubernetes](https://palark.com/blog/kubernetes-storage-performance-linstor-ceph-mayastor-vitastor)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.newrelic.com: Kubernetes Fundamentals, Part 5: Working with Kubernetes Volumes](https://newrelic.com/blog/infrastructure-monitoring/how-to-use-kubernetes-volumes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blocksandfiles.com: Lightbits Labs adds Kubernetes table stakes: CSI support](https://www.blocksandfiles.com/block/2020/06/23/lightbits-labs-adds-kubernetes-table-stakes-csi-support/1598623)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Longhorn Simplifies Distributed Block Storage in Kubernetes](https://www.suse.com/c/rancher_blog/longhorn-simplifies-distributed-block-storage-in-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [containerjournal.com: Rancher Labs Adds Support for Longhorn Storage on Kubernetes Clusters](https://cloudnativenow.com/topics/cloudnativeplatforms/rancher-labs-adds-support-for-longhorn-storage-on-kubernetes-clusters)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [searchstorage.techtarget.com: IBM Spectrum](https://www.techtarget.com/searchitchannel/definition/IBM-International-Business-Machines)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blocksandfiles.com: Kubernetes storage: SmartX’s IOMesh beats Portworx, Longhorn and OpenEBS](https://www.blocksandfiles.com/block/2021/08/05/kubernetes-storage-smartxs-iomesh-beats-portworx-longhorn-and-openebs/1617691)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [min.io](https://www.min.io)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [dok.community: Data on Kubernetes 2021 Report](https://dok.community/dokc-2021-report)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: How Kubernetes provides networking and storage to applications](https://thenewstack.io/how-kubernetes-provides-networking-and-storage-to-applications)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium: Kubernetes Storage Explained 🌟](https://medium.com/swlh/kubernetes-storage-explained-558e85596d0c)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: A Guide to Running Stateful Applications in Kubernetes](https://thenewstack.io/a-guide-to-running-stateful-applications-in-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [forbes.com: 5 Cloud Native Storage Startups To Watch Out For In 2019](https://www.forbes.com/sites/janakirammsv/2019/06/28/5-cloud-native-storage-startups-to-watch-out-for-in-2019)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium: Solution architect’s guide to Kubernetes persistent storage](https://medium.com/weareservian/solution-architects-guide-to-kubernetes-persistant-storage-3c9660187e8f)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [howtoforge.com: Storage in Kubernetes 🌟](https://www.howtoforge.com/storage-in-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [cncf.io: Container Attached Storage is Cloud Native Storage (CAS)](https://www.cncf.io/blog/2020/09/22/container-attached-storage-is-cloud-native-storage-cas)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium: Kubernetes Storage Performance Comparison v2 (2020 Updated) 🌟](https://medium.com/volterra-io/kubernetes-storage-performance-comparison-v2-2020-updated-1c0b69f0dcf4)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [softwareengineeringdaily.com: Why Is Storage On Kubernetes So Hard? 🌟](https://softwareengineeringdaily.com/2019/01/11/why-is-storage-on-kubernetes-is-so-hard)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: Compute and Storage Should Be Decoupled for Log Management' at Scale](https://thenewstack.io/why-compute-and-storage-should-be-decoupled-for-log-management-at-scale)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [gitlab.com: Kubernetes storage provider benchmarks](https://gitlab.com/mrman/k8s-storage-provider-benchmarks)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: Beyond Block and File: COSI Enables Object Storage in Kubernetes' 🌟](https://thenewstack.io/beyond-block-and-file-cosi-enables-object-storage-in-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: When Is Decentralized Storage the Right Choice?](https://thenewstack.io/when-is-decentralized-storage-the-right-choice)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: The Biggest Gap in Kubernetes Storage Architecture?](https://thenewstack.io/whats-the-biggest-gap-in-kubernetes-storage-architecture)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium: Provisioning storage in Kubernetes](https://medium.com/avmconsulting-blog/provisioning-storage-in-kubernetes-e1dc5610318d)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [kylezsembery.com: Persistent Storage in Kubernetes](https://www.kylezsembery.com/persistent-storage-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.mayadata.io: Container Attached Storage (CAS) vs. Software-Defined' Storage - Which One to Choose?](https://blog.mayadata.io/container-attached-storage-cas-vs.-software-defined-storage-which-one-to-choose)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: Stateful Workloads on Kubernetes with Container Attached' Storage 🌟](https://thenewstack.io/stateful-workloads-on-kubernetes-with-container-attached-storage)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [developers.redhat.com: How to maximize data storage for microservices and' Kubernetes, Part 1: An introduction 🌟](https://developers.redhat.com/articles/2021/08/11/how-maximize-data-storage-microservices-and-kubernetes-part-1-introduction)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.mayadata.io: Kubernetes storage basics: PV, PVC and StorageClass 🌟](https://blog.mayadata.io/kubernetes-storage-basics-pv-pvc-and-storageclass)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [ondat.io: Stateful Apps in Kubernetes are a big deal](https://www.ondat.io/blog/stateful-apps-in-kubernetes-are-a-big-deal)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [techgenix.com: Data Storage Management for Kubernetes - 5 movers and shakers](https://techgenix.com/data-storage-management-for-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: The Growth of State in Kubernetes](https://thenewstack.io/the-growth-of-state-in-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [itnext.io: Highly Available NFS cluster in Kubernetes, a cloud vendor independent' storage solution](https://itnext.io/highly-available-nfs-cluster-in-kubernetes-a-cloud-vendor-independent-storage-solution-f9a314cfdfcc)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [armosec.io: Data Storage in Kubernetes](https://www.armosec.io/blog/kubernetes-data-storage)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [infoq.com: Best Practices for Running Stateful Applications on Kubernetes](https://www.infoq.com/articles/kubernetes-stateful-applications)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/@amir.ilw: Kubernetes Storage Migration 🌟](https://medium.com/@amir.ilw/kubernetes-storage-migration-ac48f6f9f5a5)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [discoblocks.io 🌟](https://discoblocks.io)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/geekculture: Storage | Kubernetes](https://medium.com/geekculture/storage-kubernetes-92eb3d027282)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [itnext.io: Temporary Storage for Kubernetes Pods](https://itnext.io/temporary-storage-for-kubernetes-pods-f8330ad8db88)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/nerd-for-tech: Persistence with Kubernetes](https://medium.com/nerd-for-tech/persistence-with-kubernetes-46f039d9a2ad)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [cncf.io: Kubernetes storage is complex, but it’s getting better](https://www.cncf.io/blog/2023/03/28/kubernetes-storage-is-complex-but-its-getting-better)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [yuminlee2.medium.com: Kubernetes: Storage](https://yuminlee2.medium.com/kubernetes-storage-fe5363d88d42)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/kubernetes-deveops: Kubernetes — Deploying Application with Persistent' Storage](https://medium.com/kubernetes-deveops/kubernetes-deploying-application-with-persistent-storage-5068767e25f3)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [danielmangum.com: K8s ASA: The Storage Interface](https://danielmangum.com/posts/k8s-asa-the-storage-interface)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [kubermatic.com: Keeping the State of Apps 5: Introduction to Storage Classes](https://www.kubermatic.com/blog/keeping-the-state-of-apps-5-introduction-to-storage-classes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [itnext.io: Kubernetes: PersistentVolume and PersistentVolumeClaim — an overview' with examples](https://itnext.io/kubernetes-persistentvolume-and-persistentvolumeclaim-an-overview-with-examples-3c5688222f99)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: Persistent Volumes: Separating Compute and Storage](https://thenewstack.io/persistent-volumes-separating-compute-and-storage)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [developers.redhat.com: Persistent storage in action: Understanding Red Hat' OpenShift’s persistent volume framework 🌟](https://developers.redhat.com/blog/2020/10/22/persistent-storage-in-action-understanding-red-hat-openshifts-persistent-volume-framework)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [itnext.io: Resizing StatefulSet Persistent Volumes with zero downtime 🌟](https://itnext.io/resizing-statefulset-persistent-volumes-with-zero-downtime-916ebc65b1d4)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [github.com/kubernetes-sigs: Local Persistence Volume Static Provisioner' 🌟](https://github.com/kubernetes-sigs/sig-storage-local-static-provisioner) <span class='md-tag md-tag--info'>⭐ 1198</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [shuanglu1993.medium.com: What happens when volumeManager in the kubelet' starts?](https://shuanglu1993.medium.com/what-happens-when-volumemanager-in-the-kubelet-starts-1fea623ac6ce)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [linkedin.com/pulse: What are Kubernetes Persistent Volumes?](https://www.linkedin.com/pulse/what-kubernetes-persistent-volumes-gyan-prakash-1f)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/codex: Kubernetes Persistent Volume Explained](https://medium.com/codex/kubernetes-persistent-volume-explained-fb27df29c393)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [giffgaff.io: Resizing StatefulSet Persistent Volumes with zero downtime' 🌟](https://www.giffgaff.io/tech/resizing-statefulset-persistent-volumes-with-zero-downtime)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [kubermatic.com: Keeping the State of Apps 1: Introduction to Volume and' volumeMounts](https://www.kubermatic.com/blog/keeping-the-state-of-apps-1-introduction-to-volume-and-volumemounts)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.cloudnloud.com: Kubernetes Volume](https://blog.cloudnloud.com/kubernetes-volume)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [adamtheautomator.com: Effortless Storage Management With Kubernetes PVC' 🌟](https://adamtheautomator.com/kubernetes-pvc)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [portworx.com: Kubernetes Persistent Volume Tutorial by Portworx](https://portworx.com/tutorial-kubernetes-persistent-volumes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [openebs/zfs-localpv](https://github.com/openebs/zfs-localpv) <span class='md-tag md-tag--info'>⭐ 561</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [devineer.medium.com: Get to Grips with Kubernetes Volumes: A Practical Tutorial](https://devineer.medium.com/get-to-grips-with-kubernetes-volumes-a-practical-tutorial-c41853c64f02)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [airplane.dev: How to use Kubernetes ephemeral volumes & storage 🌟](https://www.airplane.dev/blog/kubernetes-ephemeral-storage)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.devgenius.io: When K8s pods are stuck mounting large volumes](https://blog.devgenius.io/when-k8s-pods-are-stuck-mounting-large-volumes-2915e6656cb8)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [spacelift.io: Kubernetes Persistent Volumes – Tutorial and Examples](https://spacelift.io/blog/kubernetes-persistent-volumes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [matthewpalmer.net: Filesystem vs Volume vs Persistent Volume 🌟](https://matthewpalmer.net/kubernetes-app-developer/articles/kubernetes-volumes-example-nfs-persistent-volume.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [dok.community: DoKC Data on Kubernetes](https://dok.community)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Create ReadWriteMany PersistentVolumeClaims on your Kubernetes Cluster 🌟](https://medium.com/asl19-developers/create-readwritemany-persistentvolumeclaims-on-your-kubernetes-cluster-3a8db51f98e3)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Digital Ocean: Kuberntes PVC ReadWriteMany access mode alternative](https://www.digitalocean.com/community/questions/kuberntes-pvc-readwritemany-access-mode-alternative)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [itnext.io: State of Persistent Storage in K8s — A Benchmark](https://itnext.io/state-of-persistent-storage-in-k8s-a-benchmark-77a96bb1ac29)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [itnext.io: Using Rook On A K3s Cluster](https://itnext.io/using-rook-on-a-k3s-cluster-8a97a75ba25e)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/@abdulfayis: storage Orchestration for Kubernetes](https://medium.com/@abdulfayis/storage-orchestration-for-kubernetes-c6370f943e23)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Robin](https://robin.io)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Reduxio](https://www.reduxio.com)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Portworx](https://portworx.com)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [OpenEBS](https://openebs.io)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [MayaData](https://mayadata.io)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [goglides.io: Running OpenEBS in Kubernetes](https://goglides.io/running-openebs-in-kubernetes/371)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [openebs/dynamic-localpv-provisioner: Dynamic Kubernetes Local Persistent' Volumes](https://github.com/openebs/dynamic-localpv-provisioner) <span class='md-tag md-tag--info'>⭐ 207</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [openebs/lvm-localpv](https://github.com/openebs/lvm-localpv) <span class='md-tag md-tag--info'>⭐ 341</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [LightOS](https://www.lightbitslabs.com/product)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Longhorn](https://longhorn.io)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: Rancher Donates its ‘Longhorn’ Kubernetes Persistent Storage' Software to CNCF](https://thenewstack.io/rancher-donates-its-longhorn-kubernetes-persistent-storage-software-to-cncf)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [aesher9o1.medium.com: Autoscale large images faster using Longhorn (distributed' storage)](https://aesher9o1.medium.com/autoscale-large-images-faster-using-longhorn-distributed-storage-618d0cf01ba2)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/@abdelrhmanahmed131: Longhorn — Distributed Block Storage for' K8s](https://medium.com/@abdelrhmanahmed131/longhorn-distributed-block-storage-for-k8s-2ea11df400d1)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [linbit.com: LINSTOR - kubernetes persistent container storage](https://linbit.com/kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [iomesh.com](https://www.iomesh.com)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [iomesh.com: Outperforming Peer Products, IOMesh Takes Cloud Native Storage' to the Next Level](https://www.iomesh.com/blog/announcing_iomesh_preview)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [docs.netapp.com: Intro to Astra Data Store preview](https://docs.netapp.com/us-en/astra-data-store/concepts/intro.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [libopenstorage/stork: Stork - Storage Operator Runtime for Kubernetes](https://github.com/libopenstorage/stork) <span class='md-tag md-tag--info'>⭐ 401</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Curve: opencurve.io](https://opencurve.io)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [simplyblock: simplyblock.io](https://simplyblock.io)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [kubernetes-csi.github.io](https://kubernetes-csi.github.io)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [github.com/kubernetes-csi](https://github.com/kubernetes-csi)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [SMB CSI Driver for Kubernetes](https://github.com/kubernetes-csi/csi-driver-smb) <span class='md-tag md-tag--info'>⭐ 639</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [github.com/yandex-cloud: CSI for S3](https://github.com/yandex-cloud/k8s-csi-s3) <span class='md-tag md-tag--info'>⭐ 855</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [sklar.rocks: How the CSI (Container Storage Interface) Works](https://sklar.rocks/how-container-storage-interface-works)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.kasten.io: Benchmarking and Evaluating Your Kubernetes Storage with' Kubestr](https://blog.kasten.io/benchmarking-kubernetes-storage-with-kubestr)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [next.redhat.com: Introducing VolSync: your data, anywhere](https://next.redhat.com/2021/08/23/introducing-volsync-your-data-anywhere)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Discoblocks: ondat.io/discoblocks](https://www.ondat.io/discoblocks)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>

## Cloud Infrastructure

### Storage

#### Distributed Filesystems

  - [Ceph: A Distributed Object, Block, and File Storage Platform](https://github.com/ceph/ceph) <span class='md-tag md-tag--info'>⭐ 16621</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The industry-standard unified, distributed storage system designed to provide excellent performance, reliability, and scalability.

*   Provides object, block, and file storage within a single cluster.
*   Acts as a foundational storage engine for large-scale Kubernetes PV platforms (Rook-Ceph) and private clouds.

---
💡 **Explore Related:** [Container Managers](./container-managers.md) | [Kubernetes Monitoring](./kubernetes-monitoring.md) | [Kubernetes Troubleshooting](./kubernetes-troubleshooting.md)

