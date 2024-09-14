
#Satelite.py
#Codigo
def simular_desintegracion_orbital():
    #Datos 


    altitud_inicial = float(input("Ingrese la altitud inicial del satélite (en km): "))
    coeficiente = float(input("Ingrese el coeficiente de arrastre inicial (un valor pequeño, como 0.01): "))
    altitud_min = float(input("Ingrese la altitud mínima de seguridad (en km): "))

    #INICIO DEL BUCLE
    orbitas = 0   #inicia contador en 0
    perdida_min = 0.01      # Un valor pequeño para determinar cuándo se estabiliza la altitud

    #Siimualcion
    while altitud_inicial > altitud_min:    #es la condicion del bucle, para que se repita hasta que la altitud inicial sea menor a la minima
        altitud_perdida = coeficiente * altitud_inicial
        altitud_inicial -= altitud_perdida
        orbitas += 1

        #Aumentar el coeficiente de de arrastre con cada orbita
        coeficiente += 0.001
        #imprimir la info actual

        print(f"orbita {orbitas}: Altitud = {altitud_inicial}km, coeficiente de arrastre = {coeficiente}")

        #verificamos si la perdida de altitud es muy pequeña para estabilizarlo

        if altitud_perdida < perdida_min:
            print(f"El satelite se ha estabilizado en una orbita a {altitud_inicial} km despues de {orbitas} orbitas ")
            return
    
    #Si el satelite reingresa en la atmosfera
    print(f"El satelite ha reingresado en la atmosfera y se ha desintegrado despues de {orbitas} orbitas ")

simular_desintegracion_orbital()
