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


def menu_principal():
    print("Mesa de Partes Digital - versión inicial")
    print("Las funciones se irán incorporando en las siguientes versiones.")


if __name__ == "__main__":
    menu_principal()
