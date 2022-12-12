lista = [4, 40, 50, 68, 28, 75, 73, 17, 55, 17]
nova_lista = []
for a, b in zip(lista, lista[1:]):
    m = 1
    for q in range(2, max(a,b)):
        if a%q == b%q == 0:
            m = q
            break
    if m == 1:
        nova_lista.append(a)
print(nova_lista)


def filtro(a,b, m=1):
    for q in range(2, max(a,b)):
        if a%q == b%q == 0:
            m = q
            break
    return True if m == 1 else False
    

lista = [a for a, b in zip(lista, lista[1:]) if filtro(a,b)]
print(lista)