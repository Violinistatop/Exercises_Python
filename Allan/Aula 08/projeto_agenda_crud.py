import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3

def criar_tabela():
    # Conexão com o banco de dados
    conn = sqlite3.connect("cadastro_contatos.db")
    cursor = conn.cursor()

    # Criação da tabela se ainda não existir
    cursor.execute('''CREATE TABLE IF NOT EXISTS cadastro
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    telefone TEXT NOT NULL,
                    email TEXT NOT NULL,
                    cpf TEXT NOT NULL)''')

    conn.commit()
    conn.close()

def inserir_contato():
    nome = entry_nome.get()
    telefone = entry_telefone.get()
    email = entry_email.get()
    cpf = entry_cpf.get()

    if nome and telefone and email and cpf:
        # Conexão com o banco de dados
        conn = sqlite3.connect("cadastro_contatos.db")
        cursor = conn.cursor()

        # Inserção dos dados na tabela
        cursor.execute("INSERT INTO cadastro (nome, telefone, email, cpf) VALUES (?, ?, ?, ?)", (nome, telefone, email, cpf))

        conn.commit()
        conn.close()

        # Limpar os campos após a inserção
        entry_nome.delete(0, tk.END)
        entry_telefone.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_cpf.delete(0, tk.END)

        messagebox.showinfo("Sucesso", "Contato inserido com sucesso.")
    else:
        messagebox.showerror("Erro", "Todos os campos são obrigatórios.")

def listar_contatos():
    # Conexão com o banco de dados
    conn = sqlite3.connect("cadastro_contatos.db")
    cursor = conn.cursor()

    # Recuperação de dados da tabela
    cursor.execute("SELECT * FROM cadastro")
    resultados = cursor.fetchall()

    conn.close()

    # Exibir os resultados em uma nova janela
    janela_listagem = tk.Toplevel(root)
    janela_listagem.title("Cadastro de Contatos")
    janela_listagem.geometry("700x300")

    frame = ttk.Frame(janela_listagem, padding=10)
    frame.pack(expand=True, fill="both")

    listbox = tk.Listbox(frame, font=("Arial", 11), selectbackground="#b4d1fd")
    listbox.pack(expand=True, fill="both")

    for row in resultados:
        listbox.insert(tk.END, f"Nome: {row[1]}, Telefone: {row[2]}, E-mail: {row[3]}, CPF: {row[4]}")

def deletar_contato():
    cpf_contato = entry_cpf_delete.get()

    if cpf_contato:
        # Conexão com o banco de dados
        conn = sqlite3.connect("cadastro_contatos.db")
        cursor = conn.cursor()

        # Exclusão de dados na tabela pelo e-mail
        cursor.execute("DELETE FROM cadastro WHERE cpf=?", (cpf_contato,))

        conn.commit()
        conn.close()

        # Limpar o campo após a exclusão
        entry_cpf_delete.delete(0, tk.END)

        messagebox.showinfo("Sucesso", "Contato deletado com sucesso.")
    else:
        messagebox.showerror("Erro", "Informe o CPF do contato a ser deletado.")

def main():
    global root
    root = tk.Tk()
    root.title("Cadastro de Contatos")
    root.geometry("500x500+500+200")  # Tamanho inicial da janela

    # Estilo do tema para melhorar a aparência
    style = ttk.Style(root)
    style.theme_use("clam")

    criar_tabela()

    frame = ttk.Frame(root, padding=10)
    frame.pack(expand=True, fill="both")

    label_nome = ttk.Label(frame, text="Nome:")
    label_nome.grid(row=0, column=0, padx=5, pady=5)
    global entry_nome
    entry_nome = ttk.Entry(frame, font=("Arial", 11))
    entry_nome.grid(row=0, column=1, padx=5, pady=5)

    label_telefone = ttk.Label(frame, text="Telefone:")
    label_telefone.grid(row=1, column=0, padx=5, pady=5)
    global entry_telefone
    entry_telefone = ttk.Entry(frame, font=("Arial", 11))
    entry_telefone.grid(row=1, column=1, padx=5, pady=5)

    label_email = ttk.Label(frame, text="E-mail:")
    label_email.grid(row=2, column=0, padx=5, pady=5)
    global entry_email
    entry_email = ttk.Entry(frame, font=("Arial", 11))
    entry_email.grid(row=2, column=1, padx=5, pady=5)

    label_cpf = ttk.Label(frame, text="CPF:")
    label_cpf.grid(row=3, column=0, padx=5, pady=5)
    global entry_cpf
    entry_cpf = ttk.Entry(frame, font=("Arial", 11))
    entry_cpf.grid(row=3, column=1, padx=5, pady=5)

    botao_inserir = ttk.Button(frame, text="Inserir", command=inserir_contato)
    botao_inserir.grid(row=4, column=0, columnspan=1, padx=5, pady=5)

    botao_listar = ttk.Button(frame, text="Listar", command=listar_contatos)
    botao_listar.grid(row=4, column=1, columnspan=2, padx=5, pady=5)

    label_cpf_delete = ttk.Label(frame, text="CPF do contato a ser deletado:")
    label_cpf_delete.grid(row=6, column=0, padx=5, pady=5)
    global entry_cpf_delete
    entry_cpf_delete = ttk.Entry(frame, font=("Arial", 11))
    entry_cpf_delete.grid(row=6, column=1, padx=5, pady=5)

    botao_deletar = ttk.Button(frame, text="Deletar", command=deletar_contato)
    botao_deletar.grid(row=7, column=1, columnspan=2, padx=5, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()