import pandas as pd

df = pd.read_csv('C:\\cursos\\sctec\\analisedados\\primeiro_projeto_python\\2.4\\Ice Cream Sales - temperatures.csv')

#mostrar na tela os valores ordenados da coluna Temperature em ordem crescente

#df.dropna(subset=['Temperature'], inplace=True)

#df.drop_duplicates(inplace=True, keep='last')

sorted_df = df.sort_values(by='Temperature', ascending=True)

print(sorted_df)