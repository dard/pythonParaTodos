nombre_archivo = input('Ingrese el nombre del archivo: ')
try:
    fopen = open(nombre_archivo)
except Exception as e:
    print('Error. Ingrese un nombre correcto')
    print(e)
    raise
    exit()
contador = 0
total = 0
promedio = 0
for linea in fopen:
    linea = linea.rstrip()

    if linea.startswith('X-DSPAM-Confidence: 0.8475'):
        extract = linea.find(':')
        extract2 = linea[extract + 1:]
        extractNum = float(extract2)
        contador += 1
        total = total + extractNum

promedio = float(total / contador)
print(contador, total, promedio)
print('Promedio spam Confidence: '+str(promedio))
