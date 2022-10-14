from math import *

listaNomes = ['andre', 'jorge', 'nando', 'rafael', 'minica', 'leandro', 'ian', 'denys', 'pedro', 'robson', 'alan', 'allesandro']
listaFloats = [5.5,3.23,5.24,10.0,29.4,74.8,53.99,88.3,93.56,21.32,11.11,19.09,23.45,24.33,9.28,2.6]
listaStr1 = ['a','b','c','d','e','f','g','h','i','j']
listaStr2 = ['1','2','3','4','5','6','7','8','9','10']

#01
def upperTransform(lista):
	for indice, item in enumerate(lista):
		lista[indice] = item.upper()
	return lista

#02
def lenghtElement(lista):
	for indice, item in enumerate(lista):
		lista[indice] = len(item)
	return lista

#03
def roundFloat(lista):
	for indice, item in enumerate(lista):
		dec = str(item).split(".")[1]
		if int(dec) % 2 == 0:
			lista[indice] = floor(item)
		else:
			lista[indice] = ceil(item)
	return lista

#4
def concacStrings(lista1, lista2):
	for indice, item in enumerate(zip(lista1, lista2)):
		lista1[indice] = item[0] + item[1]
	return lista1
