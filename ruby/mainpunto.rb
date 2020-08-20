# Cargar archivo de la clase punto
load "punto.rb"


# Crear un objeto de la clase punto y llamar a sus metodos
pa = Punto.new(0,0)
pb = Punto.new(10,10)

# Imprimimos atributos
puts "Coordenadas del punto pa: #{pa.getX()}, #{pa.getY()}"
puts "Coordenadas del punto pb: #{pb.getX()}, #{pb.getY()}"