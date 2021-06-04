class Punto():
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y
    
    def __str__(self):
        cadena="("+str(self.x)+";"+str(self.y)+")"
        return cadena
    
    def cuadrante(self):
        if self.x>0 and self.y>0:
            return 1
        elif self.x<0 and self.y>0:
            return 2
        elif self.x<0 and self.y<0:
            return 3
        elif self.x>0 and self.y<0:
            return 4

p1=Punto(1,1)
p2=Punto(-1,1)
p3=Punto(-1,-1)
p4=Punto(1,-1)

print("El punto",p1,"se ecuentra en el",p1.cuadrante(),"cuadrante")
print("El punto",p2,"se ecuentra en el",p2.cuadrante(),"cuadrante")
print("El punto",p3,"se ecuentra en el",p3.cuadrante(),"cuadrante")
print("El punto",p4,"se ecuentra en el",p4.cuadrante(),"cuadrante")


'''Desarrollar una clase que represente un punto en el plano y tenga los
siguientes métodos: inicializar los valores de x e y que llegan como parámetros,
imprimir en que cuadrante se encuentra dicho punto (concepto matemático,
primer cuadrante si x e y son positivas, si x<0 e y>0 segundo cuadrante, etc.).'''