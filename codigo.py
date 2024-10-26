"""coloca aqui los codigo de cada uno segun su orden"""
contador = 1
aprobados = 0
reprobados = 0


while contador <= 10:
    print(f'\nIngrese las notas del estudiante {contador}:')

    
    nota_1 = int(input('Ingrese la primera nota: '))
    nota_2 = int(input('Ingrese la segunda nota: '))
    nota_3 = int(input('Ingrese la tercera nota: '))
    nota_4 = int(input('Ingrese la cuarta nota: '))


    promedio = (nota_1 + nota_2 + nota_3 + nota_4) / 4
    print(f'El promedio del estudiante {contador} es de {promedio}')


    if promedio >= 90:
        print('El promedio fue excelente')
        aprobados += 1
    elif promedio >= 80:
        print('El promedio fue bueno')
        aprobados += 1
    elif promedio >= 70:
        print('El promedio es más o menos')
        aprobados += 1
    else:
        print('Reprobado')
        reprobados += 1

    contador += 1

print(f'\nTotal de estudiantes aprobados: {aprobados}')
print(f'Total de estudiantes reprobados: {reprobados}')


gana = 0
meno = 0
contador = 1
total_sueldos = 0
fuera_rango = 0


while contador <= 5:
    n = int(input(f'Ingrese el sueldo del empleado {contador} : '))

    if 100 <= n <= 1000:
        if n >= 500:
            print('Ganas más de 500')
            gana += 1
        else:
            print('Ganas menos de 500')
            meno += 1
        total_sueldos += n
        
    else:
        print('El sueldo que ingresó no está entre el rango de 100 y 1000')
        contador += 1



print(f'\nEl total de empleados que ganan más de 500 son: {gana}')
print(f'El total de empleados que ganan menos de 500 son: {meno}')
print(f'El sueldo total que gasta la empresa es de: {total_sueldos}')


contador = 1
aprobados = 0
reprobados = 0


while contador <= 10:
    print(f'\nIngrese las notas del estudiante {contador}:')

    
    nota_1 = int(input('Ingrese la primera nota: '))
    nota_2 = int(input('Ingrese la segunda nota: '))
    nota_3 = int(input('Ingrese la tercera nota: '))
    nota_4 = int(input('Ingrese la cuarta nota: '))


    promedio = (nota_1 + nota_2 + nota_3 + nota_4) / 4
    print(f'El promedio del estudiante {contador} es de {promedio}')


    if promedio >= 90:
        print('El promedio fue excelente')
        aprobados += 1
    elif promedio >= 80:
        print('El promedio fue bueno')
        aprobados += 1
    elif promedio >= 70:
        print('El promedio es más o menos')
        aprobados += 1
    else:
        print('Reprobado')
        reprobados += 1

    contador += 1

print(f'\nTotal de estudiantes aprobados: {aprobados}')
print(f'Total de estudiantes reprobados: {reprobados}')



suma_ultimos_5 = 0

for i in range(1, 11):
    numero = int(input(f'Ingrese el valor {i}: '))

    if i > 5:
        suma_ultimos_5 += numero


print(f'La suma de los últimos 5 valores ingresados es: {suma_ultimos_5}')
#------------------------------------------------------------------------------------
def numalcuadradro (num):
    resultado = print(input(num ** 2)) 
    return resultado 
#------------------------------------------------------------------------------------
def numproducto (num1, num2):
    resultado = input(f"ingrese un numero:  {num1 * num2} ")
    return resultado
#------------------------------------------------------------------------------------
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
#------------------------------------------------------------------------------------
def negativos_positivos(valores):
    negativos = []
    positivos = []
    
    for valor in valores:
        if valor < 0:
            negativos.append(valor)
        elif valor > 0:
            positivos.append(valor)
    
    return negativos, positivos

valores = [-3, 7, 0, 2, -1, 5, -4]  

# Separar y obtener las listas
negativos, positivos = negativos_positivos(valores)

# Imprimir resultados
print("Lista de valores negativos:", negativos)
print("Lista de valores positivos:", positivos)

#La segunda que solicite la carga
#de dos valores y muestre el producto de los mismos.
def adultos(edades):
    contador = 0
    for edad in edades:
        if edad >= 18:
            contador += 1
    return contador

# Bloque principal
edades = []

# Solicitar al usuario que ingrese al menos 3 edades
while len(edades) < 3:
    try:
        edad = int(input(f"Ingrese la edad {len(edades) + 1}: "))
        edades.append(edad)
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

# Contar cuántas personas son mayores de 18
cantidad_adultos = adultos(edades)

# Imprimir el resultado
print(f"La cantidad de personas con edad igual o superior a 18 es: {cantidad_adultos}")
#------------------------------------------------------------------------------------


