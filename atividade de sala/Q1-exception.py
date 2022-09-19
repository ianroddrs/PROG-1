"""
Q1
escreva um programa para ler o arquivo 'controle de fluxo.html'
informe quantas linhas tem a palavra 'fluxo' ou a palavra 'python' 
indenpedentemente de grafia. o seu programa deve tratar o erro de arquivo
inválido.
"""

"""
Q2
escreva um programa para ler o nome e o telefone de um usuário. O telefone deve conter
exatamente 9 dífgitos, caso contrário, o seu programa deve tratar essa exceção.
Caso não tenha nenhum erro, salve as informações do usuário em um arquivo chamado "contatos",
o nome e o telefone devem estar esparar por virgula.
"""

arquivo = 'Controle+de+fluxo.html'
qtd = 0

try:
	with open(arquivo, 'r', encoding='utf-8') as f:
		for linha in f:
			if 'fluxo' in linha.lower() or 'python' in linha.lower():
				qtd += 1
		print(qtd)
except FileNotFoundError:
	print('arquivo inválido')
			