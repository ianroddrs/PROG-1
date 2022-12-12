# Conjuntos
cjt = set([3,4,5,5,"Renato",5])
print(cjt)

cjt = set('Renato Hidaka Torres')
print(cjt)

A = set([3,4])
A.add(1)
A.add('Renato')
print(A)
A.remove("Renato")
A.discard(1)
print(A)
A.discard(2)
print(A)
print(A)
A.clear()
print(A)

lista = {1,2,3,4,5}
lista2 = {2,3,4}
print(5 in lista)
print(lista2.issubset(lista))

