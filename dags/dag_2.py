from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from datetime import datetime

dag = DAG(
    "02_dag",
    description="Exemplo",
    schedule=None,
    start_date=datetime(2025, 7, 31),
    catchup=False,
)

task_1 = BashOperator(task_id="tsk1", bash_command="sleep 5", dag=dag)
task_2 = BashOperator(task_id="tsk2", bash_command="sleep 5", dag=dag)
task_3 = BashOperator(task_id="tsk3", bash_command="sleep 5", dag=dag)

task_1 >> [task_2, task_3]
