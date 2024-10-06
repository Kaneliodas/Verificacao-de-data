#Programa para verificar se uma data é válida no formato dd/mm/aaaa
dia = int(input("Me diga em que dia você está: "))
mes = int(input("Me diga em que mês você está: "))
ano = int(input("Me diga em que ano você está: "))

# Verifica se o mês é válido
if mes < 1 or mes > 12:
    print("Mês inválido. Não é possível ter um mês maior que 12 ou menor que 1.")
else:
    # Verifica os dias dos meses com 30 dias
    if mes in [4, 6, 9, 11] and dia > 30:
        print("Este mês só tem 30 dias.")
    # Verifica fevereiro
    elif mes == 2:
        # Verifica se o ano é bissexto
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            if dia > 29:
                print("Fevereiro tem no máximo 29 dias em anos bissextos.")
            else:
                print(f"A data é válida: {dia}/{mes}/{ano}")
        else:
            if dia > 28:
                print("Fevereiro tem no máximo 28 dias em ano não bissexto.")
            else:
                print(f"A data é válida: {dia}/{mes}/{ano}")
    # Verifica se o dia é válido para os meses restantes (com 31 dias)
    elif dia < 1 or dia > 31:
        print("Dia inválido.")
    else:
        print(f"A data é válida: {dia}/{mes}/{ano}")
