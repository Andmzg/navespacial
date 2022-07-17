# Importamos INave que es la clase padre
from INave import *
# Importamos Nave_Interface ya que es la interfaz
from Nave_Interface import NaveInterface
# Importamos DbConexion.Repositorio ya que nos ayuda con la DB
from DbConexion.Repositorio import Repositorio


# Creacion de la clase Lanzadora (Un tipo nave que transporta a otras naves)
# Se hereda de dos clases diferentes por heredar de Inave y la interfaz NaveInterface
class Lanzadora(INave, NaveInterface):

    # Valores que se sobreescriben en los metodos heredados
    frase = "La nave ha sido lanzada"
    elevarse_f = "Estamos por los aires"
    explota_f = "BOOM"

    # Constructor de la clase Lanzadora
    # Se coloca en el constructor los dos parametros propios de la clase + los tres que hereda de la clase padre
    def __init__(self, carga_util, tipo_carga, combustiblelanza, pesolanza, paislanza):
        # El super() llama al constructor padre y se alica herencia
        super().__init__(combustiblelanza, pesolanza, paislanza)

        # Se crea un objeto a partir de la clase Repositorio
        self.repo = Repositorio()

        # Variables de instacia
        self.carga_util = carga_util
        self.tipo_carga = tipo_carga

        # Variables de instacia. Esta vez es un diccionario. Al diccionario se le pasan los datos heredados y
        # propios de la calse. Asi se puede guardar en la Db
        self.caracteristicas = {
            "nave": "lanzadora",
            "pais": paislanza,
            "peso": pesolanza,
            "combustible": combustiblelanza,
            "carga util": carga_util,
            "tipo carga": tipo_carga
        }

    # Metodo de instacia
    def soltar_carga(self):
        print("Luego de 10 min La carga se suelta.")

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

# prueba = Lanzadora("a", "b", "c", "d", "e")
# prueba.enviar_dato()
