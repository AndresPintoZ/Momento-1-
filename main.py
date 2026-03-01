import interfaz
from operaciones.agregar import agregar
from operaciones.editar import editar
from operaciones.eliminar import eliminar

def inicio():
    historial = []
    
    while True:
        print("\n1. Agregar | 2. Ver | 3. Editar | 4. Eliminar | 5. Salir")
        opcion = input("Opción: ")
        
        if opcion == "1":
            desc, monto = interfaz.pedir_datos()
            if desc is not None:
                agregar(historial, desc, monto)
        
        elif opcion == "2":
            interfaz.mostrar_lista(historial)
        
        elif opcion == "3":
            interfaz.mostrar_lista(historial)
            idx = interfaz.pedir_indice()
            desc, monto = interfaz.pedir_datos()
            if desc is not None:
                editar(historial, idx, desc, monto)
        
        elif opcion == "4":
            interfaz.mostrar_lista(historial)
            idx = interfaz.pedir_indice()
            eliminar(historial, idx)
            
        elif opcion == "5":
            print("Saliendo del sistema...")
            break

# Llamada directa a la función
inicio()