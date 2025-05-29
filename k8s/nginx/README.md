
# 🚀 NGINX Deployment with Kubernetes

This tutorial walks you through deploying an NGINX web server using Kubernetes via a simple YAML file.

## 📄 nginx-deployment.yaml

---

## 🔍 What This Does

* **Creates a Deployment** named `nginx`
* **Spins up 2 Pods** running the `nginx:latest` Docker image
* **Exposes port 80** in each Pod for web traffic

---

## ⚙️ How to Use This Deployment

### 1. Apply the Deployment

```bash
kubectl apply -f nginx-deployment.yaml
```

This will create the deployment and start two NGINX Pods.

---

### 2. Check Pods

```bash
kubectl get pods
```

Expected output:

```
NAME                     READY   STATUS    RESTARTS   AGE
nginx-7cdbd8cdc9-abcde   1/1     Running   0          30s
nginx-7cdbd8cdc9-fghij   1/1     Running   0          30s
```

---

### 3. View the Deployment

```bash
kubectl get deployments
```

or for detailed info:

```bash
kubectl describe deployment nginx
```

---

### 4. Access the Application

Expose the Deployment as a service:

```bash
kubectl expose deployment nginx --type=NodePort --port=80
```

If using **Minikube**, get the external URL:

```bash
minikube service nginx --url
```

Then open that URL in your browser — you should see the default NGINX welcome page.

---

### 5. Scale the Deployment

To change the number of replicas (e.g., from 2 to 4):

```bash
kubectl scale deployment nginx --replicas=4
```

Check the pods again:

```bash
kubectl get pods
```

---

### 6. Update the NGINX Version

Perform a rolling update to a specific version:

```bash
kubectl set image deployment/nginx nginx=nginx:1.21
```

Roll it back if needed:

```bash
kubectl rollout undo deployment nginx
```

---

### 7. View Pod Logs

```bash
kubectl logs <pod-name>
```

Replace `<pod-name>` with the actual name from `kubectl get pods`.

---

### 8. Exec into a Pod (Optional)

```bash
kubectl exec -it <pod-name> -- /bin/bash
```

Now you can explore the container's file system and running processes.

---

### 9. Clean Up

Delete the deployment and service when you're done:

```bash
kubectl delete deployment nginx
kubectl delete service nginx
```

---

## ✅ Summary

This deployment is a great starting point for learning how Kubernetes works:

* Understand how deployments manage pods and replicas
* Use labels and selectors
* Scale apps easily
* Perform updates and rollbacks
* Expose services and access your app

---

## 📦 Next Steps

* Add a `Service` with LoadBalancer or Ingress
* Attach a `ConfigMap` or `Volume`
* Deploy a custom HTML site with NGINX
* Monitor resources with `kubectl top` or Prometheus

---
