#Declaración de variables y arreglos
nombres = []              #Almacena los nombres de los clientes
apellidos = []            #Almacena los apellidos de los clientes
cantidades = []           #Almacena la cantidad de trajes comprados por el cliente
precios_unitarios = []    #Almacena el precio unitario de cada venta
totales = []              #Almacena el total a pagar de cada cliente

continuar = 's'      #Almacena el total a pagar de cada cliente
#Bucle para ingreso de datos
while continuar == 's':
    nombre = input("Ingrese el nombre del cliente: ")
    apellido = input("Ingrese el apellido del cliente: ")
    cantidad = int(input("Ingrese la cantidad de trajes a comprar: "))
    precio_unitario = float(input("Ingrese el precio unitario de cada traje: "))

    #Cálculo de subtotal
    subtotal = cantidad * precio_unitario

    #Cálculo de descuento según la cantidad de trajes
    if cantidad == 1:
        descuento = 0.10
    elif cantidad == 2:
        descuento = 0.20
    elif cantidad == 3:
        descuento = 0.40
    elif cantidad > 3:
        descuento = 0.60
    else:
        descuento = 0

    monto_descuento = subtotal * descuento
    total_pagar = subtotal - monto_descuento

    #Guardar la información en los arreglos
    nombres.append(nombre)
    apellidos.append(apellido)
    cantidades.append(cantidad)
    precios_unitarios.append(precio_unitario)
    totales.append(total_pagar)

    #Mostar información al usuario
    print("\nCliente: %s %s" % (nombre, apellido))
    print("Subtotal: $%.2f" % subtotal)
    print("Descuento aplicado: $%.2f" % monto_descuento)
    print("Total a pagar: $%.2f\n" % total_pagar)

    #Preguntar si se desea registar otro cliente
    continuar = input("¿Desea registrar otra compra? (s/n): ").lower()

#Mostar la información de todas las compras registradas
print("\n--- Resumen de compras registradas ---")
i = 0   #Contador para recorrer los arreglos
while i < len(nombres):
    print("Cliente: %s %s" % (nombres[i], apellidos[i]))
    print("Cantidad de trajes: %d" % cantidades[i])
    print("Precio unitario: $%.2f" % precios_unitarios[i])
    print("Total a pagar: $%.2f" % totales[i])
    print("-" * 30)
    i = i + 1

#Calcular el promedio de ventas
suma_totales = 0
i = 0
while i < len(totales):
    suma_totales = suma_totales + totales[i]
    i = i + 1

if len(totales) > 0:
    promedio_ventas = suma_totales / len(totales)
    print("\nPromedio de ventas realizadas: $%.2f" % promedio_ventas)

    #Determinar la venta más alta y la más baja
    venta_mas_alta = totales[0]
    venta_mas_baja = totales[0]
    i = 0
    while i < len(totales):
        if totales[i] > venta_mas_alta:
            venta_mas_alta = totales[i]
        if totales[i] < venta_mas_baja:
            venta_mas_baja = totales[i]
        i = i + 1
    print("Venta más alta: $%.2f" % venta_mas_alta)
    print("Venta más baja: $%.2f" % venta_mas_baja)
else:
    print("No se registraron ventas.")
input("\nPresione Enter para salir...")





