'''
Created on 12 sept 2026

@author: dell
'''
vector = []

def mostrar_menu():
    
    print("\n=======VECTORES========")
    print("1. Obtener posicion de Inicio")
    print("2. Obtener posicion de Fin")
    print("3. Obtener cantidad de elementos")
    print("4. Mostrar todos los elementos")
    print("5. Mostrar elemento del inicio")
    print("6. Mostrar elemento del final")
    print("7. Aumentar tamano del arreglo")
    print("8. Disminuir tamano del arreglo")
    print("9. Insertar elemento en posicion especifica")
    print("10. Insertar elemento al incio")
    print("11. Insertar elemento al final")
    print("12. Eliminar elemento de posicion especifica")
    print("13. Eliminar elemento del inicio")
    print("14. Eliminar elemento del final")
    print("15. Invertir el vector")
    print("16. Buscar elemento")
    print("17. SALIR")
    print("===========================")
    
    
while True:
        
        mostrar_menu()
        
        opcion = int(input("Seleccion una opcion"))
        
        
        if opcion ==1:
            if len(vector) == 0:
                print("El vector esta vacio")
            else:
                print("La posicion inicial es: 0")
                
                
        elif opcion ==2:
            if len(vector)== 0:
                print("El vector esta vacio")
            else:
                print("La posicion final es: ",  len(vector) -1)
                
        
        elif opcion == 3:
                print("Cantidad de elementos: ", len(vector))
            
        
        
        elif opcion == 4:
            if len(vector) == 0:
                
                print("El vector esta vacio.")
            else:
                print("Elementos del vector:")
                for i in range(len(vector)):
                    print("Posicion", i, ":", vector[i])

        elif opcion == 5:
            if len(vector) == 0:
                print("El vector esta vacio")
            else:
                print("Elemento del inicio:", vector[0])

        elif opcion == 6:
            if len(vector) == 0:
                print("El vector esta vacio")
            else:
                print("Elemento del final:", vector[-1])
                
                
        elif opcion == 7:
            cantidad = int(input("Cuantos elementos desea agregar?: "))
            
            for i in range(cantidad):
                elemento = int(input("Ingrese el elemento: "))
                vector.append(elemento)
                
            print("El tamano del vector aumento.")
            print("Vector:", vector)
            
            
        
        elif opcion == 8:
            if len(vector) == 0:
                print("El vector esta vacio.")
            else:
                cantidad = int(input("Cuantos elementos desea eliminar del final?:"))
                
                if cantidad > lec(vector):
                    print("No puede eliminar mas elementos de los que existen.")
                else:
                    for i in range(cantidad):
                        vector.pop()
                    print("El tamano del vector disminuyo.")
                    print("Vector:", vector)
                    
            
        elif opcion == 9:
            posicion = int(input("Ingrese la posicion donde desea insertar: "))

            if posicion < 0 or posicion > len(vector):
                print("Posicion no valida.")
            else:
                elemento = int(input("Ingrese el elemento: "))
                vector.insert(posicion, elemento)
                print("Elemento insertado correctamente.")
                print("Vector:", vector)

        elif opcion == 10:
            elemento = int(input("Ingrese el elemento: "))
            vector.insert(0, elemento)
            print("Elemento insertado al inicio")
            print("Vector:", vector)

        elif opcion == 11:
            elemento = int(input("Ingresa el elemento: "))
            vector.append(elemento)
            print("Elemento insertado al final")
            print("Vector:", vector)

        elif opcion == 12:
            if len(vector) == 0:
                print("El vector esta vacio")
            else:
                posicion = int(input("Ingrese la posicion que desea eliminar: "))

                if posicion < 0 or posicion >= len(vector):
                    print("Posicion no valida.")
                else:
                    eliminado = vector.pop(posicion)
                    print("Elemento eliminado:", eliminado)
                    print("Vector:", vector)

        elif opcion == 13:
            if len(vector) == 0:
                print("El vector esta vacio")
            else:
                eliminado = vector.pop(0)
                print("Elemento eliminado:", eliminado)
                print("Vector:", vector)

        elif opcion == 14:
            if len(vector) == 0:
                print("El vector esta vacio")
            else:
                eliminado = vector.pop()
                print("Elemento eliminado:", eliminado)
                print("Vector:", vector)

        elif opcion == 15:
            if len(vector) == 0:
                print("El vector esta vacio")
            else:
                vector.reverse()
                print("Vector invertido")
                print(vector)
                
                
        elif opcion == 16:
            if len(vector) == 0:
                print("EL vector esta vacio")
            else:
                elemento = int(input("Ingrese el elemento que desea buscar: "))
                
                
                if elemento in vector:
                    posicion = vector.index(elemento)
                    
                    print("Elemento encontrado")
                    print("Posicion:", posicion)
                else:
                    print("El elemento no se encuentra en el vector.")
                    
        
        elif opcion == 17:
            print("Programa terminado.")
            break
                 
        else:
            print("Opcion no valida")
                       
                            