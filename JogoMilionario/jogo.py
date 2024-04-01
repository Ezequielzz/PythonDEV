from perguntas import perguntasFacil, perguntasMédio, perguntasDificil

def apresentar_pergunta(pergunta):
    print(pergunta["pergunta"])
    for opcao in pergunta["opcoes"]:
        print(opcao)
    resposta = input("Escolha a opção correta (a, b, c, d): ").lower()
    return resposta

def jogar(perguntas):
    dinheiro_acumulado = 0
    for pergunta in perguntas:
        resposta = apresentar_pergunta(pergunta)
        if resposta == pergunta["resposta"]:
            print("Resposta correta!")
            dinheiro_acumulado += 1000  # Aumenta a pontuação em 1000
            print("Dinheiro acumulado: $", dinheiro_acumulado)
        else:
            print("Resposta incorreta!")
    print("Pontuação final: $", dinheiro_acumulado)

if __name__ == "__main__":
    jogar(perguntasFacil)
    jogar(perguntasMédio)
    jogar(perguntasDificil)
