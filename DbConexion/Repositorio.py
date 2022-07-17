from DbConexion.Dbconeccion import *


class Repositorio:  # Clase Repositorio

    # "coleccion" ahora es la coleccion "Nave" de MngoDb
    coleccion = db["Naves"]

    # Metodo para insertar datos en la BD
    def insert(self, data):
        self.coleccion.insert_one(data)

    # Metodo para buscar en la base de datos filtrando por un parametro
    def search(self, data):
        self.coleccion.find(data)

        # Ordena la busqueda en una manera mas presentable
        for doc in self.coleccion.find(data):
            print(doc)
