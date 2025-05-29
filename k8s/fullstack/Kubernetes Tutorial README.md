# Kubernetes Frontend + Backend Example

This project demonstrates a simple Kubernetes deployment of a **frontend** and **backend** connected using services and proxying requests via Nginx.

---

## 📁 Files

### Backend
- `backend-configmap.yaml`: JSON response served by the backend.
- `backend-deployment.yaml`: Python HTTP server serving JSON on port 80.
- `backend-service.yaml`: ClusterIP service exposing the backend pod.

### Frontend
- `frontend-html-configmap.yaml`: HTML + JavaScript to fetch data from backend.
- `frontend-nginx-configmap.yaml`: Nginx config for proxying `/api` to backend.
- `frontend-deployment.yaml`: Nginx container serving the static frontend and proxying.
- `frontend-service.yaml`: NodePort service exposing frontend to browser.

---

## 🚀 Deploy Steps

Make sure you have a Kubernetes cluster running. You can use `minikube` for local testing.

### 1. Start Minikube (if using)

```bash
minikube start
```

### 2. Deploy Backend

```bash
kubectl apply -f backend-configmap.yaml
kubectl apply -f backend-deployment.yaml
kubectl apply -f backend-service.yaml
```

### 3. Deploy Frontend

```bash
kubectl apply -f frontend-html-configmap.yaml
kubectl apply -f frontend-nginx-configmap.yaml
kubectl apply -f frontend-deployment.yaml
kubectl apply -f frontend-service.yaml
```

---

## 🌐 Access the App

Get the Minikube IP and port:

```bash
minikube service frontend-service
```

Open the provided URL in your browser. You should see:

```
Hello from Frontend!
{ "message": "Hello from Backend!" }
```

---

## 🛠 Notes

- Frontend talks to backend using `/api`, which is proxied to `http://backend-service`.
- Services use DNS resolution within the cluster (e.g., `backend-service.default.svc.cluster.local`).
- Use `kubectl get pods` and `kubectl logs` for debugging.

---

Happy Kubernetes-ing! 🎉
