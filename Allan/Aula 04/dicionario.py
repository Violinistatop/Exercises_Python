lista_compras = {}## criando um dicionario##

##adicionar elementos##
lista_compras = {'sabao':2, 'fruta' : 1}

## acessando valores 
valor = lista_compras ['sabao']
print(valor)

##pecorrendo os elementos de um dicionario 

for item, valor in lista_compras.items():
    print( item +":",valor)