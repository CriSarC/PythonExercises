

#%%Ejercicio 1

# Escribir un programa que pida un numero al usuario y muestre las tablas de 
# multiplicar de ese numero

NumeroX = int(input('Ingrese número del cual desea saber las tablas de multiplicar: '))

i = 0

while i <= 10:
  
    Multiplicacion = NumeroX * i
    print('{} X {} = {}'.format(NumeroX,i,Multiplicacion))
    i += 1
    

#%%Ejercicio 2

# Escribir un programa que pregunte al usuario su edad y muestre por pantalla 
# todos los años que ha cumplido (desde 1 hasta su edad).

Edad = int(input('Cuantos años tienes? '))

j = 0

while j < Edad:
    j += 1
    print(j)