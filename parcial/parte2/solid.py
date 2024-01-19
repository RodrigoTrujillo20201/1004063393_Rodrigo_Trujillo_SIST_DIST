# FigurasGeometricas.py

from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def calcular_area(self):
        pass

class Cuadrado(FiguraGeometrica):
    def __init__(self, lado):
        super().__init__("Cuadrado")
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

class Triangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        super().__init__("Triángulo")
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

class Circunferencia(FiguraGeometrica):
    def __init__(self, radio):
        super().__init__("Circunferencia")
        self.radio = radio

    def calcular_area(self):
        return 3.1416 * self.radio ** 2


def ingresar_datos_cuadrado():
    lado = float(input("Ingrese el lado del cuadrado: "))
    return Cuadrado(lado)

def ingresar_datos_triangulo():
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    return Triangulo(base, altura)

def ingresar_datos_circunferencia():
    radio = float(input("Ingrese el radio de la circunferencia: "))
    return Circunferencia(radio)

def main():
    print("Seleccione la figura geométrica:")
    print("1. Cuadrado")
    print("2. Triángulo")
    print("3. Circunferencia")

    opcion = int(input("Ingrese el número de la opción: "))

    if opcion == 1:
        figura = ingresar_datos_cuadrado()
    elif opcion == 2:
        figura = ingresar_datos_triangulo()
    elif opcion == 3:
        figura = ingresar_datos_circunferencia()
    else:
        print("Opción no válida.")
        return

    area = figura.calcular_area()
    print(f"El área de la {figura.nombre} es: {area}")

if __name__ == "__main__":
    main()

#Parte 3: 
#proposisto de la Clase Base FiguraGeometrica y Principio de Abierto Cerrado OCP
#respuesta:
#La clase base FiguraGeometrica proporciona una estructura común para todas las figuras geométricas.
# Su propósito practicamente es definir atributos compartidos y un método abstracto para el cálculo del área. 
#al seguir el Principio de Abierto Cerrado, la clase base permite la extensión sin modificar su código. 
#Nuevas figuras pueden agregarse creando clases derivadas sin alterar la clase base.

##Agregar una Nueva Figura Geométrica hexagono Siguiendo OCP
##Para agregar un hexágono al sistema, se crea una nueva clase derivada de FiguraGeometrica llamada Hexagono 
#Esta clase implementaria el método calcular_area s3egún la fórmula  para un hexágono
#Siguiendo el Principio de Abierto/Cerrado (OCP), la clase base y otras clases derivadas no necesitarían modificaciones,
# manteniendo la independencia de las clases que ya existen.

