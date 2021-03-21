# -*- coding: utf-8 -*-

import findspark
findspark.init('/home/spark/spark-2.4.0-bin-hadoop2.7')

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('trees').getOrCreate()

# Aula Árvores de Decisão

# Load training data
data = spark.read.csv('College.csv',inferSchema=True,header=True)

# A few things we need to do before Spark can accept the data!
# It needs to be in the form of two columns
# ("label","features")

# Import VectorAssembler
from pyspark.ml.feature import VectorAssembler
assembler = VectorAssembler(
  inputCols=['Apps',
             'Accept',
             'Enroll',
             'Top10perc',
             'Top25perc',
             'F_Undergrad',
             'P_Undergrad',
             'Outstate',
             'Room_Board',
             'Books',
             'Personal',
             'PhD',
             'Terminal',
             'S_F_Ratio',
             'perc_alumni',
             'Expend',
             'Grad_Rate'],
              outputCol="features")
output = assembler.transform(data)

from pyspark.ml.feature import StringIndexer
indexer = StringIndexer(inputCol="Private", outputCol="PrivateIndex")
output_fixed = indexer.fit(output).transform(output)

final_data = output_fixed.select("features",'PrivateIndex')

# Split
train_data,test_data = final_data.randomSplit([0.7,0.3])

from pyspark.ml.classification import DecisionTreeClassifier,
                                        GBTClassifier,
                                        RandomForestClassifier
                                        
# Use mostly defaults to make this comparison "fair"
dtc = DecisionTreeClassifier(labelCol='PrivateIndex',featuresCol='features')
rfc = RandomForestClassifier(labelCol='PrivateIndex',featuresCol='features')
gbt = GBTClassifier(labelCol='PrivateIndex',featuresCol='features')

# Train the models (its three models, so it might take some time)
dtc_model = dtc.fit(train_data)
rfc_model = rfc.fit(train_data)
gbt_model = gbt.fit(train_data)

# Let's compare each of these models!
dtc_predictions = dtc_model.transform(test_data)
rfc_predictions = rfc_model.transform(test_data)
gbt_predictions = gbt_model.transform(test_data)

# **Evaluation Metrics:**
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

# Select (prediction, true label) and compute test error
acc_evaluator = MulticlassClassificationEvaluator(labelCol="PrivateIndex", 
                                                  predictionCol="prediction", 
                                                  metricName="accuracy")
dtc_acc = acc_evaluator.evaluate(dtc_predictions)
rfc_acc = acc_evaluator.evaluate(rfc_predictions)
gbt_acc = acc_evaluator.evaluate(gbt_predictions)

print("Here are the results!")
print('-'*80)
print('A single decision tree had an accuracy of: {0:2.2f}%'.format(dtc_acc*100))
print('-'*80)
print('A random forest ensemble had an accuracy of: {0:2.2f}%'.format(rfc_acc*100))
print('-'*80)
print('A ensemble using GBT had an accuracy of: {0:2.2f}%'.format(gbt_acc*100))


# Exercício
df = spark.read.csv('dog_food.csv', inferSchema=True, header=True)
df.printSchema()

from pyspark.ml.feature import VectorAssembler

vector = VectorAssembler(inputCols=['A', 'B', 'C', 'D'], outputCol='features')
data = vector.transform(df)

train, test = data.randomSplit([0.7, 0.3])

from pyspark.ml.classification import DecisionTreeClassifier, RandomForestClassifier
dtc = DecisionTreeClassifier(labelCol='Spoiled')
rfc = RandomForestClassifier(labelCol='Spoiled')

dtc_model = dtc.fit(train)
rfc_model = rfc.fit(train)

dtc_model.featureImportances
rfc_model.featureImportances

dtc_pred = dtc_model.transform(test)
rfc_pred = rfc_model.transform(test)

from pyspark.ml.evaluation import BinaryClassificationEvaluator
evlt = BinaryClassificationEvaluator(labelCol='Spoiled')
evlt.evaluate(dtc_pred)
evlt.evaluate(rfc_pred)

from pyspark.ml.evaluation import MulticlassClassificationEvaluator
acc = MulticlassClassificationEvaluator(metricName='accuracy', labelCol='Spoiled')
acc.evaluate(dtc_pred)
acc.evaluate(rfc_pred)
