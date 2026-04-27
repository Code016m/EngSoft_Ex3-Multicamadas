from livraria.application.livro_controller import LivroController


def executar_app():
    controller = LivroController()
    controller.iniciar()


if __name__ == "__main__":
    executar_app()