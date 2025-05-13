Here is a complete and polished `README.md` for your Hive and Hadoop Docker Compose setup:

---

````markdown
# 🐝 Apache Hive on Hadoop with Docker Compose

This project sets up an Apache Hive environment with a PostgreSQL Metastore, running on a Hadoop HDFS cluster using Docker Compose. It includes the following components:

- 🗃️ PostgreSQL as Hive Metastore backend
- 🧠 Hive Metastore service
- 🐝 HiveServer2 (for querying)
- 🐘 Hadoop NameNode & DataNode

---

## 📦 Services Overview

| Service               | Description                            | Ports             |
|-----------------------|----------------------------------------|-------------------|
| `hive-metastore-postgres` | PostgreSQL database for Hive metastore | `5432`            |
| `namenode`            | Hadoop NameNode (HDFS)                 | `9870`, `8020`    |
| `datanode`            | Hadoop DataNode                        | `9864`            |
| `hive-metastore`      | Hive Metastore service (Thrift)        | `9083`            |
| `hive-server`         | HiveServer2 (JDBC/Beeline interface)   | `10000`           |

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/hive-hadoop-docker.git
cd hive-hadoop-docker
````

### 2. Start the Cluster

```bash
docker-compose up -d
```

> This will spin up the entire Hive + Hadoop stack in the background.

---

## ✅ Verify the Setup

### 🔍 Access Hadoop Web UI

Visit: [http://localhost:9870](http://localhost:9870)
You should see the NameNode UI and verify that the DataNode is connected.

### 🐝 Check Hive Metastore

You can verify that Hive Metastore is running by ensuring port `9083` is open:

```bash
nc -zv localhost 9083
```

### 🧪 Connect to HiveServer2

Use Beeline or any Hive JDBC client to connect:

```bash
beeline -u jdbc:hive2://localhost:10000
```

Or inside the container:

```bash
docker exec -it hive-server bash
beeline -u jdbc:hive2://localhost:10000
```

---

## 📂 Data Volumes

| Volume Name     | Mount Path                 |
| --------------- | -------------------------- |
| `namenode-data` | `/hadoop/dfs/name`         |
| `datanode-data` | `/hadoop/dfs/data`         |
| `postgres-data` | `/var/lib/postgresql/data` |

These volumes ensure persistent storage for HDFS and PostgreSQL data across container restarts.

---

## 🧼 Tear Down

To stop the cluster and remove all volumes:

```bash
docker-compose down -v
```

---

## 🧰 Requirements

* Docker
* Docker Compose
* Beeline or a JDBC client (optional)

---

## 📚 References

* [Apache Hive](https://hive.apache.org/)
* [Apache Hadoop](https://hadoop.apache.org/)
* [BDE2020 Docker Hadoop](https://github.com/big-data-europe/docker-hadoop)
* [BDE2020 Docker Hive](https://github.com/big-data-europe/docker-hive)

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
