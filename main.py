def menu():
    print("=== MENU PRINCIPAL ===")
    print(
    "Ejercicios POO:\n"
        "1. Ejercicio Personas\n"
        "2. Ejercicio Cuenta\n"
        "3. Clase Fracción\n"
        "4. Clase Complejo\n"
        "5. Cliente y Banco\n"
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
    choice = input("Elige una opcion (1-20): ")
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

        def mostrar(self):
            return self.mostrar    



def main():
    while True:
        choice = menu()
        if choice == "1":
            print("")
            ejercicio_persona()
            input("\nPresiona Enter para volver al menú...")

        elif choice == "21":
            print("saliendo del programa")
            break
        else:
            print("numero incorrecto")

        

if __name__ == "__main__":
    main()
