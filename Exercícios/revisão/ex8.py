while True:
    try:
        renda = int(input("Digite o valor da sua renda anual bruta: $"))

        if renda <= 56072.00:
            print("Você não tem custo")
        elif renda > 56072.01 and renda <= 238532.00:
            desconto1 = (7.50 / 100) * renda
            print(f"Seu custo é de {desconto1}")
        elif renda > 238532.01 and renda <= 522400.00:
            desconto2 = (15 / 100) * renda
            print(f"Seu custo é de {desconto2}")
        elif renda > 522400.01 and renda <= 987600.00:
            desconto3 = (22.50 / 100) * renda
            print(f"Seu custo é de {desconto3}")
        elif renda > 987600.01:
            desconto4 = (27.50 / 100) * renda
            print(f"Seu desconto é de {desconto4}")
        else:
            print("custo ínvalido!")
        break

    except ValueError:
        print(" Digite apenas números.")