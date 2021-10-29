def ingresarNro():

    sumNro = 0
    countNro = 0
    promNro = 0
    while True:
        try:
            nro = input('Ingrese un número: ')
            if nro == 'fin':
                print(sumNro, countNro, promNro)
                break
            else:
                sumNro += int(nro)
                countNro += 1
                promNro = sumNro/countNro
        except Exception as ex:
            raise
            print('No es numero')
            print(ex)


ingresarNro()
