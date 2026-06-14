import subprocess
import time

opcoes_validas = [0, 1, 2, 3, 4]

def calcular(opcao, num_1, num_2):
    if opcao == 1:
        return num_1 + num_2
    elif opcao == 2:
        return num_1 - num_2
    elif opcao == 3:
        return num_1 * num_2
    elif opcao == 4:
        if num_2 == 0:
            return "Erro (divisão por zero!)"
        return num_1 / num_2

def limpar_tela():
    subprocess.run('cls', shell=True)

while True:    
    print("""
    ===============================
        BEM-VINDO À CALCULADORA
    ===============================     
          
    Digite 1 para somar.
    Digite 2 para subtrair.
    Digite 3 para multiplicar.
    Digite 4 para dividir.
    
    Digite 0 para sair do programa   
    """)
    
    opcao = int(input("Selecione sua opção: "))

    if opcao not in opcoes_validas:
        print("\n❌ Opção inválida! Por favor, escolha um número de 0 a 4.")
        time.sleep(2) # Reduzido para 2 segundos
        limpar_tela()
        continue

    if opcao == 0:
        print("Calculadora finalizada. \nSaindo do programa...")
        time.sleep(2)
        limpar_tela()
        break
    else:
        num_1 = int(input("Digite o primeiro número: "))
        num_2 = int(input("Digite o segundo número: "))
        
        print(f"\nO resultado é: {calcular(opcao, num_1, num_2)}")
        
        # Trocado o sleep por um input para melhorar a experiência
        input("\nPressione Enter para voltar ao menu...")
        limpar_tela()