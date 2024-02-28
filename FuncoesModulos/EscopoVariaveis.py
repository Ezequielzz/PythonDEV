def exemplo_escopo():
    variavel_local = 10
    # print(variavel_local)

exemplo_escopo()  # Saída: 10
# print(variavel_local)  # Erro: variavel_local não está definida fora da função

def calcular_quadrado(numero):
    return numero ** 2

resultado = calcular_quadrado(5)
# print(resultado)  # Saída: 25

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

resultado = fatorial(4)
print(resultado)  # Saída: 120