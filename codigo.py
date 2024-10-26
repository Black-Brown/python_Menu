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

