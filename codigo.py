"""coloca aqui los codigo de cada uno segun su orden"""
#------------------------------------------------------------------------------------
#Realizar un programa con dos funciones. La primera debe solicitar la carga de un
#valor entero y mostrar el cuadrado de dicho valor.

def numalcuadradro (num):
    resultado = print(input(num ** 2)) 
    return resultado 
#------------------------------------------------------------------------------------
#La segunda que solicite la carga
#de dos valores y muestre el producto de los mismos.

def numproducto (num1, num2):
    resultado = input(f"ingrese un numero:  {num1 * num2} ")
    return resultado
#------------------------------------------------------------------------------------
#Realizar un programa que tenga una función que reciba un string como parámetro.
#Debe mostrar la cantidad de vocales que tiene dicho string. Se deberá llamar 3
#veces desde el bloque principal, con 3 strings diferentes.

def contar_vocales(cadena):
    vocales = "aeiouAEIOU"
    contador = 0
    for letra in cadena:
        if letra in vocales:
            contador += 1
    return contador

for i in range(3):
    cadena = input(f"Ingrese la cadena {i+1}: ")
    cantidad_vocales = contar_vocales(cadena)
    print(f"La cantidad de vocales en '{cadena}' es: {cantidad_vocales}")

"""
Crear un módulo para validación de nombres de usuarios. Dicho módulo, deberá
cumplir con los siguientes criterios de aceptación:
El nombre de usuario debe contener un mínimo de 6 caracteres y un máximo
de 12.
El nombre de usuario debe ser alfanumérico.
Nombre de usuario con menos de 6 caracteres, retorna el mensaje "El
nombre de usuario debe contener al menos 6 caracteres".
Nombre de usuario con más de 12 caracteres, retorna el mensaje "El nombre
de usuario no puede contener más de 12 caracteres".
Nombre de usuario con caracteres distintos a los alfanuméricos, retorna el
mensaje "El nombre de usuario puede contener solo letras y números".

Nombre de usuario válido, retorna True.
"""

def validar_usuario(nombre_usuario):
    # Verificar la longitud del nombre de usuario
    if len(nombre_usuario) < 6:
        return "El nombre de usuario debe contener al menos 6 caracteres."
    elif len(nombre_usuario) > 12:
        return "El nombre de usuario no puede contener más de 12 caracteres."
    
    # Verificar si el nombre de usuario es alfanumérico
    if not nombre_usuario.isalnum():
        return "El nombre de usuario puede contener solo letras y números."
    
    # Si todas las validaciones pasan
    return True


# Bucle para pedir un nombre de usuario hasta que sea válido
while True:
    nombre = input("Introduce un nombre de usuario: ")
    resultado = validar_usuario(nombre)

    if resultado is True:
        print("Nombre de usuario válido.")
        break  # Salir del bucle si el nombre es válido
    else:
        print(resultado)  # Imprimir el mensaje de error

"""
20.Escribe un programa que almacene un número y pida al usuario
adivinarlo
"""

import random

def adivinar_numero():
    # Almacenar un número aleatorio entre 1 y 50
    numero_secreto = random.randint(1, 50)
    intentos = 0
    
    print("He elegido un número entre 1 y 50. ¡Intenta adivinarlo!")
    
    while True:
        intento = int(input("Introduce tu número: "))
        intentos += 1
        
        if intento < numero_secreto:
            print("Demasiado bajo. Intenta de nuevo.")
        elif intento > numero_secreto:
            print("Demasiado alto. Intenta de nuevo.")
        else:
            print(f"¡Felicidades! Adivinaste el número {numero_secreto} en {intentos} intentos.")
            break

# Llamar a la función
adivinar_numero()



