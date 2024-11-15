#Alfonso Javier Gil Vázquez
#04/10/2024
#Escriba un programa que pida dos números enteros y que escriba si el mayor es múltiplo del menor. El programa debe avisar cuando se escriben valores negativos o nulos.

print ("COMPARADOR DE MÚLTIPLOS")
A = eval (input ("Escribe un número "))
B = eval (input ("Escribe otro número "))

if A==0 or B == 0:
    print ("Lo siento este programa no admite valores nulos")
elif A < 0 or B < 0:
    print ("Lo siento, este progrma no admite números negativos")
elif A > B:
    if A % B == 0:
        print (A, "es múltiplo de" ,B)
    else:
        print (A, "no es múltiplo de" ,B)
else:
    if B % A == 0:
        print (B, "es múltiplo de" ,A) 
    else:
        print (B, "no es múltiplo de" ,A)