"""
Nombre: listas.py
Objetivo: Muestra la función de las listas en python
Author:
Fecha: 4 de agosto de 2020
"""

def main():
    # Una lista es una estructura de datos en python
    # La ventaja aceptan datos de tipos distintos
    # Creamos una lusta
    lista = [1, 23.01, False, "hola lista", 'A', [-1, -5, "hola", 0.0], -12, 'A']
    # Lista vacia
    listaVacia = []
    # Accesando elementos de la lista 
    # Imprimimos los elementos de la lista
    for elemento in lista:
        print("El elemento de la lista es: ", elemento)
    for i in listaVacia:
        print("El elemento de la lista vacia es: ", i)

    # Imprimir un elemento de la lista
    print("Elemento de la posición 3: ", lista[3])
    print("Elemento de la posición -5: ", lista[-5])
    print(lista[-2])
    print(lista[5])
    # Leer el elemento en la posición 2 de la lista interna
    print(lista[5][-1])

    # Metodos de las listas
    lista.append("El maestro no sabe...")
    for elemento in lista:
        print("El elemento de la lista es: ", elemento)

    # Count regresa el numero de veces que se repite un elemento en la lista
    print("Elemento se repite : ", lista.count("pelonchas"))

    # index() imprime el indice de un elemento en la lista
    print("La posición de False es: ", lista.index(False))

    # Eliminar elemento de la lista: remove()
    lista.remove("A")
    for x in lista:
        print("El elemento de la lista es: ", x)

if __name__=="__main__":
    main()