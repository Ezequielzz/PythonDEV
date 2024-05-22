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
            dinheiro_acumulado += 10000  # Aumenta a pontuação em 10000
        else:
            print("Resposta incorreta! A resposta correta é:", pergunta["resposta"])
    return dinheiro_acumulado

if __name__ == "__main__":
    dinheiro_total = 0
    dinheiro_total += jogar(perguntasFacil)
    dinheiro_total += jogar(perguntasMédio)
    dinheiro_total += jogar(perguntasDificil)
    print("Pontuação total: $", dinheiro_total)
