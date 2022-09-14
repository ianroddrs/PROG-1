'''
OPERADORES - LISTA

atribuição composta
a = 1
a += 2
a |= b
b &= a or c

'''

'''
resposta operadores

1 = D
2 = C
3 = A
4 = D
5 = B

6 = {
  A = 1
  B = 2
  A, B = B, A
}
7 = {
  Maior = (A + B + abs(A - B)) / 2
}

8 = {
  1 - Inteiro
  2 - String
  3 - Inteiro
  4 - Lista (objeto)
  5 - boolean
} 

9 = {
  nome, sobrenome = 'Renato', 'Hidaka'
}

10 = {
  X = 10
  Y = 5
  X = X ** Y % 3
  
  *** NÃO É POSSÍVEL UTILIZAR ATRIBUIÇÃO COMPOSTA POIS IRÁ MUDAR A ORDEM DE PRECEDÊNCIA DAS OPERAÇÕES
}

'''


'''
 ENTRADA E SAÍDA - LISTA
 
1 = C
2 = A
3 = A

4 = {
  
}

5 = {
  '''
          *
         ***
        *****
       *******
  '''
}

7 = {
  arquivo = 'C:\\Users\\KURUMI.LAB4-PC05\\Downloads\\capitulos\\Operadores.html'
  
  with open(arquivo, 'r', encoding='utf-8') as f:
      contador = 0
      for linhas in f:
          if '</html>' in linhas:
              contador += 1
      print(contador)
}

8 = {
  i = 0
  while i <= 10:
  #   N = int(input('Digite a quantidade: '))
      N = 10
      P = input('Digite a Palavra: ')

  #   texto = (P+" ")*(N-1)+P
      texto = (P+' ')*N
      texto = texto.strip()


      with open("texto_Q8.txt", 'a', encoding='utf-8') as f:
          f.write(texto + '\n')

      i += 1
}

10 = {
  a = int((input('Valor a :')))
  b = int((input('Valor b :')))
  c = int((input('Valor c :')))

  if a > b > c:
      x, y = a, b
  elif a > c > b:
      x, y = a, c
  elif c > a > b:
      x, y = c, a
  elif b > c > a:
      x, y = b, c
  else:
      x, y = c, b

  soma = str('%.2f' % (x+y))
  sub = str('%.2f' % (x-y))
  mult = str('%.2f' % (x*y))
  div = str('%.2f' % (x/y))

  x = str(x)
  y = str(y)

  with open('operacoes.txt', 'w', encoding='utf-8') as f:
      f.write(x + ' + ' + y + ' = ' + soma + '\n')
      f.write(x + ' - ' + y + ' = ' + sub + '\n')
      f.write(x + ' * ' + y + ' = ' + mult + '\n')
      f.write(x + ' / ' + y + ' = ' + div + '\n')

}
'''
  
'''
FUNCOES

1)
  V
  F
  V
  V
  ANULADA
  F
  V
  V

2)
  V
  V
  F
  F
  V
  F
  F
  F
  
3)
  V
  F
  V
  V
  V
  
4)

  
  
  
  
  
  
  
  
  
  def f(N, X= 3)
      pass
      
  f(5, n = 2)
  
'''
