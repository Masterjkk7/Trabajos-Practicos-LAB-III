nombre = input("Ingrese su nombre en minusculas: ").lower()
vocales = 'aeiou'

if nombre[0] in vocales:
    print(nombre,"empieza con la vocal",nombre[0])
else:
    print(nombre,"no empieza con vocal")

#1.2. Solicitar la carga del nombre de una persona en minúsculas. Mostrar un mensaje si comienza con vocal dicho nombre.