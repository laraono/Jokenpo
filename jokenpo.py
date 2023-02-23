import random
opcoes = ["pedra", "papel", "tesoura"]
escolha = input('Pedra, papel, tesoura! ')
resposta = random.choice(opcoes)
if escolha in opcoes:
    if (escolha == "pedra" and resposta == "tesoura") or (escolha == "papel" and resposta == "pedra") or (escolha == "tesoura" and resposta == "papel"):
        print("Você escolheu {} e eu {} - Você ganhou!".format(escolha, resposta))
    elif escolha == resposta:
        print("Você escolheu {} e eu {} - Empate!".format(escolha, resposta))
    elif (escolha == "pedra" and resposta == "papel") or (escolha == "papel" and resposta == "tesoura") or (escolha == "tesoura" and resposta == "pedra"):
        print("Você escolheu {} e eu {} - Eu ganhei!".format(escolha, resposta))
else:
    escolha = input('Pedra, papel, tesoura! ')