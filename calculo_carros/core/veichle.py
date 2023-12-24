from abc import ABC, abstractmethod

from .utils import convert_string_to_float, convert_string_to_int


class Veiculo(ABC):
    def __init__(
        self,
        km_litro: dict,
        preco_gasolina: float = 5.65,
        tarifa_transporte_publico: float = 2.70,
    ) -> None:
        self.nome: str = ""
        self.litros_necessarios: float = 0.0
        self.km_litro = km_litro
        self.preco_gasolina = preco_gasolina
        self.tarifa_transporte_publico = tarifa_transporte_publico

    @abstractmethod
    def calcular_litros_por_distancia(self, distancia: float) -> float:
        pass

    @abstractmethod
    def calcular_preco(self, preco_gasolina: float) -> float | None:
        pass


class Carro(Veiculo):
    def calcular_litros_por_distancia(self, distancia: float) -> float:
        try:
            if self.km_litro["urbano"]["gasolina"] is not None:
                consumo_km_litro = self.km_litro["urbano"]["gasolina"]
                print(f"Consumo km por litro: {consumo_km_litro}")
                if not self.litros_necessarios:
                    self.litros_necessarios = distancia / consumo_km_litro
            return self.litros_necessarios

        except Exception as e:
            raise e

    def calcular_preco(self, preco_gasolina: float) -> float | None:
        try:
            if self.litros_necessarios is not None:
                preco = self.litros_necessarios * preco_gasolina
                return preco
        except Exception as e:
            print(
                "Primeiro veja quantos litros são necessários para percorrer uma distância."
            )
            raise e

    def realizar_viagem(
        self,
        distancia: float,
        preco_gasolina_df: float = 5.65,  # preco_gasolina,
        renova: bool = False,
    ):
        litros_necessarios_gasolina = self.calcular_litros_por_distancia(distancia)
        gasto_gasolina = self.calcular_preco(preco_gasolina_df)
        consumo_km_litro = self.km_litro["urbano"]["gasolina"]
        if gasto_gasolina is not None:
            if renova:
                self.show_renova(
                    consumo_km_litro,
                    distancia,
                    litros_necessarios_gasolina,
                    gasto_gasolina,
                )
                return

            self.show(
                consumo_km_litro,
                distancia,
                litros_necessarios_gasolina,
                gasto_gasolina,
            )

    def transporte_publico(self, transporte_publico_tarifa, dias_de_trabalho):
        if dias_de_trabalho and transporte_publico_tarifa:
            print(f"\n{8*'*'} Transporte Público {8*'*'}")
            if transporte_publico_tarifa is True:
                transporte_publico_tarifa = convert_string_to_float(
                    input("Tarifa do transporte púbico, dê enter para R$2.75: ")
                )
                if transporte_publico_tarifa is None:
                    transporte_publico_tarifa = 2.75
            if transporte_publico_tarifa:
                valor_gasto = transporte_publico_tarifa * dias_de_trabalho
                resultado_transporte_publico = f"""
\tCom o tarifa de R${transporte_publico_tarifa:.2f}, só levando o gasto é de R${valor_gasto:.2f}.
\tLevando e trazendo o gasto é de R${(valor_gasto * 2):.2f}.
"""
                print(resultado_transporte_publico)

    def dias_trabalho(self, gasto_gasolina):
        print(f"\n{8*'*'} Dias de Trabalho {8*'*'}")
        dias_de_trabalho = convert_string_to_int(
            input("Dias de trabalho, dê enter para 22 (mês útil): ")
        )
        if dias_de_trabalho is None:
            dias_de_trabalho = 22

        resultado_dias_trabalho = f"""
\tCom {dias_de_trabalho} dias com o carro só levando você gastaria R${(gasto_gasolina * 2 * dias_de_trabalho):.2f}.
\tCom o carro levando e trazendo de tarde você gastaria R${(gasto_gasolina * 4) * dias_de_trabalho:.2f} em {dias_de_trabalho} dias.
\tCom {dias_de_trabalho} dias de trabalho, você gastaria R${(gasto_gasolina * 2 * dias_de_trabalho):.2f} em {dias_de_trabalho} dias.
"""
        print(resultado_dias_trabalho)
        return dias_de_trabalho

    def show_renova(
        self,
        consumo_km_litro: float,
        distancia: float,
        litros_necessarios_gasolina: float,
        gasto_gasolina: float,
    ):
        carro_ida_volta = gasto_gasolina * 2
        resultado = f"""
\t{self.nome} faz {consumo_km_litro}km por litro de gasolina.
\tPara percorrer a distância de {distancia}km, você precisará de aproximadamente {litros_necessarios_gasolina:.2f} litros de gasolina.
\tCom o preço da gasolina a R${self.preco_gasolina:.2f}, seu gasto será de R${gasto_gasolina:.2f}.
\tSe for ida e volta, seu gasto será de R${carro_ida_volta:.2f}.
\tSe for ida e volta duas vezes no dia, seu gasto será de R${(gasto_gasolina * 4):.2f}.
"""
        print(resultado)
        dias_de_trabalho = self.dias_trabalho(gasto_gasolina)
        self.transporte_publico(self.tarifa_transporte_publico, dias_de_trabalho)

        return

    def show(
        self,
        consumo_km_litro: float,
        distancia: float,
        litros_necessarios_gasolina: float,
        gasto_gasolina: float,
    ):
        carro_ida_volta = gasto_gasolina * 2
        resultado = f"""
\t{self.nome} faz {consumo_km_litro}km por litro de gasolina.
\tPara percorrer a distância de {distancia}km, você precisará de aproximadamente {litros_necessarios_gasolina:.2f} litros de gasolina.
\tCom o preço da gasolina a R${self.preco_gasolina:.2f}, seu gasto será de R${gasto_gasolina:.2f}.
\tSe for ida e volta, seu gasto será de R${carro_ida_volta:.2f}.
\tSe for ida e volta duas vezes no dia, seu gasto será de R${(gasto_gasolina * 4):.2f}.
"""
        print(resultado)
        dias = input("Quer saber o cálculo por dias? Y/n: ").strip().lower()
        if dias == "y":
            dias_de_trabalho = self.dias_trabalho(gasto_gasolina)
            transporte = (
                input("Quer saber o cálculo por transporte publico? Y/n: ")
                .lower()
                .strip()
            )
            if transporte == "y":
                self.transporte_publico(
                    self.tarifa_transporte_publico, dias_de_trabalho
                )

        return
