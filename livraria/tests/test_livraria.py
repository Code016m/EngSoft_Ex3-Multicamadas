import unittest
from livraria.domain.livro_service import LivroService


class TestLivrariaMulticamadas(unittest.TestCase):

    def test_listar_livros(self):
        service = LivroService()

        self.assertEqual(len(service.listar_livros()), 3)

    def test_cadastrar_livro(self):
        service = LivroService()

        service.cadastrar_livro({
            "titulo": "Novo",
            "autor": "Autor X",
            "categoria": "Drama",
            "preco": 45
        })

        self.assertEqual(len(service.listar_livros()), 4)

    def test_excluir_livro(self):
        service = LivroService()

        service.excluir_livro(0)

        self.assertEqual(len(service.listar_livros()), 2)

    def test_buscar_livro(self):
        service = LivroService()

        resultado = service.buscar_por_titulo("Livro A")

        self.assertEqual(len(resultado), 1)


if __name__ == "__main__":
    unittest.main()