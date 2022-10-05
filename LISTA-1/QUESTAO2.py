
arquivo = 'D:\Workspace\PROG-1\LISTA-1\dados_DNA.txt'

def funcaoA(cadeia, padrao):
    quantidade = 0
    if padrao in cadeia:
        quantidade += 1
    return quantidade    

def funcaoB(cadeia, padrao):
    if padrao in cadeia:
        return True
    else:
        return False


def funcaoC():
    with open(arquivo, 'r', encoding='utf-8') as f:
        linhas = f.readlines()

    with open(arquivo, 'w', encoding="utf-8") as f:
        f.write(linhas[0][:-1]+',FREQ_ATGCCA,TEM_ ATGCCA\n')
        for cadeia in linhas[1:]:
            freq = funcaoA(cadeia, 'ATCCG')
            tem = funcaoB(cadeia, 'ATCCG')
            f.write(f'{cadeia[:-1]},{freq},{tem}\n')

def funcaoD():
    with open(arquivo,'r',encoding='utf-8') as f:
        linhas = f.readlines()
        qtd = 0
        for linha in linhas[1:]:
            if linha[2] == "False":
                qtd += 1
    return qtd

def funcaoE():
    with open(arquivo,'r',encoding='utf-8') as f:
        linhas = f.readlines()
        maxima = 0
        for linha in linhas[1:]:
            linha = linha.split(',')
            if int(linha[1]) > maxima:
                 maxima = linha[1]
    return maxima

def funcaoF():
    with open(arquivo,'r',encoding='utf-8') as f:
        linhas = f.readlines()
        maxima = funcaoE()
        for linha in linhas[1:]:
            index = list(enumerate(linha))[0][0]
        print(index)

    return maxima

print(funcaoE())