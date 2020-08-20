# Clase para el manejo de arreglos en ruby

class Arreglo
    
    # Método constructor
    def initialize()
        # Crear un arreglo vacio
        @vector = []
    end

    # Insertar elemento en el arreglo
    def insert(elem)
        @vector.push(elem)
    
    end

    # Buscar un elemento dentro del arreglo 
    def buscar(elem)

        @vector.each_with_index do |elemento, index|
           if elemento == elem
                puts "El elemento buscado es:[#{index}]=#{elemento}"
                return index
           # Verificamos que estamos al final del arreglo y no encontramos el elemnto
           elsif (elemento != elem) && (index+1 == @vector.length)
                puts "El elemento que buscas no existe #{elem}"
                return -1
           end
        end

    end

    # Cambiar elemento
    def cambiar(elem, elem_new)
        # Buscamos elemento y obtenemos su posición en el arreglo
        puntero = buscar(elem)
        if ( puntero >=0)
            # Elemento existe y lo modificamos
            @vector[puntero]=elem_new
            puts "Elemento modificado..."
        else
            puts "Nada se modifico..."
        end
    end

    # Borrar elemento
    def borrar(elem)
        # Buscamos elemento y obtenemos su posición en el arreglo
        puntero = buscar(elem)
        if ( puntero >=0)
            @vector.delete_at(puntero)
            puts "Elemento borrado #{elem}..."
        else
            puts "Nada se borró #{elem}..."
        end
    end

    # Imprime todos los elementos del arreglo
    def printAll()
        if @vector.length > 0
            @vector.each_with_index do |elemento, index|
                puts "Elemento[#{index}]=#{elemento}"
            end
        else
            puts "El arreglo esta vacio"
        end
    end
end
