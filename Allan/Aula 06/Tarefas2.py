#Criar uma classe lista de tarefas, que tenha exibir tarefa,criar tarefa e excluir tarefas


class ListaTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)

    def exibir_tarefas(self):
        if len(self.tarefas) == 0:
            print("A lista de tarefas está vazia.")
        else:
            print("Lista de tarefas:")
            for i, tarefa in enumerate(self.tarefas):
                print(f"{i+1}. {tarefa}")

    def excluir_tarefa(self, indice):
        if indice < 1 or indice > len(self.tarefas):
            print("Índice inválido.")
        else:
            del self.tarefas[indice-1]
            print("Tarefa excluída com sucesso.")


lista = ListaTarefas()

def adicionar_tarefa():
    tarefa = input("Digite a nova tarefa: ")
    lista.adicionar_tarefa(tarefa)
    print("Tarefa adicionada com sucesso.")

def excluir_tarefa():
    lista.exibir_tarefas()
    indice = int(input("Digite o número da tarefa que deseja excluir: "))
    lista.excluir_tarefa(indice)
    print("Tarefa excluída com sucesso.")

def menu():
    print("--- Lista de Tarefas ---")
    print("1. Adicionar Tarefa")
    print("2. Exibir Tarefas")
    print("3. Excluir Tarefa")
    print("4. Sair")

    opcao = int(input("Digite uma opção: "))

    if opcao == 1:
        adicionar_tarefa()
    elif opcao == 2:
        lista.exibir_tarefas()
    elif opcao == 3:
        excluir_tarefa()
    elif opcao == 4:
        return
    else:
        print("Ops!!Opção inválida. Tente novamente.")

    print()
    menu()

menu()