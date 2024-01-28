#Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127->721


def inverso(num): 
    inv = int(num[::-1])
    print(f'O número inverso: {num} -> {inv}')

   
num = input("Digite um número inteiro: ")

inverso(num)


