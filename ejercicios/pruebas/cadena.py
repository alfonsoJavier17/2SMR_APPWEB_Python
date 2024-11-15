# Entrada de datos
def dibujar_cuadrado_vacio(lado):
    # Generamos el cuadrado
    for i in range(lado):
        if i == 0 or i == lado - 1:
            # Si estamos en la primera o última fila, imprimimos una fila completa de asteriscos
            print('*' * lado)
        else:
            # Para las filas del medio, imprimimos un asterisco al principio y al final, y espacios en el medio
            print('*' + ' ' * (lado - 2) + '*')

# Pedimos al usuario que ingrese el tamaño del lado del cuadrado
lado = int(input("Introduce el tamaño del lado del cuadrado: "))

# Llamamos a la función para dibujar el cuadrado
dibujar_cuadrado_vacio(lado)