from .person import Pessoa
from .veichle import Carro


class Voyage2012(Carro):
    def __init__(self, dono=""):
        super().__init__({"urbano": {"gasolina": 10.7, "alcool": 7.3}})
        self.nome = "Voyage"
        self.ano = 2012
        self.cor = "Branco"
        self.configuracao = "Sedan"

        self.dono = Pessoa(dono)

    def realizar_viagem(
        self,
        distancia: float,
        preco_gasolina_df: float = 5.65,
        renova: bool = False,
    ):
        print(f"{self.nome} {self.ano} {self.cor} {self.configuracao} de {self.dono}")
        return super().realizar_viagem(
            distancia,
            preco_gasolina_df,
            renova,
        )

    def __repr__(self) -> str:
        return self.nome


class Cerato(Carro):
    def __init__(self, dono=""):
        super().__init__({"urbano": {"gasolina": 9.6, "alcool": 6.5}})
        self.nome = "Cerato"
        self.ano = 2014
        self.cor = "Cinza"
        self.configuracao = "Sedan"

        self.dono = Pessoa(dono)

    def realizar_viagem(
        self,
        distancia: float,
        preco_gasolina_df: float = 5.65,
        renova: bool = False,
    ):
        print(f"{self.nome} {self.ano} {self.cor} {self.configuracao} de {self.dono}")
        return super().realizar_viagem(
            distancia,
            preco_gasolina_df,
            renova,
        )


class Mobi(Carro):
    def __init__(self, dono=""):
        super().__init__({"urbano": {"gasolina": 13.0, "alcool": 0}})
        self.nome = "Mobi"
        self.ano = 0
        self.cor = "Branco"
        self.configuracao = "Ret"

        self.dono = Pessoa(dono)

    def realizar_viagem(
        self,
        distancia: float,
        preco_gasolina_df: float = 5.65,
        renova: bool = False,
    ):
        print(f"{self.nome} {self.ano} {self.cor} {self.configuracao} de {self.dono}")
        return super().realizar_viagem(
            distancia,
            preco_gasolina_df,
            renova,
        )

    def __repr__(self) -> str:
        return self.nome


class Rav4(Carro):
    def __init__(self, dono=""):
        super().__init__({"urbano": {"gasolina": 10.0, "alcool": 0}})
        self.nome = "Rav4"
        self.ano = 2008
        self.cor = "Preto"
        self.configuracao = ""

        self.dono = Pessoa(dono)

    def realizar_viagem(
        self,
        distancia: float,
        preco_gasolina_df: float = 5.65,
        renova: bool = False,
    ):
        print(f"{self.nome} {self.ano} {self.cor} {self.configuracao} de {self.dono}")
        return super().realizar_viagem(
            distancia,
            preco_gasolina_df,
            renova,
        )

    def __repr__(self) -> str:
        return self.nome


class CarsFactory:
    @staticmethod
    def get_car(car):
        if car == "Voyage":
            return Voyage2012()
        elif car == "Cerato":
            return Cerato()
        elif car == "Mobi":
            return Mobi()
        elif car == "Rav4":
            return Rav4()
        else:
            return None
