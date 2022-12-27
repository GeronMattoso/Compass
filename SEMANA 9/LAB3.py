# %% [markdown]
# <head>
#     <h1>Semana 9 - LAB 3<h1>
# <head>
#     <div>
#     <img align="left" alt="Geron-Mattoso" height="100" width="150" 
# src="https://spark.apache.org/images/spark-logo-rev.svg">
#     </div>

# %%
import os
caminho = os.getcwd()
print(caminho)

# %%
from pyspark import SparkContext, SQLContext
from pyspark.sql import *
from pyspark.sql.functions import *

import os
caminho = os.getcwd()
print(caminho)


spark = SparkSession.builder.appName("Exercicios").getOrCreate()

sqlContext = SQLContext(spark.sparkContext)



# %%
df_nomes = spark.read.csv(caminho + '/nomes.csv', header = True, inferSchema=True)

# %%
type(df_nomes)

# %%
df_nomes.show(5)

# %%
df_nomes.printSchema()

# %%
df_nomes.select(df_nomes.nome, df_nomes.sexo).show(5)

# %%
df_select = df_nomes.select(df_nomes.nome,
                            df_nomes.ano,
                            df_nomes.ano > 1950,
                            df_nomes.ano + 1000)
df_select.show(5)

# %%
df_nomes.registerTempTable("pessoas")

# %%
sqlContext.sql("select count (*) from pessoas").show()

# %%
sqlContext.sql("select nome, ano, ano+1000 as futuro FROM pessoas").show(5)

# %%
df_nomes.filter(df_nomes.ano > 1990).select(df_nomes.nome, df_nomes.ano).show(5)

# %%
df_nomes.filter(df_nomes.ano > 1990)\
    .select(df_nomes.nome, df_nomes.ano)\
        .orderBy(df_nomes.ano, df_nomes.nome).show(5)

df_nomes.filter(df_nomes.ano > 1990)\
    .select(df_nomes.nome, df_nomes.ano)\
        .orderBy(df_nomes.ano.desc(), df_nomes.nome).show(5)



# %%
df_nomes.select("nome", "ano", (df_nomes.ano > 2000).alias('recente')).show(5)

# %%
spark.sql("SELECT nome, ano, ano > 2000 as recente FROM pessoas").show(5)

# %%
df_nomes.groupBy('ano').count().show(5)

# %%
df_nomes.groupBy('sexo').count().show(5)

# %% [markdown]
# #### EXERCÍCIO 1: Faça o agrupamento sexo e realize a contagem. Responda as seguintes perguntas:
# 
# •	Qual o sexo que mais aparece?
# 
# •	Qual foi a diferença entre o sexo Masculino (F) e do Feminino (F)?
# 

# %%
'''Qual sexo mais aparece'''
df_quant = spark.sql("select sexo, count(sexo) as count from pessoas group by sexo")

df_quant.show(1)

'''qual a diferença entrer sexos'''

df_quant.createOrReplaceTempView("quant")

spark.sql("SELECT MAX(count)-MIN(count) AS diferenca FROM quant").show()


# %% [markdown]
# ##### EXERCÍCIO 2:  Crie uma nova coluna no DataFrame que contenha apenas números. Nesta coluna chamada RANKING deverá ter o número que representa a colocação do nome na lista, sendo o número 1 o nome mais usado em todos os anos.

# %%
''''
agrupar nomes por quantidade
Criar coluna com id e ordenar
'''
df_ranking = df_nomes.groupBy("nome")\
    .sum("total").orderBy(col("sum(total)").desc())\
        .withColumn("Ranking", monotonically_increasing_id()+1).show()


# %% [markdown]
# EXERCÍCIO 3:  Crie 03 novas colunas no DataFrame que contenha apenas Sim e Não. Cada coluna deve-se chamar DECADA_80, DECADA_90, DECADA_00 e o conteúdo deve ser SIM ou NÃO  de acordo com o ano definido na tabela.

# %%
#https://sparkbyexamples.com/pyspark/pyspark-when-otherwise/

df_decadaSN = df_nomes\
    .withColumn('DECADA_80', when((df_nomes.ano >= 1980), 'Sim').when ((df_nomes.ano < 1990), 'Nao').otherwise("df_nomes.ano"))\
        .withColumn('DECADA_90', when((df_nomes.ano >= 1990), 'Sim').when ((df_nomes.ano < 2000), 'Nao').otherwise("df_nomes.ano"))\
            .withColumn('DECADA_00', when((df_nomes.ano >= 2000), 'Sim').when((df_nomes.ano < 2010), 'Nao').otherwise("df_nomes.ano"))\

df_decadaSN.show(5)

# %% [markdown]
# EXERCÍCIO 4:  Remova do Dataframe a coluna DECADA_00 e mostrar o novo Dataframe.

# %%
df_decadaremoved00 = df_decadaSN.drop('DECADA_00')

df_decadaremoved00.show(5)

# %% [markdown]
# EXERCÍCIO 5: Gerar dois arquivos CSV. O primeiro com os nomes do sexo masculino nascidos na década de 80. O segundo com os nomes do sexo feminino nascidos na década de 80.

# %%

df_decadaremoved00.filter((df_decadaremoved00.DECADA_80 == 'Sim') & (df_decadaremoved00.sexo == 'M'))\
    .drop('DECADA_80','DECADA_90','ano', 'total', 'sexo')\
    .write.csv('./Masculino_DECADA_80', mode="overwrite")

df_decadaremoved00.filter((df_decadaremoved00.DECADA_80 == 'Sim') & (df_decadaremoved00.sexo == 'F'))\
    .drop('DECADA_80','DECADA_90','ano', 'total', 'sexo')\
    .write.csv('./Feminino_DECADA_80', mode="overwrite")


