listaNomes = ['andre', 'jorge', 'nando', 'rafael', 'minica', 'leandro', 'ian', 'denys', 'pedro', 'robson', 'alan', 'allesandro']

def upperTransform(lista):
	for indice, i in enumerate(lista):
		lista[indice] = i.upper()
	return lista

upperTransform(listaNomes)

def lenghtElement(lista):
	for indice, i in enumerate(lista):
		lista[indice] = len(i)
	return lista

print(lenghtElement(listaNomes))