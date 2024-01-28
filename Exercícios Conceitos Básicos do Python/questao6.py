#Escreva um programa que calcule o tempo de uma viagem. Faça um comparativo do mesmo percurso de avião,carro e ônibus. Levando em consideração: ● avião=600km/h ● carro=100km/h ● ônibus=80km/h

tv = int(input('Qual a distância, em quilômetros, da viagem: '))

aviao = tv / 600
carro = tv / 100
onibus = tv / 80

print (f'Sua viagem de avião levaria {aviao} horas')
print (f'Sua viagem de carro levaria {carro} horas')
print (f'Sua viagem de ônibus levaria {onibus} horas')