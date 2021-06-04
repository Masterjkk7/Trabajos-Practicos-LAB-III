mañana = []
tarde = []

print("Turno Manaña")

for x in range(4):
    flotante = float(input("Ingrese el sueldo del empleado:"))
    mañana.append(flotante)

print("Turno Tarde")

for x in range(4):
    flotante = float(input("Ingrese el sueldo del empleado:"))
    tarde.append(flotante)

print("Sueldos de la Mañana:",mañana)

print("Sueldos de la Tarde:",tarde)

#2.10. Una empresa tiene dos turnos (mañana y tarde) en los que trabajan 8 empleados
#(4 por la mañana y 4 por la tarde) Confeccionar un programa que permita almacenar
#los sueldos de los empleados agrupados en dos listas. Imprimir las dos listas de sueldos.