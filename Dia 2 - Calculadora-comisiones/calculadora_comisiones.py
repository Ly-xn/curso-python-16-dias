nombre = input("Ingrese su nombre: ")
ventas = float(input("Cuanto has vendido en este mes?: "))
porcentaje = 0.13
comisiones = round(ventas * porcentaje, 2)

print(f"Hola {nombre}, el monto de las comisiones por tus ventas en este mes son de: {comisiones}")
