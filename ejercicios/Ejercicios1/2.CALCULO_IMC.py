#Alfonso Javier Gil Vázquez
#30/09/2024
#Escriba un programa que pida dos numeros y escriba su meida aritmética

print ("CÁLCULO DE ÍNDICE DE MASA CORPORAL")
P = float (input ("¿Cuánto pesas? ")) 
H = float (input ("¿Cúanto mides en metros? "))
imc = P / H**2
print ("Su imc es" ,imc)
print ("Un ímc muy alto indica obesidad. Los valores normales de imc están entre 20 y 25,") 
print ("pero esos límites dependen de la edad, del sexo, de la constitución física, etc.") 