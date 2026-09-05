'''
Created on 28 ago 2026

@author: dell
''' 

'''Solicitar datos al usuario'''

horas_trabajadas = float(input("Ingrese las horas trabajadas: "))
precio_por_hora = float(input("Ingrese el precio por hora: "))
horas_extra_trabajadas = float(input("Ingrese las horas extras trabajadas: "))
iva = float(input("Ingrese el monto de IVA a descontar: "))
impuestos = float(input("Ingrese el monto de impuestos a descontar: "))

'''Calcular pago de horas extras'''
horas_extras = horas_extra_trabajadas * (precio_por_hora * 2)

'''Calcular salario bruto'''
salario_bruto = (horas_trabajadas * precio_por_hora) + horas_extras

'''Calcular salario neto'''
salario_neto = salario_bruto - iva - impuestos

'''Mostrar resultados'''
print("\n--- RESULTADOS ---")
print("Pago por horas extras:", horas_extras)
print("Salario bruto:", salario_bruto)
print("IVA:", iva)
print("Impuestos:", impuestos)
print("Salario neto:", salario_neto)