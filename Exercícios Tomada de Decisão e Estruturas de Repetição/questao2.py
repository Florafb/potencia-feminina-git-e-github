#Faça um Programa que pergunte em que turno você estuda.Peça para digitar M-matutino ou V-Vespertino ou N-Noturno. Imprima a mensagem "BomDia!","BoaTarde!"ou"BoaNoite!"ou"ValorInválido!", conforme o caso

turno = (input('Digite a letra do turno que você estuda (M-matutino ou V-Vespertino ou N-Noturno): '))

if turno == "M":
    print("Bom dia!")
elif turno == "V":
    print("Boa Tarde!")
elif turno == "N":
    print("Boa Noite!")
else:
    print('Valor Inválido!')