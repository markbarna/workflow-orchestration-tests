from airflow.operators.python import PythonOperator

task = PythonOperator(task_id="template", 
                    python_callable=lambda x: x,
                    templates_dict={}
                    )
