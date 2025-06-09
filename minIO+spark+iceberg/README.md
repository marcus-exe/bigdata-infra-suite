# 🧠 Data Lake Environment

This repository provides a pre-configured **Data Lake development environment** using Docker Compose. It includes components for object storage, distributed computing, SQL querying, and OLAP analysis.

## 🐳 Services

| Service        | Description                                      | URL/Port           |
|----------------|--------------------------------------------------|--------------------|
| **MinIO**      | S3-compatible object storage                     | `http://localhost:9000` (API)  
|                |                                                  | `http://localhost:9001` (Console)  
| **Spark Master** | Apache Spark master node                      | `http://localhost:8088`  
| **Spark Worker** | Apache Spark worker node                      | - (internal only)  
| **Trino**      | Distributed SQL query engine                     | `http://localhost:8080`  
| **Apache Kylin** | OLAP engine for big data analytics            | `http://localhost:7070`  

All services are connected via a shared Docker network named `datalake`.

---

## 🚀 Getting Started

### Prerequisites

- [Docker](https://www.docker.com/products/docker-desktop)
- [Docker Compose](https://docs.docker.com/compose/)

### Run the Stack

```bash
docker-compose up -d
````

To stop the stack:

```bash
docker-compose down
```

---

## 🔐 Default Credentials

### MinIO

* **Username:** `minioadmin`
* **Password:** `minioadmin`

---

## 🗂️ Volumes

* `minio_data`: Persists MinIO buckets and objects
* `kylin_data`: Persists Apache Kylin workspace

---

## 🧩 Configuration

### Trino

Custom Trino configuration should be placed inside the local `./trino/etc` directory. This folder is mounted into the container at `/etc/trino`.

---

## 🔗 Network

All services are connected via a custom Docker bridge network called `datalake`, which allows them to communicate internally by service name.

---

## 🧹 Cleanup

To remove all containers, networks, and volumes:

```bash
docker-compose down -v
```

---

## 📌 Notes

* Make sure ports like `8080`, `9000`, and `7077` are free before running the stack.
* Trino and Spark are designed to work together and can connect through internal service names (`spark-master:7077`).

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
