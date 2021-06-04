def diccionario():
    diccionario = {}
    for x in range(5):
        nombre = input("Ingrese un nombre: ")
        edad = int(input("Ingrese una edad: "))
        diccionario[nombre] = edad
    
    print("Personas =",diccionario)

    print("Personas mayores a 18")
    for x in diccionario:
        if diccionario[x]>=18:
            print(x,"=",diccionario[x])
    
    return diccionario

def promedio(diccionario):
    suma = 0
    for x in diccionario:
        suma = suma + diccionario[x]
    
    promedio = suma/len(diccionario)
    print("Promedio de edades =",promedio)

promedio(diccionario())

'''Desarrollar un programa que permita cargar 5 nombres de personas y sus
edades respectivas. Luego de realizar la carga por teclado de todos los datos
imprimir los nombres de las personas mayores de edad (mayores o iguales a 18
años). Imprimir la edad promedio de las personas.'''