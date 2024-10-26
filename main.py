def menu():
    print("")
    print("                                      === MENU PRINCIPAL ===")
    print("")
    print(
    "Ejercicios POO:\n"
        "1. Ejercicio Personas  | "
        "2. Ejercicio Cuenta\n"
        "3. Ejercicio Fraccion  | "
        "4. Ejercicio Complejo\n"
        "5. Cliente y Banco     | "
        "6. Clases Cuenta, Plazo Fijo y Caja Ahorro\n\n"
    
    "Ciclo While:\n"
        "7. Aprobados y Suspendidos de Alumnos\n"
        "8. Análisis de Sueldos de Empleados\n"
        "9. Aprobados y Suspendidos de Alumnos\n\n"
    
    "Ciclo For:\n"
        "10. Suma de Últimos 5 Números\n"
        "11. Tabla de Multiplicar\n"
        "12. Ingreso de Puntos en Cuadrantes\n"
        "13. Clasificación de Triángulos\n\n"
    
    "Funciones:\n"
        "14. Cuadrado y Producto de Números\n"
        "15. Conteo de Vocales en un String\n"
        "16. Separación de Números Positivos y Negativos\n"
        "17. Conteo de Personas Mayores de 18 Años\n\n"
    
    "Simples:\n"
        "18. Análisis de String\n\n"
    
    "Otros:\n"
        "19. Validación de Nombres de Usuario\n"
        "20. Adivina el Número"
    )
    print("")
    choice = input("Elige una opcion (1-20). Para salir (0): ")
    print("")
    return choice

def ejercicio_persona():
    print("\n--- Ejercicio Persona ---")
    class persnona:
        def __init__(self, nombre, apellido, edad, estadoCivil, numeroDocumentoIdentidad):
            self.nombre = nombre
            self.apellido = apellido
            self.edad = edad
            self.estadoCivil = estadoCivil
            self.numeroDocumentoIdentidad = numeroDocumentoIdentidad

        def obtener_nombre(self):
            return self.nombre

        def establecer_nombre(self, nombre):
            self.nombre = nombre
        
        def obtener_apellido(self):
            return self.apellido

        def establecer_apellido(self, apellido):
            self.apellido = apellido

        def obtener_edad(self):
            return self.edad

        def establecer_edad(self, edad):
            self.edad = edad

        def obtener_estadoCivil(self):
            return  self.estadoCivil

        def establecer_estadoCivil(self, estadoCivil):
            self.estadoCivil = estadoCivil
            
        def obtener_numeroDocumentoIdentidad(self):
            return self.numeroDocumentoIdentidad
        
        def establecer_numeroDocumentoIdentidad(self, numeroDocumentoIdentidad):
            self.numeroDocumentoIdentidad = numeroDocumentoIdentidad
        
    persona1 = persnona("Harry", "Potter", 17, False, 203471235)
    print(f"la edad de {persona1.nombre} es {persona1.obtener_edad()}")

    persona2 = persnona("Hermione", "Granger", 17, False, 203896545)
    print(f"el estado civil de {persona2.nombre} es: {persona2.estadoCivil}")

    persona3 = persnona("Ron", "Weasly", 0, False, 203964235)
    persona3.establecer_edad(45)
    print(f"el senior {persona3.apellido} tiene {persona3.obtener_edad()} anios")

    persona4 = persnona("Albus", "", 68, False, 203101255)
    persona4.establecer_apellido("Dumbledore")
    print(f"el apellido del senior {persona4.nombre} es {persona4.obtener_apellido()}")

    persona5 = persnona("Sirius", "Black", 45, False, 203785235)
    print(f"la identificacion del senior {persona5.apellido} es: {persona5.obtener_numeroDocumentoIdentidad()}")

    persona6 = persnona("Draco", "Malfoy", 17, False, 0)
    persona6.establecer_numeroDocumentoIdentidad(203366575)
    print(f"la nueva identificacion del senior {persona6.nombre} es {persona6.obtener_numeroDocumentoIdentidad()}")

    persona7 = persnona("Bellatrix ", "Lestrange", 49, False, 203894225)
    persona7.establecer_estadoCivil(True)
    print(f"la seniorita {persona7.nombre} es casada: {persona7.obtener_estadoCivil()}")
    print("")

