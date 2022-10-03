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

def CalculoPorcentagem(qtd):
    """
    Faz o calculo da porcentagem de números que são primos entre si

    Arguments:
        qtd: um numero inteiro

    returns:
        Uma String com o texto do valor em porcentagem da quantidade de números primos entre si dos MIL sorteados
    """
    porcentagemText = f"{qtd /10}%"

    return porcentagemText
        
    

def PROG_03():
    """
    Sorteia MIL vezes dois números aleatórios entre 1 e 100 e verifica se os mesmos são primos entre si.

    Returns:
        A porcentagem de números primos entre si considerando os MIL sorteios de números.
    """
    try:
       
        with open(arquivo, 'a', encoding='utf-8') as f:
            quantidade = 0
            for i in range(1000):
                n1 = randint(1,100)
                n2 = randint(1,100)

                EPrimo = PrimosEntreSi(int(n1), int(n2))

                quantidade += 1 if EPrimo else 0

                resposta = "SIM" if EPrimo else "NÃO"

                f.write(f'{n1},{n2} - {resposta}\n')

            porcentagem = CalculoPorcentagem(int(quantidade))    
    
    except FileNotFoundError:
        print("Arquivo para escrita não encontrado no diretório designado.")
    except TypeError:
        print("O número informado não é inteiro.")
    except ValueError:
        print("Valor informado é inválido")
    
    return porcentagem

PROG_03()