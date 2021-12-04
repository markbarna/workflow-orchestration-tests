from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime

def hello_python(params, **context):
    print(f"Input params {params}")
    print(f"Context vars: {context}")
    return

with DAG(
    dag_id='test-setup',
    start_date=datetime(2021, 1, 1),
    params={"param1": "hello", "param2": "world"},
    schedule_interval=None
) as dag:
    
    hello_bash_op = BashOperator(
        task_id="hello_bash",
        bash_command="echo 'hello world, from bash'"
    )
    
    hello_python_op = PythonOperator(
        task_id="hello_python",
        python_callable=hello_python
    )
        
    hello_bash_op >> hello_python_op