
def Suma(Num1,Num2):
    return Num1 + Num2
print(Suma(10,35))

def Resta(N1,N2):
    return N1 - N2
print(Resta(N2=2,N1=1))

def Tontin(N = None, M = None):
    if N == None: # encaso de que no ingresen valores
        print('No has ingresado los valores')
        return
    return N - M

print(Tontin(4,3))        