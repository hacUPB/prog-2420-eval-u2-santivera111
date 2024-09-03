from os import system

while True:    #Bucle infinito
    print ("1. Calcular primo\n2. Calcular par\n3.  Salir")
    opcion= int(input("Ingrese la opcion: "))

    if opcion==1:
        system("cls")
        print("Calcula si el numero es primo")
        numero= int(input("Ingrese el numero a probar: "))
        control = 1
        cont = 0

        while control <=numero:
            if (numero%control) == 0:
                cont+= 1
            control+= 1

        if cont > 2:
            print(f"{numero} no es primo")
        else:
            print(f"{numero} es primo")
    elif opcion == 2:
        system("cls")
        print("Calcula si el numero es par")
        numero= int(input("Ingrese el numero a probar: "))
        if numero%2 == 0:
            print(  f"{numero} es par")
        else:
            print(f"{numero} es impar")

    elif opcion == 3:
        system("cls")
        break #comando para finalizar un bucle
    else:
        print("Opcion no valida...")


            