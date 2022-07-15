from Nave import *

class no_tripulad:
    def __int__(self, cuerpo_estudio, en_orbita, combustible_nt, peso_nt, pais_nt):
        self.cuerpo_estudio = cuerpo_estudio
        self.en_orbita = en_orbita

        super().__init__(combustible_nt, peso_nt, pais_nt)

    def datos_tierra(self):
        print("se estan enviando datos a la tierra")

    def aterrizar(self):
        print("Aterrizando")
