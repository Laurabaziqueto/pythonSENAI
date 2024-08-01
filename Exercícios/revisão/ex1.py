while True:
    try:
        numero = float(input("Digite um numero: "))
        if numero > 0:
            print("Numero positivo")
        elif numero < 0:
            print("Numero negativo")
        else:
            print("O número é zero")
        break
    except ValueError:
        print(" digite apenas numeros. Ex: 1,-1")
