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

