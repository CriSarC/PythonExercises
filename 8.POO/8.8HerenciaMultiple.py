
#se ocupa para designar varias clases padre para poder ser usadas en una clase hija, SOLO SE PUEDE HACER EN PYTHON

class A():
    def Mensaje(self):
        print('Esta es la clase A')
        
    def Primero(self):
        print('Estas dentro de la clase A')
        
class B():
    def Mensaje(self):
        print('Esta es la clase B')
        
    def Segunda(self):
        print('Estas dentro de la clase B')
        
class C(B,A): #se ejecuta la que esta primero a la izquierda
    pass

C = C()
C.Mensaje()
C.Primero()
C.Segunda()
    