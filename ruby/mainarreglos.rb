# Cargar archivo de la clase punto
load "Arreglos.rb"

# Creamos un objeto de la clase Arreglos
vec = Arreglo.new()

# Reporte de elementos del arreglo
vec.printAll()

# Insertar un elemento
vec.insert("first")
vec.insert(12)
vec.insert(false)
vec.insert ("C")
vec.insert(12.45)
vec.printAll()

# Buscar elemento
vec.buscar(true)

# Borra elemento
vec.borrar(false)

# Modifica elemento
vec.cambiar(12, 2)
vec.printAll()