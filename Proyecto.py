import csv

def leer_csv(Nombre_Archivo: str)->list:
    lista = []
    with open(Nombre_Archivo, "r", encoding="utf8") as archivo:
        lector = csv.reader(archivo)
        for linea in lector:
            lista.append(linea)
        return lista
                

def Pedir_Datos_Inventario() -> list:
    Nombre_Producto = input("Ingresé el Nombre del Producto: ")
    Precio = float(input("Ingresé su precio: "))
    while True:
        cantidad_input = input("Ingrese la Cantidad Disponibles (número entero positivo): ")
        if cantidad_input.isdigit():  # Comprueba si la entrada es un número entero positivo
            Cantidad = int(cantidad_input)
            if Cantidad >= 1:
                break  # Si es válido, salir del bucle
            else:
                print("La cantidad debe ser un número entero positivo.")
        else:
            print("Debe ingresar un número entero válido.")
    
    Dia = int(input("Ingresé el día en que fue Ingresado: "))
    Mes = int(input("Ingresé el Mes en que fue Ingresado: "))
    Año = int(input("Ingresé el año en que fue Ingresado: "))
    Fecha = f"{Dia}-{Mes}-{Año}"
    Datos = [Nombre_Producto, Precio, Cantidad, Fecha]
    return Datos


def Pedir_Datos_Vendedor()-> list:
    Nombre = input("Escriba el Nombre del Vendedor: ")
    Edad = input("Escriba su Edad: ")
    Telefono = input("Escriba su Telefono: ")
    Comision = 20
    
    Datos = [Nombre, Edad, Telefono, Comision]
    return Datos    


