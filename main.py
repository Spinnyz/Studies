palavra = "python"
letra_acertada = ""

erros = 0
while True:
    letra_digitada = input("Digite uma letra: ").lower()
    
    if len(letra_digitada) != 1:
        print("Digite somente uma letra")
        continue
    else:
        if letra_digitada in palavra:
            print ("correto")
            letra_acertada += letra_digitada
        else:
            print("incorreto")
            erros += 1

    palavra_formada = ""
    for letra_correta in palavra:
        if letra_correta in letra_acertada:
            palavra_formada += letra_correta
        else:
            palavra_formada += "_"

    print (palavra_formada)

    if palavra_formada == palavra:
        print (f"A palavra era {palavra}")
        print (f"Você cometeu {erros} erros.")