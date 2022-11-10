from CadastraTelefone.functions import *
from flet import *

def programa():
    """Função principal do programa"""
    opcao = menu()
    while opcao != '5':
        if opcao == '1':
            listar_cadastro()
        elif opcao == '2':
            cadastrar()
        elif opcao == '3':
            atualizar()
        elif opcao == '4':
            remover()
        else:
            print("nenhuma opção válida")
        
        opcao = menu()

programa()