lista = [
    {'produto': 'A','quantidade': 10},
    {'produto': 'B','quantidade': 2},
    {'produto': 'C','quantidade': 30},
    {'produto': 'D','quantidade': 17},
]

lista = list(map(lambda item: item['produto'],filter(lambda item: item['produto'] if item['quantidade'] <= 10 else None ,lista)))
print(lista)