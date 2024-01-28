#Desenvolver um programa que solicite a idade do usuário e identifique se ele é uma criança,um adolescente,adulto ou idoso.

idade = int(input('Digite a sua idade: '))

if idade <=17:
    print('Você é uma criança!')
elif 18 <= idade <= 19: 
    print("Você é um adolescente!")
elif 20 <= idade <= 69: 
    print("Você é um adulto!")
else:
    print('Você é um idoso!')



