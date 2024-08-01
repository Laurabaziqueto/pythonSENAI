while True:
    try:
        ano_de_nascimnto = int(input('Digite o ano de nascimnto: '))
        idade = 2024 - ano_de_nascimnto

        if idade >= 18:
            print("O usuário é maior de idade")
        else:
            print("O usuário é menor de idade")

        sair = input("Deseja continuar no sistema? (sim/nao): ")
        if sair != "sim":
            print("")
            break

    except ValueError:
        print("Digite um ano válido apenas com números!")