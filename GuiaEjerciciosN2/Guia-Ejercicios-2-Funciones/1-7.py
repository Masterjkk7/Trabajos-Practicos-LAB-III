def lista():
    lista = []
    for x in range(5):
        lista.append(int(input("Ingrese un entero: ")))
    
    return lista

def mostrar(lista):
    print("Lista =",lista)
    print("Enteros de las lista > 10")
    for x in lista:
        if x>10:
            print(x)

mostrar(lista())

'''Confeccionar una función que cargue por teclado una lista de 5 enteros y la
retorne. Una segunda función debe recibir una lista y mostrar todos los valores
mayores a 10. Desde el bloque principal del programa llamar a ambas funciones.'''