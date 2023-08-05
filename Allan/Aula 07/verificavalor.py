from tkinter import *
from tkinter.constants import END


janela = Tk()
janela.title("Formulário de Cadastro")
janela.geometry("500x200+500+200")  
janela.config(bg="#0abab5")  


lblNome = Label(janela, text="Número", width=8, font="calibri")
lblNome.place(x=100, y=10)
textNome = Entry(janela, width=19, font="calibri")
textNome.place(x=200, y=10)

def Verificar():
    numero = int(textNome.get())
    if numero % 2 == 0:
        resultado = "O número é par."
    else:
        resultado = "O número é ímpar."

    lblResultado["text"] = resultado
    textNome.delete(0, END)

btnEnviar = Button(janela, text="Verificar", width=25, command=Verificar, font="calibri")
btnEnviar.place(x=150, y=50)


lblResultado = Label(janela, text="Resultado", width=40, font="calibri")
lblResultado.place(x=100, y=100)

janela.mainloop()


