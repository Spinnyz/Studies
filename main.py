import re

cpf = re.sub (
    r"[^0-9]",
    "",
    "74682489070")

# ---------- Primeiro dígito ----------
nove_digitos = cpf[:9]

contador_regressivo = 10
soma = 0

for i in nove_digitos:
    valor = int(i) * contador_regressivo
    soma += valor
    contador_regressivo -= 1

print(soma)

digito_1 = (soma * 10) % 11

if digito_1 > 9:
    digito_1 = 0
else:
    print(digito_1)


# ---------- Segundo dígito ----------
dez_digitos = cpf[:10]
segundo_contador_regressivo = 11
soma = 0

for i in dez_digitos:
    segundo_valor = int(i) * segundo_contador_regressivo
    soma += segundo_valor
    segundo_contador_regressivo -= 1

print(soma)

digito_2 = (soma * 10) % 11

if digito_2 > 9:
    digito_2 = 0
else:
    print(digito_2)


# ---------- Verificação ----------
novo_cpf = f"{nove_digitos}{digito_1}{digito_2}"
print(novo_cpf)

if novo_cpf == cpf:
    print("CPF válido")
else:
    print("CPF inválido")
