from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

with DAG(
    dag_id='template',
    start_date=datetime(2021, 1, 1),
    params={"param1": "hello", "param2": "world"},
    schedule_interval=None
) as dag:
    task = PythonOperator(task_id="template", 
                      python_callable=lambda x: x,
                      templates_dict={}
                      )    
    task 