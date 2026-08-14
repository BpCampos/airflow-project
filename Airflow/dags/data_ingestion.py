from airflow import DAG
from airflow.providers.databricks.operators.databricks import DatabricksRunNowOperator
from datetime import datetime


with DAG(
    dag_id="databricks_data_ingestion",
    start_date=datetime(2026, 8, 14),
    schedule=None,
    catchup=False,
) as dag:

    run_databricks_job = DatabricksRunNowOperator(
        task_id="run_databricks_job",
        databricks_conn_id="databricks_default",
        job_id=326218433604972
    )