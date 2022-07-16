from abc import abstractmethod
from abc import ABCMeta


class NaveInterface(metaclass=ABCMeta):

    def __init__(self, combustible, peso, pais):
        pass

    @abstractmethod
    def enviar_dato(self):
        pass

    @abstractmethod
    def elevarse(self):
        pass

    @abstractmethod
    def explota(self):
        pass