def ejecicio_cuenta():
    print("\n--- Ejercicio Cuenta ---")

    class Cuenta:
        def __init__(self, saldo):
            self.saldo = saldo
                
        def ingresar(self, monto):
            if monto > 0:
                self.saldo += monto
                print(f"ingreso realizado. Nuevo saldo es: {self.saldo}")
            else:
                print(f"el monto debe ser positivo para realizar el ingreso")
        
        def reintegro(self, monto):
            if monto > 0 and monto <= self.saldo:
                self.saldo -= monto
                print(f"reintegro realizado. Nuevo saldo es: {self.saldo}")
            else:
                print(f"el monto es invalido para realizar el reintegro")
        
        def transferecias(self, otra_cuenta, monto):
            if monto > 0 and monto <= self.saldo:
                self.saldo -= monto
                otra_cuenta.ingresar(monto)
                print(f"transferencia realizada. Nuevo saldo: {self.saldo}")
            else:
                print("el monto es inválido para realizar la transferencia.")

        def mostrar(self):
            print(f"saldo actual: {self.saldo}")   

    cuenta1 = Cuenta(100)
    cuenta2 = Cuenta(50) 

    while True:
        print(
            "\n--- Menu de Cuenta ---"
            "\n1. Ingresar Dinero"
            "\n2. Reintegro de Dinero"
            "\n3. Transferencias Bancarias"
            "\n4. Mostrar Saldo"
            "\n5. Salir"
        )
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                monto = float(input("Digite la cantidad a ingresar: "))
                print("")
                cuenta1.ingresar(monto)
                input("\nPresiona Enter para volver al menu de cuenta...")
            except ValueError:
                print("Ingrese un número válido.")
        
        elif opcion == "2":
            try:
                monto = float(input("Digite la cantidad a retirar: "))
                print("")
                cuenta1.reintegro(monto)
                input("\nPresiona Enter para volver al menu de cuenta...")
            except ValueError:
                print("Ingrese un número válido.")

        elif opcion == "3":
            try:
                monto = float(input("Ingrese la cantidad a transferir: "))
                print("")
                cuenta1.transferencias(cuenta2, monto)
                input("\nPresiona Enter para volver al menu de cuenta...")
            except ValueError:
                print("Ingrese un número válido.")
        
        elif opcion == "4":
            print("")
            cuenta1.mostrar()
            input("\nPresiona Enter para volver al menu de cuenta...")

        elif opcion == "5":
            print("Saliendo del menú de cuenta.")
            break

        else:
            print("Digite un número válido.")

def ejercicio_fraccion():
    print("\n--- Ejercicio Fraccion ---")
    print("")

    from math import gcd 

    class Fraccion:
        def __init__(self, numerador, denominador):
            if denominador == 0:
                raise ValueError("el denominador no debe estar en cero")
            self.numerador = numerador
            self.denominador = denominador
            self.simplificar()
         
        def simplificar(self):
            divisor_comun = gcd(self.numerador, self.denominador)
            self.numerador //= divisor_comun
            self.denominador //= divisor_comun

        def suma(self, otra):
            nuevo_numerador = (self.numerador * otra.denominador) + (otra.denominador * self.numerador) 
            nuevo_denominador = self.denominador * self.denominador
            resultado = Fraccion(nuevo_numerador, nuevo_denominador)
            resultado.simplificar()
            return resultado 

        def restar(self, otra):
            nuevo_numerador = (self.numerador * otra.denominador) - (otra.denominador * self.numerador) 
            nuevo_denominador = self.denominador * self.denominador
            resultado = Fraccion(nuevo_numerador, nuevo_denominador)
            resultado.simplificar()
            return resultado 

        def multiplicar(self, otra):
            nuevo_numerador = self.numerador * otra.numerador  
            nuevo_denominador = self.denominador * otra.denominador
            resultado = Fraccion(nuevo_numerador, nuevo_denominador)
            resultado.simplificar()
            return resultado 
        
        def dividir(self, otra):
            nuevo_numerador = self.numerador * otra.denominador  
            nuevo_denominador = self.denominador * otra.numerador
            resultado = Fraccion(nuevo_numerador, nuevo_denominador)
            resultado.simplificar()
            return resultado 
        
        def __str__(self):
            return f"{self.numerador} / {self.denominador}"
        
    numerador1 = int(input("ingrese el numerador de la primera fraccion: "))
    denominador1 = int(input("ingrese el denominador de la primera fraccion: "))
    Fraccion1 = Fraccion(numerador1, denominador1)
    print("")

    numerador2 = int(input("ingrese el numerador de la segunda fraccion: "))
    denominador2 = int(input("ingrese el denominador de la segunda fraccion: "))
    Fraccion2 = Fraccion(numerador2, denominador2)
    print("")

    print(f"{numerador1} / {denominador1}")
    print(f"{numerador2} / {denominador2}")
    print("")

    suma = Fraccion1.suma(Fraccion2)
    print(f"Suma: {suma}")
    print("")

    resta = Fraccion1.restar(Fraccion2)
    print(f"resta: {resta}")
    print("")

    multiplicar = Fraccion1.multiplicar(Fraccion2)
    print(f"multiplicar: {multiplicar}")
    print("")

    dividir = Fraccion1.dividir(Fraccion2)
    print(f"dividir: {dividir}")
    print("")

