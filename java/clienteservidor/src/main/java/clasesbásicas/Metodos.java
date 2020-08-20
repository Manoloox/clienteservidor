/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package clasesbásicas;

public class Metodos {
    
    public Metodos()
    {

    }

    private static void mensaje(){
        System.out.println("Hola soy un metodo estatico");
    }

    private int suma(int n1, int n2){
        return n1+n2;
    }

    private int resta(int n1, int n2){
        return n1-n2;
    }

    private int multiplicacion(int n1, int n2){
        return n1*n2;
    }

    private float divide(int n1, int n2){
        float res;
        res = (float)n1/(float)n2;
        return res;
    }

    public static void main(String [] args){
        Metodos op = new Metodos();
        System.out.println("La suma es: "+ op.suma(4,5));
        System.out.println("La resta es: "+ op.resta(4,5));
        System.out.println("La multiplicacion es: "+ op.multiplicacion(4,5));
        System.out.println("La division es: "+ op.divide(4,5));
        mensaje();
    }

}