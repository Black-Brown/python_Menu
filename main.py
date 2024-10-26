def menu():
    print("=== MENU PRINCIPAL ===")
    print(
    "Ejercicios POO:\n"
        "1. Clase Persona\n"
        "2. Clase Cuenta\n"
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
    return choice

def main():
    while True:
        choice = menu()
        

if __name__ == "__main__":
    main()
