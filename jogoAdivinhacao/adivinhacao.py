print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = 42
rodada = 1
total_de_tentativas = 3

while (rodada <= total_de_tentativas):
    print("Tentativa {} de {}".format(rodada,total_de_tentativas))
    chute_str = input("Digite o seu numero: ")
    print("Você digitou", chute_str)

    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("você acertou!")
    else:

        if (maior):
            print("você errou! O seu chute foi maior do que o número secreto")
        elif (menor):
            print("Você errou! O seu chute foi menor do que o número secreto")

    rodada = rodada + 1
