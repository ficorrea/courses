import mlflow
import mlflow.sklearn
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
import argparse
from sklearn.model_selection import train_test_split
import pandas as pd
from urllib.parse import urlparse

parser = argparse.ArgumentParser()
parser.add_argument("inputPath", help="arquivo input Iris", type=str)
parser.add_argument("experiment", help="experimento MLFLOW", type=str)
parser.add_argument("modelName", help="nome modelo MLfLow", type=str)
parser.add_argument("max_depth", help="parametro max_depth", default=2,type=int)
parser.add_argument("random_state", help="parametro random_state", default=0, type=int)
args = parser.parse_args()


iris = pd.read_csv(args.inputPath, sep=",")

X_train, X_test, y_train, y_test = train_test_split(iris.drop(['classEncoder','class'], axis=1), iris['classEncoder'], test_size=0.33)

try:
    idExperiment = mlflow.create_experiment(args.experiment)
except:
    idExperiment = mlflow.get_experiment_by_name(args.experiment).experiment_id

with mlflow.start_run(experiment_id=idExperiment):
    mlflow.log_param("max_depth", args.max_depth)
    mlflow.log_param("random_state", args.random_state)

    clf = RandomForestClassifier(max_depth=args.max_depth, random_state=args.random_state)
    clf.fit(X_train, y_train)
    predictCLF  = clf.predict(X_test)

    mlflow.log_metric("accuracy_score", accuracy_score(y_test,predictCLF))


    tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

    if tracking_url_type_store != "file":
        mlflow.sklearn.log_model(clf, "model", registered_model_name=args.modelName)
    else:
        mlflow.sklearn.log_model(clf, "model")