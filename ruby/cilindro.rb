        
    
    
    def getAltura()
        return @altura
    end  
    # Metodo Set
    def setAltura(cAltura)
        @a=cAltura
    end
end

# Definir el objeto cilindro
ca = Cilindro.new(10)
ca.setRadio(8)
puts "El area del cilindro es: #{ca.getArea(ca.getRadio())}"
puts "La altura del cilindro es: #{ca.getAltura())}"
puts "El volumen del cilindro es: #{ca.getArea(ca.getRadio())*ca.getAltura()}"