import pandas as pd

# Concatenação: Concatena 2 ou mais dataframes com as mesmas dimensões. Se for unir pelas colunas, é necessário ter a mesma 
# quantidades de colunas, se for unir pelas linhas, é necessário ter a mesma quantidade de linhas
df1 = pd.DataFrame({
    'A' : ['A0', 'A1', 'A2', 'A3'],
    'B' : ['B0', 'B1', 'B2', 'B3'],
    'C' : ['C0', 'C1', 'C2', 'C3'],
    'D' : ['D0', 'D1', 'D2', 'D3'],
}, index=[0, 1, 2, 3])

df2 = pd.DataFrame({
    'A' : ['A4', 'A5', 'A6', 'A7'],
    'B' : ['B4', 'B5', 'B6', 'B7'],
    'C' : ['C4', 'C5', 'C6', 'C7'],
    'D' : ['D4', 'D5', 'D6', 'D7'],
}, index=[4, 5, 6, 7])

df3 = pd.DataFrame({
    'A' : ['A8', 'A9', 'A10', 'A11'],
    'B' : ['B8', 'B9', 'B10', 'B11'],
    'C' : ['C8', 'C9', 'C10', 'C11'],
    'D' : ['D8', 'D9', 'D10', 'D11'],
}, index=[8, 9, 10, 11])

#concact_columns = pd.concat([df1, df2, df3]) #Unir pelas colunas
#concact_rows = pd.concat([df1, df2, df3], axis=1) #Unir pelas linhas (basta alterar o eixo de referencia)

#------------------------------------------------------------------------------------------------------

# Mesclar: Mescla os dataframes utilizando uma coluna com dados em comum.
# Utiliza uma lógica parecida com a do mesclagem do SQL
esquerda = pd.DataFrame({
    'Key' : ['K0', 'K1', 'K2', 'K3'],
    'A' : ['A0', 'A1', 'A2', 'A3'],
    'B' : ['B0', 'B1', 'B2', 'B3'],
    
})

direita = pd.DataFrame({
    'Key' : ['K0', 'K1', 'K2', 'K3'],
    'C' : ['C0', 'C1', 'C2', 'C3'],
    'D' : ['D0', 'D1', 'D2', 'D3'],
})

#inner_merge = pd.merge(esquerda, direita, how='inner', on='Key')

esquerda = pd.DataFrame({
    'Key1' : ['K0', 'K1', 'K2', 'K3'],
	'Key2' : ['K0', 'K1', 'K2', 'K3'],
    'A' : ['A0', 'A1', 'A2', 'A3'],
    'B' : ['B0', 'B1', 'B2', 'B3'],
    
})

direita = pd.DataFrame({
    'Key1' : ['K0', 'K1', 'K2', 'K3'],
	'Key2' : ['K0', 'K1', 'K2', 'K3'],
    'C' : ['C0', 'C1', 'C2', 'C3'],
    'D' : ['D0', 'D1', 'D2', 'D3'],
})

#doble_merge = pd.merge(esquerda, direita, on=['Key1', 'Key2'])
#outer_merge = pd.merge(esquerda, direita, how='outer', on=['Key1', 'Key2'])

#------------------------------------------------------------------------------------------------------

#Juntar: Combina as colunas dos dataframes indexados potencialmente diferentes em um único dataframe
esquerda = pd.DataFrame({
    'A' : ['A0', 'A1', 'A2'],
    'B' : ['B0', 'B1', 'B2'],
}, index=['K0', 'K1', 'K2'])

direita = pd.DataFrame({
    'C' : ['C0', 'C1', 'C2'],
    'D' : ['D0', 'D1', 'D2'],
}, index=['K0', 'K2', 'K3'])

#inner_join = esquerda.join(direita)
#outer_join = esquerda.join(direita,  how='outer')