#Alfonso Javier Gil Vazquez
#14/10/2024
#Pide la anchura y que dibuje un cuadrado.

def dibujar_triangulo(anchura):
    # Parte de arriba del triangulo
    for i in range(1, anchura + 1):
        print('* ' * i)
    
    # Parte de abajo del triangulo
    for i in range(anchura - 1, 0, -1):
        print('* ' * i)

# Solicitar la anchura del triangulo al usuario
anchura = int(input("Anchura del triangulo: "))
dibujar_triangulo(anchura)