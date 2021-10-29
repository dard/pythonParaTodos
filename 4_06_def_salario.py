horas = int(input(' Introduzca cantidad de horas trabajadas: '))
tarifa = float(input(' Introduzca el valor de la tarifa por hora: '))


def calculo_salario(horas, tarifa):

    if horas > 40:
        excedente = (horas - 40) * 1.5
        salario = 40 * tarifa + excedente * tarifa
        salario_re = round(salario, 2)

    else:
        salario = (horas * tarifa)
        salario_re = round(salario, 2)

    return salario_re


sal_final = calculo_salario(horas, tarifa)

print('Su salario bruto es: ' + str(sal_final))
