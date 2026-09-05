'''
Created on 24 ago 2026

@author: dell
'''
'''
   FUNDAMENTOS DE PROGRMACION
   1.Casi todo el codigo debe de ir alineado a la izquierda, excepto
   estructuras de control y otras rutinas que se especifiquen 
   con CUATRO ESPACIOS
   2. Los espacios en la parte izquierda del codigo son SINTACTICOS
   3. No lleva punto y coma al final de cada linea
   4. Tipos de datos e Identificadores (VARIABLES)
  
        Python es de TIPADO DINAMICO (Se refiere el tipo de dato al momento 
                                      de asignar su valor)
  
                                      Ejemplo en JAVA (tipado estatico)
                                        boolean sensor;
                                        byte edad => 1 byte
                                        int dato; => 4 bytes
                                        
                                        
                                      En PYTHON;
                                         edad = 45;
                                         
                                    TIPOS DE DATOS EN PYTHON
                                            BASICOS
                                                int
                                                float
                                                bool
                                                str
                                                
                                            COMPUESTAS
                                                list
                                                tuple
                                                Dictionary
                                                
                                    FUNCIONES de conversion
                                        Cadena a entero => int()
                                        Cadena a real => float ()
                                        Cadena a booleano => bool()
                                        
                                        De cualquier tipo a Cadena => str()
                                        
                                                
'''
print ("--------TIPOS DE DATOS--------")
edad = 45
temperatura_sensor = 34.67
nombre = "Luke Skywalker"
encendido = False

edad = "MARIA"
print (type(edad))
       
       
print ("--------------Depradores aritmeticos---------")

a = 357
b = 67


print(a+b)
print(a-b)
print(a*b)
print(a/b)

print(a%b)
print(a//b)

print("---------LECTURA DESDE TECLADO--------")
anioNac = int(input("Ingresa tu anio de nacimiento:  "))

print ("Edad de una persona con base a su anio de nacimiento")
#anioNac = 2000
edad = 2026 - anioNac
print(f"Hola {nombre}, Tu edad es: {edad} anios")