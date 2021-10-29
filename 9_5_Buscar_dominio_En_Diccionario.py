'''Ejercicio 5: Este programa almacena el nombre del dominio
(en vez dela dirección) desde donde fue enviado el mensaje
en vez de quiénenvióel mensaje (es decir, la dirección de
correo electrónica completa). Alfinal del programa,
imprime el contenido de tu diccionario.'''

nombre_archivo = input('Ingrese el nombre del archivo: ')
try:
    fopen = open(nombre_archivo)
except Exception as e:
    print('Error. Ingrese un nombre correcto')
    print(e)
    raise
    exit()

diccionario = dict()
contador_dominio = 0


for linea in fopen:
    # separo la linea en token palabras, creo la lista palabras
    palabras = linea.split()
    for palabra in palabras:
        # recorro la lista palabras
        # verifico que no sea una linea en blanco y que empiece con From
        if len(palabras) != 0 and palabras[0] == 'From':
            # busco en la cadena el caracter @,
            # si da -1, no lo encuentra y continua
            if palabra.find('@') == -1:
                continue
            # si no guardo la posicion de arroba
            else:
                pos_arroba = palabra.find('@')
                # rebano la palabra y extaigo el dominio
                dominio = palabra[pos_arroba + 1:]
                # depurar
                # print(palabra)
                # print(dominio)

            if dominio not in diccionario:
                # si el dominio no esta en el diccionario
                # sumo  1
                diccionario[dominio] = 1
                contador_dominio += 1
                break
            else:
                # si el dominio esta como clave en el diccionario
                # sumo al valor de la clave mas 1
                diccionario[dominio] += 1
                contador_dominio += 1
                break

print('El diccionario quedo conformado: ')
print(diccionario)
