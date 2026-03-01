def pedir_datos():
    descripcion = input("Descripción: ")
    try:
        monto = float(input("Monto: "))
        return descripcion, monto
    except ValueError:
        print("Error: Monto no válido.")
        return None, None

def mostrar_lista(lista):
    if not lista:
        print("\nNo hay registros.")
    else:
        print("\n--- Gastos Actuales ---")
        for i, gasto in enumerate(lista):
            print(f"{i}. {gasto['descripcion']} - ${gasto['monto']}")

def pedir_indice():
    try:
        return int(input("Seleccione el número: "))
    except ValueError:
        return -1
