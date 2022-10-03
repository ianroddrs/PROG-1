from urllib import response


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
            ntem = funcaoD(cadeia.split(",")[2])




funcaoC()
