from Lanzadora import Lanzadora
from  No_Tripulados import Notripulado
from  Tripulados import Tripulado
from DbConexion.Repositorio import Repositorio
from Nave_Marvin import NaveMarvin

repo = Repositorio()

opcion = 0
while opcion != 5:

    print("1.- Crear nave lanzadora")
    print("2.- Crear nave No tripulada")
    print("3.- Crear nave tripulada")
    print("4.- Crear una nave para Marvin")
    print("5.- Mostrar naves")
    print("6.- Para salir del programa")
    opcion = int(input("Ingrese la opcion deseada: "))

    if opcion != 6 and opcion != 5:
        print("------CREACION DE NAVE---------")

        tipo_comustible = input('Tipo de combustible: ')
        peso_nave = input('Peso en toneladas: ')
        pais_from = input('Pais de origen: ')

    if opcion == 1:

        carga_util = input("Peso de la carga util: ")
        tipo_carga = input("Que tipo de carga lleva: ")

        nombre_nav = Lanzadora(carga_util, tipo_carga, tipo_comustible, peso_nave, pais_from)
        nombre_nav.enviar_dato()
        nombre_nav.elevarse()
        nombre_nav.explota()
        nombre_nav.soltar_carga()
        nombre_nav.insertar()

        print("\n")

        print("------Se termino la nave lanzadora-------")

    elif opcion == 2:
        cuerpo_estudio = input("Cuerpo de estudio: ")
        en_orbita = input("Esta en orbita: ")

        nombre_nav = Notripulado(cuerpo_estudio, en_orbita, tipo_comustible, peso_nave, pais_from)
        nombre_nav.enviar_dato()
        nombre_nav.elevarse()
        nombre_nav.explota()
        nombre_nav.insertar()
        print("\n")
        print("------Se termino la nave no tripulada-------")

    elif opcion == 3:
        capacidad_tripu = input("Capacidad de tripulantes: ")
        destino = input("Su destino: ")
        mision_tripu = input("Mision a realiza: ")

        nombre_nav = Tripulado(capacidad_tripu, destino, mision_tripu, tipo_comustible, peso_nave, pais_from)
        nombre_nav.enviar_dato()
        nombre_nav.elevarse()
        nombre_nav.explota()
        nombre_nav.acople()
        nombre_nav.insertar()

        print("\n")
        print("------Se termino la nave tripulada-------")

    elif opcion == 4:
        planetaorigen = input("Introdusca el planeta de origen: ")
        planetadestino = input("Introduzaca planeta destino: ")

        nombre_nav = NaveMarvin(planetaorigen, planetadestino, tipo_comustible, peso_nave, pais_from)
        nombre_nav.enviar_dato()
        nombre_nav.elevarse()
        nombre_nav.abduccion()
        nombre_nav.explota()
        nombre_nav.insertar()

        print("\n")
        print("------Se termino la nave de Marvin-------")

    elif opcion == 5:

        print("-----------------Filtrar por----------------")
        print("a.- Pais")
        print("b.- Tipo de combustible" )
        print("c.- Peso")
        print("d.- Tipo de nave")
        buscar = input("Buscar: ")

        if buscar == "a":
            pais = input("Pais a buscar: ")
            repo.search({"pais": pais})

        elif buscar == "b":
            tipo_combus = input("Que combustible usa: ")
            repo.search({"combustible": tipo_combus})

        elif buscar == "c":
            peso = input("Peso de la nave: ")
            repo.search({"peso": peso})

        elif buscar == "d":
            nave = input("Tipo de nave: ")
            repo.search({"nave": nave})