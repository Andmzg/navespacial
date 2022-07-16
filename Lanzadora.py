from INave import *
from Nave_Interface import NaveInterface
from DbConexion.Repositorio import Repositorio

class Lanzadora(INave, NaveInterface):
    frase = "La nave ha sido lanzada"
    elevarse_f = "como Snoop Dog"
    explota_f = "BOOM"


    def __init__(self, carga_util, tipo_carga, combustible_Lanza, peso_Lanza, pais_Lanza):
        super().__init__(combustible_Lanza, peso_Lanza, pais_Lanza)
        self.repo = Repositorio()

        self.carga_util = carga_util
        self.tipo_carga = tipo_carga


        self.caracteristicas = {
            "nave": "Lanzadora",
            "pais": pais_Lanza,
            "peso": peso_Lanza,
            "combustible" : combustible_Lanza,
            "carga util": carga_util,
            "tipo carga": tipo_carga
        }

    def soltar_carga(self):
        print(f"Luego de 10 min La carga se suelta. {self.pais}")

    #Sobreescritura

    def enviar_dato(self):
         super().enviar_dato()

    def elevarse(self):
        super().elevarse()

    def explota(self):
        super().explota()

    #Mongo
    def insertar(self):
        self.repo.insert(self.caracteristicas)

# prueba = Lanzadora("a", "b", "c", "d", "e")
# prueba.enviar_dato()