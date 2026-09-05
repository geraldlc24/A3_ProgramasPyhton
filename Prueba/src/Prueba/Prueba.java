package Prueba;
import java.util.*;
public class Prueba {


	public static void main(String[] args) {
		int N = 100;
		int[] categorias = new int[7];
		
		for (int i = 0; i < N; i++) {
			double num = Math.random();
			
			
			String s = String.valueOf(num).substring(2, 7);
			int tipo = clasificar(s);
			categorias[tipo]++;
			
			
		}
		
		String[] nombres = {
				"Todos diferentes", "un par", "Dos pares",
				"Tercia", "Full", "Poker", "Quintilla"
		};
		
		System.out.println("Frecuencias Observadas");
		for (int i = 0; i < categorias.length; i++) {
			System.out.println(nombres[i] + ":  " + categorias [i]);
			
		}
double [] probabilidades = {
		0.3024, // todos diferentes
		0.5040, // un par
		0.1080, // dos pares
		0.0720, // tercia
		0.0090, // full
		0.0045, // poker
		0.0001  // quintilla
};
	double chi = 0;
for (int i = 0; i < categorias.length; i++) {
	
	double esperado = N * probabilidades[i];
	chi += Math.pow(categorias [i] - esperado, 2) /esperado;
	
}
System.out.println("Chi - cuadrada:  " +chi);

}
 public static int clasificar(String s) {
	 int []conteo = new int[10];
	 for (char c : s.toCharArray()) {
		 conteo[c - '0']++;
		 
	 }
	 
	 Arrays.sort(conteo);
	 
	 if (conteo [9] == 5) return 6; // Quintilla
	 if (conteo [9] == 4) return 5; // Poker
	 if (conteo [9] == 3 && conteo[8]== 2) return 4; //Full
	 if (conteo [9] == 3) return 3; //Tercia
	 if (conteo [9] == 2 && conteo[8]== 2) return 2; //Dos pares
	 if (conteo [9] == 2) return 1; //Un par
	return 0; // todos diferentes
 }






}


	