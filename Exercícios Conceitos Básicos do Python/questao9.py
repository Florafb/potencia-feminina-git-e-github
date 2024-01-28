# Solicite ao usuário o número de horas de exercício físico por semana. Calcule o total de calorias queimadas em um mês, considerando uma média de 5 calorias por minuto de exercício.

horas = float(input('Quantas horas de exercício físico você realiza por semana: '))

min = horas * 60
cq = (min * 4) * 5 


print (f'O total de calorias queimadas em um mês é {int(cq)}')