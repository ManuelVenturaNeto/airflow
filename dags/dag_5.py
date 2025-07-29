from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

with DAG(
    "quinta_dag",
    description="Primeira Dag",
    schedule_interval=None,
    start_date=datetime(2023, 3, 5),
    catchup=False,
) as dag:
    task_1 = BashOperator(
        task_id="tsk1", bash_command="sleep 5", dag=dag, trigger_rule="all_done"
    )
    task_2 = BashOperator(
        task_id="tsk2", bash_command="sleep 5", dag=dag, trigger_rule="all_done"
    )
    task_3 = BashOperator(
        task_id="tsk3", bash_command="sleep 5", dag=dag, trigger_rule="all_done"
    )
    task_4 = BashOperator(
        task_id="tsk4", bash_command="sleep 5", dag=dag, trigger_rule="all_done"
    )
    task_5 = BashOperator(
        task_id="tsk5", bash_command="sleep 5", dag=dag, trigger_rule="all_done"
    )
    task_6 = BashOperator(
        task_id="tsk6", bash_command="sleep 5", dag=dag, trigger_rule="all_done"
    )
    task_7 = BashOperator(
        task_id="tsk7", bash_command="sleep 5", dag=dag, trigger_rule="all_done"
    )
    task_8 = BashOperator(
        task_id="tsk8", bash_command="sleep 5", dag=dag, trigger_rule="all_done"
    )
    task_9 = BashOperator(
        task_id="tsk9", bash_command="sleep 5", dag=dag, trigger_rule="all_done"
    )

    task_1 >> task_2
    task_3 >> task_4
    [task_2, task_4] >> task_5
    task_5 >> task_6
    task_6 >> [task_7, task_8, task_9]
