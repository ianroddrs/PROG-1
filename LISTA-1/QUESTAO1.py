


count = 0
file = 'D:\Workspace\PROG-1\LISTA-1\dados_usuario.csv'
columns = [[],[],[],[],[]]
# search = input('pesquisa por nome: ')

with open(file, 'r', encoding='utf-8') as f:
    for linha in f:
        linha = linha[:len(linha) - 1]
        if count != 0:
            linha = linha.split(',')
            columns[0].append(linha[0])
            columns[1].append(linha[1])
            columns[2].append(linha[2])
            columns[3].append(linha[3])
            columns[4].append(linha[4])
        count += 1

for i in range(10):
    print(columns[4][i])
    
# # A
# def SearchName(nome = ''):
#     registers = 0
#     listaNomes = []
#     for itens in columns[3]:
#         if nome.capitalize() in itens:
#             registers += 1
#             listaNomes.append(itens)
#     return registers, listaNomes
# # B
# def SearchYearSex(ano, sexo):
#     registersAno = 0
#     registersSexo = 0
#     for itens in columns[2]:
#         if sexo.upper() in itens:
#             registersSexo += 1
#     for itens in columns[1]:
#         if ano >= itens:
#             registersAno += 1

#     return registersAno, registersSexo
# # C
# def SearchString(arg):
#     listaArgs = []
#     for itens in columns:
#         if arg in itens:
#             listaArgs.append(arg)
#     return listaArgs
# D
# def SearchID(numero):
#     listaIDs = []
#     for indice, itens in enumerate(columns[4]):
#         if itens == numero:
#             listaIDs.append(columns[0][indice])
#     return listaIDs
# E
def InsertOnTable(nome, ano, sexo, numero):
    newID = int(columns[0][-1]) + 1
    with open(file, 'a', encoding='utf-8') as f:
        f.write(f'\n{newID},{ano},{sexo},{nome.capitalize()},{numero}')
    


InsertOnTable('ian','2000','M','92')