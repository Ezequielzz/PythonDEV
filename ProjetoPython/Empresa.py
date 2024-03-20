import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import yaml

with open("ProjetoPython/empresa.yaml", "r") as file:
    empresa = yaml.safe_load(file)

df_vendas = pd.DataFrame(empresa["vendas"])
df_cliente = pd.DataFrame(empresa["comportamento_do_cliente"])
df_produto = pd.DataFrame(empresa["desempenho_do_produto"])


# Converter a coluna 'data' para o tipo datetime do pandas
df_vendas["data"] = pd.to_datetime(df_vendas["data"])

# Extrair o mês da data e adicionar como uma nova coluna chamada 'mes'
df_vendas["mes"] = df_vendas["data"].dt.month


# plt.figure(figsize=(10, 6))
# sns.barplot(
#     data=df_vendas, x="cliente_id", y="preco_unitario", palette="pastel", estimator=sum
# )
# plt.title("Desempenho de Vendas - Seaborn")
# plt.xlabel("Id Cliente")
# plt.ylabel("Preço Unitário")
# plt.grid(True)
# plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(data=df_vendas, x="mes", y="preco_unitario", palette="pastel", estimator=sum)
plt.title("Vendas Mensais")
plt.xlabel("Mês")
plt.ylabel("Receita Total")
plt.grid(True)
plt.show()
