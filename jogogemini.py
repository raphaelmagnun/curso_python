import os
import random
import time

# 1. Banco de dados do jogo isolado em uma constante
PALAVRAS = [
    "minhoca", "abacaxi", "computador", "python", "chocolate", 
    "girafa", "astronauta", "biblioteca", "cachorro", "dinossauro",
    "elefante", "foguete", "guitarra", "helicoptero", "internet",
    "jogador", "kiwi", "limonada", "borboleta", "navio"
]

def limpar_tela():
    # os.system funciona tanto no Windows (cls) quanto no Linux/Mac (clear)
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_introducao():
    print("""
    ===================================
        Bem vindo ao jogo da Forca.
    ===================================
    """)
    time.sleep(1)
    print("Nesse jogo, seu objetivo é descobrir a palavra secreta.")
    time.sleep(2)
    print("Você tem 2 chances para a palavra e 5 chances para letras.\n")
    input("Pressione ENTER para começar...")
    limpar_tela()

def desenhar_painel(espacos, vidas_letra, vidas_palavra, letras_tentadas):
    limpar_tela()
    print("=============================================")
    print(f"Palavra: {' '.join(espacos)}")
    print(f"Letras já tentadas: {', '.join(letras_tentadas)}")
    print(f"Chances (Letra): {vidas_letra} | (Palavra): {vidas_palavra}")
    print("=============================================\n")

def jogar():
    exibir_introducao()
    
    palavra_secreta = random.choice(PALAVRAS)
    espacos = ["_"] * len(palavra_secreta)
    letras_tentadas = []
    
    vidas_letra = 5
    vidas_palavra = 2

    while vidas_letra > 0 and vidas_palavra > 0:
        desenhar_painel(espacos, vidas_letra, vidas_palavra, letras_tentadas)
        
        chute = input("Digite uma letra ou arrisque a palavra: ").strip().lower()

        # Validação básica de entrada vazia
        if not chute:
            continue

        # Modo: Chute de Palavra
        if len(chute) > 1:
            if chute == palavra_secreta:
                print(f"\n🎉 Incrível! Você acertou a palavra secreta: '{palavra_secreta}'!")
                return # Encerra a função e o jogo com vitória
            else:
                print("\n❌ Que pena, você errou a palavra!")
                vidas_palavra -= 1
                time.sleep(2)

        # Modo: Chute de Letra
        else:
            if chute in letras_tentadas:
                print("\n⚠️ Você já tentou essa letra! Tente outra.")
                time.sleep(1.5)
                continue
            
            letras_tentadas.append(chute)

            if chute in palavra_secreta:
                print("\n✅ Acertou a letra!")
                for i, letra in enumerate(palavra_secreta):
                    if letra == chute:
                        espacos[i] = chute
                
                if "_" not in espacos:
                    desenhar_painel(espacos, vidas_letra, vidas_palavra, letras_tentadas)
                    print(f"\n🎉 Parabéns! Você completou a palavra: '{palavra_secreta}'!")
                    return
            else:
                print("\n❌ Essa letra não está na palavra!")
                vidas_letra -= 1
            
            time.sleep(1.5)

    # Se sair do loop sem o 'return', significa que as vidas acabaram
    limpar_tela()
    print("=============================================")
    print("                 GAME OVER                   ")
    print(f"A palavra secreta era: {palavra_secreta}")
    print("=============================================")

# O jogo só roda se este arquivo for executado diretamente
if __name__ == "__main__":
    jogar()