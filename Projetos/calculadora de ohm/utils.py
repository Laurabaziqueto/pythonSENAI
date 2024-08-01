
def calculadora():
    print("Digite o número que deseja calcular: ")
    print("0 = Sair")
    print("1 = Tensão elétrica")
    print("2 = resistência elétrica")
    print("3 = corrente de elétrica")
    print("4 = resistência resistor")

def calculo():
    while True:
        try:
            calculo = int(input("Digite qual calculo deseja calcular: "))
            return calculo
        except ValueError:
            print("Digite apenas números")

def tensao():
    resistencia = float(input("Digite o valor da resisência elétrica em volts: "))
    corrente = float(input("Digite o valor da corrente elétrica em ampere: "))
    tensao = resistencia * corrente
    return tensao

def resistencia():
    tensao =float(input("Digite o valor da tensão elétrica em volts: "))
    corrente = float(input("Digite o valor da corrente elétrica em ampere: "))
    resistencia = tensao * corrente
    return resistencia

def corrente():
    tensao = float(input("Digite o valor da tensão elétrica em volts: "))
    resistencia = float(input("Digite o valor da resistência em Ω (ohm): "))
    corrente = tensao / resistencia
    return corrente

def resistencia_resistor():
    tensao_fonte = float(input("Digite a tensão em volts: "))
    tensao_led = float(input("Digite a tensão do led em volts: "))
    corrente_led = float(input("Digite a corrente do led em ampere: "))
    resistencia_resistor = (tensao_fonte - tensao_led) / corrente_led
    return resistencia_resistor

def exibir_calculo(calculo):
    if calculo == 0:
        print("saindo do programa")
    elif calculo == 1:
        print(f"A tensão elétrica em volts é {tensao()}")
    elif calculo == 2:
        print(f"A resistência elétrica em  Ω (ohm) é {resistencia()}")
    elif calculo == 3:
        print(f"A corrente elétrica em ampere é {corrente()}")
    elif calculo == 4:
        print(f"A resistência do resistor em Ω (ohm) é {resistencia_resistor()}")
    else:
        print("Digite um valor valido")

