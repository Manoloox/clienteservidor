/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package clasesbásicas;

public class MainNomina {
    
    public static void main(String[] args){
        // Creamos un objeto de nomina
        Nomina n1 = new Nomina();
        // Crear un objeto con constructor sobrecargado
        Nomina n2 = new Nomina(1, "Lionel Messi", 3456.12f);

        System.out.println(n1.toString());
        System.out.println(n2.toString());

        n1.setClave(2);
        n1.setNombre("Cristiano Ronaldo");
        n1.setSueldo(234.56f);
        System.out.println(n1.toString());

    }
}