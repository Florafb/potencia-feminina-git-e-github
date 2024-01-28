#Crie uma função chamada contar_vogais que recebe uma string como parâmetro. Implemente a lógica para contar o número de vogais na string e retorne o total de vogais. Solicite ao usuário para inserir uma frase e utilize a função para contar as vogais.

def contar_vogais(frase): 
    frase = frase.lower() # para que a comparação não seja sensível a maiuscula/minuscula 
    qt_vogal = 0 
    vogais = 'aeiou' 
    for i in vogais: 
        qt_vogal += frase.count(i) 
   
    
    print(f"A quantidade de vogais na frase inserida é: {qt_vogal} vogais.")
     
frase = (input("Digite uma frase: "))

contar_vogais(frase)