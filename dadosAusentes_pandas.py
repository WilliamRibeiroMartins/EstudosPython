import numpy as np
import pandas as pd

d = {'A': [1, 2, np.nan], 'B': [5, np.nan, np.nan], 'C': [1, 2, 3]}

df = pd.DataFrame(d)
print('Data Frame original')
print(df)
print()

# Cria um novo data frame sem as linhas ou colunas que contém 'NaN'
# O valor informado em thresh, é a quantidade de valores que precisam estar ausentes para excluir a linha
# dfNoNan = df.dropna(thresh=2)
# print(dfNoNan)

# Cria um novo data frame substituindo os 'NaN' pelo valor informado
dfFillNan = df.fillna('teste')
    #Preenche os campos ausentes com valores do campo anterior
dfFillNan = df.fillna(method='ffill')