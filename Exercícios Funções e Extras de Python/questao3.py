#Escreva um script que pergunta ao usuário se ele deseja converter uma temperatura de grau Celsius para Fahrenheit ou vice-versa. Para cada opção, crie uma função. Plus: Crie uma terceira, que é um menu para o usuário escolher a opção desejada, onde esse menu chama a função de conversão correta.

#multiplicar a temperatura ºC por 1,8 e somar 32.
def conversao_cf(grau): 
    cf = (grau * 1.8) + 32.0
    print(f"A temperatura de Celsius para Fahrenheit: {cf}°F")
  
#Subtraímos a temperatura de ºF por 32 e dividimos o resultado por 1,8.
def conversao_fc(grau): 
    fc = (grau - 32.0) / 1.8
    print(f"A temperatura de Fahrenheit para Celsius: {fc}°C")

def menu(opcao):
    #opcao = input("O que você deseja converter: Digite A (°C -> °F ) ou Digite B (°F -> °C)")
    if opcao == "A":
       conversao_cf(grau)
    else:
        conversao_fc(grau)
    
    
   
grau = float(input("Digite um número inteiro: "))
opcao = input("O que você deseja converter? Digite A (°C -> °F ) ou Digite B (°F -> °C): ")

menu(opcao)

