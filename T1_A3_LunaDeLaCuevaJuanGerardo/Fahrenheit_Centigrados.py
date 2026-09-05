'''
Created on 4 sept 2026

@author: dell
'''
fahrenheit = float(input("Ingresa la temperatura en Fahrenheit: "))

centigrados = (fahrenheit - 32) * 5 / 9

print("Temperatura en centígrados:", centigrados)

if centigrados < 0:
    print("CONGELANTE")
else:
    print("NORMAL")