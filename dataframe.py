import pandas as pd

data = {
    'Nome': ['Alice', 'Bob', 'Charlie', 'David'],   
    'Idade': [25, 30, 35, 40],
    'Cidade': ['São Paulo', 'Bahia', 'Rio de Janeiro', 'Minas Gerais']
}

df = pd.DataFrame(data)

print(df)

#imprimir o nome
print(df['Nome'])

#imprimir a idade
print(df['Idade'])

#imprimir a cidade
print(df['Cidade']) 

#dados do dataframe
print(df['Nome'])

#acessando uma linha específica
print(df.iloc[1]) #acessa a linha 1

#acessar um valor específico
print(df.loc[0, 'Nome']) #acessa todos os nomes da linha 0