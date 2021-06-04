clave = input("Ingrese una clave: ")
contador = 0

for x in clave:
    contador = contador + 1

if contador >= 10 and contador <= 20:
    print("Su clave es valida")
else:
    print("Su clave no es valida porque tiene",contador,"caracteres")

#1.7. Solicitar el ingreso de una clave por teclado y almacenarla en una cadena de caracteres. 
# Controlar que el string ingresado tenga entre 10 y 20 caracteres para que sea válido, en caso 
# contrario mostrar un mensaje de error.