class Persona():
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_de_cuenta, balance):
        super().__init__(nombre, apellido)
        self.numero_de_cuenta = numero_de_cuenta
        self.balance = balance

    def __str__(self):
        return f"Numero de cuenta: {self.numero_de_cuenta}, Nombre: {self.nombre}, Apellido: {self.apellido}, Balance: {self.balance}"
    
    def depositar(self, monto):
        self.balance += monto

    def retirar(self, monto):
        if self.balance >= monto:
            self.balance -= monto
            print("El dinero fue retirado correctamente.")
        else:
            print("Error, saldo no disponible. Vuelva a intentarlo")

def inicio():
    print("=== Bienvenido al Banco ===")
    print()
    print("1 - Depositar")
    print("2 - Retirar")
    print("3 - Mostrar datos")
    print("4 - Salir")
       
def crear_cliente():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    return Cliente(nombre, apellido, 1110, 100)



un_cliente = crear_cliente()

opcion = 0

while opcion != 4:
    inicio()
    opcion = int(input("Ingrese una opción para continuar: "))

    if opcion == 1:
        monto = int(input("Ingrese la cantidad de dinero que quiere depositar: "))
        un_cliente.depositar(monto)
        print(f"El dinero fue depositado correctamente, su nuevo balance es: ${un_cliente.balance}")
        input("Presione Enter para volver al menu anterior... ")
    elif opcion == 2:
        print(f"Su balance es: {un_cliente.balance}")
        monto = int(input("Ingrese la cantidad de dinero que desea retirar: "))
        un_cliente.retirar(monto)
        print(f"Su balance es {un_cliente.balance}")
        input("Presione Enter para volver al menu anterior... ")
    elif opcion == 3:
        print("Sus datos son: ")
        print(un_cliente)
        input("Presione Enter para volver al menu anterior... ")
    else:
        print("Saliendo del programa...")
        break