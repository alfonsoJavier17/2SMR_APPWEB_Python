#Alfonso Javier Gil Vázquez
#30/09/2024
#Escriba un programa que pida dos numeros y escriba su meida aritmética

print ("CONVERTIDOR DE SEGUNDOS A HORAS Y MINUTOS")
C = float (input ("Escriba una cantidad de segundos "))
H = C // 3600
x = C - (H*3600)
M = x //60
S = C % 60
print (C ,"segundos son" ,M ,"minutos y" ,S ,"segundos")