'''Ejercicio 2:
Este programa cuenta la distribución de la hora del día
para cada uno de los mensajes.
Puedes extraer la hora de la línea “From” buscando la cadena horaria
y luego dividiendo la cadena en partes utilizando el carácter colon.
Una vez que hayas acumulado las cuentas para cada hora,
imprime las cuentas, una por línea, ordenadas
por hora tal como se muestra debajo.'''

nombre_archivo = input('Ingrese el nombre del archivo: ')
try:
    fopen = open(nombre_archivo)
except Exception as e:
    print('Error. Ingrese un nombre correcto')
    print(e)
    raise
    exit()

diccionario = dict()

for linea in fopen:
    # separo la linea en token palabras, creo la lista palabras
    palabras = linea.split()
    for palabra in palabras:
        # recorro la lista palabras
        if len(palabras) != 0 and palabras[0] == 'From':
            cadenaHoraria = palabras[5]
            # print(cadenaHoraria)
            hora, minuto, segundos = cadenaHoraria.split(':')

            if hora not in diccionario:
                # si la hora no esta en el diccionario
                # sumo  1
                diccionario[hora] = 1
                break
            else:
                # si la hora esta como clave en el diccionario
                # sumo al valor de la clave mas 1
                diccionario[hora] += 1
                break

print(diccionario)

lst = list()
# ordeno el diccionario por valor
for clave, valor in list(diccionario.items()):
    lst.append((clave, valor))

lst.sort(reverse=False)

# print(lst[0])
# muestro los 10 primeros [:10]
for clave, valor in lst:
    print(clave, valor)
