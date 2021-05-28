
#poder editar los metodos que una clase padre ya posee

class Animales(): #CLASE PADRE
    def __init__(self, Nombre, Mensaje):
        self.Nombre = Nombre
        self.Mensaje = Mensaje
        
    def Hablar(self):
        print(self.Mensaje)

class Perro(Animales): #CLASE HIJA
    def Hablar(self): #polimorfimo, los metodos, funciones se pueden modificar dentro de la clase hija para que hagan otra funcion
        print('Yo hago Guau')

class Pez(Animales):
    def Hablar(self):
        print('Yo no Hablo')
    
# Perro = Perro('Firulais', 'Guau')
# Perro.Hablar()

Animales = [Perro('Firulais', 'Guau'), Pez('Nemo', "Nada")] #es una lista pero a la vez un objeto
for i in Animales:
    print(i.Hablar()) 