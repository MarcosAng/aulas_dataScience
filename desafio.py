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