# -*- coding: utf-8 -*-

import findspark
findspark.init('/home/spark/spark-2.4.0-bin-hadoop2.7')

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('lr').getOrCreate()

# Aula Logistic Regression
data = spark.read.csv('titanic.csv',inferSchema=True,header=True)
data.printSchema()
data.columns

my_cols = data.select(['Survived', 'Pclass', 'Sex', 'Age', 'SibSp',
                       'Parch', 'Fare', 'Embarked'])

# Drop null colunas
my_final_data = my_cols.na.drop()

from pyspark.ml.feature import (VectorAssembler, OneHotEncoder,
                                StringIndexer)

# Working with Categorical Columns
# Categórica gender
gender_indexer = StringIndexer(inputCol='Sex',outputCol='SexIndex')
gender_encoder = OneHotEncoder(inputCol='SexIndex',outputCol='SexVec')

# Categórica embarked
embark_indexer = StringIndexer(inputCol='Embarked',outputCol='EmbarkIndex')
embark_encoder = OneHotEncoder(inputCol='EmbarkIndex',outputCol='EmbarkVec')

from pyspark.ml.classification import LogisticRegression

# Cria o classificador
log_reg_titanic = LogisticRegression(featuresCol='features',labelCol='Survived')

# Cria vetor de features
assembler = VectorAssembler(inputCols=['Pclass', 'SexVec', 'Age', 'SibSp',
                                       'Parch', 'Fare', 'EmbarkVec'],
                                        outputCol='features')

# Pipelines
from pyspark.ml import Pipeline
pipeline = Pipeline(stages=[gender_indexer,embark_indexer,
                           gender_encoder,embark_encoder,
                           assembler,log_reg_titanic])

# Split
train_titanic_data, test_titanic_data = my_final_data.randomSplit([0.7,.3])

# Treinamento usando Pipeline
fit_model = pipeline.fit(train_titanic_data)

# Teste
results = fit_model.transform(test_titanic_data)

from pyspark.ml.evaluation import BinaryClassificationEvaluator
my_eval = BinaryClassificationEvaluator(rawPredictionCol='prediction',
                                       labelCol='Survived')
results.select('Survived','prediction').show()
AUC = my_eval.evaluate(results)
AUC


# Exercício
data = spark.read.csv("customer_churn.csv", inferSchema=True, header=True)
data.printSchema()

data = data.select(['Age', 'Total_Purchase', 'Account_Manager', 'Years', 
                    'Num_Sites', 'Churn'])

# Elimina null
data = data.na.drop()
data.describe().show()

# Split
train, test = data.randomSplit([0.7, 0.3])

from pyspark.ml.classification import LogisticRegression
from pyspark.ml.feature import VectorAssembler
from pyspark.ml import Pipeline
from pyspark.ml.evaluation import BinaryClassificationEvaluator

va = VectorAssembler(inputCols=['Age', 'Total_Purchase', 'Account_Manager', 
                                'Years', 'Num_Sites'], outputCol='features')

# Depois da montagem do vetor pode-se
# usar somente as colunas necessárias, ex: 'features', 'label'
# Mas nesses casos qd não se usa o Pipeline

lr = LogisticRegression(labelCol='Churn')

# Criação do Pipeline
pipeline = Pipeline(stages=[va, lr])

# Criação do modelo
model = pipeline.fit(train)

# Teste do modelo
predictions = model.transform(test)
predictions.select(['Churn', 'prediction']).show()

# rawPredcionCol -> coluna de predições dada pelo modelo
# labelCol -> coluna com os valores supervisionados
ev = BinaryClassificationEvaluator(rawPredictionCol='prediction', labelCol='Churn')
# Avalia baseado na ROC Curve
ev.evaluate(predictions)

# Novos customers
new_data = spark.read.csv("new_customers.csv", inferSchema=True, header=True)
new_pred = model.transform(new_data)
new_pred.columns
new_pred.select(['Company', 'prediction']).show()





