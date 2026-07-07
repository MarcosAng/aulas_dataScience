import pandas as pd

funcionarios = {
    'Nome': ['Alice', 'Bob', 'Charlie', 'David'],   
    'Endereço': ['Rua A', 'Rua B', 'Rua C', 'Rua D'],
    'Data Nascimento': ['1990-01-01', '1985-05-15', '1992-09-30', '1988-12-10'],
    'Data de Admissão': ['2020-01-01', '2019-05-15', '2021-09-30', '2018-12-10'],
    'Salário': [5000, 6000, 7000, 8000],
    'Cargo': ['Analista', 'Gerente', 'Diretor', 'Presidente']
}

df = pd.DataFrame(funcionarios)
print(df)

#linhas da coluna data de admissão
print(df['Data de Admissão'])