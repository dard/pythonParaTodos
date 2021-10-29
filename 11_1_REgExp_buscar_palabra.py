'''Ejercicio uno:
escribe un programa simple que simule la operación del comando grep en Unix.
Debe pedir al usuario que ingrese una expresión regular y
cuente el número de líneas que coincidan con ésta:
$ python grep.py
Ingresa una expresión regular:
^Author
mbox.txt tiene 1798 líneas que coinciden con ^Author'''

import re

expresion = input('Ingrese una expresion regular: ')

fopen = open('mbox.txt')

diccionario = dict()
cont_lineas = 0
# expresion = '^Author'

for linea in fopen:
    # separo la linea en token palabras, creo la lista palabras
    linea = linea.rstrip()
    # con rstrip elimino espacios al final
    if re.search(expresion, linea):
        # print(linea)
        cont_lineas += 1
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


# print(diccionario)

lst = list()
# ordeno el diccionario por valor
for clave, valor in list(diccionario.items()):
    lst.append((valor, clave))

lst.sort(reverse=False)

# print(lst[0])
# muestro los 10 primeros [:10]
for valor, clave in lst:
    print(clave, '{:5d}'.format(valor))


print('Total de lineas ', '{:5d}'.format(cont_lineas), 'en el archivo %s ' % (fopen.name))
