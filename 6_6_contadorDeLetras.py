def cuenta(palabra, caracter):
    contador = 0
    for letra in palabra:
        if letra == caracter:
            contador += 1

    print(contador)
    # count hace lo mismo que la funcion cuenta
    print(palabra.count(caracter))


try:
    palabra = input('Ingrese una palabra -> ')
    caracter = input(
        'Ingrese una letra para verificar cuantas veces aparece en la palabra ingresada -> ')
except Exception as e:
    raise
    print('Error ingresar una palabra y una letra')
    print(e)
finally:
    pass


cuenta(palabra, caracter)
