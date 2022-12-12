lista = [
    {'produto': 'A','quantidade': 10},
    {'produto': 'B','quantidade': 2},
    {'produto': 'C','quantidade': 30},
    {'produto': 'D','quantidade': 17},
]

qtd = 0
for item in lista:
    qtd += item['quantidade']

qtd /= len(lista)
print(qtd)


from functools import reduce
qtd = reduce(lambda qtd, item: qtd + item['quantidade'] , lista, 0) / len(lista)
print(qtd)

lista = [
    {'produto': 'A','quantidade': 10},
    {'produto': 'B','quantidade': 2},
    {'produto': 'C','quantidade': 30},
    {'produto': 'D','quantidade': 17},
]

lista = [item['produto'] for item in lista.copy() if item['quantidade'] <= 10]
print(lista)