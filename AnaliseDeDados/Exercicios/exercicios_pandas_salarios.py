import pandas as pd

df = pd.read_csv(r'C:\Users\willi\Documents\GitHub\EstudosPython\AnaliseDeDados\Exercicios\Salaries.csv')

# Verifique o head do DataFrame
#print(df.head())

# Use o método .info () para descobrir quantas entradas existem
#print(df.info())

# Qual é o "BasePay" médio?
#print(df['BasePay'].mean())

# Qual é a maior quantidade de "OvertimePay" no conjunto de dados?
#print(df['OvertimePay'].max())

# Qual é o cargo de JOSEPH DRISCOLL? Nota: use todas as maiúsculas, caso contrário você pode obter uma resposta que não coincida
# (há também um Joseph Driscoll com minúsculas)
#print(df[df['EmployeeName'] =='JOSEPH DRISCOLL']['JobTitle'])

# Quanto JOSEPH DRISCOLL ganha (incluindo benefícios)?
#print(df[df['TotalPayBenefits'] == df['TotalPayBenefits'].max()])

# Qual o nome da pessoa paga mais baixa (incluindo benefícios)? Você percebe algo estranho sobre o quanto ele ou ela é paga?
# Não tem a informação do salario dele
#print( print(df[df['TotalPayBenefits'] == df['TotalPayBenefits'].min()]) )

# Qual foi a média (média) BasePay de todos os funcionários por ano? (2011-2014)?
#print(df.groupby('Year').mean()['BasePay'])

# Quantos títulos de trabalho únicos existem?
#print(df['JobTitle'].nunique())

# Quais são os 5 principais empregos mais comuns?
#print(df['JobTitle'].value_counts().head(5))

# Quantos Títulos de Trabalho foram representados por apenas uma pessoa em 2013? 
# (Por exemplo, títulos de trabalho com apenas uma ocorrência em 2013?)
#print(sum(df[df['Year'] == 2013]['JobTitle'].value_counts() == 1))

# Quantas pessoas têm a palavra Chefe em seu cargo?
'''def chief_string(title):
    if 'chief' in title.lower():
        return True
    else:
        return False

print( sum(df['JobTitle'].apply(lambda x: chief_string(x))) )'''
