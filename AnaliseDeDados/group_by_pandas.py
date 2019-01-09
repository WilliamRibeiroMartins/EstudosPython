import pandas as pd

data = {'Empresa': ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
        'Nome': ['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
        'Venda': [200, 120, 340, 124, 243, 350]}

df = pd.DataFrame(data)

# Basta usar o método groupby, informando pelo o que você deseja agrupar. Após o agrupamento, 
# basta realizar a operação desejada (soma, média, etc)
group_soma = df.groupby('Empresa').sum()
group_describe = df.groupby('Empresa').describe()
print(group_describe)