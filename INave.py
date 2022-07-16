from Nave_Interface import NaveInterface


class INave(NaveInterface):

    frase = ''
    elevarse_f = ''
    explota_f = ''

    def __init__(self, combustible, peso, pais):

        self.combustible = combustible
        self.peso = peso
        self.pais = pais


    def enviar_dato(self):
        print(self.frase)

    def elevarse(self):
        print(self.elevarse_f)

    def explota(self):
        print(self.explota_f)
