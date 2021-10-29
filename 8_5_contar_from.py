''' Lee un archivo, usa split para separar las lineas que empiezan con From,
luego imprime la segunda palabra que la direccion de mail del remitente
'''
nombre_archivo = input('Ingrese el nombre del archivo: ')
print('----------------------')
try:
    fopen = open(nombre_archivo)  # manejador de archivo, handler
except Exception as e:
    print('Error. Ingrese un nombre correcto')
    print(e)
    raise
    exit()

contador = 0
for linea in fopen:
    palabras = linea.split()
    if len(palabras) == 0 or palabras[0] != 'From':
        continue
    contador += 1
    print(palabras[1])
print('----------------------')
print('Cantidad de remitentes %d' % contador)
