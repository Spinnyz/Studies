class Node:
    def __init__(self, valor):
        self.valor = valor
        self.esq = None
        self.dir = None


def inverter_arvore(no):
    if no is None:
        return None

    # troca os filhos
    no.esq, no.dir = no.dir, no.esq

    # inverte recursivamente
    inverter_arvore(no.esq)
    inverter_arvore(no.dir)

    return no


print (inverter_arvore(raiz))
