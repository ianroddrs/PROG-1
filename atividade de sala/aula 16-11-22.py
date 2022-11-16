# produtos = ['banana','morango','açai','laranja']
# quantidade = [10,3,4,2]

# print(dict(map(lambda chave, valor: (chave, valor), produtos, quantidade)))

listaA,listaB,listaC,listaD = [12,123,12,1,234],[12,123,12,1,234],[12,123,12,1,234],[12,123,12,1,234]

print(list(map(lambda *arg: sum(arg), listaA,listaB,listaC,listaD)))

print([sum(arg) for arg in zip(listaA,listaB,listaC,listaD)])

lista = [19,6,5,6,-1,-5,7,-8]

print(list(filter(lambda x: x>0, lista)))


lista = ['arara', 'cachorro', 'lol', '12398120391', '21304981212321','a']

print(list(filter(lambda item: item[0].lower() == item[-1].lower(), lista)))