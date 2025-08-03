from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime
from zoneinfo import ZoneInfo
from airflow.utils.task_group import TaskGroup

with DAG(
    "06_dag",
    description="Exemplo",
    schedule="0 3-19/4 * * *",
    start_date=datetime.now(ZoneInfo("America/Sao_Paulo")),
    catchup=False,
) as dag:
    task_gp_1 = TaskGroup("gp_1", dag=dag)
    task_gp_2 = TaskGroup("gp_2", dag=dag)

    task_1 = BashOperator(
        task_id="tsk1", bash_command="sleep 5", dag=dag, trigger_rule="all_done"
    )
    task_2 = BashOperator(
        task_id="tsk2",
        bash_command="sleep 5",
        dag=dag,
        trigger_rule="all_done",
        task_group=task_gp_1,
    )
    task_3 = BashOperator(
        task_id="tsk3", bash_command="sleep 5", dag=dag, trigger_rule="all_done"
    )
    task_4 = BashOperator(
        task_id="tsk4",
        bash_command="sleep 5",
        dag=dag,
        trigger_rule="all_done",
        task_group=task_gp_1,
    )
    task_5 = BashOperator(
        task_id="tsk5", bash_command="sleep 5", dag=dag, trigger_rule="all_done"
    )
    task_6 = BashOperator(
        task_id="tsk6", bash_command="sleep 5", dag=dag, trigger_rule="all_done"
    )
    task_7 = BashOperator(
        task_id="tsk7",
        bash_command="sleep 5",
        dag=dag,
        trigger_rule="all_done",
        task_group=task_gp_2,
    )
    task_8 = BashOperator(
        task_id="tsk8",
        bash_command="sleep 5",
        dag=dag,
        trigger_rule="all_done",
        task_group=task_gp_2,
    )
    task_9 = BashOperator(
        task_id="tsk9",
        bash_command="sleep 5",
        dag=dag,
        trigger_rule="all_done",
        task_group=task_gp_2,
    )

    task_1 >> task_2
    task_3 >> task_4
    task_gp_1 >> task_5
    task_5 >> task_6
    task_6 >> task_gp_2
