from INave import *
from Nave_Interface import NaveInterface


class No_tripulado(INave, NaveInterface):
    frase = "soy un bot"
    elevarse_f = "Soy como sucrsito"
    explota_f = "soy un bot. Tambien merezco amor"

    def __init__(self, cuerpo_estudio, en_orbita, combustible_nt, peso_nt, pais_nt):
        super().__init__(combustible_nt, peso_nt, pais_nt)

        self.cuerpo_estudio = cuerpo_estudio
        self.en_orbita = en_orbita

    def aterrizar(self):
        print("Aterrizando")

    # Sobreescritura
    def enviar_dato(self):
        super().enviar_dato()

    def elevarse(self):
        super().elevarse()

    def explota(self):
        super().explota()


