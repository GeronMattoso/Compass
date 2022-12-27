# %% [markdown]
# <head>
#     <h1>Semana 9 Exercicios 1 e 2<h1>
# <head>
#     <div>
#     <img align="left" alt="Geron-Mattoso" height="100" width="150" 
# src="https://spark.apache.org/images/spark-logo-rev.svg">
#     </div>

# %%
from pyspark.sql import SparkSession, SQLContext
import pyspark.sql.functions as fc
import pyspark.sql.types
from pyspark.sql.types import StructType, StructField, StringType

spark = SparkSession\
    .builder\
        .appName("Spark Exemplos")\
            .getOrCreate()

sc = SQLContext(spark.sparkContext)
sqlContext = SQLContext(sc)

# %% [markdown]
# ##### 1 - Crie um array de 250, Int e aplique o método reverse para inverter o conteúdo.

# %%
arraySpark = spark.range(250)

arraySpark.select(fc.reverse(arraySpark.id).alias('id')).show(15)

# %% [markdown]
# ##### 2 - Crie uma lista de 20 animais, ordene-os e itere para imprimi-las individualmente cada um deles. Depois salve num arquivo texto em formato CS

# %%
dados = [["cavalo"], ["vaca"],["rato"], ["girafa"], ["anta"], ["quero-quero"],["tico-tico"],["lambari"], ["jundia"], ["pato"], \
             ["gato"], ["galo"], ["iguana"], ["pinguin"], ["boi"], ["macaco"], ["zebra"], ["babuino"], ["carcaju"], ["foca"]]


schema = [("animais")]

array = spark.createDataFrame(data = dados, schema = schema)

array.show(5)

array.select('animais').orderBy('animais').show(5)

array.write.csv('./output', mode="overwrite")


