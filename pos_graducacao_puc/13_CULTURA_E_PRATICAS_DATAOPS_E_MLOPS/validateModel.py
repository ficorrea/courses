import argparse
from mlflow.tracking import MlflowClient
import mlflow
import os 

parser = argparse.ArgumentParser()
parser.add_argument("experiment", help="experimento MLFLOW", type=str)
parser.add_argument("pathModel", help="path model MLFLOW", type=str)
args = parser.parse_args()

try:
    idExperiment = mlflow.create_experiment(args.experiment)
except:
    idExperiment = mlflow.get_experiment_by_name(args.experiment).experiment_id


client = MlflowClient()
listModel = client.list_run_infos(idExperiment)

modelo = ""
metrica = 0
for model in listModel:
    print(model.artifact_uri, model.run_uuid)
    data = client.get_run(model.run_uuid).data
    if data.metrics['accuracy_score'] > metrica:
        metrica = data.metrics['accuracy_score']
        modelo = model.artifact_uri 


f = open("scriptDeploy.txt", "a")
f.write("accuracy_score: {0}".format(metrica))
f.write("""\nmlflow models serve -m {0} -p 1234""".format(modelo[7:] + "/model"))
f.write("""\ncurl -X POST -H "Content-Type:application/json; format=pandas-split" --data '{"columns":["sepal_length", "sepal_width", "petal_length", "petal_width"],"data":[[5.6, 2.7, 4.2, 1.3]]}' http://127.0.0.1:1234/invocations""")
f.close()


os.system("cp {0} {1}".format(modelo[7:] + "/model/model.pkl", args.pathModel))



