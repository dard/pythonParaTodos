nombre_archivo = input('Ingrese el nombre del archivo: ')
try:
    fopen = open(nombre_archivo)
except Exception as e:
    print('Error. Ingrese un nombre correcto')
    print(e)
    raise
    exit()
contador = 0
for linea in fopen:
    contador += 1
    linea = linea.rstrip()
    linea = linea.upper()
    print(linea)

print(contador)
