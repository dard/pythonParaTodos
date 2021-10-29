'''Leer un archivo y guardar cada palaba en la clave del diccionario
despues con in prenguto si esa palabra es clave en el diccionario'''

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
    palabras = linea.split()
    for i in range(len(palabras)):
        k = palabras[i]
        diccionario[k] = ''
print('livng esta en el diccionario??')
print('livng' in diccionario)
print('living esta en el diccionario??')
print('living' in diccionario)
print('+++++++++++++++++++++++++++++++++++++')
print(diccionario)
