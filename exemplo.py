# o While repete tudo que está dentro dele
while True:
    # O try vai tentar executar esse bloco de codigo
    try:
        idade = int(input('Digite sua idade: '))

        # O if verifica se a idade é valida
        if idade > 0 and idade <= 100:
            print("idade:", idade)
            # O break sai do while
            break
        else:
            print("Idade invalida")

    # Caso der erro executa aqui
    except ValueError:
        print("Digite sua idade em numero. Ex: 16")
