# buscar en str la porcion de la cadena desde los :0.8475 y convertirlo a float

str = 'DSPAM-Confidence:0.8475'
dosPuntos = str.find(':')
print(dosPuntos)

num = str[dosPuntos + 1:]
t1 = type(num)
print(t1)
print(num)

numF = float(num)
t2 = type(numF)
print(t2)
print(numF)
