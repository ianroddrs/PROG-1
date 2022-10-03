arquivo = 'D:\Workspace\PROG-1\LISTA-1\dados_DNA.txt'

# def fuction(cadeia, padrao,q):
    


with open(arquivo, 'r', encoding='utf-8') as f:
    qtd = 0
    padrao = "AAAAAAAAA"
    for cadeia in f:
        if padrao in cadeia:
            qtd += 1
            print(qtd)

        