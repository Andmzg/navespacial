from Nave import *

class no_tripulado(Nave):
    def __init__(self, cuerpo_estudio, en_orbita, combustible_nt, peso_nt, pais_nt):
        super().__init__(combustible_nt, peso_nt, pais_nt)

        self.cuerpo_estudio = cuerpo_estudio
        self.en_orbita = en_orbita



    def datos_tierra(self):
        print(f"se estan enviando datos a la tierra sobre {self.cuerpo_estudio} que es el objeto a estudiar")

    def aterrizar(self):
        print("Aterrizando")

#prueba = no_tripulado()
#prueba.datos_tierra()