cpf = "57316421096"

nove_digitos = cpf[:9]

contador_regressivo = 10
soma = 0

for i in nove_digitos:
    valor = int(i) * contador_regressivo
    soma += valor
    x -= 1
    print (valor, end=" ")