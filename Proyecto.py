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
        if cantidad_input.isdigit(): 
            Cantidad = int(cantidad_input)
            if Cantidad >= 1:
                break 
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
                    break  

        if not Resultado:
            print("El producto no se encuentra en la base de datos")
        else:
            
            datos_a_imprimir = [Lista[0]] + Resultado

    
    

    return Resultado
    

def Eliminar(Nombre_Archivo: str, Nombre: str)->None:
    # Elimina un producto junto con todas las caracteristicas
    Lista = leer_csv(Nombre_Archivo)
    Resultado = Consulta_Avanzada(Nombre_Archivo, Nombre)
    datos_a_Imprimir = datos_a_imprimir = [Lista[0]] + Resultado
    Imprimir_Lista(datos_a_imprimir)

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
    lista = leer_csv(Nombre_Archivo)
    
    Consulta = Consulta_Avanzada(Nombre_Archivo, Nombre)
    datos_a_Imprimir = datos_a_imprimir = [lista[0]] + Consulta
    Imprimir_Lista(datos_a_imprimir)
    
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

    with open(Nombre_Archivo, "w", encoding="utf8", newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerows(lista)

    print("Se ha modificado la cantidad del producto correctamente.")
    Imprimir_Lista(lista)
              

def Actualizar_Ventas(Nombre_Archivo: str) -> None:
    Lista_Inventario = leer_csv("Inventario.csv")
    Lista_Vendedor = leer_csv("Vendedores.csv")
    
    Vendedor = input("Ingrese el Nombre del Vendedor: ")
    Consulta_Vendedor = Consulta_Avanzada("Vendedores.csv", Vendedor)
    datos_a_Imprimir = datos_a_imprimir = [Lista_Vendedor[0]] + Consulta_Vendedor
    Imprimir_Lista(datos_a_imprimir)
    
    if not Consulta_Vendedor:
        print(f"El vendedor '{Vendedor}' no se encuentra en la base de datos de vendedores.")
        return

    Producto = input("Ingrese el Nombre del Producto que vendió: ")
    Consulta_Producto = Consulta_Avanzada("Inventario.csv", Producto)
    datos_a_Imprimir = datos_a_imprimir = [Lista_Inventario[0]] + Consulta_Producto
    Imprimir_Lista(datos_a_imprimir)
    
    if not Consulta_Producto:
        print(f"El producto '{Producto}' no se encuentra en el inventario.")
        return

    Dia = input("Ingresé el día en que fue vendido: ")
    Mes = input("Ingresé el Mes en que fue vendido: ")
    Año = input("Ingresé el año en que fue vendido: ")
    Fecha = f"{Dia}-{Mes}-{Año}"
    while True:
        cantidad_input = input("Ingrese la Cantidad que Vendió (número entero positivo): ")
        if cantidad_input.isdigit():  
            Cantidad = int(cantidad_input)
            if Cantidad >= 1:
                break  
            else:
                print("La cantidad debe ser un número entero positivo.")
        else:
            print("Debe ingresar un número entero válido.")

    Nombre_Vendedor = Consulta_Vendedor[0][0]
    Nombre_Producto = Consulta_Producto[0][0]
    Datos = [Nombre_Producto, Nombre_Vendedor, Cantidad, Fecha]
    Registrar(Nombre_Archivo, Datos)
    
    Modificar_Producto_Inventario("Inventario.csv", Producto, Cantidad)
    

def Ventas_por_Vendedor(Nombre_Archivo_Ventas: str, Nombre_Archivo_Inventario: str) -> None:
    datos_ventas = leer_csv(Nombre_Archivo_Ventas)
    
    # Crear un diccionario para almacenar las ventas y comisiones por vendedor
    ventas_por_vendedor = {}
    
    for fila in datos_ventas[1:]:  # Excluir el encabezado
        nombre_vendedor = fila[1]
        cantidad_vendida = int(fila[2])
        
        # Consultar el precio del producto en el inventario
        producto = fila[0]
        consulta_producto = Consulta_Avanzada(Nombre_Archivo_Inventario, producto)
        
        if not consulta_producto:
            print(f"No se encontró el producto '{producto}' en el inventario.")
            continue
        
        precio_producto = float(consulta_producto[0][1])
        
        # Calcular el total de ventas y la comisión
        total_ventas = cantidad_vendida * precio_producto
        comision = total_ventas * 0.20
        
        # Actualizar el diccionario de ventas por vendedor
        if nombre_vendedor in ventas_por_vendedor:
            ventas_por_vendedor[nombre_vendedor] += total_ventas
        else:
            ventas_por_vendedor[nombre_vendedor] = total_ventas
        
    resultados = [["Nombre Vendedor", "Total Ventas", "Total Comisiones"]]
    for nombre, ventas in ventas_por_vendedor.items():
        comision = ventas * 0.20
        resultados.append([nombre, ventas, comision])
    
    with open("Ventas_por_Vendedor.csv", "w", encoding="utf8", newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerows(resultados)
    
    Imprimir_Lista(resultados)


def Ventas_por_Producto(Nombre_Archivo_Ventas: str, Nombre_Archivo_Inventario: str):
    datos_ventas = leer_csv(Nombre_Archivo_Ventas)
    inventario = leer_csv(Nombre_Archivo_Inventario)
    
    # Crear un diccionario para almacenar las ventas por producto
    ventas_por_producto = {}
    
    for fila in datos_ventas[1:]:  # Excluir el encabezado
        nombre_producto = fila[0]
        cantidad_vendida = int(fila[2])
        
        # Consultar el precio del producto en el inventario
        consulta_producto = Consulta_Avanzada(Nombre_Archivo_Inventario, nombre_producto)
        
        if not consulta_producto:
            print(f"No se encontró el producto '{nombre_producto}' en el inventario.")
            continue
        
        precio_producto = float(consulta_producto[0][1])
        
        # Calcular el total de ventas
        total_ventas = cantidad_vendida * precio_producto
        
        # Actualizar el diccionario de ventas por producto
        if nombre_producto in ventas_por_producto:
            ventas_por_producto[nombre_producto][0] += cantidad_vendida
            ventas_por_producto[nombre_producto][1] += total_ventas
        else:
            ventas_por_producto[nombre_producto] = [cantidad_vendida, total_ventas]
    
    resultados = [["Nombre Producto", "Cantidad Vendida", "Venta Total"]]
    for producto, datos in ventas_por_producto.items():
        cantidad_vendida, venta_total = datos
        resultados.append([producto, cantidad_vendida, venta_total])
    
    with open("Ventas_por_Producto.csv", "w", encoding="utf8", newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerows(resultados)
        Imprimir_Lista(resultados)
    

def Calcular_Ventas_Totales(Nombre_Archivo_Ventas: str, Nombre_Archivo_Inventario: str):
    datos_ventas = leer_csv(Nombre_Archivo_Ventas)

    # Crear un diccionario para almacenar las ventas por vendedor
    ventas_por_vendedor = {}

    for fila in datos_ventas[1:]:  # Excluir el encabezado
        nombre_vendedor = fila[1]
        cantidad_vendida = int(fila[2])

        # Consultar el precio del producto en el inventario
        producto = fila[0]
        consulta_producto = Consulta_Avanzada(Nombre_Archivo_Inventario, producto)

        if not consulta_producto:
            print(f"No se encontró el producto '{producto}' en el inventario.")
            continue

        precio_producto = float(consulta_producto[0][1])

        # Calcular el total de ventas y la comisión
        total_ventas = cantidad_vendida * precio_producto
        comision = total_ventas * 0.20

        # Actualizar el diccionario de ventas por vendedor
        if nombre_vendedor in ventas_por_vendedor:
            ventas_por_vendedor[nombre_vendedor][0] += total_ventas
            ventas_por_vendedor[nombre_vendedor][1] += comision
        else:
            ventas_por_vendedor[nombre_vendedor] = [total_ventas, comision]

    # Calcular el total de productos vendidos y el total de comisiones
    total_productos_vendidos = sum(int(fila[2]) for fila in datos_ventas[1:])
    total_comisiones = sum(comision for _, comision in ventas_por_vendedor.values())

    # Calcular el total de ventas totales
    total_ventas_totales = sum(total for total, _ in ventas_por_vendedor.values())

    # Calcular el resultado final (Ventas Totales menos Comisiones)
    resultado_final = total_ventas_totales - total_comisiones

    # Crear una lista con los resultados
    resultados = [
        ["Total Productos Vendidos", total_productos_vendidos],
        ["Total Ventas Totales", total_ventas_totales],
        ["Total Comisiones", total_comisiones],
        ["Resultado Final (Ventas Totales - Comisiones)", resultado_final]
    ]

    with open("Ventas_Totales.csv", "w", encoding="utf8", newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerows(resultados)

    Imprimir_Lista(resultados)
      


def menu_Reportes():
    while (opcion := input("""
    1. Reporte Ventas por Vendedor 
    2. Reporte Ventas por Producto
    3. Reporte Ventas Totales
    4. Regresar a Menu Principal
    
    Ingrese su Opcion: """)) != "4":
        if opcion == "1":
            Ventas_por_Vendedor("Ventas_Vendedores.csv", "Inventario.csv")
        elif opcion == "2":
            Ventas_por_Producto("Ventas_Vendedores.csv", "Inventario.csv")
        elif opcion == "3":
            Calcular_Ventas_Totales("Ventas_Vendedores.csv", "Inventario.csv",)
        elif opcion == "4":
            menu_principal()
        else:
            print("Ingrese una de las opciones") 
        

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
        

def menu_inventario():
    while(opcion := input(""" MENU
    1. Registro Producto
    2. Consulta Avanzada 
    3. Eliminar Producto
    4. Ordenar Inventario
    5. Regresar Menu Principal
    
    Introduzca su opción: """)) != "5": 
        
        if opcion == "1":
            Datos = Pedir_Datos_Inventario()
            Registrar("Inventario.csv", Datos)
            
        elif opcion == "2":
            Nombre = input("Ingrese el nombre del producto: ")
            Lista = leer_csv("Inventario.csv")
            Resultado = Consulta_Avanzada("Inventario.csv", Nombre)
            datos_a_Imprimir = datos_a_imprimir = [Lista[0]] + Resultado
            Imprimir_Lista(datos_a_imprimir)
            
        elif opcion == "3":
            Nombre = input("Ingrese el Nombre del Producto que desee Eliminar: ")
            Eliminar("Inventario.csv", Nombre)
            
        
        elif opcion == "4":
            Ordenar_Inventario("Inventario.csv")
        
        elif opcion == "5":
            menu_principal()
        
        else: 
            print("Elija una de las opciones del Menu")


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
            menu_Reportes()
    
        elif opcion == "4":
            print("Hasta Luego")
        
        else: 
            print("Introduzca una de las opciones ")
  
    
if __name__ == "__main__":
    menu_principal()

