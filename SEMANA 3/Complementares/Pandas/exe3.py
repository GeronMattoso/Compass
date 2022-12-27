import pandas as pd

#Controla o display de linhas, caso necessário
pd.set_option("display.max_rows", 60)

#Importa o Dataset
dataset = pd.read_csv('wines_SPA.csv', sep=';')

print(dataset.head())
print(dataset.info())
print(dataset.isna().sum())


#Tratando dados
dataset = dataset.drop_duplicates()
dataset = dataset.dropna()
dataset = dataset[pd.to_numeric(dataset['year'], errors='coerce').notnull()]
dataset['year'] = pd.to_numeric(dataset['year'])

dataset = dataset[pd.to_numeric(dataset['price'], errors='coerce').notnull()]
dataset['price'] = pd.to_numeric(dataset['price'])

print(dataset.info())
print(dataset.isna().sum())