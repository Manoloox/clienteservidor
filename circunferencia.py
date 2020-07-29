"""
Nombre: Circunferencia.py
Objetibo: Permite calcular el area de una circunferencia
Autor: Manuel Salvador Vázquez Lara Castellanos
Fecha: 28 de Julio de 2020
"""
# Importamos libreria math
import math as m

#-------------------------------------
# Función para calcular área
#-------------------------------------
def calcularArea(valorRadio):
	return m.pi*m.pow(valorRadio,2)

# Módulo principal
def main():
	ciclo = 'S'
	while ciclo == 'S' or ciclo == 's':
		print("--- Prgrama para calcular Área de circunferencia ---")
		vradio = int(input("Introduce valor de radio. "))
		print("El área de la circunferencia con radio igual a:{},es: {}".format(vradio, calcularArea(vradio)))
		ciclo = input("¿otro cálculo (s/n)?")
	else:
		print("*** Fin del programa")

if __name__ == "__main__":
	main()
