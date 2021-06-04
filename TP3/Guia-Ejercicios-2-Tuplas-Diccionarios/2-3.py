def mostrar(diccionario):
    print(diccionario)

def caros(diccionario):
    print("Articulos con precio mayor a 100")
    for x in diccionario:
        if diccionario[x]>100:
            print(x,":",diccionario[x])

diccionario = {}
for x in range(5):
    producto = input("Ingrese un producto: ")
    precio = int(input("Ingrese su precio: "))
    diccionario[producto] = precio

mostrar(diccionario)
caros(diccionario)

'''Crear un diccionario que permita almacenar 5 artículos, utilizar como clave el
nombre de productos y como valor el precio del mismo.
Desarrollar además las funciones de:
1) Imprimir en forma completa el diccionario
2) Imprimir solo los artículos con precio superior a 100.'''