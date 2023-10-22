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
    Vendedor = input("Ingresé el Nombre del Vendedor: ")
    Precio = float(input("Ingresé su precio: "))
    Cantidad = float(input("Ingresé la Cantidad de Existencia: "))
    Ventas = float(input("Ventas Totales: "))
    Dia = int(input("Ingresé el día en que fue Ingresado: "))
    Mes = int(input("Ingresé el Mes en que fue Ingresado: "))
    Año = int(input("Ingresé el año en que fue Ingresado: "))
    Fecha = f"{Dia}-{Mes}-{Año}"
    Datos = [Nombre_Producto, Vendedor, Precio, Cantidad, Ventas, Fecha]
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
    Resultado = []
    Busqueda = Nombre.strip().lower()
    
    with open(Nombre_Archivo, "r", encoding="utf8") as archivo:
        Lectura = csv.reader(archivo)
        encontrado = False
        
        for fila in Lectura:
            if fila:
                Nombre_en_fila = fila[0].strip().lower()
                if Nombre_en_fila == Busqueda:
                    Resultado.append(fila)
                    print(f"""
Nombre: {fila[0]}
Vendedor: {fila[1]}
Precio: {fila[2]}
Cantidad Existencia: {fila[3]}
Ventas: {fila[4]}
Llegada almacen: {fila[5]}
""")
                    encontrado = True
                    return Resultado
        
        if not encontrado:
            print("El producto no se encuentra en la base de datos")
            return Resultado
    

def Eliminar_Producto(Nombre_Archivo: str)->None:
    # Elimina un producto junto con todas las caracteristicas
    Borrar = input("Ingresé el nombre del producto que desea borrar: ")
    
    Resultado = Consulta_Avanzada(Nombre_Archivo,Borrar)

    if not Resultado:
        return
    
    lista = leer_csv(Nombre_Archivo)
    
    opcion = input("¿Desea Eliminar este producto? si/no: ").strip().lower()
    print(Resultado)
    if opcion == "si":
        for producto in Resultado:
            lista.remove(producto)
        with open(Nombre_Archivo, "w", encoding="utf8") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerows(lista)
            print("Se ha eliminado tu producto :)")
    else:
        print("No se ha eliminado tu producto")
            
    
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

def Imprimir_Lista(Nombre_Archivo: str)-> None:
    datos = leer_csv(Nombre_Archivo)
    encabezado = datos[0]
    print(encabezado)
    
    # print(tabulate(d, headers= encabezado))
            
def Modificar_Producto(Nombre_Archivo: str, Nombre: str) -> None:
    lista = leer_csv(Nombre_Archivo)
    Consulta = Consulta_Avanzada(Nombre_Archivo, Nombre)
    
    if not Consulta:
        print("No se encuentra el producto a modificar")
        return
    
    print("Información del producto a modificar:")
 
    
    opcion = input("¿Desea Modificar este producto? si/no: ").strip().lower()
    if opcion == "si":
        nuevo_nombre = input("Nuevo Nombre del Producto: ")
        nuevo_vendedor = input("Nuevo Nombre del Vendedor: ")
        nuevo_precio = float(input("Nuevo Precio: "))
        nueva_cantidad = float(input("Nueva Cantidad de Existencia: "))
        nuevas_ventas = float(input("Nuevas Ventas Totales: "))
        nuevo_dia = int(input("Nuevo Día en que fue Ingresado: "))
        nuevo_mes = int(input("Nuevo Mes en que fue Ingresado: "))
        nuevo_anio = int(input("Nuevo Año en que fue Ingresado: "))
        nueva_fecha = f"{nuevo_dia}-{nuevo_mes}-{nuevo_anio}"
        
        nuevo_producto = [nuevo_nombre, nuevo_vendedor, nuevo_precio, nueva_cantidad, nuevas_ventas, nueva_fecha]
        
        lista = [nuevo_producto if x == Consulta[0] else x for x in lista]
        
        with open(Nombre_Archivo, "w", encoding="utf8", newline="") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerows(lista)
        print("Se ha modificado tu producto correctamente.")
    else:
        print("No se ha modificado tu producto.")

def menu_vendedores():
    while (opcion := input("""
    1. Registrar Vendedor
    2. Consulta Vendedores
    3. Registrar Ventas por vendedor
    4. Cerrar programa
    Eliga su opción: """)) != "4":
        if opcion == "1":
            Datos = Pedir_Datos_Vendedor()
            Registrar("Vendedores.csv")
        
        elif opcion == "2":
            Imprimir_Lista("Vendedores.csv")
            
        elif opcion == "3":
            pass 
        
        elif opcion == "4":
            menu_inventario()
            
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
    6. Cerrar programa
    
    Introduzca su opción: """)) != "6": 
        
        if opcion == "1":
            Datos = Pedir_Datos_Inventario()
            Registrar("Inventario.csv", Datos)
            
        elif opcion == "2":
            Nombre = input("Ingrese el nombre del producto: ")
            Consulta_Avanzada("Inventario.csv", Nombre)
            
        elif opcion == "3":
            Eliminar_Producto("Inventario.csv")
            
        elif opcion == "4":
            Nombre = input("Ingrese el nombre del producto: ")
            Modificar_Producto("Inventario.csv", Nombre)
        
        elif opcion == "5":
            Ordenar_Inventario("Inventario.csv")
        
        elif opcion == "6":
            print("Hasta Pronto")
        
        else: 
            print("Elija una de las opciones del Menu")
    
import csv

def generar_reporte_ventas(Nombre_Archivo: str) -> None:
    ventas = []

    with open(Nombre_Archivo, "r", encoding="utf8") as archivo:
        lector = csv.reader(archivo)
        next(lector)  # Saltar la primera fila que es el encabezado

        for linea in lector:
            producto = linea[0]
            vendedor = linea[1]
            cantidad = float(linea[3])
            fecha = linea[5]

            venta = {
                "Producto": producto,
                "Vendedor": vendedor,
                "Cantidad": cantidad,
                "Fecha": fecha
            }
            ventas.append(venta)

    if ventas:
        print("\nReporte de Ventas:")
        for venta in ventas:
            print(f"Producto: {venta['Producto']}")
            print(f"Vendedor: {venta['Vendedor']}")
            print(f"Cantidad: {venta['Cantidad']}")
            print(f"Fecha: {venta['Fecha']}")
            print("-" * 30)
    else:
        print("No hay datos de ventas para generar un reporte.")
 
if __name__ == "__main__":
    menu_principal()