def ejercicio_complejo():
    print("\n--- Ejercicio Complejo ---")
    print("")

    class Complejo:

        def __init__(self, real, imaginario):
            self.real = real
            self.imaginario = imaginario
            
        def __str__(self):
            signo = "+" if self.imaginario >= 0 else "-"
            return f"{self.real} {signo} {abs(self.imaginario)}i"
        
        def suma(self, otro):
            real = self.real + otro.real
            imaginario = self.imaginario + otro.imaginario
            return Complejo(real, imaginario)

        def resta(self, otro):
            real = self.real - otro.real
            imaginario = self.imaginario - otro.imaginario
            return Complejo(real, imaginario)

        def multiplicar(self, otro):
            real = self.real * otro.real - self.imaginario * otro.imaginario
            imaginario = self.real * otro.imaginario + self.imaginario * otro.real
            return Complejo(real, imaginario)

        def dividir(self, otro):
            if otro.real == 0 and otro.imaginario == 0:
                raise ValueError("No se puede dividir por cero")
            divisor = otro.real**2 + otro.imaginario**2
            real = (self.real * otro.real + self.imaginario * otro.imaginario) / divisor
            imaginario = (self.imaginario * otro.real - self.real * otro.imaginario) / divisor
            return Complejo(real, imaginario)
        
    real1 = float(input("ingrese la parte real del primer numero complejo: "))
    imag1 = float(input("ingrese la parte imaginaria del primer número complejo: "))
    print("")

    real2 = float(input("ingrese la parte real del segundo numero complejo: "))
    imag2 = float(input("ingrese la parte imaginaria del segundo numero complejo: "))

    complejo1 = Complejo(real1, imag1)
    complejo2 = Complejo(real2, imag2)

    print("\nResultados de operaciones entre números complejos:")
    print(f"{complejo1} + {complejo2} = {complejo1.suma(complejo2)}")
    print(f"{complejo1} - {complejo2} = {complejo1.resta(complejo2)}")
    print(f"{complejo1} * {complejo2} = {complejo1.multiplicar(complejo2)}")
    try:
        print(f"{complejo1} / {complejo2} = {complejo1.dividir(complejo2)}")
    except ValueError as e:
        print(e)

def cliente_banco():
    print("\n--- Cliente y Banco  ---")
    print("")

    class Cliente:
        def __init__(self, nombre, cantidad_inicial):
            self.nombre = nombre
            self.cantidad = cantidad_inicial

        def depositar(self, monto):
            if monto > 0:
                self.cantidad += monto
                print(f"{self.nombre} deposito {monto}. Saldo actual: {self.cantidad}")
            else:
                print("El monto debe ser positivo para depositar")

        def extraer(self, monto):
            if 0 < monto <= self.cantidad:
                self.cantidad -= monto
                print(f"{self.nombre} retiro {monto}. Saldo actual: {self.cantidad}")
            else:
                print("El monto es invalido o insuficiente para retirar.")

        def mostrar_total(self):
            print(f"{self.nombre} tiene un saldo de: {self.cantidad}")
            return self.cantidad


    class Banco:
        def __init__(self):
            self.clientes = [
                Cliente("Cliente 1", 1000),
                Cliente("Cliente 2", 1500),
                Cliente("Cliente 3", 2000)
            ]

        def operar(self):
            self.clientes[0].depositar(500)
            self.clientes[1].extraer(300)
            self.clientes[2].depositar(1000)

        def deposito_total(self):
            total = sum(cliente.mostrar_total() for cliente in self.clientes)
            print(f"Deposito total en el banco: {total}")

    banco = Banco()
    banco.operar()        
    banco.deposito_total() 

