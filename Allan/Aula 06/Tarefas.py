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
lista.adicionar_tarefa("Estudar programação")
lista.adicionar_tarefa("Fazer exercícios")
lista.exibir_tarefas()
lista.excluir_tarefa(1)
lista.exibir_tarefas()