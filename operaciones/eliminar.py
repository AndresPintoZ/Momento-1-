def eliminar(lista, indice):
    if 0 <= indice < len(lista):
        lista.pop(indice)
    return lista