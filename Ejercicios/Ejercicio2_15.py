lista = []

for x in range(5):
    flotante = float(input("Ingrese un sueldo:"))
    lista.append(flotante)

print("Lista de sueldos:",lista)

mayor = max(lista)

print("Mayor sueldo:",mayor)

lista.append(lista.pop(lista.index(mayor)))

print("Lista modificada:",lista)

#2.15. Se debe crear y cargar una lista donde almacenar 5 sueldos. Desplazar el valor 
# mayor de la lista a la última posición.