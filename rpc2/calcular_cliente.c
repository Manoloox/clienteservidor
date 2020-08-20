#include "calcular.h" 
int main (int argc, char **argv) 
{     

    
    char *host;     CLIENT *sv;     

    int *resS, *resR, *resM;
    float *resD, *areaC;
    int *res;     if (argc!=2)         
    printf("Uso: %s  <host>\n", argv[0]);     
    else       
    {         
        host = argv[1];         
        sv = clnt_create(host, CALCULAR, UNO, "tcp");         
        if (sv != NULL)           
        {             
            resS = sumar_1(5, 2, sv);   
            resR = restar_1(5, 2, sv);  
            resM = multiplicar_1(5, 2, sv);  
            resD = dividir_1(5, 2, sv);  
            areaC = areacircunferencia_1(2.33, sv); 

            if (res != NULL)             
            {               
                printf("El servidor envio estos datos ....\n"); 
                printf("5 + 2 = %d\n", *resS);   
                printf("5 + 2 = %d\n", *resR); 
                printf("5 + 2 = %d\n", *resM); 
                printf("5 + 2 = %d\n", *resD); 
                printf("El area de la circunferencia de 2.33 es: %d\n", *areaC); 
            }             
            else             
            {                
                clnt_perror(sv, "error en RPC");             
            }             
            clnt_destroy(sv);           
            }         
            else           
            {             
                clnt_pcreateerror(host);           
        }       
    }    
                return(0);
}