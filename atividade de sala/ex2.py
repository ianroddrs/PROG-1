#atividade 2
lista = ['amarelo','laranja','verde','preto','rosa','lilas','ciano']
palavra = input('digite a substring procurada: ')
    for i in lista:
        if palavra in i:
            print(i)