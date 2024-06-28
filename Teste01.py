import tkinter as tk  # Importa a TK inter e para esse projeto vamos chama de tk
from tkinter import ttk, messagebox  # Importa dois modulos, um que melora os componente e o outro deixa o usuario exibir um mensagem na tela

# Lista para armazenar os produtos
produtos = []

# Função para cadastrar um novo produto
def cadastrar_produto():
    nome = entry_nome.get()  # entry_ cria caixa de texto, get pega o texte digitado
    descricao = entry_descricao.get()  
    valor = entry_valor.get()  
    disponivel = var_disponivel.get()  
    
    # Verificando se esta tudo ok e caso não esteja exibe a janela do messagebox
    if not nome or not descricao or not valor:
        messagebox.showwarning("Campos obrigatórios", "Por favor, preencha todos os campos.")
        return
    
    # Verifica se o valor inserido é numérico
    try:
        valor = float(valor)
    except ValueError:
        messagebox.showwarning("Valor inválido", "Por favor, insira um valor numérico para o valor do produto.")
        return
    
    # Adiciona novo produto na lista e ordena a lista pelo valor
    produtos.append({"nome": nome, "descricao": descricao, "valor": valor, "disponivel": disponivel})
    produtos.sort(key=lambda x: x["valor"])
    
    # Atualiza a a lista
    atualizar_lista()
    
    # Oculta o formulário de cadastro e mostra a listagem
    frame_cadastro.pack_forget()
    frame_listagem.pack(fill="both", expand=True)

# Função para atualizar a listagem de produtos
def atualizar_lista():
    # Limpa todos os itens da Treeview
    for row in tree.get_children():
        tree.delete(row)
    
    # Adiciona cada produto à Treeview
    for produto in produtos:
        tree.insert("", "end", values=(produto["nome"], f'R${produto["valor"]:.2f}'))

# Função para abrir o formulário de cadastro
def abrir_cadastro():
    # Oculta a listagem e mostra o formulário de cadastro
    frame_listagem.pack_forget()
    frame_cadastro.pack(fill="both", expand=True)

# Configuração da janela principal
root = tk.Tk()  # Cria a janela principal
root.title("Cadastro de Produtos")  # Define o título da janela

# Frame de cadastro
frame_cadastro = tk.Frame(root)  # Cria um frame para o formulário de cadastro
tk.Label(frame_cadastro, text="Nome do produto").pack(pady=5)  # Rótulo para o campo de nome
entry_nome = tk.Entry(frame_cadastro)  # Campo de texto para o nome
entry_nome.pack(pady=5)

tk.Label(frame_cadastro, text="Descrição do produto").pack(pady=5)  # Rótulo para o campo de descrição
entry_descricao = tk.Entry(frame_cadastro)  # Campo de texto para a descrição
entry_descricao.pack(pady=5)

tk.Label(frame_cadastro, text="Valor do produto").pack(pady=5)  # Rótulo para o campo de valor
entry_valor = tk.Entry(frame_cadastro)  # Campo de texto para o valor
entry_valor.pack(pady=5)

tk.Label(frame_cadastro, text="Disponível para venda").pack(pady=5)  # Rótulo para o campo de disponibilidade
var_disponivel = tk.StringVar(value="Sim")  # Variável para armazenar a opção selecionada
tk.Radiobutton(frame_cadastro, text="Sim", variable=var_disponivel, value="Sim").pack(anchor="w")  # Botão de opção "Sim"
tk.Radiobutton(frame_cadastro, text="Não", variable=var_disponivel, value="Não").pack(anchor="w")  # Botão de opção "Não"

tk.Button(frame_cadastro, text="Cadastrar", command=cadastrar_produto).pack(pady=20)  # Botão para cadastrar o produto
tk.Button(frame_cadastro, text="Cancelar", command=lambda: [frame_cadastro.pack_forget(), frame_listagem.pack(fill="both", expand=True)]).pack(pady=5)  # Botão para cancelar e voltar à listagem

# Frame de listagem
frame_listagem = tk.Frame(root)  # Cria um frame para a listagem de produtos
tree = ttk.Treeview(frame_listagem, columns=("nome", "valor"), show="headings")  # Cria uma Treeview para listar os produtos
tree.heading("nome", text="Nome")  # Define o cabeçalho da coluna "Nome"
tree.heading("valor", text="Valor")  # Define o cabeçalho da coluna "Valor"
tree.pack(fill="both", expand=True)

tk.Button(frame_listagem, text="Novo Produto", command=abrir_cadastro).pack(pady=20)  # Botão para abrir o formulário de cadastro

# Iniciar na tela de listagem
frame_listagem.pack(fill="both", expand=True)  # Mostra a listagem de produtos

# Loop principal da aplicação
root.mainloop()  # Inicia o loop principal da interface gráfica