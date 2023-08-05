##controle de estoque##
estoque=[]
quantidade=[]
#funcao adicionar produto ao estoque

def adicionar_produto():
 nome_produto= input("Digite o nome do produto: ")
 estoque.append(nome_produto)

quant_prod = int(input("digite a quantidade do produto"))
estoque.append(quant_prod)

#funçao para verificar se um produto exite no estoque 
def verifica_produto():
    for produto in estoque:
     if estoque[0]== estoque:
      print("o produto ",produto,"esta em estoque")
    else :
      print("não consta o produto em estoque")

def atualiza_produto():
  nova_quantidade = int(input("digite a nova quantidade do produto"))


