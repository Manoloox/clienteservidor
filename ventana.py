"""
Nombre: ventana.py
Objetivo: Muestra como trabajar con ventanas gui en python y tkinter
Autor: Manuel Salvador Vázquez Lara Castellanos
Fecha: 29 de Julio de 2020
"""

# Importar las librerias de tkinter
from tkinter import *
from tkinter import ttk



# Funcion para enviar datos al servidor
def sendToServer():
	print("Enviado ...")


# Funcion main
def main():
	# Creamos la ventana como contenedora
	win = Tk()
	# Modificamos parametros de la ventana win
	win.geometry("400x400+200+20")
	win.title("Mi primer ventana en python Tkinter")

	# Creamos etiqueta
	label = ttk.Label(win, text="Texto a Enviar al servidor").pack(side=TOP)
	txtCampo = ttk.Entry(win).pack(side=TOP)

	# Creamos un boton para enviar el contenido de la propiedad text del entry al servidor
	ttk.Button(win, text="Enviar mensaje", command=sendToServer).pack(side=BOTTOM)

	# Creamos un boton y lo colocamos en la ventana
	ttk.Button(win, text="Salir", command=quit).pack(side=BOTTOM)

	# Hacemos ciclo para dibujar y esperar eventos
	win.mainloop()


# Para funcion main
if __name__ == "__main__":
	main()
