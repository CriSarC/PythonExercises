#Solución Ejercicio

Suma = 3 + 2
Multiplicacion = 2 * 5
Division = Suma / Multiplicacion

print (Division**2)

Operacion = ((3 + 2) / (2 * 5))**2

print (Operacion)

print(pow((2+3)/(2*5),2))

# Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas.
# Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete, 
# así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. 
# Cada payaso pesa 112 g y cada muñeca 75 g. Un cliente frecuente pide la cantidad de 23 payasos y 54 muñecas, 
# realiza un programa que muestre el peso total de toda la venta.

PesoPayaso = 112 #gramos
PesoMuñeca = 75 #gramos

PedidoPayasos = 23 #unidades
PedidoMuñecas = 54 #unidades

PesoTotalPedido = PesoPayaso * PedidoPayasos + PesoMuñeca * PedidoMuñecas
PesoTotalKg = PesoTotalPedido / 1000 #peso expresado en kilogramos

print(PesoTotalKg,"Kg")
