def ingresarNro():

    sumNro = 0
    listaNumeros = []
    listaNumeros = []
    print('EL programa le solicitara que ingrese numeros, para finalizar ingrese hecho')
    while True:
        try:
            nro = input('Ingrese un número: ')
            if nro == 'hecho':
                maxNro = max(listaNumeros)
                minNro = min(listaNumeros)
                break
            else:
                sumNro += int(nro)
                listaNumeros.append(nro)
        except Exception as ex:
            print('No es numero')
            print(ex)
            raise

    print('Maximo %s ' % maxNro)
    print('Minimo %s ' % minNro)
    print('La suma de los números ingresados es %d ' % sumNro)


ingresarNro()
