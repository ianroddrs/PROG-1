lista = [13, 2, 4, 5, 4, 7, 5]
for idx in range(len(lista)-1):
    if lista[idx] > lista[idx+1]:
        lista[idx], lista[idx+1] = lista[idx+1], lista[idx]
print(lista)

def f():
    