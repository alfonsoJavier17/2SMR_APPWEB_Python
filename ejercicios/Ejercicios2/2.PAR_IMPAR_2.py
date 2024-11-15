#Alfonso Javier Gil Vázquez
#04/10/2024
#Escriba un programa que pida primero un número par (positivo o negativo) y si el valor
#no es correcto, muestre un aviso. Si el valor es correcto, pedirá un número impar
#(positivo o negativo) y si el valor no es correcto, mostrará un aviso.

print ("PAR E IMPAR (2)")
PAR = eval (input ("Escriba un número par: "))
if PAR%2==1:
    print ("Ejecute de nuevo el programa para volver a intentarlo")
IMP = eval (input ("Escriba un número par: "))
if IMP%2==0:
    print ("Ejecute de nuevo el programa para volver a intentarlo")
print ("¡Gracias por su colaboración!")