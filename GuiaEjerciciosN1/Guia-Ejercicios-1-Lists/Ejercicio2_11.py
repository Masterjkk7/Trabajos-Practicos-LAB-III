lista = []

for x in range(5):
    entero = int(input("Ingrese un entero:"))
    lista.append(entero)

mayor = lista[0]

print("Lista de enteros:",lista)

for x in lista:
    if x > mayor:
        mayor = x

print("Mayor elemento de la lista:",mayor)

#2.11. Crear y cargar una lista con 5 enteros. Implementar un algoritmo que identifique el mayor valor de la lista.