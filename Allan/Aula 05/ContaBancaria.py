#Exercício 3:Crie uma classe chamada `ContaBancaria` que tenha os atributos `titular` e `saldo`. Crie métodos para depositar e sacar dinheiro da conta, e um método para imprimir o saldo.

class Contabancaria:
    def __init__ (contaBancaria,titular,saldo=0):
        contaBancaria.titular = titular
        contaBancaria.saldo = saldo

    def depositar(contaBancaria):
        valor = int(input("Digite um valor a depositar: "))
        contaBancaria.saldo += valor  #saldo = saldo + valor

    def sacar(contaBancaria):
        valor = int(input("Digite o valor a sacar: "))
        if valor <= contaBancaria.saldo:
            contaBancaria.saldo -= valor
        else:
            print("Saldo Insuficiente")
        
    
    def imprimir_saldo(contaBancaria):
        print("Nome: ",contaBancaria.titular)
        print("Saldo: ",contaBancaria.saldo)
        

#Teste do exercício

conta = Contabancaria("Allan")
conta.depositar()
conta.sacar()
conta.imprimir_saldo()