def clase_cuenta():
    print("\n--- Clases Cuenta, Plazo Fijo y Caja Ahorro ---")
    print("")

    class Cuenta:
        def __init__(self, titular, cantidad):
            self.titular = titular
            self.cantidad = cantidad

        def imprimir_datos(self):
            print(f"Titular: {self.titular}")
            print(f"Cantidad: {self.cantidad}")


    class CajaAhorro(Cuenta):
        def __init__(self, titular, cantidad):
            super().__init__(titular, cantidad)

        def mostrar_informacion(self):
            print("\n--- Información de Caja de Ahorro ---")
            self.imprimir_datos()


    class PlazoFijo(Cuenta):
        def __init__(self, titular, cantidad, plazo, interes):
            super().__init__(titular, cantidad)
            self.plazo = plazo
            self.interes = interes

        def calcular_importe_interes(self):
            return self.cantidad * self.interes / 100

        def mostrar_informacion(self):
            print("\n--- Información de Plazo Fijo ---")
            self.imprimir_datos()
            print(f"Plazo: {self.plazo} meses")
            print(f"Interés: {self.interes}%")
            print(f"Total de interés: {self.calcular_importe_interes()}")

    caja_ahorro = CajaAhorro("Ana Perez", 1500)
    plazo_fijo = PlazoFijo("Juan Gomez", 2000, 12, 5)


    caja_ahorro.mostrar_informacion()
    plazo_fijo.mostrar_informacion()

        
def main():
    while True:
        choice = menu()
        if choice == "1":
            print("")
            ejercicio_persona()
            input("\nPresiona Enter para volver al menú...")

        elif choice == "2":
            print("")
            ejecicio_cuenta()
            input("\nPresiona Enter para volver al menú...")
        
        elif choice == "3":
            print("")
            ejercicio_fraccion()
            input("\nPresiona Enter para volver al menú...")

        elif choice == "4":
            print("")
            ejercicio_complejo()
            input("\nPresiona Enter para volver al menú...")
        
        elif choice == "5":
            print("")
            cliente_banco()
            input("\nPresiona Enter para volver al menú...")

        elif choice == "6":
            print("")
            clase_cuenta()
            input("\nPresiona Enter para volver al menú...")

        elif choice == "0":
            print("saliendo del programa")
            break
        else:
            print("numero incorrecto")

        

if __name__ == "__main__":
    main()

# def numalcuadradro (num):
#     resultado = print(input(num ** 2)) 
#     return resultado 

# def numproducto (num1, num2):
#     resultado = input(f"ingrese un numero:  {num1 * num2} ")
#     return resultado

# def contar_vocales(cadena):
#     vocales = "aeiouAEIOU"
#     contador = 0
#     for letra in cadena:
#         if letra in vocales:
#             contador += 1
#     return contador

# for i in range(3):
#     cadena = input(f"Ingrese la cadena {i+1}: ")
#     cantidad_vocales = contar_vocales(cadena)
#     print(f"La cantidad de vocales en '{cadena}' es: {cantidad_vocales}")

# def contar_vocales(cadena):
#     vocales = "aeiouAEIOU"
#     contador = 0
#     for letra in cadena:
#         if letra in vocales:
#             contador += 1
#     return contador

# for i in range(3):
#     cadena = input(f"Ingrese la cadena {i+1}: ")
#     cantidad_vocales = contar_vocales(cadena)
#     print(f"La cantidad de vocales en '{cadena}' es: {cantidad_vocales}")
    
    
# #Realizar un programa que cargue una lista de n valores enteros. Generar dos listas,
# #una con valores negativos y otra con los valores positivos e imprimir ambas listas.

# def negativos_positivos(valores):
#     negativos = []
#     positivos = []
    
#     for valor in valores:
#         if valor < 0:
#             negativos.append(valor)
#         elif valor > 0:
#             positivos.append(valor)
    
#     return negativos, positivos

# valores = [-3, 7, 0, 2, -1, 5, -4]  

# # Separar y obtener las listas
# negativos, positivos = negativos_positivos(valores)

# # Imprimir resultados
# print("Lista de valores negativos:", negativos)
# print("Lista de valores positivos:", positivos)

# #La segunda que solicite la carga
# #de dos valores y muestre el producto de los mismos.
# def adultos(edades):
#     contador = 0
#     for edad in edades:
#         if edad >= 18:
#             contador += 1
#     return contador

# # Bloque principal
# edades = []

# # Solicitar al usuario que ingrese al menos 3 edades
# while len(edades) < 3:
#     try:
#         edad = int(input(f"Ingrese la edad {len(edades) + 1}: "))
#         edades.append(edad)
#     except ValueError:
#         print("Por favor, ingrese un número entero válido.")

# # Contar cuántas personas son mayores de 18
# cantidad_adultos = adultos(edades)

# # Imprimir el resultado
# print(f"La cantidad de personas con edad igual o superior a 18 es: {cantidad_adultos}")



