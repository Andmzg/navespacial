# d1 = {"Nombre": ["Sara", 27, 1003882]}
# print(d1)

def carga_en_catalogo():
  nombre_nav = input('Nombre de la nave: ')
  tipo_combustible = input('Tipo de combustible: ')
  peso_nave = input('Peso: ')
  pais_from = input('Pais de origen: ')

  L = [tipo_combustible, peso_nave, pais_from] #Valor diccionario
  A = {nombre_nav: L} #A = nombre del diccionario
  print(A)

  add(nombre_nav, L)

  print(A)


def add(llave, valor):
  llave = llave
  valor = valor

  print(llave)
  print(valor)

  valor.append("e")
  print(valor)

if __name__ == '__main__':
  carga_en_catalogo()




