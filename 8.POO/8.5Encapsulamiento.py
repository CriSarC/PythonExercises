
#encapsulamiento es declarar atributos privados solo para una clase
class A():
    def __init__(self):
        self.Contador = 0
        
    def Incrementar(self):
        self.Contador += 1
        
    def Cuenta(self):
        return self.Contador
    
class B():
    def __init__(self):
        self.__Contador = 0 #al colocar __ el atributo queda enclapsulado, y vale solo para esta clase
        
    def Incrementar(self):
        self.__Contador += 1 #al colocar __ el atributo queda enclapsulado, y vale solo para esta clase
        
    def Cuenta(self):
        return self.__Contador #al colocar __ el atributo queda enclapsulado, y vale solo para esta clase
    
a = A() #se crea el objeto a y se iguala a la clase A()
a.Incrementar() #incrementa en uno
a.Incrementar()
print(a.Cuenta())
print(a.Contador)

b = B()
b.Incrementar()
b.Incrementar()
print(b.Cuenta())
print(b._B__Contador) #se coloca el objeto y la clase de esta manera para que se pueda usar el atributo

