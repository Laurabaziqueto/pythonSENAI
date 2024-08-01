import datetime

while True:
    try:
        tempo = datetime.datetime.now()
        dia = tempo.day
        mes = tempo.month
        ano = tempo.year
        dia_semana = tempo.strftime("%A")

        if tempo.hour < 12:
            saudacao = "Bom dia!"
        elif 12 <= tempo.hour < 18:
            saudacao = "Boa tarde!"
        else:
            saudacao = "Boa noite!"

        frase = print(f"{saudacao} today is {dia_semana},day {dia},month {mes}, from the year: {ano}.")
        break
    except ValueError:
        print("tente novamente, ocorreu um erro.")




