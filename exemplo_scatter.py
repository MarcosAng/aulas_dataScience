import matplotlib.pyplot as plt

# Definindo variaveis
x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [2, 3, 5, 7, 11, 15, 18, 20]

#criando o gráfico de dispersão
plt.scatter(x, y, label = 'Pontos', color='blue', marker='*', s=100)

plt.legend()

#Adicionando título e rótulos aos eixos
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('Gráfico de Dispersão')

plt.show()