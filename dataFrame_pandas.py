import numpy as np
import pandas as pd

np.random.seed(101)

df = pd.DataFrame(np.random.randn(5, 4), index='A B C D E'.split(), columns='W X Y Z'.split())

# O acesso aos valores é igual ao do dicionário
#print(df['W'])

# Podemos passar uma lista de colunas para exibir
#print(df[['W', 'Z']])

# Para criar uma nova coluna, é só inserir um valor nela
df['new'] = df['W'] + df['X'] # Colocando a soma das duas colunas na coluna nova
#print(df)

# Deletando uma coluna (axis=0 é a linha, axis=1 é a coluna)
df.drop('new', axis=1, inplace=True)

# Acessando um valor pelo nome das linhas e das colunas
#print(df.loc['A','W'])

# Acessando vários valores
#print(df.loc[['A', 'B'],['X', 'Y', 'Z']])

# Acessando um valor pela posição linhas e das colunas
#print(df.iloc[1:4, 2:])