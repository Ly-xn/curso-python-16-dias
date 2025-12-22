from random import randint
nombre = input("Ingrese su nombre: ")
intentos = 8
intentos_tomados = 0

print(f"Bueno, {nombre}, he pensado un número entre 1 y 100, y tienes solo ocho intentos para adivinar cuál crees que es el número")
random_number = randint(1,100)


while intentos > 0:
    intentos_tomados += 1    
    print(f"Cantidad de intentos disponibles: {intentos}")
    numero = int(input("Ingrese un numero entero del [1-100]: "))
    if numero < 0 or numero > 100:
        print("Ingresó un numero no permitido.")
    elif numero < random_number:
        print("Incorrecto. Usted a elegido un numero menor al numero secreto.")
    elif numero > random_number:
        print("Incorrecto. Usted a elegido un numero mayor al numero secreto.")      
    else:
        print(f"Usted ha ganado. Le tomo la cantidad de {intentos_tomados} intentos")
        break
    intentos -= 1
    
if intentos == 0:
    print(f"Usted ha perdido. El numero secreto era {random_number}")