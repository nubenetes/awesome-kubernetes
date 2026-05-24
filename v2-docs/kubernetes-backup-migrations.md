# Kubernetes Backup Migrations

!!! info "Architectural Context"
    Detailed reference for Kubernetes Backup Migrations in the context of The Container Stack.

## Standard Reference

  - [rancher.com: The No. 1 Rule of Disaster Recovery](https://www.suse.com/c/rancher_blog/the-no-1-rule-of-disaster-recovery)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [rancher.com: Disaster Recovery Preparedness for Your Kubernetes Clusters 🌟](https://www.suse.com/c/rancher_blog/disaster-recovery-preparedness-for-your-kubernetes-clusters)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [percona.com: Using Volume Snapshot/Clone in Kubernetes (GKE & Percona Kubernetes Operator for XtraDB Cluster)](https://www.percona.com/blog/using-volume-snapshot-clone-in-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.palark.com: Kubernetes snapshots: What are they and how to use them? 🌟](https://palark.com/blog/kubernetes-snaphots-usage)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blocksandfiles.com: Red Hat OpenShift now does container storage backup 🌟](https://www.blocksandfiles.com/container-storage/2021/01/27/red-hat-openshift-now-does-container-storage-backup/1611166)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Trillio](http://trilio.io)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Kasten](https://www.veeam.com/products/cloud/kubernetes-data-protection.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [akomljen.com: Kubernetes Backup and Restore with Velero 🌟](https://akomljen.com/kubernetes-backup-and-restore-with-velero/?utm_sq=ggwzo8xdd8)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium: Velero backup/restore for K8s Stateful Applications managed by Operators](https://medium.com/@Sandeepkallazhi/velero-backup-restore-for-k8s-stateful-applications-managed-by-operators-8fd9c732ffcc?utm_sq=gi0vbpxxa3)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [cloud.redhat.com: Velero Backup and Restore of an Application Using gp2 StorageClass on ROSA](https://www.redhat.com/en/blog/velero-backup-and-restore-of-an-application-using-gp2-storageclass-on-rosa)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [PX-Backup: docs](https://docs.portworx.com/portworx-backup-on-prem)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [containerjournal.com: Red Hat, IBM Launch Konveyor to Aggregate Kubernetes Tools](https://cloudnativenow.com/features/red-hat-ibm-launch-konveyor-to-aggregate-kubernetes-tools)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [github.com/konveyor/crane: Crane 2.0 🌟](https://github.com/migtools/crane) <span class='md-tag md-tag--info'>⭐ 54</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [kubebyexample.com: Migrating to Kubernetes with Open Source Tools (Konveyor, Tackle, KubeVirt, Forklift) 🌟](https://kubebyexample.com/community/blog/migrating-to-kubernetes-with-open-source-tools)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Automate SQL Server Backups with PowerShell](https://datacrazyworld.com/index.php/2025/03/16/automatiza-backups-de-sql-server-con-powershell)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [kube-backup: Kubernetes resource state sync to git](https://github.com/pieterlange/kube-backup) <span class='md-tag md-tag--info'>⭐ 493</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Stash](https://github.com/stashed/stash) <span class='md-tag md-tag--info'>⭐ 1414</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: Cloud Native Backups, Disaster Recovery and Migrations on' Kubernetes](https://thenewstack.io/cloud-native-backups-disaster-recovery-and-migrations-on-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [k8s-snapshots: Automatic Volume Snapshots on Kubernetes](https://github.com/miracle2k/k8s-snapshots) <span class='md-tag md-tag--info'>⭐ 350</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [infracloud.io: Protecting Kubernetes applications data using Kanister](https://www.infracloud.io/blogs/protecting-kubernetes-applications-with-kanister)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: DevSecOps Teams Need Application-Consistent Backups for' Kubernetes Workloads](https://thenewstack.io/devsecops-teams-need-application-consistent-backups-for-kubernetes-workloads)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [longhorn issue: Move replica to a different server](https://github.com/longhorn/longhorn/issues/292) <span class='md-tag md-tag--info'>⭐ 7734</span>  <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span>
  - [aithority.com: Bacula Systems Announces World’s First Enterprise-Class Backup' and Recovery Solution for Red Hat OpenShift](https://aithority.com/it-and-devops/cloud/bacula-systems-announces-worlds-first-enterprise-class-backup-and-recovery-solution-for-red-hat-openshift)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: Red Hat Brings Backup, Snapshots to OpenShift Container' Storage](https://thenewstack.io/red-hat-brings-backup-snapshots-to-openshift-container-storage)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Bacula Enterprise for OpenShift and Kubernetes 🌟](https://www.baculasystems.com)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [dani-izquierdo95.medium.com: Batch processing using Cron Jobs. MySQL automated' backup on Openshift/K8s](https://dani-izquierdo95.medium.com/mysql-automated-backup-on-openshift-k8s-3690280d304f)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [itnext.io: Backup and Restore of Kubernetes Stateful Application Data with' CSI Volume Snapshots](https://itnext.io/backup-and-restore-of-kubernetes-stateful-application-data-with-csi-volume-snapshots-14ce9e6f3778)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [dev.to: Kubernetes Backup & Restore made easy! 🌟](https://dev.to/techworld_with_nana/kubernetes-backup-restore-made-easy-2nlg)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.kasten.io: 10 Key Takeaways from Kubernetes Backup & Recovery For Dummies](https://blog.kasten.io/10-key-takeaways-from-kubernetes-backup-recovery-for-dummies)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [k8up.io](https://k8up.io)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/@amitabhprasad: Kubernetes volume backup for disaster recovery](https://medium.com/@amitabhprasad/kubernetes-volume-backup-for-disaster-recovery-56a5facee7fe)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: K8s Backup and Disaster Recovery Is More Important Than' Ever](https://thenewstack.io/k8s-backup-and-disaster-recovery-is-more-important-than-ever)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [youtube: Kubernetes.. ETCD Backup and Restore... Very Easy Steps... CKA' Exam Tips..](https://www.youtube.com/watch?app=desktop&v=mODkt1OJDew&ab_channel=AlokKumar)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [github.com/gardener/etcd-backup-restore](https://github.com/gardener/etcd-backup-restore) <span class='md-tag md-tag--info'>⭐ 328</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [kubernetes.io: Kubernetes 1.20: Kubernetes Volume Snapshot Moves to GA](https://kubernetes.io/blog/2020/12/10/kubernetes-1.20-volume-snapshot-moves-to-ga)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium: Leveraging operator pattern and VolumeSnapshots to backup databases' in Kubernetes](https://medium.com/blablacar/leveraging-operator-pattern-and-volumesnapshots-to-backup-databases-in-kubernetes-3a28aa425100)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [TrillioVault for Kubernetes](https://www.trilio.io/triliovault-for-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.kasten.io: Extending Kubernetes Application Backup and Mobility to' the Edge with Kasten K10 V4.5](https://blog.kasten.io/posts/extending-kubernetes-application-backup-and-mobility-to-the-edge-with-kasten-k10-v4.5)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: Kasten K10 V4.5: Grafana Observability, More Edge Support](https://thenewstack.io/kasten-k10-v4-5-grafana-observability-more-edge-support)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [faun.pub: Kasten K10 on KubeSphere to Ensure Kubernetes Backup and Restore](https://faun.pub/kasten-k10-on-kubesphere-to-ensure-kubernetes-backup-and-restore-1bc59a0b91aa)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [wecloudpro.com: Kubernetes Disaster Recovery with Velero 🌟](https://www.wecloudpro.com/2020/08/22/kubernetes-disaster-recovery-with-velero.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/@firat.yasar: Backup & Restore Kubernetes resources with VELERO](https://medium.com/@firat.yasar/backup-restore-kubernetes-resources-with-velero-b7fee14e7664)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [skildops.medium.com: Backup an entire Kubernetes cluster using Velero to' AWS S3](https://skildops.medium.com/backup-an-entire-kubernetes-cluster-using-velero-to-aws-s3-73d76d51d4bc)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.devgenius.io: Backup, Restore and Migrate Kubernetes Cluster resources' using Velero](https://blog.devgenius.io/backup-restore-and-migrate-kubernetes-cluster-resources-using-velero-a9b6997e4b54)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [PX-Backup](https://portworx.com/products/px-backup)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [github.com/konveyor 🌟](https://github.com/konveyor)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [engineering.konveyor.io: Konveyor Engineering Knowledgebase](https://engineering.konveyor.io)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [youtube: Crane 2 Preview: Introduction and Demo](https://www.youtube.com/watch?v=esIZS7PVrvs&ab_channel=Konveyor)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [slideshare.net: Migrating Java JBoss EAP Applications to Kubernetes With' S2I](https://www.slideshare.net/KonveyorIO/migrating-java-jboss-eap-applications-to-kubernetes-with-s2i)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>


---
💡 **Explore Related:** [Container Managers](./container-managers.md) | [Kubernetes Monitoring](./kubernetes-monitoring.md) | [Kubernetes Troubleshooting](./kubernetes-troubleshooting.md)

