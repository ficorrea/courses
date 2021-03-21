# Spark DataFrames Project Exercise 

# Let's get some quick practice with your new Spark DataFrame skills, you will be asked some basic questions about some stock market data, in this case Walmart Stock from the years 2012-2017. This exercise will just ask a bunch of questions, unlike the future machine learning exercises, which will be a little looser and be in the form of "Consulting Projects", but more on that later!
# For now, just answer the questions and complete the tasks below.

# Insere o caminho do spark
import findspark
findspark.init('/home/spark/spark-2.4.0-bin-hadoop2.7')
from pyspark.sql import SparkSession


# Use the walmart_stock.csv file to Answer and complete the  tasks below!

# Start a simple Spark Session
spark = SparkSession.builder.appName('exercise').getOrCreate()

# Load the Walmart Stock CSV File, have Spark infer the data types.
df = spark.read.csv('walmart_stock.csv', inferSchema=True, header=True)

# What are the column names?
df.columns

# What does the Schema look like?
df.printSchema()


# Print out the first 5 columns.
df.head(5)

# Use describe() to learn about the DataFrame.
df.describe().show()


# Bonus Question!
# There are too many decimal places for mean and stddev in the describe() dataframe. Format the numbers to just show up to two decimal places. Pay careful attention to the datatypes that .describe() returns, we didn't cover how to do this exact formatting, but we covered something very similar. [Check this link for a hint](http://spark.apache.org/docs/latest/api/python/pyspark.sql.html#pyspark.sql.Column.cast)
# 
# If you get stuck on this, don't worry, just view the solutions.

df.describe().printSchema()

from pyspark.sql.functions import format_number
result = df.describe()

result.select(result['summary'], 
              format_number(result['Open'].cast('float'), 2).alias('Open'),
              format_number(result['High'].cast('float'), 2).alias('High'),
              format_number(result['Low'].cast('float'), 2).alias('Low'),
              format_number(result['Close'].cast('float'), 2).alias('Close'),
              result['Volume'].cast('int')).alias('Volume').show()


# Create a new dataframe with a column called HV Ratio that is the ratio of the High Price versus volume of stock traded for a day.
new_df = df.withColumn('HV Ratio', df['High']/df['Volume'])
new_df.select('HV Ratio').show()

# What day had the Peak High in Price?
df.orderBy(df['High'].desc()).head(1)[0][0]

# What is the mean of the Close column?
from pyspark.sql.functions import mean
df.select(mean('Close')).show()

# What is the max and min of the Volume column?
from pyspark.sql.functions import max, min
df.select(max('Volume'), min('Volume')).show()

# How many days was the Close lower than 60 dollars?
df.filter('Close < 60').count()
df.filter(df['Close'] < 60).count()

from pyspark.sql.functions import count
res = df.filter(df['Close'] < 60)
res.select(count('Close')).show()

# What percentage of the time was the High greater than 80 dollars ?
# In other words, (Number of Days High>80)/(Total Days in the dataset)
df.filter(df['High'] > 80).count() / df.count() * 100

# What is the Pearson correlation between High and Volume?
# [Hint](http://spark.apache.org/docs/latest/api/python/pyspark.sql.html#pyspark.sql.DataFrameStatFunctions.corr)
from pyspark.sql.functions import corr
df.select(corr('High', 'Volume')).show()

# What is the max High per year?
from pyspark.sql.functions import year
temp_year = df.withColumn('Year', year(df['Date']))
dfg = temp_year.groupBy('Year').max()
dfg.select('Year', 'max(High)').show()

# What is the average Close for each Calendar Month?
# In other words, across all the years, what is the average Close price for Jan,Feb, Mar, etc... Your result will have a value for each of these months. 
from pyspark.sql.functions import month, avg
temp_month = df.withColumn('Month', month(df['Date']))
dfg = temp_month.groupBy('Month').avg()
dfg.select('Month', 'avg(Close)').orderBy('Month').show()
