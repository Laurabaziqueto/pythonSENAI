def verificar_triangulo():
    lado1 = float(input('Primeiro lado: '))
    lado2 = float(input('Segundo  lado: '))
    lado3 = float(input('Terceiro lado: '))

    # Testando se é triângulo
    if (lado1 + lado2 < lado3) or (lado1 + lado3 < lado2) or (lado2 + lado3 < lado1) or (lado2 + lado3 < lado1):
        print('Não é um triangulo')
    elif (lado1 == lado2) and (lado1 == lado3):
        print('Equilatero')
    elif (lado1 == lado2) or (lado1 == lado3) or (lado2 == lado3):
        print('Isósceles')
    else:
        print('Escaleno')


verificar_triangulo()