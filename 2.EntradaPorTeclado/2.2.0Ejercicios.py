# Ejercicios

#%%CONCATENAR
# Ejercicio 1

# Escribir un programa que solicite al usuario un vocal en minuscula, y luego una
#  letra en mayúsculas. El programa debe convertir la letra en minúscula y la vocal
#  en mayúscula, y al final, deben ser concatenadas ambas

VocalMinuscula = input('Por favor ingrese una vocal en minuscula: ')
LetraMayuscula = input('Por favor ingrese una letra en mayuscula: ')

VocalMayuscula = VocalMinuscula.upper()
LetraMinuscula = LetraMayuscula.lower()

print('La vocal que ingreso es: {}, y la letra es: {}'.format(VocalMayuscula,LetraMinuscula))
print('La vocal que ingreso es: {}, y la letra es: {}, la combienación entre ambas es: {}'.format(VocalMinuscula.upper(),LetraMayuscula.lower(),VocalMinuscula.upper()+LetraMayuscula.lower()))


#%%CAMBIOS DE LINEA

# Ejercicio 2

# Hacer un programa que pida al usuario su nombre, su edad y su sexo y los muestre
#   de la siguiente forma:

# Te llamas: <nombre>

# Tu edad es: <edad>

# Eres: <sexo>

Nombre = input('Nombre: ')
Edad = int(input('Edad: '))
Sexo = input('Sexo: ')

print('Te llamas: <{}> \nTu edad es: <{}> \nEres: <{}>'.format(Nombre,Edad,Sexo))

#%%REVISAR CODIGO

# El siguiente fragmento de código tiene un total de 7 bugs (O tal vez más, o tal vez menos), 
# tu deber es encontrarlos, corregirlos, pasar el código a tu editor de código y verificar que 
# estén resueltos. Fíjate muy bien en el código, no solo pueden haber errores de sintaxis...


variable1 = int(input("Ingresa el primer número: "))    

variable2 = int(input("Ingresa el segundo número: "))


resultado = variable1 * variable2


print("El resultado de multiplicacion de ambos numeros es de: {}".format(resultado))