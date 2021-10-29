'''Ejercicio 1:
Revisa el programa anterior de este modo: Lee y analizalas líneas “From”
y extrae las direcciones de correo.
Cuenta elnúmerode mensajes de cada persona utilizando un diccionario.
Después de que todos los datos hayan sido leídos, imprime la persona con
más envíos,
creando una lista de tuplas (contador, email) del diccionario.
Después ordena la lista en orden inverso e imprime la persona que tiene
más envíos'''

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

            k_email = palabras[1]

            if k_email not in diccionario:
                # si el elmail no esta en el diccionario
                # sumo  1
                diccionario[k_email] = 1
                break
            else:
                # si el email esta como clave en el diccionario
                # sumo al valor de la clave mas 1
                diccionario[k_email] += 1
                break

# print(diccionario)

lst = list()
# ordeno el diccionario por valor
for clave, valor in list(diccionario.items()):
    lst.append((valor, clave))

lst.sort(reverse=True)

print(lst[0])
# muestro los 10 primeros
for clave, valor in lst[:10]:
    print(clave, valor)
