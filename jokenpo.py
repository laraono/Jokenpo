import random
opcoes = ["pedra", "papel", "tesoura"]
escolha = input('Pedra, papel, tesoura! ').lower()
resposta = random.choice(opcoes)
pontos = 0
tentativas = 0
tentar = True

def goagain():
    novamente = input("Jogar novamente?").lower()
    if novamente == "sim":
        escolha = input('Pedra, papel, tesoura! ').lower()
    else:
        tentar = False
        return tentar


while tentar:
    if escolha in opcoes:
        if (escolha == "pedra" and resposta == "tesoura") or (escolha == "papel" and resposta == "pedra") or (escolha == "tesoura" and resposta == "papel"):
            print("Você escolheu {} e eu {} - Você ganhou!".format(escolha, resposta))
            pontos += 1
            tentativas += 1
            print("Você tem {} pontos e {} tentativas!".format(pontos, tentativas))
            goagain()
        elif escolha == resposta:
            print("Você escolheu {} e eu {} - Empate!".format(escolha, resposta))
            tentativas += 1
            print("Você tem {} pontos e {} tentativas!".format(pontos, tentativas))
            goagain()
        elif (escolha == "pedra" and resposta == "papel") or (escolha == "papel" and resposta == "tesoura") or (escolha == "tesoura" and resposta == "pedra"):
            print("Você escolheu {} e eu {} - Eu ganhei!".format(escolha, resposta))
            tentativas += 1
            print("Você tem {} pontos e {} tentativas!".format(pontos, tentativas))
            goagain()
    else:
        escolha = input('Pedra, papel, tesoura! ')

