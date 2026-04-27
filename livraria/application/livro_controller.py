from livraria.presentation.livro_view import LivroView
from livraria.domain.livro_service import LivroService

class LivroController:

    def __init__(self):
        self.service = LivroService()
        self.view = LivroView()
        self.view.set_controller(self)

    def cadastrar_livro(self):
        livro = self.view.obter_dados()
        self.service.cadastrar_livro(livro)
        self.view.limpar_campos()
        self.listar_livros()

    def listar_livros(self):
        livros = self.service.listar_livros()
        self.view.mostrar_livros(livros)

    def excluir_livro(self):
        indice = self.view.obter_indice_selecionado()

        if indice is not None:
            self.service.excluir_livro(indice)
            self.listar_livros()

    def buscar_livro(self):
        texto = self.view.obter_busca()
        livros = self.service.buscar_por_titulo(texto)
        self.view.mostrar_livros(livros)

    def iniciar(self):
        self.view.iniciar()
