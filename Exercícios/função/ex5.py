try:
  def peso ():
    peso = float(input("Digite o peso (em kg): "))
    altura = float(input("Digite a altura (em metros): "))
    imc = peso / (altura ** 2)
    print("Seu imc é:", imc)

    if imc < 18.5:
      print("Você está abaixo do peso.")
    elif 18.5 <= imc <25:
      print("seu peso está adequado.")
    elif 25 <= imc <30:
      print("você está com sobrepeso.")
    else:
      print("você está obeso")

  #Repetição do comando
  peso ()

except ValueError:
  print("digite apenas numeros para realizar a operação")