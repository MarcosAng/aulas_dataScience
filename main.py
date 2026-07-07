import pandas as pd
import numpy as np
import seaborn as sns

df = pd.read_csv('C:\\cursos\\sctec\\analisedados\\primeiro_projeto_python\\2.4\\Titanic.csv')

print(df.head())

print(df.info())

#traz informações estatísticas do dataset como media, desvio padrão, valores mínimos e máximos, entre outros.

print(df.describe())

#Datatypes das colunas do dataset
print(df.dtypes)

#Filtro
print(df[df['Age'] >=10].head())

#quantidade de linhas duplicadas
linhasduplicadas = df[df.duplicated()]
print(len(linhasduplicadas))
#imprime a quantidade de linhas do dataset
print(len(df))

df.drop_duplicates(inplace=True, keep='last')
#imprime a quantidade de linhas do dataset após remover as duplicadas
print(len(df))

#removendo linhas com valores nulos na coluna Parch
df.dropna(subset=['Parch'], inplace=True)

#substituindo valores nulos por 0
df.replace(np.nan, '0', inplace=True)
print(df)

#renomeando a coluna sex para Genero
df = df.rename(columns={'Sex': 'Genero'})
print(df.head(5))

#ordenando o dataset pela coluna Genero em ordem crescente
sorted_df = df.sort_values(by='Genero', ascending=True)