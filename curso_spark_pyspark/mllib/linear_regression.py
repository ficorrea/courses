# -*- coding: utf-8 -*-

import findspark
findspark.init('/home/spark/spark-2.4.0-bin-hadoop2.7')

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('lir').getOrCreate()

# Aula Regressão Linear

data = spark.read.csv("Ecommerce_Customers.csv",inferSchema=True,header=True)
data.printSchema()
data.show()
data.head()

# Import VectorAssembler and Vectors
from pyspark.ml.linalg import Vectors
from pyspark.ml.feature import VectorAssembler

data.columns

assembler = VectorAssembler(inputCols=["Avg Session Length", "Time on App", 
                                       "Time on Website",'Length of Membership'],
                                        outputCol="features")

output = assembler.transform(data)
output.select("features").show()
output.show()

final_data = output.select("features",'Yearly Amount Spent')

# Split dados
train_data,test_data = final_data.randomSplit([0.7,0.3])
train_data.describe().show()
test_data.describe().show()

# Create a Linear Regression Model object
from pyspark.ml.regression import LinearRegression
lr = LinearRegression(labelCol='Yearly Amount Spent')

# Fit the model to the data and call this model lrModel
lrModel = lr.fit(train_data,)

# Print the coefficients and intercept for linear regression
print("Coefficients: {} Intercept: {}".format(lrModel.coefficients,lrModel.intercept))

test_results = lrModel.evaluate(test_data)
test_results.residuals.show()

unlabeled_data = test_data.select('features')
predictions = lrModel.transform(unlabeled_data)
predictions.show()

print("RMSE: {}".format(test_results.rootMeanSquaredError))
print("MSE: {}".format(test_results.meanSquaredError))

#########################################################################################

# Exercício
df = spark.read.format('csv').option('header', 'true').load('cruise_ship_info.csv', inferSchema=True)

df.printSchema()
df.head(3)

from pyspark.ml.regression import LinearRegression
from pyspark.ml.feature import StringIndexer, VectorAssembler

ind = StringIndexer(inputCol='Cruise_line', outputCol='label_Cruise')
ind = ind.fit(df).transform(df)
ind.show()

data = ind.select('label_Cruise', 'Age', 'Tonnage', 'passengers', 
        'length', 'cabins', 'passenger_density', 'crew') 

data.show()

# Vetor
vector = VectorAssembler(inputCols=['label_Cruise', 'Age', 'Tonnage', 'passengers', 
        'length', 'cabins', 'passenger_density'], outputCol='features')

output = vector.transform(data)
output = output.select(['features', 'crew'])
output.show()

# Split
train, test = data.randomSplit([0.7, 0.3])

# Modelo
lr = LinearRegression(labelCol='crew')
model = lr.fit(train)

ev = model.evaluate(test)
ev.r2
ev.meanAbsoluteError
test_features = test.select('features')
test_features.show()
predictions = model.transform(test_features)
predictions.show()

teste = spark.createDataFrame([(1.0, 50.0, 344.33, 20.0, 4.6, 2.0, 35.9)], 
                              ['label_Cruise', 'Age', 'Tonnage', 'passengers', 
                               'length', 'cabins', 'passenger_density'])

teste = vector.transform(teste)
pred = model.transform(teste.select('features'))
pred.show()
