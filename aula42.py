frase = 'O Python é uma linguagem de programação '\
    'multiplataforma. '\
    'Python foi criado por Guido van Rossum.'

i = 0

apareceu_mais_vezes = 0
letra_que_apareceu_mais_vezes = ''

apareceu_menos_vezes = 0
letra_que_apareceu_menos_vezes = ''

while i < len(frase):

    if frase[i] == ' ':
        i += 1
        continue

    letra_atual = frase[i]
    quantas_vezes_letra_apareceu = frase.count(letra_atual)

    if quantas_vezes_letra_apareceu > apareceu_mais_vezes:
        apareceu_mais_vezes = quantas_vezes_letra_apareceu
        letra_que_apareceu_mais_vezes = frase[i]

    i += 1

print (f"A letra que aparece mais vezes é a letra ({letra_que_apareceu_mais_vezes}")
print (f"A letra ({letra_que_apareceu_mais_vezes}) apareceu {apareceu_mais_vezes} vezes.")