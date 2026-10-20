# Reconstrucción del historial de Mesa de Partes Digital

Este paquete contiene 10 versiones incrementales del archivo `mesa_partes_hospital.py`.
Cada carpeta `version_XX` representa el estado del código que correspondería a un commit.

## Importante
Este historial es una reconstrucción didáctica basada en el código final, no un registro comprobado de cómo se desarrolló originalmente.

## Versiones
1. `chore: initialize hospital records project`
2. `feat: add document search and display functions`
3. `feat: implement document registration`
4. `feat: add document consultation and listing`
5. `feat: implement document classification`
6. `feat: add document routing functionality`
7. `feat: implement document status tracking`
8. `feat: add document sorting by code`
9. `feat: persist records in text files`
10. `feat: integrate main menu and automatic saving`

## Cómo crear los commits manualmente (PowerShell)

1. Descomprime el paquete.
2. Abre PowerShell dentro de esta carpeta.
3. Crea una carpeta de repositorio aparte y entra en ella:
   ```powershell
   mkdir ..\mesa_partes_repo
   cd ..\mesa_partes_repo
   git init
   ```
4. Copia la versión 1 al repositorio, guarda el commit y repite con las demás versiones:
   ```powershell
   Copy-Item ..\mesa_partes_historial\version_01\mesa_partes_hospital.py .
   git add mesa_partes_hospital.py
   git commit -m "chore: initialize hospital records project"
   ```
   Para cada versión siguiente, repite `Copy-Item` cambiando `version_01` por `version_02`, etc., y usa el mensaje que aparece en el archivo `COMMIT.txt` de esa carpeta.
5. Comprueba el historial:
   ```powershell
   git log --oneline
   ```

## Consejo
No copies la versión 10 desde el inicio. Copia una versión, haz el commit, luego reemplaza el archivo por la siguiente versión y crea el siguiente commit. Así Git detectará los cambios incrementales.
