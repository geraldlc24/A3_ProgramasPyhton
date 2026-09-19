package Sesion05_Ejemplo_TDA_VECTOR;
import java.util.Arrays;
import java.util.Scanner;

class TDAVectorEspecial {
	Scanner entrada = new Scanner(System.in);

	//punto 1
	private byte datos[];
	
	//punto 2
	public void crearVector() {
			System.out.println("Cuantos elementos deseas ingresar:  ");
			int tam = entrada.nextInt();
			datos = new byte [tam];
			
			System.out.println("--Deberas llenar el vector a continuacion--");
			llenarDatos();
			
	}

	//punto 3
	public void llenarDatos() {
		Scanner entrada = new Scanner(System.in);
		for (int i=0; i<datos.length; i++) {
			System.out.println("Ingresar valor "+ (i+1) + ": ");
			datos [i] = entrada.nextByte();
			
		}
			
		}
	}


public class PruebaVectorEspecial {
	public static void main(String[] args) {
		
		/*int []cal = new int [10];
		 
		 String nombres[] = new String[5];
		 
		 System.out.println(Arrays.toString(cal));
		 
		 System.out.println(Arrays.toString(nombres));
		 
		 char c[] = new char[20];
		 System.out.println(Arrays.toString(c));*/
		
		
	}

}
