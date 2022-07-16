from INave import *
from Nave_Interface import NaveInterface


class Tripulado(INave, NaveInterface):
    frase = "SOS"
    elevarse_f = "Estamos en el aire"
    explota_f =  "SOS X 2"

    def __init__(self, capacidad_tripu, destino, mision_tripu, combustible_t, peso_t, pais_t):
        self.capacidad_tripu = capacidad_tripu
        self.destino = destino
        self.mision_tripo = mision_tripu

        super().__init__(combustible_t, peso_t, pais_t)


    def acople(self):
        print("La nave se aacopla a la estacion espacial")

    def aterrizar(self):
        print("Aterrizando")

    # Sobreescritura
    def enviar_dato(self):
        super().enviar_dato()

    def elevarse(self):
        super().elevarse()

    def explota(self):
        super().explota()







