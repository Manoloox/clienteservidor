import java.rmi.Remote;
import java.rmi.RemoteException;


public interface Interfaz extends Remote{
    // Lista de metodos que integranlos servicios del objeto servidor
    int  sumar(int n1, int n2) throws RemoteException;
    int  restar(int n1, int n2) throws RemoteException;
    int  multiplicar(int n1, int n2) throws RemoteException;
    float  dividir(float n1, float n2) throws RemoteException;

    // Agregamos una nueva funcion
    float calculaArea(int n1) throws RemoteException;
    
}
