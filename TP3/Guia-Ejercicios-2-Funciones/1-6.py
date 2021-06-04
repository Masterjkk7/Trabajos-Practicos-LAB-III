def suma(lista):
    aux = 0
    for x in lista:
        aux = aux + x

    return aux

def mayor(lista):
    return max(lista)

def menor(lista):
    return min(lista)

lista = [1,2,3,4,5,6,7,8,9,10]

print("Suma =",suma(lista))
print("Mayor =",mayor(lista))
print("Menor =",menor(lista))

'''Definir por asignación una lista de enteros en el bloque principal del
programa. Elaborar tres funciones, la primera recibe la lista y retorna la suma de
todos sus elementos, la segunda recibe la lista y retorna el mayor valor y la última
recibe la lista y retorna el menor.'''