cadastros = []

def get_indice(telefone):
    for idx, item in enumerate(cadastros):
        if item['telefone'] == telefone:
            return idx
    return -1

def cadastrar():
    """Função para cadastrar o nome e telefone do usuário"""
    nome = input("Digite o nome:\n")
    telefone = input("Digite o Telefone:\n")

    if get_indice(telefone) == -1:
        cadastros.append({'nome':nome, 'telefone':telefone})
        print('Usuários cad\astrados com sucesso!\n')
    else:
        print('Telefone já existe!')

def remover():
    telefone = input("Digite o telefone:\n")
    idx = get_indice(telefone)
    if idx != -1:
        cadastros.pop(idx)
        print("Usuário removido com sucesso!")
    else:
        print("Telefone não existe!")

def atualizar():


def listar_cadastro():
    """Função para listar o nome e telefone dos usuários cadastrados"""
    for item in cadastros:
        print('Nome:',item['nome'])
        print('Telefone:',item['telefone'])
        print()

def menu():
    """Função para ler a opção de menu escolhida pelo usuário"""
    print(
        """
        Escolha uma opção
        1 - listar cadastros
        2 - cadastrar
        3 - sair
        """
    )
    return input()

def programa():
    """Função principal do programa"""
    opcao = menu()
    while opcao != 3:
        if opcao == 1:
            listar_cadastro():
        elif opcao == 2:
            cadastrar()
        else:
            print("nenhuma opção válida")
        
        opcao = menu()

