def pedir_datos():
    descripcion = input("Descripción: ")
    categoria = input("Categoría (ej. Comida, Transporte): ")
    try:
        monto = float(input("Monto: "))
        return descripcion, monto, categoria
    except ValueError:
        print("Error: Monto no válido.")
        return None, None, None

def mostrar_lista(lista):
    if not lista:
        print("\nNo hay registros.")
    else:
        print("\n--- Gastos Actuales ---")
        for i, gasto in enumerate(lista):
            print(f"{i}. [{gasto['categoria'].upper()}] {gasto['descripcion']} - ${gasto['monto']}")

def mostrar_total(total):
    print(f"\n--- Total Acumulado: ${total} ---")