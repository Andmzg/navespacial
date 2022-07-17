from INave import *
from Nave_Interface import NaveInterface
from DbConexion.Repositorio import Repositorio


# Creacion de clase
class Notripulado(INave, NaveInterface):

    # Valores que se sobreescriben en los metodos heredados
    frase = "soy un bot"
    elevarse_f = "Soy como sucrsito"
    explota_f = "soy un bot. Tambien merezco amor"

    def __init__(self, cuerpo_estudio, en_orbita, combustible_nt, peso_nt, pais_nt):

        super().__init__(combustible_nt, peso_nt, pais_nt)

        self.repo = Repositorio()

        self.cuerpo_estudio = cuerpo_estudio
        self.en_orbita = en_orbita

        self.caracteristicas = {
            "nave": "No tripulada",
            "pais": pais_nt,
            "peso": peso_nt,
            "combustible": combustible_nt,
            "cuerpo de estudio": cuerpo_estudio,
            "en orbita": en_orbita
        }

    # Metodo de instacia
    def aterrizar(self):
        print("Aterrizando")

    # Sobreescritura
    def enviar_dato(self):
        super().enviar_dato()

    def elevarse(self):
        super().elevarse()

    def explota(self):
        super().explota()

    # Mongo
    def insertar(self):
        self.repo.insert(self.caracteristicas)
