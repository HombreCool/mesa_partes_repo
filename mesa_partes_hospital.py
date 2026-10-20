"""
Mesa de Partes Digital - Hospital General Santa Aurora
Prototipo funcional - Fundamentos de Programación
Solución: Arreglo Bidimensional (Matriz 100x7)
Lenguaje: Python
"""

MAX_DOCUMENTOS = 100
COLUMNAS = 7

# Índices de columnas
CODIGO = 0
NOMBRE = 1
TIPO = 2
FECHA = 3
AREA = 4
ESTADO = 5
ASUNTO = 6

# Matriz global (arreglo bidimensional)
documentos = [["" for _ in range(COLUMNAS)] for _ in range(MAX_DOCUMENTOS)]
total = 0


def buscar_documento(codigo):
    for i in range(total):
        if documentos[i][CODIGO] == codigo:
            return i
    return -1

def mostrar_documento(posicion):
    if posicion < 0 or posicion >= total:
        print("Documento no encontrado.")
        return
    print("-" * 50)
    print(f"  Código       : {documentos[posicion][CODIGO]}")
    print(f"  Solicitante  : {documentos[posicion][NOMBRE]}")
    print(f"  Tipo         : {documentos[posicion][TIPO]}")
    print(f"  Fecha        : {documentos[posicion][FECHA]}")
    print(f"  Área destino : {documentos[posicion][AREA]}")
    print(f"  Estado       : {documentos[posicion][ESTADO]}")
    print(f"  Asunto       : {documentos[posicion][ASUNTO]}")
    print("-" * 50)

def registrar_documento():
    global total
    if total >= MAX_DOCUMENTOS:
        print("No hay espacio disponible para más documentos.")
        return

    print("\n=== REGISTRAR NUEVO DOCUMENTO ===")
    codigo = input("Ingrese el código del documento: ").strip()

    if codigo == "":
        print("El código no puede estar vacío.")
        return

    # Verificar que el código no exista
    if buscar_documento(codigo) != -1:
        print("Error: Ya existe un documento con ese código.")
        return

    nombre = input("Ingrese el nombre del solicitante: ").strip()
    tipo = input("Ingrese el tipo de documento: ").strip()
    fecha = input("Ingrese la fecha de recepción (dd/mm/aaaa): ").strip()
    area = input("Ingrese el área de destino: ").strip()
    asunto = input("Ingrese el asunto del documento: ").strip()

    # Almacenar en la matriz
    documentos[total][CODIGO] = codigo
    documentos[total][NOMBRE] = nombre
    documentos[total][TIPO] = tipo
    documentos[total][FECHA] = fecha
    documentos[total][AREA] = area
    documentos[total][ESTADO] = "Registrado"
    documentos[total][ASUNTO] = asunto

    total += 1
    print(f"\nDocumento registrado correctamente. Total: {total}")

def consultar_documento():
    print("\n=== CONSULTAR DOCUMENTO ===")
    codigo = input("Ingrese el código del documento a buscar: ").strip()
    posicion = buscar_documento(codigo)
    if posicion == -1:
        print("No se encontró ningún documento con ese código.")
    else:
        print("\nDocumento encontrado:")
        mostrar_documento(posicion)

def listar_documentos():
    print("\n=== LISTADO DE DOCUMENTOS ===")
    if total == 0:
        print("No existen documentos registrados.")
        return

    print(f"{'N°':<4} {'Código':<12} {'Solicitante':<25} {'Tipo':<15} {'Estado':<12}")
    print("-" * 70)
    for i in range(total):
        print(f"{i+1:<4} {documentos[i][CODIGO]:<12} {documentos[i][NOMBRE]:<25} "
              f"{documentos[i][TIPO]:<15} {documentos[i][ESTADO]:<12}")
    print("-" * 70)
    print(f"Total de documentos: {total}")

