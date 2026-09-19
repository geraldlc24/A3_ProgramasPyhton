'''
Created on 9 sept 2026

@author: dell
'''
class Alumno: 
    #Variables de CLASE(aqui no van los ATRIBUTOS)
     
     #Constructor
     def __init__(self, nombre, carrera):
     #atributos
     self.nombre = nombre
     x = 10 #variable local dentro del constructor
     self.carrera = carrera
     self.calificaciones = [100, 90, 80]
     
     
     def metodoX(self):
         pass 
     
     def obtenerPromedio(self, limite):
         sum = 0
         for cal in self.calificaciones:
             sum += cal
             return sum/len(self.calificaciones)
         

print("===========PRUEBA OBJETOS===========")
a1 = Alumno("Luke SkyWalker", "ISC")
print(f"El promedio es: {a1.obtenerPromedio(10)}" )
print(a1.nombre)