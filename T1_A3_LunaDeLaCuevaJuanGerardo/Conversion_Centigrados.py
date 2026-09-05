'''
Created on 4 sept 2026

@author: dell
'''
centigrados = float(input("Ingresa la temperatura en grados centígrados: "))

print("¿A qué deseas convertir?")
print("1. Fahrenheit")
print("2. Kelvin")

opcion = int(input("Selecciona una opción: "))

if opcion == 1:
    fahrenheit = (centigrados * 9 / 5) + 32
    print("Temperatura en Fahrenheit:", fahrenheit)

elif opcion == 2:
    kelvin = centigrados + 273.15
    print("Temperatura en Kelvin:", kelvin)

else:
    print("Opción no válida")