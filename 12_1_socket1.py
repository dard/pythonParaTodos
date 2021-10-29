'''Ejercicio 1:
Cambia el programa del socket socket1.py
para que le pida al usuario la URL,de modo que pueda leer cualquier página web.
Puedes usar split('/')para dividir la URL en las partes que la componen,
de modo que puedas extraer el nombre del host para la llamada
a connect del socket. Añade comprobación de errores utilizando
try y except para contemplar la posibilidad de que el usuario
introduzca una URL mal formada o inexistente.'''

import socket

puerto = 80

paginaurl = input('Ingrese la url de la pagina: ')
urlsinbarras = paginaurl.split('/')
# print(urlsinbarras)
servidor = (urlsinbarras[2])
# print(paginaurl)
# print(servidor)


try:
    misock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    misock.connect((servidor, puerto))
    # cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
    # Concateno partes del string.con f-string
    cmd = f'GET {paginaurl} HTTP/1.0\r\n\r\n'.encode()
    # o con format
    # cmd = 'GET {} HTTP/1.0\r\n\r\n'.format(paginaurl).encode()
    misock.send(cmd)

except Exception as e:
    print('Error. Ingrese un nombre correcto')
    print(e)
    raise
    exit()
print(cmd)

while True:
    datos = misock.recv(512)
    if len(datos) < 1:
        break
    print(datos.decode(), end='')

misock.close()
