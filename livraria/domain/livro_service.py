from livraria.infrastructure.livro_repository import LivroRepository

class LivroService:

    def __init__(self):
        self.repo = LivroRepository()

    def listar_livros(self):
        return self.repo.listar()

    def cadastrar_livro(self, livro):
        self.repo.adicionar(livro)

    def excluir_livro(self, indice):
        self.repo.excluir(indice)

    def buscar_por_titulo(self, texto):
        livros = self.repo.listar()

        return [
            livro for livro in livros
            if texto.lower() in livro["titulo"].lower()
        ]
