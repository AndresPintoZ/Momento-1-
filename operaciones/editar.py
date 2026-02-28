def editar(lista, indice, descripcion, monto):
    if 0 <= indice < len(lista):
        lista[indice] = {"descripcion": descripcion, "monto": monto}
    return lista