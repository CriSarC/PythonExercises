
def Funcion():
    print('Hola mundo')
    
Funcion()

def FuncionSuma():
    Num1 = 50   # Las variables definidas dentro del la funcion estan enclapsuladas y no funcionan afuera de la funcion
    global Num2  #global hace que las variables se puedan aplicar en todo el programa
    Num2 = 30
    Resultado = Num1 + Num2
    
    print(Resultado)
    
FuncionSuma()    
print(Num2)