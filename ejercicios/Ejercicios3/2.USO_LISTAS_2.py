#Alfonso Javier Gil Vázquez
#09/10/2024
#Escriba un programa que pida dos números enteros y escriba la lista de números
#consecutivos que hay entre ellos, de menor a mayor.

print ("LISTA DE MENOR A MAYOR")

A = int (input("Escribe un número entero "))
B = int (input("Escribe otro un número entero "))

lista = list(range(A,B))
print (lista)