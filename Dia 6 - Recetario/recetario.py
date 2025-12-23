from pathlib import Path
import os

def limpiar_consola():
    if os.name == 'nt': 
        os.system('cls')
    else: 
        os.system('clear')

def menu():
    """
    Muestra por pantalla las distintas opciones que tiene el usuario
    """
    print("1 - Mostrar receta")
    print("2 - Crear receta")
    print("3 - Crear categoria")
    print("4 - Eliminar receta")
    print("5 - Eliminar categoria")
    print("6 - Salir")

def ingresar_directorio(ruta, nombre_carpeta):
    """
    Combina la ruta base con el nombre de la carpeta deseada.
    
    :param ruta: Recibe la ruta base (Objeto Path).
    :param nombre_carpeta: Recibe el nombre de la carpeta a acceder (str).
    :return: Objeto Path con la ruta completa.
    """
    nombre_carpeta = nombre_carpeta.capitalize()
    carpeta_destino = ruta / nombre_carpeta
    return carpeta_destino

def mostrar_categorias(ruta):
    """
    Muestra por pantalla las distintas carpetas que hay en la ruta especificada.
    
    :param ruta: Objeto Path del directorio raíz de recetas.
    """
    print("=== Categorias === ")
    for carpetas in ruta.iterdir():
        print(f"- {carpetas.name}") 

def abrir_recetas(ruta, nombre_carpeta):
    """
    Muestra las recetas de una categoría y permite leer su contenido.
    
    :param ruta: La ruta base del sistema.
    :param nombre_carpeta: El nombre de la categoría seleccionada.
    """
    nombre_carpeta = nombre_carpeta.capitalize()
    carpeta_categoria = ruta / nombre_carpeta
    lista_recetas = list(carpeta_categoria.glob("*.txt"))
    if len(lista_recetas) == 0:
        print("=== No hay recetas acá. ===")
        input("Presiona Enter para volver...")
        return
    
    print("=== TIENE ESTAS RECETAS ===")
    for r in carpeta_categoria.iterdir():
        print(f"- {r.name}")
    receta_elegida = input("Ingrese la receta que quiere leer: ")
    if not receta_elegida.endswith(".txt"):
        receta_elegida += ".txt"
    receta = carpeta_categoria / receta_elegida
    print(receta.read_text()) 
    print()


def mostrar_receta(ruta):
    """
    Le pide al usuario una categoria y utiliza la funcion abrir_recetas, 
    para abrir las recetas que hay en esa categoria
    
    :param ruta: Objeto Path del directorio raíz de recetas.
    """
    mostrar_categorias(ruta)
    categoria = input("Ingrese una categoria: ")
    abrir_recetas(ruta, categoria)
    opcion = input("Ingrese 'S' para volver al menu anterior: ")
    if opcion.lower() == 's':
        return

def crear_receta(ruta):
    """
    Crea un archivo .txt con el nombre de la receta y escribe su contenido en ella.
    
    :param ruta: Objeto Path del directorio raíz de recetas.
    """

    mostrar_categorias(ruta)    
    categoria = input("Ingrese una categoria: ") 
    ruta_categoria = ingresar_directorio(ruta, categoria)
    nombre_receta = input("Ingrese el nombre de la receta: ") + ".txt"
    contenido = input("Ingrese el contenido de la receta: ")
    archivo_nuevo = ruta_categoria / nombre_receta
    archivo_nuevo.write_text(contenido)
    print("=== LA RECETA FUE CREADA CON EXITO ===")

def crear_carpeta(ruta, nombre_carpeta):
    carpeta_nueva = ruta / nombre_carpeta
    carpeta_nueva.mkdir()
    

def crear_categoria(ruta):
    """
    Le pide al usuario una categoria y hace uso de la funcion crear_carpeta, para crear dicha carpeta con esa categoria
    
    :param ruta: Objeto Path del directorio raíz de recetas.
    """
    categoria = input("Ingrese el nombre de la categoria que quiere crear: ")
    crear_carpeta(ruta, categoria)
    print("=== LA CATEGORIA FUE CREADA CON EXITO ")
    print()
    opcion = input("Ingrese 'S' para volver al menu anterior: ")
    if opcion.lower() == 's':
        return

