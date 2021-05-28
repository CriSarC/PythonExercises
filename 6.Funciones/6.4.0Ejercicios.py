#%%Ejercicio 1

# Crear un programa que tenga dos funciones, una que contenga el area de un 
# cuadrado con argumentos de base y altura; y la otra el area de un circulo con 
# argumento de radio

def ACuadrado(Base,Altura):
    return Base * Altura

print(ACuadrado(2,5))

def ACirculo(Radio):
    pi = 3.141516
    return pi*(Radio**2)

print (ACirculo(5))
    


#%%Ejercicio 2

# Escribir una función que reciba una muestra de números en una lista y 
# devuelva su medida.

def Muestra(*Numeros):
    SumaNumeros = 0
    CantidadNumeros = 0
    for i in Numeros:
        SumaNumeros += i
    CantidadNumeros = len(Numeros)
    Media = SumaNumeros/CantidadNumeros
    return Media

print(Muestra(5,6,8))