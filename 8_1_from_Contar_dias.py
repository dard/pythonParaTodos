try:
    manejador = open('mbox-short.txt')
except Exception as e:
    print('Error. Ingrese un nombre correcto')
    print(e)
    raise
    exit()

contador = 0
for linea in manejador:
    palabras = linea.split()
    # print('depuraciòn %' % palabras)
    # if len(palabras) == 0:
    #     continue
    # if palabras[0] != 'From':
    #     continue
    if len(palabras) == 0 or palabras[0] != 'From':
        continue
    contador += 1
    print(palabras[2])
print(contador)
