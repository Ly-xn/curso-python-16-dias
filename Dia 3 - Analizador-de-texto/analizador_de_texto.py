texto = input("Por favor, ingrese un texto: ").lower()

letra1 = input("Ingrese la 1era letra: ").lower()
letra2 = input("Ingrese la 2da letra: ").lower()
letra3 = input("Ingrese la 3er letra: ").lower()

#1er analisis: ¿cuántas veces aparece cada una de las letras que eligió?
print("=== Cantidad de veces que aparece las letras ===")
print(f"Cantidad de veces que aparece la letra {letra1} es {texto.count(letra1)}")
print(f"Cantidad de veces que aparece la letra {letra2} es {texto.count(letra2)}")
print(f"Cantidad de veces que aparece la letra {letra3} es {texto.count(letra3)}")
print()

#2do analisis: cuántas palabras hay a lo largo de todo el texto

print(f"La cantidad de palabras que hay a lo largo del texto es {len(texto.split(" "))}")
print()

#3er analisis: cCual es la priemra y cual es la ultima letra

print(f"La primera letra es {texto[0]}")
print(f"La ultima letra es {texto[-1]}")
print()

#4to analisis: Invertir el orden

lista = texto.split(" ")
lista.reverse()
texto_invertido = " ".join(lista)


print(f"El texto invertido es: {texto_invertido}")
print()

#5to: La palabra Python esta en el texto?

buscar_python = 'python' in texto # Esto devuelve True o False

# Creamos un "traductor" de Booleano a Humano
diccionario = {True: "Sí", False: "No"}

# Usamos el booleano como LLAVE para buscar la respuesta
print(f"¿La palabra Python se encuentra en el texto? Respuesta: {diccionario[buscar_python]}")
