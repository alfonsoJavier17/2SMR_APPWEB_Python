#Alfonso Javier Gil Vázquez
#04/10/2024
#Escriba un programa que pida tres números y que escriba si son los tres iguales, si hay
#dos iguales o si son los tres distintos.

print ("COMPARADOR DE TRES NÚMEROS")

A = eval (input ("Escribe un número "))
B = eval (input ("Escribe otro número "))
C = eval (input ("Escribe otro número más "))

if A == B == C:
    print("Ha escrito tres veces el mismo número")
elif A == B or A==C or B==C:
    print ("Ha escrito uno de los números dos veces")
else:
    print ("los tres números que has escritos son distintos")