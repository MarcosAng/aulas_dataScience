import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('C:\\cursos\\sctec\\analisedados\\primeiro_projeto_python\\2.4\\Titanic.csv')

survived_counts = df['Survived'].value_counts()
print(survived_counts)

plt.figure(figsize=(8, 6))

plt.bar(survived_counts.index, survived_counts, color=['blue', 'orange'])

plt.title('Contagem de Sobreviventes e Não Sobreviventes')
plt.xlabel('Sobreviventes (1) e Não Sobreviventes (0)')
plt.ylabel('Contagem')
plt.show()