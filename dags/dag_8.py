from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from datetime import datetime
from zoneinfo import ZoneInfo

with DAG(
    "07_dag",
    description="Exemplo",
    schedule="0 3/4 * * *",
    start_date=datetime.now(ZoneInfo("America/Sao_Paulo")),
    catchup=False,
    tags=["processo", "tag", "pipeline"],
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

    task_1 >> task_2 >> task_3
