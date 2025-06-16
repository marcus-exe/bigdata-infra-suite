from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

def hello_world():
    print("✅ Hello from Airflow! The DAG is running successfully.")

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

# Define the DAG
with DAG(
    dag_id='example_hello_world_dag',
    default_args=default_args,
    description='A simple Hello World Airflow DAG',
    schedule_interval='@daily',  # Run daily
    start_date=datetime(2025, 6, 16),
    catchup=False,
    tags=['example'],
) as dag:

    hello_task = PythonOperator(
        task_id='say_hello',
        python_callable=hello_world,
    )

    hello_task
