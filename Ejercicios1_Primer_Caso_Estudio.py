
#Ejercicio 6 - Calcular la cantidad de vueltas que da una llanta en un kilometro

#Bienvenida
print('Bienvenidos al calculo de la cantidad de vueltas que da una llanta en un kilometro')

#Entradas

diametro = float(input('\nPorfavor ingrese la medida del diámetro de la llanta: '))

#Proceso

circunferencia = 3.14 * diametro

numeroVueltas = 1000 / circunferencia


#Salida
#El formato :.2f permite mostrar solo 2 decimales en un float
print(f'Una llanta da {numeroVueltas:.2f} vueltas en 1 kilometro' )





