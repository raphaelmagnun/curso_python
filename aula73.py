import time
import subprocess
import random

def limpar_tela():
    subprocess.run('cls', shell=True)

print ("""
       ===================================
            Bem vindo ao jogo da Forca.
       ===================================
       """)
time.sleep(1)
print ("Nesse jogo, seu objetivo é descobrir a palavra secreta.")
time.sleep(3)
print ("Você tem 2 chances de chutar a palavra secreta. E 5 chances de chutar uma letra.")
time.sleep(3)
print ("Vamos começar?")
time.sleep(3)
limpar_tela()

print ("""
       ===================================
            Bem vindo ao jogo da Forca.
       ===================================
       """)


lista_de_palavras = [
    "minhoca", "abacaxi", "computador", "python", "chocolate", 
    "girafa", "astronauta", "biblioteca", "cachorro", "dinossauro",
    "elefante", "foguete", "guitarra", "helicoptero", "internet",
    "jogador", "kiwi", "limonada", "borboleta", "navio",
    "orquestra", "passaporte", "queijo", "relogio", "sapato",
    "televisao", "universo", "vassoura", "xadrez", "zoologico",
    "aventura", "biscoito", "cadeira", "deserto", "escola",
    "floresta", "geladeira", "hospital", "ilha", "janela",
    "lampada", "mochila", "natureza", "oceano", "panela",
    "quintal", "revista", "sorvete", "travesseiro", "vampiro"
]

palavra_secreta = random.choice(lista_de_palavras)
qtd_chute_letra = 5
qtd_chute_palavra = 2
chute = ''

print ("Palavra secreta: ")
espacos = ["_"] * len(palavra_secreta)
print(' '.join(espacos))

while qtd_chute_palavra > 0 and qtd_chute_letra > 0:
    print(f'''
    =============================================
    Quantidade de letras: {len(palavra_secreta)}
    Chances para chutar letra: {qtd_chute_letra}
    Chances para chutar palavra: {qtd_chute_palavra}
    =============================================
      ''')
    
    chute = input("Digite uma letra ou arrisque a palavra: ").lower()

    if len(chute) > 1:
        if palavra_secreta == chute:
            print ("Parabéns, você descobriu a palavra.")
            print(f"A palavra é {palavra_secreta}")
            break
        else:
            print ("Que pena, você errou a palavra!")
            qtd_chute_palavra -= 1
            continue
    else:  
        acertou_alguma = False
        for i, letra in enumerate(palavra_secreta):
            if letra == chute:
                espacos[i] = chute
                acertou_alguma = True    
        if acertou_alguma:
            print(' '.join(espacos))
            print("Acertou! \n")
            
            if "_" not in espacos:
                print("Parabéns! Você descobriu todas as letras e completou a palavra!")
                break
        else:
            print("Que pena, você errou! \n")
            qtd_chute_letra -= 1

print("GAME OVER")


