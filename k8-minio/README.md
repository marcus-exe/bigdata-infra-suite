# Distributed MinIO on Kubernetes

This project deploys a **distributed MinIO** instance on Kubernetes using StatefulSets and headless services. MinIO is a high-performance, Kubernetes-native object storage compatible with the S3 API.

---

## Features

* **Distributed MinIO cluster** with multiple pods for high availability and scalability.
* Uses **StatefulSet** for stable network IDs and persistent storage.
* Exposes two main services:

  * `minio-headless`: Headless service for pod discovery.
  * `minio-service`: Cluster IP service for accessing MinIO.
* Supports **MinIO Console UI** on port `9001`.
* API compatible with Amazon S3 (port `9000`).
* Easily accessible via `kubectl port-forward` or service exposure.

---

## Prerequisites

* Kubernetes cluster (e.g., Minikube, kind, or cloud provider).
* `kubectl` CLI configured to connect to your cluster.
* `kubectl` version compatible with your cluster version.
* (Optional) Persistent volumes and storage class configured for stateful storage.

---

## Setup Instructions

### 1. Apply MinIO Kubernetes resources

```bash
kubectl apply -f minio-headless-service.yaml
kubectl apply -f minio-statefulset.yaml
kubectl apply -f minio-service.yaml
```

### 2. Verify pods are running

```bash
kubectl get pods -l app=minio
```

Wait until all MinIO pods are in `Running` status.

### 3. Access MinIO UI

Forward ports to access MinIO console and API locally:

```bash
kubectl port-forward svc/minio-service 9000:9000 9001:9001
```

Open your browser to:

* Console UI: [http://localhost:9001](http://localhost:9001)
* S3 API endpoint: [http://localhost:9000](http://localhost:9000)

Login with default credentials (unless customized):

```
Username: minioadmin
Password: minioadmin
```

---

## Usage

* Use the UI for bucket and object management.
* Use AWS SDKs or `mc` (MinIO client) for programmatic access.
* MinIO API is fully compatible with S3.

---

## Notes

* For production, consider configuring persistent volumes for data durability.
* Customize MinIO credentials via Kubernetes Secrets.
* You can expose MinIO externally using NodePort or Ingress (not included here).

---

## Troubleshooting

* If pods do not start, check logs:

  ```bash
  kubectl logs <pod-name>
  ```

* If you cannot connect, verify port-forwarding or service type.

* Validate YAML manifests for syntax errors.

---

## Resources

* [MinIO Official Docs](https://min.io/docs)
* [MinIO Kubernetes Operator](https://github.com/minio/operator)
* [Kubernetes StatefulSets](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/)

