"""Create DAG to show good practices."""

import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator



def send_failure_message():
    """Create dummy test suite to exemplify."""
    print("Dag run fail")


def task_1():
    """Create dummy test suite to exemplify."""
    print("Processing task 1")


def task_2():
    """Create dummy test suite to exemplify."""
    print("Processing task 2")


def task_3_1():
    """Create dummy test suite to exemplify."""
    print("Processing task 3.1")


def task_3_2():
    """Create dummy test suite to exemplify."""
    print("Processing task 3.2")


with DAG(
    "my_dag",
    schedule_interval="@daily",
    start_date=datetime.datetime(2022, 1, 1),
    catchup=False,
    tags=["ETL-conntector", "version_1.0.0"],
    description="ETL pipeline for connector",
    dagrun_timeout=datetime.timedelta(hours=1),
    on_failure_callback=send_failure_message,
) as dag:
    extract = PythonOperator(task_id="extract", python_callable=task_1)

    load = PythonOperator(task_id="load", python_callable=task_2)

    transform_1 = PythonOperator(task_id="transform_1", python_callable=task_3_1)

    transform_2 = PythonOperator(task_id="transform_1", python_callable=task_3_2)

    extract >> load >> [transform_1, transform_2]
