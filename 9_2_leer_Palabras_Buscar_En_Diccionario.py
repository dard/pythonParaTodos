'''Escribir un programa que clasifica cada mensaje de correo dependiendo
del día de la semana en que se recibió. Para haceresto busca las líneas
que comienzan con “From”, después busca porla tercerpalabra
y mantén un contador para cada uno de los días de la semana.
Al final del programa imprime los contenidos
de tu diccionario (el ordenno importa'''

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
contador = 0
contador2 = 0


for linea in fopen:
    palabras = linea.split()
    contador2 += 1
    for palabra in palabras:
        if len(palabras) != 0 and palabras[0] == 'From':
            contador += 1
            print(contador2, linea, contador)

            k_dia = palabras[2]
            if k_dia not in diccionario:
                diccionario[k_dia] = 1
                break
            else:
                diccionario[k_dia] += 1
                break


print('la cantidad de veces que aparece From en el archivo es %d ' % contador)
print(diccionario)
