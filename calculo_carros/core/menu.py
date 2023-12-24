from .utils import convert_string_to_int, convert_string_to_float
from core.cars import CarsFactory as cars
from core.veichle import Carro
from core.person import Pessoa


class ViagemCalculator:
    def __init__(self):
        self.pessoa = None
        self.renova = False
        self.car = None
        self.tarifa_transporte_publico = 2.70

    def chose_car(self):
        print(
            "Aqui temos os carros disponíveis para calcular viagens:\n"
            "1 - Mobi\n"
            "2 - Cerato\n"
            "3 - Rav4 - 2010\n"
            "4 - Voyage - 2012\n"
            "5 - Sair\n"
        )
        opt = input("Escolha uma opção: ")
        if convert_string_to_int(opt) == 1:
            self.car = cars.get_car("Mobi")
        elif convert_string_to_int(opt) == 2:
            self.car = cars.get_car("Cerato")
        elif convert_string_to_int(opt) == 3:
            self.car = cars.get_car("Rav4")
        elif convert_string_to_int(opt) == 4:
            self.car = cars.get_car("Voyage")
        elif convert_string_to_int(opt) == 5:
            print("Até mais!")
            self.car = None
        elif convert_string_to_int(opt) is False:
            print("Opção inválida. Tente novamente.")
        return self.car

    def iniciar_viagem(self):
        print("Seja bem-vindo(a)!\n")
        self.pessoa = Pessoa(input("Qual é o seu nome?\n"))
        print(f"Olá {self.pessoa}!\n")
        renova = str(input("Você está no renova? Y/n\n"))
        self.renova = renova.strip().lower() == "y"

        while True:
            car = self.chose_car()
            if car is None:
                return
            if car is False:
                continue
            car.dono = self.pessoa
            print(f"{self.pessoa}, você escolheu o {car.nome}.\n")
            distancia = input(
                "Agora para simularmos uma viagem, me informe a distância em km:"
            )
            if distancia.strip().lower() == "renova":
                car.realizar_viagem(2.7, renova=True)
                input("Pressione ENTER para continuar")
            else:
                distancia = convert_string_to_float(distancia)
                if distancia is False:
                    print("Distância inválida. Tente novamente.")
                    continue

                print(f"Distância em km: {distancia}")
                if self.renova:
                    car.realizar_viagem(distancia, renova=True)
                else:
                    car.realizar_viagem(distancia)
                input("Pressione ENTER para continuar")