def eliminar_archivo(ruta, nombre_carpeta):
    """
    Ingresa al directorio donde se encuentre la receta y la elimina haciendo uso de os.remove()
    
    :param ruta: Objeto Path del directorio raíz de recetas.
    :param nombre_carpeta: El nombre de la carpeta (categoria) a la cual desea acceder
    """
    nombre_carpeta = nombre_carpeta.capitalize()
    carpeta_categorias = ruta / nombre_carpeta
    lista_recetas = list(carpeta_categorias.glob("*.txt"))
    if len(lista_recetas) == 0:
        print("=== No hay recetas acá. ===")
        input("Presiona Enter para volver...")
        return
    print("=== TIENE ESTAS RECETAS ===")
    
    for r in lista_recetas: 
        print(f"- {r.name}")
    receta_elegida = input("Ingrese la receta que quiere eliminar: ")
    if not receta_elegida.endswith(".txt"):
        receta_elegida += ".txt"

    receta = carpeta_categorias / receta_elegida
    
    if not receta.exists():
        print(f"Error: La receta '{receta.name}' no existe.")
        input("Presiona Enter para volver...")
        return
    opcion_borrar = input("¿Estas seguro/a que quieres eliminar esta receta? Si/No: ")

    if opcion_borrar.lower() == "si":
        os.remove(receta)
        print()
        print("=== LA RECETA FUE BORRADA CON EXITO ===")
    else:
        print("No se borró la receta")

    opcion = input("Ingrese 'S' para volver al menu anterior: ")
    if opcion.lower() == 's':
        
        return
    print()


def eliminar_receta(ruta):
    """
    Le pide al usuario una categoria y hace uso de la funcion eliminar_archivo() para borrar una receta
    
    :param ruta: Objeto Path del directorio raíz de recetas.
    """
    mostrar_categorias(ruta)
    categoria = input("Ingrese una categoria: ")
    eliminar_archivo(ruta, categoria)

def eliminar_carpeta(ruta, nombre_carpeta):
    """
    Crea un ruta mediante la ruta raiz de carpetas y el nombre de la carpeta (categoria) y la elimina usando os.rmdir()
    
    :param ruta: Objeto Path del directorio raíz de recetas
    :param nombre_carpeta: El nombre de la carpeta (categoria)
    """
    ruta_receta = ruta / nombre_carpeta
    os.rmdir(ruta_receta) 

def eliminar_categoria(ruta):
    """
    Hace uso de la funcion eliminar_carpeta() para eliminar una carpeta (categoria). 
    Pregunta al usuario para confirmar si quiere eliminarla o no.
    
    :param ruta: Objeto Path del directorio raíz de recetas.
    """
    mostrar_categorias(ruta)
    categoria = input("Ingrese la categoria que quiere eliminar: ")
    opcion = input("¿Seguro que quiere eliminar esta categoria?: Si/No: ")
    if opcion.lower() == "si":
        eliminar_carpeta(ruta, categoria)
        print("=== LA CATEGORIA FUE BORRADA CON EXITO ===")
        input("Presiona Enter para volver...")
        return
    else:
        print("La categoria no fue borrada")
        input("Presiona Enter para volver...")
        return
    

print("=== BIENVENIDO AL RECETARIO ===")
print()
print("La carpeta Recetas se encuentra en: ")
ruta = Path.cwd() / "Recetas"
print(ruta)
print()
opcion = 0

while opcion != 6:
    limpiar_consola()
    menu()
    opcion = int(input("Eliga una opcion: "))
    if opcion == 1:
        mostrar_receta(ruta)
    elif opcion == 2:
        crear_receta(ruta)
    elif opcion == 3:
        crear_categoria(ruta)
    elif opcion == 4:
        eliminar_receta(ruta)
    elif opcion == 5:
        eliminar_categoria(ruta)