while True:
    try:
        numero1 = int(input("Digite o primeiro número inteiros: "))
        numero2 = int(input("Digite o segundo número inteiros:"))
        numero3 = int(input("Digite o terceiro número inteiros: "))

        if numero1 > numero2 and numero1 > numero3:
            print(f"O {numero1} é o maior entre os 3.")
        elif numero2 > numero1 and numero2 > numero3:
            print(f" {numero2} O maior entre os 3.")
        elif numero3 > numero1 and numero3 > numero2:
            print(f" {numero3} O maior entre os 3.")
        else:
            print("Os três números são iguais.")
        break
    except ValueError:
        print("Apenas números inteiros!")