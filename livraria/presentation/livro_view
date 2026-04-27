import tkinter as tk

class LivroView:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("EX3 Multicamadas")
        self.root.geometry("800x600")

        self.controller = None

        self.entry_titulo = tk.Entry(self.root, width=40)
        self.entry_titulo.pack()

        self.entry_autor = tk.Entry(self.root, width=40)
        self.entry_autor.pack()

        self.entry_categoria = tk.Entry(self.root, width=40)
        self.entry_categoria.pack()

        self.entry_preco = tk.Entry(self.root, width=40)
        self.entry_preco.pack()

        tk.Button(self.root, text="Cadastrar", command=self.cadastrar_click).pack()
        tk.Button(self.root, text="Listar", command=self.listar_click).pack()
        tk.Button(self.root, text="Excluir", command=self.excluir_click).pack()

        self.entry_busca = tk.Entry(self.root, width=40)
        self.entry_busca.pack()

        tk.Button(self.root, text="Buscar Livro", command=self.buscar_click).pack()

        self.lista = tk.Listbox(self.root, width=80, height=20)
        self.lista.pack()

    def set_controller(self, c):
        self.controller = c

    def cadastrar_click(self):
        self.controller.cadastrar_livro()

    def listar_click(self):
        self.controller.listar_livros()

    def excluir_click(self):
        self.controller.excluir_livro()

    def buscar_click(self):
        self.controller.buscar_livro()

    def obter_dados(self):
        return {
            "titulo": self.entry_titulo.get(),
            "autor": self.entry_autor.get(),
            "categoria": self.entry_categoria.get(),
            "preco": float(self.entry_preco.get())
        }

    def obter_busca(self):
        return self.entry_busca.get()

    def obter_indice_selecionado(self):
        item = self.lista.curselection()
        return item[0] if item else None

    def mostrar_livros(self, livros):
        self.lista.delete(0, tk.END)

        for livro in livros:
            self.lista.insert(tk.END, livro["titulo"])

    def limpar_campos(self):
        self.entry_titulo.delete(0, tk.END)
        self.entry_autor.delete(0, tk.END)
        self.entry_categoria.delete(0, tk.END)
        self.entry_preco.delete(0, tk.END)

    def iniciar(self):
        self.root.mainloop()
