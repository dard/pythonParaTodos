'''Ejercicio 2:
Este programa cuenta la distribución de la hora del día
para cada uno de los mensajes.
Puedes extraer la hora de la línea “From” buscando la cadena horaria
y luego dividiendo la cadena en partes utilizando el carácter colon.
Una vez que hayas acumulado las cuentas para cada hora,
imprime las cuentas, una por línea, ordenadas
por hora tal como se muestra debajo.'''
import re
nombre_archivo = input('Ingrese el nombre del archivo: ')
try:
    fopen = open(nombre_archivo)
except Exception as e:
    print('Error. Ingrese un nombre correcto')
    print(e)
    raise
    exit()

diccionario = dict()
hora_str = ""

print('*****************************')

for palabra in fopen:
    palabra = palabra.rstrip()
    hora = re.findall('^From .* ([0-9][0-9]):', palabra)
    if len(hora) > 0:
        hora_str = str(hora)
        if hora_str not in diccionario:
            # si la hora no esta en el diccionario
            # sumo  1
            diccionario[hora_str] = 1
            # break
        else:
            # si la hora esta como clave en el diccionario
            # sumo al valor de la clave mas 1
            diccionario[hora_str] += 1
            # break

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
