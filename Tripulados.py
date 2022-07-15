from Nave import *

class tripulado(Nave):
    def __init__(self, capacidad_tripu, destino, mision_tripu, combustible_t, peso_t, pais_t):
        self.capacidad_tripu = capacidad_tripu
        self.destino = destino
        self.mision_tripo = mision_tripu

        super().__init__(combustible_t, peso_t, pais_t)

    def acople(self):
        print("La nave se aacopla a la estacion espacial")

    def aterrizar(self):
        print("Aterrizando")




