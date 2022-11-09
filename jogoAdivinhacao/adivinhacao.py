print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = 42
chute_str = input("Digite o seu numero: ")

print("Você digitou", chute_str)

numero = int(chute_str)

if (numero_secreto == numero):
    print("você acertou!")
else:
    print("você errou!")
