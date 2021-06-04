def capicua(palabra):
    bool = True
    if palabra!=palabra[::-1]:
        bool = False

    return bool

palabra = input("Ingrese una palabra: ")
if capicua(palabra)==True:
    print("La palabra es capicua")
else:
    print("La palabra no es capicua")

'''Confeccionar una función que reciba una palabra y verifique si es capicúa (es
decir que se lee igual de izquierda a derecha que de derecha a izquierda).'''