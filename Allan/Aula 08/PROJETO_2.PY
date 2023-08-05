import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
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

lblCpf= Label(janela,text="Cpf",width=8 , font="arial")
lblCpf.place(x=100,y=150)
txtCpf= Entry(janela ,text="", width=20 , font = "arial").place(x=200, y=150)

lblEmail = Label(janela,text="Email",width=8 , font="arial")
lblEmail.place(x=100,y=200)
txtEmail = Entry(janela ,text="", width=20 , font = "arial").place(x=200, y=150)

lblTelefone= Label(janela,text="Telefone",width=8 , font="arial")
lblTelefone.place(x=100,y=250)
txtTelefone = Entry(janela ,text="", width=20 , font = "arial").place(x=200, y=200)


lblCPF= Label(janela,text="CPF",width=8 , font="arial")
lblCPF.place(x=100,y=300)
txtCPF = Entry(janela ,text="", width=20 , font = "arial").place(x=200, y=250)

lblResultado= Label(janela,text="Resultado",width=8 , font="arial")
lblResultado.place(x=100,y=450)

def listar_contatos():
    # Conexão com o banco de dados
    conn = sqlite3.connect("agenda_contatos.db")
    cursor = conn.cursor()

    # Recuperação de dados da tabela
    cursor.execute("SELECT * FROM contatos")
    resultados = cursor.fetchall()

    conn.close()

    # Exibir os resultados em uma nova janela
    janela_listagem = tk.Toplevel(root)
    janela_listagem.title("Lista de Contatos")
    janela_listagem.geometry("400x300")

    frame = ttk.Frame(janela_listagem, padding=10)
    frame.pack(expand=True, fill="both")

    listbox = tk.Listbox(frame, font=("Arial", 12), selectbackground="#b4d1fd")
    listbox.pack(expand=True, fill="both")

    for row in resultados:
        listbox.insert(tk.END, f"Nome: {row[1]}, Telefone: {row[2]}, E-mail: {row[3]}, Apelido: {row[4]}")

def deletar_contato():
    email_contato = entry_email.get()

    if email_contato:
        # Conexão com o banco de dados
        conn = sqlite3.connect("agenda_contatos.db")
        cursor = conn.cursor()

        # Exclusão de dados na tabela pelo e-mail
        cursor.execute("DELETE FROM contatos WHERE email=?", (email_contato,))

        conn.commit()
        conn.close()

        # Limpar o campo após a exclusão
        entry_email.delete(0, tk.END)

        messagebox.showinfo("Sucesso", "Contato deletado com sucesso.")
    else:
        messagebox.showerror("Erro", "Informe o e-mail do contato a ser deletado.")

def main():
    global root
    root = tk.Tk()
    root.title("Agenda de Contatos")
    root.geometry("400x300")  # Tamanho inicial da janela

    # Estilo do tema para melhorar a aparência
    style = ttk.Style(root)
    style.theme_use("clam")

def criar_tabela():
    frame = ttk.Frame(root, padding=10)
    frame.pack(expand=True, fill="both")

    label_nome = ttk.Label(frame, text="Nome:")
    label_nome.grid(row=0, column=0, padx=5, pady=5)
    global entry_nome
    entry_nome = ttk.Entry(frame, font=("Arial", 14))
    entry_nome.grid(row=0, column=1, padx=5, pady=5)

    label_telefone = ttk.Label(frame, text="Telefone:")
    label_telefone.grid(row=1, column=0, padx=5, pady=5)
    global entry_telefone
    entry_telefone = ttk.Entry(frame, font=("Arial", 14))
    entry_telefone.grid(row=1, column=1, padx=5, pady=5)

    label_email = ttk.Label(frame, text="E-mail:")
    label_email.grid(row=2, column=0, padx=5, pady=5)
    global entry_email
    entry_email = ttk.Entry(frame, font=("Arial", 14))
    entry_email.grid(row=2, column=1, padx=5, pady=5)

    label_apelido = ttk.Label(frame, text="Apelido:")
    label_apelido.grid(row=3, column=0, padx=5, pady=5)
    global entry_apelido
    entry_apelido = ttk.Entry(frame, font=("Arial", 14))
    entry_apelido.grid(row=3, column=1, padx=5, pady=5)

    botao_inserir = ttk.Button(frame, text="Inserir")
    botao_inserir.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    botao_listar = ttk.Button(frame, text="Listar", command=listar_contatos)
    botao_listar.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

    label_email_delete = ttk.Label(frame, text="E-mail do contato a ser deletado:")
    label_email_delete.grid(row=6, column=0, padx=5, pady=5)
    global entry_email_delete
    entry_email_delete = ttk.Entry(frame, font=("Arial", 14))
    entry_email_delete.grid(row=6, column=1, padx=5, pady=5)

    botao_deletar = ttk.Button(frame, text="Deletar", command=deletar_contato)
    botao_deletar.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()