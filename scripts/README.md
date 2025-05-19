---

# 🐳 Docker Log Collector Script

This script automates the process of collecting logs from Docker containers defined in `docker-compose.yml` or `docker-compose.yaml` files across multiple project directories.

---

## 📄 Features

* Scans a given directory for Docker Compose files (`.yml` or `.yaml`)
* Extracts container names from each Compose file
* Collects and aggregates logs for each container
* Outputs logs to a single file: `docker-service-logs.log`
* Simple and portable Bash script

---

## 📦 Requirements

* Bash shell (default on most Unix-based systems)
* Docker installed and running
* `docker-compose` containers using `container_name` in their definition

---

## 🚀 Usage

```bash
./docker-log-collector.sh /path/to/your/projects
```

### Arguments

* `/path/to/your/projects`: The root directory where your projects with `docker-compose` files are located (searches up to 2 levels deep)

---

## 📁 Output

The script generates a file named:

```
docker-service-logs.log
```

Located in the same directory as the script. This file contains:

* Project names
* Compose file paths
* Timestamps
* Container names
* Full logs for each container

---

## 📌 Notes

* Only containers defined with `container_name:` in the compose files will have their logs collected.
* If no Compose files or container names are found, the script exits with a helpful message.

---

## 🧪 Example

Suppose you have this structure:

```
~/projects/
├── service-a/docker-compose.yml
├── service-b/docker-compose.yaml
```

Run:

```bash
./docker-log-collector.sh ~/projects
```

After execution, view the logs:

```bash
cat docker-service-logs.log
```

---

## ✅ Sample Output

```
📦 Project: service-a
Compose File: /Users/you/projects/service-a/docker-compose.yml
Timestamp: 2025-05-19
-------------------
- my-service-a-container
...

🔹 Logs for my-service-a-container:
<docker logs output here>
```

---

## 🛠️ Customization

You can enhance the script to:

* Support services without `container_name`
* Include `docker-compose ps` to discover running containers
* Filter logs by date/time or keywords

---
