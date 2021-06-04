def cargar():
    diccionario = {}
    for x in range(3):
        lista = []
        fecha = int(input("Ingrese una fecha: "))
        for x in range(3):
            hora = input("Ingrese una hora: ")
            actividad = input("Ingrese una actividad: ")
            lista.append(hora+"->"+actividad)
        diccionario[fecha] = lista
    
    return diccionario

def mostrar(diccionario):
    print(diccionario)

def busqueda(diccionario,fecha):
    if fecha in diccionario:
        print(fecha,":",diccionario[fecha])

diccionario = cargar()
mostrar(diccionario)
fecha = int(input("Ingrese una fecha para buscar las actividades: "))
busqueda(diccionario,fecha)

'''Confeccionar una agenda. Utilizar un diccionario cuya clave sea la fecha.
Permitir almacenar distintas actividades para la misma fecha (se ingresa la hora
y la actividad). Implementar las siguientes funciones:
1) Carga de datos en la agenda.
2) Listado completo de la agenda.
3) Consulta de una fecha.'''