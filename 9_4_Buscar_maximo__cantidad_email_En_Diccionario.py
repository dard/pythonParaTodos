'''Agrega código al programa anterior para determinar quién
tiene la mayoría de mensajes en el archivo. Después de que
todos los datos hayan sido leídos y el diccionario haya sido creado,
mira a través del diccionario utilizando un bucle máximo
(ver Capítulo 5: Bucles máx-imos y mínimos)
para encontrar quién tiene la mayoría de
mensajes eimprimir cuántos mensajes tiene esa persona.'''

nombre_archivo = input('Ingrese el nombre del archivo: ')
try:
    fopen = open(nombre_archivo)
except Exception as e:
    print('Error. Ingrese un nombre correcto')
    print(e)
    raise
    exit()

diccionario = dict()
contador_email = 0
maximo = []


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

                contador_email += 1
                break
            else:
                # si el email esta como clave en el diccionario
                # sumo al valor de la clave mas 1
                diccionario[k_email] += 1
                contador_email += 1
                break
# email_max = max(maximo)
# print('Email con mas mensajes %s' % email_max)
print(diccionario)

mayor = 0
for clave in diccionario:
    # itero el diccionario y pregunto si es mayor, si clave es mayor
    # a mayor,guardo
    if diccionario[clave] > mayor:
        mayor = diccionario[clave]
# imprimo el resultado
print(clave, mayor)
