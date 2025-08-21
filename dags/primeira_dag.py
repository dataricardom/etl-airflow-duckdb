from datetime import datetime

from airflow.decorators import dag
from airflow.decorators import task

@dag(

    dag_id="primeira_dag_exemplo",
    description="exemplo etl",
    schedule="@daily",
    start_date=datetime(2023,8,21),
    catchup=False

)

def etl_exemplo():

    @task 
    def exemplo_print():
        print("Testando Dags")

    t1 = exemplo_print()

    t1

etl_exemplo()