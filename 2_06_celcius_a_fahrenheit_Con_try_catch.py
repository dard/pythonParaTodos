temp = input(' Ingrese por favor temperatura Celcius a convertir a Fahrenheit:  ')
try:
    fah = float(temp)
    res = (fah * 1.8)+ 32
    print (' La conversión de Celcius a Fahrenheit es: '+ str(res)+' ºF')

except:
       print('Por favor ingrese solo numeros')	

