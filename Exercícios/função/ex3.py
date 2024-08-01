def soma(numero1,numero2):
    return numero1+numero2

def subtracao(numero1,numero2):
    return numero1-numero2

def multiplicacao(numero1,numero2):
    return numero1*numero2

def divisao(numero1,numero2):
    return numero1/numero2

def solicitar_numero():
    numero = int(input("Digite o numero que deseja para realizar a operação: "))
    return numero


def calculadora():
    print("[1] Adição")
    print("[2] Subtração")
    print("[3] Multiplicação")
    print("[4] divisão")
    print("[0] Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        numero1 = solicitar_numero()
        numero2 = int(input("Digite o segundo numero para somar: "))
        resultado = soma(numero1, numero2)
        print(f"A soma do {numero1} mais o {numero2} é igual a {resultado}.")


    elif escolha == '2':
        numero1 = solicitar_numero()
        numero2 = int(input("Digite o segundo numero para subtrair: "))
        resultado = subtracao(numero1, numero2)
        print(f"A subtração do {numero1} menos o {numero2} é igual a {resultado}")



    elif escolha == '3':
        numero1 = solicitar_numero()
        numero2 = int(input("Digite o segundo numero para realizar a multiplicação: "))
        resultado = multiplicacao(numero1, numero2)
        print(f"A multiplicação do {numero1} vezes o {numero2}é igual a  {resultado}")


    elif escolha == '4':
        numero1 = solicitar_numero()
        numero2 = int(input("Digite o segundo numero para realizar a divisão: "))
        resultado = divisao(numero1, numero2)
        i = 1
        while i <= 10:
            print(f"O{numero1} divido pelo {numero2} e igual a {resultado}")
            i /= 1
            break

    elif escolha == '0':
        print("Saindo do programa.")
        continuar_execucao = False
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

while True:
    if not calculadora():
        print("Saindo do programa.")