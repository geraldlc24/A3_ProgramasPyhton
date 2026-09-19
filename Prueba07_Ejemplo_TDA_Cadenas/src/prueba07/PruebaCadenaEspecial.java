package prueba07;

public class PruebaCadenaEspecial {

	public static void main(String[] args) {
		
		
		System.err.println("El problema de las cades creadas con STRIN es la inmutabilidad");
		//El problema de las cadenas creadas con STRING es la INMUTABILIDAD
	
		
		int iteraciones = 1000000;
		
		long tiInicio = System.currentTimeMillis();
		String texto = "";
		for (int i=0; i<iteraciones; i++); {
			texto += "S";
			
	}

	long tFin = System.currentTimeMillis();
	long tiempoTranscurrido = tFin - tiInicio;
	System.out.printf("Tiempo transcurrido:  %d milisegundos \n", tiempoTranscurrido);
	
	
	System.out.println("Para MODIFICAR CADENAS sin impacto en la memoria");
	System.out.println("por la INMUTABILIDAD de String, se recomienda utilizar" + "StringBuilder o StringBuffer");
	
	
	tiInicio = System.currentTimeMillis();
	StringBuilder sb = new StringBuilder();
	for(int i=0; i<iteraciones; i++) {
		sb.append("S");
	}
	tFin = System.currentTimeMillis();
	tiempoTranscurrido = tFin - tiInicio;
	System.out.printf("Tiempo transcurrido: %d milisegundos \n", tiempoTranscurrido);
	
	}
}
