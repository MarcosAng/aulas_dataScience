import numpy as np

arr1 = np.array([10, 20, 30, 40, 50])

#media
media = np.mean(arr1)
print(media)

#valores minimos e maximos
minimo = np.min(arr1)
print(f"Valor mínimo: {minimo}")
maximo = np.max(arr1)
print(f"Valor máximo: {maximo}")
import matplotlib.pyplot as plt

#criando
nome_funcionarios = ['João', 'Maria', 'Pedro', 'Ana']
salarios = [2500, 3000, 2000, 3500]

plt.bar(nome_funcionarios, salarios, color='green')

#Adicionando título e rótulos aos eixos
plt.xlabel('Funcionários')
plt.ylabel('Salários')
plt.title('Salários dos Funcionários')

plt.show()
