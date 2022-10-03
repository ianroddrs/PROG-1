from math import gcd
from random import randint

arquivo = 'D:\Workspace\PROG-1\LISTA-1\primos_entre_si.txt'


def PrimosEntreSi(n1,n2):
    """
    verifica se dois números são primos entre si.

    Arguments:
        n1: um número inteiro
        n2: um número inteiro

    Returns:
        Um valor booleano que será True caso o maior divisor comum entre os números inteiros for 1 e False caso não.
    """
    mdc = gcd(n1, n2)

    if mdc == 1:
        return True
    else:
        return False


try:
    with open(arquivo, 'a', encoding='utf-8') as f:
        qtd = 0
        for i in range(1000):
            n1 = randint(1,100)
            n2 = randint(1,100)

            resposta = PrimosEntreSi(int(n1), int(n2))

            if resposta: qtd += 1

            porcentagem = qtd/10

            resposta = "SIM" if resposta else "NÃO"

            f.write(f'{n1},{n2},{resposta}\n')

        
        f.write(f'\n{porcentagem}% dos números sorteados são primos entre si.')
        
except FileNotFoundError:
    print("Arquivo para escrita não encontrado no diretório designado.")
except TypeError:
    print("O número informado não é inteiro.")
except ValueError:
    print("Valor informado é inválido")