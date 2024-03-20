import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar os dados
df = pd.read_excel('Aula8/filmes.xlsx')

# Plotar o gráfico
plt.figure(figsize=(10, 6))
plt.hist(df["Ano"], bins=5, color="skyblue", edgecolor="black")
plt.title('Variação de Avaliação dos Filmes')
plt.xlabel('Nome')
plt.ylabel('Avaliacao')
plt.tight_layout()
plt.show()

