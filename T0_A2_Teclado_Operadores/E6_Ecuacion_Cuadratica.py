'''
Created on 26 ago 2026

@author: dell
'''
'''
Sabemos que para resolver ecuacuiones cuadraticas es ax2 + bx + c =0 
entonces usamos la formula general donde x es igual a, menos b, mayor o menor la raiz de b cuadrada, 
menos cuatro ac sobre dos a 
'''

print("Vamos a ayudarte a resolver tus ecuaciones cuadraticas")
import math
 
a = float(input("Ingresa el valor de a: ")) 
b = float(input("Ingresa el valor de b: "))
c = float(input("Ingresa el valor de c: "))

discriminate = b**2 - 4*a*c

x1 = (-b + math.sqrt(discriminate)) / (2*a)
x2 = (-b - math.sqrt(discriminate)) / (2*a)

print(f"x1 = {x1}")
print(f"x2 = {x2} ")
