# dags/etl_dag.py
from airflow.decorators import dag, task
from datetime import datetime

@dag(
    schedule_interval="*/1 * * * *",
    start_date=datetime(2024, 1, 1),
    catchup=False,
    max_active_runs=1,
    tags=["etl"]
)
def etl_pipeline():

    @task
    def extract():
        from etl.extract import extract
        return extract(
            "/opt/airflow/data/daily_gym_attendance_workout_data.csv",
            "/opt/airflow/data/extracted.csv"
        )

    @task
    def transform(input_path):
        from etl.transform import transform
        return transform(
            input_path,
            "/opt/airflow/data/transformed.csv"
        )

    @task
    def load(input_path):
        from etl.load import load
        load(
            input_path,
            "/opt/airflow/data/output.csv"
        )


    raw = extract()
    processed = transform(raw)
    load(processed)

etl_pipeline()