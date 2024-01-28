#Faça um programa que lê três números inteiros e os mostra em ordem crescente.

numero1 = int(input('Digite um número 1 inteiro: '))
numero2 = int(input('Digite um  número 2 inteiro: '))
numero3 = int(input('Digite um número 3 inteiro: '))

if numero1 > numero2 and numero1 > numero3 and numero2 > numero3:
    print(f'{numero1} > {numero2} > {numero3}')
elif numero1 > numero2 and numero1 > numero3 and numero3 > numero2:
    print(f'{numero1} > {numero3} > {numero2}')
elif numero2 > numero1 and numero2 > numero3 and numero1 > numero3:
    print(f'{numero2} > {numero1} > {numero3}')
elif numero2 > numero1 and numero2 > numero3 and numero3 > numero1:
    print(f'{numero2} > {numero3} > {numero1}')
elif numero3 > numero1 and numero3 > numero2 and numero1 > numero2:
    print(f'{numero3} > {numero1} > {numero2}')
elif numero3 > numero1 and numero3 > numero2 and numero2 > numero1:
    print(f'{numero3} > {numero2} > {numero1}')

else:
    print(f'{numero1} = {numero2} = {numero3}')


    