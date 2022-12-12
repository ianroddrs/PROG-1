import random as r
saida = True
while type(saida) is bool:
    lista = []
    for item in range(5):
        lista.append(r.randrange(1,20))
    check = True
    for x, y in zip(lista[1:], lista):
        check &= x > y
    saida = lista if check else check
print(saida)

def f(saida=True):
    if type(saida) is not bool:
        return saida
    lista = []
    for item in range(5):
        lista.append(r.randrange(1,20))
    check = True
    for x, y in zip(lista[1:], lista):
        check &= x > y
    saida = lista if check else check
    return f(saida)

print(f())