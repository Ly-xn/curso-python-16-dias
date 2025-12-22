from random import choice

def recorrer_palabra(letra, vidas):
    indice = -1
    if letra in palabra_secreta:
        for l in palabra_secreta:
            indice += 1  
            if letra == l: 
                print(f"La letra se encuentra en la posicion {indice}")
                palabra_desbloqueada[indice] = letra
                return vidas
    else:
        print("La letra no se encuentra en la palabra secreta.")       
        vidas -= 1
        return vidas

def ingresar_letra():
    bandera = 0
    while bandera == 0:
        l = input("Ingrese una letra: ")
        if l.isalpha() == True:
            bandera = 1
            return l.lower()
        else:
            print("Ingrese una letra correcta.")
            bandera = 0


palabras = ["python", "manzana", "pera", "frutas", "computadora"]
palabra_secreta = choice(palabras)
lista_secreta = list(palabra_secreta)
cant_letras = len(palabra_secreta)
vidas = 6



print("=== BIENVENIDO AL JUEGO DEL AHORCADO ===")
print()
palabra_desbloqueada = list("-" * cant_letras)

while vidas >= 0:
    print(f"Cantidad de vidas actuales: {vidas}")
    print()
    print("Su palabra es:")
    print(palabra_desbloqueada)
    print()
    letra = ingresar_letra()
    
    vidas = recorrer_palabra(letra, vidas)

    if lista_secreta == palabra_desbloqueada:
        print("HAS GANADO!")
        print(f"La palabra era: {palabra_desbloqueada}")
        break
    else:
        pass
    print()

    




