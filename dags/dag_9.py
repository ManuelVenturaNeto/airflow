from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.providers.smtp.operators.smtp import EmailOperator
from datetime import datetime
from zoneinfo import ZoneInfo

with DAG(
    "09_dag",
    description="Exemplo",
    schedule=None,
    start_date=datetime.now(ZoneInfo("America/Sao_Paulo")),
    catchup=False,
    tags=["send_email_when_failed"],
) as dag:
    task_1 = BashOperator(task_id="tsk1", bash_command="sleep 5", dag=dag)

    task_2 = BashOperator(task_id="tsk2", bash_command="sleep 5", dag=dag)

    task_3 = BashOperator(task_id="tsk3", bash_command="sleep 5", dag=dag)

    task_4 = BashOperator(
        task_id="tsk4",
        # force fail
        bash_command="exit 1",
        dag=dag,
    )

    task_5 = BashOperator(
        task_id="tsk5", bash_command="sleep 5", dag=dag, trigger_rule="none_failed"
    )

    task_6 = BashOperator(
        task_id="tsk6", bash_command="sleep 5", dag=dag, trigger_rule="none_failed"
    )

    send_email = EmailOperator(
        task_id="send_email",
        to="manuueelneto@gmail.com",
        subject="Airflow Error",
        html_content="""
        <h3>Ocorreu um erro na Dag.</h3>
        <p>Dag: 07_dag </p>
        <p>Task: tsk4 falhou</p>
        """,
        trigger_rule="one_failed",
    )

    [task_1, task_2] >> task_3
    task_3 >> task_4
    task_4 >> [task_5, task_6, send_email]
