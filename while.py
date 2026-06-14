nome = 'Raphael Magnun Urbano'

contador = 0
nome_com_asterisco = ''

while contador < len(nome):
    nome_com_asterisco += nome[contador] + '*'
    contador += 1

print(nome_com_asterisco)