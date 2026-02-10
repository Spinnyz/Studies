

produtos = [
    {"nome": "Camiseta", "preco": 29.90},
    {"nome": "Calça", "preco": 99.90},
    {"nome": "Tênis", "preco": 149.90},
]

novos_produtos = [
   {**produto, "preco": produto["preco"] * 1.05} 
   if produto["preco"] > 20 else produto
   for produto in produtos
]
print(novos_produtos)