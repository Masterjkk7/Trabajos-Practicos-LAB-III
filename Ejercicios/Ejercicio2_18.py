l1 = [ 1 ]
l2 = [ 2, 3 ]
l3 = [ 4, 5, 6 ]
l4 = [ 7, 8, 9, 10 ]
l5 = [ 11, 12, 13, 14, 15]
lista = [ l1, l2, l3, l4, l5 ]

print("Lista principal:",lista)

for x in lista:
    suma = 0
    for y in x:
        suma = suma + y
    print("Suma de lista:",x,"=",suma)

#2.18. Crear una lista por asignación. La lista tiene que tener 5 elementos. 
#Cada elemento debe ser una lista, la primera lista tiene que tener un elemento, 
#la segunda dos elementos, la tercera tres elementos y así sucesivamente. 
# Sumar todos los valores de las listas.