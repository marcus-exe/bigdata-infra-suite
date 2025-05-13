
# 🐘 Hadoop Multi-Node Cluster with Docker Compose

This repository sets up a simple **Hadoop 3.2.1** cluster using **Docker Compose**, with one NameNode and two DataNodes.

---

## 📦 Services

- **NameNode**
  - Web UI: [http://localhost:9870](http://localhost:9870)
  - Exposes HDFS on port `9000`
- **DataNode1**
- **DataNode2**

Each node uses the official [BDE2020 Hadoop Docker images](https://github.com/big-data-europe/docker-hadoop).

---

## 📁 Project Structure

```bash
.
├── docker-compose.yml  # Main Hadoop cluster configuration
└── README.md           # You're here
````

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/hadoop-docker-cluster.git
cd hadoop-docker-cluster
```

### 2. Start the Cluster

```bash
docker-compose up -d
```

> This will start:
>
> * `namenode` on port 9870 (web UI) and 9000 (HDFS)
> * `datanode1` and `datanode2`, connected on a shared Docker network

---

## ✅ Verifying the Cluster

### 🔍 NameNode Web UI

Open your browser and visit:
**[http://localhost:9870](http://localhost:9870)**

Check **Cluster > Datanodes** to ensure both `datanode1` and `datanode2` are listed and marked as **Live**.

### 📂 HDFS Report

You can check DataNode registration by entering the NameNode container:

```bash
docker exec -it namenode bash
hdfs dfsadmin -report
```

### 🧪 Upload a File to HDFS

Inside the NameNode:

```bash
hdfs dfs -mkdir /test
hdfs dfs -put /etc/hosts /test/hosts
hdfs dfs -ls /test
```

---

## 🧼 Clean Up

To stop and remove all containers, networks, and volumes:

```bash
docker-compose down -v
```

---

## 🛠️ Configuration Details

### Volumes

Data is persisted using Docker volumes:

* `hadoop_namenode`
* `hadoop_datanode1`
* `hadoop_datanode2`

### Network

A custom bridge network `hadoop-net` is used to enable hostname-based communication between containers.

---

## 🧰 Requirements

* Docker
* Docker Compose

---

## 📚 References

* [BDE2020 Docker Hadoop GitHub](https://github.com/big-data-europe/docker-hadoop)
* [Apache Hadoop Documentation](https://hadoop.apache.org/docs/current/)

---

## 📄 License

```
MIT License

Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy  
of this software and associated documentation files (the "Software"), to deal  
in the Software without restriction, including without limitation the rights  
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell  
copies of the Software, and to permit persons to whom the Software is  
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all  
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER  
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,  
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE  
SOFTWARE.
```