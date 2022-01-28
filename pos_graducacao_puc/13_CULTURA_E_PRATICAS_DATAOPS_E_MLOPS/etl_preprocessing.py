import pandas as pd
from sklearn import preprocessing
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("inputPath", help="arquivo input Iris", type=str)
parser.add_argument("outputPath", help="arquivo output Iris", type=str)
args = parser.parse_args()

columns = ['sepal_length','sepal_width','petal_length','petal_width','class']

dfIris = pd.read_csv(args.inputPath, names=columns)

le = preprocessing.LabelEncoder()

dfIris['classEncoder'] = le.fit_transform(dfIris['class'])

print(dfIris.classEncoder.unique())

dfIris.to_csv(args.outputPath, index=False)