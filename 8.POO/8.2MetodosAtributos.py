
class Persona():
    Nombre = 'Carlos' #Atributo, que son caracteristicas
    Apellido = 'Vergara' #Atributo, que son caracteristicas
    Sexo = 'Masculino' #Atributo, que son caracteristicas
    Edad = 30 #Atributo, que son caracteristicas
    
    def Hablar(self, mensaje):  #Metodos que son lo mismo que funciones
        return mensaje
     
Persona = Persona()
Persona.Nombre
Persona.Apellido
Persona.Sexo
Persona.Edad

print(Persona.Hablar('Hola Soy'), '{} y mi Apellido es {}, tengo {} y de sexo {}'.format(Persona.Nombre,Persona.Apellido,Persona.Edad,Persona.Sexo))
