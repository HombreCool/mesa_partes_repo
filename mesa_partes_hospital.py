"""
Mesa de Partes Digital - Hospital General Santa Aurora
Prototipo funcional - Fundamentos de Programación
Solución: Arreglo Bidimensional (Matriz 100x7)
Lenguaje: Python
"""

# ============================================================
# CONSTANTES Y ESTRUCTURA DE DATOS
# ============================================================
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
total = 0  # Cantidad de documentos registrados


# ============================================================
# FUNCIÓN: BuscarDocumento
# Localiza un expediente por su código y devuelve su posición.
# Retorna -1 si no existe.
# ============================================================
def buscar_documento(codigo):
    for i in range(total):
        if documentos[i][CODIGO] == codigo:
            return i
    return -1


# ============================================================
# FUNCIÓN: MostrarDocumento
# Presenta los datos de un expediente en una posición dada.
# ============================================================
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


# ============================================================
# FUNCIÓN: RegistrarDocumento
# Solicita los datos, valida el código y almacena el nuevo expediente.
# ============================================================
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


# ============================================================
# FUNCIÓN: ConsultarDocumento
# Permite buscar y visualizar un documento por código.
# ============================================================
def consultar_documento():
    print("\n=== CONSULTAR DOCUMENTO ===")
    codigo = input("Ingrese el código del documento a buscar: ").strip()
    posicion = buscar_documento(codigo)
    if posicion == -1:
        print("No se encontró ningún documento con ese código.")
    else:
        print("\nDocumento encontrado:")
        mostrar_documento(posicion)


# ============================================================
# FUNCIÓN: ListarDocumentos
# Muestra todos los expedientes registrados.
# ============================================================
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


# ============================================================
# FUNCIÓN: ClasificarDocumento
# Actualiza el tipo o categoría del documento.
# ============================================================
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


# ============================================================
# FUNCIÓN: DerivarDocumento
# Asigna el área de destino y actualiza el estado.
# ============================================================
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


# ============================================================
# FUNCIÓN: ActualizarSeguimiento
# Modifica el estado del expediente.
# ============================================================
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


# ============================================================
# FUNCIÓN: OrdenarDocumentos
# Ordena los expedientes por código (ordenamiento burbuja)
# manteniendo juntos todos los datos de cada fila.
# ============================================================
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


# ============================================================
# PERSISTENCIA DE DATOS (Archivos)
# ============================================================
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


# ============================================================
# MENÚ PRINCIPAL - MesaDePartesHospital
# ============================================================
def menu_principal():
    cargar_desde_archivo()  # Cargar datos al iniciar

    while True:
        print("\n" + "=" * 55)
        print("   MESA DE PARTES - HOSPITAL GENERAL SANTA AURORA")
        print("=" * 55)
        print("  1. Registrar documento")
        print("  2. Consultar documento")
        print("  3. Listar documentos")
        print("  4. Clasificar documento")
        print("  5. Derivar documento")
        print("  6. Actualizar seguimiento")
        print("  7. Ordenar documentos por código")
        print("  8. Guardar datos en archivo")
        print("  9. Salir")
        print("=" * 55)

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_documento()
        elif opcion == "2":
            consultar_documento()
        elif opcion == "3":
            listar_documentos()
        elif opcion == "4":
            clasificar_documento()
        elif opcion == "5":
            derivar_documento()
        elif opcion == "6":
            actualizar_seguimiento()
        elif opcion == "7":
            ordenar_documentos()
        elif opcion == "8":
            guardar_en_archivo()
        elif opcion == "9":
            # Guardar automáticamente al salir
            guardar_en_archivo()
            print("\n¡Gracias por usar el sistema! Hasta pronto.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


# ============================================================
# PUNTO DE ENTRADA
# ============================================================
if __name__ == "__main__":
    menu_principal()
