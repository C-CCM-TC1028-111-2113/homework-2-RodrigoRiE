def main():
    #escribe tu código abajo de esta línea
    peso = float(input("Introduzca su peso (kg): "))
    altura = float(input("Ingrese su altura (m): "))

    BMI = peso / altura**2

    if BMI < 20 :
        print("Peso bajo")
    elif 25 > BMI >= 20:
        print("Normal")
    elif 30 > BMI >= 25:
        print("Sobre peso")
    elif 40 > BMI >= 30:
        print("Obesidad")
    elif BMI >= 40:
        print("Obesidad Morbida")
    else:
        print("Error")
    pass

if __name__=='__main__':
    main()
