import pandas as pd

movies_uri = 'https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula4.1/movies.csv'

ratings_uri = 'https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula1.2/ratings.csv'

movies, ratings = pd.read_csv(movies_uri), pd.read_csv(ratings_uri)

print('A função head pega os 5 primeiros resultados')
print(ratings.head())

print('A função print faz uma seleção de dados únicos')
print(ratings['rating'].unique())

print('A função mean faz uma média entre os dados')
print(ratings['rating'].mean())

print('A função min e max mostram, respectivamente, o menor e maior dado')
print(ratings['rating'].min(), ratings['rating'].max())

print('A função describe faz um resumo com os principais dados do dataframe')
print(ratings.describe())
