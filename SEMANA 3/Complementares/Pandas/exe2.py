import pandas as pd
import matplotlib

#Importa o Dataset
dataset = pd.read_csv('googleplaystore.csv', sep=',')

#Tratando Dados
dataset = dataset.drop_duplicates(subset=['App'])
dataset = dataset.dropna()
dataset['Reviews'] = pd.to_numeric(dataset['Reviews'])

dataset['Price'] = dataset['Price'].str.replace('$','')
dataset['Price'] = pd.to_numeric(dataset['Price'])

dataset['Installs'] = dataset['Installs'].str.replace('+','')
dataset['Installs'] = dataset['Installs'].str.replace(',','')
dataset['Installs'] = pd.to_numeric(dataset['Installs'])

# print(dataset.info())
# print(dataset.isna().sum())

sample = dataset.loc[:,['App', 'Installs']]
sample = sample.sort_values(by=['Installs', 'App'], ascending=(False,True))
sample.head(5).plot.bar(x='App', y='Installs', rot=0, figsize=(15, 8), fontsize=10)
print(sample.head(20))
