"""
Nombre: MainCircunferencia.py
Objetivo: Muestra como trabajar con multiples archivos en python
Autor: Manuel Salvador Vázquez Lara Castellanos
Fecha: 30 de julio de 2020
"""
from Circunferencia import Circunferencia

class Cilindro(Circunferencia):

    #definimos el constructor
    def __init__(self, valorX, valorY, valorRadio, valorAltura):
        # Constructor de Circunferencia
        Circunferencia.__init__(self,valorX, valorY,valorRadio)
        # Constructor de Cilindro
        self.altura = valorAltura

    def getAltura(self):
        return self.altura

    def setAltura(self, valorAltura):
        self.altura = valorAltura

    def getVolumen(self):
        return self.getArea() * self.altura

    def toString(self):
        return Circunferencia.toString(self)+" y la altura es :"+str(self.altura) + " y el volumen es:"+str(self.getVolumen())
