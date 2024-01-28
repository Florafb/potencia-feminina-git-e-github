#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.Calcule e mostre o total do seu salário no referido mês.

rh = float(input('Quanto você ganha por hora: '))
hm = float(input('Quantas horas você trabalha no mês: '))

sal = rh * hm


print (f'O total do seu salário no referido mês é R$ {sal:.2f}')