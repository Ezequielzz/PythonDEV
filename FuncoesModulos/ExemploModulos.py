import math
from datetime import datetime
import operacoes
import estatisticas


raiz_quadrada = math.sqrt(25)  # Calcula a raiz quadrada de 25
seno_30_graus = math.sin(
    math.radians(30)) 
# Calcula o seno de 30 graus convertidos para radianos
# No exemplo acima, o módulo math é importado para realizar cálculos matemáticos.
# A função radians converte graus para radianos, e sin calcula o seno.


data_atual = datetime.now()  # Obtém a data e hora atual
ano_atual = data_atual.year  # Obtém o ano atual
print(data_atual)
print(ano_atual)
# Neste exemplo, apenas a classe datetime do módulo datetime é importada.
# Isso torna o código mais legível, pois não precisamos usar o prefixo datetime. para acessar suas funcionalidades.

resultado_soma = operacoes.somar(5, 3)
resultado_subtracao = operacoes.subtrair(10, 4)

print(resultado_soma)
print(resultado_subtracao)


dados = [2, 3, 5, 7, 11, 13, 17]
media = estatisticas.calcular_media(dados)
mediana = estatisticas.calcular_mediana(dados)