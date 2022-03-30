# Pacotes 
from airflow import DGA 
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator

# Definindo argumentos basicos 
default_args = {
   'owner': 'Luiz Alexandre Moreira',
   'depends_on_past': False,
   'start_date': datetime.now(),
   'retries': 0,
   }

# Definindo a DAG 
with DAG('my-first-dag',schedule_interval=timedelta(days=1),catchup=False,default_args=default_args) as dag:
    t1 = BashOperator(
        task_id='first_etl',
        bash_command=""" cd $AIRFLOW_HOME/dags/etl_scripts/python3 ETL.py"""
        )

    print(“Executed code from my Python ETL!”)

