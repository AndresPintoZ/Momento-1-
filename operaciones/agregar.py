def agregar(lista, descripcion, monto, categoria):
    gasto = {"descripcion": descripcion, "monto": monto, "categoria": categoria}
    lista.append(gasto)
    return lista