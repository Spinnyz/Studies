
pessoa = {
    "nome": "Pedro",
    "sobrenome": "Lucas"
}

dados_pessoa = {
    "idade": 16,
    "altura": 1.75,
}

def mostra_argumentos_nomeados(*args, **kwargs):
    for chave, valor in kwargs.value():
        print(f"{chave} = {valor}")



mostra_argumentos_nomeados(**pessoa, **dados_pessoa)