import time
from random import randint, choice
import os
from datetime import datetime # Add this import
from clickhouse_driver import Client
import uuid

time.sleep(15) # Add this line for testing

client = Client(
    host=os.getenv("CLICKHOUSE_HOST", "clickhouse"),
    port=int(os.getenv("CLICKHOUSE_PORT", 9000)),
    database=os.getenv("CLICKHOUSE_DB", "production_data"),
    user=os.getenv("CLICKHOUSE_USER", "clickhouse_server_user"),
    password=os.getenv("CLICKHOUSE_PASSWORD", "salcomp_password"),
)

# Ensure the table exists
# client.execute('''
#   CREATE TABLE IF NOT EXISTS workstation_records
#   (
#     record_id UUID DEFAULT generateUUIDv4(),
#     product_id UInt32,
#     production_line_id UInt16,
#     station_id UInt16,
#     production_plan_id UInt16,
#     defect_id Nullable(UInt16),
#     produced_quantity UInt16,
#     has_defect UInt8,
#     registered_at DateTime64(3, 'America/Manaus'),
#     data_sended Bool DEFAULT false
#   )
#   ENGINE = MergeTree
#   PARTITION BY toYYYYMM(toDateTime(registered_at))
#   ORDER BY (station_id, toDateTime(registered_at))
#   TTL toDateTime(registered_at) + INTERVAL 12 MONTH DELETE
#   SETTINGS index_granularity = 8192;
# ''')

# Create a list of possible production_plan_ids
production_plan_ids = [101, 102, 103, 104, 105]

while True:
    # Generate random data for each column
    product_id = randint(1000, 9999)
    production_line_id = randint(1, 10)
    station_id = randint(1, 50)
    production_plan_id = choice(production_plan_ids) # Randomly pick a plan ID
    
    has_defect = randint(0, 1) # 0 for no defect, 1 for defect
    defect_id = randint(1, 20) if has_defect == 1 else None # Assign defect_id if has_defect is 1, otherwise None
    
    produced_quantity = randint(1, 500)
    
    registered_at = datetime.now() # Current timestamp

    # Prepare data for insertion. Note that record_id and data_sended are handled by ClickHouse defaults.
    data = [(
        product_id,
        production_line_id,
        station_id,
        production_plan_id,
        defect_id,
        produced_quantity,
        has_defect,
        registered_at
    )]

    # Use the correct table name and column order for the INSERT statement
    client.execute('''
        INSERT INTO workstation_records 
        (product_id, production_line_id, station_id, production_plan_id, defect_id, produced_quantity, has_defect, registered_at) 
        VALUES
    ''', data)
    
    print(f"Inserted row: Product ID: {product_id}, Production Line: {production_line_id}, Station ID: {station_id}, Has Defect: {bool(has_defect)}, Registered At: {registered_at}")
    
    time.sleep(2)
