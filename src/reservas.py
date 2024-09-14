import random

def main():
    # Introducción
    titulo = input("Ingrese su título (Sr o Sra): ")
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")

    print(f"{titulo} {nombre} {apellido}, ¡Bienvenido a travel!")

    # Selección del vuelo
    origen = input("Escriba su origen, MEDELLIN, BOGOTA o CARTAGENA: ")
    origen = origen.upper()

    destino = input("Escriba su destino MEDELLIN, BOGOTA o CARTAGENA: ")
    destino = destino.upper()

    while origen == destino:
        print("El destino no puede ser el mismo que el origen. Elija un destino diferente: ")
        destino = input("Escriba su destino MEDELLIN, BOGOTA o CARTAGENA: ")
        destino = destino.upper()

    # Fecha
    dia_semana = input("Escriba el día de la semana que viajará (por ejemplo, viernes): ")
    dia_mes = int(input("Escriba el día del mes que viajará (entre 1 y 31): "))

    if 1 <= dia_mes <= 31:
        print(f"Su viaje se realizará el día {dia_mes}")
    else:
        print("Siga las instrucciones, Error")
        return  # Termina el programa si hay un error

    # Calcular la distancia entre origen y destino
    if origen == "MEDELLIN" and destino == "BOGOTA":
        distancia = 240
    elif origen == "MEDELLIN" and destino == "CARTAGENA":
        distancia = 461
    elif origen == "BOGOTA" and destino == "CARTAGENA":
        distancia = 657
    elif origen == "CARTAGENA" and destino == "MEDELLIN":
        distancia = 461
    elif origen == "CARTAGENA" and destino == "BOGOTA":
        distancia = 657
    else:
        print("No disponible")
        return  # Termina el programa si la distancia no es válida

    # Precio boleto
    if distancia < 400:
        if dia_semana in ["lunes", "martes", "miércoles", "jueves"]:
            precio = 79900
        else:
            precio = 119900
    else:
        if dia_semana in ["lunes", "martes", "miércoles", "jueves"]:
            precio = 156900
        else:
            precio = 213000

    # Preguntar por asiento
    print("Elija su asiento: A (ventana), B (medio), C (sin preferencia)")

    asiento = input("Por favor ingrese A, B o C para elegir su asiento: ").upper()

    if asiento == "A":
        print("Enhorabuena, has elegido el asiento junto a la ventana.")
    elif asiento == "B":
        print("Enhorabuena, has elegido el asiento en el medio.")
    elif asiento == "C":
        print("Enhorabuena, has elegido el asiento sin preferencia.")
    else:
        print("Opción no válida, por defecto se te asignará el asiento A (VENTANA)")
        asiento = "A"

    asiento_numero = random.randint(1, 29)
    print(f"El número de su asiento es {asiento_numero}")

    print(f"{titulo} {nombre} {apellido} - Origen: {origen}, Destino: {destino}, Fecha: {dia_semana} {dia_mes}, Precio: {precio}, Asiento: {asiento}{asiento_numero}")

if __name__ == "__main__":
    main()

