
#transmitir ciertos parametros, atributos y metodos
# clase padre con metodos y atributos y van a haber clases hijas

class Animales():  #CLASE padre
    def __init__(self, Descripcion, Especie, Hablar):
        self.Descripcion = Descripcion
        self.Especie = Especie
        self.Hablar = Hablar
        
    def Habla(self):
        print('yo hago: ', self.Hablar)
        
    def Describir(self):
        print('Soy de la especie: ', self.Especie)
        
class Perro(Animales): #CLASE HIJA
    pass

class Abeja(Animales): #CLASE HIJA
    def Sonido(self, Sonido): #las clases hija pueden tener sus propios metodos, funciones
        self.Sonido = Sonido
        print(self.Sonido)
    
Perro = Perro('Perro', 'Mamifero', 'Guau')
Perro.Habla()
Perro.Describir()

Abeja = Abeja('Abeja', 'Insecto', 'Brr')
Abeja.Sonido('Brr')
Abeja.Habla()
Abeja.Describir()