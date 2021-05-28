
while True:
    try:
        edad = int(input('Ingrese su edad: '))
        print('tu edad es: ', edad)
        break
    except:
        print('Ingresaste un valor erroneo')
    finally:
        print('La ejecución ha finalizado')