#Alfonso Javier Gil Vázquez
#04/10/2024
#Escriba un programa que pida un año y que escriba si es bisiesto o no.
#Se recuerda que los años bisiestos son múltiplos de 4, pero los múltiplos de 100 no lo son, aunque los múltiplos de 400 sí.

print ("COMPARADOR DE TRES NÚMEROS")
A = eval (input ("Escribe un año y le dire si es bisiestro "))

if A % 4 ==0:
    if A % 100 != 0:
        print ("El año" ,A ,"es una año bisiestro porque es múltiplo de 4 sis ser múltiplo de 100")
    elif A % 400 == 0:
        print ("El año" ,A ,"es una año bisiestro porque es múltiplo de 400")
    else:
        if A % 100 == 0 and A % 400 != 0:
            print ("El año" ,A ,"no se un año bisiestro porque es múltiplo de 100 sin ser múltiplo de 400")
else:
    print ("el año" ,A ,"no es un año bisiestro")