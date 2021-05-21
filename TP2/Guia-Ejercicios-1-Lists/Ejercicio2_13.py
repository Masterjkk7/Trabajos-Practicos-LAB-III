lista = []

for x in range(5):
    nombre = input("Ingrese un nombre:")
    lista.append(nombre)

print("Lista de nombres:",lista)

lista_ordenada = sorted(lista)

print("Lista de nombres orenada alfabeticamente:",lista_ordenada)

print("Primer nombre:",lista_ordenada[0])

#2.13. Ingresar por teclado los nombres de 5 personas y almacenarlos en una lista. 
#Mostrar el nombre de persona menor en orden alfabético.