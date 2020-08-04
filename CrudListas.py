"""
Nombre: CrudListas.py
Objetivo: implementa las funciones crud en una lista en python
Author:
Fecha: 4 de Agosto de 2020
"""
# Declaramos una lista como variable global
lista = []


# Funcion para agregar elementos a la lista
def addElement():
    e = input("INgresa elemento: ")
    lista.append(e)
    print("Elemento agregado exitosamente")

    return

# Funcion para buscar elementos en la lista
def getElement():
    return

# Función para modificar elementos en la lista
def modifyElement():
    return

# Eliminar un elemento en la lista
def delElement():
    return

#Imprimir los elementos de la lista
def printElements():
    for i in lista:
        print("Elemento de la lista")

def dashboard():
    print("== Operaciones CRUD con lista en Python ==")
    print("1. Agregar elementos")
    print("2. Buscar elementos")
    print("3. Cambiar elementos")
    print("4. Eliminar elementos")
    print("5. Imprimir elementos")
    print("6. Salir")
    return

def main():
    ciclo = 'S'
    while ciclo == 'S' or ciclo == 's':

        dashboard()    
        ciclo = input("Seleccione una opcion entre 1 y 6: ")

        if ciclo == 1:
            # Invocar funcion para agregar elemento
            addElement()
        elif ciclo == 2:

    else:
        print("*** Fin del programa")


if __name__=="__main__":
    main()