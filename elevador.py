import subprocess
import time

def chamar_elevador (andar_atual_elevador, andar_atual_usuario):
    if andar_atual_elevador > andar_atual_usuario:
        andares = andar_atual_elevador - andar_atual_usuario
        print(f"Descendo {andares} andares...")
        time.sleep(3) 
        for andar in range(andar_atual_elevador, andar_atual_usuario - 1, -1):
            subprocess.run("cls", shell=True)
            print(f"Andar {andar}")
            time.sleep(1)
        print("Abrindo as portas do elevador...")
        andar_alvo_usuario = int(input("Digite o número do andar que você deseja ir: "))
        ir_para_andar_alvo(andar_atual_usuario, andar_alvo_usuario)
    elif andar_atual_elevador < andar_atual_usuario:
        andares = andar_atual_usuario - andar_atual_elevador
        print(f"Subindo {andares} andares...")
        time.sleep(3) 
        for andar in range(andar_atual_elevador, andar_atual_usuario + 1):
            subprocess.run("cls", shell=True)
            print(f"Andar {andar}")
            time.sleep(1)
        print("Abrindo as portas do elevador...")
        andar_alvo_usuario = int(input("Digite o número do andar que você deseja ir: "))
        ir_para_andar_alvo(andar_atual_usuario, andar_alvo_usuario)
    else:
        print("Abrindo as portas do elevador...")
        andar_alvo_usuario = int(input("Digite o número do andar que você deseja ir: "))
        ir_para_andar_alvo(andar_atual_usuario, andar_alvo_usuario)

def verifica_andar_elevador (andar_atual_elevador, andar_atual_usuario):
    if andar_atual_elevador == andar_atual_usuario:
        print("O elevador já está no seu andar. Abrindo as portas...")
        andar_alvo_usuario = int(input("Digite o número do andar que você deseja ir: "))
        ir_para_andar_alvo(andar_atual_usuario, andar_alvo_usuario)
    else:
        chamar_elevador(andar_atual_elevador, andar_atual_usuario)

def ir_para_andar_alvo (andar_atual_usuario, andar_alvo_usuario):
    if andar_atual_usuario > andar_alvo_usuario:
        andares = andar_atual_usuario - andar_alvo_usuario
        print(f"Descendo {andares} andares...")
        time.sleep(3)
        for andar in range(andar_atual_usuario, andar_alvo_usuario -1, -1):
            subprocess.run("cls", shell=True)
            print (f"Andar {andar}")
            time.sleep(1)
        print("Chegamos ao seu destino. Abrindo portas do elevador...")
    elif andar_atual_usuario < andar_alvo_usuario:
        andares = andar_alvo_usuario - andar_atual_usuario
        print (f"Subindo {andares} andares...")
        time.sleep(1)
        for andar in range(andar_atual_usuario, andar_alvo_usuario + 1):
            subprocess.run("cls", shell=True)
            print (f"Andar {andar}")
            time.sleep(1)
        print ("Chegamos ao seu destino. Abrindo portas do elevador...")
    else:
        print("Você já está no seu destino. Abrindo portas do elevador...")
    andar_atual_usuario = andar_alvo_usuario



# andar_atual_elevador = 1
# andar_atual_usuario = int(input("Digite o número do andar atual para chamar o elevador: "))   #5

# verifica_andar_elevador(andar_atual_elevador, andar_atual_usuario)


# import subprocess
# import time

# # Unificamos a lógica de mover em uma única função genérica
# def mover_elevador(andar_inicial, andar_final):
#     if andar_inicial == andar_final:
#         return # Se já está no andar, não faz nada
        
#     if andar_inicial > andar_final:
#         print(f"Descendo {andar_inicial - andar_final} andares...")
#         time.sleep(2)
#         passo = -1
#         ajuste = -1
#     else:
#         print(f"Subindo {andar_final - andar_inicial} andares...")
#         time.sleep(2)
#         passo = 1
#         ajuste = 1

#     # Um único FOR que serve para subir ou descer!
#     for andar in range(andar_inicial, andar_final + ajuste, passo):
#         subprocess.run("cls", shell=True)
#         print(f"Andar {andar}")
#         time.sleep(1)

# # --- Fluxo Principal do Programa ---
# andar_atual_elevador = 1
# andar_atual_usuario = int(input("Digite o número do seu andar atual para chamar o elevador: "))

# # 1. O elevador vai até o usuário
# if andar_atual_elevador == andar_atual_usuario:
#     print("O elevador já está no seu andar.")
# else:
#     mover_elevador(andar_atual_elevador, andar_atual_usuario)

# print("Abrindo as portas do elevador...")
# andar_atual_elevador = andar_atual_usuario # O elevador agora está com o usuário

# # 2. O usuário escolhe o destino
# andar_alvo_usuario = int(input("Digite o número do andar que você deseja ir: "))

# if andar_atual_usuario == andar_alvo_usuario:
#     print("Você já está no seu destino. Abrindo portas do elevador...")
# else:
#     mover_elevador(andar_atual_usuario, andar_alvo_usuario)
#     andar_atual_elevador = andar_alvo_usuario # Elevador para no destino final

# print("Chegamos ao seu destino. Abrindo portas do elevador...")