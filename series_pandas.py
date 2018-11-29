import numpy as np
import pandas as pd

labels = ['a', 'b', 'c']
minha_lista = [10, 20, 30]
arr = np.array([10, 20, 30])
d = {'a':10, 'b':20, 'c':30}

# Series seriam uma especie de dicionario do pandas, aonde um valor (data), está associado a um index/label (index)
series_lista = pd.Series(data=minha_lista, index=labels)
series_array = pd.Series(data=arr, index=labels)
series_dict = pd.Series(data=d, index=labels)

# Posso acessar o valor através do index, como em um dicionario
#print(series_lista['b'])

# Podemos realizar operações com as Series
ser1 = pd.Series(data=[1, 2, 3, 4], index=['EUA', 'Alemanha', 'URSS', 'Japão'])
ser2 = pd.Series(data=[1, 2, 3, 4], index=['Alemanha', 'EUA', 'Itália', 'Japão'])

ser_soma = ser1 + ser2
print(ser_soma)