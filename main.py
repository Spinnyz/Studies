cpf = "57316421096"

nove_digitos = cpf[:9]

contador_regressivo = 10
soma = 0
resultado = 0
for i in nove_digitos:
    valor = int(i) * contador_regressivo
    soma += valor
    contador_regressivo -= 1
    resultado +=valor

print(resultado)

resto =  ((resultado * 10) % 11)

if resto > 9:
    print ("O resultado é 0")

else:
    print (i)

