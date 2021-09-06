# Kubernetes Backup and Migrations
- [Introduction](#introduction)
- [Kubernetes Volume Snapshot](#kubernetes-volume-snapshot)
- [Backup with Trillio Cloud-Native Data Protection for Kubernetes, OpenStack and Virtualization](#backup-with-trillio-cloud-native-data-protection-for-kubernetes-openstack-and-virtualization)
- [Backup with Kasten K10](#backup-with-kasten-k10)
- [Backup with Velero](#backup-with-velero)
- [Konveyor Open Source Migration Tool for Kubernetes](#konveyor-open-source-migration-tool-for-kubernetes)

## Introduction
* [kube-backup: Kubernetes resource state sync to git](https://github.com/pieterlange/kube-backup)  
* [Stash](https://github.com/stashed/stash) If you are running production workloads in Kubernetes, you might want to take backup of your disks, databases etc. Stash is a cloud native data backup and recovery solution for Kubernetes workloads
* [thenewstack.io: Cloud Native Backups, Disaster Recovery and Migrations on Kubernetes](https://thenewstack.io/cloud-native-backups-disaster-recovery-and-migrations-on-kubernetes/)
* [rancher.com: The No. 1 Rule of Disaster Recovery](https://rancher.com/blog/2020/number-one-rule-disaster-recovery)
* [rancher.com: Disaster Recovery Preparedness for Your Kubernetes Clusters 🌟](https://rancher.com/blog/2020/disaster-recovery-preparedness-kubernetes-clusters)
* [k8s-snapshots: Automatic Volume Snapshots on Kubernetes](https://github.com/miracle2k/k8s-snapshots) is an operator that creates and expires snapshots according to annotations to your PersistentVolume or PersistentVolumeClaim resources.
* [infracloud.io: Protecting Kubernetes applications data using Kanister](https://www.infracloud.io/blogs/protecting-kubernetes-applications-with-kanister)
    * [kanister.io 🌟](https://kanister.io/) An extensible open-source framework for application-level data management on Kubernetes. KANISTER allows domain experts to capture application specific data management tasks in blueprints which can be easily shared and extended. The framework takes care of the tedious details around execution on Kubernetes and presents a homogeneous operational experience across applications at scale.
    * [blog.kasten.io: Move Fast and Test in Kubernetes without Breaking Things with kanister and CI/CD 🌟](https://blog.kasten.io/move-fast-and-test-in-kubernetes-without-breaking-things)
        * When using data mobility to improve your CI/CD pipeline, it’s important to consider the data at different layers in your application stack. In many instances, you must perform operations on multiple layers of your application at once, as well as interact with Kubernetes itself. Kasten by Veeam developed Kanister to address these data mobility challenges and enable organizations to test safely with real data.
        * Kanister, an open source project, provides a Kubernetes-native framework for application-level data management that supports complex data management workflows. Domain experts can capture application-specific data management tasks in blueprints, which can be easily shared and extended, eliminating many of the tedious details around execution on Kubernetes. 
        * Kanister is easy to integrate with your CI/CD pipeline, because it uses Kubernetes API extensions called custom resources. You can easily extend Kanister to work with custom applications as well as several common cloud native databases, simplifying and streamlining testing operations while reducing risk.
* [thenewstack.io: DevSecOps Teams Need Application-Consistent Backups for Kubernetes Workloads](https://thenewstack.io/devsecops-teams-need-application-consistent-backups-for-kubernetes-workloads/)
* [percona.com: Using Volume Snapshot/Clone in Kubernetes (GKE & Percona Kubernetes Operator for XtraDB Cluster)](https://www.percona.com/blog/2020/10/22/using-volume-snapshot-clone-in-kubernetes/)
* [kasten.io: Kubernetes Application Mobility](https://www.kasten.io/kubernetes/application-mobility/) Reliable and Powerful Migration of Complete Applications Across Kubernetes Clusters.
* [longhorn issue: Move replica to a different server](https://github.com/longhorn/longhorn/issues/292) 
* [aithority.com: Bacula Systems Announces World’s First Enterprise-Class Backup and Recovery Solution for Red Hat OpenShift](https://aithority.com/it-and-devops/cloud/bacula-systems-announces-worlds-first-enterprise-class-backup-and-recovery-solution-for-red-hat-openshift/)
* [cloudify.co: Migrating Pods With Containerized Applications Between Nodes In The Same Kubernetes Cluster Using Cloudify 🌟](https://cloudify.co/blog/migrating-pods-containerized-applications-nodes-kubernetes-cluster-using-cloudify/)
* [thenewstack.io: Red Hat Brings Backup, Snapshots to OpenShift Container Storage](https://thenewstack.io/red-hat-brings-backup-snapshots-to-openshift-container-storage/)
* [thenewstack.io: 5 Best Practices to Back up Kubernetes](https://thenewstack.io/5-best-practices-to-back-up-kubernetes)
* [Bacula Enterprise for OpenShift and Kubernetes 🌟](https://www.baculasystems.com/)
* [dani-izquierdo95.medium.com: Batch processing using Cron Jobs. MySQL automated backup on Openshift/K8s](https://dani-izquierdo95.medium.com/mysql-automated-backup-on-openshift-k8s-3690280d304f)
* [itnext.io: Backup and Restore of Kubernetes Stateful Application Data with CSI Volume Snapshots](https://itnext.io/backup-and-restore-of-kubernetes-stateful-application-data-with-csi-volume-snapshots-14ce9e6f3778)
* [youtube: Kubernetes.. ETCD Backup and Restore... Very Easy Steps... CKA Exam Tips..](https://www.youtube.com/watch?app=desktop&v=mODkt1OJDew&ab_channel=AlokKumar)
* [dev.to: Kubernetes Backup & Restore made easy! 🌟](https://dev.to/techworld_with_nana/kubernetes-backup-restore-made-easy-2nlg)
* [blog.kasten.io: 10 Key Takeaways from Kubernetes Backup & Recovery For Dummies](https://blog.kasten.io/10-key-takeaways-from-kubernetes-backup-recovery-for-dummies)
* [k8up.io](https://k8up.io/) Kubernetes Backup Operator distributed via a Helm chart, compatible with OpenShift and plain Kubernetes. 

## Kubernetes Volume Snapshot
* [kubernetes.io: Kubernetes 1.20: Kubernetes Volume Snapshot Moves to GA](https://kubernetes.io/blog/2020/12/10/kubernetes-1.20-volume-snapshot-moves-to-ga/)
* [itnext.io: Backup and Restore of Kubernetes Stateful Application Data with CSI Volume Snapshots](https://itnext.io/backup-and-restore-of-kubernetes-stateful-application-data-with-csi-volume-snapshots-14ce9e6f3778)
* [blocksandfiles.com: Red Hat OpenShift now does container storage backup 🌟](https://blocksandfiles.com/2021/01/27/red-hat-openshift-container-storage-backup/) Red Hat has teamed up with three container backup suppliers to integrate their services with the company’s OpenShift Kubernetes distribution. The Red Hat-certified backup products for OpenShift container storage are parent company IBM’s [Spectrum Protect Plus](https://blocksandfiles.com/2020/06/05/ibm-spectrum-protect-plus/); [TrilioVault](https://blocksandfiles.com/2020/12/10/trilio-funding/) for Kubernetes; and Veeam-owned Kasten’s [K10](https://blocksandfiles.com/2020/01/30/kasten-k10-kubernetes-container-protection/). 

## Backup with Trillio Cloud-Native Data Protection for Kubernetes, OpenStack and Virtualization
* [Trillio](http://trilio.io)
* [TrillioVault for Kubernetes](https://www.trilio.io/triliovault-for-kubernetes/)
* [redhat.com: OpenShift Backup and Cluster failover with Triliovault 🌟](https://www.redhat.com/es/about/videos/openshift-backup-and-cluster-failover-triliovault)

## Backup with Kasten K10
* [Kasten](https://www.kasten.io/)
* [redhat.com: OpenShift Backup and Recovery with Kasten K10](https://www.redhat.com/es/about/videos/openshift-backup-and-recovery-kasten-k10)

## Backup with Velero
* [akomljen.com: Kubernetes Backup and Restore with Velero 🌟](https://akomljen.com/kubernetes-backup-and-restore-with-velero/?utm_sq=ggwzo8xdd8)
* [wecloudpro.com: Kubernetes Disaster Recovery with Velero 🌟](https://www.wecloudpro.com/2020/08/22/kubernetes-disaster-recovery-with-velero.html)
* [medium: Backup,Restore & Migrate Kubernetes cluster with Velero](https://medium.com/@maheshd7878/restore-backup-migrate-kubernetes-cluster-with-velero-434fa151f1e8)
* [medium: Velero backup/restore for K8s Stateful Applications managed by Operators](https://medium.com/@Sandeepkallazhi/velero-backup-restore-for-k8s-stateful-applications-managed-by-operators-8fd9c732ffcc?utm_sq=gi0vbpxxa3)

## Konveyor Open Source Migration Tool for Kubernetes
- [github.com/konveyor 🌟](https://github.com/konveyor) - [konveyor.io](https://www.konveyor.io/) A community to build tools and document best practices to modernize workloads and bring them to Kubernetes.
- [containerjournal.com: Red Hat, IBM Launch Konveyor to Aggregate Kubernetes Tools](https://containerjournal.com/features/red-hat-ibm-launch-konveyor-to-aggregate-kubernetes-tools/)
- [engineering.konveyor.io: Konveyor Engineering Knowledgebase](https://engineering.konveyor.io/) Engineers working on Konveyor have started putting their own kbase articles here.
- [github.com/konveyor/crane: Crane 2.0 🌟](https://github.com/konveyor/crane) Crane 2, a tool for rehosting cloud workloads for Kubernetes.
    - [youtube: Crane 2 Preview: Introduction and Demo](https://www.youtube.com/watch?v=esIZS7PVrvs&ab_channel=Konveyor) Migrating workloads across clusters, from one k8s distro to another, will be the focus of open-source tool Crane 2.0. (A tool that's part of the Konveyor community.) 
