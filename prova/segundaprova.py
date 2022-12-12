'''QT1
lista = list(map(lambda item: list(item), zip(listaA,listaB,listaC)))
print(lista)
'''

'''QT2'''
lista = [
    {"medico":"Amaral", "crm": [{"no":1284, "uf": "PA"},{"no":6662, "uf": "AM"}]},
    {"medico":"Amaral", "crm": [{"no":2277, "uf": "PA"},{"no":9933, "uf": "SP"}]},
    {"medico":"Amaral", "crm": [{"no":4455, "uf": "SP"},{"no":2284, "uf": "RJ"}]}
]
crms = []
check = True

for item in lista:
    for crm in item["crm"]:
        check &= not crm["no"] in crms
        crms.append(crm["no"])
print(check)
print(crms)

from functools import reduce

crms = [crm["no"] for item in item["crm"] for item in lista]
funcao = lambda check, item: check if not crm["no"] in crms else False
check = reduce(funcao, lista, True)
print(check)

'''Q3
from functools import reduce
funcao = lambda check, item: check if {'valor','chave'} == set(item) and len(item) == 2 else False
check = reduce(funcao,lista,True)
print(check)
'''

'''QT4

import random as r

def f(a = r.randrange(1,100),b = r.randrange(1,100),c = 1):
    if a == b:
        return print(a,b,c)
    else:
        a = r.randrange(1,100)
        b = r.randrange(1,100)
        c += 1
    return f(a,b,c)

f()
'''
