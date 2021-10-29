horas = int(input(' Introduzca cantidad de horas trabajadas: '))
tarifa = float(input(' Introduzca el valor de la tarifa por hora: '))
salario = horas * tarifa
salario_re = round(salario, 2)
print('Su salario bruto es: ' + str(salario_re))
