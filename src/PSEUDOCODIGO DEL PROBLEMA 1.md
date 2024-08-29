 PSEUDOCODIGO DEL PROBLEMA 1

 Inicio
    Imprimir "Desea ser (¿Señor o Señora?: )":
    Titulo=Señora
    Titulo=Señor
    Leer titulo
    Imprimir "Ingrese su nombre:  ":
    Leer nombre 
    Imprimir "Ingrese su apellido:  ":
    Leer apellido

    Imprimir "{titulo}+{nombre}+{apellido}+ Bienvenido a Travel Airlines!  ":

    Imprimir "Escriba su origen en mayúsculas y sin tildes (MEDELLIN, BOGOTA, CARTAGENA)":
    Leer origen
    Imprimir "Escriba su destino en mayúsculas y sin tildes ":
    Leer destino

    Imprimir "Escriba el día de la semana en el que viajara (Por ejemplo: viernes)":
    Leer dia_Semana
    Imprimir "Escriba el día del mes que viajara (entre 1 y 31)"
    Leer dia_Mes

        Si 1 < dia_Mes < 31
        Imprimir "Correcto"
        Si no
        Imprimir "Error"

        Si origen = "MEDELLIN" y destino= "BOGOTA" entonces 
        distancia=240
        Sino 
            si origen ="MEDELLIN" y destino ="Cartagena" entonces 
            distancia=461
             sino 
                 si    origen = "BOGOTA" y destino = "CARTAGENA" entonces 
                    distancia= 657
                     sino
                     si origen ="Cartagena" y destino ="MEDELLIN" entonces 
                         distancia=461
                            sino origen = "Cartagena" y destino = "BOGOTA" entonces 
                                distancia= 657
        Finsi                      
            Fin si
                Finsi
                    Finsi  
                        
Si distancia <400 entonces 
    Si dia_Semana es "Lunes", "Martes", "Miércoles", "Jueves" entonces
    Precio = 79.900$
    Sino 
    Precio= 119.900$
Sino 
    Si dia_Semana es "Lunes", "Martes", "Miércoles", "Jueves" entonces
    Precio= 156.900
    Sino 
    Precio=213.000
 Finsi

 Imprimir "Prefiere ubicarse en el asiento del pasillo, junto a la ventana, o sin preferencia?":

 Si 
 pref= "pasillo" entonces
 Asiento = C
 Sino 
  Si 
  pref= "ventana"   entonces 
 Asiento = A
   Sino 
   Asiento= B
   Finsi
AsientoNum= Asiento random de 1- 29
   Imprimir "Su asiento asignado es {AsientoNum}+{Asiento}

  Imprimir "{titulo}+{nombre}+{apellido}+{origen}+{destino}+{Precio}+{AsientoNum}+{Asiento}

  Fin
   
 
  
    
