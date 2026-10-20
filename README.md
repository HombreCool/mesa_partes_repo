# Mesa de Partes Digital — Hospital General Santa Aurora

Prototipo de consola desarrollado en Python para gestionar documentos y expedientes de una mesa de partes hospitalaria. Permite registrar documentos, consultarlos, clasificarlos, derivarlos a un área, actualizar su estado, listar los registros y ordenarlos por código.

## Características

- **Registro de documentos:** guarda el código, nombre del solicitante, tipo de documento, fecha de recepción, área de destino y asunto.
- **Validación de códigos:** impide registrar un documento si el código está vacío o ya existe.
- **Consulta por código:** busca un documento y muestra todos sus datos.
- **Listado de documentos:** muestra los expedientes registrados en una tabla resumida.
- **Clasificación:** permite actualizar el tipo o la categoría de un documento.
- **Derivación:** permite cambiar el área de destino y marcar el documento como «Derivado».
- **Seguimiento:** permite actualizar el estado a «Registrado», «En proceso», «Derivado», «Atendido» o «Archivado».
- **Ordenamiento:** ordena los documentos por código mediante el algoritmo de ordenamiento burbuja.
- **Persistencia local:** guarda los registros en un archivo de texto y los carga al iniciar el programa.
- **Guardado al salir:** guarda automáticamente los datos cuando se elige la opción de salir.

## Tecnologías y conceptos

- **Lenguaje:** Python.
- **Interfaz:** menú interactivo en consola.
- **Estructura de datos:** matriz (lista bidimensional) de 100 filas y 7 columnas.
- **Persistencia:** archivo de texto `expedientes.txt`.
- **Conceptos de programación:** funciones, constantes, condicionales, ciclos, validación de entradas, búsqueda lineal, ordenamiento burbuja y manejo básico de excepciones.

## Requisitos

- Python 3 instalado.
- Una terminal o consola para ejecutar el programa.

No se requieren bibliotecas externas; el programa utiliza funcionalidades incluidas en Python.

## Instalación y ejecución

1. Descarga o clona el repositorio.
2. Abre una terminal en la carpeta que contiene `mesa_partes_hospital.py`.
3. Ejecuta:

   ```bash
   python mesa_partes_hospital.py
   ```

   En algunos sistemas, puede ser necesario usar:

   ```bash
   python3 mesa_partes_hospital.py
   ```

4. Selecciona una opción del menú e introduce los datos solicitados.

## Menú principal

1. Registrar documento
2. Consultar documento
3. Listar documentos
4. Clasificar documento
5. Derivar documento
6. Actualizar seguimiento
7. Ordenar documentos por código
8. Guardar datos en archivo
9. Salir

## Estructura de los datos

Cada documento se almacena en una fila de la matriz, con estas columnas:

| Índice | Campo | Descripción |
|---:|---|---|
| 0 | Código | Identificador del documento; debe ser único. |
| 1 | Nombre | Nombre del solicitante. |
| 2 | Tipo | Tipo o categoría del documento. |
| 3 | Fecha | Fecha de recepción, solicitada como `dd/mm/aaaa`. |
| 4 | Área | Área de destino del documento. |
| 5 | Estado | Estado actual del expediente. |
| 6 | Asunto | Motivo o asunto del documento. |

La matriz admite hasta **100 documentos**. Los registros se guardan en `expedientes.txt` en la carpeta de ejecución. Si el archivo todavía no existe, el programa comienza con una matriz vacía.

## Limitaciones conocidas

- La capacidad está limitada a 100 documentos.
- Los datos se almacenan en un archivo de texto, no en una base de datos.
- La fecha se solicita como texto; el programa no valida que sea una fecha real.
- El formato de almacenamiento usa `|` como separador. Por ello, los campos no deberían contener ese carácter.
- El prototipo está pensado para ejecutarse localmente desde una consola; no incluye interfaz gráfica, usuarios, autenticación ni acceso multiusuario.

## Objetivo académico

Este proyecto sirve como práctica de Fundamentos de Programación. Su propósito es aplicar estructuras de datos bidimensionales, modularización mediante funciones, operaciones de búsqueda y ordenamiento, validación de datos y lectura/escritura de archivos.

## Licencia

No se especifica una licencia para este proyecto.
