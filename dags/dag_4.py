from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    "04_dag",
    description="Exemplo",
    schedule=None,
    start_date=datetime(2025, 7, 31),
    catchup=False,
) as dag:
    task_1 = BashOperator(task_id="tsk1", bash_command="sleep 5", dag=dag)
    task_2 = BashOperator(task_id="tsk2", bash_command="sleep 5", dag=dag)
    task_3 = BashOperator(task_id="tsk3", bash_command="sleep 5", dag=dag)

    task_1.set_upstream(task_2)
    task_2.set_upstream(task_3)
