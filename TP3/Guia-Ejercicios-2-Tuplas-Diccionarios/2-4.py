def cargar():
    diccionario = {}
    for x in range(5):
        ingles = input("Ingrese una palabra en ingles: ")
        castellano = input("Ingrese su traduccion: ")
        diccionario[ingles] = castellano
    
    return diccionario

def mostrar(diccionario):
    print(diccionario)

def busqueda(diccionario,palabra):
    if palabra in diccionario:
        print(palabra,"=",diccionario[palabra])

diccionario = cargar()
mostrar(diccionario)
palabra = input("Ingrese una palabra para buscar su traduccion: ")
busqueda(diccionario,palabra)

'''Desarrollar una aplicación que nos permita crear un diccionario
ingles/castellano. La clave es la palabra en ingles y el valor es la palabra en
castellano.
Crear las siguientes funciones:
1) Cargar el diccionario.
2) Listado completo del diccionario.
3) Ingresar por teclado una palabra en ingles y si existe en el diccionario mostrar
su traducción.'''