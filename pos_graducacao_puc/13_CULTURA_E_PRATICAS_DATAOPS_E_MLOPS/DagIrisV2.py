from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.dummy import DummyOperator
from airflow.operators.bash_operator import BashOperator
from airflow.utils.task_group import TaskGroup

pathScript = "/Users/jeanalves/airflow/dags/etl_scripts"
pathIris =  "/Users/jeanalves/airflow/dags/etl_scripts/featurestore/iris.txt"
pathEncoder = "/Users/jeanalves/airflow/dags/etl_scripts/featurestore/irisEncoder.txt"
pathDeploy = "/Users/jeanalves/airflow/dags/deployApi/apiIris"
pathModel = "/Users/jeanalves/airflow/dags/deployApi/apiIris/model.pkl"

default_args = {
   'owner': 'teste',
   'depends_on_past': False,
   'start_date': datetime(2019, 1, 1),
   'retries': 0,
   }

with DAG(
   'dag-pipeline-iris-aula-v2',
   schedule_interval=timedelta(minutes=10),
   catchup=False,
   default_args=default_args
   ) as dag:

    start = DummyOperator(task_id="start")

    with TaskGroup("etl", tooltip="etl") as etl:
        
        t1 = BashOperator(
            dag=dag,
            task_id='download_dataset',
            bash_command="""
            cd {0}/featurestore
            curl -o iris.txt  https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data
            """.format(pathScript)
        )

        [t1]

    with TaskGroup("preProcessing", tooltip="preProcessing") as preProcessing:
        t2 = BashOperator(
            dag=dag,
            task_id='encoder_dataset',
            bash_command="""
            cd {0}
            python etl_preprocessing.py {1} {2}
            """.format(pathScript, pathIris, pathEncoder)
        )
        [t2]

    with TaskGroup("model", tooltip="model") as model:
        t3 = BashOperator(
            dag=dag,
            task_id='modelo',
            bash_command="""
            cd {0}
            python ml_sklearn.py {1} {2} {3} {4} {5}
            """.format(pathScript,pathEncoder, "IrisClassificacao", "ModeloIris", 2, 0)
        )
        [t3]

    with TaskGroup("validate", tooltip="validate") as validate:
        t4 = BashOperator(
            dag=dag,
            task_id='validate',
            bash_command="""
            cd {0}
            python validateModel.py {1} {2}
            """.format(pathScript,"IrisClassificacao", pathModel)
        )
        [t4]

    end = DummyOperator(task_id='end')
    start >> etl >> preProcessing >> model >> validate >> end