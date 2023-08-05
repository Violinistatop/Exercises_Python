class Conta:
    def __init__(contabancaria):
        contabancaria.saldo = 0
    
    def depositar(contabancaria, valor):
        contabancaria.saldo += valor
    
    def sacar(contabancaria, valor):
        if contabancaria.saldo >= valor:
            contabancaria.saldo -= valor
        else:
            print("Saldo insuficiente!")
    
    def imprimir_saldo(contabancaria):
        print("Saldo atual: R$", contabancaria.saldo)

conta1 = Conta()
conta1.depositar(100)
conta1.sacar(50)
conta1.imprimir_saldo()
