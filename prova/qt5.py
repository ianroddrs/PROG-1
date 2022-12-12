lista = [4, 40, 50, 68, 28, 75, 73, 17, 55, 17]
mm = max(lista) / min(lista)
# qtd = 0
# for item in lista:
#     if item > mm:
#         qtd += 1
# print(qtd)

from functools import reduce
funcao = lambda qtd, item: qtd +1 if item > mm else qtd

qtd = reduce(funcao, lista, 0)
print(qtd)