n=int(input("introduce un numero "))
l=[]
seguir=True
while seguir:
    if n != 0:
        n=int(input("introduce otro numero: "))
        l.append(n)
    else:
        seguir=False
print(l)