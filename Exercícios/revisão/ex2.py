while True:
    try:
        nota1 = int(input('Digite a primeira nota: '))
        nota2 = int(input('Digite a segunda nota: '))

        media = (nota1 + nota2) / 2

        if media >= 70:
            print("O aluno está aprovado!")
        else:
            print("O aluno está reprovado!")
            break
        sair = input("Deseja continuar calculando a nota? (sim/nao): ")
        if sair != "sim":
            print("")
            break
    except ValueError:
        print("Digite apenas numeros. Ex:1, 2, 3")
