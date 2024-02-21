#Criação de Listas:

# Lista de números
numeros = [1, 2, 3, 4, 5]

# Lista de strings
frutas = ["maçã", "banana", "laranja"]

# Lista mista
misturada = [1, "python", True, 3.14]

#Acesso a Elementos:

# Acesso por índice
primeiro_elemento = numeros[0]  # Resultado: 1

# Índices negativos contam a partir do final
ultimo_elemento = frutas[-1]  # Resultado: "laranja"

#Modificação de Elementos:

# Modificar um elemento
frutas[1] = "kiwi"  # Agora a lista é ["maçã", "kiwi", "laranja"]

#Adição e Remoção de Elementos:

# Adicionar elemento ao final da lista
frutas.append("uva")  # Resultado: ["maçã", "kiwi", "laranja", "uva"]

# Remover elemento por valor
frutas.remove("kiwi")  # Resultado: ["maçã", "laranja", "uva"]

# Exemplo de Slicing
sublista = numeros[1:4]  # Resultado: [2, 3, 4]




# Criação de Tuplas:

# Tupla de números
coordenadas = (10, 20, 30)

# Tupla de strings
cores = ("vermelho", "verde", "azul")

# Tupla mista
informacoes = (1, "Python", True)

#Acesso a Elementos:

# Acesso por índice
primeiro_elemento = coordenadas[0]  # Resultado: 10

# Índices negativos contam a partir do final
ultimo_elemento = cores[-1]  # Resultado: "azul"

# Imutabilidade:

# Tentativa de modificar um elemento resultará em erro
cores[0] = "amarelo"  # TypeError: 'tuple' object does not support item assignment


# Criação de Conjuntos:
# Conjunto de números
numeros = {1, 2, 3, 4, 5}

# Conjunto de letras
vogais = {'a', 'e', 'i', 'o', 'u'}

# Operações de Conjuntos:
# União de conjuntos
uniao = numeros.union(vogais)  # Resultado: {1, 2, 3, 4, 5, 'a', 'e', 'i', 'o', 'u'}

# Interseção de conjuntos
intersecao = numeros.intersection({3, 4, 5, 6})  # Resultado: {3, 4, 5}

# Diferença de conjuntos
diferenca = numeros.difference({4, 5, 6})  # Resultado: {1, 2, 3}
