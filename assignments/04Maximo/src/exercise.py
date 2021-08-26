def main():
    #escribe tu código abajo de esta línea
    A=float(input("Ingrese un numero: "))
    B=float(input("Ingrese otro numero: "))
    C=float(input("Ingrese un nuemero: "))
    if(A > B and A > C):
        print("El numero mayor es ",A)
    else:
        if(B > A and B > C):
            print("El numero mayor es ", B)
        else:
            print("El numero mayor es " , C)

    pass


if __name__=='__main__':
    main()
