# Spark DataFrames

import findspark
findspark.init('/home/spark/spark-2.4.0-bin-hadoop2.7')

# Aula 1

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('Basics').getOrCreate()

df = spark.read.json('people.json')

df.show()
df.printSchema()
df.describe()
df.columns
df.describe().show()
# Para remover trunc
df.show(truncate=False)

# Caso seja necessário alterar o schema de um dataset
from pyspark.sql.types import StructField, StringType, StructType, IntegerType

data_schema = [StructField('age', IntegerType(), True), StructField('name', StringType(), True)]
final_struct = StructType(fields=data_schema)
df = spark.read.json('people.json', schema=final_struct)
df.printSchema()

# Aula 2

df['age']
type(df['age'])

df.select('age')
type(df.select('age'))

df.select('age').show()

df.head(2)
type(df.head(2)[0])

df.select(['age', 'name']).show()


# Não é inplace
df.withColumn('double_age', df['age']*2).show()

# Não é inplace
df.withColumnRenamed('age', 'age_').show()

df.createOrReplaceTempView('people')
results = spark.sql('SELECT * FROM people')
results.show()

results = spark.sql('SELECT * FROM people where age=30')
results.show()


# Aula 3 - Operations

spark = SparkSession.builder.appName('Ops').getOrCreate()
df = spark.read.csv('appl_stock.csv', inferSchema=True, header=True)
df.printSchema()
df.show()

df.filter('Close < 500').show()
df.filter('Close < 500').select('Open').show()
df.filter(df['Close'] < 500).select(['Open', 'Close']).show()
df.filter((df['Close'] < 500) & (df['Open'] > 500)).select(['Open', 'Close']).show()
df.filter((df['Close'] < 500) & ~(df['Open'] > 500)).select(['Open', 'Close']).show()
df.filter(df['Low'] == 197.16).select('Volume').show()
result = df.filter(df['Low'] == 197.16).collect()
result
type(result)

result[0].asDict()
result[0].asDict()['High']


# Aula 4 - GroupBy and Aggregate

spark = SparkSession.builder.appName('Aggs').getOrCreate()
df = spark.read.csv('sales_info.csv', inferSchema=True, header=True)
df.show()
df.printSchema()

df.groupBy('Company')
df.groupBy('Company').mean()
df.groupBy('Company').mean().show()

df.groupBy('Company').sum().show()
df.groupBy('Company').max().show()
df.groupBy('Company').min().show()
df.groupBy('Company').count().show()

# Aggregate
df.agg({'Sales': 'max'}).show()

group_data = df.groupBy('Company')
group_data.agg({'Sales': 'mean'}).show()

from pyspark.sql.functions import countDistinct, avg, stddev

df.select(countDistinct('Sales')).show()
df.select(avg('Sales')).show()
df.select(stddev('Sales').alias('std')).show()

from pyspark.sql.functions import format_number

sales_std = df.select(stddev('Sales'))
sales_std.select(format_number('stddev_samp(Sales)', 2).alias('std')).show()

# OrderBy
df.orderBy('Sales').show()
df.orderBy(df['Sales'].desc()).show()

# Aula 5 

spark = SparkSession.builder.appName('Miss').getOrCreate()
df = spark.read.csv('ContainsNull.csv', inferSchema=True, header=True)
df.show()

df.na.drop().show()
df.na.drop(thresh=2).show()
df.na.drop(how='any').show()
df.na.drop(how='all').show()
df.na.drop(subset=['Sales']).show()

df.na.fill('No Name').show()
df.na.fill(0).show()
df.na.fill('No Value', subset=['Name']).show()

from pyspark.sql.functions import mean

mean_val = df.select(mean('Sales'))
mean_val.show()
mean_val = df.select(mean(df['Sales'])).collect()
mean_val

df.na.fill(df.select(mean(df['Sales'])).collect()[0][0], subset=['Sales']).show()

# Aula 6 - Dates and Timestamps

spark = SparkSession.builder.appName('Dates').getOrCreate()
df = spark.read.csv('appl_stock.csv', inferSchema=True, header=True)

from pyspark.sql.functions import (dayofmonth, dayofweek, dayofyear, hour, minute, second, month, year, 
                                   weekofyear, format_number, date_format)

df.select(dayofmonth(df['Date'])).show()
df.select(dayofweek(df['Date'])).show()
df.select(dayofyear(df['Date'])).show()
df.select(month(df['Date'])).show()
df.select(year(df['Date'])).show()
df.select(hour(df['Date'])).show()
df.select(minute(df['Date'])).show()
df.select(second(df['Date'])).show()

new_df = df.withColumn('Year', year(df['Date']))

new_df.groupBy('Year').mean().show()
new_df.groupBy('Year').mean().select(['Year', 'avg(Open)']).show()
new_df.groupBy('Year').mean().select(['Year', format_number('avg(Open)', 2).alias('avg(Open)')]).show()

