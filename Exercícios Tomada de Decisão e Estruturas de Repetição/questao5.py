#Desenvolva um programa que solicite ao usuário os comprimentos dos três lados de um triângulo e classifique-o como equilátero, isósceles ou escaleno. Equilátero:todos os lados com o mesmo valor isósceles: dois lados com o mesmo valor escaleno:todos os lados com medidas distintas.

lado1 = int(input('Digite o lado 1 do triângulo: '))
lado2 = int(input('Digite o lado 2 do triângulo: '))
lado3 = int(input('Digite o lado 3 do triângulo: '))

if lado1 == lado2 and lado2 == lado3 and lado1 == lado3:
    print("É um triângulo equilátero.")
elif lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
    print("É um triângulo escaleno.")
else:
    print("É um triângulo isósceles.")