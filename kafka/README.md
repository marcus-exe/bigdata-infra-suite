# Kafka + Zookeeper + Kafka UI Docker Setup

This repository provides a simple Docker Compose setup to run **Apache Kafka**, **Zookeeper**, and a **Kafka UI** locally on macOS.

---

## 📦 Services

- **Zookeeper**: Required for Kafka broker coordination.
- **Kafka**: Apache Kafka broker with advertised listener for host machine.
- **Kafka UI**: Web-based interface to monitor Kafka topics, messages, and brokers.

---

## 🚀 Getting Started

### 1. Prerequisites

- Docker & Docker Compose installed
- macOS (or a system where `host.docker.internal` resolves correctly)

### 2. Run the Stack

```bash
docker-compose up -d
````

This will spin up:

* Kafka on `localhost:9092`
* Kafka UI on `localhost:8080`

---

## ✅ Verifying the Setup

### Kafka Broker

Check if the Kafka broker is running:

```bash
docker-compose logs kafka
```

You should see lines like:

```
INFO [KafkaServer id=0] started (kafka.server.KafkaServer)
```

### Kafka UI

Open [http://localhost:8080](http://localhost:8080) in your browser to inspect topics, messages, and partitions.

---

## 🧪 Testing Kafka (Optional)

You can test Kafka with a CLI tool like [kcat](https://github.com/edenhill/kcat):

```bash
# Example: create a topic
kcat -b localhost:9092 -t test-topic -P
```

Or add a Kafka client in your preferred language (Java, Python, etc.).

---

## 🧼 Cleanup

To stop and remove all services:

```bash
docker-compose down
```

---

## 📝 Environment Configuration

Inside `docker-compose.yml`:

```yaml
KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://host.docker.internal:9092
```

This setting ensures that clients running on your host can connect to Kafka inside Docker.

---

## 📚 Resources

* [Apache Kafka](https://kafka.apache.org/)
* [Kafka UI](https://github.com/provectus/kafka-ui)
* [Zookeeper](https://zookeeper.apache.org/)

---


## 🪪 License


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
