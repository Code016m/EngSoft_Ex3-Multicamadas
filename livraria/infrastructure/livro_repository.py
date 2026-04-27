class LivroRepository:

    def __init__(self):
        self.livros = [
            {"titulo": "Livro A", "autor": "Autor 1", "categoria": "Ficção", "preco": 30},
            {"titulo": "Livro B", "autor": "Autor 2", "categoria": "Técnico", "preco": 50},
            {"titulo": "Livro C", "autor": "Autor 3", "categoria": "Drama", "preco": 40},
        ]

    def listar(self):
        return self.livros

    def adicionar(self, livro):
        self.livros.append(livro)

    def excluir(self, indice):
        del self.livros[indice]
