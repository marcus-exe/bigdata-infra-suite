# 📊 ClickHouse + Grafana + Data Generator

This project provides a ready-to-run environment using **ClickHouse** for high-performance OLAP storage, **Grafana** for visualization, and a **Python-based data generator** to simulate manufacturing station data.

## 🗂 Project Structure

```
.
├── clickhouse_init/
│   └── init.sh                       # Initializes the ClickHouse DB and tables
├── data_generator/
│   ├── app.py                        # Python script generating sample data
│   └── Dockerfile                    # Dockerfile for building the generator
├── grafana/
│   └── provisioning/
│       └── datasources/
│           └── clickhouse-datasource.yaml # Auto-configures ClickHouse in Grafana
├── docker-compose.yml               # Orchestration of services
└── README.md                        # You're here!
```

---

## 🧰 Services Overview

### 🚀 ClickHouse

* **Purpose**: Stores workstation production records with time-based partitioning and TTL cleanup.
* **Ports**:

  * `8123`: HTTP interface
  * `9000`: Native client interface
  * `9440`: TLS interface
* **Volume**: Persists data in `clickhouse_data`.

### 📈 Grafana

* **Purpose**: Visualize the data from ClickHouse.
* **Port**: `3000` (visit [http://localhost:3000](http://localhost:3000))
* **Auto-provisioned datasource**: Configured via `clickhouse-datasource.yaml`.

### ⚙️ Data Generator

* **Purpose**: Continuously inserts realistic random records into `workstation_records` table.
* **Config**: Reads connection info from `.env.development`.
* **Build**: Docker image is built from `data_generator/Dockerfile`.

---

## 💾 Database Table: `workstation_records`

| Column               | Type             | Description                        |
| -------------------- | ---------------- | ---------------------------------- |
| `record_id`          | UUID             | Auto-generated unique ID           |
| `product_id`         | UInt32           | Simulated product ID               |
| `production_line_id` | UInt16           | Line ID where the product was made |
| `station_id`         | UInt16           | Workstation ID                     |
| `production_plan_id` | UInt16           | Associated production plan         |
| `defect_id`          | Nullable(UInt16) | Defect code (nullable)             |
| `produced_quantity`  | UInt16           | Quantity produced                  |
| `has_defect`         | UInt8 (0/1)      | Indicates if there was a defect    |
| `registered_at`      | DateTime64(3)    | Record timestamp with ms precision |
| `data_sended`        | Bool             | Whether data was already sent      |

🧠 **TTL**: Records are automatically deleted **12 months** after `registered_at`.

---

## ▶️ Getting Started

### 1. Clone and Navigate

```bash
git clone https://github.com/marcus-exe/bigdata-infra-suite.git
cd bigdata-infra-suite/clickhouse+grafana
```

### 2. Create `.env.development` files

#### At root (ClickHouse and Grafana)

```env
CLICKHOUSE_DB=production_data
GF_SECURITY_ADMIN_USER=admin
GF_SECURITY_ADMIN_PASSWORD=admin
GF_INSTALL_PLUGINS=grafana-clickhouse-datasource
```

#### Inside `data_generator/`

```env
CLICKHOUSE_HOST=clickhouse
CLICKHOUSE_PORT=9000
CLICKHOUSE_DB=production_data
CLICKHOUSE_USER=clickhouse_server_user
CLICKHOUSE_PASSWORD=salcomp_password
```

### 3. Run Everything

```bash
docker-compose up --build
```

### 4. Access Grafana

* Go to: [http://localhost:3000](http://localhost:3000)
* Default login: `admin` / `admin`

---

## 🔄 Example Inserted Data

```
┌──────────────────────────────────────┬────────────┬────────────────────┬────────────┬────────────────────┬───────────┬───────────────────┬────────────┬─────────────────────────┬─────────────┐
│ record_id                            │ product_id │ production_line_id │ station_id │ production_plan_id │ defect_id │ produced_quantity │ has_defect │ registered_at           │ data_sended │
├──────────────────────────────────────┼────────────┼────────────────────┼────────────┼────────────────────┼───────────┼───────────────────┼────────────┼─────────────────────────┼─────────────┤
│ fbe93c75-d149-4e1b-bc51-20b67f8d0fe7 │       1379 │                  9 │          1 │                104 │     NULL  │                40 │          0 │ 2025-07-01 14:43:30.262 │ false       │
│ ...                                  │        ... │                ... │        ... │                ... │     ...   │              ...  │        ... │ ...                     │ ...         │
└──────────────────────────────────────┴────────────┴────────────────────┴────────────┴────────────────────┴───────────┴───────────────────┴────────────┴─────────────────────────┴─────────────┘
```

---

## 🧪 Development Notes

* The `data_generator` has a startup delay (`sleep(15)`) to wait for ClickHouse readiness.
* UUIDs and timestamps are auto-generated inside `app.py`.
* ClickHouse `init.sh` script ensures the table is created if not already present.

---

## 📦 Stopping & Cleaning Up

```bash
docker-compose down -v
```

---

## 📌 Todo Ideas

* [ ] Add dashboard provisioning JSON to Grafana
* [ ] Parametrize data generator frequency and ranges
* [ ] Add alerting in Grafana
