'''Estructura de datos, Ingeniería en sistemas computacionales 
Métodos de búsqueda: Funciones Hash
Integrantes:
Balam Castillo Pedro
Pech Cantun Diego
Loreto Huerta Filiberto
'''
import os
import time

# Esta clase permite almacenar y buscar números utilizando una tabla hash para hacer búsquedas rápidas.
class TablaHash:
    
    def __init__(self, tamaño=100003):
        self.tamaño = tamaño
        self.tabla = [[] for _ in range(tamaño)]


    # Convierte un número en una posición válida de la tabla usando el operador módulo (%).
    def funcion_hash(self, numero):
        return numero % self.tamaño

    # Guarda el número y su posición original dentro de la tabla hash.

    def insertar(self, numero, indice):
        clave = self.funcion_hash(numero)
        self.tabla[clave].append([numero, indice])

    # Busca un número dentro de la tabla hash.
    def buscar(self, numero):
        clave = self.funcion_hash(numero)

        posiciones = []

        for elemento in self.tabla[clave]:
            valor = elemento[0]
            indice = elemento[1]

            if valor == numero:
                posiciones.append(indice)

        return posiciones, clave, len(self.tabla[clave])

# Lee el archivo datos.txt y extrae todos los números.
def leer_archivo(ruta_archivo):

    numeros = []

    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:

            contenido = archivo.read()

            contenido = contenido.replace(",", " ")
            contenido = contenido.replace(";", " ")

            partes = contenido.split()

            for dato in partes:
                numeros.append(int(dato))

    except FileNotFoundError:
        print("Error: No se encontró el archivo.")
        return []

    except ValueError:
        print("Error: El archivo contiene datos no numéricos.")
        return []

    return numeros

# Guarda los números ordenados en un nuevo archivo.
def guardar_numeros(ruta_salida, numeros):
    
    with open(ruta_salida, "w", encoding="utf-8") as archivo:

        for numero in numeros:
            archivo.write(str(numero) + "\n")

# FUNCIÓN PRINCIPAL
def main():

    print("SISTEMA DE BÚSQUEDA HASH")

    # Obtenemos las rutas de los archivos.
    carpeta_actual = os.path.dirname(os.path.abspath(__file__))

    ruta_datos = os.path.join(carpeta_actual, "datos.txt")
    ruta_salida = os.path.join(carpeta_actual,"datos_ordenados.txt")

    numeros = leer_archivo(ruta_datos)

    # Verifica si se cargaron los datos.
    if len(numeros) == 0:
        print("No hay datos para procesar.")
        return

    print(f"\nSe cargaron: {len(numeros)} números")

    # Se ordenan todos los números.
    inicio_ordenamiento = time.perf_counter()

    numeros.sort()

    fin_ordenamiento = time.perf_counter()
    tiempo_ordenamiento_ms = (fin_ordenamiento - inicio_ordenamiento) * 1000

    print("\nOrdenamiento completado.")
    print(f"Tiempo de ordenamiento: "f"{tiempo_ordenamiento_ms:.4f} ms")

    # Aqui se guarda el archivo ordenado.
    guardar_numeros(ruta_salida, numeros)
    print("Archivo ordenado guardado.")

    # Se crea la tabla hash.
    tabla_hash = TablaHash()

    inicio_hash = time.perf_counter()

    # Insertamos todos los números en la tabla hash.
    for indice, numero in enumerate(numeros):
        tabla_hash.insertar(numero, indice)

    fin_hash = time.perf_counter()

    # Obtenemos el tiempo de construcción de la tabla hash.
    tiempo_hash_ms = (fin_hash - inicio_hash) * 1000

    print("\nTabla hash construida.")
    print(f"Tiempo de construcción: "f"{tiempo_hash_ms:.4f} ms")

    # MENÚ PRINCIPAL
    while True:

        print("\n")
        print("-" * 30)
        print("MENÚ")
        print("1. Buscar un número")
        print("2. Buscar múltiples números")
        print("3. Salir")

        opcion = input("\nSelecciona una opción: ")

        # opcion de solo buscar un número.
        if opcion == "1":

            try:
                numero_buscar = int(input("\nIngresa el número a buscar: "))

                inicio_busqueda = time.perf_counter()

                posiciones, clave, elementos = (tabla_hash.buscar(numero_buscar))

                fin_busqueda = time.perf_counter()

                tiempo_busqueda_ms = (fin_busqueda - inicio_busqueda) * 1000

                print("\nResultado de la búsqueda:")
                print("-" * 40)

                print("Número buscado:", numero_buscar)

                if len(posiciones) > 0:

                    print("Estado: Número encontrado.")
                    print("Primera posición (cubeta):",posiciones[0] + 1)

                else:

                    print("Estado: Número no encontrado.")

                print(f"Tiempo de búsqueda: "f"{tiempo_busqueda_ms:.2f} ms")

            except ValueError:
                print("Error: Debes ingresar un número válido.")


        # opcion de buscar varios números.
        elif opcion == "2":

            try:
                cantidad = int(input("\n¿Cuántos números deseas buscar?: "))

                if cantidad <= 0:
                    print("La cantidad debe ser mayor que cero.")

                    continue

            except ValueError:
                print("Error: Debes ingresar un número válido.")

                continue

            numeros_buscar = []

            i = 0

            while i < cantidad:

                try:
                    numero = int(input(f"Ingrese número {i + 1}: "))
                    numeros_buscar.append(numero)

                    i += 1

                except ValueError:
                    print("Error: Debes ingresar un número entero.")

            for numero_buscar in numeros_buscar:

                inicio_busqueda = time.perf_counter()

                posiciones, clave, elementos = (tabla_hash.buscar(numero_buscar))

                fin_busqueda = time.perf_counter()

                tiempo_busqueda_ms = (fin_busqueda - inicio_busqueda) * 1000

                print("\nResultado de la búsqueda:")
                print("-" * 40)

                print("Número buscado:", numero_buscar)

                if len(posiciones) > 0:

                    print("Estado: Número encontrado.")
                    print("Primera posición (cubeta):",posiciones[0] + 1)

                else:

                    print("Estado: Número no encontrado.")

                print(f"Tiempo de búsqueda: "f"{tiempo_busqueda_ms:.2f} ms")

        # Salir del programa.
        elif opcion == "3":
            print("\nSaliendo del programa.")
            break
        
        else:

            print("Opción inválida.")

if __name__ == "__main__":
    main()
