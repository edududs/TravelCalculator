from .veichle import Carro


class Pessoa:
    def __init__(self, nome, carro=None) -> None:
        self.nome: str = nome
        self.carro: Carro | None = carro

    def atribuir_carro(self, carro):
        self.carro = carro

    def __repr__(self) -> str:
        return str(self.nome)
