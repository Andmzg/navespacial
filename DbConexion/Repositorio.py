from DbConexion.Dbconeccion import *
import pprint

class Repositorio:

    coleccion = db["Naves"]

    def insert(self, data):
        self.coleccion.insert_one(data)


    def search(self, data):
        self.coleccion.find(data)

        for doc in self.coleccion.find(data):
            print(doc)




