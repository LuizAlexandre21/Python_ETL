# Pacotes 
from airflow import DGA 
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator

# Definindo argumentos basicos 
default_args = {
   'owner': 'Luiz Alexandre Moreira',
   'depends_on_past': False,
   'start_date': timedelta(days=1),
   'retries': 0,
   }

# Definindo a DAG 
with DAG('my-first-dag',schedule_interval=timedelta(days=1),catchup=False,default_args=default_args) as dag:
    t1 = BashOperator(
        task_id='first_etl',
        bash_command=""" cd $AIRFLOW_HOME/dags/etl_scripts/python3 ETL_2019.py"""
        )

    t2 = BashOperator(
        task_id='second_etl',
        bash_command=""" cd $AIRFLOW_HOME/dags/etl_scripts/python3 ETL_2020.py"""
        )

    t3 = BashOperator(
        task_id='third_etl',
        bash_command=""" cd $AIRFLOW_HOME/dags/etl_scripts/python3 ETL_2021.py"""
        )

    print(“Executed code from my Python ETL!”)

    # Pipeline 
    t1 >> t2 >> t3