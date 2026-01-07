cpf = "57316421096"

# primeiro digito
nove_digitos = cpf[:9]

contador_regressivo = 10
soma = 0
for i in nove_digitos:
    valor = int(i) * contador_regressivo
    soma += valor
    contador_regressivo -= 1

print(soma)

digito_1 =  ((soma * 10) % 11)

if digito_1 > 9:
    print ("O resultado é 0")

else:
    print (i)

