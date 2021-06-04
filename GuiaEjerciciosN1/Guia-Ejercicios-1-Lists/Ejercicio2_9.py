lista = []
suma = 0
promedio = 0

for x in range(5):
    flotante = float(input("Ingrese una altura de una persona:"))
    lista.append(flotante)
    suma = suma + flotante

promedio = suma/5

print("Alturas:",lista)
print("Promedio:",promedio)

for x in lista:
    if x > promedio:
        print(x,"esta sobre el promedio")
    elif x == promedio:
        print(x,"es igual al promedio")
    else:
        print(x,"esta por debajo del promedio")

#2.9. Obtener el promedio de las mismas. Contar cuántas personas son más altas que el
#promedio y cuántas más bajas.