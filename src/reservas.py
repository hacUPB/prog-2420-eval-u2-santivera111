
def main():
    #Pseudocodigo
  
titulo = input("Ingrese su título (Sr. o Sra.): ")
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")

print(f"{titulo} {nombre} apellido}, ¡Bienvenido a travel!

#Seleccion del vuelo

origen = input("Escriba su origen en mayúsculas y sin tildes ("MEDELLIN, BOGOTA, CARTAGENA"):

destino = input("Escriba su destino en mayúsculas y sin tildes ("MEDELLIN, BOGOTA, CARTAGENA"):

while origen == destino: 
 print"El destino no ouede ser el mismo que el origen. Elija un destino diferente ")  
  destino= input("Escriba su destino en mayusculas y sin tildes: ")

  #fecha 

  dia_semana = input("Escriba el dia de la semana que viajara: (por ejemplo virrnes):")  
dia_mes= init(input("Escriba el día del mes que viajará (entre 1 y 31): ")

if 1<=dia_mes<= 31:
 print(f" su viaje se reslizara el dia {dia_mes}")
else: 
 print(" siga las instrucciones, Error") 
 exit()

#Calcular la distancia entre origen y destino


if __name__ == "__main__":
    main()
