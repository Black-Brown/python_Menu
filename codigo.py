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

#parte de Ronny
#Ejercicios de Ronny
#Ciclo For
#Tabla de multiplicar 1 al 12

#Pedimos el numero
num = int(input("Ingresa un valor del 1 al 10: "))

#Bucle para multiplicar el numero ingresado por la tabla
if 1 <= num <= 10: #num debe estar entre 1 y 10
    for i in range(1,12):
        print(f"{num} x {i} = {num * i}")
else:
    print("Todo numero multiplicado por 0 =  0")

#-------------------------------------------------------------------------------------
#Realizar un programa que pida ingresar dos datos enteros (coordenadas x e y). Al 
# comenzar el programa se pedirá ingresar el total de puntos a procesar. Informar de 
# cuantos puntos se han ingresado en cada uno de los cuatro cuadrantes.

# Contadores para cada cuadrante
cuadrante_1 = 0
cuadrante_2 = 0
cuadrante_3 = 0
cuadrante_4 = 0

# Pedir al usuario el total de puntos a procesar
puntos_totales = int(input("Ingresa el total de puntos a procesar: "))

# Se procesa cada punto
for i in range(puntos_totales):
    coord_x = int(input(f"Ingrese la coordenada x del punto {i + 1}: "))
    coord_y = int(input(f"Ingrese la coordenada y del punto {i + 1}: "))
    
    # Saber en qué cuadrante se encuentra el punto
    if coord_x > 0 and coord_y > 0:
        cuadrante_1 += 1
    elif coord_x < 0 and coord_y > 0:
        cuadrante_2 += 1
    elif coord_x < 0 and coord_y < 0:
        cuadrante_3 += 1
    elif coord_x > 0 and coord_y < 0:
        cuadrante_4 += 1

# Resultados
print(f"Puntos en el cuadrante 1: {cuadrante_1}")
print(f"Puntos en el cuadrante 2: {cuadrante_2}")
print(f"Puntos en el cuadrante 3: {cuadrante_3}")
print(f"Puntos en el cuadrante 4: {cuadrante_4}")

#-------------------------------------------------------------------------------------
# Realizar un programa que pida ingresar dos datos enteros (coordenadas x e y). Al 
# comenzar el programa se pedirá ingresar el total de puntos a procesar. Informar de 
# cuantos puntos se han ingresado en cada uno de los cuatro cuadrantes.

# Función para clasificar el tipo de triángulo
def clasificar_triangulo(lado1, lado2, lado3):
    if lado1 == lado2 == lado3:
        return "equilátero"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        return "isósceles"
    else:
        return "escaleno"

# Función principal
def princip():
    #números de triángulos
    n = int(input("Ingrese la cantidad de triángulos a clasificar: "))
    
    # Contadores para cada tipo de triángulo
    equilateros = 0
    isosceles = 0
    escalenos = 0

    # clasificaciion
    for i in range(n):
        print(f"\nTriángulo {i + 1}:")
        lado1 = float(input("Ingrese el primer lado: "))
        lado2 = float(input("Ingrese el segundo lado: "))
        lado3 = float(input("Ingrese el tercer lado: "))
        
        tipo = clasificar_triangulo(lado1, lado2, lado3)
        
        # Tipo de triangulo
        print(f"El triángulo {i + 1} es {tipo}.")
        
        # Incrementar el contador de cada var
        if tipo == "equilátero":
            equilateros += 1
        elif tipo == "isósceles":
            isosceles += 1
        elif tipo == "escaleno":
            escalenos += 1

    # Totales
    print("\nResumen:")
    print(f"Total de triángulos equiláteros: {equilateros}")
    print(f"Total de triángulos isósceles: {isosceles}")
    print(f"Total de triángulos escalenos: {escalenos}")


princip()

#-------------------------------------------------------------------------------------
#Funciones 
# Realizar un programa con dos funciones. La primera debe solicitar la carga de un 
# valor entero y mostrar el cuadrado de dicho valor. La segunda que solicite la carga 
# de dos valores y muestre el producto de los mismos. Deberán llamar a estas dos 
# funciones desde el bloque principal (Fuera de toda función, como en el ejemplo 
# realizado al principio de este tema).


def cuadrado():
    num1 = int(input("Ingrese el primer numero: "))
    result_cuadrado = num1**2
    print( f" {num1}^2 = {result_cuadrado}")

def producto():
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))
    result_producto = num1 * num2
    print (f"{num1} x {num2} = {result_producto}")

cuadrado()
producto()

#-------------------------------------------------------------------------------------
# Realizar un programa que tenga una función que reciba un string como parámetro. 
# Debe mostrar la cantidad de vocales que tiene dicho string. Se deberá llamar 3 
# veces desde el bloque principal, con 3 strings diferentes. 

def contar_vocales(texto):
    try:
        if not texto.isalpha(): #verificar si hay un numero en el texto
            raise ValueError("El texto no debe contener numeros, ni caracteres especiales.")   #forzar manejo de error
            
        vocales = 'aeiou'
        cant_vocales = sum(1 for letra in texto.lower() if letra in vocales)    #se suma 1 a cant_vocales si en si en texto hay una vocal
        print(f"{texto} tiene {cant_vocales} vocales")
            
    except ValueError as error:
            print("¡Ha ocurrido un error!: ",error) #imprime el error

contar_vocales('0')
contar_vocales('Ronny')
contar_vocales('ITLA')  
#fin de la parte de Ronny

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
#------------------------------------------------------------------------------------
#Realizar un programa que cargue una lista de n valores enteros. Generar dos listas,
#una con valores negativos y otra con los valores positivos e imprimir ambas listas.

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

#fin de la parte de ricardo alexander
#------------------------------------------------------------------------------------


