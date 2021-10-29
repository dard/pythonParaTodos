'''Ejercicio 3:
Escribe un programa que lee un archivo e imprime las letras
en orden decreciente de frecuencia.
El programa debe convertirtodas las entradas a minúsculas
y contar solamente las letras a-z.
El programa no debe contar espacios,dígitos, signos de puntuación,
o cualquier cosa que no sean las letras a-z.
Encuentra ejemplos detexto en idiomas diferentes,
y observa cómo la frecuencia de letrasesdiferente en cada idioma.
Compara tus resultados con las tablas en
https://es.wikipedia.org/wiki/Frecuencia_de_aparici%C3%B3n_de_letras.'''
import string

nombre_archivo = input('Ingrese el nombre del archivo: ')
try:
    fopen = open(nombre_archivo)
except Exception as e:
    print('Error. Ingrese un nombre correcto')
    print(e)
    raise
    exit()

diccionario = dict()
t = tuple()
cant_total_letras = 0

for linea in fopen:
    # separo la linea en token palabras, creo la lista palabras
    linea = linea.rstrip()
    # con rstrip elimino espacios al final
    linea = linea.translate(linea.maketrans('', '', string.punctuation))
    # elimino signos de puntuación
    linea = linea.lower()
    # convierto a minúsculas
    palabras = linea.split()
    # hago una lista con linea

    for palabra in palabras:
        # recorro la lista palabras
        t = tuple(palabra)
        # separo la palabra en caracteres con tuple creo una tupla
        for tupla in t:
            # recorro la tupla
            if tupla.isdigit():
                break
            elif tupla not in diccionario:
                # si el caracter no esta en el diccionario
                # sumo  1
                diccionario[tupla] = 1
            else:
                # si el caracter esta como clave en el diccionario
                # sumo al valor de la clave mas 1
                diccionario[tupla] += 1
            cant_total_letras += 1

# print(diccionario)
print('Total de letras (%d),en el archivo %s ' % (cant_total_letras, nombre_archivo))

lst = list()
# ordeno el diccionario por clave
for letra, valor in list(diccionario.items()):
    lst.append((letra, valor))

lst.sort(reverse=False)
porcentaje = 0
# print('Letra '+'Repeticiones '+'Porcentaje')
for letra, valor in lst:
    porcentaje = ((valor/cant_total_letras)*100)
    print(letra, '{:7d}'.format(valor), '{:04.2f}'.format(porcentaje)+'%')
