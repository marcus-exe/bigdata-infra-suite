from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from clickhouse_driver import Client

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def extract_data(**context):
    source_client = Client(
        host='clickhouse_source',   # Docker service name for source ClickHouse
        port=9000,
        user='airflow',
        password='airflow_password',
        database='db1'
    )
    result = source_client.execute("SELECT id, value, timestamp FROM source_table WHERE timestamp < now()")
    context['ti'].xcom_push(key='extracted_data', value=result)

def insert_data(**context):
    data = context['ti'].xcom_pull(key='extracted_data', task_ids='extract_from_db1')
    if not data:
        return
    dest_client = Client(
        host='clickhouse_destination',   # Docker service name for destination ClickHouse
        port=9000,
        user='airflow',
        password='airflow_password',
        database='db2'
    )
    dest_client.execute("INSERT INTO destination_table (id, value, timestamp) VALUES", data)

def delete_data(**context):
    data = context['ti'].xcom_pull(key='extracted_data', task_ids='extract_from_db1')
    if not data:
        return
    ids = [str(row[0]) for row in data]  # Assuming first column is id
    ids_csv = ",".join(ids)
    source_client = Client(
        host='clickhouse_source',
        port=9000,
        user='default',
        password='',
        database='db1'
    )
    delete_query = f"ALTER TABLE source_table DELETE WHERE id IN ({ids_csv})"
    source_client.execute(delete_query)

with DAG(
    'clickhouse_transfer_dag',
    default_args=default_args,
    description='Transfer data from ClickHouse source to destination every hour and delete from source if successful',
    schedule_interval='@hourly',
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['clickhouse'],
) as dag:

    t1 = PythonOperator(
        task_id='extract_from_db1',
        python_callable=extract_data,
    )

    t2 = PythonOperator(
        task_id='insert_into_db2',
        python_callable=insert_data,
    )

    t3 = PythonOperator(
        task_id='delete_from_db1',
        python_callable=delete_data,
    )

    t1 >> t2 >> t3
