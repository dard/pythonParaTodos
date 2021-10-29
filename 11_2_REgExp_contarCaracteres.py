'''Ejercicio 2:
escribe un programa que busque líneas en la forma:
New Revision: 39772 Extrae el número de cada línea usando una expresión regular
y el métodofindall().
Registra el promedio de esos números e imprímelo.
Ingresa nombre de archivo: mbox.txt
38444.0323119 Ingresa nombre de archivo: mbox-sh'''

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
cont_lineas = 0
numero = 0
num = 0
numStr = ''
promedio = 0.0
expresion = '^New Revision:\s([0-9]+)'

for linea in fopen:
    # separo la linea en token palabras, creo la lista palabras
    linea = linea.rstrip()
    # con rstrip elimino espacios al final
    numero = re.findall(expresion, linea)

    if numero:
        # print(type(numero))
        # print(linea)
        cont_lineas += 1
        num = int(numero[0])

        # num = int(numStr)
        # print(numero, num)

        if linea not in diccionario:
            # si la hora no esta en el diccionario
            # sumo  1
            diccionario[linea] = 1
            # break
        else:
            # si la hora esta como clave en el diccionario
            # sumo al valor de la clave mas 1
            diccionario[linea] += 1
            # break

promedio += num/cont_lineas

# print(diccionario)

lst = list()
# # ordeno el diccionario por valor
# for clave, valor in list(diccionario.items()):
#     lst.append((clave, valor))

# lst.sort(reverse=False)

# print(lst[0])
# # muestro los 10 primeros [:10]
# for clave, valor in lst:
#     print(clave, '{:5d}'.format(valor))


print('En el archivo %s ' % (nombre_archivo),
      'el total de lineas con nro de Revisión es ', '{:5d}'.format(cont_lineas))
print('El promedio es ', '{:6f}'.format(promedio))
