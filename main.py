lista = []

while True:
    user = input ("[i]inserir [a]apagar [l]listar: ").lower().strip()

    if user == "i":
        valor = input ("Oque deseja inserir: ")
        lista.append(valor)

    elif user == "a":
        remove = input("Oque deseja remover: ")
        if remove in lista:
            print ("Removido")
            lista.remove(remove)
        else:
            print ("Não encontrado")
    
    elif user == "l":
        for indice, item in enumerate(lista):
            print (indice, item)
    else:
        print ("Escolha uma opção valida")