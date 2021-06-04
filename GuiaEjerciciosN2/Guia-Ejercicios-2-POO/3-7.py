class Operacion():
    def __init__(self):
        self.valor1 = 0
        self.valor2 = 0
        self.resultado = 0
    
    def cargar1(self):
        self.valor1 = int(input("Ingrese el primer valor: "))
    
    def cargar2(self):
        self.valor2 = int(input("Ingrese el segundo valor: "))
    
    def operar(self, operando):
        if operando == "+":
            self.resultado = self.valor1+self.valor2
        elif operando == "-":
            self.resultado = self.valor1-self.valor2
    
    def mostrar_resultado(self):
        print("Resultado =",self.resultado)

o=Operacion()

opcion = 0

while opcion != 3:
    print("1) Sumar valores")
    print("2) Restar valores")
    print("3) Salir del programa")
    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        o.cargar1()
        o.cargar2()
        o.operar("+")
        o.mostrar_resultado()
    elif opcion == 2:
        o.cargar1()
        o.cargar2()
        o.operar("-")
        o.mostrar_resultado()
    elif opcion == 3:
        print("Cerrando el programa...")


'''Supongamos que necesitamos implementar dos clases que llamaremos
Suma y Resta. Cada clase tiene como atributo valor1, valor2 y resultado. Los
métodos a definir son cargar1 (que inicializa el atributo valor1), carga2 (que
inicializa el atributo valor2), operar (que en el caso de la clase "Suma" suma los
dos atributos y en el caso de la clase "Resta" hace la diferencia entre valor1 y
valor2), y otro método mostrar_resultado. Si analizamos ambas clases
encontramos que muchos atributos y métodos son idénticos. En estos casos es
bueno definir una clase padre que agrupe dichos atributos y responsabilidades
comunes.'''