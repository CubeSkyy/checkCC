#Verificacao do número de cartão de cidadão
#@see https://www.autenticacao.gov.pt/documents/10179/11463/Valida%C3%A7%C3%A3o+de+N%C3%BAmero+de+Documento+do+Cart%C3%A3o+de+Cidad%C3%A3o/0dbc446b-3718-41e5-b982-551a72f8b8a8

def checkCC(cc):
    if len(cc) != 12:
        raise ValueError("O número tem que ter 12 digitos")

    for index, i in enumerate(cc):
        if index == 9 or index == 10:
            if not i.isalnum():
                raise ValueError("O número não está no formato correcto (DDDDDDDD C AAT)")
        else:
            if not i.isdigit():
                raise ValueError("O número não está no formato correcto (DDDDDDDD C AAT)")

    cc = list(cc)
    cc[9] = str(ord(cc[9].capitalize()) - 55) #Conversão de alfabeto
    cc[10] = str(ord(cc[10].capitalize()) - 55)
    cc = list(map(int, cc))

    sum = 0
    for i in range(0,len(cc)):
        if i%2 == 0:
            cc[i] *= 2
            if cc[i] >= 10:
                cc[i] -= 9
        sum += cc[i]

    return sum % 10 == 0

