frase = "Olha que,  legal"

separador = (frase.split(",")) 

for i, frase in enumerate(separador):
    separador[i] = separador[i].strip()

print(separador)