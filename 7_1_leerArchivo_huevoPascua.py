
nombre_archivo = input('Ingrese el nombre del archivo: ')

try:
    fopen = open(nombre_archivo, 'r')
except Exception as e:
    if nombre_archivo == 'na na boo boo':
        print('NA NA BOO BOO para vos - te agarre gil!!')

        print('Error. Ingrese un nombre correcto')
        print(e)
    else:
        print('El %s no puede ser abierto: ' % (nombre_archivo))
        print(e)
    exit()
if nombre_archivo == 'mbox.txt':
    contador = 0
    for linea in fopen:
        contador += 1
    print('Hay %d lineas en el %s ' % (contador, nombre_archivo))
