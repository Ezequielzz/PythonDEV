import pandas as pd
import yaml
import matplotlib.pyplot as plt


# Carregar os dados dos funcionários a partir do arquivo YAML
with open('Aula7/dados_funcionarios.yaml', 'r') as file:
    dados_yaml = yaml.safe_load(file)

# Converter para DataFrame
df = pd.DataFrame(dados_yaml['funcionarios'])

# # 1. Análise Exploratória
# print("1. Análise Exploratória:")
# print(df.head())  # Visualizar as primeiras linhas
# print(df.info())  # Informações sobre os tipos de dados e valores nulos
# print(df.describe())  # Estatísticas descritivas básicas

# # 2. Seleção e Filtragem de Dados
# print("\n2. Seleção e Filtragem de Dados:")
# funcionarios_acima_30 = df[df['Idade'] > 30]
# print("Funcionários com mais de 30 anos:")
# print(funcionarios_acima_30)


# funcionarios_salario_acima_4000 = df[df['Salario'] > 4000]
# print("\nFuncionários com salário acima de 4000:")
# print(funcionarios_salario_acima_4000)

# 3. Manipulação de Dados
print("\n3. Manipulação de Dados:")
df['salario_ajustado'] = df['Salario'] * 1.10  # Aumento de 10% no salário
print(df)

# 4. Agregação de Dados
print("\n4. Agregação de Dados:")
salario_medio = df['Salario'].mean()
print("Salário médio dos funcionários antes do ajuste:", salario_medio)


print("\n4. Agregação de Dados:")
salario_medio = df['salario_ajustado'].mean()
print("Salário médio dos funcionários depois do ajuste:", salario_medio)


idade_media = df['Idade'].mean()
print("Idade média dos funcionários:", idade_media)
