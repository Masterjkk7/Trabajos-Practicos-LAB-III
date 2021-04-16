lista = [101,20,357,777,50,63,932,81]
contador = 0

print("Numeros:",lista)

for x in lista:
    if x > 100:
        contador = contador + 1

print("Esta lista tiene",contador,"elementos que superan el valor 100")

#2.4. Definir por asignación una lista con 8 elementos enteros. Contar cuantos de dichos valores almacenan un valor superior a 100.