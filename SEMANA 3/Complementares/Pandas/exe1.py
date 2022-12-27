import pandas as pd

#Controla o display de linhas, caso necessário
#pd.set_option("display.max_rows", 60)

#Importa o Dataset
data = pd.read_csv('actors.csv', sep=',')

# #Representa o dataset
# #dataset

# #O ator/atriz com maior número de filmes
maiorNumeroAtorFilme = data[['Actor', 'Number of Movies']][data['Number of Movies'] == data['Number of Movies'].max()]
print(maiorNumeroAtorFilme)
# #O ator/atriz com maior média de filmes
# maiorMediaFilme = dataset[['Actor', 'Average per Movie']][dataset['Average per Movie'] == dataset['Average per Movie'].max()]

# #Adquire a media de filmes
# mediaFilmes = dataset['Number of Movies'].mean()

# #Filme mais frequente / moda
# filmeFrequente = dataset['#1 Movie'].value_counts().to_frame().head(1)



# #Outputs
# print(f"\n{maiorNumeroAtorFilme}\n")
# print(f"\nMédia do número de filmes: {mediaFilmes}\n")
# print(f"\n{maiorMediaFilme}\n")
# print(f"\n{filmeFrequente}\n")