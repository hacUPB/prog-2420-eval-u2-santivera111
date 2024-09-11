
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

  dia_semana = input("Escriba el dia de la semana que viajara: (por ejemplo viernes):")  
dia_mes= init(input("Escriba el día del mes que viajará (entre 1 y 31): ")

if 1<=dia_mes<= 31:
 print(f" su viaje se reslizara el dia {dia_mes}")
else: 
 print(" siga las instrucciones, Error") 
 exit()

#Calcular la distancia entre origen y destino

if origen == "MEDELLIN" and destino == "BOGOTA" : 
distancia = 240 

elif origen == "MEDELLIN" and destino == "CARTAGENA" : 
distancia = 461

elif origen == "BOGOTA" and destino == "CARTAGENA" : 
distancia = 657 

elif origen == "CARTAGENA" and destino == "MEDELLIN" : 
distancia = 461

elif origen == "CARTAGENA" and destino == "BOGOTA" : 
distancia = 461

else: 
 print("No disponible")

 #Precio boleto

if distancia < 400: 
  if dia_semana in ["lunes"," martes"," miercoles"," jueves"]:
    precio= 79900
     else:
      precio=119900
else:
   if dia_semana in ["lunes"," martes"," miercoles"," jueves"]:
    precio= 156900
     else:
      precio=213000


#Preguntar por asiento
prefer= input" Prefiere asiento del pasillo, junto a la ventana o sin preferencia ")

print("Elida su asiento: A (ventana), B (medio), C(sin preferencia )")

asiento= input("porfavor ingrese A, B o C para elegir su asiento: ").upper()

if asiento == "A":
 print ("Enhorabuena, has elegido el asiento junto a la ventana.") 
elif asiento == B
 print ("Enhorabuena, has elegido el asiento en el medio.") 
 elif asiento == C
  print ("Enhorabuena, has elegido el asiento en el medio.") 
  
 

 



if __name__ == "__main__":
    main()
