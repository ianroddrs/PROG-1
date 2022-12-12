lista = [4, 40, 50, 68, 28, 75, 73, 17, 55, 17]
nova_lista = []
for itens in zip(lista, lista[1:], lista[2:]):
    x = itens[0]
    for item in itens:
        if item < x:
            x = item
    nova_lista.append(x)
print(nova_lista)

listanova = list(map(min,zip(lista, lista[1:], lista[2:])))
print(listanova)
