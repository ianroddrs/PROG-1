# lista = [
#     {'produto': 'A','quantidade': 10},
#     {'produto': 'B','quantidade': 2},
#     {'produto': 'C','quantidade': 30},
#     {'produto': 'D','quantidade': 17},
# ]
# for idx, item in enumerate(lista.copy()):
#     if item['quantidade'] > 10:
#         lista.remove(item)
#     else:
#         lista[idx] = item['produto']
# print(lista)

lista = [
    {'produto': 'A','quantidade': 10},
    {'produto': 'B','quantidade': 2},
    {'produto': 'C','quantidade': 30},
    {'produto': 'D','quantidade': 17},
]

lista = [item['produto'] for item in lista.copy() if item['quantidade'] <= 10]
print(lista)