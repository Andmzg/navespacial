from Lazadora import *
from No_Tripulados import *
from Tripulados import *

ciclo = 0
while ciclo != 4:

    print("1.- Crear nave lanzadora")
    print("2.- Crear nave No tripulada")
    print("3.- Crear nave tripulada")
    print("4.- Para salir del programa")
    ciclo = int(input("Ingrese la opcion deseada: "))

    print("------CREACION DE NAVE---------")
    nombre_nav = input('Nombre de la nave: ')
    tipo_comustible = input('Tipo de combustible: ')
    peso_nave = input('Peso: ')
    pais_from = input('Pais de origen: ')


    if ciclo == 1:

        carga_util = input("Peso de la carga util: ")
        tipo_carga = input("Que tipo de carga lleva: ")
        nombre_nav = Lanzadora(carga_util, tipo_carga, tipo_comustible, peso_nave, pais_from)

        nombre_nav.encender_motor("encendido")
        nombre_nav.soltar_carga()
        print("------Se termino la nave lanzadora-------")

    elif ciclo == 2:
        cuerpo_estudio = input("Cuerpo de estudio: ")
        en_orbita = input("Esta en orbita: ")

        nombre_nav = no_tripulado(cuerpo_estudio, en_orbita, tipo_comustible, peso_nave, pais_from)
        nombre_nav.datos_tierra()
        print("------Se termino la nave no tripulada-------")

    elif ciclo == 3:
        capacidad_tripu = input("Capacidad de tripulantes: ")
        destino = input("Su destino: ")
        mision_tripu = input("Mision a realiza: ")

        nombre_nav = tripulado(capacidad_tripu, destino, mision_tripu, tipo_comustible, peso_nave, pais_from)
        nombre_nav.acople()

        print("------Se termino la nave tripulada-------")
