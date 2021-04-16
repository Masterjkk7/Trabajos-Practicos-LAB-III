oracion = input("Ingrese una oracion: ")
oracion_minusuclas = oracion.lower()
vocales = 'aeiou'
contador = 0

for x in oracion_minusuclas:
    if x in vocales:
        contador = contador + 1

print("La oracion ingresada contiene",contador,"vocales")

#1.6. Ingresar una oración que pueden tener letras tanto en mayúsculas como minúsculas. 
# Contar la cantidad de vocales. Crear un segundo string con toda la oración en minúsculas 
# para que sea más fácil disponer la condición que verifica que es una vocal.