#Faça um Programa que peça as quatro notas de 5 alunos, calcule e armazene numa lista a média de cada aluno,imprima o número de alunos com média maior ou igual a 7.0.

cont = 0
aluno = 0
medias = []

while cont <=4:
    nota1 = float(input('Digite a primeira nota do aluno: '))
    nota2 = float(input('Digite a segunda nota do aluno: '))
    nota3 = float(input('Digite a terceira nota do aluno: '))
    nota4 = float(input('Digite a quarta nota do aluno: '))

    media = (nota1 + nota2 + nota3 + nota4)/4

    if media >= 7:
        medias.append(media)
        aluno += 1
    
    cont+=1

print(f'O numero de alunos com media maior ou igual a 7 foi: {aluno}')


