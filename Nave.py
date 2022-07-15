class Nave:
    def __init__(self, combustible, peso, pais, motor="apagado"):

        self.combustible = combustible
        self.peso = peso
        self.pais = pais
        self.motor = motor

    def encender_motor(self, estado):
        if self.motor == estado:
            print("Motor apagado")

        elif estado == "encendido":
            self.motor = estado
            print(f'El motor esta encendido. Y se esta usando combustible {self.combustible}. '
                  f'Sale del pais {self.pais}')
        else:
            print("no se reconoce el estado")


    def elevarse(self):
        print("El cohete se eleva")


    def explota(self):
        print("El cohete exploto")
