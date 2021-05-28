
class Persona():
    def __init__(self, Nombre, Apellido): #metodo constructor
        self.Nombre = Nombre
        self.Apellido = Apellido
        print('El Objeto {} {} ha sido creado'.format(self.Nombre,self.Apellido))
        
    def __str__(self): #metodo convierte a cadena de texto
        return 'El objeto tiene como atributo el nombre {} y el apellido {}'.format(self.Nombre, self.Apellido)    
        
    def __del__(self): #metodo destructor
        
        print('El objeto {} {} ha sido destruido'.format(self.Nombre,self.Apellido))
        
    
        
Persona = Persona('Walter', 'Coto')
print(str(Persona))

