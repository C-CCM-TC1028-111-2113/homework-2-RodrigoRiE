
def main():
    #Escribe tu código debajo de esta línea
    edad = float(input("Ingresa tu edad: "))

    if edad >= 18:
      id = str(input("¿Tienes identificación oficial? (s/n): "))
      if id == "s":
        print("Trámite de licencia concedido")
      elif id == "n":
        print("No cumples requisitos")
      else:
        print("Respuesta incorrecta")  
    elif edad > 0 and edad < 18:
      print("No cumples requisitos")
    else:
      print("Respuesta incorrecta")
    pass


if __name__ == '__main__':
    main()
