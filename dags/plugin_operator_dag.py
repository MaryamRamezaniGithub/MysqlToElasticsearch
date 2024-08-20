import datetime as dt

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

from elasticsearch_plugin.hooks.elasticsearch_hook import ElasticsearchHook
from elasticsearch_plugin.operators.elasticsearch_operator import MySqlToElasticsearchTransfer

default_args = {
        'owner': 'Mohammad Fozouni',
        'start_date': dt.datetime(2022, 1, 1),
        'concurrency': 1,
        'retries': 0
}

with DAG('plugin_operator_dag',
        default_args=default_args,
        schedule_interval='@once',
	catchup=False
	) as dag:
	
	opr_transfer = MySqlToElasticsearchTransfer(task_id='mysql_to_es', sql='SELECT * FROM sources', index='sources', mysql_conn_id="mysql_default")
	opr_end = BashOperator(task_id='opr_end', bash_command='echo "Done"')
	opr_transfer >> opr_end
