
def main():
    #Pseudocodigo
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

    Imprimir "Escriba su origen en mayusculas y sin tildes (MEDELLIN, BOGOTA, CARTAGENA)":
    Leer origen
    Imprimir "Escriba su destino en mayusculas y sin tildes ":
    Leer destino

    Imprimir "Escriba el dia de la semana en el que viajara (Por ejemplo: viernes)":
    Leer dia_Semana
    Imprimir "Escriba el dia del mes que viajara (entre 1 y 31)"
    Leer dia_Mes

        Si 1 < dia_Mes < 31
        Imprimir "Correcto"
        Si no
        Imprimir "Error"

        Si origen = "Medellin" y destino= "Bogota" entonces 
        distancia=240
        Sino 
            si origen ="Medellin" y destino ="Cartagena" entonces 
            distancia=461
             sino 
                 si    origen = "Bogota" y destino = "Cartagena" entonces 
                    distancia= 657
                     sino
                     si origen ="Cartagena" y destino ="Medellin" entonces 
                         distancia=461
                            sino origen = "Cartagena" y destino = "Bogota" entonces 
                                distancia= 657
        Finsi                      
            Fin si
                Finsi
                    Finsi  
                        
Si distancia <400 entonces 
    Si dia_Semana es "Lunes", "Martes", "Miercoles", "Jueves" entonces
    Precio = 79.900$
    Sino 
    Precio= 119.900$
Sino 
    Si dia_Semana es "Lunes", "Martes", "Miercoles", "Jueves" entonces
    Precio= 156.900
    Sino 
    Precio=213.000
    



    


    


    pass # borra esta línea cuando con inicies tu código


if __name__ == "__main__":
    main()
