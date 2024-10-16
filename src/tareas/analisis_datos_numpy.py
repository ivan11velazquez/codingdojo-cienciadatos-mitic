import numpy as np
import math

CANTIDAD_PRODUCTOS = 10
TIENDAS = 5
DIAS = 7
VALOR_MAXIMO = 101
VALOR_MINIMO = 0

def generar_datos_ventas(productos, tiendas, dias):
    # Genera datos de ventas aleatorias para el número de productos, tiendas y días especificados
    return np.random.randint(VALOR_MINIMO, VALOR_MAXIMO, (productos, tiendas, dias))

def calcular_totales_ventas_por_producto(datos):
    # Calcula el total de ventas por producto a lo largo de la semana
    return np.sum(datos, axis=(1, 2))

def calcular_total_venta_producto(datos, index):
    # Calcular total de ventas de una tienda a lo largo de la semana
    print(np.sum(datos[index], axis=0))

def cantidad_producto_vendido(datos, index):
     # Calcular la cantidad total vendida de un producto
     return np.sum(datos[index])

def calcular_totales_ventas_por_tienda(datos):
    # Calcula el total de ventas por tienda a lo largo de la semana
    return np.sum(datos, axis=(0, 2))

def calcular_promedio_ventas_por_producto(datos):
    # Calcula el promedio de ventas por producto por día
    return np.mean(datos, axis=(1, 2))

def calcular_promedio_ventas_por_tienda(datos):
    # Calcula el promedio de ventas por tienda por día
    return np.mean(datos, axis=(0, 2))

def encontrar_producto_mayor_menor_ventas(totales_por_producto):
    # Encuentra el producto con mayor y menor ventas totales en la semana
    producto_mayor_ventas = np.argmax(totales_por_producto)
    producto_menor_ventas = np.argmin(totales_por_producto)
    return producto_mayor_ventas, producto_menor_ventas

def encontrar_tienda_mayor_menor_ventas(totales_por_tienda):
    # Encuentra la tienda con mayor y menor ventas totales en la semana
    tienda_mayor_ventas = np.argmax(totales_por_tienda)
    tienda_menor_ventas = np.argmin(totales_por_tienda)
    return tienda_mayor_ventas, tienda_menor_ventas


def iniciar_ejecucion():
    # Genera los datos de ventas
    print("Iniciando ejecucion\n")
    if(VALOR_MAXIMO > 101 or VALOR_MINIMO < 0):
        print("Revise los valores maximos y minimos, estan fuera de rango!")
    else:
        datos = generar_datos_ventas(CANTIDAD_PRODUCTOS, TIENDAS, DIAS)
        print("\nCalculo de datos:\n")
        # Calcula los totales y promedios
        totales_por_producto = calcular_totales_ventas_por_producto(datos)
        totales_por_tienda = calcular_totales_ventas_por_tienda(datos)
        promedio_por_producto = calcular_promedio_ventas_por_producto(datos)
        promedio_por_tienda = calcular_promedio_ventas_por_tienda(datos)

        # Encuentra el producto y la tienda con mayor y menor ventas
        producto_mayor_ventas, producto_menor_ventas = encontrar_producto_mayor_menor_ventas(totales_por_producto)
        # Se busca la cantidad de producto mas y menos vendido
        cantidad_producto_mayor_ventas = cantidad_producto_vendido(datos, producto_mayor_ventas)
        cantidad_producto_menor_ventas = cantidad_producto_vendido(datos, producto_menor_ventas)

        tienda_mayor_ventas, tienda_menor_ventas = encontrar_tienda_mayor_menor_ventas(totales_por_tienda)


        # Imprime los resultados
        print("Total de ventas por producto a lo largo de la semana:\n")
        for i in range(len(totales_por_producto)):
            print("Producto {}: {} unidades vendidas".format(i, totales_por_producto[i]))
        print("\n")

        print("Total de ventas por tienda a lo largo de la semana:\n")
        for i in range(len(totales_por_tienda)):
            print("Tienda {}: {} unidades vendidas en la semana".format(i, totales_por_tienda[i]))
        print("\n")

        print("Promedio de ventas por producto por día (Resultados redondeados hacia abajo):\n")
        for i in range(len(promedio_por_producto)):
            print("Producto {}: {} unidades en promedio semanal".format(i, math.floor(promedio_por_producto[i])))
        print("\n")
        
        print("Promedio de ventas por tienda por día:\n")
        for i in range(len(promedio_por_tienda)):
            print("Tienda {}: {} unidades en promedio diario".format(i, math.floor(promedio_por_tienda[i])))
        print("\n")


        print("Producto con mayor ventas: Producto {} con {} unidades vendidas"
            .format(producto_mayor_ventas, cantidad_producto_mayor_ventas))
        print("\n")
            
        print("Producto con menor ventas: Producto {} con {} unidades vendidas"
            .format(producto_menor_ventas, cantidad_producto_menor_ventas))
        print("\n")
        
        print("Tienda con mayor ventas: Tienda {}"
            .format(tienda_mayor_ventas))
        print("\n")

        print("Tienda con menor ventas: Tienda {}"
            .format(tienda_menor_ventas))
        print("\n")

iniciar_ejecucion()