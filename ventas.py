import csv

ventas_csv = 'ventas.csv'
datos_ventas = []

with open(ventas_csv, newline='') as archivo_csv:
    lector_csv = csv.DictReader(archivo_csv)
    for fila in lector_csv:
        datos_ventas.append(fila)


for fila in datos_ventas:
    print(fila)


ventas_por_producto_vendedor = {}

for fila in datos_ventas:
    producto = fila['Producto']
    vendedor = fila['Vendedor']
    cantidad = int(fila['Cantidad'])
    if (producto, vendedor) not in ventas_por_producto_vendedor:
        ventas_por_producto_vendedor[(producto, vendedor)] = 0
    ventas_por_producto_vendedor[(producto, vendedor)] += cantidad

print(ventas_por_producto_vendedor)

informe_csv = 'informe_de_ventas.csv'
with open(informe_csv, 'w', newline='') as archivo_informe:
    campos = ['Producto', 'Vendedor', 'Cantidad']
    escritor_csv = csv.DictWriter(archivo_informe, fieldnames=campos)
    escritor_csv.writeheader()
    
    for (producto, vendedor), cantidad in ventas_por_producto_vendedor.items():
        escritor_csv.writerow({'Producto': producto, 'Vendedor': vendedor, 'Cantidad': cantidad})
