'''Ejercicio 3:
Utiliza urllib para rehacer el ejercicio anterior de modo que
(1) reciba el documento de una URL,
(2) muestre hasta 3000 caracteres,y
(3) cuente la cantidad total de caracteres en el documento.
No te preocupes de las cabeceras en este ejercicio,
simplemente muesta los primeros 3000 caracteres del contenido del documento.'''

import urllib.request
import urllib.parse
import urllib.error

# http://data.pr4e.org/romeo.txt

limite = 100
cantidad_caracteres = 0

url = input('Ingrese la url de la pagina: ')
# http://data.pr4e.org/romeo.txt
try:
    texto_pagina = urllib.request.urlopen(url)
    # abro la pagina con urlib
except Exception as e:
    print(f'Error. Ingrese un nombre correcto, {e}')
    raise
    exit()


for linea in texto_pagina:
    linea = linea.decode().strip()
    caracteres = linea.rstrip()
    for letra in linea:
        if letra != ' ':
            cantidad_caracteres += 1
            if cantidad_caracteres < limite:
                print(linea, end=' ')

print()
print('Numero total de caracteres ', '{:5d}'.format(cantidad_caracteres))
