# Kubernetes Storage. Cloud Native Storage

1. [Introduction](#introduction)
2. [Kubernetes Storage API Interface](#kubernetes-storage-api-interface)
3. [Kubernetes Storage Classes](#kubernetes-storage-classes)
4. [Kubernetes Volumes](#kubernetes-volumes)
    1. [Kubernetes Volumes Guide](#kubernetes-volumes-guide)
5. [DoK Community](#dok-community)
6. [ReadWriteMany PersistentVolumeClaims](#readwritemany-persistentvolumeclaims)
7. [Ebooks](#ebooks)
8. [Cloud Native Storage Solutions](#cloud-native-storage-solutions)
    1. [Rook](#rook)
    2. [Robin](#robin)
    3. [Reduxio](#reduxio)
    4. [Portworx](#portworx)
    5. [StorageOS](#storageos)
    6. [OpenEBS](#openebs)
    7. [LightOS](#lightos)
    8. [Longhorn](#longhorn)
    9. [IBM Spectrum Storage Suite](#ibm-spectrum-storage-suite)
    10. [Linbit](#linbit)
    11. [Kadalu](#kadalu)
    12. [IOMesh](#iomesh)
    13. [MinIO](#minio)
    14. [NetApp Data Store](#netapp-data-store)
    15. [Stork Storage Operator](#stork-storage-operator)
    16. [Curve - OpenCurve](#curve---opencurve)
    17. [simplyblock](#simplyblock)
9. [OpenShift Container Storage Operator (OCS)](#openshift-container-storage-operator-ocs)
    1. [OCS 3 (OpenShift 3)](#ocs-3-openshift-3)
    2. [OCS 4 (OpenShift 4)](#ocs-4-openshift-4)
10. [Kubernetes CSI](#kubernetes-csi)
11. [Kubestr](#kubestr)
12. [VolSync](#volsync)
13. [Discoblocks](#discoblocks)
14. [Images](#images)
15. [Tweets](#tweets)
16. [Videos](#videos)

## Introduction

- [thenewstack.io: How Kubernetes provides networking and storage to applications](https://thenewstack.io/how-kubernetes-provides-networking-and-storage-to-applications/)
- [medium: Kubernetes Storage Explained 🌟](https://medium.com/swlh/kubernetes-storage-explained-558e85596d0c) kubernetes/volumes/claims
- [thenewstack.io: A Guide to Running Stateful Applications in Kubernetes](https://thenewstack.io/a-guide-to-running-stateful-applications-in-kubernetes/)
- [forbes.com: 5 Cloud Native Storage Startups To Watch Out For In 2019](https://www.forbes.com/sites/janakirammsv/2019/06/28/5-cloud-native-storage-startups-to-watch-out-for-in-2019/)
- [medium: Solution architect’s guide to Kubernetes persistent storage](https://medium.com/weareservian/solution-architects-guide-to-kubernetes-persistant-storage-3c9660187e8f)
- [howtoforge.com: Storage in Kubernetes 🌟](https://www.howtoforge.com/storage-in-kubernetes/)
- [cncf.io: Container Attached Storage is Cloud Native Storage (CAS)](https://www.cncf.io/blog/2020/09/22/container-attached-storage-is-cloud-native-storage-cas/)
- [thenewstack.io: The most popular cloud native solutions 🌟](https://thenewstack.io/the-most-popular-cloud-native-storage-solutions/)
- [medium: Kubernetes Storage Performance Comparison v2 (2020 Updated) 🌟](https://medium.com/volterra-io/kubernetes-storage-performance-comparison-v2-2020-updated-1c0b69f0dcf4)
- [blocksandfiles.com: geless storage is the ‘answer’ to Kubernetes data challenges](https://blocksandfiles.com/2020/12/22/the-storageless-storage-paradox/)
- [rancher.com: What is Cloud-Native Storage?](https://rancher.com/blog/2020/what-is-cloud-native-storage)
- [softwareengineeringdaily.com: Why Is Storage On Kubernetes So Hard? 🌟](https://softwareengineeringdaily.com/2019/01/11/why-is-storage-on-kubernetes-is-so-hard/)
- [devopscurry.com: Top 7 Object Storage tools to consider in 2021](https://devopscurry.com/top-7-object-storage-tools-to-consider-in-2021/)
- [thenewstack.io: Compute and Storage Should Be Decoupled for Log Management at Scale](https://thenewstack.io/why-compute-and-storage-should-be-decoupled-for-log-management-at-scale/)
- [blog.min.io: Why Kubernetes Managed Object Storage Matters](https://blog.min.io/why-kubernetes-managed/)
- [gitlab.com: Kubernetes storage provider benchmarks](https://gitlab.com/mrman/k8s-storage-provider-benchmarks)
- [ibm.com: Using Fio to Tell Whether Your Storage is Fast Enough for Etcd](https://www.ibm.com/cloud/blog/using-fio-to-tell-whether-your-storage-is-fast-enough-for-etcd)
- [marketplace.redhat.com: Dont treat Kubernetes storage as an afterthought: Turn to persistent container storage for high performance and availability](https://marketplace.redhat.com/en-us/blog/dont-treat-kubernetes-storage-as-an-afterthought)
- [thenewstack.io: Beyond Block and File: COSI Enables Object Storage in Kubernetes 🌟](https://thenewstack.io/beyond-block-and-file-cosi-enables-object-storage-in-kubernetes)
- [thenewstack.io: When Is Decentralized Storage the Right Choice?](https://thenewstack.io/when-is-decentralized-storage-the-right-choice/)
- [storj.io: Integrating Decentralized Cloud Storage with Duplicati](https://www.storj.io/blog/integrating-decentralized-cloud-storage-with-duplicati)
- [thenewstack.io: The Biggest Gap in Kubernetes Storage Architecture?](https://thenewstack.io/whats-the-biggest-gap-in-kubernetes-storage-architecture/)
- [medium: Provisioning storage in Kubernetes](https://medium.com/avmconsulting-blog/provisioning-storage-in-kubernetes-e1dc5610318d)
- [kylezsembery.com: Persistent Storage in Kubernetes](https://www.kylezsembery.com/persistent-storage-kubernetes/) In this post I’ll briefly explain how persistent storage works in Kubernetes.
- [blog.mayadata.io: Container Attached Storage (CAS) vs. Software-Defined Storage - Which One to Choose?](https://blog.mayadata.io/container-attached-storage-cas-vs.-software-defined-storage-which-one-to-choose)
- [thenewstack.io: Stateful Workloads on Kubernetes with Container Attached Storage 🌟](https://thenewstack.io/stateful-workloads-on-kubernetes-with-container-attached-storage/)
- [developers.redhat.com: How to maximize data storage for microservices and Kubernetes, Part 1: An introduction 🌟](https://developers.redhat.com/articles/2021/08/11/how-maximize-data-storage-microservices-and-kubernetes-part-1-introduction)
- [blog.mayadata.io: Kubernetes storage basics: PV, PVC and StorageClass 🌟](https://blog.mayadata.io/kubernetes-storage-basics-pv-pvc-and-storageclass)
- [infoworld.com: Kubernetes object storage best practices](https://www.infoworld.com/article/3635148/kubernetes-object-storage-best-practices.html) Like Kubernetes itself, the underlying object storage should be distributed, decoupled, declarative, and immutable.
- [ondat.io: Stateful Apps in Kubernetes are a big deal](https://www.ondat.io/blog/stateful-apps-in-kubernetes-are-a-big-deal)
- [techgenix.com: Data Storage Management for Kubernetes - 5 movers and shakers](https://techgenix.com/data-storage-management-for-kubernetes/)
- [==thenewstack.io: The Growth of State in Kubernetes==](https://thenewstack.io/the-growth-of-state-in-kubernetes/)
- [itnext.io: Highly Available NFS cluster in Kubernetes, a cloud vendor independent storage solution](https://itnext.io/highly-available-nfs-cluster-in-kubernetes-a-cloud-vendor-independent-storage-solution-f9a314cfdfcc)
- [armosec.io: Data Storage in Kubernetes](https://www.armosec.io/blog/kubernetes-data-storage/) Kubernetes in cooperation with cloud vendor infrastructure provides flexible mechanisms for data storage and management. It is up to the users to decide which mechanism best fits their application needs. However, the security side of the data storage falls completely under the user’s responsibility. Most of the default settings are wide open and require significant security expertise to protect your applications from data leakage.
- [==infoq.com: Best Practices for Running Stateful Applications on Kubernetes==](https://www.infoq.com/articles/kubernetes-stateful-applications/)
- [blog.flant.com: Comparing Ceph, LINSTOR, Mayastor, and Vitastor storage performance in Kubernetes](https://blog.flant.com/kubernetes-storage-performance-linstor-ceph-mayastor-vitastor/) Are you looking for an easy-to-use, reliable block-type storage for your cluster?
- [medium.com/@amir.ilw: Kubernetes Storage Migration 🌟](https://medium.com/@amir.ilw/kubernetes-storage-migration-ac48f6f9f5a5) Storage migrations, storage path changes or even moving to a newer faster CSI can be overwhelming. In this article, you'll learn the required steps, how to avoid the pitfalls of immutable volumes and how to plan your next migration.
- [discoblocks.io 🌟](https://discoblocks.io) - [ondat/discoblocks](https://github.com/ondat/discoblocks) **Open Source declarative disk configuration system for Kubernetes.** Discoblocks is an open-source declarative disk configuration system for Kubernetes helping to automate CRUD (Create, Read, Update, Delete) operations for cloud disk device resources attached to Kubernetes cluster nodes.
- [medium.com/geekculture: Storage | Kubernetes](https://medium.com/geekculture/storage-kubernetes-92eb3d027282) A Deep Dive into Kubernetes Storage
- [itnext.io: Temporary Storage for Kubernetes Pods](https://itnext.io/temporary-storage-for-kubernetes-pods-f8330ad8db88) Or emptyDir vs. container File System. Kubernetes applications might need some temporary storage that could be discarded after a container is stopped/removed. In this article, you will compare emptyDir and the container's local storage.
- [==container-object-storage-interface.github.io: Kubernetes COSI==](https://container-object-storage-interface.github.io/) Kubernetes Container Object Storage Interface (COSI) is a standard for exposing object storage to containerized workloads running in Kubernetes. COSI is meant to be a departure from the CSI since the latter does not work well with object storage.
- [containiq.com: Kubernetes Ephemeral Volumes & Storage | Tutorial](https://www.containiq.com/post/kubernetes-ephemeral-storage) In this article, we’ll discuss how Kubernetes handles ephemeral storage and learn how these volumes are provisioned in operating clusters.
- [medium.com/nerd-for-tech: Persistence with Kubernetes](https://medium.com/nerd-for-tech/persistence-with-kubernetes-46f039d9a2ad)
- [cncf.io: Kubernetes storage is complex, but it’s getting better](https://www.cncf.io/blog/2023/03/28/kubernetes-storage-is-complex-but-its-getting-better/)
- [==yuminlee2.medium.com: Kubernetes: Storage==](https://yuminlee2.medium.com/kubernetes-storage-fe5363d88d42) **In Kubernetes, pods are temporary and any data stored within them is lost when they’re deleted or restarted. To avoid this, use persistent storage options such as PVs(Persistent Volumes)and PVCs(Persistent Volume Claims). PVs are storage resources with an independent lifecycle, while PVCs are requests for storage. Use them for simplified storage management and scaling. Provisioning persistent volumes can be static or dynamic. StorageClass defines the provisioner, parameters, and reclaim policy for dynamically provisioned PVs.**
- [medium.com/kubernetes-deveops: Kubernetes — Deploying Application with Persistent Storage](https://medium.com/kubernetes-deveops/kubernetes-deploying-application-with-persistent-storage-5068767e25f3) Implementing Storage Controller for Auto-Provisioning

## Kubernetes Storage API Interface

- [danielmangum.com: K8s ASA: The Storage Interface](https://danielmangum.com/posts/k8s-asa-the-storage-interface/) The primary function of the Kubernetes API Server is to ingest data, store it, and then return it when requested. In this article, you will learn how the API Server stores data.

## Kubernetes Storage Classes

- [==kubermatic.com: Keeping the State of Apps 5: Introduction to Storage Classes==](https://www.kubermatic.com/blog/keeping-the-state-of-apps-5-introduction-to-storage-classes/)
- [==containiq.com: Kubernetes Storage Classes | In-Depth Tutorial==](https://www.containiq.com/post/kubernetes-storage-classes) Storage Classes are an essential part of Kubernetes, and can provide a great deal of flexibility and control over how your data is stored. In this guide, we provide an in-depth tutorial on using storage classes effectively.

## Kubernetes Volumes

- [itnext.io: Kubernetes: PersistentVolume and PersistentVolumeClaim — an overview with examples](https://itnext.io/kubernetes-persistentvolume-and-persistentvolumeclaim-an-overview-with-examples-3c5688222f99)
- [thenewstack.io: Persistent Volumes: Separating Compute and Storage](https://thenewstack.io/persistent-volumes-separating-compute-and-storage/)
- [developers.redhat.com: Persistent storage in action: Understanding Red Hat OpenShift’s persistent volume framework 🌟](https://developers.redhat.com/blog/2020/10/22/persistent-storage-in-action-understanding-red-hat-openshifts-persistent-volume-framework/)
- [itnext.io: Resizing StatefulSet Persistent Volumes with zero downtime 🌟](https://itnext.io/resizing-statefulset-persistent-volumes-with-zero-downtime-916ebc65b1d4)
- [github.com/kubernetes-sigs: Local Persistence Volume Static Provisioner 🌟](https://github.com/kubernetes-sigs/sig-storage-local-static-provisioner) **The local volume static provisioner manages PersistentVolume lifecycle for pre-allocated disks by detecting and creating PVs for each local disk on the host and cleaning up the disks when released. It does not support dynamic provisioning**
- [shuanglu1993.medium.com: What happens when volumeManager in the kubelet starts?](https://shuanglu1993.medium.com/what-happens-when-volumemanager-in-the-kubelet-starts-1fea623ac6ce) In this deep-dive, you will learn how the volumeManager sync loop is initialized and starts 3 async calls to maintain the objects 'desiredStateOfWorld' and 'actualStateOfWorld' and 'reconcile' the volumes on the node to the desired state.
- [linkedin.com/pulse: What are Kubernetes Persistent Volumes?](https://www.linkedin.com/pulse/what-kubernetes-persistent-volumes-gyan-prakash-1f/)
- [blog.newrelic.com: Kubernetes Fundamentals, Part 5: Working with Kubernetes Volumes](https://blog.newrelic.com/engineering/how-to-use-kubernetes-volumes/)
- [==medium.com/codex: Kubernetes Persistent Volume Explained==](https://medium.com/codex/kubernetes-persistent-volume-explained-fb27df29c393) Learn what a Persistent Volume is and how to create a persistent volume from a storage class. Then, learn how to create a persistent volume claim and how to attach the PVC to a Pod:
    - How to create a persistent volume from a storage class
    - How to create a persistent volume claim
    - How to attach the PVC to a Pod
- [giffgaff.io: Resizing StatefulSet Persistent Volumes with zero downtime 🌟](https://www.giffgaff.io/tech/resizing-statefulset-persistent-volumes-with-zero-downtime)
- [kubermatic.com: Keeping the State of Apps 1: Introduction to Volume and volumeMounts](https://www.kubermatic.com/blog/keeping-the-state-of-apps-1-introduction-to-volume-and-volumemounts) In this blog post, you will get a hands-on practice and learn how to provide persistent storage in the form of different volumes to the Pods.
- [blog.cloudnloud.com: Kubernetes Volume](https://blog.cloudnloud.com/kubernetes-volume)
- [==adamtheautomator.com: Effortless Storage Management With Kubernetes PVC== 🌟](https://adamtheautomator.com/kubernetes-pvc/) In this tutorial, you'll learn about Kubernetes PVC and set up a persistent volume for a MySQL database. You'll also confirm that the data persists even after deleting and recreating the pods.
- [==faun.pub: Dynamic Volume Provisioning | Kubernetes== 🌟](https://faun.pub/dynamic-volume-provisioning-kubernetes-632b43b1ee79) Dynamically provision persistent volume on Kubernetes
- [portworx.com: Kubernetes Persistent Volume Tutorial by Portworx](https://portworx.com/tutorial-kubernetes-persistent-volumes/)
    - What is K8s PV?
    - How do they differ from k8s volumes?
    - Why would you use persistent volumes?
    - How to get started using persistent volumes?
- [openebs/zfs-localpv](https://github.com/openebs/zfs-localpv) CSI Driver for dynamic provisioning of Persistent Local Volumes for Kubernetes using ZFS.
- [devineer.medium.com: Get to Grips with Kubernetes Volumes: A Practical Tutorial](https://devineer.medium.com/get-to-grips-with-kubernetes-volumes-a-practical-tutorial-c41853c64f02)
- [airplane.dev: How to use Kubernetes ephemeral volumes & storage 🌟](https://www.airplane.dev/blog/kubernetes-ephemeral-storage) This tutorial will discuss how Kubernetes handles ephemeral storage and how these volumes are provisioned in operating clusters.
- [blog.devgenius.io: When K8s pods are stuck mounting large volumes](https://blog.devgenius.io/when-k8s-pods-are-stuck-mounting-large-volumes-2915e6656cb8)
- [spacelift.io: Kubernetes Persistent Volumes – Tutorial and Examples](https://spacelift.io/blog/kubernetes-persistent-volumes)

### Kubernetes Volumes Guide

- [matthewpalmer.net: Filesystem vs Volume vs Persistent Volume 🌟](https://matthewpalmer.net/kubernetes-app-developer/articles/kubernetes-volumes-example-nfs-persistent-volume.html) This is a guide that covers:
    - How to set up and use volumes in Kubernetes
    - What are persistent volumes, and how to use them
    - How to use an NFS volume
    - Shared data and volumes between pods

## DoK Community

- [==DoK Community== 🌟](https://dok.community)
- Kubernetes was originally designed to run stateless workloads. Today, it is increasingly used to run databases and other stateful workloads. Yet despite the success of these early adopters, there remain few known good practices for running data on Kubernetes.
- After discussions with thousands of companies and individuals running data workloads on Kubernetes we’ve come to see that there is a need for a sharing of patterns and concerns about how to build and operate data-centric applications on Kubernetes. As a result, the **Data on Kubernetes Community (DoKC)** was born.
- [==dok.community: Data on Kubernetes 2021== 🌟](https://dok.community/dokc-2021-report/) Insights from over 500 executives and technology leaders on how Kubernetes is being used for data and the factors driving further adoption

## ReadWriteMany PersistentVolumeClaims

- [Create ReadWriteMany PersistentVolumeClaims on your Kubernetes Cluster 🌟](https://medium.com/asl19-developers/create-readwritemany-persistentvolumeclaims-on-your-kubernetes-cluster-3a8db51f98e3) Kubernetes allows us to provision our PersistentVolumes dynamically using PersistentVolumeClaims. Pods treat these claims as volumes. The access mode of the PVC determines how many nodes can establish a connection to it. We can refer to the resource provider’s docs for their supported access modes.
- [Digital Ocean: Kuberntes PVC ReadWriteMany access mode alternative](https://www.digitalocean.com/community/questions/kuberntes-pvc-readwritemany-access-mode-alternative)

## Ebooks

- [redhat.com: Storage Patterns for Kubernetes for dummies](https://www.redhat.com/en/engage/kubernetes-containers-storage-s-201911201051)

## Cloud Native Storage Solutions

- [itnext.io: State of Persistent Storage in K8s — A Benchmark](https://itnext.io/state-of-persistent-storage-in-k8s-a-benchmark-77a96bb1ac29)

### Rook

- [Rook](https://rook.io/)
- [itnext.io: Using Rook On A K3s Cluster](https://itnext.io/using-rook-on-a-k3s-cluster-8a97a75ba25e)
- [documentation.suse.com: Rook Best Practices for running Ceph on Kubernetes (PDF)](https://documentation.suse.com/sbp/all/pdf/SBP-rook-ceph-kubernetes_color_en.pdf)
- [medium.com/@abdulfayis: storage Orchestration for Kubernetes](https://medium.com/@abdulfayis/storage-orchestration-for-kubernetes-c6370f943e23)

### Robin

- [Robin](https://robin.io/)

### Reduxio

- [Reduxio](https://www.reduxio.com/)

### Portworx

- [Portworx](https://portworx.com/)

### StorageOS

- [StorageOS](https://storageos.com/)

### OpenEBS

- [OpenEBS](https://openebs.io/) extends the benefits of software-defined storage to cloud native through the container attached approach.
- [MayaData](https://mayadata.io/) Founder of OpenEBS
- [goglides.io: Running OpenEBS in Kubernetes](https://goglides.io/running-openebs-in-kubernetes/371/)
- [OpenEBS Features and Benefits](https://docs.openebs.io/docs/next/features.html) OpenEBS is cloudnative storage for stateful applications on K8s where "cloud native" means following a loosely coupled architecture. As such the normal benefits to cloud native, loosely coupled architectures apply.
- [openebs/dynamic-localpv-provisioner: Dynamic Kubernetes Local Persistent Volumes](https://github.com/openebs/dynamic-localpv-provisioner) Dynamic Local Volumes for Kubernetes Stateful workloads.
- [openebs/lvm-localpv](https://github.com/openebs/lvm-localpv) CSI Driver for dynamic provisioning of Persistent Local Volumes for Kubernetes using LVM.

### LightOS

- [LightOS](https://www.lightbitslabs.com/product/)
- [blocksandfiles.com: Lightbits Labs adds Kubernetes table stakes: CSI support](https://blocksandfiles.com/2020/06/23/lightbits-labs-adds-kubernetes-table-stakes-csi-support/)

### Longhorn

- [Longhorn](https://longhorn.io/)
- [thenewstack.io: Rancher Donates its ‘Longhorn’ Kubernetes Persistent Storage Software to CNCF](https://thenewstack.io/rancher-donates-its-longhorn-kubernetes-persistent-storage-software-to-cncf/). Gluster and Ceph were “designed to be run by some storage admin. In the Kubernetes world, a lot of these things tend to be deployed by DevOps teams, so (the storage layer) needs to be a lot more lightweight and a lot simpler.” — Rancher Labs CEO Sheng Liang.
- [Longhorn Simplifies Distributed Block Storage in Kubernetes](https://rancher.com/blog/2020/longhorn-container-storage)
- [containerjournal.com: Rancher Labs Adds Support for Longhorn Storage on Kubernetes Clusters](https://containerjournal.com/topics/container-management/rancher-labs-adds-support-for-longhorn-storage-on-kubernetes-clusters/)
- [aesher9o1.medium.com: Autoscale large images faster using Longhorn (distributed storage)](https://aesher9o1.medium.com/autoscale-large-images-faster-using-longhorn-distributed-storage-618d0cf01ba2)
- [medium.com/@abdelrhmanahmed131: Longhorn — Distributed Block Storage for K8s](https://medium.com/@abdelrhmanahmed131/longhorn-distributed-block-storage-for-k8s-2ea11df400d1)

### IBM Spectrum Storage Suite

- [IBM Spectrum](https://www.ibm.com/it-infrastructure/storage/spectrum) IBM Spectrum Storage software for data-driven architecture. A complete storage software family with AI-infused capability that changes the economics of storage on-prem and in the hybrid multicloud.
- [redbooks.ibm.com: IBM Storage for Red Hat OpenShift. IBM block storage & IBM Spectrum Scale](http://www.redbooks.ibm.com/abstracts/redp5565.html)
- [searchstorage.techtarget.com: IBM Spectrum](https://searchstorage.techtarget.com/definition/IBM-Spectrum)

### Linbit

- [linbit.com: LINSTOR - kubernetes persistent container storage](https://linbit.com/kubernetes/)

### Kadalu

- [Kadalu](https://github.com/kadalu/kadalu) A lightweight Persistent storage solution for Kubernetes / OpenShift using GlusterFS in background. **Kadalu is a project to provide Persistent Storage in Kubernetes. The Kadalu operator deploys CSI pods, and gluster storage pods**

### IOMesh

- [iomesh.com](https://www.iomesh.com/)
- [blocksandfiles.com: Kubernetes storage: SmartX’s IOMesh beats Portworx, Longhorn and OpenEBS](https://blocksandfiles.com/2021/08/05/kubernetes-storage-chinese-vendor-smartxs-iomesh-beats-portworx-longhorn-and-openebs/)
- [iomesh.com: Outperforming Peer Products, IOMesh Takes Cloud Native Storage to the Next Level](https://www.iomesh.com/blog/announcing_iomesh_preview)

### MinIO

- [min.io](https://min.io) Multi-Cloud Object Storage. MinIO offers high-performance, S3 compatible object storage. Native to Kubernetes, MinIO is the only object storage suite available on every public cloud, every Kubernetes distribution, the private cloud and the
edge. MinIO is software-defined and is 100% open source under GNU AGPL v3.
- [blog.min.io: Best Practices for Kubernetes Object Storage](https://blog.min.io/best-practices-for-kubernetes-object-storage/)
- [blog.min.io: Cloud-Native Object Storage Architectures: Single-Tenant vs Multi-Tenant](https://blog.min.io/single-vs-multi-tenant)

### NetApp Data Store

- [docs.netapp.com: Intro to Astra Data Store preview](https://docs.netapp.com/us-en/astra-data-store/concepts/intro.html)

### Stork Storage Operator

- [libopenstorage/stork: Stork - Storage Operator Runtime for Kubernetes](https://github.com/libopenstorage/stork) Stork - Storage Orchestration Runtime for Kubernetes

### Curve - OpenCurve

- [Curve: opencurve.io](https://opencurve.io) Curve is a high-performance, lightweight-operation, cloud-native open source distributed storage system for Kubernetes/OpenStack. Curve can also be used as a cloud storage middleware using S3-compatible object storage as a data storage engine.

### simplyblock

- [simplyblock: simplyblock.io](https://simplyblock.io) Simplyblock is a NVMe over TCP (NVMe/TCP) based disaggregated and cloud-native storage solution with high-performance and predictable low latency block storage for Kubernetes.

## OpenShift Container Storage Operator (OCS)

- [State of OpenShift Container Storage](https://www.openshift.com/blog/state-of-openshift-container-storage-eran-tamir-and-duncan-hardie-red-hat)

### OCS 3 (OpenShift 3)

- OpenShift Container Storage based on [GlusterFS](https://www.gluster.org/) technology.
- Not OpenShift 4 compliant: Migration tooling will be available to facilitate the move to OCS 4.x (OpenShift Gluster APP Mitration Tool).

### OCS 4 (OpenShift 4)

- **OCS Operator** based on Rook.io with Operator LifeCycle Manager (OLM).
- Tech Stack:
    - [Rook](https://rook.io) (don't confuse this with non-redhat ["Rook Ceph"](https://operatorhub.io/operator/rook-ceph) -> [RH ref](https://www.redhat.com/en/blog/rook-ceph-storage-operator-now-operatorhubio)).
        - Replaces [Heketi](https://github.com/heketi/heketi)  (OpenShift 3)
        - Uses **Red Hat Ceph Storage** and **Noobaa**.
    - [Red Hat Ceph Storage](https://ceph.io)
    - [Noobaa](https://www.noobaa.io):
        - Red Hat Multi Cloud Gateway (AWS, Azure, GCP, etc)
        - Asynchronous replication of data between my local ceph and my cloud provider
        - Deduplication
        - Compression
        - Encryption
- Backups available in OpenShift 4.2+ (Snapshots + Restore of Volumes)
- OCS Dashboard in OCS Operator

## Kubernetes CSI

- [kubernetes-csi.github.io](https://kubernetes-csi.github.io) Kubernetes-CSI is a community repository containing projects to enable CSI support in Kubernetes.
- [github.com/kubernetes-csi](https://github.com/kubernetes-csi) Kubernetes specific Container-Storage-Interface (CSI) components
- [SMB CSI Driver for Kubernetes](https://github.com/kubernetes-csi/csi-driver-smb) This driver allows Kubernetes to access SMB Server on both Linux and Windows nodes.
- [github.com/yandex-cloud: CSI for S3](https://github.com/yandex-cloud/k8s-csi-s3) This is a Container Storage Interface (CSI) for S3 (or S3 compatible) storage. This can dynamically allocate buckets and mount them via a fuse mount into any container.
- [sklar.rocks: How the CSI (Container Storage Interface) Works](https://sklar.rocks/how-container-storage-interface-works/)

## Kubestr

- [kubestr.io](https://kubestr.io/) Kubestr is a collection of tools to discover, validate and evaluate your kubernetes storage options.
- [blog.kasten.io: Benchmarking and Evaluating Your Kubernetes Storage with Kubestr](https://blog.kasten.io/benchmarking-kubernetes-storage-with-kubestr)

## VolSync

- [VolSync 🌟](https://github.com/backube/volsync) Asynchronous data replication for Kubernetes volumes. VolSync asynchronously replicates Kubernetes persistent volumes between clusters using either rsync or rclone. It also supports creating backups of persistent volumes via restic.
- [next.redhat.com: Introducing VolSync: your data, anywhere](https://next.redhat.com/2021/08/23/introducing-volsync-your-data-anywhere/) VolSync, a new storage-agnostic utility for exporting and importing objects from one Kubernetes namespace to another, even across clusters!

## Discoblocks

- [Discoblocks: ondat.io/discoblocks](https://www.ondat.io/discoblocks) - [github.com/ondat/discoblocks](https://github.com/ondat/discoblocks) Discoblocks is an open-source declarative disk configuration system for Kubernetes helping to automate CRUD (Create, Read, Update, Delete) operations for cloud disk device resources attached to Kubernetes cluster nodes.

## Images

??? note "Click to expand!"

    <center>
    [![gigaom radar report on storage](images/gigaom_radar_report_on_data_storage_for_k8s.png)](https://gigaom.com/report/gigaom-radar-for-data-storage-for-kubernetes/)
    </center>

## Tweets

??? note "Click to expand!"

    <center>
    <blockquote class="twitter-tweet"><p lang="en" dir="ltr">General rule of thumb: there is no such thing as persistent storage in Kubernetes.</p>&mdash; Richard North (@whichrich) <a href="https://twitter.com/whichrich/status/1479435059715321856?ref_src=twsrc%5Etfw">January 7, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
    </center>

## Videos

??? note "Click to expand!"

    <center>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/0swOh5C3OVM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </center>
