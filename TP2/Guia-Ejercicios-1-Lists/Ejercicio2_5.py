lista = ["Franco","Facundo","Zarya","Freud","Link"]
contador = 0

print("Nombres:",lista)

for x in lista:
    if len(x) >= 5:
        contador = contador + 1 
        
print(contador,"nombres de la lista tienen 5 o mas caracteres")
#2.5. Definir una lista que almacene por asignación los nombres de 5 personas. Contar cuantos de esos nombres tienen 5 o más caracteres.