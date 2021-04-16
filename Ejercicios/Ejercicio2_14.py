lista = []

for x in range(5):
    entero = int(input("Ingrese un entero:"))
    lista.append(entero)

print("Lista de enteros:",lista)

mayor = max(lista)

print("Mayor elemento de la lista:",mayor)

ocurrencias = lista.count(mayor)

if ocurrencias >= 2:
    print("El elemento:",mayor,"se repite",ocurrencias,"veces")

#2.14. Cargar una lista con 5 elementos enteros. Imprimir el mayor y un mensaje si se 
#repite dentro de la lista (es decir si dicho valor se encuentra en 2 o más posiciones en la lista)