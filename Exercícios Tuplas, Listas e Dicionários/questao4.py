# Crie um dicionário representando contatos (nome, telefone). Permita ao usuário procurar por um contato pelo nome.

contatos = {
'Aline' : '9899-01012',
'Bech' : '9856-01087',
'Kat' : '9722-34500',
'Leon' : '9756-22333',
'Will' : '9899-71255'
}

def procurar_contato(nome):
    if nome in contatos:
        return f"Nome: {nome} - telefone: {contatos[nome]}"
    else:
        return f"Contato não encontrado {nome}"

nome_pesquisa = input("Digite o contato que se deseja localizar: ")
 
resultado = procurar_contato(nome_pesquisa)
print(resultado)

