''' Lee un archivo, usa split para separar en lista cada linea,
crea una nueva lista y guarda las palabras no repetidas'''

nombre_archivo = input('Ingrese el nombre del archivo: ')
print('----------------------')
try:
    fopen = open(nombre_archivo)
except Exception as e:
    print('Error. Ingrese un nombre correcto')
    print(e)
    raise
    exit()

palabasOrigen = 0
palabasDestino = 0
nuevaLista = list()

for linea in fopen:
    palabras = linea.split()
    for i in range(len(palabras)):
        palabasOrigen += 1
        if palabras[i] not in nuevaLista:
            nuevaLista.append(palabras[i])
            palabasDestino += 1
nuevaLista.sort()
print(nuevaLista)
print('----------------------')
palabras_repetidas = palabasOrigen - palabasDestino
print('Cantidad de palabras en el texto original %s ' % palabasOrigen)
print('Cantidad de palabras en la lista nueva %s ' % palabasDestino)
print('Cantidad de palabras repetidas %d ' % palabras_repetidas)
