#Solicite ao usuário o peso em kg e a altura em metros. Calcule e imprima o Índice de Massa Corporal (IMC)usando a fórmula: IMC=peso/(alturaxaltura).

peso = float(input('Qual o seu peso, em kg: '))
altura= float(input('Qual a sua altura, em m: '))

imc = peso / (altura * altura)


print (f'Seu Índice de Massa Corporal é de {imc:.2f}')