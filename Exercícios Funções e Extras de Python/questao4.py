#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira, calcule quanto poderia comprar de cada moeda estrangeira. Considere a tabela de conversão abaixo:DólarAmericano:R$4,91 PesoArgentino:R$0,02 DólarAustraliano:R$3,18 DólarCanadense:R$3,64 FrancoSuiço:R$0,42 Euro:R$5,36 Libraesterlina:R$6,21 

def conversao_moedas(carteira): 
    da = carteira * 4.91
    pa = carteira * 0.02
    dau = carteira * 3.18
    dc = carteira * 3.64
    fs = carteira * 0.42
    euro = carteira * 5.36
    le = carteira * 6.21
    
    print(f"O que você tem na carteira daria para comprar: Dólar Americano:{da:.2f} | Peso Argentino:{pa:.2f} | Dólar Australiano:{dau:.2f} | Dólar Canadense:{dc:.2f} | Franco Suiço:{fs:.2f} | Euro:{euro:.2f} | Libra esterlina:{le:.2f}")
     
carteira = float(input("Digite quantos reias você tem na sua carteira: "))

conversao_moedas(carteira)
