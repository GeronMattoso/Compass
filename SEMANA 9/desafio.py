# %% [markdown]
# <head>
#     <h1>Semana 9 Desafio_XPTO<h1>
# <head>
#     <div>
#     <img align="left" alt="Geron-Python" height="100" width="150" 
# src="https://spark.apache.org/images/spark-logo-rev.svg">
#     </div>

# %% [markdown]
# #### 5. Desafio XPTO:
# Carregar os dados da RAW Zone para a REF Zone, unificando os dados num Bucket S3 persistino no formato parquet.
# Particionar os dados por Ano/Mês/Dia conforme a criação do Twitter. Incluir 2 colunas novas:
# 
# Sentimento: indicando Positivo quando encontrar algum símbolo como :D ou :) ou :] etc; Indicando Negativo quando encontrar algum
# símbolo como :( ou :[ ou :{ etc. Indicando Neutro, quando o tweet não tiver nenhum dos símbolos analisados. Se um tweet tiver vários
# símbolos apenas o primeiro encontrado deve ser utilizado
# 
# Símbolo: Nesta coluna você deve adicionar o símbolo encontrado no tweet. Se um tweet tiver vários símbolos apenas o primeiro
# encontrado deve ser utilizado
# 
# Vamos fazer o código Spark criado executar via EMR e Glue com a finalidade de comparação das soluções.

# %%
from pyspark import SparkContext, SQLContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
import os

caminho = os.getcwd()

spark = SparkSession.builder.appName("Desafio_XPTO").getOrCreate()

# %%
df = spark.read.option("delimiter", ";").csv(caminho + '/output_twitter.csv', header=True, inferSchema=True)

#df.show(5, truncate=False)


# %%
emocaopos = [":D",":)",":]",":-)",":P",":p",":v",": )"]
emocaoneg = [":(",":[",":{"]

todas_emocoes = [':D', ':)', ':]', ':-)', ':P', ':p', ':v', ': )',':(', ':[', ':{']

# %%
df_emocao = df.withColumn(":D", locate(":D", col("tweet_text")))\
                .withColumn(":)", locate(":)", col("tweet_text")))\
                    .withColumn(":]", locate(":]", col("tweet_text")))\
                        .withColumn(":-)", locate(":-)", col("tweet_text")))\
                            .withColumn(":P", locate(":P", col("tweet_text")))\
                                .withColumn(":p", locate(":p", col("tweet_text")))\
                                    .withColumn(":v", locate(":v", col("tweet_text")))\
                                        .withColumn(": )", locate(": )", col("tweet_text")))\
                                            .withColumn(":(", locate(":(", col("tweet_text")))\
                                                .withColumn(":[", locate(":[", col("tweet_text")))\
                                                    .withColumn(":{", locate(":{", col("tweet_text")))

df_emocao.show()

# %%
df_simbolos = df_emocao.withColumn('simbolo', least(*[(when(col(c).isNull() | (col(c) == 0), "None").otherwise(c))for c in df_emocao.columns[3:]]))

df_simbolos = df_simbolos.drop(*todas_emocoes)

df_completa = df_simbolos.withColumn('Sentimento', when(df_simbolos.simbolo.isin(emocaopos), 'positivo')\
                                                .when(df_simbolos.simbolo.isin(emocaoneg), 'negativo')\
                                                    .otherwise("neutra"))

df_completa.show(truncate=True)


# %%
df_out = df_completa.withColumn('Ano', date_format(df_completa.tweet_date, "yyyy"))\
                        .withColumn('Mes', date_format(df_completa.tweet_date, "MM"))\
                            .withColumn('Dia', date_format(df_completa.tweet_date, "dd"))
                            
df_out = df_out.filter(df_out.Ano >= 2018)

df_out.show()

df_out.write.partitionBy("Ano","Mes","Dia").parquet("./Desafio_XPTO_Out", mode = 'overwrite')
print("Done!!")


