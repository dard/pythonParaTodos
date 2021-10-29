'''Escribe un programa para leer a través de un historial de correos,
 construye un histograma utilizando un diccionario para contar cuántos
  mensajes han llegado de cada dirección de correo electrónico,
   e imprime el diccionario'''

nombre_archivo = input('Ingrese el nombre del archivo: ')
try:
    fopen = open(nombre_archivo)
except Exception as e:
    print('Error. Ingrese un nombre correcto')
    print(e)
    raise
    exit()

diccionario = dict()
buscar_From = ''
contador_email = 0


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

print('Cantidad de emails %d' % contador_email)
print(diccionario)
