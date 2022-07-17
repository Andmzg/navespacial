import pymongo

# set a 5-second connection timeout

# Creando coneccion con  mongo atlas
client = pymongo.MongoClient('mongodb+srv://andmz:abc123*@cluster0.d2i3um1.mongodb.net/'
                             'Estacion?retryWrites=true&w=majority', serverSelectionTimeoutMS=5000)
try:

    db = client['Estacion']  # Revisa la base de datos que le coloques

    collections = db.list_collection_names()  # Se buscan las colecciones de la DB

    if "Naves" not in collections:  # Si la coleccion Nave no existe, la crea
        print(client.server_info())  # Saber si me estoy conectando bien
        collection = db["Naves"]  # Creando coleccion Nave
        print('Se creo la coleccion')
        print(collection)
        # si no se inscerta algun valor no crea la coleccion
        collection.insert_one({"pais": "prueba", "combustible": "prueba", "peso": 0})
        collections = db.list_collection_names()  # Se buscan las colecciones de la DB
        print(collections)

    print("Conectado satisfactoriamente")


except Exception as error:
    print(error)
