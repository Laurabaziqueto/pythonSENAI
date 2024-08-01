while True:
    try:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o sengundo número: "))

        if numero1 > numero2:
            print(f"O {numero1} é maior que {numero2}")
        elif numero2 > numero1:
            print(f"O {numero2} é maior que {numero1}")
        else:
            print("Os números são iguais.")
        break

    except ValueError:
        print("Digite apenas números. Ex:1, 2, 3")

