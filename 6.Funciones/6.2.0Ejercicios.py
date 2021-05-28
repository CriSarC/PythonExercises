#%%Ejercicio 1

# Crear una funcion que pida dos numeros. Si el primero es mayor al segundo, el 
# programa debe retornar el valor 1; si el segundo es mayor al primero, debe 
# retornar -1; si ambos son iguales, debe retornar 0

def MayorMenor():
    Num1 = input('Ingrese primer número: ')
    Num2 = input('Ingrese segundo número: ')
    if Num1 > Num2:
        return 1
    elif Num2 > Num1:
        return -1
    else:
        return 0
print(MayorMenor())
    


#%%Ejercicio 2

# Escribir una función que calcule el total de una factura tras aplicarle el IVA.
#  La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y
#  devolver el total de la factura. Si se invoca la función sin pasarle el 
#  porcentaje de IVA, deberá aplicar un 21%.

def FacturaIVA():
    Factura = int(input('Ingrese el Costo de la Factura: '))
    
    IVA = int(input('Ingrese el IVA: '))
    if type(IVA) == str:
        ValorTotal = Factura * IVA
        return ValorTotal
    else:
      
       ValorTotal = 0.21 * Factura
       return ValorTotal
    
print(FacturaIVA())