#Alfonso Javier Gil Vázquez
#04/10/2024
#Mejore el programa anterior haciendo que tenga en cuenta que no se puede dividir por
#cero.

print ("DIVISOR DE NÚMEROS")
D = int (input ("Escriba el dividendo "))
d = int (input ("Escriba el dividendo "))

if D==0 or d==0:
    print ("No se puede dividir por cero")
elif D % d ==0:
    x= D//d
    print ("La division es exacta. Cociente:" ,x)
else:
    x= D//d
    r= D%d
    print ("La division no es exacta. Cociente:" ,x ,"Resto:" ,r)