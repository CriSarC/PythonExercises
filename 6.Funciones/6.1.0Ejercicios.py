#%%Ejercicio 1

# Crear un programa que tenga una lista, luego crear una funcion con la cual se
#  van a pedir numeros al usuario para agregar a la lista. Debes crear una segunda
#  funcion en donde se ordenen los numeros pares e impares dentro de dos listas nuevas

Lista = []
Num = 0

def Pedir():
    i = 0
    while i < 5:
        Num = int(input('Ingrese un número: '))
        Lista.append(Num)
        i += 1

def Numeros():
    Lista.sort()
    Pares = []
    Impar = []
    for i in Lista:
        if i%2 == 0:
            Pares.append(i)
        else:
            Impar.append(i)
    print(Pares)
    print(Impar)        
    
Pedir()
Numeros()

#%%Ejercicio 2

# Escribir una función que reciba un número entero positivo y devuelva su factorial.

def Factorial():
    
    Numero = int(input('Ingrese un número entero positivo: '))
    Factorial = 1
    
    for i in range(1, Numero+1):
        Factorial = Factorial * i 
    print('El Factorial de {} es = {}'.format(Numero,Factorial))

Factorial()