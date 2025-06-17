import time
from random import randint
import os
from datetime import datetime # Add this import
from clickhouse_driver import Client

time.sleep(15) # Add this line for testing

client = Client(
    host=os.getenv("CLICKHOUSE_HOST", "clickhouse_source"),
    port=int(os.getenv("CLICKHOUSE_PORT", 9000)),
    database=os.getenv("CLICKHOUSE_DB", "db1"),
    user=os.getenv("CLICKHOUSE_USER", "airflow"),
    password=os.getenv("CLICKHOUSE_PASSWORD", "airflow_password"),
)

# Ensure the table exists
client.execute('''
    CREATE TABLE IF NOT EXISTS source_table (
        id UInt64,
        value Int32,
        timestamp DateTime
    ) ENGINE = MergeTree()
    ORDER BY id
''')

counter = 0

while True:
    counter += 1
    # Use datetime.now() directly
    current_timestamp = datetime.now()
    data = [(counter, randint(0, 100), current_timestamp)]
    client.execute('INSERT INTO source_table (id, value, timestamp) VALUES', data)
    print(f"Inserted row: {data}")
    time.sleep(2)
