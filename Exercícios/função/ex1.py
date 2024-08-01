import datetime

def saudacao(nome):
    hora_atual = datetime.datetime.now().hour

    if hora_atual > 0 and hora_atual <= 5:
        print(f"boa madrugada, {nome}")
    elif hora_atual > 5 and hora_atual <= 12:
        print(f"bom dia, {nome}")
    elif hora_atual > 12 and hora_atual <= 19:
        print(f"boa tarde, {nome}")
    elif hora_atual > 19 and hora_atual <= 21:
        print(f"boa noite, {nome}")
    else:
        print(f"Resposta invalida")

def solicitacao():
    nome= input("Qual o seu nome? ")
    return nome

saudacao(solicitacao())