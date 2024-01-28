#Crie um dicionário representando um carrinho de compras. Adicione produtos(chaves)e quantidades(valores)ao carrinho. Calcule o total do carrinho de compra.

cont = 0
item = 0
carro = {}
total = 0

while cont <=2:
    produto = (input('Adicione um produto: '))
    valor = float(input('Adicione o valor: '))

    carro[produto] = valor

    cont+=1

    total += valor

print(carro)
print(f'O valor total das compras foi de R$: {total}')
    