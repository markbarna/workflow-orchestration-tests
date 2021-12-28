from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator
from datetime import datetime

with DAG(
    dag_id='template',
    start_date=datetime(2021, 1, 1),
    params={"param1": "hello", "param2": "world"},
    schedule_interval=None
) as dag:
    task = DummyOperator(task_id="dummy_operator")
    
    task 