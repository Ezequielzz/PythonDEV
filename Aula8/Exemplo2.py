import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar os dados
df = pd.read_excel('Aula8/filmes.xlsx')

# Definir o estilo dos gráficos seaborn
sns.set_style("whitegrid")

# Gráfico de distribuição das avaliações dos filmes
plt.figure(figsize=(8, 6))
sns.histplot(df['Avaliacao'], bins=10, kde=True, color='skyblue')
plt.title('Distribuição das Avaliações dos Filmes')
plt.xlabel('Avaliação')
plt.ylabel('Contagem')
plt.show()

# Gráfico de contagem de avaliações por faixa
plt.figure(figsize=(8, 6))
sns.countplot(x='Avaliacao', data=df, palette='Set2')
plt.title('Contagem de Avaliações por Faixa')
plt.xlabel('Avaliação')
plt.ylabel('Contagem')
plt.show()

# Gráfico de dispersão entre as avaliações e o ano de lançamento dos filmes
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Avaliacao', y='Ano', data=df, color='green')
plt.title('Dispersão entre Avaliações e Ano de Lançamento')
plt.xlabel('Avaliação')
plt.ylabel('Ano de Lançamento')
plt.show()
