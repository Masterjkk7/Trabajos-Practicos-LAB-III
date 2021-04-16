lista = []

for x in range(5):
    entero = int(input("Ingrese un entero:"))
    lista.append(entero)

menor = lista[0]

print("Lista de enteros:",lista)

for x in lista:
    if x < menor:
        menor = x

print("Menor elemento de la lista:",menor)
print("Posicion del menor elemento:",lista.index(menor))

#2.12. Crear y cargar una lista con 5 enteros por teclado. Implementar un algoritmo 
#que identifique el menor valor de la lista y la posición donde se encuentra.