import numpy as np

arr = np.arange(50).reshape((5, 10))
print('Array bidimensional')
print(arr)
print('')

# Os números antes da virgula, se referem as linhas, após a virgula, se referem as colunas
print(arr[:3, :5])
print('')

# Verifica todos os campos, se eles são maiores que 30
print(' Verifica todos os campos, se eles são maiores que 30')
bol = arr > 30
print(bol)
print('')

# Exibindo somente os registro que são maiores que 30
print('Exibindo somente os registro que são maiores que 30')
print(arr[bol])
print('')