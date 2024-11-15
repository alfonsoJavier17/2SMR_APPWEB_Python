#Alfonso Javier Gil Vázquez
#04/10/2024
#Escriba un programa que pida dos números enteros y que calcule su división,
#escribiendo si la división es exacta o no.


print ("DIVISOR DE NÚMEROS")
D = int (input ("Escriba el dividendo "))
d = int (input ("Escriba el dividendo "))
if D % d ==0:
    x= D//d
    print ("La division es exacta. Cociente:" ,x)
else:
    x= D//d
    r= D%d
    print ("La division no es exacta. Cociente:" ,x ,"Resto:" ,r)