from tkinter import *
from tkinter.constants import END

janela = Tk()
janela.title("formulario de cadastro")

#largura x altura + distancia da margem esquerda + distancia do topo 
janela.geometry ("500x500+500+200")

#definindo a cor de fundo da janela

janela.config(bg="gray")
#labels
lblNome = Label (janela, text="Nome",width=8,font="arial")
lblNome.place(x=100, y=100)
txtNome = Entry(janela ,text="", width=20 , font = "arial").place(x=200, y=100)


lblEmail = Label(janela,text="Email",width=8 , font="arial")
lblEmail.place(x=100,y=150)
txtEmail = Entry(janela ,text="", width=20 , font = "arial").place(x=200, y=150)

lblTelefone= Label(janela,text="Telefone",width=8 , font="arial")
lblTelefone.place(x=100,y=200)
txtTelefone = Entry(janela ,text="", width=20 , font = "arial").place(x=200, y=200)


lblCPF= Label(janela,text="CPF",width=8 , font="arial")
lblCPF.place(x=100,y=250)
txtCPF = Entry(janela ,text="", width=20 , font = "arial").place(x=200, y=250)

lblResultado= Label(janela,text="Resultado",width=8 , font="arial")
lblResultado.place(x=100,y=400)

def Enviar():
    lblResultado["text"]= "secefull!"
    
btnEnviar= Button(janela,text="ENVIAR",width=15,command=Enviar,font="arial")
btnEnviar.place(x=170,y=320)


janela.mainloop()