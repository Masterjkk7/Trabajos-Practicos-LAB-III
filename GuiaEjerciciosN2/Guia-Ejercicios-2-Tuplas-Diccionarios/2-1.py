def cargar():
    lista = []
    for x in range(5):
        pais = input("Ingrese un pais: ")
        habitantes = int(input("Ingrese su cantidad de habitantes: "))
        tupla = (pais,habitantes)
        lista.append(tupla)

    return lista

def imprimir(lista):
    print("Lista de paises =",lista)

def mayor(lista):
    mayor = lista[0][1]
    posicion = 0
    contador = 0
    for x in lista:
        if x[1]>mayor:
            mayor = x[1]
            posicion = contador

        contador = contador + 1 

    print(lista[posicion][0],"es el pais con mayor cantidad de habitantes, con un total de:",lista[posicion][1])

lista = cargar()
imprimir(lista)
mayor(lista)

'''Almacenar en una lista de 5 elementos tuplas que guarden el nombre de un
pais y la cantidad de habitantes. Definir tres funciones, en la primera cargar la
lista, en la segunda imprimirla y en la tercera mostrar el nombre del país con
mayor cantidad de habitantes.'''