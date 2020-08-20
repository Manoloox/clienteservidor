"""
Nombre: diccionario.py
Objetivo: Muestra la operacion de los diccionarios en python
Author: Manuel Salvador Vazquez Lara Castellanos
Fecha: 5 de agosto de 2020
"""

# Un diccionario es una estructura de datos que almacena valores heterogeneos
# pero los almacena en un formato de clave:valor. Quiere decir que cada elemento 
# en el diccionario se almacena como una lista de pares key:valor.
# Por ejemplo: 'nombre':'Francisco Cervantes Zambrano'
# No son mutables,es decir que no cambian. Una vez que los creamos permanecerán
# con los mismos valores, no podremos introducir mas datos

def main():
    # Creamos un diccionario con distintos key y datos
    dic = {'clave': 20082133, 'nombre':'Erick José Verduzco Campos', 'edad':54, 'cursos':['Python', 'Progra Web', 'Inteligencia Artificial']}
    tec = {'carreras':['informatica','sistemas','administracion','ambiental'],'tipo_prof':['tiempoCompleto','medioTiempo']}
    # Listar items del diccionario
    print("Los items son: ", dic)
    # Imprimir un item de un diccionario proporcionando un key
    print("El valor de la key es: ", dic['nombre'])
    # Imprimir los valores de todos los keys del diccionario
    for i in dic:
        print(i, ":", dic[i])

    # En el caso de la lista incluida como item del diccionario, lo accesamos
    for i in dic['cursos']:
        print(i)

    # INVESTIGAR LOS METODOS DE LOS DICCIONARIOS Y CORRERLOS EN EL PROGRAMA
    # GET, POP, KEY, CLEAN, ITEMS, UPDATE

    # Key devuelve un verdadero si lo que se pide esta en el diccionario y un falso si no esta
    #print(dic.has_key["nombre"])
    #print("clave" in dic)
    
    # Key recorre todo el Diccionario
    for key in dic:
        print(key, ":", dic[key])

    # ITEMS Devuelve una lista de tuplas, cada tupla se compone de dos elementos: 
    #el primero será la clave y el segundo, su valor.
    print(dic.items())

    # get devuelve el valor del elemento que estamos indicando
    print(dic.get("nombre","No existe este elemento"))

    # pop deveuelve el valor del elemento que estamos borrando
    print(dic.pop("clave"))
    #del dic["clave"]
    #print(dic)

    # copy retorna una copia del diccionario original
    #dic2 = dic.copy()
    #print(dic2)

    # UPDATE Recibe como parámetro otro diccionario. 
    # Si se tienen claves iguales, actualiza el valor de la clave repetida; 
    # si no hay claves iguales, este par clave-valor es agregado al diccionario.
    dic.update(tec)
    print(dic)

    # Elimina todos los ítems del diccionario dejándolo vacío.
    dic.clear()
    print(dic)

    

if __name__=="__main__":
    main()