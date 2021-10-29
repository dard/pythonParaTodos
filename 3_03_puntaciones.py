try:

    score = float(input('Ingrese una puntuación entre 0.1 y 1.0: '))

    if score >= 0.9 and score <= 1.0:
        print('Sobresaliente')
    elif score > 1.0:
        print('Puntuación incorrecta')
    elif score >= 0.8:
        print('Notable')
    elif score >= 0.7:
        print('Bien')
    elif score >= 0.6:
        print('Suficiente')
    elif score < 0.6:
        print('Insufuciente')

except Exception as ex:
    print('Puntuación incorrecta')
    print(ex)
