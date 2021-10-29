'''Ejercicio 4:
Cambia el programa urllinks.py para extraer y contar las etiquetas
de parrafo (p) del documento HTML recuperado y mostrar
el total de parrafos como salida del programa. No muestres el texto de
los parrafos, solo cuentalos.
Prueba el programa en varias paginas web pequenias,
y tambien en otras mas grandes.'''

import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignorar errores de certificado SSL
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Introduzca - ')
contador = 0
html = urllib.request.urlopen(url, context=ctx).read()
sopa = BeautifulSoup(html, 'html.parser')
# Recuperar todas las etiquetas de etiq
etiq = 'p'
etiquetas = sopa(etiq)

for etiqueta in etiquetas:
    contador += 1

print(contador)
print('Numero total de etiquetas %s:' % etiq + '{:5d}'.format(contador))
