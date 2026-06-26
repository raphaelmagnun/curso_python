
import subprocess

lista = []

def salvar_lista():
    with open ('lista_compras.txt', 'w', encoding='utf-8') as arquivo:
        for item in lista:
            arquivo.write(f'{item}\n')

def carregar_lista():
    try:
        with open('lista_compras.txt', 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                lista.append(linha.strip()) # O .strip() remove a quebra de linha (\n)
    except FileNotFoundError:
        # Se o arquivo não existir (primeira vez que roda), não faz nada
        pass

def limpar_tela():
    subprocess.run('cls', shell=True)

def cabecalho_sistema():
    print("""
    Bem vindo a sua lista de compras!
    Opções do sistem:
    -----------------------------------------------------
    [1]: Mostrar lista de compras
    [2]: Incluir novo item
    [3]: Excluir item da lista
    [4]: Sair
    -----------------------------------------------------
    """
    )

def incluir_item(item):
    lista.append(item)
    salvar_lista()
    return f"O item {item} foi adicionado!"

def excluir_item(indice):
    indice_real = indice - 1
    if 0 <= indice_real < len(lista):
        item = lista.pop(indice_real)
        salvar_lista()
        return f'O item {item} foi excluído com sucesso!'
    else:
        return f'o número {indice} não existe na lista!'    

def mostrar_lista():
    print ("Sua lista atual: ")
    if not lista :
        print("Sua lista atual se encontra vazia")
    else:
        for indice, nome in enumerate(lista, start=1):
            print(indice, nome)

carregar_lista()

while True:
    cabecalho_sistema()
    
    # Proteção para o menu principal
    try:
        opcao_usuario = int(input('Escolha uma opção: '))
    except ValueError:
        print("Opção inválida! Digite um número.")
        input("Pressione ENTER para continuar...")
        limpar_tela()
        continue

    if opcao_usuario == 1:
        mostrar_lista()
        input("\nPressione ENTER para voltar ao menu...") # Pausa para o usuário ler
    elif opcao_usuario == 2:
        novo_item = input("Digite o nome do novo item: ")
        print(incluir_item(novo_item))
        input("Pressione ENTER para continuar...")
    elif opcao_usuario == 3:
        mostrar_lista()
        try:
            numero_do_item = int(input("Digite o numero do item que deseja excluir: "))
            print(excluir_item(numero_do_item))
        except ValueError:
            print("Erro: Digite um número válido!")
        input("\nPressione ENTER para voltar ao menu...")
    elif opcao_usuario == 4:
        break        
    limpar_tela()

print('O sistema foi finalizado')
