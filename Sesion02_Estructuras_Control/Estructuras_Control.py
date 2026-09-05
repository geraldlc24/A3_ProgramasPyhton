'''
Created on 31 ago 2026

@author: dell
'''


print ("---------ESTRUCTURAS DE CONTROL-------")

if (True):
    print("Siempre")

if (False):
    print("Nunca")
    
a = 324
b = 43
c = 78

if (a>b and c!=a and b>c) :
    print ("Si entra")
else:
    print("No entra")
    
if a>b and c!=a and b>c :
    print ("Si entra")
else :
    print("No entra")






print("\n\n----------CICLO FOR--------------")

    
    # Ejercicio: Obtener el promedio de 5 calificaciones
    
Cantidad_Calif = int(input("Ingresa la cantidad de tus calificaciones: "))
suma = 0

for i in range(Cantidad_Calif):
    suma += int(input(f"Ingresa las calificaciones {i+1}: "))


print (f"Tu promedio es {suma/Cantidad_Calif} ")



#Ejercicio 2: Imprimir una tabla de multiplicar
'''
Ejemplo: 7 x 1 = 7
         7 x 2 = 14
         ...
'''''
tabla = int(input("Que tabla de multiplicar deseas saber? "))
limite = int(input("Hasta que numero limite? "))
for i in range(1, limite + 1):
    print(tabla, "x", i, "=", tabla * i)
    
    
#Ejercicio 3:
#Preguntar al usuario cuantas tablas desea imprimir (comenzando desde la tabla del 1, hasta la
#que indique el usuario y preguntar tambien el limite

Cantidad = int(input("Ingresa cuantas tablas deseas multiplicar"))
Limite = int(input("Hasta que numero limite?"))

for tabla in range(1, Cantidad + 1):
    print("Tabla del",    tabla)
    
    for numero in range(1, Limite + 1):
        print(tabla, "x", numero, "=", tabla * numero)
        
        
        
        
        
        
        
        
print("-------------MENUS con WHILE---------")
while(True):
    print("A ) Area Circulo")
    print("B ) Area Rectangulo")
    print("C ) Area Triangulo")
    print("-------------------")
    print("S ) Salir")
    print("Elige una opcion")
    opcion = input().upper()
    if(opcion=="A"):
        print("Elegiste A")
    elif(opcion=="B"):
        print("Elegiste B")
    elif(opcion=="C"):
        print("Elegiste C")
    elif(opcion=="S"):
        break
    else:
        print("Opcion Incorrecta!!!")
        