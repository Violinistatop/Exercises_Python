contatos = {}

def adicionar_contato():
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    email = input("Digite o email do contato: ")
    contatos[nome] = {"telefone": telefone, "email": email}
    print("Contato adicionado com sucesso!\n")

def visualizar_contatos():
    if contatos:
        for nome, valor in contatos.items():
            print("Nome:", nome)
            print("Telefone:", valor["telefone"])
            print("Email:", valor["email"])
            print("------------------------")
    else:
        print("Nenhum contato encontrado.")

def atualizar_contato():
    nome = input("Digite o nome do contato que deseja atualizar: ")
    if nome in contatos:
        telefone = input("Digite o novo telefone: ")
        email = input("Digite o novo email: ")
        contatos[nome]["telefone"] = telefone
        contatos[nome]["email"] = email
        print("Contato atualizado com sucesso!")
    else:
        print("Contato não encontrado.")
        print("Responda S para 'Sim' e N para 'Não ")
        pergunta_incluir = input("Deseja incluir novo contato?")
        if pergunta_incluir == "S":
            adicionar_contato()
        else:
            menu(5)
        

def excluir_contato():
    nome = input("Digite o nome do contato que deseja excluir: ")
    if nome in contatos:
        del contatos[nome]
        print("Contato excluído com sucesso!")
    else:
        print("Contato não encontrado.")

def menu():
    opcao = 0
    while opcao != 5:
        print("---- Gerenciador de Contatos ----")
        print("1 - Adicionar Contato")
        print("2 - Visualizar Contatos")
        print("3 - Atualizar Contato")
        print("4 - Excluir Contato")
        print("5 - Sair")
        opcao = int(input("Digite a opção desejada: "))

        if opcao == 1:
            adicionar_contato()
        elif opcao == 2:
            visualizar_contatos()
        elif opcao == 3:
            atualizar_contato()
        elif opcao == 4:
            excluir_contato()
        elif opcao == 5:
            print("Saindo...")
        else:
            print("Opção inválida. Tente novamente.")

menu()
