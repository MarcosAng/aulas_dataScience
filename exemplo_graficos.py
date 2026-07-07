import matplotlib.pyplot as plt

# criando
#plt.plot([1, 2, 3, 4], [1, 4, 9, 16])

#plt.show()

# dados
x = ['Maças', 'Bananas', 'Laranjas', 'Uvas']
y = [3, 5, 2, 8]

plt.bar(x, y)

#Adicionando título e rótulos aos eixos
plt.xlabel('Frutas')
plt.ylabel('Quantidade')
plt.title('Quantidade de Frutas')

plt.show()