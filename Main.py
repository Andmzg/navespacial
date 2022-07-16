from Lazadora import Lanzadora
from  No_Tripulados import no_tripulado
from  Tripulados import tripulado


opcion = 0
while opcion != 4:

    print("1.- Crear nave lanzadora")
    print("2.- Crear nave No tripulada")
    print("3.- Crear nave tripulada")
    print("4.- Para salir del programa")
    opcion = int(input("Ingrese la opcion deseada: "))

    if opcion !=4:
        print("------CREACION DE NAVE---------")
        nombre_nav = input('Nombre de la nave: ')
        tipo_comustible = input('Tipo de combustible: ')
        peso_nave = input('Peso en toneladas: ')
        pais_from = input('Pais de origen: ')


    if opcion == 1:

        carga_util = input("Peso de la carga util: ")
        tipo_carga = input("Que tipo de carga lleva: ")

        nombre_nav = Lanzadora(carga_util, tipo_carga, tipo_comustible, peso_nave, pais_from)
        nombre_nav.soltar_carga()

        print("\n")

        print("------Se termino la nave lanzadora-------")

    elif opcion == 2:
        cuerpo_estudio = input("Cuerpo de estudio: ")
        en_orbita = input("Esta en orbita: ")

        nombre_nav = no_tripulado(cuerpo_estudio, en_orbita, tipo_comustible, peso_nave, pais_from)
        nombre_nav.enviar_dato()
        print("\n")
        print("------Se termino la nave no tripulada-------")

    elif opcion == 3:
        capacidad_tripu = input("Capacidad de tripulantes: ")
        destino = input("Su destino: ")
        mision_tripu = input("Mision a realiza: ")

        nombre_nav = tripulado(capacidad_tripu, destino, mision_tripu, tipo_comustible, peso_nave, pais_from)
        nombre_nav.acople()

        print("\n")
        print("------Se termino la nave tripulada-------")
