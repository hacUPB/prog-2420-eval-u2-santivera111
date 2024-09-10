Inicio

solicitar al usuario la altitud inicial (kilometros) 
solicitar usuario coeficiente de arrastre (decimal pequeño)
solicitar altitud minima

solicitar altitud inicial

definir altitud actual, la cual sera la inicial 

inicialmente las orbitas en = 0

mientras 

altitud actual > altitud minima
calcular altitud perdida como coeficiente de arrastre * altitud actual

Restar altitud perdida a altitud actual

se incrementara ceficiente en 0.0001
aumentar contador de orbitas. 

Si altitud perdida < umbral estabilidad
 imprimir "Estabilizacion en la orbita baja"
 imprmir "Altitud actual" "orbitas"
fin

Si altitud actual >= altitud minima
 imprimir "El satelite ha ingresado en la atmosfera"
 Imprimir "Orbitas" 
Fin




 
  
    
