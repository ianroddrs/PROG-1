'''
#atividade 1

lista = range(2, 1 + int(input("Verificar números primos até: ")))

for i in lista:
    for j in range(2,i): 
        if(i % j==0): 
            break
    else: 
        print(i)
'''
'''
#atividade 2

lista = ['amarelo','laranja','verde','preto','rosa','lilas','ciano']

palavra = input('digite a substring procurada: ')
    for i in lista:
        if palavra in i:
            print(i)
'''    

#atividade 3

lista = ['amarelo','laranja','verde','preto','rosa','lilas','ciano']

arquivo = 'arquivo.txt'

with open(arquivo, 'r', encoding='utf-8') as f:
    for palavra in lista:
        contador = 0
        for linhas in f:
            if palavra in linhas:
                contador += 1
        print(palavra, "=", contador)