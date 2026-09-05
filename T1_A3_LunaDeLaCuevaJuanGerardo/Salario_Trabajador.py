'''
Created on 4 sept 2026

@author: dell
'''

dias_trabajados = float(input("Ingresa los días trabajados: "))
pago_hora = float(input("Ingresa el pago por hora: "))
dias_extras = float(input("Ingresa los días extras trabajados: "))


salario_normal = dias_trabajados * pago_hora


if dias_extras <= 5:
    pago_extras = dias_extras * pago_hora * 2
else:
    pago_extras = dias_extras * pago_hora * 3


salario_bruto = salario_normal + pago_extras

if salario_bruto > 20000:
    ispt = salario_bruto * 0.16
else:
    ispt = salario_bruto * 0.14


salario_neto = salario_bruto - ispt

print("Salario bruto:", salario_bruto)
print("ISPT:", ispt)
print("Salario neto:", salario_neto)