def Registrar(Nombre_archivo: str, Datos:list )-> None:
    # Registra Nombre Producto, Vendedor, Precio, Cantidad Existencia, Ventas, Llegada al Almacen 
    with open(Nombre_archivo, "a", newline="\n", encoding="utf8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(Datos)
        print("Se ha Agregado Correctamente")


def Consulta_Avanzada(Nombre_Archivo: str, Nombre: str) -> list:
    Lista = leer_csv(Nombre_Archivo)
    Resultado = []
    Busqueda = Nombre.strip().lower()

    with open(Nombre_Archivo, "r", encoding="utf8") as archivo:
        Lectura = csv.reader(archivo)
        
        for fila in Lectura:
            if fila:
                Nombre_en_fila = fila[0].strip().lower()
                if Nombre_en_fila == Busqueda:
                    Resultado.append(fila)
                    break  # Rompe el bucle después de encontrar el primer resultado

        if not Resultado:
            print("El producto no se encuentra en la base de datos")
        else:
            # Combina el encabezado y el producto encontrado en una sola lista
            datos_a_imprimir = [Lista[0]] + Resultado

            # Imprimir el encabezado y el producto encontrado en formato de celdas
            Imprimir_Lista(datos_a_imprimir)

    return Resultado
    

def Eliminar(Nombre_Archivo: str, Nombre: str)->None:
    # Elimina un producto junto con todas las caracteristicas
    
    Resultado = Consulta_Avanzada(Nombre_Archivo, Nombre)

    if not Resultado:
        return
    
    lista = leer_csv(Nombre_Archivo)
    
    opcion = input("¿Desea Eliminarlo? si/no: ").strip().lower()
    print(Resultado)
    if opcion == "si":
        for producto in Resultado:
            lista.remove(producto)
        with open(Nombre_Archivo, "w", encoding="utf8") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerows(lista)
            print("Se ha eliminado")
    else:
        print("No se ha eliminado")
            
               
def Ordenar_Inventario(Nombre_Archivo: str) -> None:
    lista = leer_csv(Nombre_Archivo)
    
    opcion = input("""
                Escoja cómo quiere ordenarlo:
                   1) Alfabéticamente
                   2) Productos más Vendidos 
                   3) Productos más Caros
                   Elija el número: """)
    
    if opcion == "1":
        # Filtrar las listas que tienen al menos un elemento y excluir el encabezado
        lista_filtrada = [fila for fila in lista[1:] if fila]
        # Ordenar alfabéticamente por el primer elemento de cada lista
        lista_ordenada = sorted(lista_filtrada, key=lambda x: x[0])
        
        # Escribir los datos ordenados en el archivo CSV
        with open(Nombre_Archivo, "w", encoding="utf8", newline="") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerows([lista[0]] + lista_ordenada)  # Agregar el encabezado
            
        
    elif opcion == "2":
        # Ordenar por productos más vendidos (orden descendente)
        lista_filtrada = [fila for fila in lista[1:] if fila]
        lista_ordenada = sorted(lista_filtrada, key=lambda x: float(x[4]), reverse=True)
        
        # Escribir los datos ordenados en el archivo CSV
        with open(Nombre_Archivo, "w", encoding="utf8", newline="") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerows([lista[0]] + lista_ordenada)  # Agregar el encabezado
            
            
    elif opcion == "3":
        # Ordenar por productos más caros (orden descendente)
        lista_filtrada = [fila for fila in lista[1:] if fila]
        lista_ordenada = sorted(lista_filtrada, key=lambda x: float(x[2]), reverse=True)
        
        # Escribir los datos ordenados en el archivo CSV
        with open(Nombre_Archivo, "w", encoding="utf8", newline="") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerows([lista[0]] + lista_ordenada)  # Agregar el encabezado
    else:
        print("Opción no válida")


def Imprimir_Lista(Datos: list) -> None:

    # Inicializar la lista de longitudes máximas con un valor mínimo
    columna_long = [float('-inf')] * len(Datos[0])

    # Calcular la longitud máxima de cada columna
    for fila in Datos:
        for i, cell in enumerate(fila):
            columna_long[i] = max(columna_long[i], len(str(cell)))

    # Imprimir los datos en formato de celdas
    for fila in Datos:
        Formato_Fila = [str(cell).ljust(length) for cell, length in zip(fila, columna_long)]
        print(" | ".join(Formato_Fila))

    # Imprimir una línea divisoria
    divisor = "+".join("-" * (length + 2) for length in columna_long)
    print(divisor)

             
def Modificar_Producto_Inventario(Nombre_Archivo: str, Nombre: str, cantidad_vendida: int) -> None:
    # Obtiene la lista completa de productos desde el archivo "Inventario.csv"
    lista = leer_csv(Nombre_Archivo)
    
    # Busca el producto a modificar
    Consulta = Consulta_Avanzada(Nombre_Archivo, Nombre)
    
    if not Consulta:
        print("No se encuentra el producto a modificar")
        return

    # Calcula la nueva cantidad
    nueva_cantidad = int(Consulta[0][2]) - cantidad_vendida

    # Verifica que la nueva cantidad sea válida
    if nueva_cantidad < 0:
        print("Error: La cantidad vendida es mayor que la cantidad existente.")
        return

    # Actualiza la cantidad en la lista
    Consulta[0][2] = nueva_cantidad

    # Encuentra la posición del producto en la lista
    for i, fila in enumerate(lista):
        if fila[0] == Consulta[0][0]:
            index = i
            break

    # Actualiza la lista con la nueva información
    lista[index] = Consulta[0]

    # Escribe la lista actualizada en el archivo "Inventario.csv"
    with open(Nombre_Archivo, "w", encoding="utf8", newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerows(lista)

    print("Se ha modificado la cantidad del producto correctamente.")
    Imprimir_Lista(lista)
            
    

def Actualizar_Ventas(Nombre_Archivo: str) -> None:
    Vendedor = input("Ingrese el Nombre del Vendedor: ")
    Consulta_Vendedor = Consulta_Avanzada("Vendedores.csv", Vendedor)
    if not Consulta_Vendedor:
        print(f"El vendedor '{Vendedor}' no se encuentra en la base de datos de vendedores.")
        return

    Producto = input("Ingrese el Nombre del Producto que vendió: ")
    Consulta_Producto = Consulta_Avanzada("Inventario.csv", Producto)
    if not Consulta_Producto:
        print(f"El producto '{Producto}' no se encuentra en el inventario.")
        return

    Dia = input("Ingresé el día en que fue vendido: ")
    Mes = input("Ingresé el Mes en que fue vendido: ")
    Año = input("Ingresé el año en que fue vendido: ")
    Fecha = f"{Dia}-{Mes}-{Año}"
    while True:
        cantidad_input = input("Ingrese la Cantidad que Vendió (número entero positivo): ")
        if cantidad_input.isdigit():  # Comprueba si la entrada es un número entero positivo
            Cantidad = int(cantidad_input)
            if Cantidad >= 1:
                break  # Si es válido, salir del bucle
            else:
                print("La cantidad debe ser un número entero positivo.")
        else:
            print("Debe ingresar un número entero válido.")

    Nombre_Vendedor = Consulta_Vendedor[0][0]
    Nombre_Producto = Consulta_Producto[0][0]
    Datos = [Nombre_Producto, Nombre_Vendedor, Cantidad, Fecha]
    Registrar(Nombre_Archivo, Datos)
    
    Modificar_Producto_Inventario("Inventario.csv", Producto, Cantidad)
    
    
    


def menu_vendedores():
    while (opcion := input("""
    1. Registrar Vendedor
    2. Consulta Vendedores
    3. Registrar Ventas por vendedor
    4. Eliminar Vendedor
    5. Volver Menu Principal
    Eliga su opción: """)) != "5":
        if opcion == "1":
            Datos = Pedir_Datos_Vendedor()
            Registrar("Vendedores.csv",Datos)
        
        elif opcion == "2":
            Datos = leer_csv("Vendedores.csv")
            Imprimir_Lista(Datos)
            
        elif opcion == "3":
            Actualizar_Ventas("Ventas_Vendedores.csv")
        
        elif opcion == "4":
            Nombre = input("Ingrese el Vendedor que desea Eliminar: ")
            Eliminar("Vendedores.csv")
        
        elif opcion == "5":
            menu_principal()
            
        else: 
            print("Eliga una de las opciones: ")
        
        
def menu_principal():
    while (opcion := input("""
    1. Inventario
    2. Vendedores
    3. Reporte de Ventas
    4. Cerrar Programa
    
    Introduzca su opción Porfavor: """)) != "4":
        if opcion == "1":
            menu_inventario()
            
        elif opcion == "2":
            menu_vendedores()
            
        elif opcion == "3":
            pass 
        elif opcion == "4":
            print("Hasta Luego")
        else: 
            print("Introduzca una de las opciones ")
        

def menu_inventario():
    while(opcion := input(""" MENU
    1. Registro Producto
    2. Consulta Avanzada 
    3. Eliminar Producto
    4. Modificar Producto
    5. Ordenar Inventario
    6. Regresar Menu Principal
    
    Introduzca su opción: """)) != "6": 
        
        if opcion == "1":
            Datos = Pedir_Datos_Inventario()
            Registrar("Inventario.csv", Datos)
            
        elif opcion == "2":
            Nombre = input("Ingrese el nombre del producto: ")
            Consulta_Avanzada("Inventario.csv", Nombre)
            
        elif opcion == "3":
            Nombre = input("Ingrese el Nombre del Producto que desee Eliminar: ")
            Eliminar("Inventario.csv", Nombre)
            
        elif opcion == "4":
            Nombre = input("Ingrese el nombre del producto: ")
            Modificar_Producto("Inventario.csv", Nombre)
            pass
        
        elif opcion == "5":
            Ordenar_Inventario("Inventario.csv")
        
        elif opcion == "6":
            menu_principal()
        
        else: 
            print("Elija una de las opciones del Menu")
    

if __name__ == "__main__":
    menu_principal()

