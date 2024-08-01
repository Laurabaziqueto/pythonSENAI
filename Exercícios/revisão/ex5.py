while True:
    try:
        numero = int(input("Digite um número de 1 a 7 para saber o dia da semana: "))

        if numero == 1:
            print("Domingo-feira")
        elif numero == 2:
            print("Segunda-feira")
        elif numero == 3:
            print("Terça-feira")
        elif numero == 4:
            print("Quarta-feira")
        elif numero == 5:
            print("Quinta-feira")
        elif numero == 6:
            print("Sexta-feira")
        else:
            print("Esse dia da semana não existe.")
        break

    except ValueError:
        print("Digite apenas números!")
