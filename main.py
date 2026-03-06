import interfaz
from operaciones.agregar import agregar
from operaciones.editar import editar
from operaciones.eliminar import eliminar
from operaciones.totales import calcular_total # Nueva importación

def inicio():
    historial = []
    
    while True:
        print("\n1. Agregar gasto")
        print("2. Ver gastos")
        print("3. Editar gasto")
        print("4. Eliminar gasto")
        print("5. Ver total acumulado") # Nueva opción
        print("6. Salir")

        opcion = input("Opción: ")
        
        if opcion == "1":
            desc, monto, cat = interfaz.pedir_datos()
            if desc is not None:
                agregar(historial, desc, monto, cat)
        
        elif opcion == "2":
            interfaz.mostrar_lista(historial)
        
        elif opcion == "3":
            interfaz.mostrar_lista(historial)
            idx = interfaz.pedir_indice()
            desc, monto, cat = interfaz.pedir_datos()
            if desc is not None:
                editar(historial, idx, desc, monto, cat)
        
        elif opcion == "4":
            interfaz.mostrar_lista(historial)
            idx = interfaz.pedir_indice()
            eliminar(historial, idx)
            
        elif opcion == "5":
            total = calcular_total(historial)
            interfaz.mostrar_total(total)
            
        elif opcion == "6":
            print("Saliendo del sistema...")
            break

inicio()