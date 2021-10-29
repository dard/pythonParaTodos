'''Ejercicio 5:
(Avanzado) Cambia el programa del socket de modo que
solamente muestra datos después de que se haya recibido
la cabecera y la línea en blanco.
Recuerda que recv recibe caracteres (saltos de línea incluidos), no líneas.'''

import socket

puerto = 80
lst = list()

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
    datos = misock.recv(1024)
    if len(datos) < 1:
        break
    print(datos.decode())
    lst = list(datos)
    print(lst)
print(type(lst))
misock.close()
