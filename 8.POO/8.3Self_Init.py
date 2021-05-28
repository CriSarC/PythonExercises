
class Persona():
    Nombre = False
    
    def __init__(self, Nombre, Apellido): #init hace que este Primer metodo que se va a ejecutar en toda la clase, también puede automatizar atributos 
        self.Nombre = Nombre
        self.Apellido = Apellido
        print('Has creado el objeto Persona. Con el Nombre {} y el Apellido {}'.format(Nombre,Apellido))
    
    def Datos(self):
       self.Nombre = True #las variables que estan dentro de esta función no pueden usarse afuera, el global se remplaza por el self
        
Persona = Persona('Juan','Carranza')


