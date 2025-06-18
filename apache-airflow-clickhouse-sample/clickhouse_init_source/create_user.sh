#!/bin/bash
set -e # Exit immediately if a command exits with a non-zero status

echo "Waiting for ClickHouse server to be ready..."
# Loop to wait until clickhouse-client can successfully connect
# This prevents race conditions where the script runs before ClickHouse is fully up
for i in $(seq 1 10); do
    clickhouse-client --host localhost --query "SELECT 1" > /dev/null 2>&1 && break
    echo "ClickHouse server not yet ready, waiting (attempt $i/10)..."
    sleep 3
done
echo "ClickHouse server is ready."

echo "Creating user 'airflow' and granting permissions on db1 for clickhouse_source..."
clickhouse-client --host localhost --query "
  CREATE USER IF NOT EXISTS airflow IDENTIFIED BY 'airflow_password';
  GRANT ALL ON db1.* TO airflow;
"

echo "Creating table 'source_table' in db1..."
clickhouse-client --host localhost --database db1 --query "
  CREATE TABLE IF NOT EXISTS source_table (
      id UInt64,
      value Int32,
      timestamp DateTime
  ) ENGINE = MergeTree()
  ORDER BY id;
"

echo "User and table setup complete for clickhouse_source."