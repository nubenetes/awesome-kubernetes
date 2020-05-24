# Cloud Native Storage
- [Introduction](#introduction)
- [Solutions](#solutions)
- [OpenShift Container Storage Operator (OCS)](#openshift-container-storage-operator-ocs)
    - [OCS 3 (OpenShift 3)](#ocs-3-openshift-3)
    - [OCS 4 (OpenShift 4)](#ocs-4-openshift-4)

## Introduction
- [A Guide to Running Stateful Applications in Kubernetes](https://thenewstack.io/a-guide-to-running-stateful-applications-in-kubernetes/)
- [5 Cloud Native Storage Startups To Watch Out For In 2019](https://www.forbes.com/sites/janakirammsv/2019/06/28/5-cloud-native-storage-startups-to-watch-out-for-in-2019/)

## Solutions
- [OpenEBS](https://openebs.io/) extends the benefits of software-defined storage to cloud native through the container attached approach. 
    - [MayaData](https://mayadata.io/) Founder of OpenEBS
- [StorageOS](https://storageos.com/)
- [Rook](https://rook.io/)
- [Robin](https://robin.io/)
- [Reduxio](https://www.reduxio.com/)
- [Portworx](https://portworx.com/)
- [Longhorn](https://longhorn.io/)
    - [thenewstack.io: Rancher Donates its ‘Longhorn’ Kubernetes Persistent Storage Software to CNCF](https://thenewstack.io/rancher-donates-its-longhorn-kubernetes-persistent-storage-software-to-cncf/). Gluster and Ceph were “designed to be run by some storage admin. In the Kubernetes world, a lot of these things tend to be deployed by DevOps teams, so (the storage layer) needs to be a lot more lightweight and a lot simpler.” — Rancher Labs CEO Sheng Liang.

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
 