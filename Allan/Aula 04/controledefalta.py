###sistema de controle de falta###


quantidade_falta = int(input("digite a quantidade de falta:"))

if(quantidade_falta<= 0.25*80):
    print("voce esta dentro do limeite de faltas.")
else:
    print("voce excedeu o limite de faltas.")
    