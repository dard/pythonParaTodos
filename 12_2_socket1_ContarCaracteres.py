'''Ejercicio 2:
Cambia el programa del socket para que cuente el número
de caracteres que ha recibido y se detenga, con un texto en pantalla,
después de que se hayan mostrado 3000 caracteres.
El programa debe recuperar el documento completo y contar el número total de
caracteres,mostrando ese total al final del documento.'''

import socket

puerto = 80
contador = 0
copia = ''

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
# print(cmd)

while True:
    datos = misock.recv(512)
    if len(datos) < 1:
        break
    else:
        copia += datos.decode()
        for linea in copia:
            caracteres = linea.rstrip()
            if caracteres != '':
                contador += 1
                # if contador < 300:
                #     print(caracteres)


print(copia)
print()
print('Numero total de caracteres ', '{:5d}'.format(contador))
misock.close()
