# 1 - Variáveis e Operações com Números:
# Crie três variáveis, a, b e c, representando os coeficientes de uma equação quadrática (ax^2 + bx + c).
# Calcule as raízes da equação usando a fórmula de Bhaskara.

# import math

# a = float(input("Digite o coeficiente 'a': "))
# b = float(input("Digite o coeficiente 'b': "))
# c = float(input("Digite o coeficiente 'c': "))
# delta = b**2 - 4*a*c

# if delta < 0:
#     print("A equação não possui raízes reais.")
# elif delta == 0:
#     x = -b / (2 * a)
#     print(f"A equação tem apenas uma raiz real: {x}")
# else:
#     x1 = (-b + math.sqrt(delta)) / (2 * a)
#     x2 = (-b - math.sqrt(delta)) / (2 * a)
#     print(f"A equação tem duas raízes reais: {x1} e {x2}")


# Implemente um programa que converta um valor em dólares para outras moedas (por exemplo, euros e libras).
# Solicite ao usuário o valor em dólares e a taxa de conversão.

# dolar_usuario = float(input("Informe o valor em dólares: "))

# # Definindo taxas de câmbio fixas
# taxacambio_euros = 0.93  # 1 dólar = 0.85 euros
# taxacambio_libras = 0.80  # 1 dólar = 0.72 libras

# euros = round(dolar_usuario * taxacambio_euros, 2)
# libras = round(dolar_usuario * taxacambio_libras, 2)

# print(f"O equivalente a {dolar_usuario} dólares são {euros} euros e {libras} libras.")


# 2 - Manipulação de Strings:
# Crie uma função que receba uma string como entrada e retorne True se ela for um palíndromo
# (lê-se igual de trás para frente), e False caso contrário.

def verificar_palindromo(frase):
    frase = frase.replace(" ", "")
    inicio = 0
    fim = len(frase) - 1

    while inicio < fim:
        if frase[inicio] != frase[fim]:
            return False
        inicio += 1
        fim -= 1
    return True

frase = input("Digite uma frase para verificar se é um palíndromo: ")
resultado = verificar_palindromo(frase)
if resultado:
    print("A frase é um palíndromo.")
else:
    print("A frase não é um palíndromo.")


# Implemente um programa que recebe uma frase do usuário e identifica a palavra mais longa na frase.
