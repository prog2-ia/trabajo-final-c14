import csv
import os


def obtener_ruta_csv(nombre_archivo):
    """Devuelve la ruta del archivo CSV dentro de la carpeta datos."""
    carpeta_datos = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "datos"))
    os.makedirs(carpeta_datos, exist_ok=True)
    return os.path.join(carpeta_datos, nombre_archivo)


def leer_csv(nombre_archivo):
    """Lee un CSV y devuelve una lista de filas como diccionarios."""
    ruta = obtener_ruta_csv(nombre_archivo)
    if not os.path.exists(ruta):
        return []
    with open(ruta, "r", newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        return [fila for fila in lector]


def escribir_csv(nombre_archivo, filas, campos):
    """Escribe un CSV completo desde una lista de diccionarios."""
    ruta = obtener_ruta_csv(nombre_archivo)
    with open(ruta, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(filas)


def agregar_fila_csv(nombre_archivo, fila, campos):
    """Añade una fila nueva al CSV, creando el archivo si no existe."""
    filas = leer_csv(nombre_archivo)
    filas.append(fila)
    escribir_csv(nombre_archivo, filas, campos)


def eliminar_filas_csv(nombre_archivo, clave, valor, campos):
    """Elimina todas las filas cuyo campo clave coincida con valor."""
    filas = [fila for fila in leer_csv(nombre_archivo) if fila.get(clave) != valor]
    escribir_csv(nombre_archivo, filas, campos)


def modificar_fila_csv(nombre_archivo, clave, valor, nuevos_datos, campos):
    """Modifica las filas que coincidan en clave=valor con nuevos_datos."""
    filas = leer_csv(nombre_archivo)
    for fila in filas:
        if fila.get(clave) == valor:
            fila.update(nuevos_datos)
    escribir_csv(nombre_archivo, filas, campos)
