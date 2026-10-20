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

def menu_principal():
    print("Mesa de Partes Digital - versión inicial")
    print("Las funciones se irán incorporando en las siguientes versiones.")


if __name__ == "__main__":
    menu_principal()
