# ClickHouse Data Pipeline with Data Generator

This repository contains a Docker Compose setup for a simple data pipeline involving two ClickHouse instances (source and destination) and a Python application that continuously generates and inserts data into the source ClickHouse.

## Table of Contents

  * [Overview](https://www.google.com/search?q=%23overview)
  * [Project Structure](https://www.google.com/search?q=%23project-structure)
  * [Getting Started](https://www.google.com/search?q=%23getting-started)
      * [Prerequisites](https://www.google.com/search?q=%23prerequisites)
      * [Setup](https://www.google.com/search?q=%23setup)
      * [Running the Services](https://www.google.com/search?q=%23running-the-services)
  * [Accessing ClickHouse](https://www.google.com/search?q=%23accessing-clickhouse)
      * [Source ClickHouse (`db1`)](https://www.google.com/search?q=%23source-clickhouse-db1)
      * [Destination ClickHouse (`db2`)](https://www.google.com/search?q=%23destination-clickhouse-db2)
  * [Next Steps (Airflow Integration)](https://www.google.com/search?q=%23next-steps-airflow-integration)

-----

## Overview

This Docker Compose setup orchestrates the following services:

  * **`clickhouse_source`**: A ClickHouse database instance (`db1`) that serves as the data source. It's initialized with an `airflow` user and a `source_table` for data ingestion.
  * **`clickhouse_destination`**: Another ClickHouse database instance (`db2`) intended to be the destination for data moved from the source.
  * **`data_generator`**: A Python application that continuously inserts random data into the `source_table` in `clickhouse_source`.

The ultimate goal for this setup is to integrate with Apache Airflow to periodically move data from `clickhouse_source` to `clickhouse_destination` and then clear the source, on an hourly basis.

-----

## Project Structure

```
.
├── data_generator/
│   ├── app.py          # Python script to generate data and insert into ClickHouse
│   └── Dockerfile      # Builds the Python data_generator image
├── clickhouse_init/
│   └── init.sql        # SQL script to initialize the source ClickHouse database (creates db1, user, and grants permissions)
└── docker-compose.yaml # Defines all the services and their configurations

```

-----

## Getting Started

Follow these steps to get your ClickHouse data pipeline up and running.

### Prerequisites

  * **Docker Desktop** (or Docker Engine and Docker Compose) installed on your machine.

### Running the Services

From the root directory of the project (where `docker-compose.yaml` is located), run the following command:

```bash
docker-compose up --build
```

  * `docker-compose up`: Starts all services defined in `docker-compose.yaml`.
  * `--build`: Rebuilds the `data_generator` Docker image. This is important if you make changes to `data_generator/Dockerfile` or `data_generator/app.py`.

The services will start in the foreground, and you'll see logs from each container. The `data_generator` will begin inserting data into `clickhouse_source`.

To run in detached mode (in the background):

```bash
docker-compose up --build -d
```

To stop all services:

```bash
docker-compose down
```

To stop and remove volumes (useful for a clean start):

```bash
docker-compose down -v
```

-----

## Accessing ClickHouse

You can connect to your ClickHouse instances using the `clickhouse-client` command-line tool, either directly within the container or from your host machine if ports are exposed.

### Source ClickHouse (`db1`)

  * **Container Name:** `clickhouse_source`
  * **Exposed Host Port:** `9001` (maps to container port `9000`)
  * **Database:** `db1`
  * **User:** `airflow`
  * **Password:** `airflow_password`

#### Method 1: Connect from within the `clickhouse_source` container (Recommended)

```bash
docker exec -it clickhouse_source clickhouse-client \
  --user airflow \
  --password airflow_password \
  --database db1
```

Once connected, you can run queries like:

```sql
SHOW TABLES;
SELECT count(*) FROM source_table;
SELECT * FROM source_table ORDER BY timestamp DESC LIMIT 5;
```

#### Method 2: Connect from your host machine

If you have `clickhouse-client` installed locally:

```bash
clickhouse-client \
  --host 127.0.0.1 \
  --port 9001 \
  --user airflow \
  --password airflow_password \
  --database db1
```

### Destination ClickHouse (`db2`)

  * **Container Name:** `clickhouse_destination`
  * **Exposed Host Port:** `9002` (maps to container port `9000`)
  * **Database:** `db2`
  * **User:** `airflow`
  * **Password:** `airflow_password`

You can connect similarly:

```bash
docker exec -it clickhouse_destination clickhouse-client \
  --user airflow \
  --password airflow_password \
  --database db2
```

Or from your host:

```bash
clickhouse-client \
  --host 127.0.0.1 \
  --port 9002 \
  --user airflow \
  --password airflow_password \
  --database db2
```

-----

## Next Steps (Airflow Integration)

This setup provides the foundational ClickHouse instances and a data source. The next phase involves integrating Apache Airflow to orchestrate the data movement. You would typically:

1.  Set up your Apache Airflow environment (likely in a separate `docker-compose.yaml`).
2.  Configure ClickHouse connections within Airflow.
3.  Create a DAG (Directed Acyclic Graph) in Airflow to:
      * Read data from `clickhouse_source.source_table`.
      * Insert that data into a table in `clickhouse_destination.db2`.
      * Delete the processed data from `clickhouse_source.source_table`.
      * Schedule this DAG to run hourly.
