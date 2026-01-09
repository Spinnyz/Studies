perguntas = [{
    "pergunta": "Quanto é 2+2?",
    "opcoes": ["1", "3", "4", "5"],
    "resposta": "4"
},
{
  "pergunta": "Quanto é 5*6?",
  "opcoes": ["11", "30", "56", "60"],
  "resposta": "30"
},
{
  "pergunta": "Quanto é 10/2?",
  "opcoes": ["2", "5", "10", "20"],
  "resposta": "5"  
}
]

for pergunta in perguntas:
    print("Pergunta:", pergunta["pergunta"])
    print()


    for i, opcao in enumerate(pergunta["opcoes"]):
        print(f"{i}) {opcao}")
        print()