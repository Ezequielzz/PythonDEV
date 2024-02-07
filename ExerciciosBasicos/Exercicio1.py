# 1 - Variáveis e Operações com Números:
# Crie duas variáveis, a e b, atribua valores e realize as seguintes operações:

a = 10
b = 5

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
divisao_inteira = a // b
resto = a % b
potencia = a**b

# print(soma, subtracao, multiplicacao, divisao, divisao_inteira, resto, potencia)


# Declare uma variável para representar o raio de um círculo e calcule sua área 
# usando a fórmula área = π * raio^2. Considere π como 3.14.

raio = 12

area = 3.14 * raio**2

# print(area)

# 2 - Manipulação de Strings:
# Declare duas strings, nome e sobrenome, e concatene-as para formar o nome completo. Imprima o resultado.

nome = "João"
sobrenome = "Silva"
nome_completo = nome + " " + sobrenome

# print(nome_completo)

# Crie uma string que represente uma frase e use métodos de string para:

# Converter todas as letras para maiúsculas.
# Converter todas as letras para minúsculas.
# Substituir uma palavra por outra na frase.

fraseSpfc = "Amado clube brasileiro!"

fraseSpfc_upper = fraseSpfc.upper()

fraseSpfc_lower = fraseSpfc.lower()

fraseSpfc_substituida =  fraseSpfc.replace("brasileiro", "paulista")

# print(fraseSpfc)
# print(fraseSpfc_upper)
# print(fraseSpfc_lower)
# print(fraseSpfc_substituida)

# 3 - Utilização de Listas e Tuplas:
# Crie uma lista com três cores diferentes. Adicione mais duas cores a essa lista e imprima-a.

cores = [ "Vermelho", "Verde", "Azul"]

cores.append("Amarelo")
cores.append("Rosa")

# Declare uma tupla com as coordenadas (latitude, longitude) de um local e imprima cada valor separadamente.

# Declarando a tupla com as coordenadas
coordenadas = (40.7128, -74.0060)

# Imprimindo cada valor separadamente
latitude, longitude = coordenadas
print("Latitude:", latitude)
print("Longitude:", longitude)


# 4 - Uso de Operadores Lógicos em Estruturas Condicionais:
# Crie duas variáveis booleanas, tem_sol e tem_chuva, representando condições climáticas. Utilize essas variáveis
# em uma estrutura condicional para decidir se é um dia agradável ou não.

tem_sol = True
tem_chuva = False

if tem_sol:
    print("Dia Agradavel")
elif tem_chuva:
    print("Dia Chuvoso")

# Solicite ao usuário dois números e use operadores lógicos para verificar se ambos são números pares.
# Imprima o resultado.
    
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

sao_pares = (numero1 % 2 == 0) and (numero2 % 2 == 0)

if sao_pares:
    print("Ambos os números são pares.")
else:
    print("Um dos números não é par.")


# Crie uma lista de números e use uma estrutura de repetição para percorrer a lista.
# Utilize operadores lógicos para verificar e imprimir quais números são múltiplos de 3 e ímpares.

# Peça ao usuário para digitar a sua idade e verifique se ela está dentro do intervalo de 18 a 65 anos.
# Imprima uma mensagem correspondente.

# Esses exercícios proporcionarão uma prática abrangente nos temas de operadores e tipos de variáveis em Python,
# ajudando a solidificar o entendimento desses conceitos fundamentais na linguagem de programação.
