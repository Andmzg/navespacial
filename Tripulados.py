from INave import *
from Nave_Interface import NaveInterface
from DbConexion.Repositorio import Repositorio


class Tripulado(INave, NaveInterface):
    frase = "Estamos bien"
    elevarse_f = "Estamos en el aire"
    explota_f = "SOS X 2"

    def __init__(self, capacidad_tripu, destino, mision_tripu, combustible_t, peso_t, pais_t):
        super().__init__(combustible_t, peso_t, pais_t)

        self.repo = Repositorio()

        self.capacidad_tripu = capacidad_tripu
        self.destino = destino
        self.mision_tripo = mision_tripu

        self.caracteristicas = {
            "nave": "tripulada",
            "pais": pais_t,
            "peso": peso_t,
            "combustible": combustible_t,
            "capacidad de tripulantes": capacidad_tripu,
            "destino de la mision": destino,
            "mision": mision_tripu,
        }

    def acople(self):
        print("La nave se acopla a la estacion espacial")

    def aterrizar(self):
        print("Aterrizando")

    # Sobreescritura
    def enviar_dato(self):
        super().enviar_dato()

    def elevarse(self):
        super().elevarse()

    def explota(self):
        super().explota()

    def insertar(self):
        self.repo.insert(self.caracteristicas)
