#Ejercicio 7 - Calcular la longitud de la sombre de un edificio de 20 metros

#Se invoca la librería math que permite traer las funciones tan() y radians()

#import math 

#Entrada

#altura = 20
#angulo = int(input('Ingrese el ángulo del sol hacia el edificio: '))

#Proceso
#Esta formuala convierte los grados a radianes
#longitud_sombra = altura / math.tan(math.radians(angulo))

#Salida
#El formato :.2f permite mostrar solo 2 decimales en un float
#print(f'La lingitud de la sombra de un edificio de 20 metros es de: {longitud_sombra:.2f} metros')





import requests

respuesta = requests.get("https://api.github.com")
print("Código de respuesta:", respuesta.status_code)




















