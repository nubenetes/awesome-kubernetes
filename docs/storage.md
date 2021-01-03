# Cloud Native Storage
- [Introduction](#introduction)
- [Ebooks](#ebooks)
- [Cloud Native Storage Solutions](#cloud-native-storage-solutions)
	- [Rook](#rook)
	- [Robin](#robin)
	- [Reduxio](#reduxio)
	- [Portworx](#portworx)
	- [StorageOS](#storageos)
	- [OpenEBS](#openebs)
	- [LightOS](#lightos)
	- [Longhorn](#longhorn)
	- [IBM Spectrum Storage Suite](#ibm-spectrum-storage-suite)
- [OpenShift Container Storage Operator (OCS)](#openshift-container-storage-operator-ocs)
	- [OCS 3 (OpenShift 3)](#ocs-3-openshift-3)
	- [OCS 4 (OpenShift 4)](#ocs-4-openshift-4)

## Introduction
- [thenewstack.io: A Guide to Running Stateful Applications in Kubernetes](https://thenewstack.io/a-guide-to-running-stateful-applications-in-kubernetes/)
- [forbes.com: 5 Cloud Native Storage Startups To Watch Out For In 2019](https://www.forbes.com/sites/janakirammsv/2019/06/28/5-cloud-native-storage-startups-to-watch-out-for-in-2019/)
- [thenewstack.io: Persistent Volumes: Separating Compute and Storage](https://thenewstack.io/persistent-volumes-separating-compute-and-storage/)
- [medium: Solution architect’s guide to Kubernetes persistent storage](https://medium.com/weareservian/solution-architects-guide-to-kubernetes-persistant-storage-3c9660187e8f)
- [howtoforge.com: Storage in Kubernetes 🌟](https://www.howtoforge.com/storage-in-kubernetes/)
- [cncf.io: Container Attached Storage is Cloud Native Storage (CAS)](https://www.cncf.io/blog/2020/09/22/container-attached-storage-is-cloud-native-storage-cas/)
- [thenewstack.io: The most popular cloud native solutions 🌟](https://thenewstack.io/the-most-popular-cloud-native-storage-solutions/)
- [medium: Kubernetes Storage Performance Comparison v2 (2020 Updated) 🌟](https://medium.com/volterra-io/kubernetes-storage-performance-comparison-v2-2020-updated-1c0b69f0dcf4)
- [blocksandfiles.com: geless storage is the ‘answer’ to Kubernetes data challenges](https://blocksandfiles.com/2020/12/22/the-storageless-storage-paradox/)
- [developers.redhat.com: Persistent storage in action: Understanding Red Hat OpenShift’s persistent volume framework 🌟](https://developers.redhat.com/blog/2020/10/22/persistent-storage-in-action-understanding-red-hat-openshifts-persistent-volume-framework/)
- [rancher.com: What is Cloud-Native Storage?](https://rancher.com/blog/2020/what-is-cloud-native-storage)
- [softwareengineeringdaily.com: Why Is Storage On Kubernetes So Hard? 🌟](https://softwareengineeringdaily.com/2019/01/11/why-is-storage-on-kubernetes-is-so-hard/)

## Ebooks
- [redhat.com: Storage Patterns for Kubernetes for dummies](https://www.redhat.com/en/engage/kubernetes-containers-storage-s-201911201051)

## Cloud Native Storage Solutions
- [itnext.io: State of Persistent Storage in K8s — A Benchmark](https://itnext.io/state-of-persistent-storage-in-k8s-a-benchmark-77a96bb1ac29)

### Rook
- [Rook](https://rook.io/)

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

### LightOS
- [LightOS](https://www.lightbitslabs.com/product/)
- [blocksandfiles.com: Lightbits Labs adds Kubernetes table stakes: CSI support](https://blocksandfiles.com/2020/06/23/lightbits-labs-adds-kubernetes-table-stakes-csi-support/)

### Longhorn
- [Longhorn](https://longhorn.io/)
- [thenewstack.io: Rancher Donates its ‘Longhorn’ Kubernetes Persistent Storage Software to CNCF](https://thenewstack.io/rancher-donates-its-longhorn-kubernetes-persistent-storage-software-to-cncf/). Gluster and Ceph were “designed to be run by some storage admin. In the Kubernetes world, a lot of these things tend to be deployed by DevOps teams, so (the storage layer) needs to be a lot more lightweight and a lot simpler.” — Rancher Labs CEO Sheng Liang.
- [Longhorn Simplifies Distributed Block Storage in Kubernetes](https://rancher.com/blog/2020/longhorn-container-storage)
- [containerjournal.com: Rancher Labs Adds Support for Longhorn Storage on Kubernetes Clusters](https://containerjournal.com/topics/container-management/rancher-labs-adds-support-for-longhorn-storage-on-kubernetes-clusters/)

### IBM Spectrum Storage Suite
- [IBM Spectrum](https://www.ibm.com/it-infrastructure/storage/spectrum) IBM Spectrum Storage software for data-driven architecture. A complete storage software family with AI-infused capability that changes the economics of storage on-prem and in the hybrid multicloud.
- [redbooks.ibm.com: IBM Storage for Red Hat OpenShift. IBM block storage & IBM Spectrum Scale](http://www.redbooks.ibm.com/abstracts/redp5565.html)
- [searchstorage.techtarget.com: IBM Spectrum](https://searchstorage.techtarget.com/definition/IBM-Spectrum)

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

---
<center>
[![gigaom radar report on storage](images/gigaom_radar_report_on_data_storage_for_k8s.png)](https://gigaom.com/report/gigaom-radar-for-data-storage-for-kubernetes/)
</center>
