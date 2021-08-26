def main():
    # Escribe el código adecuado para completar el programa
    A=float(input("Ingrese un numero: "))
    B=float(input("Ingrese otro numero: "))
    C=float(input("Ingrese un nuemero: "))
    
    if (C>B and B>A):
        print(A," , ",B," , ",C)
    elif (C>A and A>B):
        print(B," , ",A," , ",C)
    elif (B>A and A>C):
        print(C," , ",A," , ",B)
    elif (A>B and B>C):
        print(C," , ",B," , ",A)
    elif (B>C and C>A):
        print(A," , ",C," , ",B)
    elif (A>C and C>B):
        print(B," , ",C," , ",A)
    else:
        print("Son numeros iguales")
    pass


if __name__=='__main__':
    main()
