def conversor_temperatura(celsius):
    # Converter Celsius para Fahrenheit
    fahrenheit = (celsius * 9/5) + 32
    # Converter Celsius para Kelvin
    kelvin = celsius + 273.15
    return fahrenheit, kelvin

# Solicitar ao usuário uma temperatura em Celsius
celsius = float(input("Digite a temperatura em graus Celsius: "))

# Chamar a função e obter as conversões
fahrenheit, kelvin = conversor_temperatura(celsius)

# Exibir os resultados
print(f"A temperatura de {celsius}°C em Fahrenheit é {fahrenheit}°F")
print(f"A temperatura de {celsius}°C em Kelvin é {kelvin}K")