import random

print("Seja bem vindo ao jogo Par ou Impar!")

while True:
    escolha_usuario = input("Escolha par ou impar: ")
    try:
        numero_usuario = int(input("Escolha um numero: "))

        numero_computador = random.randint(1, 10)
        print("numero do computador:", numero_computador)

        soma = numero_usuario + numero_computador
        print("soma:", soma)
        resultado = soma % 2 == 0

        if (escolha_usuario == 'par' and resultado) or (escolha_usuario == 'impar' and not resultado):
            print("Você ganhou!")
        else:
            print("Você perdeu!")

        jogar_novamente = input("Deseja continuar?: ")
        if jogar_novamente != "sim":
            print("obrigada por jogar!")

    except ValueError:
        print("digite apenas numeros. Ex: 1,2,3,4")