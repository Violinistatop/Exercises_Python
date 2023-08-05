agenda = {}

def adicionar_contato():
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    email = input("Digite o email do contato: ")
    contato = {"Telefone": telefone, "Email": email}
    agenda[nome] = contato
    print("Contato adicionado com sucesso!")

def visualizar_contato():
    nome = input("Digite o nome do contato: ")
    if nome in agenda:
        contato = agenda[nome]
        print(f"Nome: {nome}")
        print(f"Telefone: {contato['Telefone']}")
        print(f"E-mail: {contato['Email']}")
    else:
        print("Contato não encontrado!")

def atualizar_contato():
    nome = input("Digite o nome do contato que deseja atualizar: ")
    if nome in agenda:
        telefone = input("Digite o novo telefone do contato: ")
        email = input("Digite o novo email do contato: ")
        contato = {"Telefone": telefone, "Email": email}
        agenda[nome] = contato
        print("Contato atualizado com sucesso!")
    else:
        print("Contato não encontrado!")

def excluir_contato():
    nome = input("Digite o nome do contato que deseja excluir: ")
    if nome in agenda:
        del agenda[nome]
        print("Contato removido com sucesso!")
    else:
        print("Contato não encontrado!")

# Exemplo de uso:
while True:
    print("1. Adicionar contato")
    print("2. Visualizar contato")
    print("3. Atualizar contato")
    print("4. Excluir contato")
    print("5. Sair")
    
    opcao = input("Digite o número da opção desejada: ")
    
    if opcao == "1":
        adicionar_contato()
    elif opcao == "2":
        visualizar_contato()
    elif opcao == "3":
        atualizar_contato()
    elif opcao == "4":
        excluir_contato()
    elif opcao == "5":
        break
    else:
        print("Opção inválida. Tente novamente.")
