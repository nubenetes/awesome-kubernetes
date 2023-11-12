# Kubernetes Backup and Migrations

1. [Introduction](#introduction)
2. [ETCD Backup](#etcd-backup)
3. [Kubernetes Volume Snapshot](#kubernetes-volume-snapshot)
4. [Backup with Trillio Cloud-Native Data Protection for Kubernetes, OpenStack and Virtualization](#backup-with-trillio-cloud-native-data-protection-for-kubernetes-openstack-and-virtualization)
5. [Backup with Kasten K10](#backup-with-kasten-k10)
6. [Backup with Velero](#backup-with-velero)
7. [Backup with Portworx PX-Backup](#backup-with-portworx-px-backup)
8. [Backup for GKE](#backup-for-gke)
9. [Konveyor Open Source Migration Tool for Kubernetes](#konveyor-open-source-migration-tool-for-kubernetes)
10. [Other Tools](#other-tools)
11. [Books](#books)
12. [Slides](#slides)
13. [Videos](#videos)

## Introduction

- [kube-backup: Kubernetes resource state sync to git](https://github.com/pieterlange/kube-backup)
- [Stash](https://github.com/stashed/stash) If you are running production workloads in Kubernetes, you might want to take backup of your disks, databases etc. Stash is a cloud native data backup and recovery solution for Kubernetes workloads
- [thenewstack.io: Cloud Native Backups, Disaster Recovery and Migrations on Kubernetes](https://thenewstack.io/cloud-native-backups-disaster-recovery-and-migrations-on-kubernetes/)
- [rancher.com: The No. 1 Rule of Disaster Recovery](https://rancher.com/blog/2020/number-one-rule-disaster-recovery)
- [rancher.com: Disaster Recovery Preparedness for Your Kubernetes Clusters 🌟](https://rancher.com/blog/2020/disaster-recovery-preparedness-kubernetes-clusters)
- [k8s-snapshots: Automatic Volume Snapshots on Kubernetes](https://github.com/miracle2k/k8s-snapshots) is an operator that creates and expires snapshots according to annotations to your PersistentVolume or PersistentVolumeClaim resources.
- [infracloud.io: Protecting Kubernetes applications data using Kanister](https://www.infracloud.io/blogs/protecting-kubernetes-applications-with-kanister)
    - [kanister.io 🌟](https://kanister.io/) An extensible open-source framework for application-level data management on Kubernetes. KANISTER allows domain experts to capture application specific data management tasks in blueprints which can be easily shared and extended. The framework takes care of the tedious details around execution on Kubernetes and presents a homogeneous operational experience across applications at scale.
    - [blog.kasten.io: Move Fast and Test in Kubernetes without Breaking Things with kanister and CI/CD 🌟](https://blog.kasten.io/move-fast-and-test-in-kubernetes-without-breaking-things)
        - When using data mobility to improve your CI/CD pipeline, it’s important to consider the data at different layers in your application stack. In many instances, you must perform operations on multiple layers of your application at once, as well as interact with Kubernetes itself. Kasten by Veeam developed Kanister to address these data mobility challenges and enable organizations to test safely with real data.
        - Kanister, an open source project, provides a Kubernetes-native framework for application-level data management that supports complex data management workflows. Domain experts can capture application-specific data management tasks in blueprints, which can be easily shared and extended, eliminating many of the tedious details around execution on Kubernetes.
        - Kanister is easy to integrate with your CI/CD pipeline, because it uses Kubernetes API extensions called custom resources. You can easily extend Kanister to work with custom applications as well as several common cloud native databases, simplifying and streamlining testing operations while reducing risk.
- [thenewstack.io: DevSecOps Teams Need Application-Consistent Backups for Kubernetes Workloads](https://thenewstack.io/devsecops-teams-need-application-consistent-backups-for-kubernetes-workloads/)
- [percona.com: Using Volume Snapshot/Clone in Kubernetes (GKE & Percona Kubernetes Operator for XtraDB Cluster)](https://www.percona.com/blog/2020/10/22/using-volume-snapshot-clone-in-kubernetes/)
- [kasten.io: Kubernetes Application Mobility](https://www.kasten.io/kubernetes/application-mobility/) Reliable and Powerful Migration of Complete Applications Across Kubernetes Clusters.
- [longhorn issue: Move replica to a different server](https://github.com/longhorn/longhorn/issues/292)
- [aithority.com: Bacula Systems Announces World’s First Enterprise-Class Backup and Recovery Solution for Red Hat OpenShift](https://aithority.com/it-and-devops/cloud/bacula-systems-announces-worlds-first-enterprise-class-backup-and-recovery-solution-for-red-hat-openshift/)
- [cloudify.co: Migrating Pods With Containerized Applications Between Nodes In The Same Kubernetes Cluster Using Cloudify 🌟](https://cloudify.co/blog/migrating-pods-containerized-applications-nodes-kubernetes-cluster-using-cloudify/)
- [thenewstack.io: Red Hat Brings Backup, Snapshots to OpenShift Container Storage](https://thenewstack.io/red-hat-brings-backup-snapshots-to-openshift-container-storage/)
- [thenewstack.io: 5 Best Practices to Back up Kubernetes](https://thenewstack.io/5-best-practices-to-back-up-kubernetes)
- [Bacula Enterprise for OpenShift and Kubernetes 🌟](https://www.baculasystems.com/)
- [dani-izquierdo95.medium.com: Batch processing using Cron Jobs. MySQL automated backup on Openshift/K8s](https://dani-izquierdo95.medium.com/mysql-automated-backup-on-openshift-k8s-3690280d304f)
- [itnext.io: Backup and Restore of Kubernetes Stateful Application Data with CSI Volume Snapshots](https://itnext.io/backup-and-restore-of-kubernetes-stateful-application-data-with-csi-volume-snapshots-14ce9e6f3778)
- [dev.to: Kubernetes Backup & Restore made easy! 🌟](https://dev.to/techworld_with_nana/kubernetes-backup-restore-made-easy-2nlg)
- [blog.kasten.io: 10 Key Takeaways from Kubernetes Backup & Recovery For Dummies](https://blog.kasten.io/10-key-takeaways-from-kubernetes-backup-recovery-for-dummies)
- [k8up.io](https://k8up.io/) Kubernetes Backup Operator distributed via a Helm chart, compatible with OpenShift and plain Kubernetes.
- [medium.com/@amitabhprasad: Kubernetes volume backup for disaster recovery](https://medium.com/@amitabhprasad/kubernetes-volume-backup-for-disaster-recovery-56a5facee7fe)
- [thenewstack.io: K8s Backup and Disaster Recovery Is More Important Than Ever](https://thenewstack.io/k8s-backup-and-disaster-recovery-is-more-important-than-ever/) Here are some considerations of a successful Kubernetes data protection strategy.
- [martinheinz.dev: Backup-and-Restore of Containers with Kubernetes Checkpointing API](https://martinheinz.dev/blog/85) Kubernetes v1.25 introduced Container Checkpointing API as an alpha feature. This provides a way to backup-and-restore containers running in Pods, without ever stopping them. This feature is primarily aimed at forensic analysis, but general backup-and-restore is something any Kubernetes user can take advantage of. So, let's take a look at this brand-new feature and see how we can enable it in our clusters and leverage it for backup-and-restore or forensic analysis.
- [martinheinz.dev: Backup-and-Restore of Containers with Kubernetes Checkpointing API](https://martinheinz.dev/blog/85) Kubernetes v1.25 introduced Container Checkpointing API — a way to backup-and-restore containers running in Pods, without stopping them. In this article, you'll take a look at it and learn how to leverage it for backup-and-restore or forensic analysis.
- [blog.palark.com: Kubernetes snapshots: What are they and how to use them? 🌟](https://blog.palark.com/kubernetes-snaphots-usage/) With snapshots, you can make more efficient use of your storage solution by creating consistent backups and cloning volumes. In this article, you will find an introduction to snapshots in Kubernetes and an overview of typical use cases.

## ETCD Backup

- [youtube: Kubernetes.. ETCD Backup and Restore... Very Easy Steps... CKA Exam Tips..](https://www.youtube.com/watch?app=desktop&v=mODkt1OJDew&ab_channel=AlokKumar)
- [gsanjeewa1111.medium.com: How to backup and restore the ETCD in the Rancher cluster](https://gsanjeewa1111.medium.com/how-to-backup-and-restore-the-etcd-in-the-rancher-cluster-f4f075f528c2)
- [github.com/gardener/etcd-backup-restore](https://github.com/gardener/etcd-backup-restore) Collection of components to backup and restore the Etcd of a Kubernetes cluster. It also provides the ability to validate the data directory, so that we could know the data directory is in good shape to bootstrap etcd successfully.

## Kubernetes Volume Snapshot

- [kubernetes.io: Kubernetes 1.20: Kubernetes Volume Snapshot Moves to GA](https://kubernetes.io/blog/2020/12/10/kubernetes-1.20-volume-snapshot-moves-to-ga/)
- [itnext.io: Backup and Restore of Kubernetes Stateful Application Data with CSI Volume Snapshots](https://itnext.io/backup-and-restore-of-kubernetes-stateful-application-data-with-csi-volume-snapshots-14ce9e6f3778)
- [blocksandfiles.com: Red Hat OpenShift now does container storage backup 🌟](https://blocksandfiles.com/2021/01/27/red-hat-openshift-container-storage-backup/) Red Hat has teamed up with three container backup suppliers to integrate their services with the company’s OpenShift Kubernetes distribution. The Red Hat-certified backup products for OpenShift container storage are parent company IBM’s [Spectrum Protect Plus](https://blocksandfiles.com/2020/06/05/ibm-spectrum-protect-plus/); [TrilioVault](https://blocksandfiles.com/2020/12/10/trilio-funding/) for Kubernetes; and Veeam-owned Kasten’s [K10](https://blocksandfiles.com/2020/01/30/kasten-k10-kubernetes-container-protection/).
- [medium: Leveraging operator pattern and VolumeSnapshots to backup databases in Kubernetes](https://medium.com/blablacar/leveraging-operator-pattern-and-volumesnapshots-to-backup-databases-in-kubernetes-3a28aa425100)

## Backup with Trillio Cloud-Native Data Protection for Kubernetes, OpenStack and Virtualization

- [Trillio](http://trilio.io)
- [TrillioVault for Kubernetes](https://www.trilio.io/triliovault-for-kubernetes/)
- [redhat.com: OpenShift Backup and Cluster failover with Triliovault 🌟](https://www.redhat.com/es/about/videos/openshift-backup-and-cluster-failover-triliovault)

## Backup with Kasten K10

- [Kasten](https://www.kasten.io/)
- [redhat.com: OpenShift Backup and Recovery with Kasten K10](https://www.redhat.com/es/about/videos/openshift-backup-and-recovery-kasten-k10)
- [blog.kasten.io: Extending Kubernetes Application Backup and Mobility to the Edge with Kasten K10 V4.5](https://blog.kasten.io/posts/extending-kubernetes-application-backup-and-mobility-to-the-edge-with-kasten-k10-v4.5)
- [thenewstack.io: Kasten K10 V4.5: Grafana Observability, More Edge Support](https://thenewstack.io/kasten-k10-v4-5-grafana-observability-more-edge-support/)
- [faun.pub: Kasten K10 on KubeSphere to Ensure Kubernetes Backup and Restore](https://faun.pub/kasten-k10-on-kubesphere-to-ensure-kubernetes-backup-and-restore-1bc59a0b91aa)

## Backup with Velero

- [github.com/vmware-tanzu/velero](https://github.com/vmware-tanzu/velero) Backup and migrate Kubernetes applications and their persistent volumes
- [akomljen.com: Kubernetes Backup and Restore with Velero 🌟](https://akomljen.com/kubernetes-backup-and-restore-with-velero/?utm_sq=ggwzo8xdd8)
- [wecloudpro.com: Kubernetes Disaster Recovery with Velero 🌟](https://www.wecloudpro.com/2020/08/22/kubernetes-disaster-recovery-with-velero.html)
- [medium: Backup,Restore & Migrate Kubernetes cluster with Velero](https://medium.com/@maheshd7878/restore-backup-migrate-kubernetes-cluster-with-velero-434fa151f1e8)
- [medium: Velero backup/restore for K8s Stateful Applications managed by Operators](https://medium.com/@Sandeepkallazhi/velero-backup-restore-for-k8s-stateful-applications-managed-by-operators-8fd9c732ffcc?utm_sq=gi0vbpxxa3)
- [cloud.redhat.com: Velero Backup and Restore of an Application Using gp2 StorageClass on ROSA](https://cloud.redhat.com/blog/velero-backup-and-restore-of-an-application-using-gp2-storageclass-on-rosa)
- [medium.com/@firat.yasar: Backup & Restore Kubernetes resources with VELERO](https://medium.com/@firat.yasar/backup-restore-kubernetes-resources-with-velero-b7fee14e7664)
- [skildops.medium.com: Backup an entire Kubernetes cluster using Velero to AWS S3](https://skildops.medium.com/backup-an-entire-kubernetes-cluster-using-velero-to-aws-s3-73d76d51d4bc) Maintaining backup is always rewarding. Learn how to backup and restore an entire K8s cluster in this detailed article
- [blog.devgenius.io: Backup, Restore and Migrate Kubernetes Cluster resources using Velero](https://blog.devgenius.io/backup-restore-and-migrate-kubernetes-cluster-resources-using-velero-a9b6997e4b54) In this tutorial, you'll learn how to take a backup of resources running in a Kubernetes cluster and migrate them to another cluster using Velero

## Backup with Portworx PX-Backup

- [PX-Backup](https://portworx.com/products/px-backup/)
- [PX-Backup: docs](https://backup.docs.portworx.com/)
- With PX-Backup, backups of OpenShift applications can also be provided in a secure, self-service environment.

## Backup for GKE

- [cloud.google.com: Announcing Backup for GKE: the easiest way to protect GKE workloads](https://cloud.google.com/blog/products/storage-data-transfer/google-cloud-launches-backups-for-gke)

## Konveyor Open Source Migration Tool for Kubernetes

- [github.com/konveyor 🌟](https://github.com/konveyor) - [konveyor.io](https://www.konveyor.io/) A community to build tools and document best practices to modernize workloads and bring them to Kubernetes.
- [containerjournal.com: Red Hat, IBM Launch Konveyor to Aggregate Kubernetes Tools](https://containerjournal.com/features/red-hat-ibm-launch-konveyor-to-aggregate-kubernetes-tools/)
- [engineering.konveyor.io: Konveyor Engineering Knowledgebase](https://engineering.konveyor.io/) Engineers working on Konveyor have started putting their own kbase articles here.
- [github.com/konveyor/crane: Crane 2.0 🌟](https://github.com/konveyor/crane) Crane 2, a tool for rehosting cloud workloads for Kubernetes.
    - [youtube: Crane 2 Preview: Introduction and Demo](https://www.youtube.com/watch?v=esIZS7PVrvs&ab_channel=Konveyor) Migrating workloads across clusters, from one k8s distro to another, will be the focus of open-source tool Crane 2.0. (A tool that's part of the Konveyor community.)
- [kubebyexample.com: Migrating to Kubernetes with Open Source Tools (Konveyor, Tackle, KubeVirt, Forklift) 🌟](https://kubebyexample.com/en/community/blog/migrating-to-kubernetes-with-open-source-tools) **KubeByExample's newest learning path applies open source tools to help you rehost, replatform, and refractor your applications to Kubernetes.**
- [slideshare.net: Migrating Java JBoss EAP Applications to Kubernetes With S2I](https://www.slideshare.net/KonveyorIO/migrating-java-jboss-eap-applications-to-kubernetes-with-s2i)
    - Despite the incredible pace of adoption of container orchestration platforms, the vast majority of EAP workloads are still running on VMs or bare metal. In a lot of cases enterprise operation teams are mandated to modernize and move these workloads to the cloud, and containerization and migration to Kubernetes is the natural destination. When talking about this migration path, we're often asked questions like:
        - What's involved?
        - How easy is it to move these workloads?
        - How can you be sure of no code changes?
        - What tools are there to assist with this effort?
        - What are the benefits of moving workloads to Kubernetes?
    - In this meetup, Philip Hayes, Runtimes Practice Lead at Red Hat, will provide answers to these questions and also include a step-by-step guide to migrating an EAP 7 application to Kubernetes.
    - [youtube: Migrating JBoss EAP Applications to Kubernetes with Source-to-Image (S2I)](https://www.youtube.com/watch?v=9hDdg_Beui4&ab_channel=Konveyor)

## Other Tools

- [k8up.io](https://k8up.io) K8up is a Kubernetes Operator that helps you:
    - Backup all PVCs marked as ReadWriteMany or with a specific label
    - Perform individual, on-demand backups
    - Schedule backups to be executed on a regular basis
    - And more

## Books

- [kasten.io: Kubernetes Backup & Recovery For Dummies (Free e-book)](https://www.kasten.io/kubernetes/resources/books/kubernetes-backup-and-dr-for-dummies)

## Slides

<details>
  <summary>Click to expand!</summary>

<center>
<iframe src="//www.slideshare.net/slideshow/embed_code/key/1AC3zrxTauWgCT" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/KonveyorIO/migrating-java-jboss-eap-applications-to-kubernetes-with-s2i" title="Migrating Java JBoss EAP Applications to Kubernetes With S2I" target="_blank">Migrating Java JBoss EAP Applications to Kubernetes With S2I</a> </strong> from <strong><a href="//www.slideshare.net/KonveyorIO" target="_blank">Konveyor Community</a></strong> </div>
</center>
</details>

## Videos

<details>
  <summary>Click to expand!</summary>

<center>
<iframe width="560" height="315" src="https://www.youtube.com/embed/9hDdg_Beui4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<iframe width="560" height="315" src="https://www.youtube.com/embed/01qcYSck1c4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</center>
</details>

