from Lazadora import *
tipo_nave = input("Escoga un tipo de nave: \n -lanzadora \n -no tripuladas \n -tripuladas \n >>>")

nombre_nav = input('Nombre de la nave: ')
tipo_comustible = input('Tipo de combustible: ')
peso_nave = input('Peso: ')
pais_from = input('Pais de origen: ')


if tipo_nave == "lanzadora":
    carga_util = input("Peso de la carga util: ")
    tipo_carga = input("Que tipo de carga lleva: ")
    nombre_nav = Lanzadora(carga_util, tipo_carga, tipo_comustible, peso_nave, pais_from)

    nombre_nav.encender_motor("encendido")
    nombre_nav.soltar_carga()

else:
    print("Exito")

