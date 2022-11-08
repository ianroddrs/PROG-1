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
    telefone = input('Digite o telefone:\n')
    idx = get_indice(telefone)
    if idx != -1:
        nome = input('Digite o nome:\n')
        telefone = input('Digite o telefone:\n')
        idx_confirmacao = get_indice(telefone)
        if idx_confirmacao == -1 or idx_confirmacao == idx:
            cadastros[idx] = {'nome':nome, 'telefone':telefone}
    else:
        print('Telefone não existe!')

def listar_cadastro():
    """Função para listar o nome e telefone dos usuários cadastrados"""
    if len(cadastros) == 0:
        print('Nenhum cadastro listado.')
    else:
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
2 - novo cadastro
3 - atualizar cadastro
4 - remover cadastro
5 - sair
"""
    )
    return input()