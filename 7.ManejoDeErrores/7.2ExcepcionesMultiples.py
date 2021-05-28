#%%XeroDivisionError

while True:
    try:
        Num1 = int(input('Ingrese un Número: '))
        Resultado = 100/Num1
        print(Resultado)
        break
    except ZeroDivisionError:
        print('No se puede dividir entre cero')
       
#%%ValueError
       
while True:
    try:
        Edad = int(input('Ingresa tu edad: '))
        print('Tu edad es: ', Edad)
        break
    except ValueError: #cuando no se ingresa el tipo de dato que se espera
        print('has colocado un valor erroneo')
        
#%%KeyboardInterrupt        

while True:
    try:
        edad = int(input('Ingresa tu edad: '))
        print('tue edad es: ', edad)
        break
    except KeyboardInterrupt: #cuando se cancela con control + c
        print('\nHas cancelado la ejecución')
        break
        