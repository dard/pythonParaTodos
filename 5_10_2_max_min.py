def ingresarNro():

    sumNro = 0
    maximo = []
    minimo = []
    print('EL programa le solicitara que ingrese numeros, para finalizar ingrese fin')
    while True:
        try:
            nro = input('Ingrese un número: ')
            if nro == 'fin':
                maxNro = max(maximo)
                minNro = min(minimo)
                print(sumNro, maxNro, minNro)
                break
            else:
                sumNro += int(nro)
                maximo.append(nro)
                minimo.append(nro)
        except Exception as ex:
            print('No es numero')
            print(ex)
            raise


ingresarNro()
