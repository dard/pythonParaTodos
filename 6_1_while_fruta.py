def recorrerFruta():

    fruta = 'banana'
    tamaño = len(fruta)
    # print(tamaño)

    start = tamaño - 1
    # print(start)

    end = 0

    while start >= end:
        for caracter in fruta:
            print(caracter)
            start -= 1

    # fruta = 'banana'
    # indice = 0
    # while indice < len(fruta):
    #
    #     letra = fruta[indice]
    #     print(letra)
    #     indice = indice+1


recorrerFruta()
