from Nave import *

class Lanzadora(Nave):
    def __init__(self, carga_util, tipo_carga, combustible_Lanza, peso_Lanza, pais_Lanza):
        super().__init__(combustible_Lanza, peso_Lanza, pais_Lanza)

        self.carga_util = carga_util
        self.tipo_carga = tipo_carga

    def soltar_carga(self):
        print("Luego de 10 min La carga se suelta")


