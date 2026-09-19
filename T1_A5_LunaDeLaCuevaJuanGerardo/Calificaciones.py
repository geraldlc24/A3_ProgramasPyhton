'''
Created on 9 sept 2026

@author: dell

'''

alumnos = int(input("De cuantos alumnos desea ingresar calificaciones"))
alumnos = []



cantidad = int(input("Cuantas calificaciones deseas ingresar?" ))
calificaciones = []

for i in range(cantidad):
    calificacion = float(input(f"ingrese la calificacion {i + 1}: "))
    calificaciones.append(calificacion)
    
promedio = sum("calificaciones")/ cantidad

aprobatorias = []
for calificacion in calificaciones:
    if calificacion >= 70:
        aprobatorias.append(calificacion)
    
    if len(aprobatorias) > 0:
        promedio_aprobatorias = sum(aprobatorias) / len(aprobatorias)
    else
    
        promedio_aprobatorias=0
        
    mayores = []
    
    for calificacion in calificaciones:
        if calificacion > promedio:
            mayores.append(calificacion)
            
    if len(mayores) > 0:
        promedio_mayores = sum(mayores) / len(mayores)
    
    else 
    promedio_mayores = 0
    
    
    print('--------RESULTADOS--------')
    print("calificaciones:", calificaciones)
    print("Promedio General:", promedio)
    print("promedio aprobatorias:", promedio_aprobatorias)
    print("promedio mayores al promedio:", promedio_mayores)
    