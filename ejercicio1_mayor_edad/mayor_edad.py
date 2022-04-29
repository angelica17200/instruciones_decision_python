"""Ejercicio 1:
progrma para verificar si una persona
es mayor de edad"""

from errno import EADDRNOTAVAIL


print("----------------------------------")
print("-----------MAYOR DE EDAD----------")
print("----------------------------------")

# input 
edad = int(input("Digite la edad:"))

# processing 
if edad >= 18:
     print("La persona es MAYOR DE EDAD")
else:
     print("La persona es MENOR DE EDAD")