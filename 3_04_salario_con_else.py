horas = int(input(' Introduzca cantidad de horas trabajadas: '))
tarifa = float(input(' Introduzca el valor de la tarifa por hora: '))
if horas > 40:
    excedente = (horas - 40) * 1.5
    salario = 40 * tarifa + excedente * tarifa
    salario_re = round(salario, 2)
    print('Su salario bruto es: ' + str(salario_re))
else:
    salario = (horas * tarifa)
    salario_re = round(salario, 2)

    print('Su salario bruto es: ' + str(salario_re))
