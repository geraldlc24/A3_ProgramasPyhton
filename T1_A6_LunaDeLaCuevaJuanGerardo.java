package prueba07;
import java.util.Scanner;


public class Aspirante {
	private static String[] nombre;
	private static String[] PrimerAp;
	private static String []SegundoAp;
	private static int [] edad;
	private static String[] direccion;
	private static String[] telefono;
	private static String [] correo;
	private static String[] redesSociales;
	private static String[] carrerasInteres;
	private static String[] escuelaProcedencia;
	private static String[] bachillerato;

		public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		System.out.println("==================================");
		System.out.println("       FICHAS DE INGRESO ISC"); 
		System.out.println("=================================="); 
		System.out.print("Cuantos aspirantes desea ingresar: "); 
		int cantidad = sc.nextInt(); 
		sc.nextLine();
		
		nombre = new String[cantidad]; 
		PrimerAp = new String[cantidad]; 
		SegundoAp = new String[cantidad]; 
		edad = new int[cantidad]; 
		direccion = new String[cantidad]; 
		telefono = new String[cantidad]; 
		correo = new String[cantidad]; 
		redesSociales = new String[cantidad]; 
		carrerasInteres = new String[cantidad];
		escuelaProcedencia = new String[cantidad];
		bachillerato = new String[cantidad];
	
	for (int i = 0; i < cantidad; i++) {
	System.out.println("\n--- ASPIRANTE " + (i + 1) + " ---");
	System.out.print("Nombre: ");
	nombre [i] = sc.nextLine();
	
	System.out.println("Primer Apellido:");
	PrimerAp[i] = sc.nextLine();
	
	System.out.println("Segundo Apellido:");
	SegundoAp[i] = sc.nextLine();
	
	System.out.print("Edad: "); 
	edad [i] = sc.nextInt();
	
	sc.nextLine(); 
	System.out.print("Direccion: ");
	direccion[i] = sc.nextLine();
	
	System.out.print("Telefono: ");
	telefono [1] = sc.nextLine(); 
	
	System.out.print("Redes sociales: ");
	redesSociales[i] = sc.nextLine(); 
	
	System.out.print("Carrera de interes: ");
	carrerasInteres[i] = sc.nextLine();
	
	System.out.print("Escuela de procedencia: "); 
	escuelaProcedencia[i] = sc.nextLine();
	
	System.out.print("Bachillerato: ");
    bachillerato[i] = sc.nextLine();
	}
	
	System.out.println("\n\n=================================="); 
	System.out.println(" FICHAS DE INGRESO ISC");
	System.out.println("=================================="); 
	for (int i = 0; i < cantidad; i++) {
		
		System.out.println("\nFicha de ingreso: " + String.format("%03d", i + 1));
		System.out.println("======================");
		System.out.println("Nombre: " + nombre[i]); 
		System.out.println("Primer Apellido: " + PrimerAp[i]);
		System.out.println("Segundo Apellido: " + SegundoAp[i]);
		System.out.println("Edad: " + edad[i] + " años");
		System.out.println("Direccion: " + direccion[i]); 
		System.out.println("Telefono: " + telefono[i]); 
		System.out.println("Correo electronico: " + correo[i]); 
		System.out.println("Redes Sociales: " + redesSociales[i]); 
		System.out.println("Carrera(s) de interes: " + carrerasInteres[i]); 
		System.out.println("Escuela de procedencia: " + escuelaProcedencia[i]);
		System.out.println("Bachillerato cursado: " + bachillerato[i]); 
		} 
	sc.close(); 
	} 
	}	
	
		

	
	


