'''
Created on 2 sept 2026

@author: dell
'''
"""
CADENAS O STRING (en Python Str)

    Es un conjunto de 0-N caracteres formado por LETRAS, NUMEROS 
    y/o CARACTERES ESPECIALES
    
"""
cadena_vacia = ""
nombre = "Luke Skywalker"
edad = "30"
temperatura1 = "45.8 C"
temperatura2 = "23.1 F"

print(temperatura1 + temperatura2)

cad = "Ingenieria en Sistemas Computacionales"

print(cad.upper())
print(cad)

print(f"Total de caracteres de una cadena:  {len(cad) } ")

print(cad.find("a"))
print(cad.find("en"))
print(cad.find("Sistemas"))


print(cad.count("a"))
print(cad.count("t"))


print("magia7".isalnum())
print("magia".isalpha())
print("magia7".isnumeric())
print("7.2".isnumeric())


print(cad.replace(" ", ""))


print("------------TECNICA de SLICING--------------")

print( cad[5:10] )
print( cad[:] )
print( cad[20:] )
print( cad[:15] )

print( cad[3] )


print("------------Analisis de Cadenas------------")

contador_vocales = 0
for i in range(0, len(cad)):
    #print(cad[i])
    cad2= cad.upper()
    if(cad2[i]=="A" or cad2[i]=="E" or cad2[i]=="I" or cad2[i]=="O" or cad2[i]=="U"):
            contador_vocales += 1
        
print("Contador_vocales")


for i in range(5000):
    print(chr(i))
    
    