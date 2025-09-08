lista_de_compras = []

def adicionar_item(item):
    lista_de_compras.append(item)
    print(f"'{item}' adicionado à lista.")

def remover_item(item):
    if item in lista_de_compras:
        lista_de_compras.remove(item)
        print(f"'{item}' removido da lista.")
    else:
        print(f"'{item}' não está na lista.")

while True:
    print("\n--- Menu ---")
    print("1. Adicionar item")
    print("2. Remover item")
    print("3. Ver lista")
    print("4. Sair")
    
    escolha = input("Digite sua opção: ")
    
    if escolha == '1':
        item = input("Qual item você quer adicionar? ")
        adicionar_item(item)
    elif escolha == '2':
        item = input("Qual item você quer remover? ")
        remover_item(item)
    elif escolha == '3':
        print("\nSua lista de compras:", lista_de_compras)
    elif escolha == '4':
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")