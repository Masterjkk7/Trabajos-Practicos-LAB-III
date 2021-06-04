def mostrar(diccionario):
    print(diccionario)
    for x in diccionario:
        print(x,":",diccionario[x])

diccionario = {}
for x in range(5):
    pais = input("Ingrese un pais: ")
    habitantes = int(input("Ingrese su cantidad de habitantes: "))
    diccionario[pais] = habitantes

mostrar(diccionario)

'''En el bloque principal del programa definir un diccionario que almacene los
nombres de paises como clave y como valor la cantidad de habitantes.
Implementar una función para mostrar cada clave y valor.'''