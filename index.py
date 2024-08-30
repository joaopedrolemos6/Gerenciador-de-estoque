import tkinter as tk
from tkinter import messagebox

produtos = {}

def adicionar_produto():
    nome = entry_nome.get()
    quantidade = entry_quantidade.get()

    if nome and quantidade.isdigit():
        produtos[nome] = int(quantidade)
        messagebox.showinfo("Sucesso", f"Produto '{nome}' adicionado com sucesso!")
        entry_nome.delete(0, tk.END)
        entry_quantidade.delete(0, tk.END)
    else:
        messagebox.showwarning("Erro", "Por favor, insira um nome válido e uma quantidade numérica.")

def remover_produto():
    nome = entry_nome.get()

    if nome in produtos:
        del produtos[nome]
        messagebox.showinfo("Sucesso", f"Produto '{nome}' removido com sucesso!")
    else:
        messagebox.showwarning("Erro", f"Produto '{nome}' não encontrado no estoque.")

    entry_nome.delete(0, tk.END)
    entry_quantidade.delete(0, tk.END)

def atualizar_quantidade():
    nome = entry_nome.get()
    quantidade = entry_quantidade.get()

    if nome in produtos and quantidade.isdigit():
        produtos[nome] = int(quantidade)
        messagebox.showinfo("Sucesso", f"Quantidade do produto '{nome}' atualizada com sucesso!")
    else:
        messagebox.showwarning("Erro", f"Produto '{nome}' não encontrado no estoque ou quantidade inválida.")

    entry_nome.delete(0, tk.END)
    entry_quantidade.delete(0, tk.END)

def consultar_estoque():
    estoque = "\n".join([f"{nome}: {quantidade}" for nome, quantidade in produtos.items()])
    if estoque:
        messagebox.showinfo("Estoque Atual", estoque)
    else:
        messagebox.showinfo("Estoque Atual", "Estoque vazio.")

root = tk.Tk()
root.title("Controle de Estoque")

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)

label_nome = tk.Label(root, text="Nome do Produto:")
label_nome.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

entry_nome = tk.Entry(root)
entry_nome.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

label_quantidade = tk.Label(root, text="Quantidade:")
label_quantidade.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

entry_quantidade = tk.Entry(root)
entry_quantidade.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

btn_adicionar = tk.Button(root, text="Adicionar Produto", command=adicionar_produto)
btn_adicionar.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

btn_remover = tk.Button(root, text="Remover Produto", command=remover_produto)
btn_remover.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

btn_atualizar = tk.Button(root, text="Atualizar Quantidade", command=atualizar_quantidade)
btn_atualizar.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

btn_consultar = tk.Button(root, text="Consultar Estoque", command=consultar_estoque)
btn_consultar.grid(row=3, column=1, padx=10, pady=10, sticky="nsew")

root.mainloop()