def clasificar_documento():
    print("\n=== CLASIFICAR DOCUMENTO ===")
    codigo = input("Ingrese el código del documento: ").strip()
    posicion = buscar_documento(codigo)
    if posicion == -1:
        print("Documento no encontrado.")
        return

    print("Documento actual:")
    mostrar_documento(posicion)
    nuevo_tipo = input("Ingrese el nuevo tipo/categoría: ").strip()
    if nuevo_tipo:
        documentos[posicion][TIPO] = nuevo_tipo
        print("Documento clasificado correctamente.")
    else:
        print("No se realizó ningún cambio.")

def derivar_documento():
    print("\n=== DERIVAR DOCUMENTO ===")
    codigo = input("Ingrese el código del documento: ").strip()
    posicion = buscar_documento(codigo)
    if posicion == -1:
        print("Documento no encontrado.")
        return

    print("Documento actual:")
    mostrar_documento(posicion)
    nueva_area = input("Ingrese el área de destino: ").strip()
    if nueva_area:
        documentos[posicion][AREA] = nueva_area
        documentos[posicion][ESTADO] = "Derivado"
        print("Documento derivado correctamente.")
    else:
        print("No se realizó ningún cambio.")

def actualizar_seguimiento():
    print("\n=== ACTUALIZAR SEGUIMIENTO ===")
    codigo = input("Ingrese el código del documento: ").strip()
    posicion = buscar_documento(codigo)
    if posicion == -1:
        print("Documento no encontrado.")
        return

    print("Documento actual:")
    mostrar_documento(posicion)
    print("\nEstados disponibles:")
    print("  1. Registrado")
    print("  2. En proceso")
    print("  3. Derivado")
    print("  4. Atendido")
    print("  5. Archivado")
    opcion = input("Seleccione el nuevo estado (1-5): ").strip()

    estados = {
        "1": "Registrado",
        "2": "En proceso",
        "3": "Derivado",
        "4": "Atendido",
        "5": "Archivado"
    }

    if opcion in estados:
        documentos[posicion][ESTADO] = estados[opcion]
        print(f"Estado actualizado a: {estados[opcion]}")
    else:
        print("Opción inválida. No se realizó ningún cambio.")

def ordenar_documentos():
    global total
    if total <= 1:
        print("No hay suficientes documentos para ordenar.")
        return

    print("\nOrdenando documentos por código...")
    # Ordenamiento burbuja (ascendente por código)
    for i in range(total - 1):
        for j in range(total - 1 - i):
            if documentos[j][CODIGO] > documentos[j + 1][CODIGO]:
                # Intercambiar filas completas
                documentos[j], documentos[j + 1] = documentos[j + 1], documentos[j]

    print("Documentos ordenados correctamente por código.")
    listar_documentos()

ARCHIVO = "expedientes.txt"

def guardar_en_archivo():
    """Guarda todos los documentos en un archivo de texto."""
    try:
        with open(ARCHIVO, "w", encoding="utf-8") as f:
            f.write(str(total) + "\n")
            for i in range(total):
                linea = "|".join(documentos[i])
                f.write(linea + "\n")
        print(f"Datos guardados correctamente en '{ARCHIVO}'.")
    except Exception as e:
        print(f"Error al guardar: {e}")

def cargar_desde_archivo():
    """Carga los documentos desde el archivo de texto."""
    global total
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            lineas = f.readlines()
            if not lineas:
                return
            total = int(lineas[0].strip())
            for i in range(total):
                if i + 1 < len(lineas):
                    partes = lineas[i + 1].strip().split("|")
                    if len(partes) == COLUMNAS:
                        for j in range(COLUMNAS):
                            documentos[i][j] = partes[j]
        print(f"Se cargaron {total} documentos desde '{ARCHIVO}'.")
    except FileNotFoundError:
        print("No existe archivo previo. Se inicia con matriz vacía.")
    except Exception as e:
        print(f"Error al cargar: {e}")
        total = 0

def menu_principal():
    print("Mesa de Partes Digital - versión inicial")
    print("Las funciones se irán incorporando en las siguientes versiones.")


if __name__ == "__main__":
    menu_principal()
