# -*- coding: utf-8 -*-

import findspark
findspark.init('/home/spark/spark-2.4.0-bin-hadoop2.7')

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('cluster').getOrCreate()

# Aula Cluster
from pyspark.ml.clustering import KMeans

# Loads data.
dataset = spark.read.csv("seeds_dataset.csv",header=True,inferSchema=True)

from pyspark.ml.feature import VectorAssembler
vec_assembler = VectorAssembler(inputCols = dataset.columns, outputCol='features')
final_data = vec_assembler.transform(dataset)

from pyspark.ml.feature import StandardScaler
scaler = StandardScaler(inputCol="features", outputCol="scaledFeatures", 
                        withStd=True, withMean=False)
# Compute summary statistics by fitting the StandardScaler
scalerModel = scaler.fit(final_data)
# Normalize each feature to have unit standard deviation.
final_data = scalerModel.transform(final_data)


# Trains a k-means model.
kmeans = KMeans(featuresCol='scaledFeatures',k=3)
model = kmeans.fit(final_data)
# Evaluate clustering by computing Within Set Sum of Squared Errors.
wssse = model.computeCost(final_data)
print("Within Set Sum of Squared Errors = " + str(wssse))

# Shows the result.
centers = model.clusterCenters()
model.transform(final_data).select('prediction').show()
 
# Exercício
df = spark.read.csv('hack_data.csv', inferSchema=True, header=True)
df.columns

from pyspark.ml.feature import VectorAssembler
vector = VectorAssembler(inputCols=['Session_Connection_Time',
                                    'Bytes Transferred',
                                    'Kali_Trace_Used',
                                    'Servers_Corrupted',
                                    'Pages_Corrupted',
                                    'WPM_Typing_Speed'], outputCol='features')
data = vector.transform(df)

from pyspark.ml.feature import StandardScaler
scaler = StandardScaler(inputCol="features", outputCol="sc_Features", 
                        withStd=True, withMean=False)

sc = scaler.fit(data)
data = sc.transform(data)

from pyspark.ml.clustering import KMeans
km = KMeans(featuresCol='sc_Features', k=5)

model = km.fit(data)
model.clusterCenters()

data = model.transform(data)
data.select('prediction').show()

data.groupBy('prediction').count().show()
