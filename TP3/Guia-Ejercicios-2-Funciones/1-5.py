def caracteres(nombre):
    print(nombre,"=",len(nombre))
    
    return len(nombre)

nombre1 = input("Ingrese un nombre: ")
n1 = caracteres(nombre1)
nombre2 = input("Ingrese otro nombre: ")
n2 = caracteres(nombre2)


if n1>n2:
    print("El string",nombre1,"tiene mas caracteres")
elif n1<n2:
    print("El string",nombre2,"tiene mas caracteres")

'''Confeccionar una función que le enviemos como parámetro un string y nos
retorne la cantidad de caracteres que tiene. En el bloque principal solicitar la carga
de dos nombres por teclado y llamar a la función dos veces. Imprimir en el bloque
principal cual de las dos palabras tiene más caracteres.'''