"""Create DAG to show good practices."""

import datetime
import time

from airflow import DAG
from airflow.operators.python import PythonOperator


def send_failure_message():
    print("Dag run fail")


def download_invoices():
    print("Dowloading invoice!!!")
    time.sleep(5)
    print("Downloaded!")


def transform_invoices():
    print("Transform invoice")


def save_to_database():
    print("Save invoices to database")


def generate_report():
    print("Generate report")


def notify_via_email():
    print("Notify via email")


with DAG(
        "my_dag",
        schedule_interval="@daily",
        start_date=datetime.datetime(2022, 1, 1),
        catchup=False,
        tags=["ETL-pipeline", "version_1.0.0"],
        description="ETL pipeline",
        dagrun_timeout=datetime.timedelta(hours=1),
        on_failure_callback=send_failure_message,
) as dag:
    download_invoices_op = PythonOperator(task_id="download_invoices", python_callable=download_invoices)

    transform_invoices_op = PythonOperator(task_id="transform_invoices", python_callable=transform_invoices)

    save_to_database_op = PythonOperator(task_id="save_to_database", python_callable=save_to_database)

    generate_report_op = PythonOperator(task_id="generate_report", python_callable=generate_report)

    notify_via_email_op = PythonOperator(task_id="notify_via_email", python_callable=notify_via_email)

    ##TODO: Implement the workflow

