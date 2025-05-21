---

# 🚀 How to Run Apache Kylin (v5.0.2-GA) with Docker

This guide walks you through pulling and running the standalone version of **Apache Kylin 5.0.2-GA** using Docker.

---

## 📦 Step 1: Pull the Docker Image

```bash
docker pull apachekylin/apache-kylin-standalone:5.0.2-GA
```

---

## 🛠 Step 2: Run the Docker Container

```bash
docker run -d \
    --name Kylin5-Machine \
    --hostname localhost \
    -e TZ=UTC \
    -m 10G \
    -p 7070:7070 \  # Kylin Web UI
    -p 8088:8088 \  # YARN ResourceManager
    -p 9870:9870 \  # HDFS NameNode
    -p 8032:8032 \  # YARN ResourceManager Scheduler
    -p 8042:8042 \  # NodeManager Web UI
    -p 2181:2181 \  # Zookeeper
    apachekylin/apache-kylin-standalone:5.0.2-GA
```

💡 **Tip:** Ensure you have at least **10GB of memory** allocated to Docker.

---

## 📄 Step 3: View Logs

To monitor the container logs in real-time:

```bash
docker logs --follow Kylin5-Machine
```

---

## 🌐 Web Interfaces

| Service Name | URL                                                                 |
| ------------ | ------------------------------------------------------------------- |
| **Kylin**    | [http://localhost:7070/kylin](http://localhost:7070/kylin%E2%81%A0) |
| **YARN**     | [http://localhost:8088](http://localhost:8088)                      |
| **HDFS**     | [http://localhost:9870](http://localhost:9870)                      |

---

## 🔐 Kylin Login Credentials

* **Username:** `ADMIN`
* **Password:** `KYLIN`

---

## 🧱 Ports Summary

| Port | Service              |
| ---- | -------------------- |
| 7070 | Apache Kylin Web UI  |
| 8088 | YARN ResourceManager |
| 9870 | HDFS NameNode UI     |
| 8032 | YARN Scheduler       |
| 8042 | NodeManager UI       |
| 2181 | Zookeeper            |

---

## 🌐 Web Interfaces

| Service Name | URL                                                                 |
| ------------ | ------------------------------------------------------------------- |
| **Kylin**    | [http://localhost:7070/kylin](http://localhost:7070/kylin%E2%81%A0) |
| **YARN**     | [http://localhost:8088](http://localhost:8088)                      |
| **HDFS**     | [http://localhost:9870](http://localhost:9870)                      |

---

## ⚠️ **Note:**
This Docker container is officially supported **only on Linux machines**.
For Windows or macOS, running the container may result in unexpected issues or incompatibility.

---

## 📚 Resources

* [Apache Kylin Documentation](https://kylin.apache.org/docs/)

---



