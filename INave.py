from Nave_Interface import NaveInterface


class INave(NaveInterface):

    # Valores iniciales o predeterminados de los metodos definidos
    frase = ''
    elevarse_f = ''
    explota_f = ''

    # Metodo constructor. Contiene Caracteristicas en comun de las naves
    def __int__(self, combustible, peso, pais):
        # Instancias de la clase INave
        self.combustible = combustible

        # Variables de instacia
        self.peso = peso
        self.pais = pais

    # Metodos que se sobre sobreescriben
    def enviar_dato(self):
        print(self.frase)

    def elevarse(self):
        print(self.elevarse_f)

    def explota(self):
        print(self.explota_f)
