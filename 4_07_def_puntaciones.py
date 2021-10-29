try:
    score = float(input('Ingrese una puntuación entre 0.1 y 1.0: '))
except Exception as ex:
    print('Puntuación incorrecta')
    print(ex)


def calcula_calificacion(score):
    try:

        if score >= 0.9 and score <= 1.0:
            calificacion = 'Sobresaliente'
        elif score > 1.0:
            calificacion = 'Puntuación incorrecta'
        elif score >= 0.8:
            calificacion = 'Notable'
        elif score >= 0.7:
            calificacion = 'Bien'
        elif score >= 0.6:
            calificacion = 'Suficiente'
        elif score < 0.6:
            calificacion = 'Insufuciente'

    except Exception as ex:
        print('Puntuación incorrecta')
        print(ex)

    return calificacion


nota = calcula_calificacion(score)
print('Su calificación es: '+str(nota))
