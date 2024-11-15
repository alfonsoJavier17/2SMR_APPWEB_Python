#Alfonso Javier Gil Vázquez
#09/10/2024
#Escriba un programa que pida un número entero mayor que cero y que escriba sus
#divisores.

print ("DIVISORES")

N = int(input("Escriba un número mayor que cero: "))

if N<0:
    print ("Le he pedido un número entero mayot que cero")
else:
    for i in range(1,N+1):
        if N % i == 0:
            print (i, end=" ")