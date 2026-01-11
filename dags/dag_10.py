from __future__ import annotations

from datetime import datetime

from airflow import DAG
from airflow.providers.google.cloud.operators.bigquery import BigQueryInsertJobOperator


def create_dag() -> DAG:
    """Create a DAG that runs a BigQuery SQL job."""
    dag: DAG = DAG(
        dag_id="dag_10",
        start_date=datetime(2025, 1, 1),
        schedule=None,
        catchup=False,
        tags=["bigquery"],
    )

    with dag:
        BigQueryInsertJobOperator(
            task_id="run_sql",
            gcp_conn_id="google_cloud_default",
            location="US",
            configuration={
                "query": {
                    "query": """
                    CREATE OR REPLACE TABLE `pets-482115.teste_dbt.minha_tabela` AS
                    SELECT
                      CURRENT_TIMESTAMP() AS processed_at
                    """,
                    "useLegacySql": False,
                }
            },
        )

    return dag


dag: DAG = create_dag()
