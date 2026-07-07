import numpy as np


arr2 = np.array([[1, 2, 3], 
                 [4, 5, 6], 
                 [7, 8, 9]

])

print(arr2[1,2]) # saida

#informacoes da matriz

print(f"Shape da matriz: {arr2.shape}")
print(f"Número de dimensões: {arr2.size}")
print(f"Tipo dos elementos: {arr2.dtype}")

#operacoes matematicas

arr1 = np.array([10, 20, 38, 48, 65])

print(arr1 + 10) #soma 10 a cada elemento
print(arr1 * 2) #multiplica cada elemento por 
print(arr1 / 2) #divide cada elemento por 2

print('Media:')
print(np.mean(arr1)) #media dos elementos da matriz

print('Mediana:')
print(np.median(arr1)) #mediana dos elementos da matriz

print('Desvio Padrão:')
print(np.std(arr1)) #desvio padrao dos elementos da matriz  

print('Variância:')
print(np.var(arr1)) #variancia dos elementos da matriz