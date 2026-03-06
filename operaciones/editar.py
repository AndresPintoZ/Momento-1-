def editar(lista, indice, descripcion, monto, categoria):
    if 0 <= indice < len(lista):
        lista[indice] = {"descripcion": descripcion, "monto": monto, "categoria": categoria}
    return lista