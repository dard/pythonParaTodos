t1 = [1, 2, 3, 4]


def remover(t):
    # elimina el primer elemento y el ultimo elemento de la lista
    del t[0]
    del t[-1]

    return t


print(t1)
remover(t1)
print(t1)
