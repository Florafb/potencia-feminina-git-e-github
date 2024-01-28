#O programa deve calcular e apresentar a quantidade de números pares e ímpares inseridos.O processo de leitura deve ser encerrado quando o usuário informar o valor zero.Certifique-se de incluir validações para garantir que apenas números positivos sejam considerados na contagem e cálculos.


p = 0 
i = 0 
while True: 
    n = int(input("Digite um número (para finalizar, digite 0): "))

    if n == 0:
        break

    if n > 0:    
        if n % 2 == 0:   
            p = p + 1 
        else: 
            i = i + 1  

    else:
        print ("Digite um número positivo!")
    
print(f"Quantidade de números pares: {p} | Quantidade de números ímpares: {i}")