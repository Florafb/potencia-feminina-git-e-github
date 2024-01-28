#Criar um programa em Python que solicite três números ao usuário, utilize estruturas condicionais para determinar o maior entre eles e apresente o resultado.

numero1 = int(input('Digite seu número 1: '))
numero2 = int(input('Digite seu número 2: '))
numero3 = int(input('Digite seu número 3: '))

if numero1 > numero2 and numero1 > numero3:
    print(f'O maior múmero é: {numero1}') 
elif numero2 > numero1 and numero2 > numero3:
    print(f'O maior múmero é: {numero2}')
else:
    print(f'O maior múmero é: {numero3}')