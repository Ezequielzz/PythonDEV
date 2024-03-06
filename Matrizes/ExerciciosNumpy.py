import numpy as np
import matplotlib.pyplot as plt

# Dados fictícios de preços médios diários para duas ações (em dólares)
preco_medio_acao1 = np.array([50, 52, 48, 55, 53, 51, 49, 50, 54, 52])
preco_medio_acao2 = np.array([120, 122, 118, 125, 123, 121, 119, 120, 124, 122])

# Número de ações que o investidor possui de cada empresa
acoes_acao1 = 100  # Exemplo: o investidor possui 100 ações da Ação 1
acoes_acao2 = 50  # Exemplo: o investidor possui 50 ações da Ação 2

# Calculando o valor do investimento em cada dia
# Exibindo os resultados diariamente
valInvAcao1 = acoes_acao1 * preco_medio_acao1
valInvAcao2 = acoes_acao2 * preco_medio_acao2
patrimonioTotal = valInvAcao1 + valInvAcao2

for dia in range(len(preco_medio_acao1)):
    print(
        f"Dia {dia+1}: Valor do investimento na Ação 1: ${valInvAcao1[dia]} - Valor do investimento na Ação 2: ${valInvAcao2[dia]}"
    )

# Plotando o gráfico da evolução patrimonial do investidor
dias = list(range(1, 11))

plt.plot(dias, patrimonioTotal, label='Patrimônio Total', marker='o', linestyle='-', color='b')
plt.plot(dias, valInvAcao2, label='Valor Investido na Ação 2', marker='o', linestyle='-', color='g')
plt.plot(dias, valInvAcao1, label='Valor Investido na Ação 1', marker='o', linestyle='-', color='r')

plt.xlabel('Dia')
plt.ylabel('Valor ($)')
plt.title('Evolução Patrimonial e de Ações do Investidor')
plt.legend()
plt.grid(True)
plt.show()
